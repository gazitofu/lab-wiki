"""Member and author name matching shared by render_lists.py and check_lab.py."""
import re


def exact_name(n):
    # brief-common §5.6-2: the member mark needs the identical name. Only posted marks, a leading Dr./Prof., an explicit
    # 'Family, Given', unicode hyphen characters and spacing runs are normalised; order, spacing between name parts,
    # hyphens and initials are not (Kyungtae Hong ≠ Kyung Tae Hong, Sol Kim ≠ S. Kim).
    n = re.sub('[*\u2020\u2021#+\u271d\u00b6\u00a7]', '', n or '').strip()
    n = re.sub(r'^(?:Dr|Prof)\.?\s+', '', n)
    n = re.sub('[\u2010\u2011\u2012\u2013\u2212]', '-', n)
    if n.count(',') == 1:
        fam, giv = (x.strip() for x in n.split(','))
        n = f'{giv} {fam}'
    return re.sub(r'\s+', ' ', n).strip()


def same_person(a, b):
    ea, eb = exact_name(a), exact_name(b)
    if not ea or not eb:
        return False
    # a lab page that writes the whole name in capitals (JAEKYUNG YI) differs from the author list only in case
    return ea == eb or ((ea.isupper() or eb.isupper()) and ea.casefold() == eb.casefold())
