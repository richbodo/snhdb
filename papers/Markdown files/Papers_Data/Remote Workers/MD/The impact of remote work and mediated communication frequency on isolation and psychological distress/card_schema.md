id: "van-2022-the-impact-of-remote-work-and"
title: "The impact of remote work and mediated communication frequency on isolation and psychological distress"
authors:
  - "Van Zoonen, Ward"
  - "Sivunen, Anu E."
year: 2022
doi: "10.1080/1359432x.2021.2002299"
venue: {type: "journal", name: "European Journal of Work and Organizational Psychology", volume: 31, issue: 4, pages: "610-621"}
citation: "Van Zoonen et al. (2022). The impact of remote work and mediated communication frequency on isolation and psychological distress. European Journal of Work and Organizational Psychology, 31(4), 610-621. https://doi.org/10.1080/1359432x.2021.2002299"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A three-wave cross-lagged panel survey of Finnish employees during the COVID-19 pandemic
  finds that remote work frequency increases perceived physical isolation over time, while
  frequency of mediated (ICT) communication with colleagues reduces it, and that these two
  effects are independent rather than interacting. The study also finds a reciprocal,
  bidirectional relationship between isolation and psychological distress: isolation
  predicts later distress and distress also predicts later isolation, supporting a 'strain-
  effect' alongside the more commonly hypothesized 'stressor-effect.'
claims:
  - text: "Remote work frequency at T1 significantly increased isolation at T2 (B = 0.121, 95% CI [.022, .218], p = .024), and remote work at T2 increased isolation at T3 (B = 0.187, 95% CI [.080, .294], p = .001), supporting the hypothesis that remote work frequency drives later isolation."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation"]
    predictors: ["remote-work-intensity"]
  - text: "Mediated communication frequency reduced isolation across waves (T1->T2: B = -0.155, 95% CI [-.260, -.051], p = .005; T2->T3: B = -0.131, 95% CI [-.253, -.018], p = .022), but did not moderate the remote-work-to-isolation effect (interaction ns at both lags), indicating remote work and communication frequency act as independent, opposing predictors of isolation rather than interacting."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation", "communication"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Isolation and psychological distress showed a reciprocal cross-lagged relationship: isolation at T1 increased distress at T2 (B = 0.032, p = .030) and isolation at T2 increased distress at T3 (B = 0.030, p = .050), while distress at T1 also increased isolation at T2 (B = 0.142, p = .050) and distress at T2 increased isolation at T3 (B = 0.204, p = .003); remote work's effect on distress at T3 and mediated communication's effect on distress were both significant indirect (mediated-through-isolation) effects."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation", "mental-health", "stress"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "Finnish employees recruited via convenience sampling (labour unions, ministries) during the first COVID-19 lockdown, surveyed across three waves; analytic sample completed all three waves"
  where: ["Finland"]
  when: "March 2020 - October 2020"
  n: 1164
  sector: ["public-administration", "professional-services", "information-communications", "education", "manufacturing"]
  sample_notes: >
    Initial T1 response 5,452; T2 response rate 34.76% of T1 (59.5% of invited, n=1,895); T3
    response rate 21.35% of T1 (61.42% of invited, n=1,164 retained for analysis).
    Predominantly female (76.6%), mean age 46.45, mean tenure 11.07 years; only 11.7%
    managers. Little's MCAR test indicated missingness was not completely at random, though
    non-response analyses found no significant differences in study constructs or model
    relationships between panel completers and dropouts.
limitation:
  primary: "Isolation was measured only as physical/perceived-separation isolation using a 4-item scale adapted from Orhan et al. (2016); other dimensions of isolation (informational, professional, social) that prior work shows can behave differently were not assessed."
  others:
    - "Unequal time lags between waves (short T1-T2, longer T2-T3, driven by pandemic timeline logistics rather than theory) complicate comparison of effect sizes across lags."
    - "No measures of task interdependence, perceived autonomy/control, or how synchronously vs. asynchronously the communication technologies were actually used."
    - "Strict longitudinal measurement invariance could not be established, limiting comparison of latent factor means across waves; all measures were self-reported at every wave, raising (though empirically mitigated) common-method-bias concerns."
risk_of_bias: "medium"
relevance_to_project: >
  Provides longitudinal, causally-ordered (cross-lagged) evidence that remote work frequency
  and ICT communication frequency have independent, opposing effects on physical isolation,
  and that isolation and psychological distress reinforce each other bidirectionally over
  time -- directly informing SNH's choice of isolation/distress measures and its rationale
  for prioritizing communication-frequency interventions (e.g., structured check-ins) as a
  distinct lever from simply reducing remote-work days.
tags:
  topic: ["remote-work", "isolation", "mental-health", "wellbeing"]
  method: ["longitudinal", "survey", "cross-lagged-panel"]
  population: ["remote-workers", "finland", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The impact of remote work and mediated communication frequency on isolation and psychological distress/The impact of remote work and mediated communication frequency on isolation and psychological distress.md"
  pdf: "papers/Remote Workers/The impact of remote work and mediated communication frequency on isolation and psychological distress.pdf"
  notes: null
