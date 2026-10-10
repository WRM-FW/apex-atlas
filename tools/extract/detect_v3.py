"""Detect corner-number bubbles + sector attribution in the 2026 F1 track maps.

v3: size gates normalised by map resolution, plus disk-annulus and outer-rim
tests to separate real corner bubbles from checkerboard / label text.
"""
from PIL import Image
import numpy as np
from scipy import ndimage
import glob, json, os

MAPS = 'F1_2026_Track_Maps'
OUT = '_work/out'
os.makedirs(OUT, exist_ok=True)

STYLE_B = ('05_', '19_', '20_', '21_', '22_', '23_', '24_')
SECTOR_COLORS = {
    'A': {'S1': (229, 16, 115), 'S2': (255, 209, 0), 'S3': (64, 152, 217)},
    'B': {'S1': (255, 0, 0), 'S2': (255, 211, 0), 'S3': (0, 178, 227)},
}


def norm(v, s):
    return v / s


def label_clusters(rgb, alpha, style, s):
    """s = image width / 1920 (resolution scale)."""
    lum_min, lum_max = rgb.min(axis=2), rgb.max(axis=2)
    ink = ((lum_max < 90) if style == 'A' else (lum_min > 200)) & (alpha > 128)
    lab, n = ndimage.label(ink, structure=np.ones((3, 3), bool))
    glyphs = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        npix = int((lab[sl] == i).sum())
        nh, nw = h / s, w / s
        if not (6.0 <= nh <= 27 and 2 <= nw <= 46):
            continue
        fill = npix / float(h * w)
        if fill < 0.18 or fill > 0.93:
            continue
        glyphs.append(dict(x0=sl[1].start, y0=sl[0].start, x1=sl[1].stop, y1=sl[0].stop,
                           h=h, w=w, npix=npix, fill=round(fill, 2)))
    par = list(range(len(glyphs)))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for i, g in enumerate(glyphs):
        for j in range(i + 1, len(glyphs)):
            k = glyphs[j]
            dx = max(0, max(g['x0'], k['x0']) - min(g['x1'], k['x1']))
            dy = max(0, max(g['y0'], k['y0']) - min(g['y1'], k['y1']))
            tol = 0.62 * max(g['h'], k['h']) + 2 * s
            if dx <= tol and dy <= 3 * s and abs(g['h'] - k['h']) <= 8 * s:
                ra, rb = find(i), find(j)
                if ra != rb:
                    par[rb] = ra
    groups = {}
    for i in range(len(glyphs)):
        groups.setdefault(find(i), []).append(glyphs[i])
    out = []
    for mem in groups.values():
        if len(mem) > 3:
            continue
        x0 = min(m['x0'] for m in mem); y0 = min(m['y0'] for m in mem)
        x1 = max(m['x1'] for m in mem); y1 = max(m['y1'] for m in mem)
        w, h = x1 - x0, y1 - y0
        if h / s > 29 or w / s > 50:
            continue
        out.append(dict(cx=(x0 + x1) / 2, cy=(y0 + y1) / 2, w=w, h=h, ng=len(mem),
                        fills=[m['fill'] for m in mem]))
    return out


def circle_profile(rgb, cx, cy, r, style):
    h, w = rgb.shape[:2]
    disk = (rgb.min(axis=2) > 170) if style == 'A' else (rgb.max(axis=2) < 90)
    hits = tot = 0
    for k in range(36):
        th = 2 * np.pi * k / 36
        x = int(round(cx + np.cos(th) * r)); y = int(round(cy + np.sin(th) * r))
        if not (0 <= x < w and 0 <= y < h):
            continue
        tot += 1
        hits += bool(disk[y, x])
    return hits / max(tot, 1)


def sector_of(rgb, alpha, cx, cy, style, reach):
    pal = SECTOR_COLORS[style]
    h, w = alpha.shape
    x0, x1 = max(0, int(cx - reach)), min(w, int(cx + reach))
    y0, y1 = max(0, int(cy - reach)), min(h, int(cy + reach))
    sub = rgb[y0:y1, x0:x1].astype(int)
    best = (10 ** 9, None, None)
    for name, col in pal.items():
        dist = np.abs(sub - np.array(col)).max(axis=2)
        i = np.unravel_index(np.argmin(dist), dist.shape)
        if int(dist[i]) < best[0]:
            best = (int(dist[i]), name, (int(x0 + i[1]), int(y0 + i[0])))
    if best[0] > 40:
        return None, None, best[0]
    return best[1], best[2], best[0]


def analyze(path):
    base = os.path.basename(path)
    style = 'B' if base.startswith(STYLE_B) else 'A'
    im = Image.open(path).convert('RGBA')
    a = np.asarray(im).astype(np.int16)
    rgb, alpha = a[..., :3], a[..., 3]
    W, H = im.size
    s = W / 1920.0
    clusters = label_clusters(rgb, alpha, style, s)
    res = []
    for c in clusters:
        r = max(c['h'] * 1.75, c['w'] * 1.05) + 5 * s          # inner disk radius guess
        disk = circle_profile(rgb, c['cx'], c['cy'], r, style)
        rim = 1.0 - circle_profile(rgb, c['cx'], c['cy'], r * 1.22, style)
        sec, proj, dist = sector_of(rgb, alpha, c['cx'], c['cy'], style, int(140 * s))
        res.append(dict(cx=round(c['cx'], 1), cy=round(c['cy'], 1), w=round(c['w'], 1),
                        h=round(c['h'], 1), ng=c['ng'], fills=c['fills'],
                        disk=round(disk, 2), rim=round(rim, 2), sector=sec,
                        sector_px=proj, sector_dist=dist))
    return style, im.size, res


if __name__ == '__main__':
    for p in sorted(glob.glob(os.path.join(MAPS, '*.png'))):
        base = os.path.basename(p)
        style, size, res = analyze(p)
        json.dump(dict(file=base, style=style, size=list(size), cands=res),
                  open(os.path.join(OUT, base.replace('.png', '.json')), 'w'), indent=1)
        print('%-42s style=%s n=%d' % (base, style, len(res)))
