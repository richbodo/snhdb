id: "mackinnon-2004-confidence-limits-for-the-indirect-effect"
title: "Confidence Limits for the Indirect Effect: Distribution of the Product and Resampling Methods"
authors:
  - "MacKinnon, David P."
  - "Lockwood, Chondra M."
  - "Williams, Jason"
year: 2004
doi: "10.1207/s15327906mbr3901_4"
venue: {type: "journal", name: "Multivariate Behavioral Research", volume: 39, issue: 1, pages: "99-128"}
citation: "MacKinnon et al. (2004). Confidence Limits for the Indirect Effect: Distribution of the Product and Resampling Methods. Multivariate Behavioral Research, 39(1), 99-128. https://doi.org/10.1207/s15327906mbr3901_4"
article_type: "methods"
method: {design: "simulation-study", approach: "modelling", evidence_level: "strong", preregistered: false}
gist: >
  This methods paper uses large-scale Monte Carlo simulation to show that the standard
  z-test confidence limits for an indirect (mediated) effect are imbalanced because the
  sampling distribution of a product of two regression coefficients is not normal. It
  evaluates two fixes -- confidence limits based on the distribution of the product (the M
  and empirical-M tests) and six resampling methods (jackknife, percentile/bias-
  corrected/bootstrap-t/bootstrap-Q bootstrap, Monte Carlo) -- and finds the bias-corrected
  bootstrap gives the most accurate coverage and greatest statistical power, illustrated
  with an applied mediation example from a school-based steroid-prevention trial.
claims:
  - text: "Confidence limits for the indirect effect based on the traditional z test (dividing the effect by its multivariate-delta standard error and comparing to the normal distribution) are consistently imbalanced: across 80 simulated combinations of sample size (50-1000) and path effect sizes, the proportion of true values falling outside the confidence interval was almost always below the nominal .025 per tail, indicating reduced statistical power to detect true mediated effects."
    evidence: "simulation-study"
    support_strength: "strong"
    outcomes: ["statistical-power"]
    predictors: ["mediation-analysis"]
  - text: "The distribution-of-product (M) test, which uses critical values from the non-normal distribution of the product of two normal random variables, produced confidence limits closer to the nominal Type I error rate than the z test in nearly all 80 parameter combinations in Study 1, though it was still imperfect for zero/small effect sizes and small samples."
    evidence: "simulation-study"
    support_strength: "strong"
    outcomes: ["statistical-power"]
    predictors: ["mediation-analysis"]
  - text: "Among six resampling methods compared across sample sizes of 25-200 in Study 2, the bias-corrected bootstrap had the best overall performance -- Type I error rates closest to nominal levels and the greatest statistical power -- while the traditional z test and jackknife performed worst (outside robustness criteria 144 and 138 times respectively out of 240 checks, versus 73 for bias-corrected bootstrap)."
    evidence: "simulation-study"
    support_strength: "strong"
    outcomes: ["statistical-power"]
    predictors: ["mediation-analysis"]
population:
  who: "Not a human sample: a Monte Carlo simulation across 80 (Study 1) and 40 (Study 2) combinations of sample size and path effect sizes for a single-mediator regression model; illustrated with an applied example of N=861 high-school football players from the ATLAS anabolic-steroid-prevention program (15 treatment, 16 control schools)."
  where: ["USA"]
  when: "Simulation conducted circa early 2000s; ATLAS example data collected in the 1990s"
  n: 861
  sector: ["academic", "education"]
  sample_notes: >
    Simulation population is entirely synthetic (SAS-generated normal data), so
    representativeness is not applicable to the core method; the illustrative ATLAS example
    is a real but unrelated prevention-trial dataset used only to demonstrate the
    computations, not as a research sample for this paper's own claims.
limitation:
  primary: "Findings are limited to a single indirect-effect model with one mediator and ordinary least-squares regression; extension to indirect effects involving three or more paths (product of three+ random variables) lacks tabled critical values and was not simulated here."
  others:
    - "The paper is silent on conceptual/causal-inference issues in mediation (correct temporal ordering, no omitted variables, no measurement error), assuming the mediation model is correctly specified."
    - "Resampling methods require raw data and more computation, and the 'first law of statistical analysis' problem means different analysts bootstrapping the same data can reach different conclusions."
risk_of_bias: "low"
relevance_to_project: >
  SNH research frequently tests mediation hypotheses (e.g., remote-work intensity ->
  isolation -> burnout, or social support -> belonging -> retention); this paper's finding
  that traditional z-based confidence intervals for indirect effects understate significance
  and that bias-corrected bootstrap or distribution-of-product tests are more accurate
  directly informs which statistical test the project should use/cite when evaluating
  mediator-based claims in the corpus.
tags:
  topic: ["methodology", "measurement"]
  method: ["quantitative", "simulation"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Confidence Limits for the Indirect Effect  Distribution of the Product and Resampling Methods/Confidence Limits for the Indirect Effect  Distribution of the Product and Resampling Methods.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Confidence Limits for the Indirect Effect  Distribution of the Product and Resampling Methods.pdf"
  notes: null
