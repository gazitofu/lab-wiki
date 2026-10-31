# Semantic Scholar title search via fetch.py (robots, spacing). Usage: python3 s2search.py OUT.json "title" ...
import json, sys, urllib.parse, difflib, re
from pathlib import Path
from meta import get_json, norm
out = Path(sys.argv[1]); rows = json.loads(out.read_text()) if out.exists() else []
for q in sys.argv[2:]:
    d, rec = get_json('https://api.semanticscholar.org/graph/v1/paper/search?limit=3&fields=title,abstract,year,venue,externalIds,authors&query=' + urllib.parse.quote(q))
    row = dict(query=q, s2_raw_key=rec.get('raw_key'), s2_result=rec.get('result'), s2_status=rec.get('http_status'))
    if d and d.get('data'):
        best = max(d['data'], key=lambda it: difflib.SequenceMatcher(None, norm(q), norm(it.get('title'))).ratio())
        row.update(s2_title=best.get('title'), title_ratio=round(difflib.SequenceMatcher(None, norm(q), norm(best.get('title'))).ratio(), 3), s2_abstract=best.get('abstract'), year=best.get('year'), venue=best.get('venue'), ids=best.get('externalIds'), authors=[a.get('name') for a in best.get('authors', [])])
    rows.append(row); out.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
for r in rows: print(r.get('title_ratio'), r.get('s2_status'), bool(r.get('s2_abstract')), (r.get('s2_title') or r['query'])[:80])
