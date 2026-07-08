id: "jibunoh-2025-impact-of-remote-work-dynamics-on"
title: "Impact of Remote Work Dynamics on Mental Health and Productivity"
authors:
  - "Jibunoh, Joy"
  - "Ezichi, Ogbonnaya"
  - "Okpanachi, Victor"
  - "Amaechi, Chibuzor"
  - "Awosan, Wuraola"
  - "Tchoumo, Prosper"
  - "Sanusi, Jubril"
year: 2025
doi: "10.4236/ojd.2025.141002"
venue: {type: "journal", name: "Open Journal of Depression", volume: 14, issue: 01, pages: "13-27"}
citation: "Jibunoh et al. (2025). Impact of Remote Work Dynamics on Mental Health and Productivity. Open Journal of Depression, 14(01), 13-27. https://doi.org/10.4236/ojd.2025.141002"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "low", preregistered: false}
gist: >
  Using a secondary Kaggle dataset of 5000 employees across six global regions and seven
  industries, this cross-sectional study finds that only 33.5% of respondents are satisfied
  with remote work and that workplace location (remote or hybrid vs. onsite) is the only
  statistically significant predictor of that satisfaction in a logistic regression, while
  gender, industry, region, and years of experience are not. Roughly three-quarters of
  employees report a mental health condition (anxiety, burnout, or depression) regardless of
  gender, and hybrid/remote workers report modestly better work-life balance than onsite
  workers (40% vs 37.2% high balance).
claims:
  - text: "Only 33.5% of employees (1675/5000) reported being satisfied with remote work, significantly less than the 50% baseline proportion tested (exact binomial test, p ≈ 0), with 66.5% unsatisfied or neutral."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Approximately 75% of employees across all genders reported a mental health condition (anxiety, burnout, or depression) — 75.27% of women, 76.61% of men, 74.63% of non-binary employees — with no significant gender difference in susceptibility."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["mental-health", "anxiety", "burnout", "depression"]
    predictors: ["remote-work-intensity"]
  - text: "In binary logistic regression, workplace location was the only statistically significant predictor of remote-work satisfaction (Wald = 13.24, df = 2, p = 0.001): both remote (Exp(β) = 0.841, 95% CI 0.728–0.973) and hybrid (Exp(β) = 0.767, 95% CI 0.664–0.887) locations were associated with lower odds of satisfaction than onsite work, while age, gender, region, industry, years of experience, and meeting frequency were not significant predictors."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
population:
  who: "5000 employees drawn from a public Kaggle dataset spanning multiple industries (IT, consulting, retail, finance, healthcare, manufacturing, education) and work locations (remote, hybrid, onsite)"
  where: ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
  when: null
  n: 5000
  sector: ["technology", "finance", "healthcare", "manufacturing", "retail", "education", "consulting"]
  sample_notes: >
    Data were obtained secondhand from a public Kaggle dataset ('Remote Work & Mental
    Health'); the original survey's recruitment method, response rate, data-collection
    period, and representativeness are not described by the study authors.
limitation:
  primary: "The dataset is a secondary, publicly-posted Kaggle dataset whose original sampling frame, recruitment method, response rate, and data-collection dates are not described, making representativeness and even provenance of the 5000-respondent sample impossible to verify."
  others:
    - "Cross-sectional self-report design cannot establish causal direction between remote work location and mental health or satisfaction outcomes."
    - "Mental health condition was measured as a single self-reported categorical variable (anxiety/burnout/depression/none) without validated clinical instruments."
    - "Published in an SCIRP open-access journal (Open Journal of Depression), whose peer-review rigor is widely questioned in the literature."
risk_of_bias: "high"
relevance_to_project: >
  Offers rough population-level base rates (about 75% self-reported mental health condition,
  roughly one-third satisfaction with remote work) and evidence that self-reported workplace
  location, not demographic or industry factors, predicts remote-work satisfaction in this
  sample — useful as a coarse prevalence anchor and a caution against assuming demographic-
  targeted SNH interventions will move satisfaction more than format/location choices
  themselves, though the unverifiable data provenance limits how much weight to give it.
tags:
  topic: ["remote-work", "hybrid-work", "mental-health", "job-satisfaction", "wellbeing"]
  method: ["cross-sectional", "secondary-data"]
  population: ["remote-workers", "hybrid-workers", "global-sample", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/MD/Impact of Remote Work Dynamics on Mental Health and Productivity/Impact of Remote Work Dynamics on Mental Health and Productivity.md"
  pdf: "papers/Academic/Impact of Remote Work Dynamics on Mental Health and Productivity.pdf"
  notes: null
