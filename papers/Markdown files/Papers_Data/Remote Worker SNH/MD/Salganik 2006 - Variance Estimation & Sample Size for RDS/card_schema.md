id: "salganik-2006-variance-estimation-design-effects-and-sample"
title: "Variance Estimation, Design Effects, and Sample Size Calculations for Respondent-Driven Sampling"
authors:
  - "Salganik, Matthew J."
year: 2006
doi: "10.1007/s11524-006-9106-x"
venue: {type: "journal", name: "Journal of Urban Health", volume: 83, issue: "S1", pages: null}
citation: "Salganik (2006). Variance Estimation, Design Effects, and Sample Size Calculations for Respondent-Driven Sampling. Journal of Urban Health, 83(S1). https://doi.org/10.1007/s11524-006-9106-x"
article_type: "methods"
method: {design: "methods", approach: "modelling", evidence_level: "moderate", preregistered: false}
gist: >
  This methodological paper develops a bootstrap procedure for constructing confidence
  intervals around respondent-driven sampling (RDS) prevalence estimates and shows via
  simulation that it outperforms the 'naive' method that ignores the complex link-tracing
  sample design. It also characterizes RDS design effects across simulated network
  structures (ranging from below 1 to as high as 10, depending on interconnectedness and
  degree distribution) and, using data from six real RDS studies, estimates a typical design
  effect of about 2, leading to a practical recommendation that RDS studies use roughly
  double the sample size that simple random sampling would require. The paper is
  foundational for anyone designing a network-based (chain-referral) survey of a hard-to-
  reach population and wanting statistically defensible uncertainty estimates and sample-
  size planning.
claims:
  - text: "In simulations, the proposed bootstrap percentile-method confidence intervals achieved coverage close to nominal (phi_boot ~ 0.9 for a 90% interval) and consistently outperformed the naive method (which treats RDS data as a simple random sample), which produced intervals that were too narrow across all tested parameter ranges."
    evidence: "methods"
    support_strength: "moderate"
    outcomes: ["estimation-precision"]
    predictors: ["sampling-method"]
  - text: "RDS design effects (variance inflation relative to simple random sampling) varied widely with network structure: they generally exceeded 1, decreased as interconnectedness between subgroups (I) increased, were minimized when subgroups had equal total degree (P_A D_A = P_B D_B) rather than equal average degree, and were sensitive to the assumed degree distribution (Poisson degree distributions produced markedly lower, sometimes sub-1, design effects than exponential distributions)."
    evidence: "methods"
    support_strength: "moderate"
    outcomes: ["estimation-precision"]
    predictors: ["network-structure", "sampling-method"]
  - text: "Applying the method to six published RDS studies (Latino gay men in Chicago n=69 and San Francisco n=72, MDMA/Ecstasy users in Ohio n=374, and jazz musicians in New York City n=253-263) yielded estimated design effects ranging from 1.1 to 2.4, averaging around 2; based on this, the paper recommends that RDS studies plan for a sample size roughly twice what simple random sampling would require."
    evidence: "methods"
    support_strength: "low-to-moderate"
    outcomes: ["estimation-precision"]
    predictors: ["sampling-method", "network-structure"]
population:
  who: "Simulated hidden populations (networks of 10,000 nodes with a binary trait split across two groups) plus six previously published respondent-driven sampling field studies of hard-to-reach groups: Latino gay men, MDMA/Ecstasy users, and jazz musicians."
  where: ["USA"]
  when: null
  n: null
  sector: ["public-health", "hidden-populations"]
  sample_notes: >
    Simulation results are based on constructed hypothetical populations, not real-world
    sampling, so generalizability depends on how well simulated degree/interconnectedness
    assumptions match real hidden populations; the real-study design-effect estimates (Table
    1) come from only six previously published RDS datasets with sample sizes of 69-374, a
    small and non-random selection of available RDS studies.
limitation:
  primary: "The core design-effect findings are derived entirely from computer simulation and 'have not been verified analytically' because no closed-form expression for RDS variance could be derived, so their generalization to arbitrary real networks is uncertain."
  others:
    - "The design effect was found to be highly sensitive to the assumed degree distribution (Poisson vs. exponential) for reasons the author states are 'currently unknown', undermining confidence in any single point recommendation."
    - "The real-study design-effect estimates (~2) come from only six datasets, all analyzed with the paper's own bootstrap method, so the 'assume a design effect of 2' rule of thumb is explicitly labeled 'preliminary' and may not hold for populations with different network structures."
    - "Degree (network size) in RDS relies on self-reported number of relationships, which the author notes may be inaccurate and can bias prevalence estimates independent of the variance issues addressed here."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Respondent-driven sampling is a network-based recruitment and estimation method for
  populations that are hard to enumerate through standard sampling frames; this paper's
  design-effect and sample-size guidance (assume ~2x the SRS sample size, verify precision
  via bootstrap CIs) is directly applicable if the SNH project needs to survey a hidden or
  hard-to-reach subgroup (e.g., isolated remote workers, burned-out maintainers not visible
  through official rosters) via peer referral rather than a known sampling frame, and warns
  that naive confidence intervals on such chain-referral samples will be systematically too
  narrow.
tags:
  topic: ["methodology", "measurement"]
  method: ["simulation", "bootstrap", "sampling-method"]
  population: ["hidden-populations", "public-health"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Salganik 2006 - Variance Estimation & Sample Size for RDS/Salganik 2006 - Variance Estimation & Sample Size for RDS.md"
  pdf: "papers/Remote Worker SNH/Salganik 2006 - Variance Estimation & Sample Size for RDS.pdf"
  notes: null
