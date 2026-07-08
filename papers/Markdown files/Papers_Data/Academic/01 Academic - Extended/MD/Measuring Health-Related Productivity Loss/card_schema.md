id: "mitchell-2011-measuring-health-related-productivity-loss"
title: "Measuring Health-Related Productivity Loss"
authors:
  - "Mitchell, Rebecca J."
  - "Bates, Paul"
year: 2011
doi: "10.1089/pop.2010.0014"
venue: {type: "journal", name: "Population Health Management", volume: 14, issue: 2, pages: "93-98"}
citation: "Mitchell et al. (2011). Measuring Health-Related Productivity Loss. Population Health Management, 14(2), 93-98. https://doi.org/10.1089/pop.2010.0014"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using Health Risk Appraisal survey data from over 1 million employed OptumHealth
  participants (2007-2009), this study used propensity-score matching to isolate the
  productivity impact of 13 chronic health conditions and 4 lifestyle health risks (e.g.,
  obesity, smoking, high blood pressure/cholesterol), measuring both absenteeism and
  presenteeism (via the Work Limitations Questionnaire). It found that employees with health
  conditions or high risk levels lost significantly more workdays to absence and reduced on-
  the-job performance than matched healthy controls, and monetized these losses to show they
  can rival or exceed direct medical costs, with depression ranking among the three
  costliest conditions for productivity.
claims:
  - text: "After propensity-score matching and regression adjustment, employees with a given health condition or health risk had productivity costs ranging from $15 to $1,601 more per year than matched employees without it; for a 10,000-employee company this implies nearly $3.8 million in additional annual productivity loss."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["health-status"]
  - text: "Cancer, bronchitis, and depression were among the top three health conditions ranked by annual productivity cost per person, and combined productivity costs across conditions equaled about $0.40 for every $1 of medical costs for an average-size employer."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "mental-health"]
    predictors: ["health-status"]
  - text: "Productivity loss showed a dose-response relationship with health burden: participants with 2+ health conditions averaged 3.0 absent days and 20.1 unproductive days per year versus 1.4 and 3.7 days for those with none, and participants at high risk (5+ risk factors) averaged 3.6 absent days and 28.9 unproductive days versus 1.6 and 5.1 for low-risk participants."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "wellbeing"]
    predictors: ["health-status"]
population:
  who: "Employed U.S. adults (ages 18-70) who completed employer-sponsored OptumHealth Health Risk Appraisal (HRA) surveys; a subgroup completed a second survey ~1 year later forming a matched-cohort sample used for cost analyses."
  where: ["United States"]
  when: "January 2007 to December 2009"
  n: 1000000
  sector: ["corporate", "occupational-health"]
  sample_notes: >
    Baseline sample of ~1.3 million HRA respondents narrowed to 1 million after
    age/completeness exclusions; ~260,000 also completed a follow-up survey and formed the
    cohort used for propensity-matched cost estimates. Sample drawn only from employers
    purchasing OptumHealth HRA services (77% white, 58% female, average age 42), which
    limits representativeness; all health measures (conditions, blood pressure, cholesterol,
    height/weight) were self-reported.
limitation:
  primary: "Monetization relies on an assumed wage multiplier (1.61) and extrapolation of 2-week presenteeism recall to annual estimates, and propensity-score matching cannot control for all confounders, so causal attribution of costs to specific conditions is uncertain."
  others:
    - "All health condition, risk factor, and biometric data (blood pressure, cholesterol, height, weight) were self-reported and not independently verified"
    - "Sample limited to employers who purchased OptumHealth HRA services, restricting generalizability across industries and job types"
    - "No direct linkage to actual medical claims data; medical cost comparisons used separate benchmark (ETG) data rather than the same participants' claims"
risk_of_bias: "medium"
relevance_to_project: >
  Offers a concrete, monetized method for quantifying how health conditions -- including
  depression, which ranked among the top three costliest for productivity -- translate into
  absenteeism and presenteeism losses, giving the SNH project a template and benchmark for
  building a cost/ROI case that mental-health and burnout-related interventions in
  remote/hybrid workplaces are not just wellbeing goods but financially material to
  employers.
tags:
  topic: ["mental-health", "wellbeing", "burnout", "measurement"]
  method: ["survey", "quasi-experimental"]
  population: ["employed-adults", "us-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Measuring Health-Related Productivity Loss/Measuring Health-Related Productivity Loss.md"
  pdf: "papers/Academic/01 Academic - Extended/Measuring Health-Related Productivity Loss.pdf"
  notes: null
