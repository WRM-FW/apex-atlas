"""Generate per-sector 'dim' layers so the site can spotlight one sector of a map.

For each track and sector we build a mask of that sector's coloured centreline
(dilated to road width) plus its corner bubbles, then export an overlay image
that is transparent there and dark everywhere else.  The site simply stacks it.
"""
from PIL import Image, ImageDraw
import numpy as np
from scipy import ndimage
import json, os, sys

SRC = 'F1_2026_Track_Maps'
SITE = sys.argv[1] if len(sys.argv) > 1 else 'apex-atlas'
W_OUT = 1600
ALPHA = 170

PAL = {
    'A': {'S1': (229, 16, 115), 'S2': (255, 209, 0), 'S3': (64, 152, 217)},
    'B': {'S1': (255, 0, 0), 'S2': (255, 211, 0), 'S3': (0, 178, 227)},
}
STYLE_B = ('05_', '19_', '20_', '21_', '22_', '23_', '24_')

os.makedirs(os.path.join(SITE, 'assets', 'dim'), exist_ok=True)
geo = json.load(open(os.path.join('_work', 'out', 'manifest.json')))
labels = json.load(open(os.path.join('_work', 'out', 'labels.json')))

for slug, meta in geo.items():
    fname = meta['file']
    tpath = os.path.join(SITE, 'data', 'tracks', slug + '.json')
    if not os.path.exists(tpath):
        print('skip (no track json):', slug)
        continue
    t = json.load(open(tpath))
    style = 'B' if fname.startswith(STYLE_B) else 'A'
    im = Image.open(os.path.join(SRC, fname)).convert('RGBA')
    W, H = im.size
    s = W_OUT / float(W)
    im = im.resize((W_OUT, int(H * s)), Image.LANCZOS)
    a = np.asarray(im)
    rgb = a[..., :3].astype(int)
    h_out, w_out = rgb.shape[:2]

    # road width scales with the *output* resolution (maps share one design ratio)
    rad = max(8, int(round(27 * (W_OUT / 1920.0))))
    yy, xx = np.mgrid[-rad:rad + 1, -rad:rad + 1]
    disk = (xx ** 2 + yy ** 2) <= rad ** 2

    for sec in ('S1', 'S2', 'S3'):
        col = np.array(PAL[style][sec])
        m = (np.abs(rgb - col).max(axis=2) <= 45)
        # drop anti-alias speckles before dilating, otherwise they bloom into blobs
        lab, n = ndimage.label(m)
        if n:
            sizes = ndimage.sum(m, lab, np.arange(1, n + 1))
            keep_ids = np.flatnonzero(sizes >= 60) + 1
            m = np.isin(lab, keep_ids)
        m = ndimage.binary_dilation(m, structure=disk)
        # keep this sector's corner bubbles visible
        ov = Image.new('L', (w_out, h_out), 0)
        d = ImageDraw.Draw(ov)
        for h in t['hotspots']:
            if h['sector'] != sec:
                continue
            x, y = h['x'] / 100.0 * w_out, h['y'] / 100.0 * h_out
            r = 32 * (W_OUT / 1920.0)
            d.ellipse([x - r, y - r, x + r, y + r], fill=255)
        keep = m | (np.asarray(ov) > 128)
        layer = np.zeros((h_out, w_out, 4), np.uint8)
        layer[..., 0] = 13
        layer[..., 1] = 13
        layer[..., 2] = 20
        layer[..., 3] = np.where(keep, 0, ALPHA)
        Image.fromarray(layer, 'RGBA').save(
            os.path.join(SITE, 'assets', 'dim', '%s_%s.webp' % (slug, sec)),
            quality=82, method=6)
    print('%-14s ok  dilate_radius=%d  %dx%d' % (slug, rad, w_out, h_out))
