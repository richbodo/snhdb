id: "ralph-2020-pandemic-programming"
title: "Pandemic programming"
authors:
  - "Ralph, Paul"
  - "Baltes, Sebastian"
  - "Adisaputri, Gianisa"
  - "Torkar, Richard"
  - "Kovalenko, Vladimir"
  - "Kalinowski, Marcos"
  - "Novielli, Nicole"
  - "Yoo, Shin"
  - "Devroey, Xavier"
  - "Tan, Xin"
  - "Zhou, Minghui"
  - "Turhan, Burak"
  - "Hoda, Rashina"
  - "Hata, Hideaki"
  - "Robles, Gregorio"
  - "Milani Fard, Amin"
  - "Alkadhi, Rana"
year: 2020
doi: "10.1007/s10664-020-09875-y"
venue: {type: "journal", name: "Empirical Software Engineering", volume: 25, issue: 6, pages: "4927-4961"}
citation: "Ralph et al. (2020). Pandemic programming. Empirical Software Engineering, 25(6), 4927-4961. https://doi.org/10.1007/s10664-020-09875-y"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A 12-language survey of 2225 software developers and other software professionals across
  53 countries found that emotional wellbeing and perceived productivity both declined
  significantly after switching to working from home during the COVID-19 pandemic, and that
  the two declines were closely intertwined. A structural equation model shows that pandemic
  fear, poor disaster preparedness, and poor home-office ergonomics drive these declines,
  that isolation is the strongest predictor of fear, and that women, parents, and people
  with disabilities appear disproportionately affected. The authors also find little
  consensus among developers about which organizational support actions actually help,
  arguing against one-size-fits-all interventions.
claims:
  - text: "Both wellbeing and perceived productivity declined significantly after developers switched to working from home due to COVID-19 (Wilcoxon signed-rank test, p<.001; wellbeing Cliff's delta=0.12±0.03, productivity delta=0.13±0.03), and change in wellbeing and change in productivity were strongly, directly related in the structural model (path coefficient=0.822, z=18.361, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "productivity", "stress"]
    predictors: ["remote-work-intensity", "technostress"]
  - text: "In the SEM, home office ergonomics and pandemic-related fear predicted change in wellbeing (ergonomics beta=0.125, p<.001; fear beta=-0.031, p=.011), while ergonomics and disaster preparedness predicted change in productivity (ergonomics beta=0.242, p<.001; disaster preparedness beta=0.097, p=.005); isolation (not leaving home except for necessities) was the strongest predictor of fear (beta=0.502, p<.001), and disaster preparedness reduced fear (beta=-0.336, p=.002)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "productivity", "stress"]
    predictors: ["isolation", "home-office-ergonomics", "disaster-preparedness"]
  - text: "Exploratory subgroup analyses suggest disproportionate effects on protected groups: women reported significantly more fear (beta=0.273, p=.025); people with disabilities had less-prepared, less-ergonomic setups and more fear; and people living with young children had significantly less ergonomic home offices (beta=-0.163, p<.001), with effects sometimes conflicting (e.g., disability had both a direct positive and an indirect negative effect on productivity)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["stress", "productivity", "wellbeing"]
    predictors: ["caregiving-responsibilities", "disability-status", "gender"]
population:
  who: "Software developers and other software professionals worldwide who switched from working in an office to working from home because of COVID-19 (most respondents self-identified as developers)"
  where: ["Germany", "Russia", "Brazil", "Italy", "United States", "South Korea", "Belgium", "China", "Turkey", "India", "and 43 other countries (53 total)"]
  when: "March 27 - April 16, 2020"
  n: 2225
  sector: ["software-development", "technology"]
  sample_notes: >
    Convenience/snowball sampling via an anonymous 12-language questionnaire with country-
    specific advertising by a 17-author international team; 2668 total responses, 2225
    usable after excluding non-inclusion-criteria and blank responses. Sample skewed male
    (81% vs 18% female, 1% non-binary), 94% full-time employed, median age 30-34; response-
    bias check (completers vs non-completers of open-ended items) found only small, near-
    negligible differences (eta-squared <=0.009).
limitation:
  primary: "Wellbeing and productivity 'before' working from home were measured retrospectively via self-report at the same time as the 'after' measure, so causal precedence and recall accuracy cannot be fully verified despite the sophisticated SEM analysis."
  others:
    - "Non-random convenience/snowball sampling; despite 12-language localization the sample is unevenly distributed across countries (e.g., far more German than Southeast Asian respondents) and any random sample of developers is inherently hard to achieve."
    - "Perceived productivity (HPQ scale) is not the same as actual/objective productivity, and its validity in software development or during pandemics specifically is unconfirmed."
    - "Google Forms platform limited the ability to detect response bias (no partial-response or bounce-rate data, no protection against multiple submissions)."
risk_of_bias: "medium"
relevance_to_project: >
  Provides one of the largest quantitative models linking crisis-driven remote work to
  wellbeing and productivity, empirically showing isolation as a strong predictor of
  pandemic-related fear and home-office ergonomics/disaster-preparedness as levers
  organizations can act on; its finding of no organizational-support action universally
  rated helpful (Table 7) directly informs SNH's case for individualized rather than one-
  size-fits-all interventions.
tags:
  topic: ["remote-work", "wellbeing", "isolation", "productivity", "mental-health", "technostress"]
  method: ["survey", "cross-sectional"]
  population: ["software-developers", "international-sample", "remote-work"]
source:
  markdown: "Papers_Data/Academic/MD/How COVID-19 affects software developers and how their organizations can help/How COVID-19 affects software developers and how their organizations can help.md"
  pdf: "papers/Academic/How COVID-19 affects software developers and how their organizations can help.pdf"
  notes: null
