id: "hooper-2008-structural-equation-modelling-guidelines-for-determining"
title: "Structural Equation Modelling: Guidelines for Determining Model Fit"
authors:
  - "Hooper, Daire"
  - "Coughlan, Joseph"
  - "Mullen, Michael R."
year: 2008
doi: null
venue: {type: "journal", name: "The Electronic Journal of Business Research Methods, 6(1), 53-60", volume: null, issue: null, pages: null}
citation: "Hooper et al. (2008). Structural Equation Modelling: Guidelines for Determining Model Fit. The Electronic Journal of Business Research Methods, 6(1), 53-60."
article_type: "methods"
method: {design: "review-scoping", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methods paper synthesizes decades of statistical debate on how to assess model fit in
  structural equation modelling (SEM), reviewing absolute, incremental, and parsimony fit
  indices (chi-square, RMSEA, GFI/AGFI, SRMR, NFI/NNFI, CFI, PGFI/PNFI). It converges on a
  concrete reporting recommendation -- always report the chi-square statistic with df and p,
  plus RMSEA with its confidence interval, SRMR, CFI, and one parsimony index -- and warns
  against 'index shopping' for whichever statistic makes a poorly-fitting model look
  acceptable. For the SNH project it functions as a citable methodological standard for any
  quantitative SEM work (e.g. modelling how loneliness, social support, or burnout predict
  turnover) done within or cited by the corpus.
claims:
  - text: "Best-practice reporting for SEM model fit is to include the Chi-Square statistic with its degrees of freedom and p-value, the RMSEA with its confidence interval, the SRMR, the CFI, and one parsimony fit index such as the PNFI, because these are the indices found least sensitive to sample size, model misspecification, and parameter estimates."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["sample-size"]
  - text: "Consensus threshold recommendations from the reviewed literature: RMSEA close to .06 or a stringent upper limit of .07 indicates good fit, SRMR values below .08 are acceptable, and CFI/NNFI values of .95 or greater are indicative of good model fit (Hu and Bentler, 1999)."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["threshold-criteria"]
  - text: "The Model Chi-Square test is highly sensitive to sample size: it nearly always rejects the model when large samples are used, but lacks statistical power to discriminate good from poor fitting models when samples are small, limiting its use as a standalone fit measure."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["sampling-method"]
population:
  who: "Not an empirical human-subjects study; it is a methodological synthesis aimed at researchers across the social sciences who use structural equation modelling, drawing on statistics and simulation literature from 1974-2007."
  where: []
  when: null
  n: null
  sector: ["academic-research"]
  sample_notes: >
    No primary data were collected; the paper is a narrative review/synthesis of prior
    statistical and simulation studies on SEM fit indices, so there is no sample, response
    rate, or representativeness to assess.
limitation:
  primary: "As a non-systematic narrative synthesis of the fit-index literature (not a formal systematic or scoping review with a documented search protocol), the selection and weighting of which studies and thresholds to foreground reflects the authors' judgment."
  others:
    - "The paper itself notes that many recommended cut-off values (e.g. for RMSEA, CFI) lack universal consensus and have shifted substantially over time, so the 'guidelines' it distills are contingent rather than fixed statistical facts."
    - "Published in 2008, so it does not reflect SEM fit-index methodology debates from the subsequent 15+ years."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a standard methodological reference for judging model fit in structural equation
  modelling; it is relevant to the SNH project as a citable statistical standard whenever
  the corpus's own or cited quantitative studies use SEM to model relationships among
  constructs like loneliness, isolation, social support, burnout, or turnover, so that
  reported fit statistics can be evaluated against consensus thresholds.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-scoping"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Structural Equation Modelling_ Guidelines for Determining Model F/Structural Equation Modelling_ Guidelines for Determining Model F.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Structural Equation Modelling_ Guidelines for Determining Model F.pdf"
  notes: "no-doi: journal article"
