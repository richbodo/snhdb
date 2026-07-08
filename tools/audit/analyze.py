#!/usr/bin/env python3
"""Analyze manifest.json → issues.json + summary counts on stdout.

Issue categories:
  unconverted_pdf        PDF with no markdown conversion folder
  orphan_conversion      conversion folder with no matching source PDF
  truncated_pages        converter processed fewer pages than the PDF has
  low_text_ratio         markdown much shorter than pdftotext extraction
  ends_mid_sentence      markdown ends without sentence-final punctuation
  tiny_markdown          markdown under 1000 chars
  missing_md_file        conversion folder with no main .md file
  card_missing_doi       card doi null but a DOI exists in source pdf/md
  card_doi_mismatch      card doi not found in source pdf or md text
  card_no_doi_anywhere   empirical/review card with no DOI in card or source
  boilerplate_gist       gist text shared verbatim by >=3 cards
  boilerplate_relevance  relevance_to_project shared verbatim by >=3 cards
  bad_authors            authors empty, missing, or single-token junk
  title_is_filename      card title == conversion folder name
  duplicate_card_title   same normalized title on >1 card
  raw_doi_id             card id is a raw DOI, not a slug
  conversion_without_card  conversion folder not matched by any card
  card_without_conversion  card whose source.markdown doesn't resolve
  duplicate_pdf          same normalized name at multiple paths
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "tools" / "audit" / "out"
man = json.loads((OUT / "manifest.json").read_text())


def norm_key(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    name = re.sub(r"\.(pdf|docx|md)$", "", name)
    return re.sub(r"[^a-z0-9]+", " ", name).strip()


def strip_dup_suffix(key):
    return re.sub(r"\s*\(\d+\)$", "", key).strip()


issues = defaultdict(list)

pdfs = man["pdfs"]
convs = man["conversions"]
cards = man["cards"]

pdf_by_key = defaultdict(list)
for p in pdfs:
    pdf_by_key[p["key"]].append(p)

conv_by_key = defaultdict(list)
for c in convs:
    conv_by_key[c["key"]].append(c)

# resolve card -> conversion via source.markdown
conv_by_path = {}
for c in convs:
    # conv path like papers/Markdown files/Papers_Data/<topic>/MD/<name>
    tail = c["path"].split("Papers_Data/", 1)[-1]
    conv_by_path[tail.lower()] = c

def card_conv(card):
    sm = card.get("source_markdown") or ""
    sm = sm.replace("Papers_Data/", "", 1)
    folder = "/".join(sm.split("/")[:-1]).lower()
    return conv_by_path.get(folder)

# ---- matching pdf <-> conversion ----
matched_conv_keys = set()
for p in pdfs:
    keys = [p["key"], strip_dup_suffix(p["key"])]
    hit = None
    for k in keys:
        if conv_by_key.get(k):
            hit = conv_by_key[k][0]
            break
    if hit:
        p["_conv"] = hit["path"]
        hit.setdefault("_pdfs", []).append(p["path"])
        matched_conv_keys.add(hit["key"])
    else:
        issues["unconverted_pdf"].append({"pdf": p["path"], "pages": p["pages"]})

for c in convs:
    if "_pdfs" not in c and not c["source_is_docx"]:
        issues["orphan_conversion"].append({"conv": c["path"]})

# duplicate PDFs
for k, plist in pdf_by_key.items():
    if len(plist) > 1:
        issues["duplicate_pdf"].append({"key": k, "paths": [p["path"] for p in plist]})
base_groups = defaultdict(list)
for k in pdf_by_key:
    base_groups[strip_dup_suffix(k)].append(k)
for base, ks in base_groups.items():
    if len(ks) > 1:
        paths = [p["path"] for k in ks for p in pdf_by_key[k]]
        issues["duplicate_pdf"].append({"key": base, "paths": paths})

# ---- truncation ----
for c in convs:
    pdf = None
    if c.get("_pdfs"):
        cand = [p for p in pdfs if p["path"] == c["_pdfs"][0]]
        pdf = cand[0] if cand else None
    if c["md_file"] is None:
        issues["missing_md_file"].append({"conv": c["path"]})
        continue
    if pdf and pdf["pages"] and c["meta_pages"] and c["meta_pages"] < pdf["pages"]:
        issues["truncated_pages"].append(
            {"conv": c["path"], "pdf": pdf["path"],
             "converted_pages": c["meta_pages"], "pdf_pages": pdf["pages"]})
    if pdf and pdf["text_chars"] and pdf["text_chars"] > 4000 and c["md_chars"]:
        ratio = c["md_chars"] / pdf["text_chars"]
        if ratio < 0.5:
            issues["low_text_ratio"].append(
                {"conv": c["path"], "pdf": pdf["path"],
                 "md_chars": c["md_chars"], "pdf_chars": pdf["text_chars"],
                 "ratio": round(ratio, 2)})
    if c["md_chars"] is not None and c["md_chars"] < 1000:
        issues["tiny_markdown"].append({"conv": c["path"], "md_chars": c["md_chars"]})
    if c["ends_mid_sentence"]:
        issues["ends_mid_sentence"].append(
            {"conv": c["path"], "tail": (c["last_120_chars"] or "")[-80:]})

# ---- DOI checks ----
def norm_doi(d):
    return (d or "").strip().lower().replace("https://doi.org/", "")

for card in cards:
    conv = card_conv(card)
    src_dois = set()
    if conv:
        src_dois |= set(conv.get("dois_in_md") or [])
        for pp in conv.get("_pdfs", []):
            cand = [p for p in pdfs if p["path"] == pp]
            if cand:
                src_dois |= set(cand[0].get("dois_in_pdf") or [])
    cd = norm_doi(card.get("doi"))
    ident = {"card_title": card["title"], "file": card["file"], "doi": card.get("doi")}
    if not conv:
        issues["card_without_conversion"].append(
            {**ident, "source_markdown": card.get("source_markdown")})
    if cd:
        if src_dois and cd not in src_dois:
            issues["card_doi_mismatch"].append(
                {**ident, "dois_in_source": sorted(src_dois)[:5],
                 "conv": conv["path"] if conv else None})
        elif not src_dois:
            issues["card_doi_unverifiable"].append(
                {**ident, "note": "no DOI found in source pdf/md to check against"})
    else:
        if src_dois:
            issues["card_missing_doi"].append(
                {**ident, "dois_in_source": sorted(src_dois)[:5]})
        elif card.get("article_type") in ("empirical", "review", "methods",
                                          "methodological", "theory", "theoretical"):
            issues["card_no_doi_anywhere"].append(
                {**ident, "article_type": card.get("article_type")})

# ---- card quality ----
def norm_text(t):
    return re.sub(r"\s+", " ", (t or "").strip().lower())

gists = defaultdict(list)
rels = defaultdict(list)
titles = defaultdict(list)
for card in cards:
    g = norm_text(card.get("gist"))
    # boilerplate detector: also catch the templated lead-in
    gists[g].append(card)
    rels[norm_text(card.get("relevance"))].append(card)
    titles[norm_text(card.get("title"))].append(card)

    a = card.get("authors")
    if not a or (isinstance(a, list) and (
            len(a) == 0 or all(isinstance(x, str) and ("," not in x and len(x.split()) <= 2) for x in a))):
        issues["bad_authors"].append(
            {"card_title": card["title"], "file": card["file"], "authors": a})
    cid = card.get("id") or ""
    if cid.startswith("10."):
        issues["raw_doi_id"].append({"card_title": card["title"], "id": cid, "file": card["file"]})
    conv = card_conv(card)
    if conv and norm_key(card.get("title") or "") == conv["key"]:
        issues["title_is_filename"].append({"card_title": card["title"], "conv": conv["path"]})

for g, cs in gists.items():
    if g and len(cs) >= 3:
        issues["boilerplate_gist"].append(
            {"gist_head": g[:100], "count": len(cs),
             "cards": [c["title"] for c in cs][:8]})
# templated lead-in even when unique overall
LEADIN = "this source gives the project a retrieval card"
n_leadin = sum(1 for g in gists for _ in gists[g] if g.startswith(LEADIN))
for r, cs in rels.items():
    if r and len(cs) >= 3:
        issues["boilerplate_relevance"].append(
            {"relevance_head": r[:100], "count": len(cs),
             "cards": [c["title"] for c in cs][:8]})
for t, cs in titles.items():
    if t and len(cs) > 1:
        issues["duplicate_card_title"].append(
            {"title": cs[0]["title"], "count": len(cs), "files": sorted({c['file'] for c in cs})})

# conversions not covered by any card
carded = set()
for card in cards:
    conv = card_conv(card)
    if conv:
        carded.add(conv["path"])
for c in convs:
    if c["path"] not in carded:
        issues["conversion_without_card"].append(
            {"conv": c["path"], "has_local_card_file": c["has_card_file"]})

# ---- write ----
out = {k: v for k, v in sorted(issues.items())}
(OUT / "issues.json").write_text(json.dumps(out, indent=1))
print(f"cards: {len(cards)}  conversions: {len(convs)}  pdfs: {len(pdfs)}")
print(f"cards with templated gist lead-in: {n_leadin}")
print(f"card parse errors: {len(man['card_parse_errors'])}")
for k, v in out.items():
    print(f"{k}: {len(v)}")
