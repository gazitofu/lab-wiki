# Crossref title search restricted to journal articles (preprint DOIs such as PsyArXiv/SSRN/Research Square are never adopted).
# Usage: python3 cr_journal.py SLUG RANK [RANK ...] -> prints best journal-article match per rank (title ratio, DOI, container)
import json, sys, urllib.parse, difflib
from pathlib import Path
import meta
slug = sys.argv[1]; ranks = {int(x) for x in sys.argv[2:]}
sel = {c['rank']: c for c in json.loads(Path(f'{slug}-selection.json').read_text())['candidates']}
for r in sorted(ranks):
    c = sel[r]
    d, rec = meta.get_json('https://api.crossref.org/works?rows=5&filter=type:journal-article&query.bibliographic=' + urllib.parse.quote(c['title']))
    items = d['message']['items'] if d else []
    best = max(items, key=lambda it: difflib.SequenceMatcher(None, meta.norm(c['title']), meta.norm((it.get('title') or [''])[0])).ratio(), default=None)
    if best:
        ratio = difflib.SequenceMatcher(None, meta.norm(c['title']), meta.norm((best.get('title') or [''])[0])).ratio()
        print(slug, r, round(ratio, 3), best.get('DOI'), (best.get('container-title') or [''])[0], '|', c['venue'][:50])
    else:
        print(slug, r, 'no journal match', rec.get('http_status'))
