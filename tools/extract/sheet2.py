"""Contact sheet v2: one cell per detected candidate, magenta crosshair marking the
exact cluster centre so the digit under the crosshair is the answer."""
from PIL import Image, ImageDraw, ImageFont
import glob, json, os, sys

MAPS = 'F1_2026_Track_Maps'
OUT = '_work/out'
SHEET = os.path.join(OUT, 'sheets2')
os.makedirs(SHEET, exist_ok=True)

CELL = 240
PAD = 30
COLS = 4


def build(base, big=False):
    js = json.load(open(os.path.join(OUT, base.replace('.png', '.json'))))
    cands = js['cands']
    im = Image.open(os.path.join(MAPS, base)).convert('RGBA')
    W, H = im.size
    s = W / 1920.0
    half = int((78 if big else 40) * s)
    rows = (len(cands) + COLS - 1) // COLS
    sheet = Image.new('RGB', (COLS * (CELL + 10) + 10, rows * (CELL + PAD + 10) + 10), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.load_default(size=24)
    except TypeError:
        f = ImageFont.load_default()
    for i, c in enumerate(js['cands']):
        cx, cy = c['cx'], c['cy']
        x0, y0 = max(0, int(cx - half)), max(0, int(cy - half))
        x1, y1 = min(W, int(cx + half)), min(H, int(cy + half))
        crop = im.crop((x0, y0, x1, y1)).convert('RGB')
        cw, ch = crop.size
        canvas = Image.new('RGB', (cw + 40, ch + 40), (255, 255, 255))
        canvas.paste(crop, (20, 20))
        ox, oy = 20 + (cx - x0), 20 + (cy - y0)          # centre inside canvas
        k = CELL / float(canvas.size[0])
        canvas = canvas.resize((int(canvas.size[0] * k), int(canvas.size[1] * k)), Image.LANCZOS)
        gx, gy = 10 + (i % COLS) * (CELL + 10), 10 + (i // COLS) * (CELL + PAD + 10)
        sheet.paste(canvas, (gx, gy + PAD))
        mx, my = gx + ox * k, gy + PAD + oy * k
        d.line([mx - 18, my, mx + 18, my], fill=(255, 0, 255), width=3)
        d.line([mx, my - 18, mx, my + 18], fill=(255, 0, 255), width=3)
        d.rectangle([gx, gy + PAD, gx + canvas.size[0], gy + PAD + canvas.size[1]], outline=(0, 0, 0), width=2)
        d.text((gx + 4, gy + 2), '#%d %s' % (i, c['sector']), fill=(200, 0, 0), font=f)
    p = os.path.join(SHEET, base.replace('.png', '_sheet2.png'))
    sheet.save(p)
    print('%-42s n=%-3d %s' % (base, len(cands), p))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--big']
    big = '--big' in sys.argv
    files = args or [os.path.basename(x) for x in sorted(glob.glob(os.path.join(MAPS, '*.png')))]
    for a in files:
        build(a, big=big)
