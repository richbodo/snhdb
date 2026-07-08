id: "salkever-2023-open-source-maintainers-exploring-the-people"
title: "Open Source Maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects"
authors:
  - "Salkever, Alex"
year: 2023
doi: null
venue: {type: "report", name: "Linux Foundation Research", volume: null, issue: null, pages: null}
citation: "Salkever (2023). Open Source Maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects. Linux Foundation Research."
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Based on 32 hour-long interviews with 'super maintainers' of critical open source projects
  (e.g., Linux, Kubernetes, PostgreSQL, Git, NumPy, PyTorch, Storybook), this Linux
  Foundation report documents how maintainers balance contributor onboarding, governance,
  documentation, funding, diversity, and burnout. It finds that contributor experience is
  widely perceived to degrade as projects mature, that most maintainers are salaried to work
  on their projects yet feel under-recognized, and that maintainers rely on informal, self-
  devised boundary-setting and automation practices to avoid burnout. The report synthesizes
  these interviews into a set of practitioner best-practices rather than testing hypotheses.
claims:
  - text: "75% of the 32 interviewed super-maintainers served as both maintainers and code contributors (25% maintainer-only, none contributor-only), spending an average of 70% of their working time on the open source project; only one of the projects examined had just a single maintainer."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration"]
    predictors: ["workload"]
  - text: "Multiple long-tenured maintainers (e.g., PostgreSQL's Andres Freund) reported that new-contributor experience has deteriorated over time as project maturity, PR volume, and code complexity increased, leading to slower, shallower maintainer responses than early contributors received, despite deliberate efforts to preserve a welcoming onboarding experience."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["retention"]
    predictors: ["workload", "community-engagement"]
  - text: "Maintainers described burnout as driven by the public, always-on, consensus-heavy nature of open source governance (illustrated by Jupyter's 2022 shift from rough consensus to a modular Executive Committee/Steering Council structure after consensus-driven decision-making contributed to leader burnout), and reported preventing it via explicit work-hour/communication boundaries, workflow automation, accepting the work is never 'finished,' and taking breaks."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["burnout"]
    predictors: ["boundary-management", "leadership-style"]
population:
  who: "32 purposively selected 'super maintainers' and core contributors of open source projects identified by LF Research's Census II work as among the ~200 most critical/widely-depended-upon OSS projects (e.g., Linux, Kubernetes, containerd, PostgreSQL, Git, cURL, NumPy, PyTorch, Jupyter, Storybook, Salt, Webpack, Babel, React)."
  where: []
  when: "interviews conducted prior to publication in July 2023; exact interview window not stated"
  n: 32
  sector: ["open-source"]
  sample_notes: >
    Purposive, non-random sample skewed toward well-resourced, full-time-employed
    maintainers (all but two had full-time employer support) of long-lived, high-visibility
    projects backed by large tech companies (Amazon, Microsoft, IBM, Meta, VMware, Red Hat);
    maintainers drawn from 'a half dozen countries', 6 of 32 female; three interviewees
    discussed past (not current) maintainer roles. Not representative of the broader
    population of smaller or unaffiliated OSS maintainers.
limitation:
  primary: "Small, purposive, non-random sample of 32 highly visible 'super maintainers' from large, well-funded, corporate-backed projects limits generalizability to typical, smaller, or unaffiliated open source maintainers, who the report itself notes face different funding and burnout pressures."
  others:
    - "No formal qualitative coding methodology, inter-rater reliability, or preregistration is described; findings are presented as narrative synthesis of interview themes and illustrative quotes rather than systematically coded/quantified results."
    - "Produced and funded by the Linux Foundation itself, which may bias framing toward practices favorable to foundation-affiliated and corporate-sponsored open source models."
    - "Reported percentages (e.g., 75% dual role, 38% employer support) come from a self-selected group of 32 and are presented without confidence intervals or statistical testing."
risk_of_bias: "medium"
relevance_to_project: >
  Provides concrete, named burnout-prevention practices (boundary-setting, automation,
  distributing governance/decision-making, employer financial support) and a documented case
  (Jupyter's consensus-to-council governance shift) linking maintainer burnout to
  organizational structure, which the SNH project can draw on when designing interventions
  or measures for maintainer-burnout and community-engagement in open-source/tech
  communities.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["qualitative"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Articles/MD/Open Source Maintainers Report 2023 Linux Foundation Research/Open Source Maintainers Report 2023 Linux Foundation Research.md"
  pdf: "papers/Articles/Open Source Maintainers Report 2023 Linux Foundation Research.pdf"
  notes: "no-doi: web article / no registered DOI found"
