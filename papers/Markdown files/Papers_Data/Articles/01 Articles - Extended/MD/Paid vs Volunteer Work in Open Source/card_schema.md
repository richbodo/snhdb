id: "riehle-2014-paid-vs-volunteer-work-in-open"
title: "Paid vs. Volunteer Work in Open Source"
authors:
  - "Riehle, Dirk"
  - "Riemer, Philipp"
  - "Kolassa, Carsten"
  - "Schmidt, Michael"
year: 2014
doi: "10.1109/hicss.2014.407"
venue: {type: "conference", name: "2014 47th Hawaii International Conference on System Sciences", volume: null, issue: null, pages: "3286-3295"}
citation: "Riehle et al. (2014). Paid vs. Volunteer Work in Open Source. 2014 47th Hawaii International Conference on System Sciences, 3286-3295. https://doi.org/10.1109/hicss.2014.407"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Analyzing commit timestamps from the Linux kernel (2005-2011) and a 2008 snapshot of over
  5,000 Ohloh open-source projects (2000-2007), the authors use a conservative working-hours
  proxy (Mon-Fri, 9am-5pm local time = paid work) to estimate that roughly 50% of all open-
  source contribution has been paid corporate work for years, with the paid share flat over
  time in the broad Ohloh sample but rising then plateauing for Linux. They propose the
  ratio of paid to volunteer contributors as a practical indicator project leaders can use
  to gauge community health, noting small projects are often fully company-paid while large,
  healthy public projects sustain a 10-20% paid-developer mix alongside volunteers.
claims:
  - text: "About 50% of all open-source commits occurred during working hours: 45.00% of Linux kernel author contributions and 51.36% of committer integrations were made Mon-Fri 9am-5pm, versus 47.3% (known committers) and 55.4% (extended committers) for the 5,117-project Ohloh sample."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["open-source-maintenance", "organizational-culture"]
  - text: "The share of working-time (paid) contribution to the broad Ohloh project sample stayed statistically flat from 2000-2007 (F-test rejects any trend at 98% confidence) despite near-exponential growth in overall project activity, while the Linux kernel showed a clear upward trend in paid work from 2007-2010 that then plateaued."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["open-source-maintenance"]
  - text: "Using a conservative 95%+ working-hours threshold to classify 'paid developers,' at least 23.15% of Linux kernel authors and 11.28% of committers, and 17.97% of Ohloh extended committers, were paid; many of the smallest OSS projects were fully company-paid, while large healthy public projects (e.g. GNOME, Eclipse, KDE) maintained a 10-20% paid-developer share alongside volunteers."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["retention", "turnover"]
    predictors: ["open-source-maintenance", "organizational-culture"]
population:
  who: "Software developers/committers contributing to the Linux kernel and to a large cross-section of active open-source projects; unit of analysis is commit-level timestamps, not surveyed individuals."
  where: ["Global (contributor timezones inferred); activity strongly dominated by Western/Christian-calendar countries"]
  when: "Linux kernel: 2005-2011 commit history; Ohloh projects: 2000-2007 commit history from a 2008 database snapshot"
  n: 5117
  sector: ["open-source"]
  sample_notes: >
    Ohloh sample of 5,117 'active' projects (~30% of an estimated 18,000 active OSS projects
    circa 2007) drawn from an 8.7M-commit, 9,192-project snapshot; only 45,870 distinct
    committers, of whom just 580 (1.3%, but 8% of commits) had hand-identified timezones
    ('known committers'), with the rest timezone-imputed via a least-squares heuristic
    ('extended committers'). Paid-work status is inferred purely from commit timing, not
    verified employment records, and a bias check (t-test across activity-ranked committer
    bins) failed to reject the no-bias null but could not rule bias out.
limitation:
  primary: "Paid vs. volunteer status is inferred indirectly from whether a commit timestamp falls in a Mon-Fri 9am-5pm window, not from actual employment or compensation data, so misclassification (enthusiast paid developers working off-hours, or volunteers with flexible daytime schedules) is likely and the authors themselves call the paid-developer estimate a conservative lower bound."
  others:
    - "Ohloh data is an aging 2008 snapshot (activity through 2007) and no comparably detailed public dataset was available to update it at time of writing."
    - "The working-hours definition encodes a Western Mon-Fri workweek assumption; the analysis notes cultures with Saturday workweeks show little open-source activity, but this could still misclassify contributors elsewhere."
    - "Ohloh could not distinguish authors from committers (unlike Git-based Linux data), and timezone assignment for the majority of committers is a statistical estimate rather than a direct observation."
risk_of_bias: "medium"
relevance_to_project: >
  Offers a concrete, low-cost behavioral metric (paid/volunteer contributor ratio, derivable
  from commit timestamps) that the SNH project could adapt as an indicator of open-source
  community health and sustainability risk, complementing self-report measures of maintainer
  burnout; the finding that healthy large projects sustain ~10-20% paid contributors
  alongside volunteers gives a reference range for evaluating whether a project's
  paid/volunteer balance signals health versus over-reliance on either group.
tags:
  topic: ["open-source", "community-health", "maintainer-burnout", "methodology"]
  method: ["secondary-data", "longitudinal"]
  population: ["open-source-contributors"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Paid vs Volunteer Work in Open Source/Paid vs Volunteer Work in Open Source.md"
  pdf: "papers/Articles/01 Articles - Extended/Paid vs Volunteer Work in Open Source.pdf"
  notes: null
