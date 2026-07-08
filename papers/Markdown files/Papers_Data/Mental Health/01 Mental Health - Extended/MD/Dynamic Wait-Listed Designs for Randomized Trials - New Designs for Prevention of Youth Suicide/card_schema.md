id: "brown-2006-dynamic-wait-listed-designs-for-randomized"
title: "Dynamic wait-listed designs for randomized trials: new designs for prevention of youth suicide"
authors:
  - "Brown, C Hendricks"
  - "Wyman, Peter A"
  - "Guo, Jing"
  - "Peña, Juan"
year: 2006
doi: "10.1191/1740774506cn152oa"
venue: {type: "journal", name: "Clinical Trials", volume: 3, issue: 3, pages: "259-271"}
citation: "Brown et al. (2006). Dynamic wait-listed designs for randomized trials: new designs for prevention of youth suicide. Clinical Trials, 3(3), 259-271. https://doi.org/10.1191/1740774506cn152oa"
article_type: "methods"
method: {design: "design-report", approach: "modelling", evidence_level: "moderate", preregistered: false}
gist: >
  This paper introduces the 'dynamic wait-listed design,' a generalization of the classic
  randomized wait-listed trial in which units (e.g., schools) are assigned to intervention
  at multiple random time points rather than just two. Using Poisson power calculations, the
  authors show this design nearly always increases statistical power over a standard wait-
  listed design, with efficiency gains ranging from 33% to 100% depending on effect size and
  time-varying background rates. They illustrate the method with an ongoing school-based
  gatekeeper training (QPR) trial for youth suicide prevention in a Georgia school district.
claims:
  - text: "Dynamic wait-listed designs always yield higher statistical power than a traditional two-phase wait-listed design; efficiency gains are typically 33% and can approach 100% when the intervention effect is large or background rate variation across time is low."
    evidence: "design-report"
    support_strength: "moderate"
    outcomes: ["measurement"]
    predictors: ["intervention"]
  - text: "Converting the Georgia gatekeeper trial's second phase from a fixed wait-list to a dynamic design raises statistical power to detect a 23% increase in suicidal-youth referral rates (vs. needing a 32% increase under the standard design at 80% power), equivalent to adding six more schools to the study without added cost."
    evidence: "design-report"
    support_strength: "moderate"
    outcomes: ["help-seeking"]
    predictors: ["intervention", "network-structure"]
  - text: "Baseline surveillance data from the district showed roughly 6% of middle/high schoolers reported a suicide attempt in the past year (~3,600 of 60,000 students), yet school staff successfully identified and referred only an estimated 5% of these suicidal youth (193/3,600) prior to gatekeeper training."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["help-seeking", "suicidal-ideation"]
    predictors: ["intervention", "sampling-method"]
population:
  who: "Middle and high school staff (~2,500 in early-intervention schools) and students (ages 11-18) in 32 schools of a large Georgia public school district, used as the applied case for a QPR gatekeeper-training suicide-prevention trial that motivated the new statistical design."
  where: ["USA (Georgia)"]
  when: "2003-2006 (trial began January 2004; baseline surveys 2003-2004 school year)"
  n: 60000
  sector: ["education", "mental-health-services"]
  sample_notes: >
    Applied example is a real, funded (NIMH) cluster-randomized wait-listed trial in 32
    schools stratified by school level and prior crisis-referral rate; staff baseline survey
    used a random 10% sample per school; student suicidality data came from an anonymous
    online survey with only a 'modest fraction' of eligible eighth/tenth graders completing
    it, limiting representativeness. The paper's main content, however, is
    statistical/mathematical derivation, not an empirical outcome study.
limitation:
  primary: "Like all wait-listed designs, the dynamic version can only evaluate short-term intervention impact, since by design every unit eventually receives the intervention and no long-term control group remains."
  others:
    - "Power gains are derived under Poisson/gamma-Poisson modeling assumptions (count or rate outcomes with time-varying but exchangeable background rates); benefits are much smaller or absent for single-measurement or non-count outcomes."
    - "The design is inappropriate when high-risk participants might withdraw before receiving a delayed intervention (e.g., trials in individuals with prior suicide attempts)."
    - "The Georgia trial application is illustrative/prospective in this paper (power projections), not a completed outcome evaluation of the QPR program's effect on suicide referrals."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This paper is a statistical/design methods reference relevant to how SNH-adjacent
  prevention or intervention trials (e.g., gatekeeper training, peer-support programs,
  community-based interventions) could be evaluated more efficiently when outcomes are low-
  base-rate counts (such as help-seeking, crisis referrals, or suicidal ideation); it offers
  a concrete design pattern for staged rollout studies that also improves logistics of
  training delivery, which is analogous to phased deployment of SNH interventions across
  teams or communities.
tags:
  topic: ["suicide-prevention", "methodology", "measurement"]
  method: ["design-report", "modelling"]
  population: ["adolescents"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Dynamic Wait-Listed Designs for Randomized Trials - New Designs for Prevention of Youth Suicide/Dynamic Wait-Listed Designs for Randomized Trials - New Designs for Prevention of Youth Suicide.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Dynamic Wait-Listed Designs for Randomized Trials - New Designs for Prevention of Youth Suicide.pdf"
  notes: null
