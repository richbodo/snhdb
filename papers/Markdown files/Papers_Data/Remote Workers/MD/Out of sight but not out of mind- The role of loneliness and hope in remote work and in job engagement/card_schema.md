id: "bareket-2023-out-of-sight-but-not-out"
title: "Out of sight but not out of mind: The role of loneliness and hope in remote work and in job engagement"
authors:
  - "Bareket-Bojmel, Liad"
  - "Chernyak-Hai, Lily"
  - "Margalit, Malka"
year: 2023
doi: "10.1016/j.paid.2022.111955"
venue: {type: "journal", name: "Personality and Individual Differences", volume: 202, issue: null, pages: "111955"}
citation: "Bareket-Bojmel et al. (2023). Out of sight but not out of mind: The role of loneliness and hope in remote work and in job engagement. Personality and Individual Differences, 202, 111955. https://doi.org/10.1016/j.paid.2022.111955"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A survey of 349 US/UK employees found that remote work does not uniformly reduce job
  engagement; instead, loneliness moderates the relationship, with remote work predicting
  significantly lower engagement only for employees with moderate or high loneliness, not
  for those with low loneliness. A moderated-mediation model further showed that among
  highly lonely employees, remote work was positively associated with hope, which in turn
  predicted higher job engagement, suggesting hope as a resource that can offset engagement
  loss in this vulnerable group. The authors argue this challenges the blanket assumption
  that remote work harms engagement and instead points to loneliness-targeted and hope-
  building interventions as the design lever.
claims:
  - text: "Loneliness significantly moderated the relationship between remote work and job engagement (b = -0.04, SE = 0.01, beta = -0.11, p = .01); simple slopes showed remote work significantly and negatively predicted job engagement for employees with high loneliness (b = -0.08, beta = -0.23, p < .001) and moderate loneliness (b = -0.04, beta = -0.12, p = .01), but not for those with low loneliness (b = -0.001, p = .96)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["loneliness", "remote-work-intensity"]
  - text: "Among employees with high loneliness, remote work significantly predicted higher hope (b = 0.09, SE = 0.03, beta = 0.19, p = .006), and hope significantly predicted job engagement (b = 0.41, beta = 0.57, p < .001); a bootstrapped moderated-mediation index (0.02, 95% CI [0.002, 0.04]) confirmed hope mediated the remote work-engagement link specifically at high loneliness levels, with no significant mediation at average or low loneliness."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["hope", "loneliness", "remote-work-intensity"]
  - text: "Hope and loneliness were strongly negatively correlated (r = -0.46, p < .001), and loneliness was negatively correlated with job engagement (r = -0.27, p < .001), while remote work days showed no significant zero-order correlation with either job engagement (r = -0.07) or hope (r = 0.05), indicating loneliness -- not remote work per se -- is the key risk factor."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["loneliness", "hope"]
population:
  who: "349 employees (170 men, 177 women, 2 other) from the US and UK, employed at least 20 hours/week (excluding freelancers), recruited via the Prolific online platform"
  where: ["United States", "United Kingdom"]
  when: null
  n: 349
  sector: ["general-workforce"]
  sample_notes: >
    Recruited via Prolific with high-reputation filter (>=95% prior approval rate); 51 of
    400 initial respondents excluded for failing prescreening/attention checks. 61% UK, 33%
    US, 6% other nationality; ages 21-69 (M=38.81, SD=9.95); 69% worked remotely at least
    one day/week, 35% fully remote (5 days), 31% fully office-based -- sample skewed toward
    high-frequency remote workers, limiting generalizability to low/no remote-work contexts.
limitation:
  primary: "Cross-sectional, single-sample correlational design (all self-report) precludes causal inference and raises common method variance concerns, though procedural safeguards (anonymity, separated question blocks, attention checks) were used to mitigate this."
  others:
    - "Unequal representation across remote-work intensity, with a disproportionate share working fully remote (5 days/week), limiting power to detect effects at intermediate remote-work levels."
    - "Remote work was measured with a single item (days worked remotely) rather than a validated multidimensional measure, and burnout was not assessed despite being theoretically relevant."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs SNH design by identifying loneliness as the moderating variable that
  determines whether remote work harms engagement, and hope as a candidate intervention
  target/mediator that can protect engagement specifically among lonely remote workers --
  supporting a targeted (not blanket) intervention design for remote-worker social network
  health.
tags:
  topic: ["remote-work", "loneliness", "job-engagement", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement.md"
  pdf: "papers/Remote Workers/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement.pdf"
  notes: null
