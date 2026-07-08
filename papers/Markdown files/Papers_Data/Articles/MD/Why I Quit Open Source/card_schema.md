id: "sapegin-nd-why-i-quit-open-source"
title: "Why I quit open source"
authors:
  - "Sapegin, Artem"
year: null
doi: null
venue: {type: "other", name: "sapegin.me (personal blog)", volume: null, issue: null, pages: null}
citation: "Sapegin (None). Why I quit open source. sapegin.me (personal blog)."
article_type: "commentary"
method: {design: "case-study", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  A veteran open-source maintainer (roughly ten years, publisher of the widely-used React
  Styleguidist project) explains in first person why he quit maintaining open-source
  software entirely, arguing that quitting, not the moderation tips in GitHub's official
  burnout-avoidance guide, was the only solution that actually worked for him. He attributes
  his burnout to entitled and toxic users, low-quality drive-by pull requests, failure to
  build a sustaining contributor community even around a 10K-star project, near-zero
  financial compensation, and mounting tooling/configuration overhead, and closes by
  describing how he now treats his repos as private projects that happen to be public.
claims:
  - text: "The maintainer reports receiving essentially no sustainable income from a decade of open-source work: an Open Collective project budget of about $8/month, zero results from GitHub Sponsors aside from one $550 payment from GitHub itself that was later cancelled, and no payments via a 'Buy Me a Coffee' link despite the project's popularity."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "job-satisfaction"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "Even his most popular project (10,000+ GitHub stars) never developed a self-sustaining contributor community; occasional volunteers still required heavy guidance from him, so the project remained a single point of failure that would stop entirely if he stopped working on it."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration", "isolation", "burnout"]
    predictors: ["community-engagement", "network-structure", "open-source-maintenance"]
  - text: "He identifies entitled/toxic user behavior (demands, insults, spam pings, low-effort 'hit and run' pull requests, and abuse during Hacktoberfest) as a primary driver of burnout, and argues GitHub's platform does too little to detect, remove, or discourage this behavior."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["burnout", "stress"]
    predictors: ["open-source-maintenance", "psychological-safety", "workload"]
population:
  who: "A single individual open-source maintainer (JavaScript/TypeScript ecosystem, author of React Styleguidist and other projects) recounting roughly ten years of unpaid maintenance work."
  where: []
  when: null
  n: 1
  sector: ["tech", "open-source"]
  sample_notes: >
    First-person autobiographical blog post; n=1, no systematic data collection, no external
    verification of the claims about compensation or contribution volume.
limitation:
  primary: "Single-author anecdotal account with no independent data or systematic sampling; findings are one maintainer's retrospective attribution of his own burnout and cannot be generalized to open-source maintainers broadly."
  others:
    - "No date given in the source, so it is unclear how recent the experience or the GitHub ecosystem context is."
    - "Written explicitly as a rebuttal to a specific GitHub guide, which frames the piece argumentatively rather than as neutral description."
risk_of_bias: "high"
relevance_to_project: >
  Provides a vivid, specific first-person account of the mechanisms (unrewarded labor, toxic
  user entitlement, inability to build a sustaining community, tooling overhead) that the
  project's maintainer-burnout and open-source community-health design work needs to
  address; useful as illustrative evidence and for generating hypotheses, not as a causal or
  generalizable finding.
tags:
  topic: ["maintainer-burnout", "open-source", "burnout", "community-health"]
  method: ["case-study"]
  population: ["software-developers", "open-source-maintainers"]
source:
  markdown: "Papers_Data/Articles/MD/Why I Quit Open Source/Why I Quit Open Source.md"
  pdf: "papers/Articles/Why I Quit Open Source.pdf"
  notes: "no-doi: confirmed none (manual review)"
