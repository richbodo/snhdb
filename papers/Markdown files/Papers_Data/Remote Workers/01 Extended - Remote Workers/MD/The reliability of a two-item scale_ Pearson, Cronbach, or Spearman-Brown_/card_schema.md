id: "eisinga-2013-the-reliability-of-a-two-item"
title: "The reliability of a two-item scale: Pearson, Cronbach, or Spearman-Brown?"
authors:
  - "Eisinga, Rob"
  - "Grotenhuis, Manfred te"
  - "Pelzer, Ben"
year: 2013
doi: "10.1007/s00038-012-0416-3"
venue: {type: "journal", name: "International Journal of Public Health", volume: 58, issue: 4, pages: "637-642"}
citation: "Eisinga et al. (2013). The reliability of a two-item scale: Pearson, Cronbach, or Spearman-Brown?. International Journal of Public Health, 58(4), 637-642. https://doi.org/10.1007/s00038-012-0416-3"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methodological note derives and simulates reliability estimates for two-item scales
  under classical test theory, comparing the Pearson inter-item correlation, Cronbach's
  coefficient alpha, and the Spearman-Brown split-half formula. Using worked numerical
  examples and 1.6x10^9 simulated parameter combinations across parallel, tau-equivalent,
  and congeneric measurement models, the authors show that alpha is unbiased only under the
  restrictive tau-equivalence assumption and otherwise underestimates true reliability,
  whereas Spearman-Brown is on average less biased and always >= alpha. It concludes that
  when researchers must use a two-item scale, the Spearman-Brown coefficient (not Pearson r
  or alpha) should be reported.
claims:
  - text: "Cronbach's alpha is an unbiased estimator of a two-item scale's true reliability only when the items are at least essentially tau-equivalent; when items are congeneric (unequal factor loadings), alpha substantially underestimates true reliability even as inter-item correlation grows (e.g., a simulated example gives alpha = 0.441 versus true reliability r^2_tauY = 0.690)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The Spearman-Brown split-half coefficient (rho = 2r/(1+r)) is never lower than, and is almost always higher than, coefficient alpha for a two-item scale, and across simulations it is on average less biased than alpha, especially as inter-item correlation increases; the authors recommend it as the most appropriate reliability statistic for two-item scales."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The raw Pearson correlation between the two items is not an adequate reliability estimate for the composite two-item scale; it instead reflects the reliability of a single item (e.g., in a parallel-measures example, Pearson r = 0.640 while true scale reliability equals 0.780)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
population:
  who: "No human sample; a statistical/methodological demonstration using worked numerical examples and simulated data spanning parallel, tau-equivalent, essentially tau-equivalent, and congeneric two-item measurement models under classical test theory."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    Simulation generated all combinations of four loading/error parameters equidistant in
    [0,1] at .005 intervals (1.6x10^9 combinations); no empirical dataset or human
    respondents are used, so representativeness is not applicable.
limitation:
  primary: "The analysis is purely analytical/simulation-based and does not test the recommendations against real survey data, so its conclusions about bias apply to the idealized measurement models rather than to any specific empirical two-item scale."
  others:
    - "The authors explicitly note there is no statistical way to test the tau-equivalence or local-independence assumptions with only two items, so applied researchers cannot verify which measurement model their own two-item scale actually satisfies."
    - "The paper is a technical note that assumes readers already accept two-item scales are used out of necessity; it does not evaluate substantive social-network-health constructs directly."
risk_of_bias: "not-applicable"
relevance_to_project: >
  SNH surveys frequently rely on short (often two-item) measures of constructs like
  loneliness, social support, or burnout for time-constrained remote-worker samples; this
  paper gives a concrete, evidence-based rule (report Spearman-Brown rather than Cronbach's
  alpha or raw Pearson r) for computing and reporting the reliability of any such
  abbreviated scale used in the project's instruments.
tags:
  topic: ["measurement", "methodology"]
  method: ["theory", "analytical"]
  population: ["not-applicable"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_.pdf"
  notes: null
