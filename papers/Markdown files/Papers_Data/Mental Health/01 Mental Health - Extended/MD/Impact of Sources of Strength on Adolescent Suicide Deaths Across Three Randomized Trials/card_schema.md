id: "wyman-2023-impact-of-sources-of-strength-on"
title: "Impact of Sources of Strength on adolescent suicide deaths across three randomized trials"
authors:
  - "Wyman, Peter"
  - "Cero, Ian"
  - "Brown, Charles Hendricks"
  - "Espelage, Dorothy"
  - "Pisani, Anthony"
  - "Kuehl, Tomei"
  - "Schmeelk-Cone, Karen"
year: 2023
doi: "10.1136/ip-2023-044944"
venue: {type: "journal", name: "Injury Prevention", volume: 29, issue: 5, pages: "442-445"}
citation: "Wyman et al. (2023). Impact of Sources of Strength on adolescent suicide deaths across three randomized trials. Injury Prevention, 29(5), 442-445. https://doi.org/10.1136/ip-2023-044944"
article_type: "empirical"
method: {design: "rct", approach: "experiment", evidence_level: "moderate", preregistered: false}
gist: >
  This paper pools three cluster-randomized trials (78 high schools, ~40,748 student-years
  of exposure) of Sources of Strength, a peer-leader, social-network-informed suicide
  prevention program, to test its effect on actual student suicide deaths. No suicides
  occurred in intervention schools versus four in control schools (rate of 0 vs. 20.86 per
  100,000), but statistical significance depended on the test used: a state-level exact test
  across all 78 schools found fewer suicides in intervention schools (p=0.047), while a
  stricter test restricted to the 72 randomly paired schools found no significant difference
  (p=0.150). The authors argue the mixed result reflects the low statistical power inherent
  to mortality outcomes in RCTs and call for adaptive, state-wide roll-out trial designs to
  confirm the signal.
claims:
  - text: "Across three pooled cluster RCTs (78 schools, 40,748 student-years), zero suicides occurred in Sources of Strength intervention schools versus four in control schools, an aggregated suicide rate of 0 vs. 20.86 per 100,000 person-years."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["suicidal-ideation"]
    predictors: ["intervention", "peer-mentoring", "network-structure"]
  - text: "A state-level exact test pooling all 78 schools found significantly fewer suicides in intervention vs. control schools (p=0.047), but a stricter test limited to the 72 schools randomized in matched pairs found no significant difference (p=0.150), indicating results were sensitive to statistical model choice."
    evidence: "rct"
    support_strength: "low-to-moderate"
    outcomes: ["suicidal-ideation"]
    predictors: ["intervention", "sampling-method"]
  - text: "Across the underlying trials, Sources of Strength's benefits depended on implementation fidelity: one trial showed short-term increases in student help-seeking and adult support that were lost as fidelity declined, and the program became potentially iatrogenic for ninth-graders in low-fidelity schools, whereas a later trial with expanded adult mentor training showed more consistent reductions in suicidal behaviors."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["help-seeking", "suicidal-ideation"]
    predictors: ["intervention", "peer-mentoring", "social-support"]
population:
  who: "High school students across 78 schools in three pooled cluster-randomized trials of the Sources of Strength suicide prevention program"
  where: ["USA"]
  when: "2007-2019 (Georgia, North Dakota, New York, and Colorado trial cohorts)"
  n: 39960
  sector: ["education"]
  sample_notes: >
    Pooled analysis of three separately conducted cluster RCTs (school-level randomization,
    matched pairs with 6 schools unpaired due to logistics); trials varied in duration (one
    semester vs. two school years) and in state/region, which the authors note complicates
    direct synthesis; total student rosters across trials = 39,960.
limitation:
  primary: "Suicide mortality is a rare outcome, giving the exact tests low statistical power, and results were inconsistent across the two statistical models used (significant in the more inclusive state-level test, non-significant in the stricter matched-pairs test)."
  others:
    - "Trials differed in active study duration (one school semester vs. two school years), and no adjustment was made for this variability because trial 1 had zero deaths."
    - "Only three trials were available, making it difficult to disentangle effects of trial length or other between-trial differences from the intervention effect."
    - "Low implementation fidelity in one trial was associated with potentially adverse (iatrogenic) effects on suicidal behavior in younger students, raising concern that mortality effects could also be fidelity-dependent."
risk_of_bias: "low"
relevance_to_project: >
  Provides RCT-level evidence that a scalable, peer-led social-network intervention
  (training key opinion leaders to spread help-seeking norms through friendship networks)
  can plausibly reduce the most severe outcome (suicide mortality), directly informing SNH's
  interest in network-structure-based interventions and upstream suicide-prevention design;
  the fidelity-dependence finding is a caution for any SNH intervention relying on peer
  leaders or champions.
tags:
  topic: ["suicide-prevention", "community-health", "social-support"]
  method: ["rct", "cluster-randomized", "meta-analytic-pooling"]
  population: ["adolescents", "school-based"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Impact of Sources of Strength on Adolescent Suicide Deaths Across Three Randomized Trials/Impact of Sources of Strength on Adolescent Suicide Deaths Across Three Randomized Trials.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Impact of Sources of Strength on Adolescent Suicide Deaths Across Three Randomized Trials.pdf"
  notes: null
