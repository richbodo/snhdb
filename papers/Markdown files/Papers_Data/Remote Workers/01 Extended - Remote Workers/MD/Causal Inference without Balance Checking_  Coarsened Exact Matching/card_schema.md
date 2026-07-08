id: "iacus-2012-causal-inference-without-balance-checking-coarsened"
title: "Causal Inference without Balance Checking: Coarsened Exact Matching"
authors:
  - "Iacus, Stefano M."
  - "King, Gary"
  - "Porro, Giuseppe"
year: 2012
doi: "10.1093/pan/mpr013"
venue: {type: "journal", name: "Political Analysis", volume: 20, issue: 1, pages: "1-24"}
citation: "Iacus et al. (2012). Causal Inference without Balance Checking: Coarsened Exact Matching. Political Analysis, 20(1), 1-24. https://doi.org/10.1093/pan/mpr013"
article_type: "methods"
method: {design: "theory", approach: "modelling", evidence_level: "reference", preregistered: false}
gist: >
  The paper introduces Coarsened Exact Matching (CEM), a nonparametric preprocessing method
  for observational causal inference that bounds covariate imbalance, model dependence, and
  estimation error ex ante rather than requiring iterative post hoc balance checking. Using
  Monte Carlo simulation and a canonical job-training benchmark data set, the authors show
  CEM dominates propensity-score, Mahalanobis, and genetic matching on bias, variance, RMSE,
  and imbalance reduction, while being far faster and more robust to measurement error. Its
  contribution to the SNH project is purely methodological: a candidate tool for
  strengthening causal inference in future observational remote-work or community-health
  analyses, not substantive findings about social connection or wellbeing.
claims:
  - text: "In 5000 Monte Carlo replications based on the Lalonde/Dehejia-Wahba job-training data, CEM reduced RMSE of the treatment-effect estimate by 93% relative to the raw (unmatched) data (RMSE 111.38 vs 1622.63) and eliminated 99.8% of bias, outperforming Mahalanobis matching (RMSE 1077.20), propensity-score matching (1058.28), and genetic matching (505.55)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["estimation-bias"]
    predictors: ["sampling-method"]
  - text: "Across 5000 simulated perturbations of an earnings variable (to test robustness to measurement error), CEM preserved 95.3% of treated units and 97.7% of control units in the matched set, compared to roughly 70-81% for propensity-score, Mahalanobis, and genetic matching."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement-error"]
    predictors: ["sampling-method"]
  - text: "In an empirical illustration on the Lalonde observational data, CEM reduced multivariate imbalance (L1) by 17.47% (0.977 to 0.806) and achieved exact zero mean-difference balance on all binary/categorical covariates (marital status, no-degree, race, unemployment indicators), whereas propensity-score matching reduced imbalance only 2.48% and left substantial residual imbalance on those same covariates."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["covariate-balance"]
    predictors: ["sampling-method"]
population:
  who: "Not a human-subjects study of remote work or SNH outcomes; illustrative data are Monte Carlo simulations and the canonical Lalonde (1986) National Supported Work Demonstration job-training benchmark, combining 297 experimental treated participants with 2,490 PSID observational control units."
  where: ["USA"]
  when: "Original NSW/PSID data from the 1970s-80s; paper published 2012"
  n: 2787
  sector: ["labor-market"]
  sample_notes: >
    This is a statistics/econometrics methods paper, not an SNH empirical study; the
    'sample' is a standard causal-inference benchmark data set (job-training earnings) used
    only to demonstrate the matching algorithm's statistical properties.
limitation:
  primary: "The method is demonstrated only on a canonical econometric benchmark (job-training earnings data) and simulations, not on any social-network-health, remote-work, isolation, or wellbeing outcome, so it offers no substantive SNH evidence, only a candidate analytic tool."
  others:
    - "Simulation results depend on a specific nonlinear data-generating process chosen to replicate a prior benchmark (Diamond and Sekhon 2005) and may not generalize to all covariate structures encountered in SNH data."
    - "CEM's imbalance reduction trades off against matched sample size (e.g., 176 of 297 treated units retained in the empirical example), which can reduce statistical power."
    - "Results and comparisons come entirely from the method's own developers with no independent replication reported in this paper."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Offers a matching method (CEM) that SNH researchers could adopt to strengthen causal
  claims from observational remote-work or community data (e.g., estimating effects of an
  intervention on burnout, turnover, or isolation) while avoiding the iterative balance-
  checking failures common with propensity-score matching; relevant as a methodological
  reference for future SNH causal analyses rather than as substantive evidence.
tags:
  topic: ["methodology", "measurement"]
  method: ["theory", "secondary-data"]
  population: ["labor-market-participants"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Causal Inference without Balance Checking_  Coarsened Exact Matching/Causal Inference without Balance Checking_  Coarsened Exact Matching.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Causal Inference without Balance Checking_  Coarsened Exact Matching.pdf"
  notes: null
