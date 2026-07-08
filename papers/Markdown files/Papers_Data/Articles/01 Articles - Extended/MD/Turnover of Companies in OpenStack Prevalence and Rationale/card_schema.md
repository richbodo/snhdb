id: "zhang-2022-turnover-of-companies-in-openstack-prevalence"
title: "Turnover of Companies in OpenStack: Prevalence and Rationale"
authors:
  - "Zhang, Yuxia"
  - "Liu, Hui"
  - "Tan, Xin"
  - "Zhou, Minghui"
  - "Jin, Zhi"
  - "Zhu, Jiaxin"
year: 2022
doi: "10.1145/3510849"
venue: {type: "journal", name: "ACM Transactions on Software Engineering and Methodology", volume: 31, issue: 4, pages: "1-24"}
citation: "Zhang et al. (2022). Turnover of Companies in OpenStack: Prevalence and Rationale. ACM Transactions on Software Engineering and Methodology, 31(4), 1-24. https://doi.org/10.1145/3510849"
article_type: "empirical"
method: {design: "mixed-methods", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This mixed-methods study of 18 versions of OpenStack finds that company (not just
  individual developer) withdrawal is common and accelerating: about 12% of sustaining
  companies exit each version, and 266 of 490 companies (54%) ultimately withdrew, with
  withdrawals outpacing new company joins after version 13. Withdrawn companies contributed
  far less before leaving (median 1 developer, 6 commits, 3 repos) and had roughly 2.7x
  lower contribution intensity than companies that stayed, though similar breadth of
  repositories touched. An email survey and Cox survival model show withdrawal reasons
  cluster into company, community, developer, and project factors, with achieving or failing
  a commercial goal most common, and low contribution intensity, business-integration goals,
  and small company scale statistically predicting withdrawal.
claims:
  - text: "Approximately 12% of companies sustaining in a given OpenStack version withdraw by the next version, and more than half of companies that join in any given version eventually withdraw; the number of withdrawing companies surpasses new joiners starting around version 13-14, ending the ecosystem's growth trend in contributing organizations."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "retention"]
    predictors: ["organizational-culture", "community-engagement"]
  - text: "Withdrawn companies (n=266) made limited contributions before leaving (median 1 developer, 6 commits, 3 repositories, 2 versions) and had a contribution intensity approximately 2.7 times lower than companies that joined in the same version but stayed (Mann-Whitney p=0.037, medium effect r=-0.36), while contribution extent (repository scope) was similar between the two groups (p=0.63, r=-0.086)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "collaboration"]
    predictors: ["community-engagement", "organizational-culture"]
  - text: "A Cox survival model (n=977 company-versions, 260 withdrawal events, concordance=0.86) found lower contribution intensity, an 'integrating business' commercial goal, and being a development-infrastructure vendor significantly predicted higher withdrawal hazard, while larger company scale (1,000-10,000+ employees, hazard reduced ~83%) and a 'selling partial solutions' goal predicted higher survival; project/community domination was not a significant predictor despite being frequently cited in survey responses."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["turnover", "retention"]
    predictors: ["organizational-culture", "workload", "community-engagement"]
population:
  who: "Companies contributing code to the OpenStack open-source cloud-computing ecosystem across 18 software versions (roughly a decade), plus a subset of their developer representatives surveyed by email"
  where: ["international (OpenStack global contributor base, company HQs not restricted to one country)"]
  when: "OpenStack versions 1 through 18 (approx. 2010-2021), data collected/analyzed through January 2021"
  n: 490
  sector: ["open-source", "technology"]
  sample_notes: >
    490 companies and 9,653 developers across 1,292 repositories and 338,035 commits form
    the core commit-mining dataset (266 identified as withdrawn, ~89% validated accuracy).
    Email survey of 455 candidate developer-representatives from withdrawn companies yielded
    38 responses from 37 distinct companies (16% response rate after excluding 222 bounced
    emails), a plausible source of self-report and selection bias. Survival model used a
    smaller manually-coded subsample of 60 withdrawn and 60 sustaining companies for
    commercial-goal data.
limitation:
  primary: "Withdrawal is inferred algorithmically from commit-history gaps (not confirmed departure) for the large-scale quantitative analysis, and while manually validated at ~89% accuracy, the method only captures withdrawal from source-code contribution, missing other contribution types (reviewing, issue reporting) that some 'withdrawn' companies may still perform."
  others:
    - "Email survey has a low 16% response rate and relies on self-reported reasons from company representatives, who may self-censor or give socially acceptable rather than true reasons for withdrawal."
    - "The survival model's commercial-goal and scale data were manually coded for only a 120-company subsample, limiting statistical power and generalizability of the predictive factors."
    - "Single-ecosystem case study (OpenStack only); authors note generalization is to theoretical propositions, not necessarily to all OSS ecosystems, especially those less dominated by commercial contributors."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs how the SNH project might operationalize organizational-level
  'turnover/retention' and 'community-engagement' constructs beyond individual developers:
  it offers a validated method (contribution-interval survival analysis) and concrete
  predictors (contribution intensity, organizational goal type, organizational scale) for
  detecting disengagement risk in open-source/tech communities before it happens, which is
  transferable to designing early-warning or retention interventions for maintainer and
  contributor-organization health.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "measurement"]
  method: ["mixed-methods", "secondary-data", "survey"]
  population: ["open-source-contributors", "organizations"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Turnover of Companies in OpenStack Prevalence and Rationale/Turnover of Companies in OpenStack Prevalence and Rationale.md"
  pdf: "papers/Articles/01 Articles - Extended/Turnover of Companies in OpenStack Prevalence and Rationale.pdf"
  notes: null
