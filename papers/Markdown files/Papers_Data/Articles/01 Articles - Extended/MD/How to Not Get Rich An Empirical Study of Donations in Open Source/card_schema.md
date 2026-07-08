id: "overney-2020-how-to-not-get-rich-an"
title: "How to Not Get Rich: An Empirical Study of Donations in Open Source"
authors:
  - "Overney, Cassandra"
  - "Meinicke, Jens"
  - "Kästner, Christian"
  - "Vasilescu, Bogdan"
year: 2020
doi: null
venue: {type: "conference", name: "Proceedings of the 42nd International Conference on Software Engineering (ICSE '20)", volume: null, issue: null, pages: null}
citation: "Overney et al. (2020). How to Not Get Rich: An Empirical Study of Donations in Open Source. Proceedings of the 42nd International Conference on Software Engineering (ICSE '20)."
article_type: "empirical"
method: {design: "mixed-methods", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This mixed-methods study mines GitHub and npm repositories to characterize the emerging
  phenomenon of open-source donations: how many projects ask for them, which platforms they
  use, what characteristics predict asking for and receiving funds, why developers say they
  want the money, and whether donations actually move the needle on project activity. It
  finds donation requests are rare (well under 1% of repositories), donations are often
  framed by maintainers as a last-ditch appeal tied to unsustainable workload, and receiving
  donations shows little to no measurable association with subsequent engineering activity,
  while projects that ask but fail to receive funding tend to decline further.
claims:
  - text: "25,885 of 77,934,441 GitHub repositories (0.04%) and 1,145 of 537,640 npm packages (0.2%) explicitly requested donations as of May 23, 2019, most commonly via PayPal and Patreon, with adoption rising steadily since about 2012."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["open-source-funding"]
    predictors: ["open-source-maintenance"]
  - text: "In qualitative analysis of 109 donation-request texts, 48% cited engineering activities (including paying a developer's salary) as the funding goal, with some maintainers explicitly framing appeals as a 'cry for help' before abandoning an unsustainable project (e.g., 'Before I give up ... completely I wanted to give this one last try')."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "help-seeking"]
    predictors: ["workload", "open-source-maintenance"]
  - text: "Interrupted time-series models on 337 projects found no significant short-term change in commit activity after a project's first donation (β=0.03, n.s.), only a weak positive association between total earnings and commit volume (~35% more commits per e-fold increase in funding), and a decline in activity among projects that asked for but never received donations."
    evidence: "longitudinal"
    support_strength: "low-to-moderate"
    outcomes: ["productivity", "retention"]
    predictors: ["intervention", "open-source-maintenance"]
population:
  who: "Open-source software projects hosted on GitHub (and the subset also published on npm) that publicly request donations via detectable platforms (PayPal, Patreon, OpenCollective, Kickstarter, etc.); deeper qualitative sub-samples of README files, donation-platform profile pages, and OpenCollective transaction ledgers were also analyzed."
  where: []
  when: "Snapshot as of May 23, 2019, with longitudinal repository history extending back to roughly 2012"
  n: 25885
  sector: ["software-development", "open-source"]
  sample_notes: >
    Population sizes vary by research question: full census across 77.9M GitHub repos /
    537,640 npm packages (RQ1-2); 25,885 GitHub / 1,145 npm donation-seeking repos plus
    matched non-donation controls for regression modeling (RQ3-4); a purposive qualitative
    sample of 109 repositories for coding donation expectations (RQ5); 337 projects meeting
    activity-window requirements for interrupted time-series modeling (RQ6); and 60 hand-
    coded plus 540 auto-classified OpenCollective projects for spending analysis (RQ7).
    Authors deliberately excluded surveys/interviews with maintainers for ethical reasons
    (avoiding burdening a population already flagged as stressed/burned out), relying only
    on public artifacts.
limitation:
  primary: "The study relies entirely on public repository artifacts (README files, donation-platform pages, GHTorrent metadata) and explicitly avoided surveys or interviews with developers, so it cannot capture private/undetectable donation channels (e.g., Bitcoin, informal sponsorship) or developers' actual psychological state, motivations, or stress levels—only what they chose to disclose publicly."
  others:
    - "The interrupted time-series outcome models are correlational and rely on only two coarse proxy measures (commit counts, issue-resolution speed) for a small subsample of well-funded projects, and explicitly could not measure hypothesized outcomes like reduced developer stress or burnout."
    - "Findings are restricted to projects using automatically detectable donation platforms on GitHub as of a single May 2019 snapshot and may not generalize to non-GitHub-hosted projects or undisclosed funding arrangements."
    - "Self-reported donation goals in README/profile text may not honestly reflect maintainers' true intentions due to self-censorship of less socially acceptable motives (acknowledged by the authors)."
risk_of_bias: "medium"
relevance_to_project: >
  Provides empirical grounding for the SNH project's interest in maintainer burnout and
  sustainability: it documents how rare donation-based funding actually is (0.04% of GitHub
  repos), how often donation appeals are explicitly framed as a workload-driven 'cry for
  help' rather than routine fundraising, and shows that receiving donations does little to
  measurably relieve activity/workload strain—evidence that money alone is an insufficient
  intervention for open-source maintainer wellbeing and that other social-support mechanisms
  deserve attention.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health", "methodology"]
  method: ["mixed-methods", "secondary-data", "regression-modeling"]
  population: ["open-source-maintainers", "github-repositories"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/How to Not Get Rich An Empirical Study of Donations in Open Source/How to Not Get Rich An Empirical Study of Donations in Open Source.md"
  pdf: "papers/Articles/01 Articles - Extended/How to Not Get Rich An Empirical Study of Donations in Open Source.pdf"
  notes: "no-doi: web article / no registered DOI found"
