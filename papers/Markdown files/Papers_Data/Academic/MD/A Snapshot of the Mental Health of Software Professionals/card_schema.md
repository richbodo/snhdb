id: "almeida-2024-a-snapshot-of-the-mental-health"
title: "A Snapshot of the Mental Health of Software Professionals"
authors:
  - "Almeida, Eduardo  Santana de"
  - "Nunes, Ingrid  Oliveira de"
  - "Oliveira, Raphael  Pereira de"
  - "Carvalho, Michelle  Larissa Luciano"
  - "Brunoni, André Russowsky"
  - "Rong, Shiyue"
  - "Ahmed, Iftekhar"
year: 2024
doi: "10.2139/ssrn.4849630"
venue: {type: "preprint", name: null, volume: null, issue: null, pages: null}
citation: "Almeida et al. (2024). A Snapshot of the Mental Health of Software Professionals.. https://doi.org/10.2139/ssrn.4849630"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A cross-sectional survey of 500 software professionals from 35 countries found that 30.2%
  had been diagnosed with a mental health disorder (past or current), with anxiety (20.6%)
  and depression (14.8%) most common, and that 25.2% scored as having moderately severe or
  severe depression on the PHQ-9. Using Spearman correlations, the study identifies work-
  nature, work-environment, and work-schedule factors (freelance work type, the test-
  engineer role, home-office work before COVID-19, unrealistic deadlines, abrupt task
  changes, and working more hours than expected) that are associated with a history of
  mental health disorders, while a healthy relationship with colleagues is associated with
  lower odds. It also documents that leisure, social, and family time dropped significantly
  during the COVID-19 pandemic and was already lower among professionals with a history of
  mental health disorders.
claims:
  - text: "30.2% (151/500) of software professionals reported being diagnosed with a mental health disorder in the past or currently; anxiety (20.6%, 103/500) and depression (14.8%, 74/500) were most common, and 25.2% (126/500) scored as moderately severe or severe depression on the PHQ-9, including 19.4% of those with no prior diagnosed history."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "depression", "anxiety"]
    predictors: []
  - text: "Freelance work type (Spearman rho=0.09, p=0.03) and the test-engineer role (rho=0.15, p=0.0004) were positively associated with a history of mental health disorders, while working for an organization was negatively associated (rho=-0.10, p=0.02); organization size and team size showed no significant correlation."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health"]
    predictors: ["remote-work-intensity", "workload"]
  - text: "Working more actual hours than expected (Cohen's d=-0.27 all respondents; -0.21 for those with mental health history), unrealistic deadlines, abruptly changed tasks, and pre-pandemic home-office work were each significantly correlated with a history of mental health disorders, whereas a strongly agreed healthy relationship with colleagues was associated with lower odds (rho=-0.10, p=0.02); leisure, social activity, hobby, and family time all declined significantly during COVID-19 (largest effect: social activities, Cohen's d=1.97)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "burnout", "work-life-balance"]
    predictors: ["workload", "remote-work-intensity", "team-cohesion", "boundary-management"]
population:
  who: "500 software professionals (developers, architects, project managers, test engineers, and others) recruited via social media, convenience sampling, and snowballing"
  where: ["Brazil", "Germany", "USA", "France", "31 other countries (35 total)"]
  when: "May-July 2021"
  n: 500
  sector: ["software-industry", "open-source", "private-organization", "freelance"]
  sample_notes: >
    Convenience/snowball sample skewed heavily toward Brazil (74.8%); 82% male; anonymous,
    self-selected, non-probability recruitment via authors' personal networks, so not
    representative of the global software workforce; 503 raw responses with 3 disqualified
    (2 non-consenting, 1 duplicate).
limitation:
  primary: "Convenience/snowball sampling via authors' personal networks and social media produces a non-representative, geographically skewed sample (nearly 75% Brazil, 82% male), limiting generalizability despite the large N."
  others:
    - "Cross-sectional design precludes causal claims about which work characteristics trigger mental health disorders versus merely co-occurring with them."
    - "Self-reported diagnosis history and PHQ-9 screening are not clinician-verified diagnoses."
    - "Many correlations, while statistically significant, have small effect sizes (rho often below 0.15), so practical significance is limited."
risk_of_bias: "medium"
relevance_to_project: >
  Provides base-rate evidence (30.2% disorder prevalence, 25.2% moderate-to-severe
  depression by PHQ-9) and specific workplace predictors (freelance status, unrealistic
  deadlines, abrupt task changes, excess hours, home-office work, colleague relationship
  quality) that the SNH project can use to prioritize which remote-work and community
  stressors to target with interventions, and to justify measuring colleague relationship
  quality and workload predictability as levers for wellbeing.
tags:
  topic: ["mental-health", "remote-work", "burnout", "work-life-balance", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["software-professionals", "open-source", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/MD/A Snapshot of the Mental Health of Software Professionals/A Snapshot of the Mental Health of Software Professionals.md"
  pdf: "papers/Academic/A Snapshot of the Mental Health of Software Professionals.pdf"
  notes: null
