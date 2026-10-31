# Extract a posted abstract from already-fetched paper pages (paper_page.raw_key) for rows still without an abstract.
# Heuristic: text after a line that is exactly 'Abstract'/'ABSTRACT'/'Abstract:' until the next short heading-like line; or arXiv 'Abstract:' blockquote.
# Usage (inside batch folder): python3 ../tools/page_abstract.py RAWDIR SLUG [SLUG ...]   -> prints candidates; adopt with --write
import json, re, sys
from pathlib import Path
RAW = Path(sys.argv[1]); args = sys.argv[2:]; write = '--write' in args; slugs = [a for a in args if a != '--write']
STOP = re.compile(r'^(Method|Methods|Overview|Introduction|Results?|Video|BibTeX|Citation|Paper|Code|Acknowledg|Pipeline|Approach|Framework|Qualitative|Quantitative|Comparison|Experiments?|Contribution|Downloads?|Submission history|Comments:|Subjects:|Cite as:)\b', re.I)
for slug in slugs:
    p = Path(f'{slug}-meta.json'); rows = json.loads(p.read_text())
    for r in rows:
        pp = r.get('paper_page') or {}
        if r.get('abstract_source') or not pp.get('raw_key'):
            continue
        lines = [l.strip() for l in (RAW / f"{pp['raw_key']}.txt").read_text().splitlines() if l.strip()]
        ab = None
        for i, l in enumerate(lines):
            m = re.match(r'^(abstract|초록)\s*:?\s*(.*)$', l, re.I)
            if m:
                buf = [m.group(2)] if m.group(2) else []
                for l2 in lines[i + 1:]:
                    if STOP.match(l2) or (len(l2) < 40 and buf and not l2.endswith(('.', ','))):
                        break
                    buf.append(l2)
                    if sum(len(x) for x in buf) > 3000: break
                cand = ' '.join(buf).strip()
                if len(cand) > 300:
                    ab = cand; break
        print(slug, r['rank'], r.get('tier'), 'len', len(ab or ''), (ab or '')[:160])
        if write and ab:
            r['page_abstract'] = ab; r['abstract_source'] = 'paper-page'
    if write:
        p.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
