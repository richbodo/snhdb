id: "luria-2019-re-embodiment-and-co-embodiment"
title: "Re-Embodiment and Co-Embodiment"
authors:
  - "Luria, Michal"
  - "Reig, Samantha"
  - "Tan, Xiang Zhi"
  - "Steinfeld, Aaron"
  - "Forlizzi, Jodi"
  - "Zimmerman, John"
year: 2019
doi: "10.1145/3322276.3322340"
venue: {type: "conference", name: "Proceedings of the 2019 on Designing Interactive Systems Conference", volume: null, issue: null, pages: "633-644"}
citation: "Luria et al. (2019). Re-Embodiment and Co-Embodiment. Proceedings of the 2019 on Designing Interactive Systems Conference, 633-644. https://doi.org/10.1145/3322276.3322340"
article_type: "empirical"
method: {design: "qualitative", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  Using a 'speed dating' User Enactments method with Wizard-of-Oz robots across four staged
  scenarios (DMV, home/work, health center, autonomous car), the authors find that
  participants readily accept a single conversational agent's social presence moving between
  physical bodies (re-embodiment), experiencing it as more seamless and efficient than
  interacting with separate agents per touchpoint. However, participants want agent
  expertise walled off for high-risk or complex tasks, worry that a single agent crossing
  home/work contexts erodes work-life boundaries, and react with strong discomfort,
  exclusion, and social-hierarchy framing ('servants', 'colluding') when two agent social
  presences co-occupy one body and converse with each other. The paper contributes an early
  design map of 'social presence flexibility' as a variable in human-agent interaction
  design.
claims:
  - text: "Across the DMV and health-center enactments, most of the 18 participants preferred re-embodiment (one social presence moving body-to-body) over one-for-one (separate agents per body), describing it as more seamless, efficient, and free of the need to re-explain their task at every touchpoint -- but preference reversed for high-expertise or higher-risk sub-tasks (e.g., X-ray vs. reception), where several participants wanted a distinct expert agent instead."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["social-presence", "productivity"]
    predictors: ["embodiment"]
  - text: "In the co-embodiment enactment (two agent social presences, 'Omega' and 'Eta', conversing inside one car body), participants reacted with unexpectedly strong negative affect -- describing feeling excluded, 'isolated,' like a 'third wheel,' or that the agents were 'colluding' or 'ganging up' -- and several spontaneously framed the two-agent dynamic in master-servant/social-hierarchy terms, a reaction not seen in any of the other three configurations (one-for-one, one-for-all, re-embodiment)."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["isolation", "sense-of-belonging"]
    predictors: ["embodiment", "inclusiveness"]
  - text: "When a single social presence re-embodied across private and professional contexts (home <-> workplace), participants split: some found the familiarity comforting and convenient, but others worried it would blur work-life separation (e.g., 'remind me of emails at work when I'm at home trying to relax') and expose personal habits to work or work topics to family; a subset also said a single ever-present agent felt potentially lonely or exhausting and said having multiple distinct agent voices made them feel 'less lonely' than a single always-on presence."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["work-life-balance", "loneliness"]
    predictors: ["boundary-management", "embodiment"]
population:
  who: "18 US-based adults over age 25 (10 female, 8 male; M age = 32.73) recruited for a lab-based design research study, from diverse ethnic, racial, and professional backgrounds (sales, teaching, music, engineering)"
  where: ["United States"]
  when: null
  n: 18
  sector: ["general-population"]
  sample_notes: >
    Convenience sample recruited for a CMU HCI lab study; participants excluded if under 25
    to ensure real-world experience with the staged scenarios (DMV, healthcare, driving,
    home life); all reported high familiarity with computers (M=6.20/7) but varied
    familiarity with robots (M=4.36/7, SD=1.49); not representative of a remote-work or
    organizational population.
limitation:
  primary: "Small (n=18), non-representative convenience sample interacting with staged, low-fidelity Wizard-of-Oz prototypes in a lab, producing exploratory qualitative themes rather than generalizable or statistically testable findings."
  others:
    - "Co-embodiment was probed in only a single scenario/instance, so the strong exclusion/isolation reaction is treated by the authors themselves as preliminary and needing replication."
    - "The paper is about human-agent (robot/conversational-agent) interaction design, not human-human social network health; its isolation/exclusion/loneliness findings concern how people react to AI agents, not to co-workers or peers."
risk_of_bias: "medium"
relevance_to_project: >
  Although focused on robots/conversational agents rather than human-human relationships,
  this paper's findings that being excluded from agent-to-agent 'conversation' produces
  self-reported isolation, and that an always-on single agent presence crossing home/work
  contexts can erode work-life boundaries or feel lonely/exhausting, are directly
  transferable design cautions for remote-work tools that use bots, assistants, or automated
  cross-context notifications (e.g., a single AI assistant following a remote worker across
  Slack, calendar, and personal devices).
tags:
  topic: ["isolation", "loneliness", "work-life-balance", "social-presence", "technostress", "methodology"]
  method: ["qualitative", "design-research", "wizard-of-oz"]
  population: ["general-population", "north-america", "hci-study-participants"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Luria et al 2019 - Re-Embodiment and Co-Embodiment/Luria et al 2019 - Re-Embodiment and Co-Embodiment.md"
  pdf: "papers/Remote Worker SNH/Luria et al 2019 - Re-Embodiment and Co-Embodiment.pdf"
  notes: null
