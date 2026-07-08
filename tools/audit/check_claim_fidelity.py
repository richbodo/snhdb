#!/usr/bin/env python3
"""Cheap corpus-wide fidelity check for regenerated cards: every numeric/statistic
token in a card's claims should appear in the source markdown. Reports per-card
match rates; low rates flag possible hallucination for human QA.

Not proof of correctness (numbers can match but be misattributed) — it is a
screen that catches fabricated statistics. Run after assemble_cards.py --apply.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
MD_ROOT = REPO / "papers" / "Markdown files" / "Papers_Data"
OUT = REPO / "tools" / "audit" / "out"

NUM = re.compile(r"(?<![\w.])(\d+(?:\.\d+)+|\d+(?:,\d{3})+|\d{2,})(?!\d)")
IGNORE = {"19", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "95", "90", "99"}  # covid/CI/years


def norm_digits(text):
    text = unicodedata.normalize("NFKD", text)
    return text.replace(",", "").replace("−", "-").replace("–", "-")


def main():
    rows = []
    for card in sorted(MD_ROOT.rglob("MD/*/card_schema.md")):
        if "Backup" in str(card):
            continue
        folder = card.parent
        mds = [f for f in folder.iterdir() if f.suffix == ".md" and f.name != "card_schema.md"]
        if not mds:
            continue
        try:
            doc = yaml.safe_load(card.read_text(errors="replace"))
        except Exception:
            continue
        claims = " ".join(c.get("text", "") for c in (doc.get("claims") or []))
        nums = [n for n in NUM.findall(norm_digits(claims)) if n not in IGNORE]
        if not nums:
            rows.append({"folder": folder.name, "nums": 0, "found": 0, "rate": None})
            continue
        src = norm_digits(mds[0].read_text(errors="replace"))
        found = sum(1 for n in set(nums) if n in src)
        rate = round(found / len(set(nums)), 2)
        rows.append({"folder": folder.name, "nums": len(set(nums)), "found": found, "rate": rate,
                     "missing": [n for n in set(nums) if n not in src][:6]})
    (OUT / "fidelity.json").write_text(json.dumps(rows, indent=1))
    with_nums = [r for r in rows if r["rate"] is not None]
    full = sum(1 for r in with_nums if r["rate"] == 1.0)
    low = sorted([r for r in with_nums if r["rate"] < 0.8], key=lambda r: r["rate"])
    print(f"cards checked: {len(rows)}  with numeric claims: {len(with_nums)}  "
          f"all-numbers-found: {full}  below-0.8: {len(low)}")
    for r in low[:20]:
        print(f"  {r['rate']:.2f} {r['folder'][:55]} missing={r['missing']}")


if __name__ == "__main__":
    main()
