"""Merge hand-authored content with detected map geometry into the site's JSON data.

Emits:
  <site>/data/season.json          season overview, rules, archetypes, legend, glossary, index
  <site>/data/tracks/<id>.json     one file per track (specs + sectors + corner analysis + hotspots)
Checks: corner codes referenced by prose exist on the map; every corner is covered by a sector.
"""
import json, os, re, sys, importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'

CONTENT = {}
for mod in ('content_a', 'content_b', 'content_c', 'content_d'):
    CONTENT.update(importlib.import_module(mod).TRACKS)
S = importlib.import_module('content_season')


def parse_cs(cs):
    """'T1-T2' -> ['1','2'];  'T20A' -> ['20A'];  'T13-T15' -> ['13','14','15']"""
    codes = [c.strip().lstrip('Tt') for c in cs.split('-')]
    if len(codes) == 1:
        return [codes[0]]
    a, b = codes
    na, sa = int(re.match(r'\d+', a).group()), a[len(re.match(r'\d+', a).group()):]
    nb, sb = int(re.match(r'\d+', b).group()), b[len(re.match(r'\d+', b).group()):]
    if sa or sb:
        return [a, b]
    return [str(i) for i in range(na, nb + 1)]


os.makedirs(os.path.join(SITE, 'data', 'tracks'), exist_ok=True)
warnings, index = [], []

for tid, t in CONTENT.items():
    geo_path = os.path.join(SITE, 'data', 'corners', tid + '.json')
    if not os.path.exists(geo_path):
        warnings.append('%s: no geometry file' % tid)
        continue
    geo = json.load(open(geo_path))
    by_code = {c['n']: c for c in geo['corners']}
    codes = list(by_code)

    # sector membership by the guide's turn ranges
    for s in t['sectors']:
        lo, hi = s['rng']
        in_rng = lambda c: (c.isdigit() and lo <= int(c) <= hi) or (
            not c.isdigit() and lo <= int(re.match(r'\d+', c).group()) <= hi)
        s['corners'] = [c for c in codes if in_rng(c)]

    # corner-analysis groups
    groups = []
    for g in t['corners_analysis']:
        cs_codes = parse_cs(g['cs'])
        missing = [c for c in cs_codes if c not in by_code]
        if missing:
            warnings.append('%s: prose refers to corners absent from map: %s (%s)' % (tid, missing, g['cs']))
        sec = None
        for s in t['sectors']:
            if cs_codes[0] in s['corners']:
                sec = s['id']
        groups.append(dict(cs=g['cs'], codes=cs_codes, name=g['name'], text=g['text'], sector=sec))

    hot = []
    for c in geo['corners']:
        sec = next((s['id'] for s in t['sectors'] if c['n'] in s['corners']), None)
        grp = next((i for i, g in enumerate(groups) if c['n'] in g['codes']), None)
        if sec is None:
            warnings.append('%s: corner %s not covered by any sector range' % (tid, c['n']))
        hot.append(dict(n=c['n'], x=c['x'], y=c['y'], sector=sec, group=grp))

    total = len(codes)
    out = dict(
        id=tid, round=t['round'], name_zh=t['zh'], name_en=t['en'],
        circuit_zh=t['circuit_zh'], circuit_en=t['circuit_en'],
        country=t['country'], city=t['city'], flag=t['flag'], dates=t['dates'],
        sprint=t['sprint'], kind=t['kind'], archetype=t['archetype'],
        length_km=t['length'], laps=t['laps'],
        corners=dict(total=total, left=t['left'], right=t['right'],
                     guide_total=(15 if tid == 'madring' else total)),
        record=(None if not t['record'] else dict(time=t['record'], driver=t['record_who'], year=t['record_year'])),
        metrics=dict(downforce=t['downforce'], throttle_pct=t['throttle'],
                     braking=t['braking'], tyre_wear=t['tyre']),
        intro=t['intro'], sectors=t['sectors'], corner_groups=groups, hotspots=hot,
        setup_2026=t['setup'], watch=t['watch'],
        map=dict(file='assets/maps/%s.webp' % tid, thumb='assets/maps/%s_thumb.webp' % tid,
                 w=geo['w'], h=geo['h']),
    )
    json.dump(out, open(os.path.join(SITE, 'data', 'tracks', tid + '.json'), 'w', newline='\n'),
              ensure_ascii=False, indent=1)
    index.append(dict(id=tid, round=t['round'], name_zh=t['zh'], name_en=t['en'],
                      circuit_zh=t['circuit_zh'], circuit_en=t['circuit_en'], country=t['country'],
                      city=t['city'], flag=t['flag'], dates=t['dates'], sprint=t['sprint'],
                      length_km=t['length'], laps=t['laps'], corners_total=total,
                      archetype=t['archetype'], kind=t['kind'], thumb='assets/maps/%s_thumb.webp' % tid,
                      throttle_pct=t['throttle'], downforce=t['downforce'], braking=t['braking'],
                      intro_short=t['intro'].split('。')[0] + '。'))

index.sort(key=lambda r: (r['round'] == '—', r['round']))
season = dict(
    season=S.SEASON, rules=S.RULES, archetypes=S.ARCHETYPES, map_legend=S.MAP_LEGEND,
    watch_tips=S.WATCH_TIPS, glossary=S.GLOSSARY, data_sources=S.DATA_SOURCES, tracks=index,
)
json.dump(season, open(os.path.join(SITE, 'data', 'season.json'), 'w', newline='\n'),
          ensure_ascii=False, indent=1)

print('tracks written: %d' % len(index))
for w in warnings:
    print('  WARN', w)
if not warnings:
    print('  no consistency warnings')
