#!/usr/bin/env python3
"""Build per-paper payloads for Phase 3 card regeneration.

Merges the conversion inventory with Phase 2's verified metadata so each
payload carries everything a generation agent + the assembler need.
Writes out/gen_payloads.json. Usage: gen_payloads.py [topic-filter]
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MD_ROOT = REPO / "papers" / "Markdown files" / "Papers_Data"
OUT = REPO / "tools" / "audit" / "out"
STAGING = OUT / "cards_gen"
STAGING.mkdir(parents=True, exist_ok=True)

meta = {m["card"]: m for m in json.loads((OUT / "verified_metadata.json").read_text())}
man = json.loads((OUT / "manifest.json").read_text())


def nk(n):
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\.(pdf|docx|md)$", "", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()


pdf_by_key = {}
for p in man["pdfs"]:
    pdf_by_key.setdefault(p["key"], p["path"])
    pdf_by_key.setdefault(re.sub(r"\s*\(\d+\)$", "", p["key"]).strip(), p["path"])

topic_filter = sys.argv[1] if len(sys.argv) > 1 else None
payloads = []
for card_path in sorted(MD_ROOT.rglob("MD/*/card_schema.md")):
    if "Backup" in str(card_path):
        continue
    folder = card_path.parent
    topic = str(folder.relative_to(MD_ROOT)).split("/")[0]
    if topic_filter and topic != topic_filter:
        continue
    mds = [f for f in folder.iterdir() if f.suffix == ".md" and f.name != "card_schema.md"]
    if not mds:
        continue
    rel_card = str(card_path.relative_to(REPO))
    m = meta.get(rel_card, {})
    rec = m.get("record")
    status = m.get("status", "unknown")
    # preserve existing no-doi note if any
    note = None
    txt = card_path.read_text(errors="replace")
    nm = re.search(r'notes:\s*"(no-doi:[^"]*)"', txt)
    if nm:
        note = nm.group(1)
    payloads.append({
        "idx": len(payloads),
        "topic": topic,
        "folder": folder.name,
        "card_path": rel_card,
        "md_path": str(mds[0]),
        "md_chars": mds[0].stat().st_size,
        "pdf_path": pdf_by_key.get(nk(folder.name)),
        "record": rec,
        "doi_status": status,
        "no_doi_note": note,
        # hash of card path = stable across corpus renumbering/renames of OTHER items
        "staging_file": str(STAGING / (
            __import__("hashlib").md5(rel_card.encode()).hexdigest()[:8] + "-"
            + re.sub(r"[^a-zA-Z0-9]+", "-", folder.name)[:52].strip("-") + ".json")),
    })

(OUT / "gen_payloads.json").write_text(json.dumps(payloads, indent=1))
from collections import Counter
print(f"{len(payloads)} payloads", Counter(p['topic'] for p in payloads))
