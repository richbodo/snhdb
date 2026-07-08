#!/usr/bin/env python3
"""Verify card DOIs against Crossref.

For every card with a DOI: GET https://api.crossref.org/works/<doi> and compare
the registered title with the card title AND the conversion folder name
(card titles are often filenames, so check both).

For cards with no DOI anywhere: query Crossref by title and report the best
candidate DOI + similarity, as a suggestion only.

Writes out/crossref.json. Be polite: ~1 req/sec, mailto in UA.
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

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "tools" / "audit" / "out"
MAILTO = "richbodo@gmail.com"
UA = {"User-Agent": f"snhdb-corpus-audit/1.0 (mailto:{MAILTO})"}

man = json.loads((OUT / "manifest.json").read_text())


def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def sim(a, b):
    return round(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio(), 2)


def get(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"_http_error": e.code}
    except Exception as e:
        return {"_error": str(e)[:200]}


def folder_name(card):
    sm = card.get("source_markdown") or ""
    parts = sm.split("/")
    return parts[-2] if len(parts) >= 2 else ""


results = []
seen = {}
cards = man["cards"]
with_doi = [c for c in cards if c.get("doi")]
no_doi = [c for c in cards if not c.get("doi")]
print(f"{len(with_doi)} cards with DOI, {len(no_doi)} without", file=sys.stderr)

for i, card in enumerate(with_doi):
    doi = card["doi"].strip().lower().replace("https://doi.org/", "")
    if doi in seen:
        res = dict(seen[doi])
    else:
        data = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))
        time.sleep(1.0)
        if "_http_error" in data:
            res = {"doi": doi, "status": f"http_{data['_http_error']}"}
        elif "_error" in data:
            res = {"doi": doi, "status": "error", "error": data["_error"]}
        else:
            msg = data.get("message", {})
            cr_title = (msg.get("title") or [""])[0]
            authors = [a.get("family", "") for a in (msg.get("author") or [])][:6]
            year = None
            for k in ("published-print", "published-online", "issued"):
                dp = (msg.get(k) or {}).get("date-parts")
                if dp and dp[0]:
                    year = dp[0][0]
                    break
            res = {"doi": doi, "status": "ok", "cr_title": cr_title,
                   "cr_authors": authors, "cr_year": year,
                   "cr_container": (msg.get("container-title") or [""])[0]}
        seen[doi] = res
    res = dict(res)
    res.update({
        "card_title": card["title"], "card_file": card["file"],
        "sim_card_title": sim(res.get("cr_title", ""), card["title"] or ""),
        "sim_folder": sim(res.get("cr_title", ""), folder_name(card)),
    })
    res["kind"] = "verify"
    results.append(res)
    print(f"[{i+1}/{len(with_doi)}] {doi} -> {res['status']} "
          f"sim_title={res['sim_card_title']} sim_folder={res['sim_folder']}", file=sys.stderr)

for i, card in enumerate(no_doi):
    q = folder_name(card) or card.get("title") or ""
    if not q:
        continue
    url = ("https://api.crossref.org/works?rows=1&query.bibliographic="
           + urllib.parse.quote(q))
    data = get(url)
    time.sleep(1.0)
    items = ((data.get("message") or {}).get("items") or []) if "_http_error" not in data and "_error" not in data else []
    if items:
        it = items[0]
        cr_title = (it.get("title") or [""])[0]
        results.append({
            "kind": "suggest", "card_title": card["title"], "card_file": card["file"],
            "query": q, "suggested_doi": it.get("DOI"),
            "cr_title": cr_title, "sim_folder": sim(cr_title, q),
            "cr_year": ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],
        })
    else:
        results.append({"kind": "suggest", "card_title": card["title"],
                        "card_file": card["file"], "query": q, "suggested_doi": None})
    print(f"[suggest {i+1}/{len(no_doi)}] {q[:60]}", file=sys.stderr)

(OUT / "crossref.json").write_text(json.dumps(results, indent=1))
ok = [r for r in results if r["kind"] == "verify"]
bad = [r for r in ok if r["status"] != "ok"]
weak = [r for r in ok if r["status"] == "ok" and max(r["sim_card_title"], r["sim_folder"]) < 0.6]
sugg = [r for r in results if r["kind"] == "suggest" and r.get("suggested_doi")
        and r.get("sim_folder", 0) >= 0.75]
print(f"\nverified: {len(ok)}  unresolvable DOIs: {len(bad)}  "
      f"resolves-but-wrong-paper: {len(weak)}  confident suggestions: {len(sugg)}")
