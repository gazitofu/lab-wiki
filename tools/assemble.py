#!/usr/bin/env python3
"""head + tail(마커 치환) + fn → wiki/kaist/{slug}.md

사용: python3 ../tools/assemble.py SLUG
tail 안의 <!--MEMBERS--> <!--ALUMNI--> <!--PAPERS--> <!--PATENTS--> <!--PROJECTS--> <!--NEWS--> <!--AWARDS-->
마커를 {slug}.lists.md의 같은 구역으로 바꾼다. lists.md 첫 구역(마커 전)이 MEMBERS다.
"""
import re, sys, pathlib
from inst import INSTS, detect

slug = sys.argv[1]
lists = pathlib.Path(f'{slug}.lists.md').read_text()
parts = re.split(r'^<!--([A-Z]+)-->\s*$', lists, flags=re.M)
sec = {'MEMBERS': parts[0].strip()}
for i in range(1, len(parts), 2):
    sec[parts[i]] = parts[i + 1].strip()
tail = pathlib.Path(f'{slug}.tail.md').read_text()
for k, v in sec.items():
    tail = tail.replace(f'<!--{k}-->', v)
left = re.findall(r'<!--[A-Z]+-->', tail)
if left:
    sys.exit(f'치환 안 된 마커: {left}')
head = pathlib.Path(f'{slug}.head.md').read_text().rstrip()
fn = pathlib.Path(f'{slug}.fn.md').read_text().strip()
out = pathlib.Path(f"{INSTS[detect()]['wiki']}/{slug}.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(head + '\n\n' + tail.strip() + '\n' + fn + '\n')
print(out)
