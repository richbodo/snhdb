id: "crowston-2004-effective-work-practices-for-software-engineering"
title: "Effective Work Practices for Software Engineering: Free/Libre Open Source Software Development"
authors:
  - "Crowston, Kevin"
  - "Annabi, Hala"
  - "Howison, James"
  - "Masango, Chengetai"
year: 2004
doi: null
venue: {type: "conference", name: "WISER'04 Workshop on Interdisciplinary Software Engineering Research, Newport Beach, California (ACM)", volume: null, issue: null, pages: null}
citation: "Crowston et al. (2004). Effective Work Practices for Software Engineering: Free/Libre Open Source Software Development. WISER'04 Workshop on Interdisciplinary Software Engineering Research, Newport Beach, California (ACM)."
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  This conference paper builds a theoretical model of FLOSS (Free/Libre Open Source
  Software) team effectiveness by extending Hackman's input-process-output model of work-
  team effectiveness with coordination theory (managing task/resource/actor dependencies)
  and Weick and Roberts' collective mind theory (contribution, representation,
  subordination). Drawing on the FLOSS and distributed-work literatures, the authors
  synthesize prior findings (e.g., the core/co-developer/active-user/passive-user 'onion'
  structure, effort penalties of distance) into a set of testable propositions and lay out a
  data-collection plan (mailing-list archives, CVS logs, interviews, observation) for future
  empirical work. It contributes a theoretical scaffold rather than new empirical results.
claims:
  - text: "FLOSS development teams are repeatedly described in the literature as having a hierarchical, onion-like structure: a small, highly interactive core of developers who write most of the code and control design, surrounded by a larger, more loosely coupled group of co-developers, then active users who report bugs/features, then passive users; core developers face a significant barrier to entry because they must have deep understanding of the software and its processes."
    evidence: "review-scoping"
    support_strength: "low"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "community-engagement"]
  - text: "Distributed/FLOSS teams generally require more on-task effort to be effective than co-located teams because participants are distant and less familiar with each other's work, and this additional required effort has been linked in prior empirical studies (Herbsleb et al. 2001; Mockus et al. 2000) to delays in software release compared to traditional face-to-face teams."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["productivity", "collaboration"]
    predictors: ["remote-work-intensity", "workload"]
  - text: "FLOSS software quality and development speed are attributed in the reviewed literature to two mechanisms: developers being users of their own software (eliminating much requirements ambiguity) and open access to source code letting users become co-developers, which the literature credits with letting hundreds of contributors handle mundane work (e.g., testing, estimated to consume over 50% of cost in non-FLOSS projects) and fix bugs/evolve features quickly."
    evidence: "review-scoping"
    support_strength: "low"
    outcomes: ["productivity", "collaboration"]
    predictors: ["open-source-maintenance", "community-engagement"]
population:
  who: "Not a primary study of a sample; the paper synthesizes prior descriptive/case-study literature on FLOSS projects (e.g., Linux, Apache, Mozilla, GNOME) and proposes a future research design targeting FLOSS developers, teams, and project artifacts."
  where: []
  when: null
  n: null
  sector: ["open-source"]
  sample_notes: >
    No new empirical data was collected for this paper; it is a conceptual/propositional
    piece. The 'proposed data collection' section describes planned future sources (project
    demographics, mailing-list and bug-tracker archives, CVS logs, developer interviews,
    conference observation, virtual ethnography) that had not yet been executed or analyzed
    at time of writing.
limitation:
  primary: "The theoretical model and all of its propositions are untested at time of publication; the paper is a research proposal/framework, not a report of empirical findings, so none of its claims about team effectiveness have been validated against data."
  others:
    - "Much of the underlying FLOSS literature it synthesizes is written by developers/consultants with partisan or promotional interests, and well-documented case studies are scarce and skew toward reporting successes rather than failures."
    - "The widely-cited 'onion' team-structure model it relies on is based on only a few case studies and, as the authors themselves note, 'has not been extensively tested.'"
risk_of_bias: "not-applicable"
relevance_to_project: >
  Offers the SNH project a ready-made theoretical scaffold — core/co-developer/active-
  user/passive-user structure, coordination-theory dependency management, and collective-
  mind (contribution/representation/subordination) constructs — for operationalizing
  community engagement, participation-role structure, and coordination mechanisms as
  predictors of collaboration and burnout in open-source and remote-team settings, and for
  designing the kind of trace-data-plus-interview measurement plan (mailing lists, commit
  logs, interviews) the project itself would need.
tags:
  topic: ["open-source", "collaboration", "community-health", "methodology"]
  method: ["theory"]
  population: ["open-source-developers", "distributed-teams"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Effective Work Practices for Software Engineering Free Libre Open Source Software Development/Effective Work Practices for Software Engineering Free Libre Open Source Software Development.md"
  pdf: "papers/Articles/01 Articles - Extended/Effective Work Practices for Software Engineering Free Libre Open Source Software Development.pdf"
  notes: "no-doi: web article / no registered DOI found"
