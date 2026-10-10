"""Build the site's corner geometry (percentage coords) + optimised map images.

Outputs (into the site source tree, originals untouched):
  <site>/assets/maps/<id>.webp        detail map, 1600px wide
  <site>/assets/maps/<id>_thumb.webp  calendar thumbnail, 640px wide
  <site>/data/corners/<id>.json       geometry only (merged with prose later)
"""
from PIL import Image
import json, os, re, sys

SRC = 'F1_2026_Track_Maps'
OUT = '_work/out'
SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

# file -> canonical track id
SLUG = {
    '01_Australia_Melbourne.png': 'albert-park',
    '02_China_Shanghai.png': 'shanghai',
    '03_Japan_Suzuka.png': 'suzuka',
    '04_Bahrain_GP_Sepang_Malaysia.png': 'sepang',
    '05_Saudi_Arabia_Jeddah.png': 'jeddah',
    '06_USA_Miami.png': 'miami',
    '07_Canada_Montreal.png': 'montreal',
    '08_Monaco_MonteCarlo.png': 'monaco',
    '09_Spain_Barcelona_Catalunya.png': 'barcelona',
    '10_Austria_Spielberg.png': 'red-bull-ring',
    '11_GreatBritain_Silverstone.png': 'silverstone',
    '12_Belgium_Spa.png': 'spa',
    '13_Hungary_Hungaroring.png': 'hungaroring',
    '14_Netherlands_Zandvoort.png': 'zandvoort',
    '15_Italy_Monza.png': 'monza',
    '16_Spain_Madrid_Madring.png': 'madring',
    '17_Azerbaijan_Baku.png': 'baku',
    '18_Singapore.png': 'marina-bay',
    '19_USA_Austin_COTA.png': 'cota',
    '20_Mexico_MexicoCity.png': 'rodriguez',
    '21_Brazil_Interlagos.png': 'interlagos',
    '22_USA_LasVegas.png': 'las-vegas',
    '23_Qatar_Lusail.png': 'lusail',
    '24_AbuDhabi_YasMarina.png': 'yas-marina',
}

os.makedirs(os.path.join(SITE, 'assets', 'maps'), exist_ok=True)
os.makedirs(os.path.join(SITE, 'data', 'corners'), exist_ok=True)

labels = json.load(open(os.path.join(OUT, 'labels.json')))
manifest = {}

for fname, slug in SLUG.items():
    js = json.load(open(os.path.join(OUT, fname.replace('.png', '.json'))))
    W, H = js['size']
    lab = labels[fname]
    corners = []
    for k, v in lab.items():
        if v is None:
            continue
        c = js['cands'][int(k)]
        corners.append({
            'n': str(v),
            'num': int(v) if str(v).isdigit() else int(re.match(r'\d+', str(v)).group()),
            'sfx': '' if str(v).isdigit() else str(v)[len(re.match(r'\d+', str(v)).group()):],
            'x': round(c['cx'] / W * 100, 3),
            'y': round(c['cy'] / H * 100, 3),
        })
    corners.sort(key=lambda c: (c['num'], c['sfx']))
    json.dump({'id': slug, 'source': fname, 'w': W, 'h': H, 'corners': corners},
              open(os.path.join(SITE, 'data', 'corners', slug + '.json'), 'w'),
              ensure_ascii=False, indent=1)

    im = Image.open(os.path.join(SRC, fname)).convert('RGBA')
    for tag, width, q in (('', 1600, 90), ('_thumb', 640, 78)):
        r = im.copy()
        if r.width > width:
            r = r.resize((width, round(r.height * width / r.width)), Image.LANCZOS)
        r.save(os.path.join(SITE, 'assets', 'maps', '%s%s.webp' % (slug, tag)),
               quality=q, method=6)
    manifest[slug] = {'file': fname, 'corners': len(corners), 'aspect': round(H / W, 4)}
    print('%-14s %-42s corners=%-3d aspect=%.3f' % (slug, fname, len(corners), H / W))

json.dump(manifest, open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1)
print('\ntotal corners:', sum(m['corners'] for m in manifest.values()))
