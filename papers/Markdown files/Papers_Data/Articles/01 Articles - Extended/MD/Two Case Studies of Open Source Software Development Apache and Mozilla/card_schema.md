id: "mockus-2005-two-case-studies-of-open-source"
title: "Two Case Studies of Open Source Software Development: Apache and Mozilla"
authors:
  - "Mockus, Audris"
  - "Fielding, Roy T."
  - "Herbsleb, James D."
year: 2005
doi: "10.7551/mitpress/5326.003.0016"
venue: {type: "book", name: "Perspectives on Free and Open Source Software", volume: null, issue: null, pages: "163-210"}
citation: "Mockus et al. (2005). Two Case Studies of Open Source Software Development: Apache and Mozilla. Perspectives on Free and Open Source Software, 163-210. https://doi.org/10.7551/mitpress/5326.003.0016"
article_type: "empirical"
method: {design: "case-study", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This paper mines email, CVS, and bug-database archives from the Apache and Mozilla open
  source projects (plus five commercial telecom projects as a baseline) to show that OSS
  communities have a highly skewed 'onion' participation structure: a small core of 15-35
  developers does the great majority of new-functionality work, while much larger and looser
  groups handle defect repair and problem reporting. It argues that as project size grows
  beyond roughly 10-15 people, informal trust-based coordination among core developers
  becomes insufficient and is replaced by formal mechanisms such as enforced code ownership
  and mandatory multi-stage inspection (as seen in Mozilla versus Apache), trading
  development speed for coordination capacity.
claims:
  - text: "In Apache, the top 15 ('core') developers contributed more than 83% of modification requests and code deltas, 88% of added lines, and 91% of deleted lines, while a much larger and more loosely engaged group did the bulk of defect reporting: about 3,060 people submitted 3,975 problem reports but only 458 of them (591 reports) led to an actual code change."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "open-source-maintenance"]
  - text: "Despite being volunteer and part-time, Apache's core developers were roughly as productive as full-time developers on comparable commercial telecom projects (within a factor of 1.5 in KLOC/developer/year) and Apache's pre-system-test defect density (2.64 defects/KLOC added) was substantially lower than four commercial comparison projects (5.7-6.9 defects/KLOC added at the same development stage)."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: ["productivity", "performance"]
    predictors: ["team-cohesion", "open-source-maintenance"]
  - text: "As module size scaled beyond what a small informally-coordinated core could handle, Mozilla adopted formal code ownership and mandatory two-stage inspections; per-module core teams ranged from 22 to 36 developers (versus Apache's 15), and this formality came with a large cost in speed: roughly half of Apache's problem reports were resolved within a single day, while Mozilla's median resolution intervals ran from about 15 to 50 days depending on module and outcome."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: ["collaboration", "productivity"]
    predictors: ["team-cohesion", "network-structure"]
population:
  who: "Archival trace data from two large open source software communities (Apache HTTP Server: ~388 code contributors and ~3,060 distinct problem reporters from 1995-1999; seven Mozilla browser modules: 486 code contributors and ~6,837 problem reporters, 1998-2001) benchmarked against five in-house commercial telecommunications software projects at Lucent/Avaya."
  where: ["United States"]
  when: "Apache: Feb 1995-May 1999 (email/CVS archives); Mozilla: 1998-2001; commercial comparison projects: contemporaneous telecom development at Lucent/Avaya"
  n: null
  sector: ["software-development", "open-source-software", "telecommunications"]
  sample_notes: >
    Not a random sample: Apache and Mozilla were chosen as prominent, well-documented OSS
    projects, and the five commercial projects were chosen for data availability and
    researcher familiarity rather than representativeness. Population counts vary by measure
    (e.g., 388 Apache code contributors vs. ~3,060 problem reporters) because different
    archival sources (email, CVS, BUGDB/Bugzilla) capture different participant roles.
limitation:
  primary: "Two-case comparative design with a convenience sample of five commercial baseline projects chosen for the authors' familiarity and data access rather than random or representative selection, limiting generalizability of the hypotheses to other OSS communities or hybrid commercial/OSS efforts."
  others:
    - "Defect density measures are acknowledged by the authors to be confounded by unmeasured usage intensity and code verbosity ('bloat'), with no fully satisfactory solution offered."
    - "Mozilla had not yet shipped a non-beta release at time of writing, so postrelease defect density (the customer-relevant measure used for Apache) could not be computed for Mozilla, weakening the cross-project comparison."
    - "Qualitative process descriptions relied on a small number of core informants (one Apache core developer/co-author; Mozilla's 'Chief Lizard Wrangler') reviewed by only one or two additional people each, risking an idealized or narrow account of how governance actually worked."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational quantitative account of the OSS 'onion' participation structure the
  SNH project's open-source/maintainer-burnout strand relies on: it shows the funnel from
  thousands of problem reporters down to a small (15-35 person) core that carries most
  development workload, and it documents the concrete mechanism (informal trust-based
  coordination vs. enforced code ownership plus mandatory inspection) that governs how
  coordination and workload concentration change as a community scales, directly informing
  how the project models maintainer workload and community-engagement structure.
tags:
  topic: ["open-source", "collaboration", "community-health", "maintainer-burnout", "productivity"]
  method: ["case-study", "secondary-data"]
  population: ["open-source-contributors", "software-engineers"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Two Case Studies of Open Source Software Development Apache and Mozilla/Two Case Studies of Open Source Software Development Apache and Mozilla.md"
  pdf: "papers/Articles/01 Articles - Extended/Two Case Studies of Open Source Software Development Apache and Mozilla.pdf"
  notes: null
