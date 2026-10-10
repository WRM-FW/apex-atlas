"""Audit overlay v2: draw a numbered badge on every detected candidate, and dump a
coordinate table so readings can be cross-checked."""
from PIL import Image, ImageDraw, ImageFont
import json, os, sys

OUT = '_work/out'
VIEW = os.path.join(OUT, 'audit')
os.makedirs(VIEW, exist_ok=True)


def build(base, max_w=1760):
    js = json.load(open(os.path.join(OUT, base.replace('.png', '.json'))))
    im = Image.open(os.path.join('F1_2026_Track_Maps', base)).convert('RGBA')
    W, H = im.size
    s = max_w / W
    im = im.resize((max_w, int(H * s)))
    bg = Image.new('RGB', im.size, (255, 255, 255))
    bg.paste(im, (0, 0), im)
    d = ImageDraw.Draw(bg)
    try:
        f = ImageFont.load_default(size=17)
    except TypeError:
        f = ImageFont.load_default()
    rows = []
    for i, c in enumerate(js['cands']):
        x, y = c['cx'] * s, c['cy'] * s
        bx, by = x + 26, y - 26                     # badge position, up-right of centre
        d.line([x, y, bx, by], fill=(0, 120, 255), width=2)
        d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(0, 120, 255))
        r = 15
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=(255, 255, 0), outline=(200, 0, 0), width=2)
        t = str(i)
        d.text((bx - 8 * len(t), by - 8), t, fill=(180, 0, 0), font=f)
        rows.append('#%d  (%.0f, %.0f)  sector=%s' % (i, c['cx'], c['cy'], c['sector']))
    p = os.path.join(VIEW, base.replace('.png', '_audit.jpg'))
    bg.save(p, quality=90)
    open(os.path.join(VIEW, base.replace('.png', '_cands.txt')), 'w').write('\n'.join(rows))
    print('%-42s n=%d -> %s' % (base, len(js['cands']), p))


if __name__ == '__main__':
    import glob
    files = sys.argv[1:] or [os.path.basename(x) for x in sorted(glob.glob('F1_2026_Track_Maps/*.png'))]
    for a in files:
        build(a)
