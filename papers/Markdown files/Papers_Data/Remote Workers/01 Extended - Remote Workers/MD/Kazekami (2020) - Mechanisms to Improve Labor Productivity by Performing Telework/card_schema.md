id: "kazekami-2020-mechanisms-to-improve-labor-productivity-by"
title: "Mechanisms to improve labor productivity by performing telework"
authors:
  - "Kazekami, Sachiko"
year: 2020
doi: "10.1016/j.telpol.2019.101868"
venue: {type: "journal", name: "Telecommunications Policy", volume: 44, issue: 2, pages: "101868"}
citation: "Kazekami (2020). Mechanisms to improve labor productivity by performing telework. Telecommunications Policy, 44(2), 101868. https://doi.org/10.1016/j.telpol.2019.101868"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using two-wave panel data from the Japanese Panel Study of Employment Dynamics (2017-2018)
  and fixed-effect and difference-in-differences models, this study traces the mechanisms by
  which telework raises labor productivity in Japan. It finds an inverted-U relationship
  between weekly telework hours and productivity, shows that the productivity gain runs
  mainly through increased life satisfaction (not happiness or work satisfaction), and shows
  telework is most valuable for workers with long or crowded commutes, even though it also
  raises the stress of balancing work and domestic chores.
claims:
  - text: "For continuing teleworkers, each additional weekly telework hour raised labor productivity by about ¥160 (~US$1.48) per hour (β=0.0160, p<.05), but the squared telework-hours term was significantly negative (β=-0.000392, p<.05), indicating productivity gains reverse once telework hours become too high."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Telework significantly increased life satisfaction, happiness, and work satisfaction (order-logit coefficients on 1-5 dissatisfaction scales: life satisfaction β=-0.897***, work satisfaction β=-1.240***, happiness β=-0.839***), but only life satisfaction significantly fed through to raise labor productivity (β=-0.00464, p<.10); happiness and work satisfaction had no significant productivity effect."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "job-satisfaction", "wellbeing"]
    predictors: ["remote-work-intensity"]
  - text: "The productivity benefit of telework was concentrated among long or crowded commuters: telework hours significantly raised productivity for workers commuting more than 60 minutes (β=0.0184-0.0201, p<.01) and for those commuting by crowded train/bus (β=0.0249-0.0252, p<.01), but had no significant effect for workers with commutes under 60 minutes or who commuted by car, bicycle, or foot."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
population:
  who: "Japanese regular employees aged under 60 from the Japanese Panel Study of Employment Dynamics; roughly 9,200 regular employees answered each year, with telework subsamples of 219 (started telework), 291 (continued telework), and 171 (stopped telework)"
  where: ["Japan"]
  when: "January 2017 and January 2018 (covering 2016-2017 employment)"
  n: 9200
  sector: ["general-workforce"]
  sample_notes: >
    Nationally representative online panel benchmarked to the Labor Force Survey for
    gender/age/employment-type/region distribution, but the teleworker subsamples analyzed
    in the productivity mechanism models are small (171-291 workers), and only regular (not
    non-regular) employees under 60 are included.
limitation:
  primary: "Telework subsamples are small (171-291 workers) and most teleworkers telework only a few hours per week, so the study cannot establish effects for full-time or high-frequency telework, and results for workers who start or stop telework are often statistically inconclusive."
  others:
    - "Fixed-effect and difference-in-differences designs reduce but do not eliminate self-selection into telework as an alternative explanation"
    - "The trivial-duties/interruption-avoidance mechanism produced counterintuitive, often insignificant results, weakening that part of the causal story"
    - "Findings are specific to Japan's telework norms, commuting patterns, and family-care policy context, limiting generalizability"
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, panel-data evidence that telework's productivity payoff is
  nonlinear (too many telework hours erode it) and operates through life satisfaction and
  commute-stress relief rather than through happiness or job discretion, which is directly
  useful for calibrating SNH guidance on remote-work intensity and for choosing which
  wellbeing measures (life satisfaction vs. happiness) actually track productivity outcomes.
tags:
  topic: ["remote-work", "productivity", "wellbeing", "work-life-balance"]
  method: ["longitudinal", "secondary-data"]
  population: ["japan", "office-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework.pdf"
  notes: null
