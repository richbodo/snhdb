id: "cole-2003-testing-mediational-models-with-longitudinal-data"
title: "Testing Mediational Models With Longitudinal Data: Questions and Tips in the Use of Structural Equation Modeling."
authors:
  - "Cole, David A."
  - "Maxwell, Scott E."
year: 2003
doi: "10.1037/0021-843x.112.4.558"
venue: {type: "journal", name: "Journal of Abnormal Psychology", volume: 112, issue: 4, pages: "558-577"}
citation: "Cole et al. (2003). Testing Mediational Models With Longitudinal Data: Questions and Tips in the Use of Structural Equation Modeling.. Journal of Abnormal Psychology, 112(4), 558-577. https://doi.org/10.1037/0021-843x.112.4.558"
article_type: "methods"
method: {design: "methods", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  Cole and Maxwell extend Baron and Kenny's cross-sectional mediation framework to
  longitudinal structural equation modeling, mathematically demonstrating that cross-
  sectional estimates of mediational paths are biased except under narrow, rarely-met
  conditions (e.g., X and M equally stable over time), and that measurement error, wave-
  spacing, and 'half-longitudinal' designs systematically distort indirect-effect estimates.
  They propose a five-step SEM procedure (test the measurement model, test for added
  components/omitted confounds, test for omitted paths, test stationarity, then estimate
  overall direct/indirect effects) for rigorously testing whether a mediator explains a
  causal chain over time.
claims:
  - text: "Cross-sectional correlations accurately reproduce true longitudinal mediational path coefficients (a and b) only under narrow, rarely-satisfied conditions (e.g., a or b equal zero, or X and M are exactly equally stable over time); outside these conditions cross-sectional data systematically over- or underestimate the longitudinal mediation effect."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
  - text: "When the mediator (M) is measured with random error, path a and path b are both underestimated while the residual direct effect c is spuriously overestimated (e.g., in a worked example, reliability of .5 in M drops path b from .80 to .30 while inflating c from .00 to .47), meaning unreliable mediator measures make full mediation look like partial or no mediation."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
  - text: "The magnitude of estimated mediational (indirect) effects depends heavily on the time lag between waves of data collection: only an assessment interval of exactly the causally-optimal lag (1I) yields unbiased time-specific effects, and researchers should instead sum 'overall' indirect effects across all valid tracings between the first and last wave rather than relying on a single time-specific ab product, since longer or mismatched lags can badly misrepresent the true mediated effect."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
population:
  who: "Not an empirical study of human participants; a methodological/statistical article illustrating structural equation modeling procedures with algebraic derivations and one hypothetical numeric worked example (arbitrary path coefficients), drawing on examples from the clinical/psychopathology literature (e.g., Andrews 1995, Trull 2001, Tein et al. 2000) to illustrate common design flaws."
  where: []
  when: null
  n: null
  sector: ["academic"]
  sample_notes: >
    No primary data collection; this is a statistical methods/tutorial paper with a
    hypothetical illustrative model, not a study with a sample.
limitation:
  primary: "The proposed five-step approach and 'overall effect' framework require at least three (ideally more) waves of multi-measure longitudinal data with empirically pre-established optimal time lags between waves, conditions rarely met in real studies, and the authors note no general test of statistical significance for overall indirect effects (beyond the 3-wave case) had yet been developed at time of writing."
  others:
    - "Recommendations assume linear, stationary causal processes and observational (non-experimental) designs; the authors explicitly caveat that randomized experimental manipulation of the mediator provides more compelling causal evidence than any SEM correction of observational data."
    - "The worked numerical example uses arbitrary illustrative path coefficients rather than real data, so its magnitudes are pedagogical, not empirical estimates."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a core methodological reference for any SNH analysis that models a mediator (e.g.,
  loneliness or social support) between a predictor (e.g., remote-work intensity) and an
  outcome (e.g., burnout, turnover): it warns against 'half-longitudinal' designs, single-
  wave mediator measurement, and mismatched survey-wave spacing, and gives a concrete five-
  step SEM checklist for defensibly testing such mediation claims in panel/longitudinal SNH
  survey data.
tags:
  topic: ["methodology", "measurement"]
  method: ["longitudinal", "structural-equation-modeling"]
  population: ["methodology"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling.pdf"
  notes: null
