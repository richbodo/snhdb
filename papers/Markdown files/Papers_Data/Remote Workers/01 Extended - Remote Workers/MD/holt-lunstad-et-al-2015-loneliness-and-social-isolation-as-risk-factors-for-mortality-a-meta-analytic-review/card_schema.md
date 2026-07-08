id: "holt-2015-loneliness-and-social-isolation-as-risk"
title: "Loneliness and Social Isolation as Risk Factors for Mortality"
authors:
  - "Holt-Lunstad, Julianne"
  - "Smith, Timothy B."
  - "Baker, Mark"
  - "Harris, Tyler"
  - "Stephenson, David"
year: 2015
doi: "10.1177/1745691614568352"
venue: {type: "journal", name: "Perspectives on Psychological Science", volume: 10, issue: 2, pages: "227-237"}
citation: "Holt-Lunstad et al. (2015). Loneliness and Social Isolation as Risk Factors for Mortality. Perspectives on Psychological Science, 10(2), 227-237. https://doi.org/10.1177/1745691614568352"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  This meta-analytic review pools 70 independent prospective studies (3,407,134
  participants, ~7-year average follow-up) and finds that social isolation, loneliness, and
  living alone each independently and comparably predict earlier mortality, with fully-
  adjusted odds ratios of 1.29, 1.26, and 1.32 respectively. Objective and subjective
  isolation measures did not differ in predictive strength, and the risk was actually larger
  for adults under 65 than for older adults, challenging the assumption that isolation is
  chiefly an old-age problem. The authors argue the magnitude of this risk rivals well-
  established mortality risk factors like obesity and smoking, and call for social
  isolation/loneliness to be treated as a public health priority.
claims:
  - text: "Across fully adjusted statistical models controlling for health status and other confounds, weighted average odds ratios for mortality were 1.29 for social isolation, 1.26 for loneliness, and 1.32 for living alone, corresponding to 26-32% increased likelihood of death, with no significant difference among the three measures."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness", "social-support"]
  - text: "Risk from social deficits was moderated by age: studies with average participant age under 65 had larger effect sizes (OR = 1.57 adjusted, 1.92 unadjusted) than studies with participants over 75 (OR = 1.14 adjusted, 1.28 unadjusted), indicating isolation and loneliness are more predictive of death in midlife than in old age."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness"]
  - text: "Unadjusted effect sizes were significantly larger than fully adjusted ones (p < .001), and studies that failed to exclude terminally ill or already-declining participants at baseline showed inflated risk estimates (OR = 1.95 vs. 1.38), underscoring the importance of controlling for reverse causality via prior health status when estimating the isolation-mortality link."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness", "social-support"]
population:
  who: "70 independent prospective cohort/longitudinal studies (January 1980-February 2014) of adults with quantitative mortality outcomes as a function of social isolation, loneliness, or living alone"
  where: ["Europe", "North America", "Asia", "Australia", "multiple regions"]
  when: "1980-2014 (studies with initial data collection averaging 1993)"
  n: 3407134
  sector: ["public-health", "clinical", "community"]
  sample_notes: >
    63% community (normal population) samples, 37% patients with a medical condition; mean
    participant age 66.0 at intake, mean follow-up 7.1 years; 24% of studies had average age
    <=59, only 9% <50; high between-study heterogeneity (I2 = 97.8%); publication bias
    checks (Egger's test, fail-safe N = 1,268, trim-and-fill) found no evidence of missing
    studies.
limitation:
  primary: "Extremely high heterogeneity across included studies (I2 = 97.8%) means pooled effect sizes mask substantial variability, and causality cannot be confirmed despite prospective designs and covariate adjustment."
  others:
    - "Very few studies measured both objective isolation and loneliness in the same sample, so direct within-study comparisons of their relative/synergistic effects remain rare and largely untested."
    - "Marital status was not coded as a moderator despite being plausibly confounded with both age and living-alone status, limiting interpretation of the age-moderation finding."
    - "Most data still come from older-adult samples (only 24% averaged age <=59), so conclusions about younger and midlife adults rest on a comparatively small subset of studies."
risk_of_bias: "low"
relevance_to_project: >
  This is a foundational, high-N quantification of the health stakes of isolation and
  loneliness that the SNH project can cite to justify prioritizing connection and belonging
  interventions; the finding that midlife/working-age adults (not just the elderly) show the
  largest mortality risk from isolation directly supports targeting remote and hybrid
  workers, not just retirees, in SNH design and measurement choices.
tags:
  topic: ["isolation", "loneliness", "wellbeing", "mental-health", "community-health"]
  method: ["review-systematic", "secondary-data"]
  population: ["older-adults", "general-population", "community-samples"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review.pdf"
  notes: null
