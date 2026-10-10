"""Validate the transcribed corner labels: completeness + spatial continuity."""
import json, os, math

OUT = '_work/out'
labels = json.load(open(os.path.join(OUT, 'labels.json')))
PDF_N = {'01': 14, '02': 16, '03': 18, '04': 15, '06': 19, '07': 14, '08': 19, '09': 14,
         '10': 10, '11': 18, '12': 19, '13': 14, '14': 14, '15': 11, '16': 20, '17': 20,
         '18': 19, '19': 20, '20': 17, '21': 15, '22': 17, '23': 16, '24': 16}

bad = 0
for base in sorted(labels):
    js = json.load(open(os.path.join(OUT, base.replace('.png', '.json'))))
    cands = js['cands']
    W, H = js['size']
    lab = labels[base]
    assigned = {}
    for k, v in lab.items():
        c = cands[int(k)]
        assigned[str(v)] = (c['cx'], c['cy'])
    plain = sorted(int(v) for v in assigned if str(v).isdigit())
    suffix = sorted(v for v in assigned if not str(v).isdigit())
    n = len(plain)
    problems = []
    if plain != list(range(1, n + 1)):
        missing = sorted(set(range(1, n + 1)) - set(plain))
        problems.append('NOT-CONTIGUOUS missing=%s dup=%s' % (missing, sorted(set(x for x in plain if plain.count(x) > 1))))
    # spatial continuity along the numbering
    diag = math.hypot(W, H)
    jumps = []
    for i in range(1, n):
        a, b = assigned.get(str(i)), assigned.get(str(i + 1))
        if a and b:
            d = math.hypot(a[0] - b[0], a[1] - b[1]) / diag
            if d > 0.22:
                jumps.append('T%d->T%d %.0f%%' % (i, i + 1, d * 100))
    key = base[:2]
    exp = PDF_N.get(key)
    tag = 'pdf=%s map=%d%s' % (exp, n, ('+' + ','.join(suffix)) if suffix else '')
    if problems or jumps:
        bad += 1
        print('!! %-40s %s  %s %s' % (base, tag, ';'.join(problems), ';'.join(jumps)))
    else:
        flag = '' if (exp is None or exp == n) else '   <-- differs from guide'
        print('ok %-40s %s%s' % (base, tag, flag))
print('\ntracks with issues: %d' % bad)
