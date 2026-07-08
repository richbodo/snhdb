id: "baltes-2022-sampling-in-software-engineering-research-a"
title: "Sampling in software engineering research: a critical review and guidelines"
authors:
  - "Baltes, Sebastian"
  - "Ralph, Paul"
year: 2022
doi: "10.1007/s10664-021-10072-8"
venue: {type: "journal", name: "Empirical Software Engineering", volume: 27, issue: 4, pages: null}
citation: "Baltes et al. (2022). Sampling in software engineering research: a critical review and guidelines. Empirical Software Engineering, 27(4). https://doi.org/10.1007/s10664-021-10072-8"
article_type: "methods"
method: {design: "review-critical", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  A critical review of 120 top-venue software engineering papers (2014-2019) finds that
  purposive (73.0%) and convenience (11.3%) sampling dominate, while probability sampling
  appears in only 8.3% of the 210 coded sampling stages, and nearly a quarter of stages
  never explain how the sample was obtained. Baltes and Ralph diagnose this as a
  'generalizability crisis' rooted in the near-total absence of usable sampling frames for
  software engineering phenomena, and synthesize an extensive primer plus concrete
  guidelines for researchers and reviewers on describing, defending, and evaluating sampling
  honestly instead of overselling representativeness.
claims:
  - text: "Across 210 sampling stages coded from 120 full papers in ICSE, FSE, TSE and TOSEM (2014-2019), purposive sampling was used in 149 stages (73.0%) and convenience sampling in 23 (11.3%), while probability sampling (simple random or stratified random) accounted for only 17 stages (8.3%); 49 stages (24.0%) did not explain the sampling strategy at all."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
  - text: "Predominantly quantitative studies outnumbered predominantly qualitative studies 126 to 16 among the 144 studies analyzed, and code artifacts were the most common unit of observation (132 of 204 sampling stages, 64.7%) versus people (37, 18.1%) or non-code artifacts (33, 16.2%)."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
  - text: "86 of 120 articles offered some justification for sample quality, most commonly asserting the sample was 'real-world' (29 articles), 'large' (16), 'representative' (13), or 'diverse' (8), frequently without explaining the actual sampling procedure used to obtain it."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
population:
  who: "120 full research papers (144 reported studies, 210 sampling stages) drawn via stratified random sampling (5 papers per venue-year) from four A* software engineering venues; also the general population of software engineering researchers addressed by the guidelines."
  where: []
  when: "2014-2019"
  n: 120
  sector: ["academia"]
  sample_notes: >
    Sampling frame restricted to full technical-track papers in ICSE, FSE, TSE and TOSEM
    (1,830 papers); coding was manual, done primarily by the first author with second-author
    audit of ambiguous cases; results are explicitly stated to generalize only to high-
    quality, English-language SE research at these four venues, not to SE research
    generally.
limitation:
  primary: "The review's evidentiary base is limited to four top-tier venues (ICSE, FSE, TSE, TOSEM) over six years, so findings may not generalize to other outlets, workshops, older research, or future methodological trends."
  others:
    - "Coding of sampling technique, methodology, and units of observation required subjective interpretation, mitigated only by second-author audit of ambiguous cases rather than full independent double-coding."
    - "The authors explicitly frame this as a purposive 'critical review' rather than a systematic review, so it deliberately analyzes a sample of primary studies rather than the full population of SE research."
risk_of_bias: "medium"
relevance_to_project: >
  Because SNH draws heavily on software-engineering research about open-source maintainers
  and remote developer communities, this paper's finding that 92% of top-venue SE sampling
  stages are non-probability (purposive/convenience) and often unexplained gives the project
  a concrete basis for weighing the generalizability of OSS/maintainer-burnout studies cited
  elsewhere in the corpus, and its guidelines (state the sampling algorithm, avoid
  overselling representativeness, match sampling strategy to epistemology) are directly
  applicable if SNH conducts its own developer or maintainer sampling.
tags:
  topic: ["methodology", "measurement", "open-source"]
  method: ["review-critical", "secondary-data"]
  population: ["academia"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Sampling in Software Engineering Research A Critical Review and Guidelines/Sampling in Software Engineering Research A Critical Review and Guidelines.md"
  pdf: "papers/Academic/01 Academic - Extended/Sampling in Software Engineering Research A Critical Review and Guidelines.pdf"
  notes: null
