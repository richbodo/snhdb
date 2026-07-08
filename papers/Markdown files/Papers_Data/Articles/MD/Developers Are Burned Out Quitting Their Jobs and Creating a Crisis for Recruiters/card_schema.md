id: "case-2022-developers-are-burned-out-quitting-their"
title: "Developers are burned out, quitting their jobs and creating a crisis for recruiters"
authors:
  - "Case, Tony"
year: 2022
doi: null
venue: {type: "other", name: "WorkLife (worklife.news)", volume: null, issue: null, pages: null}
citation: "Case (2022). Developers are burned out, quitting their jobs and creating a crisis for recruiters. WorkLife (worklife.news)."
article_type: "commentary"
method: {design: "theory", approach: "interview", evidence_level: "weak", preregistered: false}
gist: >
  This WorkLife.news trade article reports that software developers are burning out and
  leaving jobs in large numbers, citing two vendor survey reports (LaunchDarkly and EDB) and
  quoting five engineering executives on causes and fixes. The executives point to
  distributed-team communication breakdowns, expanded developer responsibilities (QA,
  security, license compliance), and lack of autonomy or onboarding support as drivers of
  burnout and attrition, and describe practices like asynchronous communication, deep-focus
  time blocks, and periodic in-person team bonding as mitigations.
claims:
  - text: "A LaunchDarkly report found that nearly 7 in 10 developers (67%) have left a job (or know someone who has) due to pressure around minimizing deployment errors, and 61% said their companies' cumbersome development processes are barriers to innovation."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["turnover", "burnout", "productivity"]
    predictors: ["workload", "organizational-culture", "technostress"]
  - text: "An EDB survey found that just under half (46%) of developers said they were very satisfied in their current roles, even as they continued to weigh other job options amid a possible recession."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["job-satisfaction", "turnover"]
    predictors: ["organizational-culture", "workload"]
  - text: "Engineering leaders interviewed attributed developer burnout in fully distributed teams primarily to poor intra-team communication and unclear vision/mission, and separately to insufficient structure and support for early- and mid-career hires, arguing this forces companies to over-hire scarce senior developers."
    evidence: "qualitative"
    support_strength: "speculative"
    outcomes: ["burnout", "turnover", "communication"]
    predictors: ["team-cohesion", "remote-work-intensity", "leadership-style", "autonomy"]
population:
  who: "Software developers and engineering leaders in the tech industry, as characterized in two vendor-commissioned surveys and quotes from five named engineering executives (Sonatype, ClickUp, Jobsity, Kong, Netlify)"
  where: ["USA"]
  when: "2022"
  n: null
  sector: ["tech", "open-source"]
  sample_notes: >
    This is a journalism piece, not a primary study: it summarizes findings from two
    external vendor surveys (LaunchDarkly report; EDB 'Open Source Talent Survey 2022')
    without giving their sample sizes, response rates, or methodology, and supplements them
    with opinion quotes from five engineering executives with no disclosed selection method.
limitation:
  primary: "Trade-journalism piece that reports secondhand statistics from two vendor-commissioned surveys without any methodological detail (sample size, response rate, instrument), so the cited percentages cannot be independently assessed for rigor."
  others:
    - "Causal claims about burnout drivers (remote/distributed communication, lack of autonomy) come from unstructured executive opinion quotes, not from any study design."
    - "Executives quoted have a commercial interest in promoting their own companies' tools or practices (e.g. async communication, deep-focus blocks), which is a source of bias."
risk_of_bias: "high"
relevance_to_project: >
  Captures practitioner-level framing of developer and open-source-maintainer burnout
  drivers -- distributed-team communication gaps, expanded on-call/security
  responsibilities, low autonomy, and weak onboarding support -- plus proposed mitigations
  (async communication, protected deep-focus time, periodic in-person bonding) that the SNH
  project can use as candidate intervention ideas to test against stronger evidence, not as
  evidence itself.
tags:
  topic: ["burnout", "remote-work", "open-source", "maintainer-burnout", "job-satisfaction"]
  method: ["qualitative", "cross-sectional"]
  population: ["software-developers", "tech", "open-source", "remote-workers"]
source:
  markdown: "Papers_Data/Articles/MD/Developers Are Burned Out Quitting Their Jobs and Creating a Crisis for Recruiters/Developers Are Burned Out Quitting Their Jobs and Creating a Crisis for Recruiters.md"
  pdf: "papers/Articles/Developers Are Burned Out Quitting Their Jobs and Creating a Crisis for Recruiters.pdf"
  notes: "no-doi: web article / no registered DOI found"
