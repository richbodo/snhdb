id: "podsakoff-2003-common-method-biases-in-behavioral-research"
title: "Common method biases in behavioral research: A critical review of the literature and recommended remedies."
authors:
  - "Podsakoff, Philip M."
  - "MacKenzie, Scott B."
  - "Lee, Jeong-Yeon"
  - "Podsakoff, Nathan P."
year: 2003
doi: "10.1037/0021-9010.88.5.879"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 88, issue: 5, pages: "879-903"}
citation: "Podsakoff et al. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies.. Journal of Applied Psychology, 88(5), 879-903. https://doi.org/10.1037/0021-9010.88.5.879"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "strong", preregistered: false}
gist: >
  This is the field-defining critical review of common method variance (CMV) in behavioral
  research: it catalogs the mechanisms by which shared measurement method (rather than the
  constructs themselves) inflates or deflates observed relationships between self-reported
  predictor and criterion variables, and evaluates the procedural and statistical remedies
  available to control for it. Drawing on Cote and Buckley's (1987) meta-analysis of 70
  multitrait-multimethod studies, the authors show method variance typically accounts for
  roughly a quarter of measure variance and can shift observed correlations dramatically,
  then systematically critique widely used fixes (Harman's single-factor test, marker-
  variable and partial-correlation techniques, latent-method-factor CFA models) as
  individually insufficient. For the SNH corpus, which relies heavily on single-source self-
  report surveys of remote workers (loneliness, burnout, belonging, engagement measured via
  the same instrument), this paper is the standard reference for assessing whether a given
  study's design adequately guards against common method bias.
claims:
  - text: "Meta-analytic evidence across 70 multitrait-multimethod construct validation studies indicates that, on average, about 26.3% of the variance in a typical research measure is attributable to systematic method variance rather than the construct of interest, ranging from 15.8% in marketing to 30.5% in education studies; attitude measures average 40.7% method variance versus 22.5% for job performance measures."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "wellbeing"]
    predictors: ["sampling-method"]
  - text: "Studies contrasting relationships estimated with versus without common method variance controlled found that, on average, method-contaminated analyses explained approximately 35% of variance in a relationship versus approximately 11% when method variance was controlled, and method effects can either inflate or deflate (not just inflate) observed correlations depending on the correlation between methods."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "performance"]
    predictors: ["sampling-method"]
  - text: "Commonly used post hoc statistical remedies have serious limitations: Harman's single-factor test provides no statistical control and becomes less conservative as the number of variables increases; the marker-variable/partial-correlation technique fails to control for major CMV sources like implicit theories and consistency motif and wrongly assumes method bias only inflates (never deflates) relationships; and even latent single-method-factor CFA approaches assume the method factor does not interact with trait constructs, an assumption that is often untested."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
population:
  who: "Not an empirical sample; the review synthesizes findings from prior multitrait-multimethod (MTMM) meta-analyses (notably Cote & Buckley 1987's 70 construct-validation studies) and dozens of methodological/statistical studies in psychology, marketing, management, and education."
  where: []
  when: null
  n: null
  sector: ["academic"]
  sample_notes: >
    No primary data collection by the authors; population is the set of published MTMM and
    method-bias studies cited throughout the article, spanning multiple disciplines and
    decades up to 2002.
limitation:
  primary: "As a narrative (non-systematic) critical review, it does not report a reproducible search/inclusion protocol, so coverage of the method-bias literature, while extensive, is not guaranteed to be exhaustive or free of selection bias."
  others:
    - "The quantitative estimates of method variance (e.g., 26.3% average) come from a single meta-analytic source (Cote & Buckley, 1987) whose generalizability across all research domains and construct types is uncertain."
    - "The paper is prescriptive/methodological rather than substantive: it makes no claims about any specific social, organizational, or health outcome, only about measurement artifact risk in self-report research designs."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This paper is the standard citation for justifying (or critiquing) survey design choices
  across the SNH corpus, most of which relies on single-source, same-instrument self-reports
  of loneliness, isolation, burnout, and belonging alongside self-reported predictors like
  social support or workload; it directly informs whether such studies' correlational
  findings should be discounted for common method bias and what procedural safeguards
  (temporal/proximal/methodological separation, respondent anonymity, improved item wording)
  a well-designed SNH survey should adopt.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-narrative", "analytical"]
  population: ["general"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review.pdf"
  notes: null
