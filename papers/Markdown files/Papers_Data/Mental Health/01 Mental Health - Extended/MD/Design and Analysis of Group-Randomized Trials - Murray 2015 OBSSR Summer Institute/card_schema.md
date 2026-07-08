id: "murray-2007-design-and-analysis-of-group-randomized"
title: "Design and Analysis of Group-Randomized Trials"
authors:
  - "Murray, David M"
year: 2007
doi: "10.1093/oso/9780195120363.001.0001"
venue: {type: "book", name: null, volume: null, issue: null, pages: null}
citation: "Murray (2007). Design and Analysis of Group-Randomized Trials.. https://doi.org/10.1093/oso/9780195120363.001.0001"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This is a training slide deck by David Murray (NIH OBSSR) on the design and analysis of
  group-randomized trials (GRTs) and individually randomized group treatment trials (IRGTs)
  — designs where an intervention is delivered to intact groups (worksites, clinics,
  communities, small treatment groups) rather than to independent individuals. It explains
  why the intraclass correlation (ICC) among members of the same group inflates variance and
  Type I error when analyses ignore the nested structure, and lays out which analytic
  strategies (mixed-model ANOVA/ANCOVA, random coefficients models, GEE, randomization
  tests) preserve valid inference. It is a methodological reference for anyone planning to
  evaluate a group- or community-level intervention rather than an empirical SNH study
  itself.
claims:
  - text: "Analyzing data from a group-randomized or individually-randomized-group-treatment trial as if participants were independently randomized (ignoring the positive intraclass correlation among group members) inflates the Type I error rate — often to 30-50% in GRTs and 15-25% in IRGTs — even when the ICC is small."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["type-i-error-rate"]
    predictors: ["intraclass-correlation", "network-structure"]
  - text: "The design effect (DEFF), which quantifies how much variance is inflated by clustering, rises sharply with both the ICC and the number of members per group; worked examples show DEFF reaching 25.95 for a GRT with ICC=0.05 and 500 members per group, meaning statistical power collapses unless this is accounted for at the design stage."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["type-i-error-rate"]
    predictors: ["intraclass-correlation", "network-structure"]
  - text: "Mixed-model ANOVA/ANCOVA (General or Generalized Linear Mixed Model) maintains nominal Type I error rates across a wide range of GRT conditions when there are one or two measurement time points, but has an inflated Type I error rate when group-specific trends are heterogeneous over three or more time points — in which case random coefficients (growth curve) models are recommended instead."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["type-i-error-rate"]
    predictors: ["study-design", "cluster-randomization"]
population:
  who: "No original human sample; a statistical-methods lecture illustrating GRT/IRGT design and analysis using examples from named NIH-funded trials (e.g., the Health Care Systems Collaboratory's 7 pragmatic trials, the Childhood Obesity Prevention and Treatment Research studies) and citations to prior simulation work."
  where: ["USA"]
  when: "2015"
  n: null
  sector: ["healthcare", "academia"]
  sample_notes: >
    Conference/training slide deck (2015 OBSSR Summer Institute); presents no original data
    collection, only worked formulas, illustrative tables, and references to prior published
    simulation studies (e.g., Gail et al. 1996; Varnell et al. 2001) to support its
    recommendations.
limitation:
  primary: "As a slide-deck training presentation rather than a peer-reviewed paper, its claims are stated without full methodological detail and rely on citing prior primary/simulation studies by author-year rather than reproducing their results."
  others:
    - "Not an empirical or SNH-specific study — it is general statistical methodology for cluster/group-randomized designs applicable to any group-level health intervention, not specifically to remote work, isolation, or social network health."
    - "Several illustrative figures (power/precision tradeoffs, design diagrams) are embedded images not captured as text in this conversion, limiting reproducibility of some numeric examples."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Directly useful if the SNH project ever evaluates a team-, org-, or community-level
  intervention (e.g., a manager-training or community-engagement program rolled out to whole
  teams) rather than randomizing individuals: it explains why individual-level analysis of
  such designs produces false-positive intervention effects and prescribes the mixed-model,
  random-coefficients, and GEE approaches needed for valid inference and power calculations
  in that scenario.
tags:
  topic: ["methodology", "measurement"]
  method: ["theory"]
  population: ["research-methodologists"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Design and Analysis of Group-Randomized Trials - Murray 2015 OBSSR Summer Institute/Design and Analysis of Group-Randomized Trials - Murray 2015 OBSSR Summer Institute.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Design and Analysis of Group-Randomized Trials - Murray 2015 OBSSR Summer Institute.pdf"
  notes: null
