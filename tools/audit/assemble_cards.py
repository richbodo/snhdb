#!/usr/bin/env python3
"""Phase 3 assembler: staged generation JSON + Phase 2 verified record
-> final card_schema.md, behind a validation gate.

Deterministic fields (id/title/authors/year/doi/venue/citation/source) come
from the verified record (or the agent's byline for no-DOI sources); the LLM
output supplies only fields that require reading the paper.

Usage: assemble_cards.py [--apply] [topic-filter]
Without --apply: validate everything, write nothing, print a report.
"""
import json
import re
import sys
import textwrap
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "tools" / "audit" / "out"
APPLY = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if a != "--apply"]
TOPIC = args[0] if args else None

EVID = {"speculative", "weak", "low", "low-to-moderate", "moderate", "strong",
        "very-strong", "reference"}
ROB = {"low", "medium", "high", "unclear", "not-applicable"}
ATYPE = {"empirical", "review", "theory", "methods", "commentary"}
VTYPE = {"journal", "book", "report", "thesis", "conference", "preprint", "other"}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BOILER_RELEVANCE_HEADS = (
    "useful for the remote-work stream because it indexes",
    "useful for anchoring snh theory-building",
    "useful for upstream mental-health framing",
    "useful for practitioner-facing context on open-source",
    "useful for the snh remote-worker evidence stream",
)


def q(s):
    return '"' + str(s).replace('\\', '\\\\').replace('"', "'").replace("\n", " ") + '"'


def block(s, indent="  "):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return "\n".join(textwrap.wrap(s, width=92, initial_indent=indent, subsequent_indent=indent))


def slugify(author, year, title):
    def n(t):
        t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
        return re.sub(r"[^a-z0-9]+", " ", t).strip()
    fam = n(author).split()[0] if author else "anon"
    words = "-".join(n(title).split()[:6])
    return f"{fam}-{year or 'nd'}-{words}"[:80]


ROB_MAP = {"moderate": "medium", "low-to-moderate": "medium", "very-low": "low",
           "na": "not-applicable", "none": "not-applicable"}


def normalize(gen):
    """Repair mechanical enum drift and list-length overruns in agent output.
    Content problems still fail validation."""
    rob = gen.get("risk_of_bias")
    if rob in ROB_MAP:
        gen["risk_of_bias"] = ROB_MAP[rob]
    for c in gen.get("claims") or []:
        for fld in ("outcomes", "predictors"):
            vals = [v for v in (c.get(fld) or []) if isinstance(v, str) and v.strip()]
            c[fld] = vals[:4]
        # a claim may honestly lack predictors (e.g. prevalence findings) but
        # needs at least one retrieval hook overall
        if not c["outcomes"] and not c["predictors"]:
            topic = ((gen.get("tags") or {}).get("topic") or ["methodology"])
            c["outcomes"] = topic[:1]
    tags = gen.get("tags") or {}
    if not tags.get("population"):
        sect = ((gen.get("population") or {}).get("sector") or ["general"])
        tags["population"] = [s for s in sect if isinstance(s, str)][:4] or ["general"]
        gen["tags"] = tags
    for fld in ("topic", "method", "population"):
        vals = [v for v in (tags.get(fld) or []) if isinstance(v, str) and v.strip()]
        tags[fld] = vals[:6]
    return gen


