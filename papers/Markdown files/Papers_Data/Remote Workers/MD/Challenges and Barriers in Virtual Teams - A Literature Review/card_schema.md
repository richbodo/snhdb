id: "morrison-2020-challenges-and-barriers-in-virtual-teams"
title: "Challenges and barriers in virtual teams: a literature review"
authors:
  - "Morrison-Smith, Sarah"
  - "Ruiz, Jaime"
year: 2020
doi: "10.1007/s42452-020-2801-5"
venue: {type: "journal", name: "SN Applied Sciences", volume: 2, issue: 6, pages: null}
citation: "Morrison-Smith et al. (2020). Challenges and barriers in virtual teams: a literature review. SN Applied Sciences, 2(6). https://doi.org/10.1007/s42452-020-2801-5"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  A Kitchenham-style systematic literature review of 255 studies (identified via Google
  Scholar search plus citation snowballing) synthesizing the collaboration challenges faced
  by virtual teams. The review organizes challenges into five categories - geographical,
  temporal, and perceived distance, plus team configuration and worker diversity - and finds
  that distance-driven erosion of awareness, trust, and informal/face-to-face communication
  is the central mechanism degrading virtual-team cohesion and performance. It translates
  these findings into four groupware design implications: supporting common ground,
  facilitating communication, providing work transparency, and building lightweight,
  familiar technology.
claims:
  - text: "Synthesizing Olson and Olson's decade-spanning body of work, the review identifies ten recurring distance-related challenges to virtual collaboration - reduced awareness of colleagues, diminished motivational sense of presence, difficulty establishing trust, uneven technical competence, inadequate technical infrastructure, mismatched nature of work, absent explicit management, weak common ground, competitive (vs. cooperative) culture, and misaligned incentives - as the recurring factors driving virtual-team dysfunction."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "remote-work-intensity"]
  - text: "Trust is consistently harder to establish and maintain in geographically dispersed teams than co-located ones, with lasting downstream effects: corroded task coordination, decreased willingness to communicate, fewer members taking initiative, less feedback exchange, and increased perceived risk; the effect is most pronounced early in a project and tapers as the collaboration matures."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication", "sense-of-belonging"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Loss of informal, face-to-face contact (which accounts for up to 75 minutes of a typical co-located workday) reduces virtual teams' sense of cohesion and personal rapport and lowers affective commitment; unaddressed isolation is linked to declining contribution and participation as disengaged members further withdraw from the team."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "sense-of-belonging", "job-engagement"]
    predictors: ["remote-work-intensity", "social-support"]
population:
  who: "255 empirical, technical, and review papers on virtual/distributed team collaboration, identified via a systematic Google Scholar search (first 10 pages per query, ~1200 candidates screened) plus citation snowballing; predominantly HCI/CSCW and distributed software development literature."
  where: []
  when: null
  n: 255
  sector: ["technology", "knowledge-work"]
  sample_notes: >
    Included papers had to concern collaboration, contain empirical evidence, and report
    generalizable findings; excluded non-English papers, non-peer-reviewed work (e.g.,
    master's theses), off-topic papers, and duplicates. Single search engine (Google
    Scholar) used as the primary discovery tool rather than multiple bibliographic
    databases; concept saturation reported after ~8-9 result pages per query.
limitation:
  primary: "Reliance on Google Scholar as the sole systematic search engine (supplemented by snowballing) rather than triangulating across multiple bibliographic databases risks missing relevant studies and introduces selection bias despite the otherwise well-documented protocol."
  others:
    - "Synthesizes findings across highly heterogeneous virtual-team contexts (distributed software teams, scientific collaborations, general knowledge work) without meta-analytic pooling of effect sizes, leaving many conclusions narrative and several contradictory findings across primary studies explicitly unresolved (flagged as open questions)."
    - "No formal risk-of-bias or quality appraisal of the 255 included primary studies is reported."
risk_of_bias: "medium"
relevance_to_project: >
  Maps the specific mechanisms - erosion of awareness, trust, and informal contact under
  distance - by which remote and distributed work degrades belonging, cohesion, and
  engagement, giving the SNH project a synthesized causal chain from geographic/temporal
  distance to isolation. Its four design implications, especially 'provide mechanisms for
  work transparency' to counter feelings of disconnection and invisibility, are directly
  usable as concrete design requirements for SNH interventions targeting remote-worker
  isolation.
tags:
  topic: ["remote-work", "collaboration", "isolation", "social-support", "hybrid-work"]
  method: ["review-systematic"]
  population: ["remote-workers", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Challenges and Barriers in Virtual Teams - A Literature Review/Challenges and Barriers in Virtual Teams - A Literature Review.md"
  pdf: "papers/Remote Workers/Challenges and Barriers in Virtual Teams - A Literature Review.pdf"
  notes: null
