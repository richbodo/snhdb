id: "bekahhw-2024-the-silent-crisis-in-open-source"
title: "The Silent Crisis in Open Source: When Maintainers Walk Away"
authors:
  - "BekahHW"
year: 2024
doi: null
venue: {type: "other", name: "OpenSauced Blog", volume: null, issue: null, pages: null}
citation: "BekahHW (2024). The Silent Crisis in Open Source: When Maintainers Walk Away. OpenSauced Blog."
article_type: "commentary"
method: {design: "theory", approach: "other", evidence_level: "speculative", preregistered: false}
gist: >
  This OpenSauced blog post uses the 2022 departure of node-pre-gyp maintainer Dane
  Springmeyer as a case to argue that open source projects face a 'silent crisis' of
  maintainer attrition driven by burnout, loneliness, and lack of institutional support. It
  proposes two quantitative proxies for project vulnerability -- the Lottery Factor
  (dependency concentration among top contributors) and Contributor Confidence (likelihood
  that stargazers/forkers return to contribute) -- and calls for sustainable funding,
  succession planning, and community health metrics as mitigations.
claims:
  - text: "A project is considered vulnerable by the Lottery Factor metric if two or fewer contributors account for 50% or more of the project's pull request contributions, indicating a single point of failure risk."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["turnover", "collaboration"]
    predictors: ["open-source-maintenance", "network-structure"]
  - text: "The Contributor Confidence metric predicts the likelihood that users who star or fork a repository return to make contributions; a score in the 30-40% range is described as indicating a healthy, active project."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["retention", "collaboration"]
    predictors: ["community-engagement", "sense-of-belonging"]
  - text: "The author frames maintainer departures (e.g., node-pre-gyp, Faker.js) as driven by burnout, loneliness, and an unsustainable 'free labor' model, and argues this causes loss of institutional knowledge, security vulnerabilities, and cascading risk to dependent projects."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "turnover", "isolation"]
    predictors: ["workload", "social-support", "open-source-maintenance"]
population:
  who: "Not a research sample; a practitioner blog post illustrated by anecdotal cases of individual open source maintainers (e.g., Dane Springmeyer of node-pre-gyp, Marak Squires of Faker.js)."
  where: []
  when: "2024"
  n: null
  sector: ["open-source"]
  sample_notes: >
    No systematic data collection; single case anecdote plus references to two proprietary
    OpenSauced platform metrics without validation data, methodology, or citations to peer-
    reviewed sources.
limitation:
  primary: "No empirical evidence, data, or methodology is presented; claims about burnout, loneliness, and metric validity are asserted rather than tested or sourced."
  others:
    - "Promotes the author's own company's (OpenSauced) proprietary metrics without independent validation."
    - "Relies on a single anecdotal case (node-pre-gyp) generalized to the whole open source ecosystem."
risk_of_bias: "high"
relevance_to_project: >
  Illustrates practitioner-level framing of maintainer burnout and loneliness as a social-
  network-health problem in open source, and surfaces two candidate operational metrics
  (Lottery Factor, Contributor Confidence) that could inform SNH measures of community
  concentration risk and engagement health, though neither is empirically validated here.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "burnout"]
  method: ["theory"]
  population: ["open-source"]
source:
  markdown: "Papers_Data/Articles/MD/The Silent Crisis in Open Source When Maintainers Walk Away/The Silent Crisis in Open Source When Maintainers Walk Away.md"
  pdf: "papers/Articles/The Silent Crisis in Open Source When Maintainers Walk Away.pdf"
  notes: "no-doi: web article / no registered DOI found"
