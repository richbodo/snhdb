id: "anon-nd-release-assurance-why-innovative-software-delivery"
title: "Release Assurance: Why Innovative Software Delivery Starts with Trust and Psychological Safety"
authors:
year: null
doi: null
venue: {type: "report", name: "LaunchDarkly", volume: null, issue: null, pages: null}
citation: "LaunchDarkly (None). Release Assurance: Why Innovative Software Delivery Starts with Trust and Psychological Safety. LaunchDarkly."
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low", preregistered: false}
gist: >
  This vendor-commissioned survey report from LaunchDarkly (a feature-flag/release-
  management company) surveys 500 software developers and finds that psychological safety
  and leadership support around release risk are strongly tied to job satisfaction and
  retention. It reports that 67% of developers have quit or know a colleague who quit over
  pressure to minimize deployment mistakes, that job satisfaction is far higher when
  leadership prioritizes developer outcomes, and that confidence in a team's ability to
  safely release code is linked to felt empowerment to innovate.
claims:
  - text: "67% of developers say they themselves have quit a job (36%) or know someone who has (35%, overlapping categories) due to pressure to minimize deployment mistakes/rollbacks; among those who describe their release process as an obstacle to innovation, 74% report this quitting behavior, rising to 78% at companies where developer outcomes are a low priority."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["turnover", "retention"]
    predictors: ["psychological-safety", "leadership-style", "organizational-culture"]
  - text: "92% of developers report being very (53%) or somewhat (39%) satisfied with their job; satisfaction is sharply higher (86%) at companies where leadership treats improving developer outcomes as a top/large priority versus only 14% satisfied where it is not a priority."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction"]
    predictors: ["leadership-style", "psychological-safety"]
  - text: "93% of developers agree that gaining confidence in their team's ability to safely release code makes them feel empowered to innovate more (52% strongly agree), and 56% say smaller, more frequent deployments would increase their confidence versus larger, less frequent ones."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-engagement", "productivity"]
    predictors: ["psychological-safety", "workload"]
population:
  who: "500 software developers across a range of industries and job titles, surveyed for a LaunchDarkly-commissioned industry report"
  where: []
  when: null
  n: 500
  sector: ["technology", "software"]
  sample_notes: >
    Vendor-commissioned market-research survey; sampling frame, recruitment method, country
    mix, and survey instrument are not disclosed in the report, so representativeness cannot
    be assessed.
limitation:
  primary: "This is a vendor marketing/lead-generation report (published by LaunchDarkly, a release-management tool vendor) with no disclosed sampling methodology, response rate, or peer review, so findings should be treated as directional industry-survey data rather than rigorous research."
  others:
    - "All findings are self-reported cross-sectional percentages with no statistical testing, confidence intervals, or controls for confounds."
    - "Turnover figures rely on retrospective recall ('have you or someone you know ever quit'), which is prone to recall and social-desirability bias."
    - "No demographic, geographic, or company-size breakdown is given, limiting generalizability."
risk_of_bias: "high"
relevance_to_project: >
  Offers industry (non-academic) survey evidence that developers' perceived psychological
  safety around risk-taking and release process is linked to job satisfaction and self-
  reported turnover, which is relevant to the SNH project's interest in how organizational
  trust/leadership support functions as a predictor of burnout-adjacent turnover and
  retention in tech workplaces — though the vendor-sponsored, undisclosed-methodology nature
  means it should be cited as weak/corroborating evidence only, not as a primary source.
tags:
  topic: ["psychological-safety", "job-satisfaction", "productivity", "technostress"]
  method: ["survey"]
  population: ["software-developers", "industry-survey"]
source:
  markdown: "Papers_Data/Articles/MD/LaunchDarkly Release Assurance Why Innovative Software Delivery Starts with Trust and Psychological Safety/LaunchDarkly Release Assurance Why Innovative Software Delivery Starts with Trust and Psychological Safety.md"
  pdf: "papers/Articles/LaunchDarkly Release Assurance Why Innovative Software Delivery Starts with Trust and Psychological Safety.pdf"
  notes: "no-doi: web article / no registered DOI found"
