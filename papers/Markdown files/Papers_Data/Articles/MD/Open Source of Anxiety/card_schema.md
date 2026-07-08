id: "zhu-2019-open-source-of-anxiety"
title: "(Open) source of anxiety"
authors:
  - "Zhu, Henry"
year: 2019
doi: null
venue: {type: "other", name: "Increment", volume: null, issue: null, pages: null}
citation: "Zhu (2019). (Open) source of anxiety. Increment."
article_type: "commentary"
method: {design: "case-study", approach: "other", evidence_level: "speculative", preregistered: false}
gist: >
  A first-person essay by Henry Zhu, a maintainer of the Babel JavaScript compiler and
  former maintainer of JSCS, recounts how open-source maintainer work eroded his boundaries
  and mental health, producing chronic anxiety and physical symptoms like insomnia, eczema,
  and backaches. He argues the mismatch between a huge, largely invisible user base and a
  tiny, under-resourced maintainer team is structural, and calls for transparency mechanisms
  (workload visibility, queue systems) and built-in rest cycles ('digital seasons') to make
  maintenance sustainable.
claims:
  - text: "The author describes experiencing sustained anxiety and physical symptoms (insomnia, eczema flare-ups, backaches) that he attributes directly to unbounded, always-on maintainer responsibilities and the inability to set boundaries around communication and availability."
    evidence: "case-study"
    support_strength: "speculative"
    outcomes: ["burnout", "anxiety", "mental-health"]
    predictors: ["workload", "boundary-management", "open-source-maintenance"]
  - text: "Babel, the compiler he maintains, was kept running by six people with only the author working on it full time, yet at the time of writing had over 1.7 million dependent repositories on GitHub and had surpassed 8.5 million weekly npm downloads for v7 alone -- a case illustration of the gap between infrastructure scale and maintainer capacity."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "sustainability"]
    predictors: ["workload", "open-source-maintenance"]
  - text: "The author argues that maintainer overload is worsened by lack of transparency about workload and queues, and by open-source culture having no equivalent of seasonal or ritual rest; he proposes visibility tools (e.g., a take-a-number style queue) and community-defined boundary practices as remedies."
    evidence: "case-study"
    support_strength: "speculative"
    outcomes: ["burnout", "communication"]
    predictors: ["boundary-management", "organizational-culture"]
population:
  who: "Single open-source maintainer (Babel, formerly JSCS) reflecting on his own personal experience; no other participants studied"
  where: []
  when: null
  n: 1
  sector: ["open-source", "software"]
  sample_notes: >
    First-person autobiographical essay, not a research study; no sampling, recruitment, or
    data collection procedures -- observations are drawn solely from the author's own
    retrospective account.
limitation:
  primary: "This is a single first-person, retrospective personal essay rather than a research study, so its observations reflect one individual's experience and cannot be generalized to maintainers broadly."
  others:
    - "No systematic data collection, measurement instruments, or comparison group"
    - "Published as an opinion/personal essay in a magazine (Increment), not peer-reviewed"
risk_of_bias: "high"
relevance_to_project: >
  Offers vivid first-person qualitative evidence of the mechanisms behind maintainer burnout
  in open-source communities -- blurred work/life boundaries, invisibility of non-coding
  labor, and severe mismatch between dependent user base and maintainer headcount --
  directly informing the SNH project's understanding of maintainer-burnout risk factors and
  possible boundary-management or workload-transparency interventions.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "mental-health", "wellbeing"]
  method: ["qualitative", "case-study"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Articles/MD/Open Source of Anxiety/Open Source of Anxiety.md"
  pdf: "papers/Articles/Open Source of Anxiety.pdf"
  notes: "no-doi: web article / no registered DOI found"
