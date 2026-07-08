id: "steinmacher-2019-overcoming-social-barriers-when-contributing-to"
title: "Overcoming Social Barriers When Contributing to Open Source Software Projects"
authors:
  - "Steinmacher, Igor"
  - "Gerosa, Marco"
  - "Conte, Tayana U."
  - "Redmiles, David F."
year: 2019
doi: "10.1007/s10606-018-9335-z"
venue: {type: "journal", name: "Computer Supported Cooperative Work (CSCW)", volume: 28, issue: "1-2", pages: "247-290"}
citation: "Steinmacher et al. (2019). Overcoming Social Barriers When Contributing to Open Source Software Projects. Computer Supported Cooperative Work (CSCW), 28(1-2), 247-290. https://doi.org/10.1007/s10606-018-9335-z"
article_type: "empirical"
method: {design: "mixed-methods", approach: "interview", evidence_level: "moderate", preregistered: false}
gist: >
  Through a systematic literature review, practitioner surveys, and semi-structured
  interviews with 35 developers across 13 OSS projects, the authors build a model of 58
  onboarding barriers, 13 of them social (e.g., not receiving an answer, impolite replies,
  difficulty finding a mentor, shyness, cultural/language differences). They then design and
  evaluate FLOSScoach, an onboarding portal built from the model, in a two-iteration diary
  study with 43 undergraduate contributors, finding it reduced newcomers' need to interact
  with the community and helped those who did reach out communicate more effectively.
claims:
  - text: "13 social barriers were identified and organized into categories (reception issues, newcomers' communication behavior, finding a mentor, language/cultural differences); reception problems such as 'not receiving an answer' and 'delayed answers' were the most frequently and consistently evidenced across the SLR, surveys, and interviews."
    evidence: "qualitative"
    support_strength: "moderate"
    outcomes: ["retention", "communication", "isolation"]
    predictors: ["social-support", "community-engagement", "sampling-method"]
  - text: "In the FLOSScoach diary study, 15 of 43 tracked participants attempted to interact with the community at all, and every participant who did receive a community response reported it was welcoming and helpful, while three participants who received no answer described frustration ('demotivated', 'anesthetized'); the portal group completed the assignment at a higher rate (24/31, 77%) than the control group (19/34, 56%)."
    evidence: "mixed-methods"
    support_strength: "low-to-moderate"
    outcomes: ["communication", "collaboration", "retention"]
    predictors: ["intervention", "social-support"]
  - text: "Projects hosted on social-coding platforms (GitHub/GitLab) showed fewer mentions of social barriers such as difficulty finding a mentor than projects on their own forges or SourceForge, and older/larger projects tended to present more reported barriers, though difficulty finding a mentor and reception issues recurred across nearly all project types regardless of size, age, or language."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["collaboration", "retention"]
    predictors: ["network-structure", "peer-mentoring", "organizational-culture"]
population:
  who: "OSS project newcomers, dropouts, and experienced/core members from real-world community-based projects (Phase I: 9 students, 24 survey respondents, 35 interviewees across 13-19 projects incl. LibreOffice, OpenOffice, JabRef, Firefox, Moodle); Phase II: 43 analyzed undergraduate CS students recruited from two Brazilian universities to attempt real OSS contributions with or without the FLOSScoach portal"
  where: ["Brazil", "multiple countries of interviewed OSS contributors (France, Germany, Canada, Hungary, Australia, Turkey, Mexico, India, US, UK, Greece, China)"]
  when: "2013-2015"
  n: 43
  sector: ["open-source"]
  sample_notes: >
    Phase I combined convenience-sample survey respondents (9 mailing lists), snowball-
    recruited interviewees, and a 21-study SLR; self-selection and social-desirability bias
    likely among volunteer respondents. Phase II used undergraduate students (mostly with
    little/no industry experience) as proxies for OSS newcomers, which limits
    generalizability to real-world volunteer contributors; only 44 of 65 initial diary
    participants met inclusion criteria (>=3 entries, code contribution).
limitation:
  primary: "Phase II generalizability is limited because participants were undergraduate students completing a course assignment (not self-motivated volunteer contributors), and the diary-based, small-sample design (43 analyzed, split across control/portal groups) supports qualitative insight rather than statistically powered causal claims about the portal's effect."
  others:
    - "Data collected 2013-2015, before GitHub/social-coding norms became dominant in OSS, so barrier prevalence may not reflect current platforms."
    - "SLR and interview coding involved subjective qualitative interpretation, mitigated only by multi-researcher discussion, not independent inter-rater reliability statistics."
    - "Self-selection and social-desirability bias likely in open-invitation survey/interview recruitment."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs SNH's model of what drives isolation vs. belonging in open-source
  communities: it operationalizes concrete, actionable social barriers (unanswered messages,
  unkind tone, absent mentors, shyness/fear, language/cultural friction) and shows that a
  lightweight structural intervention (an onboarding portal with guidance and message
  templates) measurably reduced newcomers' need for and anxiety around social contact, which
  is a directly transferable design pattern for reducing maintainer/contributor isolation
  and improving retention.
tags:
  topic: ["open-source", "community-health", "isolation", "social-support", "collaboration"]
  method: ["mixed-methods", "qualitative", "review-systematic"]
  population: ["open-source-contributors", "students"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Overcoming Social Barriers When Contributing to Open Source Software Projects/Overcoming Social Barriers When Contributing to Open Source Software Projects.md"
  pdf: "papers/Articles/01 Articles - Extended/Overcoming Social Barriers When Contributing to Open Source Software Projects.pdf"
  notes: null
