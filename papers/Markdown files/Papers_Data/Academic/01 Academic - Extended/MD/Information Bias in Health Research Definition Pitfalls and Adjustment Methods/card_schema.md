id: "althubaiti-2016-information-bias-in-health-research-definition"
title: "Information bias in health research: definition, pitfalls, and adjustment methods"
authors:
  - "Althubaiti, Alaa"
year: 2016
doi: "10.2147/jmdh.s104807"
venue: {type: "journal", name: "Journal of Multidisciplinary Healthcare", volume: null, issue: null, pages: "211"}
citation: "Althubaiti (2016). Information bias in health research: definition, pitfalls, and adjustment methods. Journal of Multidisciplinary Healthcare, 211. https://doi.org/10.2147/jmdh.s104807"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  Althubaiti's narrative review catalogs three under-examined forms of information
  (measurement) bias in health research: self-reporting bias (social desirability and recall
  bias), measurement error bias (systematic vs. random), and confirmation bias, explaining
  the mechanism and consequence of each with worked examples (e.g., case-control recall
  asymmetry inflating odds ratios; naive analysis biasing regression estimators). It
  proposes concrete mitigation strategies -- internal/external validation studies,
  standardized scales (Marlowe-Crowne, Martin-Larsen), memory aids and shortened recall
  windows, calibration and statistical adjustment (simulation-extrapolation, regression
  calibration, instrumental-variable methods), and blinding/independent-check protocols for
  confirmation bias -- summarized in a study-design-by-bias-type reference table.
claims:
  - text: "In case-control studies, cases are more likely than healthy controls to recall past exposure to risk factors, so true exposure tends to be underreported in controls and overreported in cases; this widens the observed exposure-rate gap and inflates the observed odds ratio."
    evidence: "review-narrative"
    support_strength: "low"
    outcomes: ["measurement-bias"]
    predictors: ["sampling-method", "recall-bias"]
  - text: "Analyses that ignore measurement error ('naive analysis') can yield inconsistent or biased and inefficient estimators of regression parameters, producing poor confidence intervals and hypothesis tests; systematic errors are correctable via calibration studies, while random errors require statistical adjustment methods such as simulation-extrapolation, regression calibration, or instrumental-variable approaches."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["measurement-bias"]
    predictors: ["measurement-error", "intervention"]
  - text: "Even gold-standard validation methods carry error: in a cited validation study using 24-hour urinary excretion to estimate sodium intake, the estimated sodium intake tended to be lower than the true amount, illustrating that biological/laboratory measurement is not immune to bias."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["measurement-bias"]
    predictors: ["measurement-error"]
population:
  who: "Not a study of a human sample; a methodological guidance paper aimed at epidemiologists and medical/health researchers who design and analyze observational or experimental studies using self-report, laboratory, or clinical-judgment data."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No primary data collection; the paper synthesizes prior literature and cites
    illustrative examples (e.g., drug-use self-report validation, sodium-intake validation,
    blood-alcohol measurement error) drawn from other published studies rather than
    conducting new research.
limitation:
  primary: "This is a narrative, non-systematic review with no stated search strategy, inclusion criteria, or quality appraisal of the literature it draws on, so its claims cannot be treated as a comprehensive or quantitative synthesis of the evidence on information bias."
  others:
    - "The paper addresses general epidemiological and clinical research methodology, not any SNH-specific population, exposure, or outcome, so it functions only as background methods guidance rather than direct SNH evidence."
    - "Worked examples (e.g., sodium-intake validation, blood-alcohol measurement error) are illustrative single citations rather than a systematically assembled evidence base."
risk_of_bias: "medium"
relevance_to_project: >
  The paper itself contains no SNH findings, but it is directly usable as project methods
  guidance: it flags recall bias and social-desirability bias as threats whenever SNH corpus
  studies rely on self-reported loneliness, burnout, or social-support measures, and it
  supplies concrete mitigation tools (validation studies, standardized desirability scales,
  shortened recall windows, statistical adjustment for measurement error) that can inform
  how the project weighs self-report-based evidence when rating support_strength across
  other cards.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-narrative", "analytical"]
  population: ["researchers", "not-applicable"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Information Bias in Health Research Definition Pitfalls and Adjustment Methods/Information Bias in Health Research Definition Pitfalls and Adjustment Methods.md"
  pdf: "papers/Academic/01 Academic - Extended/Information Bias in Health Research Definition Pitfalls and Adjustment Methods.pdf"
  notes: null
