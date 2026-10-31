# Fetch metadata/abstracts for {slug}-selection.json candidates via meta.one (Crossref, then Semantic Scholar only if no Crossref abstract).
# Usage: python3 fetch_meta.py SLUG [SLUG ...]  -> writes {slug}-meta.json (one row per candidate, with rank/tier/theme/why and match quality)
import json, re, sys
from pathlib import Path
import meta
# census-11 visualai: CS venues ('CVPR 2024', 'NeurIPS 2025', "CHI EA '24") are conferences too, so the journal-lab guard below must not zero them
# snu-05 icsl: abbreviated venue names ('IEEE Symp. VLSI Circuits Dig.', 'Conf.', 'Dig.') are conferences too
CONF = re.compile(r"(?i)proc|conference|symposium|symp\.|conf\.|dig\.|\bdigest\b|workshop|meeting|congress|\b(?:CVPR|ICCV|ECCV|NeurIPS|NIPS|ICLR|ICML|AAAI|IJCAI|SIGGRAPH|CHI|UIST|CSCW|ISMAR|VRST|ICRA|IROS|CoRL|RSS|ACL|EMNLP|NAACL|KDD|WACV|3DV|BMVC|MICCAI|ITSC|ICASSP|INTERSPEECH)\b|^[A-Z][A-Za-z0-9&-]{1,15}(?: [A-Z][A-Za-z]{1,10})?\s*'?\d{2,4}$")
for slug in sys.argv[1:]:
    sel = json.loads(Path(f'{slug}-selection.json').read_text())
    out = []
    for c in sel['candidates']:
        link = c.get('doi_or_link') or ''
        m = re.search(r'(10\.\d{4,9}/[^\s"<>]+)', link)
        q = 'DOI:' + m.group(1).rstrip('.,;)') if m else c['title']
        try:
            row = meta.one(q)
        except Exception as e:
            row = dict(query=q, error=f'{type(e).__name__}: {e}'[:200])
        row.update({k: c.get(k) for k in ('rank', 'tier', 'theme', 'title', 'year', 'venue', 'pi_role', 'pi_role_basis', 'why', 'doi_or_link')}); row['authors_posted'] = c.get('authors')
        if not m and row.get('type') == 'proceedings-article' and not CONF.search(c.get('venue') or ''):
            # a conference abstract with the same title (CLEO, Quantum 2.0, IEEE BCI) can outrank the journal paper the lab lists
            row['title_ratio'] = 0.0
        if not m and row.get('title_ratio') is not None and row['title_ratio'] < 0.9:
            row['match_warning'] = 'Crossref title match below 0.9; DOI/abstract not adopted'
            for k in ('doi', 'cr_abstract', 's2_abstract', 'authors', 'cr_title', 'container', 'volume', 'issue', 'page', 'published_online', 'published_print', 'type', 'is_referenced_by'):  # Crossref matched another work: keep none of its fields
                row.pop(k, None)
            row['abstract_source'] = None
        if not row.get('abstract_source') and link.startswith('http') and not m:
            # no DOI and no abstract: read the linked paper page (lab/venue page) so the writer can quote its posted abstract
            meta.fetch.fetch_one(link)
            rec = meta.last_log()
            row['paper_page'] = dict(url=link, result=rec.get('result'), raw_key=rec.get('raw_key'))
        out.append(row)
        Path(f'{slug}-meta.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    prim = [r for r in out if r.get('tier') == 'primary']
    print(slug, 'primary with abstract', sum(1 for r in prim if r.get('abstract_source')), '/', len(prim), '| all', sum(1 for r in out if r.get('abstract_source')), '/', len(out))
