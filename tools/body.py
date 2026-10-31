# Print the main content of a fetched page: drop short lines repeated on the page (menus) and image-only lines.
# Usage: python3 body.py RAWDIR RAWKEY [start] [count]
import sys, collections
from pathlib import Path
raw, key = Path(sys.argv[1]), sys.argv[2]
start = int(sys.argv[3]) if len(sys.argv) > 3 else 0
count = int(sys.argv[4]) if len(sys.argv) > 4 else 400
lines = [l.strip() for l in (raw / f'{key}.txt').read_text().splitlines() if l.strip()]
c = collections.Counter(lines)
out = [l for l in lines if not (c[l] > 1 and len(l) < 45) and not (l.startswith('[img:') and l.endswith(']'))]
print('\n'.join(out[start:start + count]))
