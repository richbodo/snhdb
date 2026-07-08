id: "crowston-2006-assessing-the-health-of-open-source"
title: "Assessing the Health of Open Source Communities"
authors:
  - "Crowston, K."
  - "Howison, J."
year: 2006
doi: "10.1109/mc.2006.152"
venue: {type: "journal", name: "Computer", volume: 39, issue: 5, pages: "89-91"}
citation: "Crowston et al. (2006). Assessing the Health of Open Source Communities. Computer, 39(5), 89-91. https://doi.org/10.1109/mc.2006.152"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "low", preregistered: false}
gist: >
  This practitioner-oriented IT Professional article by Crowston and Howison offers a
  framework for assessing FLOSS project health before contributing to or relying on a
  project, centered on an 'onion' model of concentric community roles (core developers,
  project leaders, codevelopers, active users). Drawing on the authors' own SourceForge
  research and prior motivation studies, it argues that healthy communities keep core teams
  small (rarely more than 10 developers), maintain a buffer of active users who shield core
  developers from routine support burden, and successfully manage leadership transitions. It
  gives IT professionals concrete signs to check (mailing lists, IRC tone, release
  management, leadership turnover) as proxies for community health and sustainability.
claims:
  - text: "Analysis of more than 100,000 SourceForge projects found that fewer than 1 percent have ever had more than 10 developers with commit access, indicating that small core teams (3-10 people) are typical and adequate even for successful FLOSS projects."
    evidence: "case-study"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "community-engagement"]
  - text: "Healthy FLOSS communities have an onion-shaped structure in which a wide circle of active users (testing releases, filing bug reports, answering setup questions) forms a buffer that protects core developers from burnout and from being overwhelmed by peripheral/passive users, as illustrated by a sociogram of bug-fixing interactions in the SquirrelMail project."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["burnout", "collaboration"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Citing prior survey research (Ghosh et al.; Lakhani and Wolf), the article reports that FLOSS contributor motivations are diverse and rank, in decreasing order of relevance: intellectual engagement, knowledge sharing, interest in the product itself, and ideology/reputation/community obligation, with reputation's importance rising the longer a participant has been involved."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-engagement"]
    predictors: ["community-engagement"]
population:
  who: "FLOSS open-source projects and their developer/leader/user communities in general, illustrated with the SourceForge project population and specific examples (Apache, Linux, Debian, Perl, SquirrelMail)"
  where: []
  when: null
  n: null
  sector: ["open-source"]
  sample_notes: >
    Not an original empirical study; it is a synthesis/practitioner-advice piece that cites
    the authors' own (then in-press) SourceForge analysis and other researchers' motivation
    surveys rather than presenting new primary data collection.
limitation:
  primary: "The article is a practitioner-oriented magazine synthesis, not a primary empirical study; its central statistic (the 1% figure) and other claims rely on citations to the authors' separate in-press work without methodological detail presented here."
  others:
    - "No original data collection or analysis is reported within the article itself"
    - "Recommendations (e.g., an ideal active-user buffer of 'one or two longer-term participants') are heuristic and anecdotal rather than statistically derived"
risk_of_bias: "high"
relevance_to_project: >
  Provides a concrete, reusable structural model (core developers / leaders / codevelopers /
  active users) for diagnosing open-source community health, and directly ties community
  structure to maintainer burnout by identifying the active-user buffer as a protective
  mechanism against core-developer burnout and support overload.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "collaboration"]
  method: ["case-study", "secondary-data"]
  population: ["open-source-contributors", "software-developers"]
source:
  markdown: "Papers_Data/Academic/MD/Assessing the Health of Open Source Communities/Assessing the Health of Open Source Communities.md"
  pdf: "papers/Academic/Assessing the Health of Open Source Communities.pdf"
  notes: null
