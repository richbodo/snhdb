id: "geiger-2021-the-labor-of-maintaining-and-scaling"
title: "The Labor of Maintaining and Scaling Free and Open-Source Software Projects"
authors:
  - "Geiger, R. Stuart"
  - "Howard, Dorothy"
  - "Irani, Lilly"
year: 2021
doi: "10.1145/3449249"
venue: {type: "journal", name: "Proceedings of the ACM on Human-Computer Interaction", volume: 5, issue: "CSCW1", pages: "1-28"}
citation: "Geiger et al. (2021). The Labor of Maintaining and Scaling Free and Open-Source Software Projects. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1), 1-28. https://doi.org/10.1145/3449249"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Based on 37 semi-structured interviews with F/OSS maintainers, this study finds that the
  labor of maintaining open-source projects does not simply grow with scale but transforms
  in kind -- from solo, ad-hoc upkeep into distributed, rule-bound organizational,
  financial, and emotional labor. It introduces two influential constructs, 'scalar labor'
  (the work of building capacity to meet a project's growing needs) and 'scalar debt' (the
  burnout-inducing deficit that accrues when growth outpaces that capacity), and documents
  how popular maintainers can become hypervisible 'microcelebrities' rather than invisible
  infrastructure workers.
claims:
  - text: "As F/OSS projects scale across many dimensions (users, contributors, codebase complexity, ecosystem interdependence), the work of maintaining them does not merely increase in volume but fundamentally changes in kind (e.g., ad-hoc solo governance shifts to formal multi-maintainer structures; user support moves from a growth opportunity to an 'overwhelming flood' requiring triage teams and rules), and interviewees repeatedly linked this intensification to demotivation, exhaustion, and burnout."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "The paper introduces the concept of 'scalar debt' -- an accumulated deficit when a project's growth in users/contributors outpaces growth in its organizational capacity to maintain itself -- which interviewees described as living in a 'constant state of incipient crisis, overwork, or burnout' while trying to keep projects from falling further behind."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "Contrary to the dominant framing of infrastructural maintenance as invisible work, maintainers of large, popular F/OSS projects can become hypervisible 'microcelebrities' with large social-media followings who are routinely invited to speak at conferences and companies, yet this status generates its own invisible burdens (torrents of unsolicited messages, behind-the-scenes dispute adjudication) rather than relieving maintenance labor."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["burnout", "social-presence"]
    predictors: ["open-source-maintenance"]
population:
  who: "37 current or former maintainers/core contributors of free and open-source software (F/OSS) projects, purposively sampled for diversity in geography, gender, employment status/sector, and project type/size, focused on projects that began as volunteer efforts and became widely relied-upon infrastructure"
  where: ["United States", "multiple countries (14 countries of origin, 12 of residence, across 5 continents)"]
  when: "2019-2020"
  n: 37
  sector: ["open-source", "technology"]
  sample_notes: >
    Non-random, purposive plus snowball sampling via personal networks, F/OSS conferences, a
    Twitter call for participation, and cold e-mail; not intended to be representative.
    Post-interview demographic survey completed by 85%: 19% women/female, 81% men/male, 0%
    non-binary; 72% white/Caucasian; ages 25-64 (53% aged 30-39); US most common country of
    birth (47%) and residence (56%).
limitation:
  primary: "Non-random, self-selected sample of 37 maintainers recruited through personal networks, conferences, and snowball sampling limits generalizability, and the sample specifically excludes the overwhelming majority of F/OSS projects that are single-maintainer or entirely corporate-developed."
  others:
    - "Retrospective interview accounts may be inaccurate; the authors note the study could be complemented by participant-observation, diary studies, or trace-data analysis for more contemporaneous data."
    - "All three authors have direct personal experience as F/OSS contributors/maintainers and the research was funded by non-profit foundations that also directly fund F/OSS projects, which the authors acknowledge may have shaped interviewee responses and analytic distance."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's model of open-source maintainer burnout: the 'scalar
  labor'/'scalar debt' framework gives a design-relevant mechanism (organizational capacity
  failing to keep pace with growth) for predicting when community-health interventions are
  needed, and the paper's concrete drivers of burnout -- user-support overload, emotional
  labor from entitled users, funding-driven governance strain, and
  hypervisibility/microcelebrity dynamics -- are candidate measurable predictors for an SNH
  maintainer-burnout instrument.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["qualitative", "interview"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Academic/MD/The Labor of Maintaining and Scaling Free and Open-Source Software Projects/The Labor of Maintaining and Scaling Free and Open-Source Software Projects.md"
  pdf: "papers/Academic/The Labor of Maintaining and Scaling Free and Open-Source Software Projects.pdf"
  notes: null
