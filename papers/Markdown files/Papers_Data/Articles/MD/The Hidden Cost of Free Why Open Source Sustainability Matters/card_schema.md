id: "bekahhw-2024-the-hidden-cost-of-free-why"
title: "The Hidden Cost of Free: Why Open Source Sustainability Matters"
authors:
  - "BekahHW"
year: 2024
doi: null
venue: {type: "other", name: "OpenSauced Blog", volume: null, issue: null, pages: null}
citation: "BekahHW (2024). The Hidden Cost of Free: Why Open Source Sustainability Matters. OpenSauced Blog."
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This OpenSauced blog post frames open-source software sustainability as a tragedy-of-the-
  commons problem: companies and users capture enormous value from OSS (citing an HBS
  estimate of $8.8 trillion in demand-side value versus $4.15 billion in supply-side value)
  while maintenance work falls on a small, often unpaid group of maintainers. Drawing on
  Nadia Eghbal's 'Working in Public' and the 2024 Tidelift State of the Open Source
  Maintainer Report (60% of maintainers unpaid, preference for recurring over one-time
  income, paid maintainers more likely to follow security practices), the piece argues that
  free-riding and lack of compensation drive maintainer burnout, security risk, and project
  abandonment, and proposes direct-payment models like Sentry's OSS Pledge as a remedy.
claims:
  - text: "Citing an HBS working paper (Hoffmann, Nagle & Zhou), the demand-side value of widely-used open source software is estimated at $8.8 trillion versus a supply-side value of $4.15 billion, and 96% of that demand-side value is created by only 5% of OSS developers."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["productivity"]
    predictors: ["open-source-maintenance", "network-structure"]
  - text: "The 2024 Tidelift State of the Open Source Maintainer Report found that 60% of maintainers remain unpaid for their work, and that paid maintainers are significantly more likely to implement critical security practices than unpaid ones."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["burnout", "retention"]
    predictors: ["open-source-maintenance", "organizational-culture"]
  - text: "The same Tidelift report found maintainers overwhelmingly prefer predictable, recurring income over one-time payments, motivating direct-payment interventions such as Sentry's OSS Pledge, which asks companies to pay a minimum of $2,000 per full-time-equivalent developer per year to maintainers of their choosing."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["burnout", "job-satisfaction"]
    predictors: ["intervention", "open-source-maintenance"]
population:
  who: "Open-source software maintainers and the companies/users who depend on their work, discussed through secondary sources rather than an original sample."
  where: []
  when: "2024"
  n: null
  sector: ["technology"]
  sample_notes: >
    Blog essay synthesizing secondary sources (an HBS working paper on OSS value, the 2024
    Tidelift State of the Open Source Maintainer Report, Nadia Eghbal's 'Working in Public',
    and Linux Foundation reports); no original data collection, sample, or methodology of
    its own.
limitation:
  primary: "This is an advocacy/opinion blog post rather than primary research: it synthesizes and paraphrases secondary reports without describing their methodology, sampling, or effect-size confidence, so the cited statistics cannot be independently verified from this document."
  others:
    - "Sources are chosen illustratively to support an argument rather than through a systematic search"
    - "Author is Developer Experience Lead at OpenSauced, a company with a commercial interest in open-source analytics and community narratives"
    - "No original quantitative or qualitative data collected by the author"
risk_of_bias: "high"
relevance_to_project: >
  Articulates a tragedy-of-the-commons mechanism (free-riding, uncompensated labor,
  concentrated maintenance burden) linking open-source sustainability to maintainer burnout
  and security risk, and surfaces survey evidence (60% unpaid; preference for recurring
  income) and a concrete compensation-based intervention (Sentry's OSS Pledge) relevant to
  the project's maintainer-burnout prevention and sustainability-intervention design
  questions.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["theory"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Articles/MD/The Hidden Cost of Free Why Open Source Sustainability Matters/The Hidden Cost of Free Why Open Source Sustainability Matters.md"
  pdf: "papers/Articles/The Hidden Cost of Free Why Open Source Sustainability Matters.pdf"
  notes: "no-doi: web article / no registered DOI found"
