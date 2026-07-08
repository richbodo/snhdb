id: "miyake-2021-job-stress-and-loneliness-among-remote"
title: "Job stress and loneliness among remote workers"
authors:
  - "Miyake, Fuyu"
  - "Odgerel, Chimed-Ochir"
  - "Hino, Ayako"
  - "Ikegami, Kazunori"
  - "Nagata, Tomohisa"
  - "Tateishi, Seiichiro"
  - "Tsuji, Mayumi"
  - "Matsuda, Shinya"
  - "Ishimaru, Tomohiro"
year: 2021
doi: "10.1101/2021.05.31.21258062"
venue: {type: "preprint", name: null, volume: null, issue: null, pages: null}
citation: "Miyake et al. (2021). Job stress and loneliness among remote workers.. https://doi.org/10.1101/2021.05.31.21258062"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This nationwide Japanese survey of 4,052 remote desk workers during the COVID-19 pandemic
  found that working remotely 4+ days per week was moderately associated with loneliness
  (AOR=1.60), while low co-worker support (AOR=4.06) and low supervisor support (AOR=2.49)
  were strongly associated with loneliness. High psychological job demands were also linked
  to loneliness (AOR=2.04), but decision latitude was not, suggesting that social support
  from colleagues matters more for preventing remote-work loneliness than the sheer amount
  of remote work or job control.
claims:
  - text: "Remote workers with low co-worker support had far greater odds of feeling lonely than those with high co-worker support (AOR=4.06, 95% CI 2.82-5.84, P<0.001), the strongest predictor in the model."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support"]
  - text: "Low supervisor support was also strongly associated with loneliness (AOR=2.49, 95% CI 1.79-3.47, P<0.001), though the association was weaker than for co-worker support."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support", "leadership-style"]
  - text: "Frequency of remote work (4+ days/week vs. 1 day/week) was moderately associated with loneliness (AOR=1.60, 95% CI 1.04-2.46, P=0.033), and high psychological job demands were associated with greater loneliness (AOR=2.04, 95% CI 1.39-2.99, P<0.001), while decision latitude showed no significant association."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["remote-work-intensity", "workload"]
population:
  who: "Full-time Japanese desk workers doing remote work during the COVID-19 pandemic, recruited from a larger nationwide internet survey (CORoNaWork Project)"
  where: ["Japan"]
  when: "December 2020"
  n: 4052
  sector: ["general-workforce"]
  sample_notes: >
    Subsample of 4,052 remote desk workers drawn from 27,036 eligible respondents (33,087
    originally sampled) via cluster sampling stratified by sex, job type, and region based
    on COVID-19 incidence data; online self-administered survey, so generalizability to non-
    internet users is limited; loneliness measured with a single UCLA Loneliness Scale item
    (yes/no), which is a coarse binary measure.
limitation:
  primary: "Cross-sectional design precludes causal inference; reverse causality (e.g., lonely workers avoiding remote work, or vice versa) cannot be ruled out, though authors argue employees had limited choice over telework frequency during the pandemic."
  others:
    - "Loneliness assessed via a single yes/no question rather than a validated multi-item scale, limiting measurement precision and only capturing presence/absence rather than severity."
    - "Internet-based sampling and voluntary participation raise generalizability concerns, and the pandemic context (state-of-emergency conditions, forced telework) may limit applicability to routine/non-crisis remote work."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantified, adjusted effect sizes showing that co-worker and supervisor support
  are far stronger predictors of remote-worker loneliness than remote-work frequency itself,
  directly informing SNH's prioritization of peer/manager support interventions over simply
  limiting remote-work days as a loneliness-prevention lever.
tags:
  topic: ["remote-work", "loneliness", "social-support", "isolation", "mental-health"]
  method: ["cross-sectional", "survey"]
  population: ["remote-workers", "japan", "desk-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Job Stress and Loneliness Among Remote Workers/Job Stress and Loneliness Among Remote Workers.md"
  pdf: "papers/Remote Workers/Job Stress and Loneliness Among Remote Workers.pdf"
  notes: null
