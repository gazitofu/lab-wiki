# -*- coding: utf-8 -*-
"""Check Lab-wiki tag vocabulary, trends, and page annotations (stdlib only)."""

import argparse
from inst import detect, gloss_key
from collections import Counter, defaultdict
import json
from pathlib import Path
import re


ID = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
ITEM = re.compile(r"^(?P<name>[^\[\],]+?)(?P<fns>(?:\[\^[A-Za-z0-9_-]+\])+)$")
FN = re.compile(r"\[\^([A-Za-z0-9_-]+)\]")
DEF = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:", re.M)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


class JsonFile:
    """Keep JSON value locations so diagnostics refer to the actual input line."""

    def __init__(self, path, checker, optional=False):
        self.path = path
        self.locations = {(): 1}
        self.data = {}
        try:
            self.text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            checker.issue(optional, path, 1, "missing_file", "파일 없음")
            return
        except (OSError, UnicodeError) as exc:
            checker.issue(False, path, 1, "read_file", str(exc))
            return
        try:
            data = json.loads(self.text)
        except json.JSONDecodeError as exc:
            checker.issue(False, path, exc.lineno, "json", exc.msg)
            return
        if not isinstance(data, dict):
            checker.issue(False, path, 1, "json_object", "최상위는 객체여야 함")
            return
        self.data = data
        decoder = json.JSONDecoder()

        def skip(i):
            while i < len(self.text) and self.text[i].isspace():
                i += 1
            return i

        def visit(i, keys):
            i = skip(i)
            self.locations[keys] = self.text.count("\n", 0, i) + 1
            if self.text[i] == "{":
                i = skip(i + 1)
                while self.text[i] != "}":
                    key, i = decoder.raw_decode(self.text, i)
                    i = visit(skip(i) + 1, keys + (key,))
                    i = skip(i)
                    if self.text[i] != ",":
                        break
                    i = skip(i + 1)
                return i + 1
            if self.text[i] == "[":
                i, n = skip(i + 1), 0
                while self.text[i] != "]":
                    i = skip(visit(i, keys + (n,)))
                    n += 1
                    if self.text[i] != ",":
                        break
                    i = skip(i + 1)
                return i + 1
            return decoder.raw_decode(self.text, i)[1]

        visit(0, ())

    def line(self, keys):
        while keys not in self.locations:
            keys = keys[:-1]
        return self.locations[keys]