def validate(gen, payload):
    errs = []
    def need(cond, msg):
        if not cond:
            errs.append(msg)
    need(gen.get("article_type") in ATYPE, f"article_type invalid: {gen.get('article_type')}")
    m = gen.get("method") or {}
    need(m.get("evidence_level") in EVID, f"method.evidence_level invalid: {m.get('evidence_level')}")
    need(isinstance(m.get("preregistered"), bool), "method.preregistered must be bool")
    gist = (gen.get("gist") or "").strip()
    need(len(gist) >= 150, "gist too short (<150 chars)")
    need("retrieval card" not in gist.lower(), "gist uses old template language")
    claims = gen.get("claims") or []
    need(2 <= len(claims) <= 3, f"need 2-3 claims, got {len(claims)}")
    texts = set()
    for i, c in enumerate(claims):
        t = (c.get("text") or "").strip()
        need(len(t) >= 40, f"claim {i} text too short")
        need(t not in texts, f"claim {i} duplicates another claim")
        texts.add(t)
        need(c.get("support_strength") in EVID - {"reference"},
             f"claim {i} support_strength invalid")
        for fld in ("outcomes", "predictors"):
            vals = c.get(fld) or []
            need(len(vals) <= 4, f"claim {i} {fld} too many slugs")
            for v in vals:
                need(bool(SLUG.match(v)), f"claim {i} {fld} bad slug: {v}")
        need(bool(c.get("outcomes") or c.get("predictors")), f"claim {i} has no retrieval tags")
    pop = gen.get("population") or {}
    who = (pop.get("who") or "").strip()
    need(len(who) >= 15, "population.who too short")
    need("policy target population" not in who, "population.who is old boilerplate")
    need(gen.get("risk_of_bias") in ROB, f"risk_of_bias invalid: {gen.get('risk_of_bias')}")
    rel = re.sub(r"\s+", " ", (gen.get("relevance_to_project") or "")).strip().lower()
    need(len(rel) >= 80, "relevance_to_project too short")
    need(not any(rel.startswith(b) for b in BOILER_RELEVANCE_HEADS),
         "relevance_to_project matches old boilerplate")
    lim = gen.get("limitation") or {}
    need(len((lim.get("primary") or "").strip()) >= 20, "limitation.primary too short")
    tags = gen.get("tags") or {}
    for fld in ("topic", "method", "population"):
        vals = tags.get(fld) or []
        need(1 <= len(vals) <= 6, f"tags.{fld} needs 1-6 slugs")
    if not payload.get("record"):
        b = gen.get("byline") or {}
        need(bool((b.get("title") or "").strip()), "no-DOI source: byline.title required")
    return errs


