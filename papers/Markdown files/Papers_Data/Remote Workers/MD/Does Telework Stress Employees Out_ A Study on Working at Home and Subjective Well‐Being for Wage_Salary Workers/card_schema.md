id: "song-2018-does-telework-stress-employees-out-a"
title: "Does Telework Stress Employees Out? A Study on Working at Home and Subjective Well-Being for Wage/Salary Workers"
authors:
  - "Song, Younghwan"
  - "Gao, Jia"
year: 2018
doi: "10.2139/ssrn.3301758"
venue: {type: "journal", name: "SSRN Electronic Journal", volume: null, issue: null, pages: null}
citation: "Song et al. (2018). Does Telework Stress Employees Out? A Study on Working at Home and Subjective Well-Being for Wage/Salary Workers. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3301758"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using individual fixed-effects models on 11,793 diary-day activity episodes from 3,962 US
  wage/salary workers in the 2010/2012/2013 American Time Use Survey Well-Being Modules,
  this paper finds that working at home has a net negative effect on instantaneous
  subjective well-being rather than the stress-relief benefit often claimed for telework.
  Bringing work home on weekdays is associated with lower happiness, and telework (on both
  weekdays and weekends/holidays) is associated with higher stress relative to working in
  the workplace, with effects concentrated among parents, especially fathers.
claims:
  - text: "In fixed-effects models, bringing work home on weekdays is associated with a 0.330-point drop in happiness (p<.05) relative to working in the workplace, and telework on weekdays is associated with a 0.298-point increase in stress (p<.05), on a 0-6 instantaneous affect scale."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "stress"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Telework on weekends/holidays is also associated with higher stress (0.494-point increase, p<.05) relative to working in the workplace, indicating no measurable stress benefit from working at home even outside normal business hours; the study finds no significant beneficial effect of any form of homeworking on any well-being measure."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["remote-work-intensity"]
  - text: "Effects are heterogeneous by parental status and gender: fathers bringing work home on weekdays report 0.585-point lower happiness, 0.350-point higher pain, and 0.314-point higher sadness (all p<.05), and 0.500-point higher stress when teleworking; mothers report lower stress but higher tiredness when bringing work home weekdays and lower happiness when teleworking weekdays, while childless workers show little difference on weekdays but childless females report higher stress (0.901, p<.05) when teleworking on weekends/holidays."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing", "work-life-balance"]
    predictors: ["boundary-management", "remote-work-intensity"]
population:
  who: "Full-time, non-self-employed US wage/salary workers aged 18-65 who reported at least one work episode on their diary day"
  where: ["United States"]
  when: "2010, 2012, and 2013 (American Time Use Survey Well-Being Modules)"
  n: 3962
  sector: ["general-workforce"]
  sample_notes: >
    11,793 activity episodes (up to 3 per respondent) from 3,962 respondents after dropping
    missing data and single-episode respondents; nationally representative ATUS sampling
    frame but very small subsamples for bringing-work-home episodes (as few as 51-179),
    especially in gender/parental-status subgroup analyses, limiting power for those
    breakdowns; only one respondent per household interviewed, so no couples in the sample.
limitation:
  primary: "Telework vs. bringing-work-home is inferred indirectly from commuting patterns rather than asked directly, so some episodes (especially on weekends/holidays) are likely misclassified between the two homeworking types."
  others:
    - "Individual fixed-effects models cannot rule out unobserved confounders that vary across the small number of within-day episodes, even though many activity-level controls are included."
    - "Subsample sizes for bringing-work-home episodes are very small (e.g., 51 weekend episodes), producing wide confidence intervals for several heterogeneity estimates."
    - "Findings are specific to full-time wage/salary workers and instantaneous (episode-level) affect on a single diary day, which may not generalize to sustained remote-work experience or to self-employed/gig workers."
risk_of_bias: "low"
relevance_to_project: >
  Provides quasi-causal (fixed-effects) evidence that remote/telework is associated with
  higher momentary stress and that informal after-hours homework reduces happiness, directly
  informing the SNH project's design assumption that flexibility alone does not guarantee
  well-being and that boundary-management supports (childcare, defined work hours,
  workspace) may be needed to offset telework's stress costs, particularly for parents.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing", "measurement"]
  method: ["fixed-effects", "secondary-data", "quantitative"]
  population: ["remote-workers", "parents", "gender-differences"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Does Telework Stress Employees Out_ A Study on Working at Home and Subjective Well‐Being for Wage_Salary Workers/Does Telework Stress Employees Out_ A Study on Working at Home and Subjective Well‐Being for Wage_Salary Workers.md"
  pdf: null
  notes: null
