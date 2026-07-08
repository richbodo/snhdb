id: "miller-2019-why-do-people-give-up-flossing"
title: "Why Do People Give Up FLOSSing? A Study of Contributor Disengagement in Open Source"
authors:
  - "Miller, Courtney"
  - "Widder, David Gray"
  - "Kästner, Christian"
  - "Vasilescu, Bogdan"
year: 2019
doi: "10.1007/978-3-030-20883-7_11"
venue: {type: "book", name: "IFIP Advances in Information and Communication Technology", volume: null, issue: null, pages: "116-129"}
citation: "Miller et al. (2019). Why Do People Give Up FLOSSing? A Study of Contributor Disengagement in Open Source. IFIP Advances in Information and Communication Technology, 116-129. https://doi.org/10.1007/978-3-030-20883-7_11"
article_type: "empirical"
method: {design: "mixed-methods", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This mixed-methods study surveys 151 established open source contributors who recently
  disengaged from all public GitHub activity, then uses Cox proportional-hazards survival
  modeling on 206 contributors (103 disengaged, 103 control) to test which factors predict
  disengagement. Occupational transitions (job or school changes) were by far the most
  commonly cited reason for disengagement, more so than lack of peer support or loss of
  interest, and contributors working nights/weekends cited social reasons more than those
  working office hours. The survival model confirms that working during office hours and
  experiencing a job/school transition both significantly increase disengagement risk, while
  higher activity level and working on more popular projects decrease it.
claims:
  - text: "In an open-ended survey of 151 recently disengaged contributors (239 total reasons cited), occupational reasons such as job or school transitions were the most common category (106 citations), more frequent than lack of peer support or losing interest in FLOSS, which are more commonly emphasized in prior literature."
    evidence: "mixed-methods"
    support_strength: "moderate"
    outcomes: ["turnover", "retention"]
    predictors: ["community-engagement", "social-support"]
  - text: "In the Cox proportional-hazards survival model (n=206 contributors, 103 disengaged), experiencing a job/school transition in the last year increased risk of disengagement by a hazard ratio of 2.48 (p<0.01), and working predominantly during office hours (vs. nights/weekends) increased disengagement risk with a hazard ratio of 1.56-2.20 (p<0.05)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["turnover", "retention"]
    predictors: ["boundary-management", "workload"]
  - text: "Higher overall activity level (hazard ratio 0.36, p<0.001) and working on more popular projects (higher GitHub stars; hazard ratio 0.85-0.86, p<0.01) both significantly decreased a contributor's risk of disengagement, while doing more support-oriented work (issues/PR management) showed no statistically significant effect on disengagement risk."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["retention", "turnover"]
    predictors: ["community-engagement", "network-structure"]
population:
  who: "Established open source contributors on GitHub who had contributed at least 100 commits per six-month period for three consecutive periods (18 months of sustained activity); survey sample of 151 who then went nearly silent (disengaged), plus a survival-model sample of 206 (103 disengaged 'treatment', 103 active 'control')"
  where: []
  when: "GHTorrent trace data version 2018-08; survey conducted circa 2018-2019"
  n: 206
  sector: ["open-source"]
  sample_notes: >
    Survey invited 702 identified recently-disengaged contributors with public email
    addresses; received 151 valid responses (21.5% response rate). Survival model further
    restricted to 206 of these plus controls for whom public CV data could be located (34
    excluded for lack of CV data), risking selection bias. Sample targets established/highly
    active contributors, not peripheral or episodic ones, so findings may not generalize to
    occasional contributors.
limitation:
  primary: "The survival model's treatment group is limited to survey respondents with locatable public CVs, introducing selection bias and constraining statistical power due to the resulting moderate sample size (206)."
  others:
    - "Self-reported survey reasons for disengagement may be subject to social-desirability bias (respondents citing more acceptable reasons like job transitions rather than dissatisfaction or conflict)."
    - "Disengagement was operationalized as a sudden drop in public GitHub activity within a six-month window, which may not capture more gradual disengagement and could misclassify moves to private repositories or other platforms."
    - "Findings are specific to highly active, established contributors identified via GHTorrent trace data and may not generalize to peripheral, episodic, or non-GitHub open source contributors."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a concrete, trace-data-operationalizable predictor set (job/school transitions,
  working-hours pattern, activity level, project popularity) for identifying at-risk open
  source contributors before they disengage, directly informing SNH's design of early-
  warning or support-targeting mechanisms for maintainer/contributor burnout and turnover.
  The finding that occupational transitions dominate self-reported disengagement reasons
  over lack of peer support suggests SNH interventions should consider life-transition-aware
  support alongside community-belonging interventions.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "methodology"]
  method: ["mixed-methods", "survey"]
  population: ["open-source-contributors"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Why Do People Give Up FLOSSing A Study of Contributor Disengagement in Open Source/Why Do People Give Up FLOSSing A Study of Contributor Disengagement in Open Source.md"
  pdf: "papers/Articles/01 Articles - Extended/Why Do People Give Up FLOSSing A Study of Contributor Disengagement in Open Source.pdf"
  notes: null
