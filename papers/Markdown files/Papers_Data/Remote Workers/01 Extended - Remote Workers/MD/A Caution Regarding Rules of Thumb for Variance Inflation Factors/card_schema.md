id: "obrien-2007-a-caution-regarding-rules-of-thumb"
title: "A Caution Regarding Rules of Thumb for Variance Inflation Factors"
authors:
  - "O’brien, Robert M."
year: 2007
doi: "10.1007/s11135-006-9018-6"
venue: {type: "journal", name: "Quality &amp; Quantity", volume: 41, issue: 5, pages: "673-690"}
citation: "O’brien (2007). A Caution Regarding Rules of Thumb for Variance Inflation Factors. Quality &amp; Quantity, 41(5), 673-690. https://doi.org/10.1007/s11135-006-9018-6"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  O'Brien argues that popular rules of thumb for the Variance Inflation Factor (VIF of 4 or
  10) misidentify 'serious' multi-collinearity because they ignore other factors that
  jointly determine the variance of a regression coefficient: the variance explained in the
  dependent variable (R2y), sample size, and the variance of the predictor itself. Using
  algebraic derivation and hypothetical comparison scenarios, the paper shows that
  regression coefficients with VIF values of 20 or 40 can be more precisely estimated
  (larger t-values, narrower confidence intervals) than a baseline model with a low VIF of
  1.25, once R2y and n are taken into account. It concludes that automatically dropping
  variables, combining them into indices, or using ridge regression solely because VIF
  exceeds a threshold can do more harm than the collinearity itself, unless motivated by
  theory.
claims:
  - text: "In an illustrative comparison, a regression coefficient with VIF = 40, R2y = 0.95, and n = 1,585 had a t-value of 7.35, versus t = 3.00 for a baseline model with VIF = 1.25, R2y = 0.40, and n = 100 -- i.e., the model with far higher VIF produced a more precisely estimated, more statistically significant coefficient."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["multicollinearity", "sample-size", "variance-explained"]
  - text: "Widely cited VIF thresholds (rule of 4 or rule of 10, e.g., from Menard 1995, Neter et al. 1989, Hair et al. 1995, and Marquardt 1970) are used in practice as blanket indicators of 'serious' multi-collinearity without regard to sample size, the variance explained by the model, or the variance of the predictor of interest, leading researchers and reviewers to question results that are statistically solid."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["multicollinearity"]
  - text: "Common remedies for high VIF -- dropping a correlated independent variable, combining variables into a single index, or applying ridge regression -- can introduce specification error or biased estimates unless theoretically motivated, because dropping a variable changes what the remaining coefficient actually represents (no longer controlling for the dropped variable)."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["model-specification"]
population:
  who: "Not an empirical study of human subjects; a mathematical/analytical demonstration using hypothetical baseline and comparison OLS regression scenarios (Table I) aimed at social-science researchers who use multiple regression"
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No sample; illustrative numerical scenarios (R2i, R2y, n, VIF combinations) are
    constructed to demonstrate algebraic relationships, not drawn from real data.
limitation:
  primary: "The paper is a purely analytical demonstration using hypothetical baseline and comparison regression scenarios rather than empirical data, so how well its illustrative parameter combinations match any given real-world analysis is left to the reader to judge."
  others:
    - "Addresses only ordinary least squares linear regression; does not extend the argument to logistic, multilevel, or other regression frameworks common in social/organizational research."
    - "Assumes correctly specified models and unbiased estimators; does not address interactions between collinearity and omitted-variable bias or measurement error."
risk_of_bias: "not-applicable"
relevance_to_project: >
  SNH survey-based regression models often include correlated predictors (e.g., workload,
  isolation, social support, technostress) that can produce high VIF values; this paper is a
  methodological reference cautioning the project against automatically dropping, combining,
  or ridge-regressing such predictors based on VIF thresholds alone, and instead
  interpreting collinearity diagnostics jointly with sample size and model R2 when analyzing
  SNH survey data.
tags:
  topic: ["methodology", "measurement"]
  method: ["analytical"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/A Caution Regarding Rules of Thumb for Variance Inflation Factors/A Caution Regarding Rules of Thumb for Variance Inflation Factors.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/A Caution Regarding Rules of Thumb for Variance Inflation Factors.pdf"
  notes: null