class Checker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.fields = {}
        self.tags = {}
        self.names = {}
        self.aliases = defaultdict(list)
        self.labs = {}
        self.with_tags = 0
        self.without_tags = 0

    def issue(self, warning, path, line, code, reason):
        target = self.warnings if warning else self.errors
        target.append({"file": str(path), "line": line, "code": code, "reason": reason})

    def at(self, source, keys, code, reason, warning=False):
        self.issue(warning, source.path, source.line(keys), code, reason)

    def array(self, source, obj, key, keys):
        value = obj.get(key, [])
        if not isinstance(value, list):
            self.at(source, keys + (key,), "array", f"{key}는 배열이어야 함")
            return []
        return value

    def vocabulary(self, path):
        src = JsonFile(path, self)
        for n, line in enumerate(getattr(src, "text", "").splitlines(), 1):
            if "\u2014" in line:
                self.issue(False, path, n, "em_dash", "U+2014 줄표 금지")
        for key in ("fields", "tags"):
            if key not in src.data:
                self.at(src, (), "required_key", f"최상위 {key} 필수")
        for i, field in enumerate(self.array(src, src.data, "fields", ())):
            keys = ("fields", i)
            if not isinstance(field, dict):
                self.at(src, keys, "field_object", "field는 객체여야 함")
                continue
            fid = field.get("id")
            if not nonempty(fid):
                self.at(src, keys + ("id",), "field_id", "field id가 비어 있음")
            elif fid in self.fields:
                self.at(src, keys + ("id",), "field_duplicate", f"field id 중복: {fid}")
            else:
                self.fields[fid] = field
            if not nonempty(field.get("name_ko")):
                self.at(src, keys + ("name_ko",), "field_name", "field name_ko가 비어 있음")

        entries = []
        owners = defaultdict(set)
        seen_ids, seen_names = set(), set()
        for i, tag in enumerate(self.array(src, src.data, "tags", ())):
            keys = ("tags", i)
            if not isinstance(tag, dict):
                self.at(src, keys, "tag_object", "tag는 객체여야 함")
                continue
            entries.append((i, tag))
            tid, name = tag.get("id"), tag.get("name_ko")
            if not isinstance(tid, str) or not ID.fullmatch(tid):
                self.at(src, keys + ("id",), "tag_id", f"tag id 형식 오류: {tid}")
            if isinstance(tid, str):
                if tid in seen_ids:
                    self.at(src, keys + ("id",), "tag_duplicate", f"tag id 중복: {tid}")
                seen_ids.add(tid)
                self.tags.setdefault(tid, tag)
            if not nonempty(name):
                self.at(src, keys + ("name_ko",), "tag_name", "tag name_ko가 비어 있음")
            elif name in seen_names:
                self.at(src, keys + ("name_ko",), "name_duplicate", f"name_ko 중복: {name}")
            else:
                seen_names.add(name)
                self.names[name] = tag
            if isinstance(name, str) and any(c in name for c in ",[]"):
                self.at(src, keys + ("name_ko",), "name_punctuation", "name_ko에 쉼표 또는 대괄호 금지")
            for key in ("name_ko", "name_en"):
                if nonempty(tag.get(key)):
                    owners[tag[key].casefold()].add(i)
            aliases = self.array(src, tag, "aliases", keys)
            for alias in aliases:
                if nonempty(alias):
                    owners[alias.casefold()].add(i)

        for i, tag in entries:
            keys = ("tags", i)
            tid = tag.get("id")
            if tag.get("axis") not in ("method", "object", "application"):
                self.at(src, keys + ("axis",), "axis", "axis는 method/object/application이어야 함")
            if tag.get("status") not in ("active", "deprecated"):
                self.at(src, keys + ("status",), "status", "status는 active/deprecated이어야 함")
            fields = self.array(src, tag, "fields", keys)
            if not fields:
                self.at(src, keys + ("fields",), "tag_fields_empty", "tag fields가 1개 이상 필요")
            for j, fid in enumerate(fields):
                if not isinstance(fid, str) or fid not in self.fields:
                    self.at(src, keys + ("fields", j), "tag_field", f"없는 field id: {fid}")
            for j, related in enumerate(self.array(src, tag, "related", keys)):
                if not isinstance(related, str) or related not in self.tags:
                    self.at(src, keys + ("related", j), "related_missing", f"없는 related id: {related}")
                elif related == tid:
                    self.at(src, keys + ("related", j), "related_self", "related에 자기 자신 금지")
            merged = tag.get("merged_into")
            if tag.get("status") == "active" and ("merged_into" not in tag or merged is not None):
                self.at(src, keys + ("merged_into",), "active_merge", "active의 merged_into는 null이어야 함")
            if tag.get("status") == "deprecated":
                dest = self.tags.get(merged) if isinstance(merged, str) else None
                if not dest or dest.get("status") != "active":
                    self.at(src, keys + ("merged_into",), "deprecated_merge", "deprecated의 merged_into는 active tag id여야 함")
            if not nonempty(tag.get("definition")):
                self.at(src, keys + ("definition",), "definition", "definition이 비어 있음")
            seen = set()
            own_names = {tag[k].casefold() for k in ("name_ko", "name_en") if nonempty(tag.get(k))}
            for j, alias in enumerate(self.array(src, tag, "aliases", keys)):
                where = keys + ("aliases", j)
                if not nonempty(alias):
                    self.at(src, where, "alias_string", "별칭은 비어 있지 않은 문자열이어야 함")
                    continue
                folded = alias.casefold()
                if folded in seen:
                    self.at(src, where, "alias_duplicate", f"같은 태그 안 별칭 중복: {alias}")
                seen.add(folded)
                if owners[folded] - {i}:
                    self.at(src, where, "alias_collision", f"다른 태그의 이름 또는 별칭과 충돌: {alias}")
                if folded in own_names:
                    self.at(src, where, "alias_own_name", f"같은 태그 이름과 같은 별칭: {alias}", True)
                if len(re.sub(r"\s", "", alias)) <= 2:
                    self.at(src, where, "alias_short", f"공백 제외 2글자 이하 별칭: {alias}", True)
                self.aliases[folded].append(tag)

    def trends(self, path):
        src = JsonFile(path, self, optional=True)
        seen = set()
        for i, trend in enumerate(self.array(src, src.data, "trends", ())):
            keys = ("trends", i)
            if not isinstance(trend, dict):
                self.at(src, keys, "trend_object", "trend는 객체여야 함")
                continue
            tid = trend.get("id")
            if not isinstance(tid, str) or not ID.fullmatch(tid):
                self.at(src, keys + ("id",), "trend_id", f"trend id 형식 오류: {tid}")
            if isinstance(tid, str):
                if tid in seen:
                    self.at(src, keys + ("id",), "trend_duplicate", f"trend id 중복: {tid}")
                seen.add(tid)
            if not nonempty(trend.get("query")):
                self.at(src, keys + ("query",), "trend_query", "query가 비어 있음")
            tags = self.array(src, trend, "tags", keys)
            if not tags:
                self.at(src, keys + ("tags",), "trend_tags_empty", "trend tags가 1개 이상 필요")
            for j, tag_id in enumerate(tags):
                tag = self.tags.get(tag_id) if isinstance(tag_id, str) else None
                where = keys + ("tags", j)
                if tag is None:
                    self.at(src, where, "trend_tag", f"없는 tag id: {tag_id}")
                elif tag.get("status") == "deprecated":
                    self.at(src, where, "trend_deprecated", f"deprecated 태그 {tag_id}: merged_into={tag.get('merged_into')}", True)
            terms = [(keys + ("query",), trend.get("query"))]
            terms += [(keys + ("aliases", j), alias) for j, alias in enumerate(self.array(src, trend, "aliases", keys))]
            for where, term in terms:
                if not isinstance(term, str):
                    continue
                matches = [tag_id for tag_id, tag in self.tags.items()
                           if term.casefold() in {v.casefold() for v in
                               [tag.get("name_ko")] + (tag.get("aliases") if isinstance(tag.get("aliases"), list) else [])
                               if isinstance(v, str)}]
                if matches:
                    self.at(src, where, "trend_overlap", f"태그 이름과 트렌드가 겹침: {term} ({', '.join(matches)})", True)

    def page(self, path, require):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.issue(False, path, 1, "read_page", str(exc))
            return
        lines = text.splitlines()
        found = {key: [i for i, line in enumerate(lines) if line.startswith(f"- {key}:")]
                 for key in ("대분야", "태그")}
        lab = {"fields": [], "tags": []}
        self.labs[gloss_key('snu' if path.parent.name == 'snu' else 'kaist', path.stem)] = lab
        if not any(found.values()):
            self.without_tags += 1
            if require:
                self.issue(False, path, 1, "required_tags", "태그 없음 (--require)")
            return
        if found["태그"]:
            self.with_tags += 1
        else:
            self.without_tags += 1
        first_quote = next((i for i, line in enumerate(lines) if line.startswith("> ")), len(lines))
        first_list = next((i for i, line in enumerate(lines) if line.startswith("- ")), len(lines))
        end_list = first_list
        while end_list < len(lines):
            line = lines[end_list]
            if line.strip() and not line.startswith(("- ", " ", "\t")):
                break
            end_list += 1
        subject = next((i for i, line in enumerate(lines) if line.startswith("- 분야:")), None)
        for key, indices in found.items():
            if not indices:
                other = next(v[0] for v in found.values() if v)
                self.issue(False, path, other + 1, "paired_lines", f"대분야와 태그 줄은 함께 있어야 함: {key} 없음")
            for index in indices:
                if index != indices[0]:
                    self.issue(False, path, index + 1, "duplicate_line", f"{key} 줄은 최대 1개")
                if index >= first_quote:
                    self.issue(False, path, index + 1, "after_summary", f"{key} 줄은 첫 > 요약 앞이어야 함")
                if not first_list <= index < end_list:
                    self.issue(False, path, index + 1, "outside_first_list", f"{key} 줄은 첫 - 목록 안이어야 함")
                if subject is not None and index <= subject:
                    self.issue(False, path, index + 1, "before_subject", f"{key} 줄은 - 분야: 뒤여야 함")
                if not lines[index].startswith(f"- {key}: "):
                    self.issue(False, path, index + 1, "line_format", f"- {key}: 뒤에 공백 필요")
        if found["대분야"]:
            index = found["대분야"][0]
            values = lines[index].removeprefix("- 대분야: ").split(", ")
            lab["fields"] = values
            if not 1 <= len(values) <= 2:
                self.issue(False, path, index + 1, "field_count", "대분야는 1–2개여야 함")
            if len(set(values)) != len(values):
                self.issue(False, path, index + 1, "page_field_duplicate", "대분야 중복")
            valid_names = [f.get("name_ko") for f in self.fields.values()]
            for value in values:
                if value not in valid_names:
                    self.issue(False, path, index + 1, "page_field", f"없는 대분야 이름: {value}")
        if not found["태그"]:
            return
        index = found["태그"][0]
        items = lines[index].removeprefix("- 태그: ").split(", ")
        if len(items) > 8:
            self.issue(False, path, index + 1, "tag_count_max", f"태그 수 {len(items)}: 8개 초과")
        if len(items) < 3:
            self.issue(True, path, index + 1, "tag_count_min", f"태그 수 {len(items)}: 3개 미만")
        defined = set(DEF.findall(text))
        seen = set()
        for item in items:
            match = ITEM.fullmatch(item)
            if not match:
                self.issue(False, path, index + 1, "tag_item", f"태그 항목 형식 오류: {item}")
                continue
            name, fns = match["name"], FN.findall(match["fns"])
            if not 1 <= len(fns) <= 3:
                self.issue(False, path, index + 1, "fn_count", f"{name}: 각주는 1–3개여야 함")
            for fn in fns:
                if fn not in defined:
                    self.issue(False, path, index + 1, "fn_missing", f"{name}: 각주 정의 없음 [^{fn}]")
            tag = self.names.get(name)
            if tag is None:
                aliases = self.aliases.get(name.casefold(), [])
                reason = (f"별칭 {name}: 정식 이름 {', '.join(t['name_ko'] for t in aliases)} 사용"
                          if aliases else f"없는 태그 이름: {name}")
                self.issue(False, path, index + 1, "page_alias" if aliases else "page_tag", reason)
                continue
            if tag.get("status") != "active":
                target = self.tags.get(tag.get("merged_into"), {}) if isinstance(tag.get("merged_into"), str) else {}
                self.issue(False, path, index + 1, "page_deprecated", f"deprecated 태그 {name}: merged_into={tag.get('merged_into')}, 대상 이름 {target.get('name_ko', '없음')}")
                continue
            tid = tag.get("id")
            if not isinstance(tid, str) or tid not in self.tags:
                continue
            if tid in seen:
                self.issue(False, path, index + 1, "page_tag_duplicate", f"같은 태그 두 번 금지: {name}")
                continue
            seen.add(tid)
            lab["tags"].append({"id": tid, "name": name, "fns": fns,
                                "grade": "paper" if any(re.fullmatch(r"p\d+", fn) for fn in fns) else "intro"})

    def result(self):
        tags = {tid: {"labs": [], "paper": 0, "intro": 0} for tid in self.tags}
        for slug, lab in self.labs.items():
            for tag in lab["tags"]:
                tags[tag["id"]]["labs"].append(slug)
                tags[tag["id"]][tag["grade"]] += 1
        return {"labs": self.labs, "tags": tags, "errors": self.errors, "warnings": self.warnings}

    def output(self, result):
        for label, issues in (("오류", self.errors), ("경고", self.warnings)):
            for issue in issues:
                print(f"{issue['file']}:{issue['line']}: {label} [{issue['code']}] {issue['reason']}")
        counts = Counter({tid: len(t["labs"]) for tid, t in result["tags"].items()})
        ranked = sorted(counts, key=lambda tid: (-counts[tid], tid))
        def describe(ids):
            return ", ".join(f"{tid}({counts[tid]})" for tid in ids) or "없음"
        singles = sum(n == 1 for n in counts.values())
        ratio = singles / len(counts) * 100 if counts else 0.0
        print(f"문서 수 {len(self.labs)} | 태그 단 문서 수 {self.with_tags} | 태그 없음 {self.without_tags}")
        print(f"태그별 랩 수 상위 10: {describe(ranked[:10])}")
        print(f"랩 0곳 태그: {describe(tid for tid in ranked if counts[tid] == 0)}")
        print(f"1곳 태그 수 {singles}/{len(counts)} ({ratio:.2f}%, 전체 어휘 태그 기준)")
        print(f"10곳 이상 태그: {describe(tid for tid in ranked if counts[tid] >= 10)}")
        print(f"오류 {len(self.errors)} | 경고 {len(self.warnings)}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--vocab", type=Path)
    parser.add_argument("--trends", type=Path)
    parser.add_argument("--require", action="store_true")
    parser.add_argument("--json", type=Path)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("pages", nargs="*", type=Path)
    args = parser.parse_args(argv)
    checker = Checker()
    checker.vocabulary(args.vocab or args.repo / "wiki/tags.json")
    checker.trends(args.trends or args.repo / "wiki/trend-queries.json")
    pages = args.pages if args.pages else sorted(p for inst in (("kaist", "snu") if args.all else (detect(),))
                                                for p in (args.repo / "wiki" / inst).glob("*.md"))
    for page in sorted(set(pages)):
        if not page.name.endswith("-sources.md"):
            checker.page(page, args.require)
    result = checker.result()
    if args.json:
        try:
            args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            checker.issue(False, args.json, 1, "write_json", str(exc))
    checker.output(result)
    return 1 if checker.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
