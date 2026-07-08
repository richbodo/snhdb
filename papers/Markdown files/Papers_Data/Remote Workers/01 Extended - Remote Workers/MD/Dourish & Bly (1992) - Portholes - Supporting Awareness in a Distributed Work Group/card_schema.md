id: "dourish-1992-portholes"
title: "Portholes"
authors:
  - "Dourish, Paul"
  - "Bly, Sara"
year: 1992
doi: "10.1145/142750.142982"
venue: {type: "conference", name: "Proceedings of the SIGCHI conference on Human factors in computing systems  - CHI '92", volume: null, issue: null, pages: "541-547"}
citation: "Dourish et al. (1992). Portholes. Proceedings of the SIGCHI conference on Human factors in computing systems  - CHI '92, 541-547. https://doi.org/10.1145/142750.142982"
article_type: "empirical"
method: {design: "case-study", approach: "ethnography", evidence_level: "weak", preregistered: false}
gist: >
  Describes Portholes, a 1992 CSCW media-space system that shares regularly-updated snapshot
  images (plus e-mail/audio 'snippet' links) between two distributed Xerox research sites to
  support passive awareness of remote colleagues. Based on informal field observation plus a
  3-day diary/questionnaire with the system's early users, the authors report that people
  used Portholes both as a lightweight information tool (checking colleague availability,
  predicting free time) and as a shared community space (informal 'sightings', personal
  audio snippets), and that use coincided with increased informal, unprompted cross-site
  communication and a reported sense of connection despite few prior direct interactions
  between the two sites.
claims:
  - text: "Of 15 users asked to log Portholes use over a 3-day period and complete a questionnaire, 11 responded, and all but one reported using the pvc and/or edison clients at least a few times a day during that period."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["social-presence", "collaboration"]
    predictors: ["network-structure"]
  - text: "Users described two main modes of use -- Portholes as an information tool (quickly checking a remote colleague's availability to avoid wasted visits/calls) and Portholes as a community (seeing colleagues arrive/leave, sharing whimsical audio 'snippets', 'feeling some connection' to people at the remote site), including one exchange where a Saturday worker messaged 'It's nice to know I'm not completely alone!'"
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["sense-of-belonging", "isolation", "communication"]
    predictors: ["social-support"]
  - text: "Authors report that informal, unprompted cross-site communication among the ~22 distributed users (10 at PARC, 12 at EuroPARC) increased after Portholes deployment, and server statistics collected four months after the initial questionnaire indicated participants remained regular users."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["communication", "collaboration"]
    predictors: ["network-structure", "embodiment"]
population:
  who: "Members of two linked media-space research groups using the Portholes awareness system: 10 users at Xerox PARC (Palo Alto) and 12 at Rank Xerox EuroPARC (Cambridge, UK); a 15-person subset was asked to diary/answer a questionnaire, of whom 11 responded."
  where: ["USA", "UK"]
  when: "1991-1992"
  n: 22
  sector: ["technology"]
  sample_notes: >
    Convenience sample of the researchers' own colleagues and lab members who were early
    adopters of an in-house prototype; questionnaire response rate 11/15; authors are also
    the system's designers, so evaluation is informal, anecdotal, and self-selected rather
    than a controlled study.
limitation:
  primary: "Extremely small, self-selected sample (22 total users, 11 questionnaire respondents) evaluated with informal/anecdotal field observations and a short 3-day diary period, with no control condition or validated outcome measures, so claims about awareness fostering community are suggestive rather than demonstrated."
  others:
    - "Authors are also the system's designers and site colleagues of the participants, creating potential evaluator/social-desirability bias."
    - "No standardized measures of loneliness, belonging, or wellbeing were used -- evidence is qualitative quotes and usage anecdotes."
    - "Early-stage prototype with reliability problems (unreliable images, slow updates) that participants themselves flagged as limiting use, confounding assessment of the awareness concept itself."
risk_of_bias: "high"
relevance_to_project: >
  A foundational CSCW paper for the SNH project's interest in ambient/passive-awareness
  features (presence indicators, activity feeds) as a design lever for reducing remote-
  worker isolation: it offers early qualitative evidence that low-bandwidth awareness of
  distributed colleagues can increase informal communication and produce a subjective 'sense
  of community,' but with weak methodological rigor that should temper how strongly the
  project cites it as causal evidence.
tags:
  topic: ["remote-work", "social-presence", "community-health", "isolation", "collaboration"]
  method: ["qualitative", "case-study"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group.pdf"
  notes: null
