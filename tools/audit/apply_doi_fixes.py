#!/usr/bin/env python3
"""Phase 2: repair DOIs and backfill Crossref-verified metadata into the
per-paper card_schema.md files (source of truth per repair-plan decision #1).

Logic per card:
  - current DOI verified correct (Crossref title ~ card title/folder >= 0.8): keep,
    still backfill authors/year/venue/citation from the Crossref record.
  - otherwise search Crossref bibliographically (folder name, then card title):
      best-hit similarity >= AUTO_T  -> accept + backfill
      MANUAL_T..AUTO_T               -> manual queue (no changes written)
      < MANUAL_T                     -> web-article/no-DOI classification if in a
                                        web-content topic, else manual queue
Outputs:
  out/verified_metadata.json  per-card outcome + the Crossref record applied
  out/manual_queue.json       cards needing a human/LLM decision
Options: --apply to write changes; default dry-run. --decisions FILE to apply
resolved manual-queue entries {card_path: doi_or_null}.
"""
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
MD_ROOT = REPO / "papers" / "Markdown files" / "Papers_Data"
OUT = REPO / "tools" / "audit" / "out"
APPLY = "--apply" in sys.argv
AUTO_T, MANUAL_T = 0.90, 0.70
UA = {"User-Agent": "snhdb-corpus-audit/1.0 (mailto:richbodo@gmail.com)"}
WEB_TOPICS = ("Articles",)  # topics whose no-match items are web articles

decisions = {}
if "--decisions" in sys.argv:
    decisions = json.loads(Path(sys.argv[sys.argv.index("--decisions") + 1]).read_text())

# cache of prior verification results keyed by doi
verify_cache = {}
cr_file = OUT / "crossref.json"
if cr_file.exists():
    for r in json.loads(cr_file.read_text()):
        if r.get("kind") == "verify" and r.get("status") == "ok":
            verify_cache.setdefault(r["doi"], r)

api_cache_path = OUT / "crossref_api_cache.json"
api_cache = json.loads(api_cache_path.read_text()) if api_cache_path.exists() else {}


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def get(url):
    if url in api_cache:
        return api_cache[url]
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
    except Exception as e:
        data = {"_error": getattr(e, "code", str(e)[:120])}
    api_cache[url] = data
    time.sleep(1.0)
    return data


def cr_work(doi):
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
    return d.get("message") if isinstance(d, dict) and "message" in d else None