def render(gen, payload):
    rec = payload.get("record")
    if rec:
        ident = {"id": slugify((rec["authors"][0].split(",")[0] if rec["authors"] else ""), rec["year"], rec["title"]),
                 "title": rec["title"], "authors": rec["authors"], "year": rec["year"],
                 "doi": rec["doi"], "vtype": rec["venue_type"], "vname": rec["container"],
                 "vol": rec.get("volume"), "iss": rec.get("issue"), "pages": rec.get("pages")}
    else:
        b = gen.get("byline") or {}
        ident = {"id": slugify((b.get("authors") or ["anon"])[0].split(",")[0], b.get("year"), b.get("title")),
                 "title": b.get("title"), "authors": b.get("authors") or [], "year": b.get("year"),
                 "doi": None, "vtype": b.get("venue_type") if b.get("venue_type") in VTYPE else "other",
                 "vname": b.get("venue_name"), "vol": None, "iss": None, "pages": None}
    au = ident["authors"]
    cit_a = (au[0].split(",")[0] + (" et al." if len(au) > 1 else "")) if au else (ident["vname"] or "Unknown")
    vol = f", {ident['vol']}" if ident.get("vol") else ""
    iss = f"({ident['iss']})" if ident.get("iss") else ""
    pg = f", {ident['pages']}" if ident.get("pages") else ""
    tail = f" https://doi.org/{ident['doi']}" if ident["doi"] else ""
    citation = f"{cit_a} ({ident['year']}). {ident['title']}. {ident['vname'] or ''}{vol}{iss}{pg}.{tail}".replace(" .", ".")

    def numor(v):
        return v if isinstance(v, int) or (isinstance(v, str) and v.isdigit()) else (q(v) if v else "null")

    m = gen["method"]
    pop = gen["population"]
    lim = gen["limitation"]
    tags = gen["tags"]
    md_rel = "Papers_Data/" + str(Path(payload["md_path"]).resolve().relative_to((REPO / "papers" / "Markdown files" / "Papers_Data").resolve()))
    L = []
    L.append(f"id: {q(ident['id'])}")
    L.append(f"title: {q(ident['title'])}")
    L.append("authors:")
    for a in au:
        L.append(f"  - {q(a)}")
    L.append(f"year: {ident['year'] if ident['year'] else 'null'}")
    L.append(f"doi: {q(ident['doi']) if ident['doi'] else 'null'}")
    L.append("venue: {type: %s, name: %s, volume: %s, issue: %s, pages: %s}" % (
        q(ident["vtype"]), q(ident["vname"]) if ident["vname"] else "null",
        numor(ident.get("vol")), numor(ident.get("iss")),
        q(ident["pages"]) if ident.get("pages") else "null"))
    L.append(f"citation: {q(citation)}")
    L.append(f"article_type: {q(gen['article_type'])}")
    L.append("method: {design: %s, approach: %s, evidence_level: %s, preregistered: %s}" % (
        q(m["design"]), q(m["approach"]), q(m["evidence_level"]),
        "true" if m["preregistered"] else "false"))
    L.append("gist: >")
    L.append(block(gen["gist"]))
    L.append("claims:")
    for c in gen["claims"]:
        L.append(f"  - text: {q(c['text'])}")
        L.append(f"    evidence: {q(c.get('evidence') or m['design'])}")
        L.append(f"    support_strength: {q(c['support_strength'])}")
        L.append("    outcomes: [%s]" % ", ".join(q(v) for v in c["outcomes"]))
        L.append("    predictors: [%s]" % ", ".join(q(v) for v in c["predictors"]))
    L.append("population:")
    L.append(f"  who: {q(pop['who'])}")
    L.append("  where: [%s]" % ", ".join(q(w) for w in (pop.get("where") or [])))
    L.append(f"  when: {q(pop['when']) if pop.get('when') else 'null'}")
    L.append(f"  n: {pop['n'] if isinstance(pop.get('n'), int) else 'null'}")
    L.append("  sector: [%s]" % ", ".join(q(s) for s in (pop.get("sector") or [])))
    L.append("  sample_notes: >")
    L.append(block(pop.get("sample_notes") or "None recorded.", "    "))
    L.append("limitation:")
    L.append(f"  primary: {q(lim['primary'])}")
    L.append("  others:")
    for o in (lim.get("others") or []):
        L.append(f"    - {q(o)}")
    L.append(f"risk_of_bias: {q(gen['risk_of_bias'])}")
    L.append("relevance_to_project: >")
    L.append(block(gen["relevance_to_project"]))
    L.append("tags:")
    for fld in ("topic", "method", "population"):
        L.append("  %s: [%s]" % (fld, ", ".join(q(v) for v in (tags.get(fld) or []))))
    L.append("source:")
    L.append(f"  markdown: {q(md_rel)}")
    L.append(f"  pdf: {q(payload['pdf_path']) if payload.get('pdf_path') else 'null'}")
    note = payload.get("no_doi_note")
    if not note and not ident["doi"]:
        st = (gen.get("byline") or {}).get("source_type") or "source"
        note = f"no-doi: {st}"
    L.append(f"  notes: {q(note) if note else 'null'}")
    return "\n".join(L) + "\n"


def main():
    payloads = json.loads((OUT / "gen_payloads.json").read_text())
    if TOPIC:
        payloads = [p for p in payloads if p["topic"] == TOPIC]
    ok = failed = missing = 0
    failures = []
    for p in payloads:
        sf = Path(p["staging_file"])
        if not sf.exists():
            missing += 1
            failures.append({"folder": p["folder"], "errors": ["staging file missing"]})
            continue
        try:
            gen = json.loads(sf.read_text())
        except Exception as e:
            failed += 1
            failures.append({"folder": p["folder"], "errors": [f"staging JSON invalid: {e}"]})
            continue
        gen = normalize(gen)
        errs = validate(gen, p)
        if not errs:
            try:
                text = render(gen, p)
                doc = yaml.safe_load(text)
                assert isinstance(doc, dict) and doc.get("title") and doc.get("claims")
            except Exception as e:
                errs = [f"render/YAML failed: {str(e)[:120]}"]
        if errs:
            failed += 1
            failures.append({"folder": p["folder"], "errors": errs})
            continue
        ok += 1
        if APPLY:
            (REPO / p["card_path"]).write_text(text)
    (OUT / "assemble_report.json").write_text(json.dumps(failures, indent=1))
    print(f"ok={ok} failed={failed} missing={missing} apply={APPLY}")
    for f in failures[:15]:
        print(" FAIL:", f["folder"][:55], "|", "; ".join(f["errors"])[:120])


if __name__ == "__main__":
    main()
