# Restore Crossref author lists in {slug}-meta.json rows whose 'authors' was overwritten by the lab string (fetch_meta bug, 2026-10-19).
import json, sys
from pathlib import Path
RAW = Path(sys.argv[1]); slugs = sys.argv[2:]
for slug in slugs:
    p = Path(f'{slug}-meta.json'); rows = json.loads(p.read_text()); n = 0
    for r in rows:
        if isinstance(r.get('authors'), str):
            r['authors_posted'] = r['authors']; r['authors'] = []
            k = r.get('crossref_raw_key')
            if k and (RAW / f'{k}.raw').exists():
                d = json.loads((RAW / f'{k}.raw').read_bytes())
                m = d['message']
                if 'items' in m:
                    items = m['items']; doi = (r.get('doi') or '').lower()
                    m = next((it for it in items if (it.get('DOI') or '').lower() == doi), None) or {}
                r['authors'] = [' '.join(x for x in [a.get('given'), a.get('family')] if x) for a in m.get('author', [])]
                n += 1
    p.write_text(json.dumps(rows, ensure_ascii=False, indent=1)); print(slug, 'restored', n)
