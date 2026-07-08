id: "spector-2006-method-variance-in-organizational-research"
title: "Method Variance in Organizational Research"
authors:
  - "Spector, Paul E."
year: 2006
doi: "10.1177/1094428105284955"
venue: {type: "journal", name: "Organizational Research Methods", volume: 9, issue: 2, pages: "221-232"}
citation: "Spector (2006). Method Variance in Organizational Research. Organizational Research Methods, 9(2), 221-232. https://doi.org/10.1177/1094428105284955"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Spector argues that common method variance (CMV) -- the widely accepted claim that
  correlations among variables measured with the same self-report survey are automatically
  inflated -- is a 'methodological urban legend' rather than an established empirical fact.
  Reviewing meta-analyses and monomethod-versus-multimethod comparisons, he shows that
  candidate biasing variables (social desirability, negative affectivity, acquiescence)
  produce only small, inconsistent, construct-specific correlation distortion rather than a
  universal method-driven inflation, and he recommends abandoning the term CMV in favor of
  construct-specific analysis of measurement bias plus targeted design and statistical
  controls.
claims:
  - text: "In Boswell, Boudreau, and Dunford's (2004) study of 5 self-report turnover-process variables from the same questionnaire (n = 1,601), 4 of 10 (40%) correlations among the variables were nonsignificant and the largest significant correlation was only .20, despite power sufficient to detect correlations as small as .07 -- contradicting the assumption that CMV automatically produces a baseline of inflated correlations among monomethod self-report measures."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "job-satisfaction"]
    predictors: ["sampling-method"]
  - text: "Moorman and Podsakoff's (1992) meta-analysis of 36 samples (33 studies) linking social desirability to nine organizational variables found a mean correlation of only .05 (range .01-.17), with four of nine confidence intervals including zero, and a follow-up study found most partial correlations controlling for social desirability differed from zero-order correlations by no more than .02-.04 -- indicating social desirability is not a universal source of correlation inflation."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["sampling-method", "social-desirability-bias"]
  - text: "Crampton and Wagner's (1994) analysis of over 40,000 correlations from 581 articles, comparing 143 monomethod versus multimethod variable-pair correlations, found monomethod correlations were significantly higher in only 26.6% of cases, lower in 11.2%, and not significantly different in 62.2% of cases, refuting the idea that using a single method (e.g., self-report) universally inflates observed relationships."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "performance"]
    predictors: ["sampling-method"]
population:
  who: "Not an original empirical sample; a critical synthesis of prior organizational-research studies and meta-analyses on method variance, including Boswell et al. (2004, n=1,601), Moorman & Podsakoff (1992, 36 samples/33 studies), Ones et al. (1996), and Crampton & Wagner (1994, 581 articles)."
  where: []
  when: "Literature reviewed spans 1959-2004"
  n: null
  sector: []
  sample_notes: >
    This is a conceptual/methodological essay (an invited AOM conference paper expanded into
    a journal article), not a primary data collection; the 'sample' is the set of prior
    published organizational-behavior studies and meta-analyses the author re-analyzes and
    cites as evidence.
limitation:
  primary: "As a narrative argumentative essay rather than a systematic or pre-registered review, the selection and emphasis of supporting studies is not governed by a transparent, replicable search protocol and may be susceptible to the author's own confirmation bias against the CMV consensus he is critiquing."
  others:
    - "Relies heavily on comparisons between monomethod and multimethod (or partialled) correlations as evidence of 'no bias,' but the author himself notes multimethod data are not necessarily more valid, so absence of inflation could reflect attenuation in the comparison method rather than absence of CMV."
    - "Focuses on a narrow set of candidate biasing variables (social desirability, negative affectivity, acquiescence) and organizational-behavior constructs; findings may not generalize to other self-report domains, such as loneliness or social-support scales used in SNH research."
risk_of_bias: "medium"
relevance_to_project: >
  SNH research leans heavily on single-occasion self-report surveys of loneliness,
  isolation, social support, burnout, and job satisfaction; this paper is directly relevant
  evidence for whether such monomethod self-report findings should be discounted as
  automatically inflated by common method variance, and supports treating bias risk on a
  construct-by-construct basis (with targeted design/statistical controls) rather than
  dismissing SNH self-report findings wholesale.
tags:
  topic: ["methodology", "measurement", "job-satisfaction"]
  method: ["theory", "secondary-data"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend.pdf"
  notes: null
