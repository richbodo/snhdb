id: "anon-2010-supplemental-material-for-a-general-multilevel"
title: "Supplemental Material for A General Multilevel SEM Framework for Assessing Multilevel Mediation"
authors:
year: 2010
doi: "10.1037/a0020141.supp"
venue: {type: "journal", name: "Psychological Methods", volume: null, issue: null, pages: null}
citation: "Psychological Methods (2010). Supplemental Material for A General Multilevel SEM Framework for Assessing Multilevel Mediation. Psychological Methods. https://doi.org/10.1037/a0020141.supp"
article_type: "methods"
method: {design: "methods", approach: "modelling", evidence_level: "reference", preregistered: false}
gist: >
  This is a statistics methods paper (Preacher, Zyphur, & Zhang, 2010, Psychological
  Methods) that develops a general multilevel structural equation modeling (MSEM) framework
  for testing mediation hypotheses in nested/clustered data, such as individuals nested in
  teams or organizations. It shows analytically that conventional multilevel modeling (MLM)
  approaches to mediation conflate within-group and between-group effects and cannot handle
  designs where the mediator or outcome is measured at the group level, and it demonstrates
  with three re-analyzed datasets that MSEM can yield substantively different conclusions
  than conventional MLM/two-step approaches, including finding a significant indirect effect
  of perceived transformational leadership on team performance via team satisfaction where a
  standard aggregation approach found none. For the SNH project it functions as the
  reference method for correctly testing multilevel mediation hypotheses (e.g., team-level
  leadership or culture predicting individual burnout or turnover via individual-level
  social support or engagement) without the conflation bias inherent to naive MLM mediation
  tests.
claims:
  - text: "Standard MLM approaches to mediation with nested data conflate the between-group and within-group components of the indirect effect into a single biased slope, and the common group-mean-centering fix (the 'unconflated multilevel model,' UMM) still yields a biased between-group indirect effect when cluster sizes are small or a predictor's intraclass correlation (ICC) is low; the paper derives the expected bias analytically (Eq. 1-2)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement-bias"]
    predictors: ["sampling-method"]
  - text: "Reanalyzing survey data from 79 team leaders and 429 team members at a Chinese telecom customer-service center, MSEM found a significant indirect effect of leader-reported shared vision on member-reported team potency via leader identification with the team (indirect effect = .218, 90% CI [0.055, 0.432]), a larger and less precise estimate than the conventional two-step OLS+MLM approach applied to the identical data (.146, p < .05, 90% CI [0.044, 0.269])."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["leadership-style", "team-cohesion"]
  - text: "Reanalyzing the same team dataset for an upward (bottom-up) 1-1-2 mediation model, MSEM found a significant indirect effect of members' perceived transformational leadership on manager-rated team performance via team satisfaction (a x b = .697, 90% CI [0.022, 1.459]), whereas the conventional two-step aggregation approach on the identical data found no significant effect (a x b = .053, p < .85), showing that method choice alone can reverse a mediation study's substantive conclusion."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "job-satisfaction"]
    predictors: ["leadership-style"]
population:
  who: "Not a substantive study population; the paper's target audience is quantitative researchers testing multilevel mediation hypotheses. Its three illustrative reanalyses use: (1) 2,993 sixth-grade students nested in 126 teachers from the Michigan Study of Adolescent Life Transitions (1983-1985); (2) and (3) 429 team members nested in 79 team leaders at a Chinese telecommunications customer-service center."
  where: ["USA", "China"]
  when: "1983-1985 (Example 1, MSALT); data period unreported for Examples 2-3 (customer service center dataset)"
  n: null
  sector: ["education", "telecommunications"]
  sample_notes: >
    The datasets are re-used purely to demonstrate the MSEM technique, not to test SNH-
    relevant hypotheses; no response-rate or representativeness information is given, and
    results should not be read as generalizable substantive findings about leadership,
    teams, or students.
limitation:
  primary: "As a statistical methods paper, its 'results' are illustrative model comparisons on datasets unrelated to social network health (student achievement, team potency, leadership) rather than tests of loneliness, isolation, burnout, or turnover, so its relevance to the project is entirely methodological (how to correctly analyze nested SNH data), not substantive."
  others:
    - "The proposed MSEM framework cannot easily accommodate more than two hierarchical levels and cannot use restricted maximum likelihood estimation for small samples."
    - "Confidence-interval methods for MSEM indirect effects (e.g., the parametric bootstrap used here) were novel and less validated at time of publication than single-level mediation CI methods."
    - "The authors' own examples show that 2-2-1 and 1-1-2 indirect-effect estimates are highly sensitive to modeling choice (MSEM vs. two-step/aggregation), so applied use requires careful, theory-driven specification to avoid analogous over- or under-estimation of effects."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Provides the statistical framework the project would need to correctly test multilevel
  mediation hypotheses common in SNH research -- e.g., whether team-level leadership style
  or organizational culture affects individual burnout or turnover via individual-level
  social support, isolation, or engagement -- without the within/between conflation bias
  that its own examples show can flip a mediation study's substantive conclusion
  (significant vs. null).
tags:
  topic: ["methodology", "measurement"]
  method: ["structural-equation-modeling", "multilevel-modeling", "quantitative"]
  population: ["students", "teams", "employees"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/A General Multilevel SEM Framework for Assessing Multilevel Mediation/A General Multilevel SEM Framework for Assessing Multilevel Mediation.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/A General Multilevel SEM Framework for Assessing Multilevel Mediation.pdf"
  notes: null
