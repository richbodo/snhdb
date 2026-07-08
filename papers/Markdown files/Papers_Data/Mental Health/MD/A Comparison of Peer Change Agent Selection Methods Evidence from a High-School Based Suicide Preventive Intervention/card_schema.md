id: "pickering-2022-a-comparison-of-peer-change-agent"
title: "A comparison of peer change agent selection methods: Evidence from a high-school based suicide preventive intervention"
authors:
  - "Pickering, Trevor A."
  - "Wyman, Peter A."
  - "Valente, Thomas W."
year: 2022
doi: "10.1186/s12889-022-13372-w"
venue: {type: "journal", name: "BMC Public Health", volume: 22, issue: 1, pages: null}
citation: "Pickering et al. (2022). A comparison of peer change agent selection methods: Evidence from a high-school based suicide preventive intervention. BMC Public Health, 22(1). https://doi.org/10.1186/s12889-022-13372-w"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using baseline social-network survey data from 5,746 students across 20 high schools
  implementing the Sources of Strength suicide-prevention program, this study compares the
  school staff's actual peer-leader selections against several theoretical, network-informed
  selection methods (opinion leadership, friendship-network centrality metrics, key-players
  algorithm, and hybrid combinations). It finds low overlap between adult-selected and
  network-optimal peer leader sets, systematic demographic trade-offs across methods, and
  that schools whose adult-selected leaders more closely matched network-informed sets saw
  greater diffusion of the intervention, especially peer-to-peer communication and media
  exposure.
claims:
  - text: "Adult-selected peer leaders (APL) had low concordance with theoretically-optimal peer leader sets identified from network data, ranging from 13.3% overlap with the Key Players method to 22.7% overlap with an influence-weighted hybrid method."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "sampling-method"]
  - text: "Selection method produced systematic demographic trade-offs: friendship-network-based selection (in-degree, closeness) produced peer leader sets that were more white and younger than the general student body, while the Key Players algorithm produced the most demographically representative sets across sex, race, age, and grade."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging"]
    predictors: ["network-structure", "inclusiveness", "sampling-method"]
  - text: "School-level concordance between adult-selected leaders and theoretical network-informed sets predicted intervention diffusion: a 1-percentage-point increase in Peer Opinion Leader concordance was associated with a 0.82 percentage-point increase in students reporting direct peer communication about the program (p<.001), and nearly all network-informed methods placed peer leaders closer than adult-selected leaders to at-risk students (suicidal ideation/attempt, network-peripheral, no trusted adult)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["communication", "suicidal-ideation", "help-seeking"]
    predictors: ["network-structure", "peer-mentoring", "intervention"]
population:
  who: "High-school students (grades 9-12) in schools implementing the Sources of Strength peer-led suicide prevention program, plus the subset of 429-459 students selected as adult-chosen peer leaders each school year"
  where: ["United States (New York, North Dakota)"]
  when: "2010-2013 (baseline enrollment across four intervention cohorts; diffusion assessed after first program year)"
  n: 5746
  sector: ["education", "youth-mental-health"]
  sample_notes: >
    20 high schools (of 40 in a larger effectiveness-implementation RCT) randomized to
    immediate implementation; schools in predominantly rural/small-town/micropolitan
    counties with above-average youth suicide rates; average survey enrollment 82.2% (range
    65.9-98.3%) of students; peer leaders were staff-nominated (up to 6 nominations per
    staff member) targeting 5-10% of students, with 83.2% of invited students enrolling with
    parent permission and youth assent.
limitation:
  primary: "The theoretical, network-informed peer leader sets were never actually implemented in schools -- the study only correlates hypothetical set concordance with observed diffusion, so causal claims about which selection method would improve diffusion are unverified."
  others:
    - "Adult selection of peer leaders followed no fully standardized algorithm, so APL sets may be unreproducible, limiting generalizability of concordance findings to other studies or contexts."
    - "School-level regression analyses of concordance and diffusion relied on only 20 school-level observations, limiting statistical power and precision."
    - "Important non-network determinants of diffusion (peer leader willingness, attitudes, persuasiveness, attendance, personality) were not measured and could confound the observed associations."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs how the SNH project might identify and recruit community 'peer leaders'
  or connectors for support and prevention efforts: it shows that intuitive, staff-driven
  selection under-uses available network information, that different network metrics
  (centrality vs. key-players vs. opinion leadership) trade off representativeness against
  closeness to at-risk/isolated members, and that a hybrid selection approach may best
  balance reach, diversity, and proximity to at-risk individuals -- a concrete, evidence-
  based method for designing peer-support or ambassador programs in remote/distributed
  communities.
tags:
  topic: ["suicide-prevention", "community-health", "social-support", "methodology"]
  method: ["longitudinal", "secondary-data", "network-analysis"]
  population: ["adolescents", "school-based", "at-risk-youth"]
source:
  markdown: "Papers_Data/Mental Health/MD/A Comparison of Peer Change Agent Selection Methods Evidence from a High-School Based Suicide Preventive Intervention/A Comparison of Peer Change Agent Selection Methods Evidence from a High-School Based Suicide Preventive Intervention.md"
  pdf: "papers/Mental Health/A Comparison of Peer Change Agent Selection Methods Evidence from a High-School Based Suicide Preventive Intervention.pdf"
  notes: null
