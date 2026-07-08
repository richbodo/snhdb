id: "speed-2025-open-source-maintainers-are-really-feeling"
title: "Open source maintainers are really feeling the squeeze"
authors:
  - "Speed, Richard"
year: 2025
doi: null
venue: {type: "other", name: "The Register", volume: null, issue: null, pages: null}
citation: "Speed (2025). Open source maintainers are really feeling the squeeze. The Register."
article_type: "commentary"
method: {design: "case-study", approach: "interview", evidence_level: "weak", preregistered: false}
gist: >
  This Register news article surveys the state of open source maintainer burnout as of early
  2025, built around quotes from the State Of Open Conference (SOO), the abrupt resignation
  of Asahi Linux lead Hector Martin, and interviews with maintainers (Jamie Tanna) and
  researchers (Google's Sophia Vargas, Kubernetes maintainers Kat Cosgrove and Jeremy
  Rickard). It cites external survey data showing widespread maintainer overload and abuse
  from entitled users, and argues that pay alone will not fix the problem — many projects
  need more contributors for non-code labor (mentorship, triage, community management) as
  much as money.
claims:
  - text: "The 2024 Tidelift State of the Open Source Maintainer survey found that roughly 60% of maintainers had either quit or were considering quitting, cited as evidence of chronic under-support relative to the growing enterprise appetite for open source software."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["turnover", "burnout"]
    predictors: ["workload", "organizational-culture"]
  - text: "In an informal survey of Kubernetes project contributors (explicitly described by the researchers as too small to be statistically significant), 70% of respondents who observed abuse directed at maintainers said they had considered whether to keep contributing to the project."
    evidence: "cross-sectional"
    support_strength: "speculative"
    outcomes: ["turnover", "community-engagement"]
    predictors: ["organizational-culture", "psychological-safety"]
  - text: "Analysis referenced from the Linux Foundation/Harvard Census II report indicates that even widely used, 'critical infrastructure' open source projects are typically maintained by very few people, often with a single person doing most of the work, concentrating burnout and continuity risk."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "turnover"]
    predictors: ["open-source-maintenance", "workload"]
population:
  who: "Open source maintainers and contributors discussed via conference talks and interviews (e.g., Jamie Tanna of oapi-codegen, Hector Martin of Asahi Linux, Kubernetes maintainers Kat Cosgrove and Jeremy Rickard), plus survey populations cited secondhand (Tidelift maintainer respondents, Linux Foundation Census II project contributors)."
  where: []
  when: "2024-2025"
  n: null
  sector: ["technology", "open-source"]
  sample_notes: >
    This is a journalistic article, not a primary study: it synthesizes conference quotes,
    individual interviews, and citations to external survey reports rather than presenting
    its own sampled data; underlying survey sample sizes and response rates are not given in
    the article.
limitation:
  primary: "The article is journalism, not primary research — it aggregates quotes and secondhand citations of other organizations' surveys/reports without presenting original methodology, sampling, or data."
  others:
    - "The Kubernetes maintainer survey it cites is explicitly flagged by its own researchers as too small to be statistically significant."
    - "No details on response rates, sampling frames, or measurement instruments are provided for the Tidelift or Linux Foundation figures it references."
risk_of_bias: "high"
relevance_to_project: >
  Gives the SNH project current, quotable texture on maintainer burnout mechanisms — abusive
  user interactions, chronic under-resourcing, and concentration of workload on very few
  contributors ('bus factor') — and flags two primary sources worth pulling directly (2024
  Tidelift maintainer survey; Linux Foundation/Harvard Census II) for harder evidence on
  open-source maintainer turnover and burnout.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["qualitative", "secondary-data"]
  population: ["open-source-maintainers", "open-source-contributors"]
source:
  markdown: "Papers_Data/Articles/MD/Open Source Maintainers Are Really Feeling the Squeeze/Open Source Maintainers Are Really Feeling the Squeeze.md"
  pdf: "papers/Articles/Open Source Maintainers Are Really Feeling the Squeeze.pdf"
  notes: "no-doi: web article / no registered DOI found"
