id: "capra-2008-a-framework-for-evaluating-managerial-styles"
title: "A Framework for Evaluating Managerial Styles in Open Source Projects"
authors:
  - "Capra, Eugenio"
  - "Wasserman, Anthony I."
year: 2008
doi: "10.1007/978-0-387-09684-1_1"
venue: {type: "book", name: "IFIP – The International Federation for Information Processing", volume: null, issue: null, pages: "1-14"}
citation: "Capra et al. (2008). A Framework for Evaluating Managerial Styles in Open Source Projects. IFIP – The International Federation for Information Processing, 1-14. https://doi.org/10.1007/978-0-387-09684-1_1"
article_type: "empirical"
method: {design: "mixed-methods", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  The paper develops the Software Project Governance Framework (SPGF), which scores software
  projects along four dimensions -- contribution, project leadership, working practices, and
  testing -- to position them on a continuum from fully closed to fully open governance.
  Built from interviews with 25 project managers and validated against more than 70
  commercial and community open-source projects, the framework is illustrated with case
  studies of OpenOffice, MySQL, and SugarCRM showing how corporate-led open-source projects
  can still adopt fully distributed, virtual working practices. It contributes a structured
  way to characterize how geographically dispersed, community-governed teams organize
  communication, decision-making, and quality control.
claims:
  - text: "Across the validation sample of 70+ projects, working practices were the most 'open' dimension: 57% of projects scored the maximum (4) for being widely dispersed and communicating entirely through virtual tools with rare or no physical meetings, versus only 15% scoring maximum openness on testing."
    evidence: "mixed-methods"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "MySQL, though centrally controlled by a company (scoring 1 on contribution and project leadership), scored 4 on working practices: developers were located in 26 countries, worked from home, met only once or twice a year, and coordinated asynchronously via IRC, shared task lists, and email to bridge time zones."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "organizational-culture"]
  - text: "Survey data across the sample showed roughly 50% of code in community open-source projects is developed by hired (paid) rather than volunteer developers, and physical face-to-face meetings occur in only about 35% of projects, indicating that most governance and coordination happens through virtual/asynchronous channels regardless of a project's formal openness."
    evidence: "mixed-methods"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "Project managers, community managers, QA managers, VPs of engineering, committers, and project leaders from more than 70 commercial and community-based software projects (open and closed source), plus 25 project managers interviewed in the initial framework-development phase"
  where: []
  when: null
  n: 70
  sector: ["open-source-software", "software-industry"]
  sample_notes: >
    Convenience sample of mature, well-known projects drawn from SourceForge, Apache,
    Tigris, and Java.net meeting minimum size criteria (at least 2 administrators and 2
    contributors); explicitly skewed toward large, established projects rather than small
    teams, so findings may not generalize to nascent or small-scale open-source communities.
limitation:
  primary: "The framework is qualitative and ordinal by design (scores 1-4 per dimension), explicitly not intended for absolute cross-project comparison, and its dimension scores rest on the authors' interpretive judgment from interview data rather than independently verifiable metrics."
  others:
    - "Sample selection favored large, mature, well-known projects, introducing selection bias away from smaller or struggling open-source communities."
    - "Case studies (OpenOffice, MySQL, SugarCRM) are illustrative rather than representative, and scoring rationale relies on the authors' own coding of interview responses."
    - "No statistical testing or correlation analysis is reported between SPGF dimensions and outcomes like project success or code quality; the paper explicitly frames this as future work."
risk_of_bias: "medium"
relevance_to_project: >
  Provides an empirically grounded, four-dimension taxonomy (contribution, leadership,
  working practices, testing) for characterizing how distributed open-source teams organize
  communication and governance, useful for SNH work on measuring network structure and
  collaboration norms in maintainer/contributor communities. The finding that even
  corporate-controlled projects (e.g., MySQL) can be fully virtual and asynchronous is
  directly relevant to designing for remote, geographically dispersed collaboration without
  assuming volunteer-led governance.
tags:
  topic: ["open-source", "remote-work", "collaboration", "community-health", "methodology"]
  method: ["mixed-methods", "interview", "case-study"]
  population: ["open-source-contributors", "software-developers"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/A Framework for Evaluating Managerial Styles in Open Source Projects/A Framework for Evaluating Managerial Styles in Open Source Projects.md"
  pdf: "papers/Articles/01 Articles - Extended/A Framework for Evaluating Managerial Styles in Open Source Projects.pdf"
  notes: null
