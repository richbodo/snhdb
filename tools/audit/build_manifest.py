#!/usr/bin/env python3
"""Build a manifest of the snhdb corpus: every PDF, every markdown conversion,
every card — matched to each other by normalized name.

Outputs manifest.json in the directory given as argv[1] (default: tools/audit/out).

Slow part: pdfinfo + pdftotext over every PDF (~317). Run once; re-run only
when the corpus changes.
"""
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAPERS = REPO / "papers"
MD_ROOT = PAPERS / "Markdown files" / "Papers_Data"
BACKUP_MARKER = "Backup"

OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "tools" / "audit" / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def norm_key(name: str) -> str:
    """Normalize a filename/folder name for matching."""
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode()
    name = name.lower()
    name = re.sub(r"\.(pdf|docx|md)$", "", name)
    name = re.sub(r"[^a-z0-9]+", " ", name)
    return name.strip()


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return None


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]\)}]+", re.I)


def clean_doi(d: str) -> str:
    d = d.rstrip(".,;:")
    # common OCR/extraction junk suffixes
    d = re.sub(r"(https?|Get|Downloaded|Copyright|©).*$", "", d)
    return d.strip().lower()


def find_dois(text: str):
    return sorted({clean_doi(m) for m in DOI_RE.findall(text or "") if clean_doi(m)})


# ---------------- PDFs ----------------
def scan_pdfs():
    pdfs = []
    for p in sorted(PAPERS.rglob("*.pdf")):
        rel = p.relative_to(REPO)
        if BACKUP_MARKER in str(rel):
            continue
        entry = {
            "path": str(rel),
            "key": norm_key(p.name),
            "bytes": p.stat().st_size,
            "pages": None,
            "text_chars": None,
            "dois_in_pdf": [],
            "pdf_error": None,
        }
        info = run(["pdfinfo", str(p)])
        if info and info.returncode == 0:
            m = re.search(r"^Pages:\s+(\d+)", info.stdout, re.M)
            if m:
                entry["pages"] = int(m.group(1))
        else:
            entry["pdf_error"] = (info.stderr.strip()[:200] if info else "timeout")
        txt = run(["pdftotext", "-q", str(p), "-"])
        if txt and txt.returncode == 0:
            entry["text_chars"] = len(txt.stdout)
            # DOIs usually on first pages; but search all extracted text
            entry["dois_in_pdf"] = find_dois(txt.stdout)[:10]
        pdfs.append(entry)
        print(f"pdf {len(pdfs)}: {rel}", file=sys.stderr)
    return pdfs


# ---------------- Conversions ----------------
SENT_END = re.compile(r'[.!?…]["\')\]]*\s*$')


def scan_conversions():
    convs = []
    for md_dir in sorted(MD_ROOT.rglob("MD")):
        if not md_dir.is_dir() or BACKUP_MARKER in str(md_dir):
            continue
        for folder in sorted(md_dir.iterdir()):
            if not folder.is_dir():
                continue
            rel = folder.relative_to(REPO)
            mds = [f for f in folder.iterdir()
                   if f.suffix == ".md" and f.name != "card_schema.md"]
            metas = list(folder.glob("*_meta.json"))
            entry = {
                "path": str(rel),
                "key": norm_key(folder.name),
                "topic": str(md_dir.relative_to(MD_ROOT).parent),
                "md_file": None, "md_chars": None, "md_lines": None,
                "ends_mid_sentence": None, "last_120_chars": None,
                "source_is_docx": ".docx" in folder.name or any(".docx" in f.name for f in mds),
                "meta_pages": None,
                "dois_in_md": [],
                "has_card_file": (folder / "card_schema.md").exists(),
                "has_references_heading": None,
                "figure_count": len(list(folder.glob("_page_*.jpeg"))) + len(list(folder.glob("*_page_*.jpeg"))),
            }
            if mds:
                md = mds[0]
                text = md.read_text(errors="replace")
                entry["md_file"] = md.name
                entry["md_chars"] = len(text)
                entry["md_lines"] = text.count("\n") + 1
                stripped = text.rstrip()
                entry["ends_mid_sentence"] = not bool(SENT_END.search(stripped[-200:])) if stripped else True
                entry["last_120_chars"] = stripped[-120:]
                entry["dois_in_md"] = find_dois(text)[:10]
                entry["has_references_heading"] = bool(
                    re.search(r"^#+\s*(references|bibliography|works cited)", text, re.I | re.M))
            if metas:
                try:
                    meta = json.loads(metas[0].read_text())
                    ps = meta.get("page_stats")
                    if isinstance(ps, list):
                        entry["meta_pages"] = len(ps)
                except Exception as e:
                    entry["meta_error"] = str(e)[:100]
            convs.append(entry)
    return convs


# ---------------- Cards ----------------
def parse_cards_file(path: Path):
    import yaml
    text = path.read_text(errors="replace")
    # drop the single permitted heading and any markdown fences
    chunks = re.split(r"^---\s*$", text, flags=re.M)
    cards, errors = [], []
    for i, chunk in enumerate(chunks):
        body = re.sub(r"^#.*$", "", chunk, flags=re.M).strip()
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        body = re.sub(r"^```(yaml)?\s*$", "", body, flags=re.M).strip()
        if not body:
            continue
        try:
            doc = yaml.safe_load(body)
        except Exception as e:
            errors.append({"file": str(path.relative_to(REPO)), "chunk": i,
                           "error": str(e)[:200], "head": body[:120]})
            continue
        if not isinstance(doc, dict) or "title" not in doc:
            continue
        src = (doc.get("source") or {}) if isinstance(doc.get("source"), dict) else {}
        cards.append({
            "file": str(path.relative_to(REPO)),
            "chunk": i,
            "id": doc.get("id"),
            "title": doc.get("title"),
            "authors": doc.get("authors"),
            "year": doc.get("year"),
            "doi": doc.get("doi"),
            "article_type": doc.get("article_type"),
            "gist": doc.get("gist"),
            "relevance": doc.get("relevance_to_project"),
            "source_markdown": src.get("markdown"),
            "citation": doc.get("citation"),
            "venue": doc.get("venue"),
            "population": doc.get("population"),
            "n_claims": len(doc.get("claims") or []),
        })
    return cards, errors


def scan_cards():
    all_cards, all_errors = [], []
    for f in sorted(MD_ROOT.rglob("*Card_Schemas.md")):
        if BACKUP_MARKER in str(f):
            continue
        cards, errors = parse_cards_file(f)
        all_cards += cards
        all_errors += errors
    return all_cards, all_errors


def main():
    print("scanning conversions...", file=sys.stderr)
    convs = scan_conversions()
    print(f"{len(convs)} conversion folders", file=sys.stderr)
    print("scanning cards...", file=sys.stderr)
    cards, card_errors = scan_cards()
    print(f"{len(cards)} cards, {len(card_errors)} parse errors", file=sys.stderr)
    print("scanning pdfs (slow)...", file=sys.stderr)
    pdfs = scan_pdfs()
    manifest = {"pdfs": pdfs, "conversions": convs,
                "cards": cards, "card_parse_errors": card_errors}
    out = OUT_DIR / "manifest.json"
    out.write_text(json.dumps(manifest, indent=1))
    print(f"wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
