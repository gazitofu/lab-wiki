# Re-run meta.one (Crossref, then S2) for rows whose Crossref request did not succeed (crossref_raw_key is None) or for the ranks given.
# Keeps selection fields; applies the same title-ratio guard as fetch_meta.py. Never run while another job writes the same meta.json.
# Usage (inside batch folder): python3 ../tools/rerun_meta.py SLUG [rank ...]
import json, re, sys
from pathlib import Path
sys.path.insert(0, '.')
import meta
slug = sys.argv[1]; ranks = {int(x) for x in sys.argv[2:]}
sel = {c['rank']: c for c in json.loads(Path(f'{slug}-selection.json').read_text())['candidates']}
path = Path(f'{slug}-meta.json'); rows = json.loads(path.read_text())
for i, r in enumerate(rows):
    if (ranks and r['rank'] not in ranks) or (not ranks and r.get('crossref_raw_key')):
        continue
    c = sel[r['rank']]; link = c.get('doi_or_link') or ''
    m = re.search(r'(10\.\d{4,9}/[^\s"<>]+)', link)
    q = 'DOI:' + m.group(1).rstrip('.,;)') if m else c['title']
    try:
        new = meta.one(q)
    except Exception as e:
        print(slug, r['rank'], 'error', e); continue
    if not m and new.get('title_ratio') is not None and new['title_ratio'] < 0.9:
        new['match_warning'] = 'Crossref title match below 0.9; DOI/abstract not adopted'
        for k in ('doi', 'cr_abstract', 's2_abstract'):
            new.pop(k, None)
        new['abstract_source'] = None
    # descriptive fields come from the current selection (a rank may have been swapped to another paper); paper_page only if the title is unchanged
    keep = {k: c.get(k) for k in ('rank', 'tier', 'theme', 'title', 'year', 'venue', 'pi_role', 'pi_role_basis', 'why', 'doi_or_link')}
    keep.update(authors_posted=c.get('authors'), paper_page=r.get('paper_page') if r.get('title') == c.get('title') else None)
    if not new.get('abstract_source') and r.get('abstract_source') and r.get('title') == c.get('title'):
        print(slug, r['rank'], 'kept old row (new has no abstract)'); continue
    new.update({k: v for k, v in keep.items() if v is not None}); rows[i] = new
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    print(slug, r['rank'], new.get('crossref_raw_key') is not None, new.get('doi'), new.get('abstract_source'), new.get('title_ratio'))
