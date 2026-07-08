id: "posel-2021-job-loss-and-mental-health-during"
title: "Job loss and mental health during the COVID-19 lockdown: Evidence from South Africa"
authors:
  - "Posel, Dorrit"
  - "Oyenubi, Adeola"
  - "Kollamparambil, Umakrishnan"
year: 2021
doi: "10.1371/journal.pone.0249352"
venue: {type: "journal", name: "PLOS ONE", volume: 16, issue: 3, pages: "e0249352"}
citation: "Posel et al. (2021). Job loss and mental health during the COVID-19 lockdown: Evidence from South Africa. PLOS ONE, 16(3), e0249352. https://doi.org/10.1371/journal.pone.0249352"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using two waves of South Africa's NIDS-CRAM telephonic panel survey during the COVID-19
  lockdown, this study exploits the pandemic's exogenous job losses as a natural experiment
  to estimate the effect of job loss and furlough on depressive symptoms (PHQ-2). Adults who
  retained employment reported significantly lower depression scores than those who lost
  jobs, with the protective effect of employment growing the longer it was retained, while
  furlough (having a job to return to but no current work or pay) conferred no mental-health
  benefit at all. Paid leave, by contrast, was strongly protective, suggesting that
  continued income rather than job attachment per se buffers mental health during economic
  shocks.
claims:
  - text: "Adults who retained employment in Wave 1 were 5.1 percentage points more likely to report no depressive symptoms than those who lost their jobs, rising to a further 6 percentage points more likely if they also retained employment in Wave 2, indicating the mental-health benefit of employment compounds over time."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["intervention"]
  - text: "Being furloughed (not working, not earning, but with a job to return to) showed no significant relationship with PHQ-2 depression scores compared to job loss, meaning the mere expectation of future work provided no measurable psychological protection."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["workload"]
  - text: "Adults on paid leave in Wave 2 were about 10 percentage points less likely than those who had lost their job to report no depressive symptoms, and paid leave produced significantly lower depression scores even relative to actively working adults (chi-square = 8.02, p < 0.02), indicating continued income protects mental health more than job status alone."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["social-support"]
population:
  who: "Adults aged 18+ in South Africa who were employed immediately before the COVID-19 hard lockdown, re-interviewed in both waves of the NIDS-CRAM rapid mobile survey with complete data on key variables"
  where: ["South Africa"]
  when: "May-August 2020 (NIDS-CRAM Waves 1-2), with baseline mental health data from NIDS 2017"
  n: 2213
  sector: ["general-population", "mixed-employment"]
  sample_notes: >
    Sample drawn from the 2017 National Income Dynamics Study (NIDS) panel via stratified
    batch sampling; Wave 1 surveyed 7073 adults, Wave 2 re-interviewed 5676 (80.2% response
    rate); analytic sample restricted to the 2213 pre-lockdown employed adults with non-
    missing data across both waves. No survey weights used (authors treat estimates as
    sample-based, not population-representative); telephonic interviews may still under-
    represent those without phone access.
limitation:
  primary: "Mental health measures are not directly comparable across time points: NIDS 2017 used the CES-D 10 while NIDS-CRAM Wave 2 used the abbreviated PHQ-2, precluding individual fixed-effects models or before/after comparisons of the same depression instrument."
  others:
    - "The 2-item PHQ-2 is a coarse screener that is less sensitive to variation in depression severity than the full PHQ-9 or CES-D 10, likely underestimating true symptom severity."
    - "No survey weights were applied, so estimates are sample-based rather than nationally representative, despite the underlying panel's stratified design."
    - "Observation window covers only the first few months of lockdown (through August 2020), limiting inference about longer-term mental health trajectories."
risk_of_bias: "low"
relevance_to_project: >
  Provides a rare quasi-experimental (exogenous shock) estimate of how job loss versus
  continued income affects depression, directly informing SNH's evidence base on
  economic/employment precarity as a predictor of mental-health decline; the finding that
  furlough (job security without income or activity) offers no protection is relevant to
  designing remote-work and community interventions that address income/activity continuity,
  not just formal job status.
tags:
  topic: ["mental-health", "wellbeing"]
  method: ["longitudinal", "survey"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa.md"
  pdf: "papers/Academic/01 Academic - Extended/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa.pdf"
  notes: null
