"""Pre-publish checks for ApexAtlas (runs in CI and locally).

1. No root-absolute paths anywhere — GitHub Pages may serve the site from a
   sub-directory (username.github.io/repo/), where "/assets/..." would 404.
2. Every local file referenced by HTML/CSS/JS actually exists.
3. Every data/tracks/*.json is well formed and its hotspots stay inside the map.

Usage:  python tools/check_site.py [site-root]
"""
import json, os, re, sys, glob

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
TEXT_EXT = ('.html', '.css', '.js', '.json')
REF = re.compile(r'''(?:src|href)\s*=\s*["']([^"']+)["']|url\(\s*["']?([^"')]+)["']?\s*\)''')
errors, warnings = [], []


def is_local(ref):
    ref = ref.strip()
    return not (ref.startswith(('http:', 'https:', 'data:', 'mailto:', 'tel:', '#', 'blob:'))
                or ref in ('', 'about:blank'))


# ---- 1 + 2: scan source files for references ------------------------------
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '.github')]
    for fn in files:
        if not fn.endswith(TEXT_EXT):
            continue
        p = os.path.join(dirpath, fn)
        rel_dir = os.path.relpath(dirpath, ROOT)
        txt = open(p, encoding='utf-8').read()
        # JS builds most URLs at runtime from data, so there we only enforce the
        # absolute-path rule and leave existence checks to the data pass below.
        check_exists = fn.endswith(('.html', '.css'))
        for m in REF.finditer(txt):
            ref = (m.group(1) or m.group(2) or '').strip()
            if ref.startswith('/') and not ref.startswith('//'):
                errors.append('%s: root-absolute path "%s" breaks under a Pages sub-path' % (
                    os.path.relpath(p, ROOT), ref))
                continue
            if not is_local(ref) or not check_exists:
                continue
            target = ref.split('#')[0].split('?')[0]
            if not target:
                continue
            base = ROOT if rel_dir == '.' else os.path.join(ROOT, rel_dir)
            fp = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(fp):
                errors.append('%s: missing local file "%s"' % (os.path.relpath(p, ROOT), ref))

# ---- runtime-built paths (js builds these from data) -----------------------
for ref in ['assets/maps/', 'assets/dim/', 'data/tracks/', 'data/season.json', 'css/app.css', 'js/app.js']:
    if not os.path.exists(os.path.join(ROOT, ref.rstrip('/'))):
        errors.append('expected path not found: %s' % ref)

# ---- 3: validate track data ------------------------------------------------
season = json.load(open(os.path.join(ROOT, 'data', 'season.json'), encoding='utf-8'))
ids = [t['id'] for t in season['tracks']]
if len(ids) != len(set(ids)):
    errors.append('season.json has duplicate track ids')

total_corners = 0
for path in sorted(glob.glob(os.path.join(ROOT, 'data', 'tracks', '*.json'))):
    t = json.load(open(path, encoding='utf-8'))
    tid = t['id']
    if tid not in ids:
        errors.append('%s: not listed in season.json index' % tid)
    codes = [h['n'] for h in t['hotspots']]
    if len(codes) != len(set(codes)):
        errors.append('%s: duplicate hotspot codes' % tid)
    total_corners += len(codes)
    for h in t['hotspots']:
        if not (0 <= h['x'] <= 100 and 0 <= h['y'] <= 100):
            errors.append('%s: hotspot T%s outside the image (%.1f, %.1f)' % (tid, h['n'], h['x'], h['y']))
        if h['group'] is not None and not (0 <= h['group'] < len(t['corner_groups'])):
            errors.append('%s: hotspot T%s points at missing group %s' % (tid, h['n'], h['group']))
    for img in (t['map']['file'], t['map']['thumb']):
        if not os.path.exists(os.path.join(ROOT, img)):
            errors.append('%s: missing image %s' % (tid, img))
    for sec in ('S1', 'S2', 'S3'):
        dim = 'assets/dim/%s_%s.webp' % (tid, sec)
        if not os.path.exists(os.path.join(ROOT, dim)):
            warnings.append('%s: no sector layer %s (spotlight falls back)' % (tid, dim))
    nums = sorted({int(re.match(r'\d+', c).group()) for c in codes})
    if nums != list(range(1, max(nums) + 1)):
        warnings.append('%s: corner numbers are not contiguous 1..N (%s)' % (tid, nums))
    suffixed = [c for c in codes if not c.isdigit()]
    if suffixed:
        print('  note: %s has suffixed corners %s (kept as drawn on the map)' % (tid, suffixed))

print('tracks: %d | corners: %d | glossary: %d | rules: %d'
      % (len(ids), total_corners, len(season['glossary']), len(season['rules'])))
for w in warnings:
    print('  warn:', w)
if errors:
    for e in errors:
        print('  ERROR:', e)
    sys.exit(1)
print('OK: no absolute paths, all referenced files present, data consistent.')
