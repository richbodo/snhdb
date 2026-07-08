id: "barcomb-2020-uncovering-the-periphery-a-qualitative-survey"
title: "Uncovering the Periphery: A Qualitative Survey of Episodic Volunteering in Free/Libre and Open Source Software Communities"
authors:
  - "Barcomb, Ann"
  - "Kaufmann, Andreas"
  - "Riehle, Dirk"
  - "Stol, Klaas-Jan"
  - "Fitzgerald, Brian"
year: 2020
doi: "10.1109/tse.2018.2872713"
venue: {type: "journal", name: "IEEE Transactions on Software Engineering", volume: 46, issue: 9, pages: "962-980"}
citation: "Barcomb et al. (2020). Uncovering the Periphery: A Qualitative Survey of Episodic Volunteering in Free/Libre and Open Source Software Communities. IEEE Transactions on Software Engineering, 46(9), 962-980. https://doi.org/10.1109/tse.2018.2872713"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  Based on a qualitative survey (interviews with 11 community managers and 9 episodic
  volunteers across 13 FLOSS communities, triangulated with 50 supplemental documents), the
  paper argues that the core/periphery 'Onion model' oversimplifies peripheral contributors
  and proposes replacing it with the habitual/episodic volunteer distinction drawn from the
  general volunteering literature. It finds episodic volunteering (EV) is widespread across
  all types of FLOSS contribution (not just code), that five volunteering-retention
  constructs (motivation, social norms, psychological sense of community, satisfaction,
  community commitment) apply in FLOSS, and that no community studied had a deliberate
  strategy for managing or retaining episodic (as opposed to habitual) contributors.
claims:
  - text: "Episodic volunteering was observed in every type of FLOSS contribution examined (code, translation, documentation, events, evangelism, support) across all 13 communities studied, yet none of the community managers interviewed reported a deliberate strategy for recruiting or retaining episodic (versus habitual) volunteers."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["retention"]
    predictors: ["organizational-culture", "community-engagement"]
  - text: "Personal invitation, not formal recruitment channels, was the most common route into volunteering for non-code contributors; although an intake questionnaire suggested episodic volunteers did not see social norms (pressure/support from friends and family) as relevant to their participation, interview data showed several had actually started volunteering after a personal invitation from someone they knew."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["retention", "community-engagement"]
    predictors: ["social-norms", "social-support"]
  - text: "Satisfaction — especially feeling appreciated for one's contributions — was the reason most frequently cited by episodic volunteers and community managers for continued participation, and episodic volunteers who talked publicly about their FLOSS involvement were more inclined to report intention to remain, regardless of how long they had already been contributing."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["retention", "job-satisfaction"]
    predictors: ["sense-of-belonging", "community-engagement"]
population:
  who: "11 community managers (CM1–CM11) and 9 self-selected episodic volunteers (EV1–EV9, some active in multiple projects) drawn from 13 FLOSS communities (Mozilla, Perl Foundation, Chef, Red Hat, Bolt CMS, JSON-RPC Client, ownCloud, Zato, Butterfly Effect, Gnash, Django, KDE, TinyRPC), plus 50 supplemental documents (public interviews, web pages, mailing-list threads) for triangulation."
  where: []
  when: "Autumn 2014 to Spring 2017"
  n: 20
  sector: ["open-source"]
  sample_notes: >
    Theoretical/purposive sampling designed to span multi-/single-project and
    vendor-/community-oriented quadrants; community managers recruited via personal contacts
    and mailing-list ads; episodic volunteers self-selected through an open call on social
    media, mailing lists, and conferences (Mozfest, FOSDEM) tied to a parallel motivations
    survey, screened by self-reported episodic status and hours; contribution levels were
    cross-checked against commit counts for only about half of code-contributing
    participants; small, non-probabilistic sample not intended to be statistically
    representative.
limitation:
  primary: "Small, self-selected qualitative sample (20 interviewees across 13 communities) relying substantially on self-reported volunteering behavior and retrospective identification of episodic status, so the study can describe patterns but cannot establish causal or quantitative links between the five proposed retention constructs and actual retention."
  others:
    - "Exploratory design was built to test researcher-derived predictions from the general volunteering literature rather than to generate a fully independent theory, risking confirmation bias despite member checks and investigator triangulation"
    - "Most claims about contribution levels/motivations rely on self-report rather than behavioral trace data"
    - "Findings, while consistent across the sampled communities, are explicitly described by the authors as not generalizable to all FLOSS communities"
risk_of_bias: "medium"
relevance_to_project: >
  Provides a concrete, literature-grounded framework (contributor motivation, social norms,
  psychological sense of community, satisfaction, community commitment) plus specific
  practices (thanking/crediting all contribution types, personal invitations, low-effort
  task-finding dashboards, time-based releases, opt-in calls for help) for designing
  engagement and retention mechanisms aimed at the large, mostly-ignored periphery of
  infrequent open-source contributors, directly relevant to SNH's community-health and
  maintainer-burnout design work on episodic rather than only habitual/core participation.
tags:
  topic: ["open-source", "community-health", "job-engagement", "social-support"]
  method: ["qualitative", "interview"]
  population: ["open-source-contributors", "volunteers", "community-managers"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Uncovering the Periphery A Qualitative Survey of Episodic Volunteering in Free Libre and Open Source Software Communities/Uncovering the Periphery A Qualitative Survey of Episodic Volunteering in Free Libre and Open Source Software Communities.md"
  pdf: "papers/Articles/01 Articles - Extended/Uncovering the Periphery A Qualitative Survey of Episodic Volunteering in Free Libre and Open Source Software Communities.pdf"
  notes: null
