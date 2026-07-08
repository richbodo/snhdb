id: "smith-2024-the-developer-crisis-mental-health-burnout"
title: "The Developer Crisis: Mental Health, Burnout, and Retention"
authors:
  - "Smith, Craig"
year: 2024
doi: null
venue: {type: "other", name: "The New Stack", volume: null, issue: null, pages: null}
citation: "Smith (2024). The Developer Crisis: Mental Health, Burnout, and Retention. The New Stack."
article_type: "commentary"
method: {design: "theory", approach: "secondary-data", evidence_level: "weak", preregistered: false}
gist: >
  A trade-publication opinion piece arguing that UK software companies risk losing
  developers to burnout and turnover unless they address unpaid overtime, meeting overload,
  rigid training programs, and tedious backend work. It strings together burnout, quit-
  intention, and productivity statistics from third-party surveys (JetBrains, Stack
  Overflow, McKinsey, standout-cv, ITPro) to make the case for flexible schedules, feedback
  loops, and tooling investment, but conducts no original research of its own.
claims:
  - text: "67% of developers have left a job, or know someone who has, specifically to avoid pressure to minimize deployment errors; among those who stayed, 28% reported lowered productivity due to excessive stress."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["turnover", "stress", "productivity"]
    predictors: ["workload", "technostress"]
  - text: "Nearly three-quarters of developers report having experienced burnout on the job, cited from JetBrains' 2023 developer ecosystem survey."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["burnout"]
    predictors: ["workload", "technostress"]
  - text: "47% of burned-out developers use self-help apps to track their health, and asking developers directly how they spend their time can shorten project lead times by up to 40% (cited McKinsey figure)."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["burnout", "productivity"]
    predictors: ["intervention", "workload"]
population:
  who: "Software developers generally, with a UK-market framing (referencing UK tech vacancy projections); population is characterized only via statistics borrowed from other surveys, not sampled directly by this article."
  where: ["United Kingdom", "unspecified/global (per cited surveys)"]
  when: "2023-2024 (cited survey data)"
  n: null
  sector: ["technology", "software-development"]
  sample_notes: >
    This is a secondary/opinion piece; it has no sample of its own. It aggregates statistics
    from at least six external sources (JetBrains DevEcosystem 2023, Stack Overflow 2023,
    McKinsey, ITPro, standout-cv, worklife.news) without stating their sample sizes,
    sampling methods, or exact dates, so figures cannot be independently verified within
    this document.
limitation:
  primary: "The piece is an opinion/advisory trade article, not original research: it aggregates statistics from multiple third-party surveys without describing their methodology, sample size, or exact survey date, so the cited figures are unverifiable from this document alone."
  others:
    - "Author is an ecommerce technology consultant, not a researcher, writing for a sponsor-supported trade publication (The New Stack)"
    - "Recommendations (reduce meetings, flexible training, offload menial coding tasks) are prescriptive assertions not tested for effectiveness in this piece"
    - "No discussion of causality, confounds, or generalizability of the borrowed statistics"
risk_of_bias: "high"
relevance_to_project: >
  Useful as a source of widely-circulated industry burnout and turnover figures for software
  developers (burnout prevalence, overtime-driven quitting, self-help app adoption) that can
  motivate the SNH project's developer/maintainer burnout framing, but each figure should be
  traced back to and verified against its primary survey (e.g., JetBrains DevEcosystem,
  Stack Overflow Developer Survey) before being cited as evidence.
tags:
  topic: ["burnout", "job-satisfaction", "wellbeing", "technostress"]
  method: ["secondary-data", "survey"]
  population: ["software-developers", "tech-industry"]
source:
  markdown: "Papers_Data/Articles/MD/The Developer Crisis Mental Health Burnout and Retention/The Developer Crisis Mental Health Burnout and Retention.md"
  pdf: "papers/Articles/The Developer Crisis Mental Health Burnout and Retention.pdf"
  notes: "no-doi: web article / no registered DOI found"