def cr_search(q):
    d = get("https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(q))
    return ((d.get("message") or {}).get("items") or []) if isinstance(d, dict) else []


def rec_from_msg(msg):
    if not msg:
        return None
    year = None
    for k in ("published-print", "published-online", "issued"):
        dp = (msg.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            year = dp[0][0]
            break
    authors = []
    for a in (msg.get("author") or []):
        fam, giv = a.get("family"), a.get("given")
        if fam:
            authors.append(f"{fam}, {giv}" if giv else fam)
    tmap = {"journal-article": "journal", "proceedings-article": "conference",
            "book-chapter": "book", "book": "book", "posted-content": "preprint",
            "report": "report", "dissertation": "thesis"}
    # Crossref titles can contain embedded newlines/footnote markers — flatten
    title = re.sub(r"\s+", " ", (msg.get("title") or [""])[0]).strip(" *")
    return {
        "doi": (msg.get("DOI") or "").lower(),
        "title": title,
        "authors": authors,
        "year": year,
        "venue_type": tmap.get(msg.get("type"), "other"),
        "container": (msg.get("container-title") or [None])[0],
        "volume": msg.get("volume"),
        "issue": msg.get("issue"),
        "pages": msg.get("page"),
    }


def slug(rec):
    fam = norm((rec["authors"][0].split(",")[0]) if rec["authors"] else "anon").replace(" ", "-")
    words = norm(rec["title"]).split()[:6]
    return f"{fam}-{rec['year'] or 'nd'}-{'-'.join(words)}"[:80]


def q(s):
    return '"' + str(s).replace('"', "'") + '"'


def rewrite_card(path: Path, rec):
    """Line-based update of id/title/authors/year/doi/venue/citation, preserving
    the rest of the card (gist, claims, ...) untouched."""
    lines = path.read_text(errors="replace").splitlines()
    out, i = [], 0
    top = re.compile(r"^([a-z_]+):")
    cit_authors = (rec["authors"][0].split(",")[0] + (" et al." if len(rec["authors"]) > 1 else "")) if rec["authors"] else ""
    vol = f", {rec['volume']}" if rec["volume"] else ""
    iss = f"({rec['issue']})" if rec["issue"] else ""
    pg = f", {rec['pages']}" if rec["pages"] else ""
    citation = f"{cit_authors} ({rec['year']}). {rec['title']}. {rec['container'] or ''}{vol}{iss}{pg}. https://doi.org/{rec['doi']}"
    venue = ("venue: {type: %s, name: %s, volume: %s, issue: %s, pages: %s}" % (
        q(rec["venue_type"]),
        q(rec["container"]) if rec["container"] else "null",
        rec["volume"] if (rec["volume"] or "").isdigit() else (q(rec["volume"]) if rec["volume"] else "null"),
        rec["issue"] if (rec["issue"] or "").isdigit() else (q(rec["issue"]) if rec["issue"] else "null"),
        q(rec["pages"]) if rec["pages"] else "null"))
    repl = {
        "id": f"id: {q(slug(rec))}",
        "title": f"title: {q(rec['title'])}",
        "year": f"year: {rec['year'] if rec['year'] else 'null'}",
        "doi": f"doi: {q(rec['doi'])}",
        "venue": venue,
        "citation": f"citation: {q(citation)}",
    }
    while i < len(lines):
        m = top.match(lines[i])
        key = m.group(1) if m else None
        if key == "authors":
            out.append("authors:")
            for a in rec["authors"] or []:
                out.append(f"  - {q(a)}")
            i += 1
            while i < len(lines) and (lines[i].startswith(("  ", "\t")) or lines[i].strip() == ""):
                if lines[i].strip() == "" and i + 1 < len(lines) and top.match(lines[i + 1]):
                    break
                if top.match(lines[i]):
                    break
                i += 1
            continue
        if key in repl:
            out.append(repl[key])
            # skip continuation lines of flow maps / quoted scalars spanning lines
            i += 1
            while i < len(lines) and not top.match(lines[i]) and lines[i].strip() != "" \
                    and (lines[i].startswith((" ", "\t"))):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    path.write_text("\n".join(out) + "\n")


def set_no_doi_note(path: Path, reason):
    text = path.read_text(errors="replace")
    new = re.sub(r"(\n\s*notes:\s*)(null|~|\"\")", lambda m: m.group(1) + q("no-doi: " + reason), text, count=1)
    if new == text and "no-doi" not in text:
        new = text.rstrip("\n") + f'\n# no-doi: {reason}\n'
    path.write_text(new)


def main():
    results, queue = [], []
    folders = sorted(p.parent for p in MD_ROOT.rglob("MD/*/card_schema.md") if "Backup" not in str(p))
    for n, folder in enumerate(folders):
        card_path = folder / "card_schema.md"
        try:
            doc = yaml.safe_load(card_path.read_text(errors="replace"))
        except Exception as e:
            results.append({"card": str(card_path.relative_to(REPO)), "status": "yaml-error", "error": str(e)[:120]})
            continue
        if not isinstance(doc, dict):
            results.append({"card": str(card_path.relative_to(REPO)), "status": "yaml-error"})
            continue
        fname = folder.name
        ctitle = doc.get("title") or ""
        cdoi = (doc.get("doi") or "").lower().replace("https://doi.org/", "").strip() or None
        topic = str(folder.relative_to(MD_ROOT)).split("/")[0]
        entry = {"card": str(card_path.relative_to(REPO)), "folder": fname, "topic": topic,
                 "old_doi": cdoi}
        rel = str(card_path.relative_to(REPO))

        # manual decision override
        if rel in decisions:
            dec = decisions[rel]
            if dec:
                rec = rec_from_msg(cr_work(dec))
                if rec:
                    entry.update(status="manual-applied", record=rec)
                    if APPLY:
                        rewrite_card(card_path, rec)
                else:
                    entry.update(status="manual-doi-unresolvable", doi=dec)
            else:
                entry.update(status="manual-no-doi")
                if APPLY:
                    set_no_doi_note(card_path, "confirmed none (manual review)")
            results.append(entry)
            print(f"[{n+1}/{len(folders)}] {entry['status']}: {fname[:60]}", file=sys.stderr)
            continue

        rec = None
        # 1) is the existing DOI already verified good?
        if cdoi:
            v = verify_cache.get(cdoi)
            cr_title = v.get("cr_title") if v else None
            if cr_title is None:
                msg = cr_work(cdoi)
                cr_title = (msg.get("title") or [""])[0] if msg else None
            if cr_title and max(sim(cr_title, ctitle), sim(cr_title, fname)) >= 0.8:
                rec = rec_from_msg(cr_work(cdoi))
                entry["status"] = "kept-verified"
        # 2) re-resolve by search
        if rec is None:
            best, best_s = None, 0.0
            for query in {fname, ctitle} - {""}:
                for it in cr_search(query):
                    t = (it.get("title") or [""])[0]
                    s = max(sim(t, fname), sim(t, ctitle))
                    if s > best_s:
                        best, best_s = it, s
            if best and best_s >= AUTO_T:
                rec = rec_from_msg(best)
                entry["status"] = "resolved" if not cdoi else "replaced"
                entry["similarity"] = round(best_s, 2)
            elif best and best_s >= MANUAL_T:
                entry.update(status="manual-queue", similarity=round(best_s, 2),
                             candidate_doi=(best.get("DOI") or "").lower(),
                             candidate_title=(best.get("title") or [""])[0],
                             card_title=ctitle)
                queue.append(entry)
            else:
                if topic in WEB_TOPICS:
                    entry["status"] = "no-doi-web"
                    if APPLY:
                        set_no_doi_note(card_path, "web article / no registered DOI found")
                else:
                    entry.update(status="manual-queue", similarity=round(best_s, 2) if best else 0,
                                 candidate_doi=(best.get("DOI") or "").lower() if best else None,
                                 candidate_title=(best.get("title") or [""])[0] if best else None,
                                 card_title=ctitle)
                    queue.append(entry)
        if rec:
            entry["record"] = rec
            if APPLY:
                rewrite_card(card_path, rec)
        results.append(entry)
        print(f"[{n+1}/{len(folders)}] {entry['status']}: {fname[:60]}", file=sys.stderr)
        if (n + 1) % 25 == 0:
            api_cache_path.write_text(json.dumps(api_cache))

    api_cache_path.write_text(json.dumps(api_cache))
    OUT.mkdir(exist_ok=True)
    (OUT / "verified_metadata.json").write_text(json.dumps(results, indent=1))
    (OUT / "manual_queue.json").write_text(json.dumps(queue, indent=1))
    from collections import Counter
    print(Counter(r["status"] for r in results))
    print(f"manual queue: {len(queue)}  (apply={APPLY})")


if __name__ == "__main__":
    main()
