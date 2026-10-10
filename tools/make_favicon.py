"""Generate the ApexAtlas favicon from the exact .brand-mark CSS spec.

Source of truth (css/app.css):
    width/height 26px; border-radius 50%
    background conic-gradient(from 210deg, #e51073, #ffd100, #4098d9, #e51073)
    box-shadow 0 0 0 2px #0d0d14, 0 0 0 3px rgba(247,244,241,.35)
    ::after inset 7px -> inner disc radius 6, colour #0d0d14

Radii in that 26px box (units = px): conic ring 0..13, ink gap 13..15,
light hairline 15..16, inner hole radius 6.  Both the SVG and the PNG are
produced from these same numbers, so the browser-tab icon and the in-page
mark cannot drift apart.

Outputs into <site>/assets: favicon.svg, favicon.png (64), apple-touch-icon.png (180)

Usage:  python tools/make_favicon.py [site-root]
"""
import math
import os
import sys

from PIL import Image

SITE = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = os.path.join(SITE, 'assets')
os.makedirs(OUT, exist_ok=True)

S1, S2, S3 = (229, 16, 115), (255, 209, 0), (64, 152, 217)
INK = (13, 13, 20)
PAPER = (247, 244, 241)
START_DEG = 210.0
HAIR_ALPHA = 89                                    # rgba(...,.35)

R_CONIC, R_INK, R_HAIR, R_HOLE = 13.0, 15.0, 16.0, 6.0


def conic_rgb(css_angle):
    """Colour of `conic-gradient(from 210deg, S1, S2, S3, S1)` at a CSS angle
    (degrees, clockwise from 12 o'clock)."""
    t = (((css_angle - START_DEG) % 360.0) / 360.0)
    segs = [(S1, S2), (S2, S3), (S3, S1)]
    i = min(int(t * 3), 2)
    f = t * 3 - i
    a, b = segs[i]
    return tuple(round(a[k] + (b[k] - a[k]) * f) for k in range(3))


def css_angle(dx, dy):
    return (math.degrees(math.atan2(dx, -dy)) + 360.0) % 360.0


def render(px, ss=4):
    """Antialiased raster of the mark at `px` logical pixels (transparent bg)."""
    n = px * ss
    scale = (R_HAIR * 2) / n                        # the mark spans the canvas
    c = (n - 1) / 2.0
    img = Image.new('RGBA', (n, n), (0, 0, 0, 0))
    pix = img.load()
    for y in range(n):
        for x in range(n):
            dx, dy = (x - c) * scale, (y - c) * scale
            r = math.hypot(dx, dy)
            if r > R_HAIR:
                continue
            if r <= R_HOLE:
                pix[x, y] = INK + (255,)             # inner disc
            elif R_CONIC < r <= R_INK:
                pix[x, y] = INK + (255,)             # ink gap ring
            elif R_INK < r <= R_HAIR:
                pix[x, y] = PAPER + (HAIR_ALPHA,)    # light hairline ring
            else:
                pix[x, y] = conic_rgb(css_angle(dx, dy)) + (255,)
    return img.resize((px, px), Image.LANCZOS)


def build_svg(size=64, wedges=180):
    """Vector twin: pie slices of the conic ring, then gap ring, hairline and hole."""
    k = size / (R_HAIR * 2)
    cx = cy = size / 2.0
    step = 360.0 / wedges

    def pt(r, css_angle):
        a = math.radians(css_angle)
        return '%.2f %.2f' % (cx + r * k * math.sin(a), cy - r * k * math.cos(a))

    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" width="%g" height="%g">'
             % (size, size, size, size),
             '<title>ApexAtlas</title>']

    for i in range(wedges):
        # draw each slice a touch wider on both sides so neighbours always
        # overlap; otherwise an antialiased seam shows at the shared edge
        a0 = START_DEG + i * step - 0.6
        a1 = START_DEG + (i + 1) * step + 0.6
        col = conic_rgb(START_DEG + (i + 0.5) * step)
        parts.append('<path fill="rgb(%d,%d,%d)" d="M%.2f %.2f L%s A%.2f %.2f 0 0 1 %s Z"/>' % (
            col[0], col[1], col[2], cx, cy, pt(R_CONIC, a0),
            R_CONIC * k, R_CONIC * k, pt(R_CONIC, a1)))

    parts.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="none" stroke="rgb(%d,%d,%d)" stroke-width="%.2f"/>'
                 % (cx, cy, (R_CONIC + R_INK) / 2 * k, INK[0], INK[1], INK[2], (R_INK - R_CONIC) * k))
    parts.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="none" stroke="rgba(%d,%d,%d,.35)" stroke-width="%.2f"/>'
                 % (cx, cy, (R_INK + R_HAIR) / 2 * k, PAPER[0], PAPER[1], PAPER[2], (R_HAIR - R_INK) * k))
    parts.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="rgb(%d,%d,%d)"/>'
                 % (cx, cy, R_HOLE * k, INK[0], INK[1], INK[2]))
    parts.append('</svg>')
    return ''.join(parts)


if __name__ == '__main__':
    svg = build_svg()
    with open(os.path.join(OUT, 'favicon.svg'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(svg)
    print('favicon.svg          %.1f KB' % (len(svg.encode()) / 1024))
    for name, px in (('favicon.png', 64), ('apple-touch-icon.png', 180)):
        path = os.path.join(OUT, name)
        render(px).save(path, optimize=True)
        print('%-20s %dx%d  %.1f KB' % (name, px, px, os.path.getsize(path) / 1024))
