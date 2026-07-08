id: "herbsleb-2003-an-empirical-study-of-speed-and"
title: "An empirical study of speed and communication in globally distributed software development"
authors:
  - "Herbsleb, J.D."
  - "Mockus, A."
year: 2003
doi: "10.1109/tse.2003.1205177"
venue: {type: "journal", name: "IEEE Transactions on Software Engineering", volume: 29, issue: 6, pages: "481-494"}
citation: "Herbsleb et al. (2003). An empirical study of speed and communication in globally distributed software development. IEEE Transactions on Software Engineering, 29(6), 481-494. https://doi.org/10.1109/tse.2003.1205177"
article_type: "empirical"
method: {design: "mixed-methods", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Herbsleb and Mockus analyze change-management data and two employee surveys from two
  geographically distributed telecommunications software departments to explain why cross-
  site work takes longer. Distributed modification requests took about 2.5 times as long to
  complete as same-site ones in both departments, and statistical (graphical) modeling
  showed this delay was not explained by task size or complexity but was mediated almost
  entirely by the larger number of people distributed tasks required. Survey data further
  show that distributed social networks are smaller, communicate less frequently, are harder
  to navigate to find expertise, and feel less like a cohesive 'team' than co-located
  networks, and the paper argues these network deficiencies are the mechanism that pulls
  extra people into distributed work and thereby causes delay.
claims:
  - text: "Distributed modification requests (MRs) took about 2.5 times as long to complete as same-site MRs in both organizations studied: Department A averaged 5 days (single-site) vs 12.7 days (distributed, p<0.001); Department B averaged 7 days vs 18 days (p<0.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "productivity"]
    predictors: ["network-structure", "remote-work-intensity"]
  - text: "In multiple regression and graphical (covariance-selection) models, the number of people involved in an MR was the strongest and most consistent predictor of completion interval, and the distributed/same-site variable had no significant direct effect on interval once other factors were controlled -- distributed work increased delay only indirectly, by requiring more people."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "productivity"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Survey data (Department A, n=92-98, response rates 60-83%) showed distributed social networks were smaller (mean 4.9-4.8 remote contacts vs 16.0-7.6 local, p<.0001), communicated far less frequently, and were rated significantly harder to identify/contact experts within than local networks; workers also reported significantly less 'team' feeling and less help received (though not less help given) from remote vs local colleagues (p<.0001), while perceived disagreement about task priorities did not differ by site (not significant)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "sense-of-belonging", "communication"]
    predictors: ["network-structure", "team-cohesion", "social-support"]
population:
  who: "Software engineers and managers in two distributed telecommunications departments of a single company: Department A (UK, Germany, two India sites, ~40-75 people/site) and Department B (Midwestern US and Ireland, ~30-60 people/site); MR analysis covers 2,227 (Dept A) and 4,974 (Dept B) modification requests over 2.5-3.5 years; survey analysis covers Department A only (98 of 117 invited in 1998, 83% response; 96 of 160 invited in 1999, 60% response)."
  where: ["United Kingdom", "Germany", "India", "United States", "Ireland"]
  when: "July 1997 to July 1999 (change data); surveys administered November 1998 and June 1999"
  n: 96
  sector: ["technology", "software-industry"]
  sample_notes: >
    Two-organization replication design strengthens generalizability of the MR-interval
    finding, but survey data come only from Department A (Department B could not be surveyed
    due to organizational changes), and all data are from a single company in the telecom
    software domain.
limitation:
  primary: "The proposed causal mechanisms linking specific social-network deficiencies (H1-H5) to the need for more people on distributed MRs are explicitly labeled speculative by the authors -- the survey supports the existence of network differences, but the paper does not directly test that these differences cause the added-people effect."
  others:
    - "Single-company, single-industry (telecom software) setting limits generalizability to other organizational or distributed-work arrangements (e.g., outsourcing)."
    - "Confounding factors such as cultural background, language, and differing site histories could explain reduced 'teamness' and communication differences instead of (or in addition to) geographic distribution per se."
    - "CM system data only capture people who formally opened MRs or committed code deltas, undercounting informal help such as advice-giving that does not leave a system trace."
risk_of_bias: "low"
relevance_to_project: >
  Provides a rigorously replicated, quantitative mechanism -- smaller, less frequent,
  harder-to-navigate distributed social networks force more people into a task, which drives
  delay -- directly relevant to designing SNH interventions (e.g., expertise-finding tools,
  presence/awareness features, liaison roles) intended to substitute for the informal, co-
  located communication that remote and distributed teams lack. Also offers a validated
  survey instrument (network size, communication frequency, teamness/help items) usable to
  measure social network health in distributed teams.
tags:
  topic: ["remote-work", "collaboration", "productivity", "community-health"]
  method: ["mixed-methods", "secondary-data", "survey"]
  population: ["software-engineers", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development.pdf"
  notes: null
