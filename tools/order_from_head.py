# Print the --order string recovered from {slug}.head.md's representative-paper table: the DOI of each row,
# or r<meta rank> (matched by title in {slug}-meta.json) for rows without a DOI link.
# Usage (inside a batch folder): python3 ../tools/order_from_head.py SLUG
import json, re, sys
from pathlib import Path
slug = sys.argv[1]
meta = json.loads(Path(f'{slug}-meta.json').read_text())
norm = lambda s: re.sub(r'[^a-z0-9]', '', (s or '').lower())
rows = re.findall(r'^\| (\d+) \| \d{4} \| (.*?) \|', Path(f'{slug}.head.md').read_text(), re.M)
out = []
for n, cell in rows:
    m = re.search(r'https://doi\.org/(10\.[^)\s]+)', cell)
    if m:
        out.append(m.group(1)); continue
    title = norm(re.sub(r'^\[|\]\(.*$', '', cell.split(' · ')[0]))
    hit = [r['rank'] for r in meta if title and title in norm(r.get('title')) or norm(r.get('title')) and norm(r.get('title')) in title]
    if len(hit) != 1:
        sys.exit(f'row {n}: no unique meta match for {cell[:60]!r} -> {hit}')
    out.append(f'r{hit[0]}')
print(','.join(out))
