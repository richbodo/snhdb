id: "thompson-2022-why-open-source-developers-are-burning"
title: "Why Open-Source Developers Are Burning Out"
authors:
  - "Thompson, Clive"
year: 2022
doi: null
venue: {type: "other", name: "Better Programming (Medium)", volume: null, issue: null, pages: null}
citation: "Thompson (2022). Why Open-Source Developers Are Burning Out. Better Programming (Medium)."
article_type: "commentary"
method: {design: "case-study", approach: "other", evidence_level: "speculative", preregistered: false}
gist: >
  This Medium/Better Programming piece uses the January 2022 'colors' npm library incident —
  in which maintainer Marak Squires intentionally sabotaged his own widely-used code,
  breaking thousands of dependent apps — as a case study for arguing that open-source
  maintenance has become unpaid, unsustainable labor performed by stressed individuals
  rather than the collaborative 'barn-raising' the movement promised. The corpus copy
  available here is truncated at Medium's paywall, so only the opening anecdote and framing
  are present, not the article's full argument or sourcing.
claims:
  - text: "The npm library 'colors', used by roughly 19,000 software projects with over 20 million weekly downloads, was deliberately sabotaged by its own maintainer, Marak Squires, who added an infinite loop producing garbled output and breaking dependent applications."
    evidence: "case-study"
    support_strength: "speculative"
    outcomes: ["burnout"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "Unnamed observers linked the sabotage to burnout, noting Squires had recently said he was feeling burned out and speculating about unspecified mental-health issues as a contributing factor."
    evidence: "case-study"
    support_strength: "speculative"
    outcomes: ["burnout", "mental-health"]
    predictors: ["open-source-maintenance"]
population:
  who: "A single open-source maintainer (Marak Squires, developer of the npm 'colors' and 'faker' libraries) used as an illustrative case; the article's implicit broader subject is unpaid maintainers of widely-depended-upon open-source software."
  where: []
  when: "January 2022"
  n: null
  sector: ["open-source", "software-development"]
  sample_notes: >
    This corpus copy contains only the article's opening ~500 words (the 'colors' library
    anecdote) before hitting a Medium members-only paywall; the rest of the file is site
    navigation, author bio, and unrelated 'recommended' article links, not further article
    content. No systematic sample — a single high-profile incident used illustratively, not
    research data.
limitation:
  primary: "Only the introductory anecdote of the article is present in this corpus copy; the full piece is behind Medium's paywall, so its main argument, evidence, and any additional examples are missing from this source file."
  others:
    - "Journalistic commentary, not peer-reviewed research, and even the visible portion rests on a single high-profile incident used illustratively."
    - "The claim that Squires's actions were mental-health related is attributed only to unnamed 'observers', with no cited sources."
risk_of_bias: "high"
relevance_to_project: >
  Provides a vivid, widely-cited motivating case for the SNH project's maintainer-burnout
  concern — sabotage of critical infrastructure as a visible failure mode of unsupported
  unpaid open-source labor — useful for framing why-it-matters narratives, though the
  fragment available here is too thin and unsourced to use as evidentiary support for any
  specific claim.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "mental-health"]
  method: ["case-study"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Articles/MD/Why Open-Source Developers Are Burning Out/Why Open-Source Developers Are Burning Out.md"
  pdf: "papers/Articles/Why Open-Source Developers Are Burning Out.pdf"
  notes: "no-doi: web article / no registered DOI found"
