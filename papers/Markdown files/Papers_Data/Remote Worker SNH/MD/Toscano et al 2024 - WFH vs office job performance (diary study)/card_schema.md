id: "toscano-2025-the-influence-of-working-from-home"
title: "The Influence of Working from Home vs. Working at the Office on Job Performance in a Hybrid Work Arrangement: A Diary Study"
authors:
  - "Toscano, Ferdinando"
  - "González-Romá, Vicente"
  - "Zappalà, Salvatore"
year: 2025
doi: "10.1007/s10869-024-09970-7"
venue: {type: "journal", name: "Journal of Business and Psychology", volume: 40, issue: 2, pages: "497-512"}
citation: "Toscano et al. (2025). The Influence of Working from Home vs. Working at the Office on Job Performance in a Hybrid Work Arrangement: A Diary Study. Journal of Business and Psychology, 40(2), 497-512. https://doi.org/10.1007/s10869-024-09970-7"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  An 8-day diary study of 203 Italian municipal hybrid workers tests a JD-R mediation model
  comparing days working from home (WFH) to days at the office (WATO). It finds a positive
  motivational pathway (WFH raises concentration, which raises work engagement, which raises
  daily performance) but also a negative 'disengagement' pathway in which WFH raises social
  isolation, which lowers work engagement and thereby lowers performance; the hypothesized
  health-impairment pathway through isolation-driven tension was not supported, and the net
  daily effect of WFH on performance was small but positive.
claims:
  - text: "WFH (vs. WATO) had a statistically significant positive indirect relationship with daily job performance via daily concentration and daily work engagement (unstandardized indirect estimate = 0.03, SE = 0.008, 95% CI [0.015, 0.041]; partially standardized indirect effect, PSIE = 0.04), supporting a motivational mechanism."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "job-engagement"]
    predictors: ["remote-work-intensity"]
  - text: "A 'disengagement effect' was found: WFH had a significant negative indirect relationship with daily job performance via daily social isolation and daily work engagement (indirect estimate = -0.01, SE = 0.003, 95% CI [-0.015, -0.005]; PSIE = -0.01), while the hypothesized isolation-to-tension health-impairment pathway was not statistically significant (95% CI included zero)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "job-engagement", "isolation"]
    predictors: ["isolation", "remote-work-intensity"]
  - text: "The net effect of WFH on daily job performance was positive because the significant positive indirect effect (via concentration and engagement, plus a direct WFH-to-engagement path) outweighed the significant negative one (via isolation and engagement); combined PSIE across the significant paths was 0.08-0.09, described by the authors as small but non-trivial for a daily-level effect."
    evidence: "longitudinal"
    support_strength: "low-to-moderate"
    outcomes: ["performance"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "Civil servants in an Italian municipality working a hybrid arrangement (1-2 WFH days/week), varied occupations including administrative staff, accountants, architects, engineers, police officers, librarians, and educators"
  where: ["Italy"]
  when: "June 2021 (8 consecutive working days)"
  n: 203
  sector: ["public-sector", "government"]
  sample_notes: >
    751 valid daily responses (503 office days, 248 WFH days) from 203 participants, average
    3.70 days/participant; response rate 46.2%; mean age 48.5 (SD 9.75), 74.3% women, 58.3%
    college-educated, mean tenure 16.1 years; WFH days were scheduled at employee-supervisor
    discretion, not random assignment.
limitation:
  primary: "Despite the multi-day diary design, all mediators and the outcome were measured concurrently at the same daily time point via self-report, so the study is effectively cross-sectional at the day level and cannot support causal claims about the mediation pathways."
  others:
    - "Single-item measures were used for daily tension and daily job concentration, which the authors defend but which remain a validity concern."
    - "All variables (including self-reported job performance) came from the same source (employees), raising common-method variance concerns, and WFH days were not randomly assigned but chosen jointly with supervisors."
    - "Sample is limited to one public-sector municipality with a below-target response rate (46.2%), limiting generalizability to other sectors or work contexts."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a concrete, quantified dual-pathway model relevant to SNH's remote-work design
  problem: it shows WFH-induced social isolation has a measurable, statistically significant
  negative effect on work engagement and downstream performance (a 'disengagement' mechanism
  distinct from stress/tension), which is direct evidence that organizations should target
  daily social-isolation mitigation (virtual coffee breaks, structured check-ins) even when
  WFH's net productivity effect is positive.
tags:
  topic: ["remote-work", "hybrid-work", "isolation", "job-engagement", "productivity"]
  method: ["diary-study", "survey", "mediation-analysis"]
  population: ["public-sector", "hybrid-workers"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Toscano et al 2024 - WFH vs office job performance (diary study)/Toscano et al 2024 - WFH vs office job performance (diary study).md"
  pdf: "papers/Remote Worker SNH/Toscano et al 2024 - WFH vs office job performance (diary study).pdf"
  notes: null
