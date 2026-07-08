id: "finley-2021-how-open-source-maintainers-keep-contributorsand"
title: "How open source maintainers keep contributors—and themselves—happy"
authors:
  - "Finley, Klint"
year: 2021
doi: null
venue: {type: "other", name: "The ReadME Project (GitHub)", volume: null, issue: null, pages: null}
citation: "Finley (2021). How open source maintainers keep contributors—and themselves—happy. The ReadME Project (GitHub)."
article_type: "commentary"
method: {design: "case-study", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  This GitHub ReadME Project article reports practitioner advice from talks at the 2021
  Global Maintainer Summit on sustaining open-source contributor communities. Maintainers
  from projects like Kubernetes, Rust, Python, Homebrew, Prometheus, Home Assistant, and
  NgRX describe practices for attracting and retaining contributors: staying visibly active,
  responding quickly, offering recognition and escalating responsibility, automating triage
  (linters, bots, stale-issue closers), setting clear project scope, and saying no to
  proposals kindly and promptly. It frames contributor-relations work as central to
  maintainer sustainability and burnout prevention, arguing that scaling community
  management, not just code, is the key challenge facing popular projects.
claims:
  - text: "Multiple maintainers (Kubernetes' Brendan Burns, Tern's Rose Judge) emphasized that slow response times to issues and pull requests discourage future participation from both new and existing contributors."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["community-engagement", "retention"]
    predictors: ["leadership-style", "organizational-culture"]
  - text: "Automation of contribution triage (linters, auto-formatters, and custom bots such as Python's 'Bedevere' and 'Miss-islington') reduced maintainer workload and interpersonal friction, e.g. Homebrew's shift to automated code review eliminated maintainers being 'accused of being pedantic' over style disputes."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "collaboration"]
    predictors: ["workload", "open-source-maintenance"]
  - text: "Maintainers reported that avoiding scope creep and defining a clear project vision (e.g. NgRX's design documents) made it easier to decline contributions without guilt, and that framing rejections as directed at the proposal rather than the person preserved contributor goodwill."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "collaboration", "retention"]
    predictors: ["leadership-style", "boundary-management"]
population:
  who: "Maintainers and community leads of prominent open-source projects (Kubernetes, Rust, Python, Homebrew, Prometheus, Home Assistant, NgRX, Tern, FOSSASIA) speaking at GitHub's Global Maintainer Summit, June 8-9 2021"
  where: ["Global (open-source community, virtual/GitHub-hosted summit)"]
  when: "2021"
  n: null
  sector: ["open-source"]
  sample_notes: >
    Not a study; a journalistic summary of conference talks by a small, self-selected set of
    prominent maintainers. No systematic sampling, no quantitative data on how
    representative these practices are of maintainers broadly.
limitation:
  primary: "This is journalism synthesizing anecdotal advice from conference speakers, not original research; no data collection, sample, or empirical test of which practices actually improve contributor retention or maintainer wellbeing."
  others:
    - "Advice is drawn from a handful of high-profile, well-resourced projects (Kubernetes, Rust, Python) and may not generalize to smaller or resource-poor projects."
    - "The markdown conversion has severe character corruption (missing letters throughout, e.g. 'th' for 'the'), degrading readability though the substantive content remains inferable."
risk_of_bias: "high"
relevance_to_project: >
  Provides practitioner-level, ground-truth vocabulary and candidate mechanisms (response
  latency, automation of triage, scope-setting, rejection framing) linking maintainer
  burnout and contributor retention in open-source communities -- useful as a source of
  hypotheses to test empirically and as evidence that maintainer burden and 'saying no' are
  recognized, felt problems in the community the SNH project targets.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["case-study"]
  population: ["open-source"]
source:
  markdown: "Papers_Data/Articles/MD/How Open Source Maintainers Keep Contributors and Themselves Happy/How Open Source Maintainers Keep Contributors and Themselves Happy.md"
  pdf: "papers/Articles/How Open Source Maintainers Keep Contributors and Themselves Happy.pdf"
  notes: "no-doi: web article / no registered DOI found"
