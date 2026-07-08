id: "wang-2020-unveiling-elite-developers-activities-in-open"
title: "Unveiling Elite Developers’ Activities in Open Source Projects"
authors:
  - "Wang, Zhendong"
  - "Feng, Yang"
  - "Wang, Yi"
  - "Jones, James A."
  - "Redmiles, David"
year: 2020
doi: "10.1145/3387111"
venue: {type: "journal", name: "ACM Transactions on Software Engineering and Methodology", volume: 29, issue: 3, pages: "1-35"}
citation: "Wang et al. (2020). Unveiling Elite Developers’ Activities in Open Source Projects. ACM Transactions on Software Engineering and Methodology, 29(3), 1-35. https://doi.org/10.1145/3387111"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This study mines fine-grained GitHub event data (900,862 events, Jan 2015-Oct 2018) from
  20 large open source projects to profile 'elite' developers (those with write/admin
  privileges) across four activity types: communicative, organizational, supportive, and
  typical (coding). It finds elite developers perform the large majority of nontechnical
  work as well as most code, that their effort mix shifts sharply toward nontechnical work
  as a project grows while their coding stagnates or declines, and that this nontechnical
  effort is generally negatively correlated with project productivity and (mixed) with
  quality, except supportive effort which is linked to a higher bug fix rate. The paper
  frames this as a workload-imbalance and role-transition dilemma with direct implications
  for maintainer burnout and tool/workflow design.
claims:
  - text: "Elite developers perform over 50% of organizational, supportive, and typical activities and 34% of communicative activities in their projects; on average an elite developer performs 7x more communicative, 145x more organizational, 22x more supportive, and 22x more typical activities per month than a nonelite developer."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["burnout", "collaboration"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "As projects grow, elite developers significantly increase communicative and supportive effort while typical (coding) activity growth is significantly lower and even negative on average (-1.63% monthly growth), meaning an elite developer does roughly half the technical work after three years that they did initially, even as communicative and supportive work doubled."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "In fixed-effects panel regressions, elite developers' communicative and supportive effort shares are negatively correlated with new commits and (via supportive share) with longer bug cycle time (productivity loss, beta = -155.96 to -138.21, p<.01-.001); organizational and supportive effort shares are positively correlated with new bugs found (quality loss), while supportive effort share is positively correlated with bug fix rate (quality gain); these effects are stronger in company-sponsored projects."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "collaboration"]
    predictors: ["workload", "open-source-maintenance"]
population:
  who: "20 large, established open source GitHub projects (11 company-sponsored, 9 non-company-sponsored) with formal PR-based governance, at least 100 pull requests and 50 contributors historically; unit of analysis is elite vs. nonelite developer activity aggregated to project-months."
  where: []
  when: "January 2015 to October 2018"
  n: 720
  sector: ["open-source"]
  sample_notes: >
    Sample is 20 purposively selected large, mature GitHub projects (e.g., React,
    TensorFlow, TiDB); 720 project-month observations (20 projects x 36 months) used in
    regressions. Elite status inferred indirectly via a permissions-check heuristic (write-
    permission-requiring actions) rather than direct access to GitHub's permission list,
    with a 90-day rolling 'elite-ship' window. Findings generalize only to large, governed
    OSS projects, not small/medium ones, and rely solely on public GitHub trace data (no
    email, IRC, or chat channels).
limitation:
  primary: "All regressions establish correlation, not causation, between elite developers' effort allocation and project productivity/quality outcomes, despite the paper's narrative framing some relationships as if causal."
  others:
    - "Elite/nonelite status and activity categories are inferred from a single data source (public GitHub events) using an indirect permissions-check heuristic, since GitHub does not expose actual permission lists to outside researchers."
    - "Sample is restricted to 20 large, well-governed projects with established PR workflows, so findings may not generalize to small, informal, or poorly governed OSS projects."
    - "Some GitHub event data (e.g., certain issue-management actions) could only be captured via a supplementary customized API script, and non-GitHub communication channels (email, IRC, Slack) are entirely excluded."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, project-scale evidence that open-source maintainers' (elite
  developers') shift toward communicative/organizational/supportive labor as projects scale
  is associated with productivity loss and mixed quality effects, directly substantiating
  the maintainer-burnout and workload-imbalance mechanism the SNH project cares about, and
  motivating tool/workflow interventions (task delegation, automation of routine
  admin/support work) to protect maintainer wellbeing.
tags:
  topic: ["open-source", "maintainer-burnout", "collaboration", "community-health"]
  method: ["secondary-data", "longitudinal", "panel-regression"]
  population: ["open-source-maintainers", "software-developers"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Unveiling Elite Developers Activities in Open Source Projects/Unveiling Elite Developers Activities in Open Source Projects.md"
  pdf: "papers/Articles/01 Articles - Extended/Unveiling Elite Developers Activities in Open Source Projects.pdf"
  notes: null
