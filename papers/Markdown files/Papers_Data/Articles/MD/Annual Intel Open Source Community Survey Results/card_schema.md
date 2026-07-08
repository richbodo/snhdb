id: "mcdonald-2024-annual-intel-open-source-community-survey"
title: "Annual Intel Open Source Community Survey Results"
authors:
  - "McDonald, Nikki"
year: 2024
doi: null
venue: {type: "other", name: "Intel Open Ecosystem", volume: null, issue: null, pages: null}
citation: "McDonald (2024). Annual Intel Open Source Community Survey Results. Intel Open Ecosystem."
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "weak", preregistered: false}
gist: >
  Reports results of Intel's second annual survey of 666 open source community members (Dec
  2023-Jan 2024), finding maintainer burnout as the top-cited challenge (45%), followed by
  documentation/onboarding (41%) and sustainability (37%). Also documents a decline in self-
  identified female respondents (15% to 7% year over year), continued strong engagement
  despite burnout (91% contributed vs 84% prior year), and growing interest in open source's
  role in AI innovation (82% rate it highly important). The piece is a corporate blog
  summary of survey findings rather than a peer-reviewed study, with no methodology detail
  on sampling or recruitment beyond an n and a date range.
claims:
  - text: "Maintainer burnout was the top-cited challenge among open source community survey respondents, selected by 45% (n=666), narrowly ahead of documentation/onboarding difficulties (41%) and sustainability concerns (37%)."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["burnout"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "Self-identified female respondents dropped sharply year over year, from 15% to 7%, while male respondents made up 79% of the sample, underscoring a persistent and worsening gender diversity gap in open source participation."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["sense-of-belonging"]
    predictors: ["inclusiveness"]
  - text: "Despite widely reported burnout, contribution activity increased: 91% of respondents said they had contributed to open source projects in the past year versus 84% the previous year, with about 4 in 10 contributing at least weekly."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["job-engagement", "retention"]
    predictors: ["open-source-maintenance", "community-engagement"]
population:
  who: "666 self-selected respondents to Intel's annual open source community survey, majority male (79%), late 30s, one-third US-based and two-thirds international"
  where: ["United States", "international (unspecified)"]
  when: "December 2023-January 2024"
  n: 666
  sector: ["open-source", "technology"]
  sample_notes: >
    Self-selected survey audience reached via Intel's open source community channels; no
    sampling frame, response rate, or representativeness analysis reported; some sub-
    questions (e.g. conference attendance) had much smaller n (~200).
limitation:
  primary: "No methodological detail is given on sampling frame, recruitment channel, or response rate, so results likely reflect a self-selected, Intel-affiliated audience rather than the broader open source population."
  others:
    - "Corporate blog format with no statistical testing, confidence intervals, or comparison of subgroup differences beyond simple percentages."
    - "Written by Intel staff with an evident promotional interest in favorable framing of Intel's open source involvement."
    - "Year-over-year comparisons (e.g. gender shift, contribution rate) may reflect sample composition changes rather than true population trends."
risk_of_bias: "high"
relevance_to_project: >
  Provides a large-sample (though non-random) data point that maintainer burnout is the
  single most commonly cited top challenge among open source contributors, directly
  supporting the SNH project's focus on maintainer burnout as a target outcome, and flags a
  widening gender-diversity gap as a related community-health signal worth tracking.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["survey", "cross-sectional"]
  population: ["open-source-maintainers", "software-developers"]
source:
  markdown: "Papers_Data/Articles/MD/Annual Intel Open Source Community Survey Results/Annual Intel Open Source Community Survey Results.md"
  pdf: "papers/Articles/Annual Intel Open Source Community Survey Results.pdf"
  notes: "no-doi: web article / no registered DOI found"
