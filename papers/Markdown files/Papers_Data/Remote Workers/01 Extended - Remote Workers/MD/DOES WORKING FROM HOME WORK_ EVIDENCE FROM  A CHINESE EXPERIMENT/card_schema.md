id: "bloom-2015-does-working-from-home-work-evidence"
title: "Does Working from Home Work? Evidence from a Chinese Experiment *"
authors:
  - "Bloom, Nicholas"
  - "Liang, James"
  - "Roberts, John"
  - "Ying, Zhichun Jenny"
year: 2015
doi: "10.1093/qje/qju032"
venue: {type: "journal", name: "The Quarterly Journal of Economics", volume: 130, issue: 1, pages: "165-218"}
citation: "Bloom et al. (2015). Does Working from Home Work? Evidence from a Chinese Experiment *. The Quarterly Journal of Economics, 130(1), 165-218. https://doi.org/10.1093/qje/qju032"
article_type: "empirical"
method: {design: "rct", approach: "experiment", evidence_level: "very-strong", preregistered: false}
gist: >
  This is the landmark Ctrip field experiment (Bloom, Liang, Roberts, and Ying, QJE 2015):
  249 call-center volunteers were randomized by odd/even birthdate to work from home four
  days a week or stay fully office-based for nine months. Home working raised performance
  13% (9% from more minutes worked per shift via fewer breaks/sick days, 4% from more calls
  per minute in a quieter environment), cut attrition by half, and raised self-reported
  satisfaction, but cut promotion rates conditional on performance by roughly half. When
  Ctrip later let everyone choose their location, over half of participants switched (many
  citing loneliness), and selection effects nearly doubled the measured gain to 22%.
claims:
  - text: "Working from home increased overall employee performance by 13% (0.232 SD, p<0.01) during the nine-month RCT, with 9.2% coming from more minutes worked per shift (fewer breaks, sick days, and late starts) and about 3.3-4% from more calls handled per minute, attributed to a quieter home environment."
    evidence: "rct"
    support_strength: "very-strong"
    outcomes: ["productivity", "performance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Attrition among home workers fell to 17% versus 35% for the office-based control group over the experimental period (about a 50% relative reduction), and home workers reported significantly higher satisfaction, more positive attitude, and less work exhaustion on weekly surveys."
    evidence: "rct"
    support_strength: "very-strong"
    outcomes: ["turnover", "retention", "job-satisfaction", "burnout"]
    predictors: ["remote-work-intensity"]
  - text: "Working from home was associated with about a 50% lower promotion rate conditional on performance, and after the experiment ended over half of treatment-group volunteers and two-thirds of control-group volunteers who could freely choose declined to work from home, most citing loneliness and lack of social contact as the reason."
    evidence: "rct"
    support_strength: "strong"
    outcomes: ["turnover", "loneliness", "sense-of-belonging"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "996 call-center order-takers/placers/correctors in the airfare and hotel departments of Ctrip's Shanghai call center (a NASDAQ-listed, 16,000-employee Chinese travel agency); 249 volunteers who met eligibility (6+ months tenure, home broadband, private room) were randomized 131 treatment / 118 control."
  where: ["China"]
  when: "December 2010-August 2011 (nine-month experiment), with performance/attrition/promotion data followed through September 2012 and a follow-up survey in May 2013"
  n: 249
  sector: ["call-center", "travel-industry", "corporate"]
  sample_notes: >
    51% of the 994 eligible employees volunteered for WFH; randomization was by odd/even
    birthdate in a public lottery. Treatment/control balance was good (only 1 of 18
    characteristics differed at 5%, joint F-test p=.466). Findings are specific to a single
    large Chinese firm's routinized, individually-monitored call-center job and may not
    generalize to work requiring teamwork or less quantifiable output.
limitation:
  primary: "External validity is limited to highly routinized, individually monitored, easily quantified jobs (call-center work) at a single firm with an unusually comprehensive performance-tracking system; the authors explicitly caution the results may not extend to jobs requiring teamwork or in-person collaboration."
  others:
    - "Compliance with assigned WFH status was imperfect (80-90% of treatment group actually worked from home), so estimates are intention-to-treat rather than pure treatment-on-the-treated."
    - "Differential attrition (worse performers in the control group were more likely to quit) likely biases the estimated treatment effect downward, per the authors' own bounding analysis, though this does not undermine the main findings."
    - "Loneliness/isolation is documented only via employees' stated reasons for switching back to the office and satisfaction surveys, not a validated loneliness or social-support instrument."
risk_of_bias: "low"
relevance_to_project: >
  This is a rare randomized-controlled-trial-quality causal estimate that remote work can
  raise both productivity and satisfaction while measurably increasing loneliness and
  reducing promotion visibility -- directly informing the SNH project's core tension between
  remote-work benefits and social-connection/career-visibility costs, and giving a
  quantified, RCT-grade baseline (halved attrition, reduced promotion, loneliness-driven
  reselection) for any design or measurement work on remote-worker social health.
tags:
  topic: ["remote-work", "job-satisfaction", "productivity", "loneliness", "isolation"]
  method: ["rct"]
  population: ["call-center-workers", "china", "corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT.pdf"
  notes: null
