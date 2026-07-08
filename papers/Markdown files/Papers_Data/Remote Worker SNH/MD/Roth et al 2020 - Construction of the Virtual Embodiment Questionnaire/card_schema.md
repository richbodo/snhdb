id: "roth-2020-construction-of-the-virtual-embodiment-questionnaire"
title: "Construction of the Virtual Embodiment Questionnaire (VEQ)"
authors:
  - "Roth, Daniel"
  - "Latoschik, Marc Erich"
year: 2020
doi: "10.1109/tvcg.2020.3023603"
venue: {type: "journal", name: "IEEE Transactions on Visualization and Computer Graphics", volume: 26, issue: 12, pages: "3546-3556"}
citation: "Roth et al. (2020). Construction of the Virtual Embodiment Questionnaire (VEQ). IEEE Transactions on Visualization and Computer Graphics, 26(12), 3546-3556. https://doi.org/10.1109/tvcg.2020.3023603"
article_type: "methods"
method: {design: "scale-development", approach: "experiment", evidence_level: "moderate", preregistered: false}
gist: >
  The paper develops and psychometrically validates the Virtual Embodiment Questionnaire
  (VEQ), a 12-item, three-factor scale (body ownership, agency, perceived change in body
  schema) for VR avatar experiences, using confirmatory factor analysis on pooled data from
  three manipulation experiments (N=196) and a fourth latency/jitter validation study
  (N=22). The resulting scale fit the data well (SB chi-square(51)=52.50, p=.416,
  RMSEA=.013, CFI=.998) and showed acceptable reliability and greater sensitivity to agency
  manipulations than a prior rubber-hand-illusion-derived scale. It contributes a ready-to-
  use, freely available instrument for measuring how strongly a user experiences an avatar
  as their own body-relevant for any research on avatar-mediated presence or collaboration.
claims:
  - text: "A confirmatory factor analysis on N=196 (pooled across three VR manipulation experiments) confirmed a 12-item, three-factor structure of virtual embodiment (ownership, agency, change) with good model fit (SB chi-square(51)=52.50, p=.416, RMSEA=.013, 90% CI [.000,.052], SRMR=.047, robust CFI=.998) and acceptable internal consistency (Cronbach's alpha: ownership=.783, agency=.764, change=.765)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["social-presence"]
    predictors: ["embodiment"]
  - text: "In a repeated-measures validation study (N=22), simulated motion latency and latency jitter significantly reduced perceived agency (F(1.74,63.55)=7.50, p=.003, partial eta^2=.263) and ownership (F(3,63)=3.57, p=.024, partial eta^2=.138), but did not significantly affect the change factor; the largest latency (353ms) degraded agency/ownership more than a comparable latency jitter (~103ms) or a moderate fixed delay (207ms)."
    evidence: "rct"
    support_strength: "low-to-moderate"
    outcomes: ["embodiment"]
    predictors: ["technostress"]
  - text: "The VEQ agency subscale detected simulation-delay manipulations with greater sensitivity than a comparison scale adapted from rubber-hand-illusion research (Kalckert & Ehrsson), and VEQ factors correlated as expected with (self-)presence measures (e.g., ownership with general/spatial presence and realness) while remaining empirically discriminable from them, supporting convergent and discriminant validity."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["social-presence"]
    predictors: ["embodiment"]
population:
  who: "University students (mostly with prior VR experience) recruited to participate in lab-based VR embodiment experiments; four separate samples (n=50, 48, 70, 22) pooled for scale construction (N=196) and validation (N=22)"
  where: ["Germany"]
  when: null
  n: 218
  sector: ["academia"]
  sample_notes: >
    Convenience samples individually recruited through a university participant pool;
    participants excluded post hoc for tracking errors/technical problems; predominantly
    students, mostly with previous VR experience, gender-imbalanced in places (e.g., Study
    3: 46 female/24 male); not representative of general or remote-worker populations.
limitation:
  primary: "Authors themselves note the findings are limited by the specific mirror-based lab scenarios and the size/composition of the (largely student) samples, so generalization to other VR contexts, populations, or field settings is untested."
  others:
    - "The VEQ deliberately omits a self-location factor present in some competing embodiment frameworks, so it does not capture that dimension of embodiment."
    - "The validation (latency) study had only N=22 participants, limiting power for subtler effects and for confirming the null result on the 'change' factor."
    - "All embodiment inductions used a mirror/first-person avatar paradigm with fixed instructions; performance in non-mirror scenarios (games, activities, social multi-user settings) is untested."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a validated, freely available instrument (the VEQ) for measuring how strongly
  users experience an avatar as their own body in VR-directly usable if the SNH project
  studies avatar-mediated remote collaboration or virtual meeting spaces, since embodiment
  quality is a plausible predictor of social presence and interaction quality in such
  settings. It is a measurement/methods contribution rather than direct evidence about
  isolation, burnout, or turnover.
tags:
  topic: ["measurement", "social-presence", "methodology", "remote-work"]
  method: ["scale-development", "experiment", "cross-sectional"]
  population: ["students"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Roth et al 2020 - Construction of the Virtual Embodiment Questionnaire/Roth et al 2020 - Construction of the Virtual Embodiment Questionnaire.md"
  pdf: "papers/Remote Worker SNH/Roth et al 2020 - Construction of the Virtual Embodiment Questionnaire.pdf"
  notes: null
