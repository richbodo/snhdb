id: "malone-1994-the-interdisciplinary-study-of-coordination"
title: "The interdisciplinary study of coordination"
authors:
  - "Malone, Thomas W."
  - "Crowston, Kevin"
year: 1994
doi: "10.1145/174666.174668"
venue: {type: "journal", name: "ACM Computing Surveys", volume: 26, issue: 1, pages: "87-119"}
citation: "Malone et al. (1994). The interdisciplinary study of coordination. ACM Computing Surveys, 26(1), 87-119. https://doi.org/10.1145/174666.174668"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Malone and Crowston synthesize computer science, economics, organization theory, and
  biology into a unified 'coordination theory,' defining coordination as the process of
  managing dependencies among activities and cataloguing generic dependency types (shared
  resources, producer/consumer, simultaneity, task/subtask) alongside the coordination
  processes used to manage each. Drawing on formal models and case examples, the survey
  argues that information technology's main effect is to lower coordination costs, which can
  substitute for existing coordination, increase the total amount of coordination performed,
  or enable entirely new 'coordination-intensive' organizational structures such as
  adhocracies and smaller, more market-mediated firms. It also surfaces the 'discretionary
  database' incentive problem in cooperative-work tools, where individual users benefit from
  viewing shared information without needing to contribute it, illustrated by a consulting
  firm's underused Lotus Notes deployment.
claims:
  - text: "Formal queuing-theory models of alternative task-assignment mechanisms (Malone & Smith) showed a three-way tradeoff: centralized schemes had the lowest coordination costs but were most vulnerable to processor/actor failure; decentralized markets were least vulnerable to failure but had high coordination costs; decentralized 'product hierarchies' had low coordination costs but incurred high production costs from unused capacity."
    evidence: "modelling"
    support_strength: "moderate"
    outcomes: ["productivity", "collaboration"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "Citing econometric analysis of the U.S. economy from 1975-1985 (Brynjolfsson et al. 1994), the authors report that greater use of information technology is correlated with decreases in both firm size and vertical integration; as an illustrative case, the share of airline reservations booked through travel agents (versus calling airlines directly) rose from 35% to 70% after computerized reservation systems were introduced."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["productivity"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "Cooperative-work tools built around 'discretionary databases' (e.g., shared calendars, Lotus Notes) create a free-rider equilibrium: users can obtain full benefit from viewing shared information without contributing to it, so rational individual incentives can drive contribution toward zero; a case study of a large consulting firm (Orlikowski 1992) found employees rewarded for being the individual 'expert' were reluctant to post their knowledge into a shared database that would erode that status."
    evidence: "case-study"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration", "help-seeking"]
    predictors: ["organizational-culture", "psychological-safety"]
population:
  who: "Not an original empirical sample: a narrative synthesis across computer science, economics, organization theory, and biology literature, illustrated with cited empirical studies such as Danziger et al.'s survey of computerization decisions in 42 U.S. local governments and Orlikowski's case study of a consulting firm's groupware deployment."
  where: ["USA"]
  when: "Literature synthesized spans roughly 1950s-1994; illustrative cited empirical studies date from 1975-1992"
  n: null
  sector: ["technology", "corporate", "government"]
  sample_notes: >
    As a theoretical survey (ACM Computing Surveys, 1994), the paper has no independent
    sample of its own; any n's, response rates, or representativeness belong to the
    individual cited primary studies (e.g., Malone & Smith's formal models, Danziger et
    al.'s 42-government dataset) and are not independently verifiable from this document.
limitation:
  primary: "As a 1994 theoretical synthesis, its predictions about IT's organizational effects (smaller firms, more markets, adhocracies) are speculative extrapolations from early formal models and small case examples that predate cloud computing, social media, distributed version control, and modern remote/open-source tooling, limiting direct applicability to today's virtual work contexts."
  others:
    - "Relies heavily on selective anecdotes and single-organization case examples (e.g., one consulting firm's Lotus Notes use) rather than a systematic empirical review."
    - "No explicit literature-search or study-selection methodology is described, so coverage of each contributing discipline may be uneven or biased toward the authors' own prior work (frequently self-cited)."
risk_of_bias: "medium"
relevance_to_project: >
  Establishes the foundational 'coordination theory' vocabulary (managing dependencies via
  shared-resource, producer/consumer, simultaneity, and task/subtask processes) that later
  open-source and distributed-work research builds on, and its analysis of the
  'discretionary database' free-rider problem in cooperative-work tools directly foreshadows
  the incentive and psychological-safety challenges the SNH project faces in designing tools
  that encourage remote workers and OSS contributors to share knowledge rather than free-
  ride on others' contributions.
tags:
  topic: ["collaboration", "remote-work", "open-source", "methodology"]
  method: ["theory", "secondary-data"]
  population: ["organizations", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination.pdf"
  notes: null
