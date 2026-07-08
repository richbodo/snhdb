id: "ab-2017-discriminant-validity-assessment-use-of-fornell"
title: "Discriminant Validity Assessment: Use of Fornell &amp; Larcker criterion versus HTMT Criterion"
authors:
  - "Ab Hamid, M R"
  - "Sami, W"
  - "Mohmad Sidek, M H"
year: 2017
doi: "10.1088/1742-6596/890/1/012163"
venue: {type: "journal", name: "Journal of Physics: Conference Series", volume: 890, issue: null, pages: "012163"}
citation: "Ab Hamid et al. (2017). Discriminant Validity Assessment: Use of Fornell &amp; Larcker criterion versus HTMT Criterion. Journal of Physics: Conference Series, 890, 012163. https://doi.org/10.1088/1742-6596/890/1/012163"
article_type: "methods"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "low", preregistered: false}
gist: >
  This paper re-analyzes a 429-respondent PLS-SEM dataset (six latent constructs:
  leadership, culture, productivity, employee, stakeholder, university performance) to
  compare two discriminant-validity tests. The Fornell-Larcker criterion judged all six
  constructs acceptably discriminant, but the newer, more conservative heterotrait-monotrait
  (HTMT) ratio flagged 8 of 15 construct pairs as problematic, revealing multicollinearity
  the older test missed. The authors argue HTMT should be the preferred criterion for
  validating reflective measurement models in survey-based SEM research.
claims:
  - text: "Using the Fornell-Larcker criterion, all six latent constructs (leadership, culture, productivity, employee, stakeholder, university performance) showed acceptable discriminant validity, with only two near-threshold violations: productivity-employee (difference of 0.009) and productivity-stakeholder (difference of 0.007), both judged negligible."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
  - text: "Applying the HTMT0.85 criterion to the same dataset flagged 8 of the 15 construct pairs (e.g., culture-productivity, culture-employee, culture-stakeholder, productivity-employee, productivity-stakeholder, productivity-university performance, employee-stakeholder, stakeholder-university performance) as lacking discriminant validity, indicating multicollinearity that the Fornell-Larcker test failed to detect."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
  - text: "The authors conclude that HTMT is a stricter and more sensitive test than either Fornell-Larcker or cross-loading assessment, and that the six-construct survey instrument used in this study needs to be revised and re-evaluated because it did not meet the more conservative HTMT standard."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
population:
  who: "429 respondents from a prior survey used to empirically validate a value-based excellence model for higher education institutions (HEIs), originally collected by Ab Hamid (2012) and reused here for a methods demonstration."
  where: ["Malaysia"]
  when: "2012 (original data collection); reanalyzed 2017"
  n: 429
  sector: ["higher-education"]
  sample_notes: >
    Data reused from a prior doctoral/empirical study of leadership, culture, productivity,
    employee, stakeholder, and university-performance constructs in Malaysian HEIs; no
    missing data reported, but this article gives no information on the original sampling
    method or response rate.
limitation:
  primary: "The comparison of validity criteria rests on a single reused dataset from one higher-education context, so it cannot establish how often Fornell-Larcker and HTMT would diverge across other populations, sectors, or measurement models."
  others:
    - "No information is given in this article about the original sampling method, response rate, or representativeness of the 429 respondents."
    - "The paper only tests one HTMT threshold (0.85) without robustness checks against the alternative 0.90 threshold it mentions."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a technical methods reference on assessing discriminant validity in PLS-SEM survey
  instruments, not a substantive SNH finding; it is relevant if the project validates its
  own latent-construct measures (e.g., belonging, isolation, burnout scales) via reflective
  PLS-SEM models, since it warns that the commonly used Fornell-Larcker criterion can pass
  constructs that a stricter HTMT test flags as insufficiently distinct.
tags:
  topic: ["methodology", "measurement"]
  method: ["survey", "secondary-data"]
  population: ["higher-education"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion.pdf"
  notes: null
