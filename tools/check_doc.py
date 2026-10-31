# Static checks for a rewritten wiki page: footnote refs/defs 1:1, banned strings, markdown render leftovers.
import re, sys
import markdown
bad_words = ['—', '미수집', '미검증', 'kaist:', 'snu:', '확인하지 않았다', 'IF=', 'Impact Factor', 'acceptance rate', '[SCIE', '[SSCI', '[A&HCI', 'Q1,', 'Q2,', 'JCR', 'section_note', '이전 등록본', '_posted']
# process notes belong only on the -sources page (memory labwiki-body-no-process-notes)
body_only = ['옮기지 않았다', '읽히지 않', '채택률', '신상 소식', '뺐다', '넣지 않았다', 'Crossref에서', 'Google Scholar로']
for f in sys.argv[1:]:
    t = open(f).read()
    refs = set(re.findall(r'\[\^([A-Za-z0-9_-]+)\](?!:)', t)); defs = set(re.findall(r'^\[\^([A-Za-z0-9_-]+)\]:', t, re.M))
    h = markdown.markdown(t, extensions=['tables', 'footnotes'])
    words = bad_words + body_only if not f.endswith('-sources.md') else [w for w in bad_words if w != '확인하지 않았다']
    hits = [w for w in words if w in t] + re.findall(r'\bIF\s?\d[\d.]*', t) + re.findall(r'내부 수집 대장|details\.md|connections\.md', t) + re.findall(r'<(?!https?://)[A-Za-z/!][^>]*>', re.sub(r'`[^`\n]*`', '', t))  # build-v03 rejects raw HTML
    hits += [f'ctrl U+{ord(c):04X}' for c in sorted(set(re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', t)))]  # stray control bytes from scraped text
    hits += [a for a in re.findall(r'<a href="([^"]*)"', h) if not re.match(r'https?://|#|(?:\./)?(?:wiki/(?:kaist|snu)/)?[\w-]+\.md$', a)]  # build-v03 accepts only these link targets
    print(f.split('/')[-1], 'chars', len(t), '| missing defs', sorted(refs - defs), '| unused defs', sorted(defs - refs), '| leftover [^', h.count('[^'), '| banned', hits)
