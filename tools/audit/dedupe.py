#!/usr/bin/env python3
"""Deduplicate PDFs (and their conversion folders) per the approved policy:
keep one copy per paper — prefer the copy with a conversion, then the
non-suffixed name, then the best-fit topic folder. Deletions are recorded in
DUPLICATES.md.

Run with --apply to execute; default is a dry-run that prints the action plan.
"""
import hashlib
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAPERS = REPO / "papers"
MD_ROOT = PAPERS / "Markdown files" / "Papers_Data"
APPLY = "--apply" in sys.argv

# topic dir -> its MD trees
TOPIC_MD = {
    "Academic": ["Academic/MD"],
    "Academic/01 Academic - Extended": ["Academic/01 Academic - Extended/MD"],
    "Articles": ["Articles/MD"],
    "Articles/01 Articles - Extended": ["Articles/01 Articles - Extended/MD"],
    "Mental Health": ["Mental Health/MD"],
    "Mental Health/01 Mental Health - Extended": ["Mental Health/01 Mental Health - Extended/MD"],
    "Remote Worker SNH": ["Remote Worker SNH/MD"],
    "Remote Workers": ["Remote Workers/MD"],
    "Remote Workers/01 Extended - Remote Workers": ["Remote Workers/01 Extended - Remote Workers/MD"],
}


def topic_of(pdf: Path) -> str:
    rel = pdf.relative_to(PAPERS)
    return str(rel.parent)


def conv_folder(pdf: Path) -> Path | None:
    t = topic_of(pdf)
    stem = pdf.name[:-4]  # strip .pdf
    for md in TOPIC_MD.get(t, []):
        cand = MD_ROOT / md / stem
        if cand.is_dir():
            return cand
    return None


def nk(n):
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\.pdf(\.pdf)?$", "", n)
    n = re.sub(r"\s*\((\d+|duplicate)\)\s*", " ", n)
    n = re.sub(r"\(v\d+\)", " ", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()


# Distinct documents that share a name — never treat as duplicates of each other
DISTINCT = {
    "papers/Mental Health/01 Mental Health - Extended/Effects of a Universal Classroom Behavior Management Program on Young Adult Outcomes (4).pdf",
}

# Cross-topic keeper preference by normalized-name substring
TOPIC_PREF = {
    "flossing": "Articles/01 Articles - Extended",
    "turnover of companies in openstack": "Articles/01 Articles - Extended",
    "telecommuting": "Remote Workers/01 Extended - Remote Workers",
    "job demands job resources": "Remote Workers/01 Extended - Remote Workers",
}


def suffix_rank(p: Path):
    # non-suffixed best; only a suffix at the END of the name counts
    # (author-year like "(2003)" mid-name must not match)
    if re.search(r"\((\d+|duplicate|v\d+)\)\s*(\.pdf)+$", p.name, re.I):
        return 1
    return 1 if p.name.lower().endswith(".pdf.pdf") else 0


def main():
    pdfs = [p for p in PAPERS.rglob("*.pdf")
            if "Backup" not in str(p) and p.is_file()
            and str(p.relative_to(REPO)) not in DISTINCT]
    # union-find: same md5 OR same normalized name => same group
    parent = {p: p for p in pdfs}
    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    hashes = {p: hashlib.md5(p.read_bytes()).hexdigest() for p in pdfs}
    byhash = defaultdict(list)
    byname = defaultdict(list)
    for p in pdfs:
        byhash[hashes[p]].append(p)
        byname[nk(p.name)].append(p)
    for ps in list(byhash.values()) + list(byname.values()):
        for other in ps[1:]:
            union(ps[0], other)
    groups = defaultdict(list)
    for p in pdfs:
        groups[find(p)].append(p)

    actions = []  # (keeper, [losers])
    for key, ps in sorted(groups.items(), key=lambda kv: str(kv[0])):
        if len(ps) < 2:
            continue
        key = nk(ps[0].name)
        def score(p):
            pref = TOPIC_PREF.get(next((k for k in TOPIC_PREF if k in key), ""), None)
            return (
                0 if conv_folder(p) else 1,
                suffix_rank(p),
                0 if (pref and topic_of(p) == pref) else 1,
                len(str(p)),
            )
        keeper = sorted(ps, key=score)[0]
        losers = [p for p in ps if p != keeper]
        actions.append((keeper, losers, hashes))

    ledger = ["# Duplicate removals — recorded per repair-plan decision #2",
              "", f"Deduplicated on 2026-07-07 by tools/audit/dedupe.py.",
              "Format: kept copy, then removed copies (md5 of removed content).", ""]
    for keeper, losers, hashes in actions:
        kc = conv_folder(keeper)
        print(f"KEEP  {keeper.relative_to(REPO)}  (conv: {'yes' if kc else 'NO'})")
        ledger.append(f"- **Kept:** `{keeper.relative_to(REPO)}`")
        for l in losers:
            lc = conv_folder(l)
            same = hashes[l] == hashes[keeper]
            print(f"  DEL {l.relative_to(REPO)}  [{'identical' if same else 'same-paper, different bytes'}]"
                  f"{'  +conv-folder' if lc and kc else ''}")
            ledger.append(f"  - removed `{l.relative_to(REPO)}` (md5 {hashes[l][:12]},"
                          f" {'identical' if same else 'same paper, different download'})")
            if APPLY:
                l.unlink()
                if lc and kc and lc != kc:
                    shutil.rmtree(lc)
                    ledger.append(f"  - removed conversion folder `{lc.relative_to(REPO)}`")
            elif lc and kc and lc != kc:
                print(f"      would also remove conv folder: {lc.relative_to(REPO)}")
        ledger.append("")
    if APPLY:
        (REPO / "DUPLICATES.md").write_text("\n".join(ledger) + "\n")
        print("\nwrote DUPLICATES.md")
    else:
        print("\nDRY RUN — re-run with --apply to execute")


if __name__ == "__main__":
    main()
