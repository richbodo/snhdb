id: "l-2022-the-effects-of-remote-work-on"
title: "The effects of remote work on collaboration among information workers"
authors:
  - "L, Yang"
  - "D, Holtz"
  - "S, Jaffe"
  - "S, Suri"
  - "S, Sinha"
  - "J, Weston"
  - "C, Joyce"
  - "N, Shah"
  - "K, Sherman"
  - "B, Hecht"
  - "J, Teevan"
year: 2022
doi: "10.1530/ey.19.15.13"
venue: {type: "journal", name: "Yearbook of Paediatric Endocrinology", volume: null, issue: null, pages: null}
citation: "L et al. (2022). The effects of remote work on collaboration among information workers. Yearbook of Paediatric Endocrinology. https://doi.org/10.1530/ey.19.15.13"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  Using a natural experiment created by Microsoft's company-wide COVID-19 work-from-home
  mandate, this study analyzes six months of telemetry data (email, IM, calls, calendars)
  from 61,182 US employees to causally estimate how firm-wide remote work reshapes
  collaboration networks and communication. It finds that remote work made collaboration
  networks more static and siloed—reducing cross-group and bridging ties while increasing
  time spent with strong ties—and shifted communication from synchronous (meetings, calls)
  toward asynchronous (email, IM) channels, patterns the authors argue plausibly impede the
  flow of new information across the organization.
claims:
  - text: "Firm-wide remote work decreased the number of bridging ties (ties spanning structural holes) by 0.09FV (P<0.001) and the share of collaboration time spent with bridging ties by 0.41FV (P<0.001), while decreasing cross-group ties by 0.04FV and cross-group time share by 0.26FV, indicating networks became more siloed."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
  - text: "Firm-wide remote work decreased scheduled meeting hours by 0.16FV (P<0.001) and net synchronous video/audio communication by 0.05FV (P=0.006), while increasing emails sent by 0.08FV (P<0.001) and instant messages sent by 0.50FV (P<0.001), a shift from synchronous toward asynchronous communication."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["communication", "collaboration"]
    predictors: ["remote-work-intensity"]
  - text: "Remote work made collaboration networks more static: the number of connections churned per month fell by 0.05FV (P=0.006) and connections added fell by 0.04FV (P=0.015), with the share of time spent with newly added ties dropping by 0.29FV (P<0.001), reducing opportunities to benefit from new or reactivated ties."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "61,182 US Microsoft employees (excluding senior leadership and teams handling highly sensitive data), spanning software/hardware engineering, marketing, and business operations roles"
  where: ["United States"]
  when: "December 2019 - June 2020"
  n: 61182
  sector: ["technology", "corporate"]
  sample_notes: >
    Single large US tech firm (Microsoft); natural experiment from the company-wide COVID-19
    WFH mandate (March-April 2020); sample reweighted via coarsened exact matching (CEM)
    comparing pre-pandemic remote vs. office workers; final remote:non-remote ratio 1:4.6;
    excludes senior leadership and non-US employees.
limitation:
  primary: "Results are drawn from a single large US technology firm (Microsoft) over a short three-month post-mandate window, so generalizability to other sectors, countries, firm sizes, or long-term (rather than pandemic-onset) remote work is uncertain."
  others:
    - "Productivity and innovation outcomes were not directly measured, only inferred from network and communication changes."
    - "Causal identification depends on untestable identifying assumptions (parallel trends, exogeneity, additive separability of ego/collaborator/COVID effects)."
    - "Cannot fully disentangle remote-work effects from other concurrent COVID-19 disruptions (e.g., caregiving, stress) despite the difference-in-differences design's attempt to do so."
risk_of_bias: "low"
relevance_to_project: >
  Provides causal, large-N evidence that mandated full-time remote work directly reduces
  bridging- and weak-tie collaboration and increases network fragmentation and staticness—a
  core mechanism-level finding for SNH's argument that remote/hybrid work design must
  actively counteract siloing (e.g., via engineered cross-group touchpoints) rather than
  assume ties translate unchanged online.
tags:
  topic: ["remote-work", "hybrid-work", "collaboration", "productivity", "measurement"]
  method: ["quasi-experimental", "secondary-data", "longitudinal"]
  population: ["tech-workers", "remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Effects of Remote Work on Collaboration Among Information Workers/The Effects of Remote Work on Collaboration Among Information Workers.md"
  pdf: "papers/Remote Workers/The Effects of Remote Work on Collaboration Among Information Workers.pdf"
  notes: null
