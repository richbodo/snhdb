#!/usr/bin/env python3
"""Regenerate the combined *_Card_Schemas.md files from the per-paper
card_schema.md files (which are the source of truth — repair-plan decision #1).

Each topic's combined file covers the topic's MD tree AND its '01 ... Extended'
subtree, matching the original layout. A generation header records provenance.
Run after any change to individual cards. Idempotent.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MD_ROOT = REPO / "papers" / "Markdown files" / "Papers_Data"

TOPICS = {
    "Academic": "Academic_Card_Schemas.md",
    "Articles": "Articles_Card_Schemas.md",
    "Mental Health": "Mental_Health_Card_Schemas.md",
    "Remote Worker SNH": "Remote_Worker_SNH_Card_Schemas.md",
    "Remote Workers": "Remote_Workers_Card_Schemas.md",
}


def main():
    for topic, fname in TOPICS.items():
        tdir = MD_ROOT / topic
        cards = sorted(tdir.glob("*/MD/*/card_schema.md")) + sorted(tdir.glob("MD/*/card_schema.md"))
        cards = [c for c in cards if "Backup" not in str(c)]
        parts = [f"# Card Schemas - {topic}",
                 "",
                 "<!-- GENERATED FILE - do not edit. Source of truth is each paper's",
                 "     MD/<paper>/card_schema.md. Regenerate with:",
                 "     python3 tools/audit/build_combined_cards.py -->",
                 ""]
        bodies = []
        for c in sorted(cards, key=lambda p: p.parent.name.lower()):
            bodies.append(c.read_text(errors="replace").strip())
        parts.append("\n\n---\n\n".join(bodies))
        out = tdir / fname
        out.write_text("\n".join(parts) + "\n")
        print(f"{out.relative_to(REPO)}: {len(bodies)} cards")


if __name__ == "__main__":
    main()
