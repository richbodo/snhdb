id: "brown-2008-methods-for-testing-theory-and-evaluating"
title: "Methods for testing theory and evaluating impact in randomized field trials: Intent-to-treat analyses for integrating the perspectives of person, place, and time"
authors:
  - "Brown, C. Hendricks"
  - "Wang, Wei"
  - "Kellam, Sheppard G."
  - "Muthén, Bengt O."
  - "Petras, Hanno"
  - "Toyinbo, Peter"
  - "Poduska, Jeanne"
  - "Ialongo, Nicholas"
  - "Wyman, Peter A."
  - "Chamberlain, Patricia"
  - "Sloboda, Zili"
  - "MacKinnon, David P."
  - "Windham, Amy"
year: 2008
doi: "10.1016/j.drugalcdep.2007.11.013"
venue: {type: "journal", name: "Drug and Alcohol Dependence", volume: 95, issue: null, pages: "S74-S104"}
citation: "Brown et al. (2008). Methods for testing theory and evaluating impact in randomized field trials: Intent-to-treat analyses for integrating the perspectives of person, place, and time. Drug and Alcohol Dependence, 95, S74-S104. https://doi.org/10.1016/j.drugalcdep.2007.11.013"
article_type: "methods"
method: {design: "case-study", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methodology paper by the Prevention Science and Methodology Group establishes
  standards for intent-to-treat (ITT) analysis in multilevel, group-randomized field trials
  (RFTs), extending pharmaceutical-trial ITT conventions to designs where randomization
  occurs at classroom, school, district, or county level. Drawing on six real RFTs
  (including the Baltimore Prevention Program's Good Behavior Game and the Georgia
  Gatekeeper suicide-prevention training trial), the authors specify rules for defining the
  analytic denominator, classifying mobile/late-entering subjects, and handling missing
  longitudinal data (FIML, multiple imputation), then present growth mixture models (GMM)
  and generalized additive mixed models (GAMM) for detecting who benefits from an
  intervention, for how long, and under what contextual conditions. It contributes a
  reusable analytic and reporting framework rather than a single substantive finding about
  social connection.
claims:
  - text: "Two defensible but distinct ITT denominator rules are needed for group-randomized trials: (1) restrict to subjects present at the start of the intervention period, which protects against late entrants being informatively assigned to condition but limits sample size, versus (2) include all subjects who enter throughout the intervention period, which maximizes sample and generalizability but risks bias if late entrants are non-randomly steered into conditions (e.g., principals disproportionately placed late-entering aggressive children into Good Behavior Game classrooms in the First Generation Baltimore Prevention Program trial)."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: []
    predictors: ["sampling-method"]
  - text: "In the Georgia Gatekeeper suicide-prevention training trial, ITT impact analyses of school staff outcomes (knowledge, attitudes, referral behavior) showed somewhat smaller training effects than parallel 'as-treated' analyses that used staff's actual (not intended) training condition, illustrating the conservative bias built into ITT estimates when compliance/exposure is imperfect."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["help-seeking"]
    predictors: ["intervention", "peer-mentoring"]
  - text: "Standard missing-data handling of last-observation-carried-forward (LOCF), still common in pharmaceutical ITT submissions, is statistically inefficient and introduces bias and misleadingly precise standard errors; the authors instead recommend full-information maximum likelihood or multiple imputation, both of which require only a missing-at-random assumption and were demonstrated on a two-stage Conduct Disorder diagnostic follow-up in the First Generation Baltimore Prevention Program trial."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: []
    predictors: ["sampling-method"]
population:
  who: "Not a single sampled population; a methods/framework paper illustrated using six US randomized field trials of universal, selective, and indicated prevention programs, spanning individual-, classroom-, school-, district-, and county-level randomization (e.g., Rochester Resilience Program, First and Third Generation Baltimore Prevention Program, Georgia Gatekeeper suicide-prevention training, Adolescent Substance Abuse Prevention Study, California MTFC trial)"
  where: ["United States"]
  when: null
  n: null
  sector: ["education", "public-health", "mental-health-services"]
  sample_notes: >
    Sample sizes for the illustrative trials range from roughly 470 children (Rochester
    Resilience Program) to 50,000 students (Georgia Gatekeeper); no single unified sample
    underlies the paper's own claims since it is a statistical-methods exposition, not a
    primary empirical study.
limitation:
  primary: "As a methods/framework paper, its own 'findings' are prescriptive standards and illustrative re-analyses rather than new substantive evidence about social connection or wellbeing, so support_strength for its claims reflects methodological consensus, not effect-size precision."
  others:
    - "Recommendations are built almost entirely from the authors' own multi-decade portfolio of prevention trials (Prevention Science and Methodology Group), limiting independent validation of the proposed ITT standards."
    - "The paper explicitly warns that its variation-in-impact methods (GAMM, GMM) can produce spurious subgroup findings if applied exploratorily without correction for multiple comparisons or theoretical pre-specification."
    - "Growth mixture / latent class models discussed are acknowledged elsewhere in the literature to be sensitive to distributional assumptions and can overextract classes."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Because the SNH project draws on suicide-prevention and prevention-science methodology,
  this paper is a foundational reference for how to correctly define analytic denominators,
  handle attrition/missing data, and test for who benefits under what conditions when the
  project runs or evaluates group-level interventions (e.g., team- or org-level social-
  support programs) rather than individually randomized ones; it directly informs how to
  avoid inflated or spurious subgroup claims about intervention impact on isolation,
  burnout, or belonging.
tags:
  topic: ["suicide-prevention", "methodology", "measurement"]
  method: ["case-study", "analytical"]
  population: ["students", "school-staff", "youth"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Methods for Testing Theory and Evaluating Impact in Randomized Field Trials - Intent-to-Treat Analyses/Methods for Testing Theory and Evaluating Impact in Randomized Field Trials - Intent-to-Treat Analyses.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Methods for Testing Theory and Evaluating Impact in Randomized Field Trials - Intent-to-Treat Analyses.pdf"
  notes: null
