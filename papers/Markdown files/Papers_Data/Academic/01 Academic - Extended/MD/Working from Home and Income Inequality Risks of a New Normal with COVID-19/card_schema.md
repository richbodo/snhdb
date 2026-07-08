id: "bonacini-2021-working-from-home-and-income-inequality"
title: "Working from home and income inequality: risks of a ‘new normal’ with COVID-19"
authors:
  - "Bonacini, Luca"
  - "Gallo, Giovanni"
  - "Scicchitano, Sergio"
year: 2021
doi: "10.1007/s00148-020-00800-7"
venue: {type: "journal", name: "Journal of Population Economics", volume: 34, issue: 1, pages: "303-360"}
citation: "Bonacini et al. (2021). Working from home and income inequality: risks of a ‘new normal’ with COVID-19. Journal of Population Economics, 34(1), 303-360. https://doi.org/10.1007/s00148-020-00800-7"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using unconditional quantile (RIF) regression on a merged Italian dataset (INAPP-PLUS 2018
  labour survey and the 2013 Italian Survey of Professions), this study estimates how a
  persistent, COVID-19-driven increase in work-from-home (WFH) feasibility would reshape the
  distribution of labour income. Swapping 10 percentage points of employees from low to high
  WFH feasibility raises mean annual income by about EUR 259 (1%) and widens the Gini index
  by about 0.004, with the wage premium concentrated among male, older, and highly-educated
  employees and largest in provinces hardest hit by COVID-19 infection. The paper argues
  that expanding remote work without regulation and compensating policy (income support,
  childcare, human-capital investment) risks deepening existing labour-market inequalities
  rather than being a socially neutral 'new normal.'
claims:
  - text: "A 10-percentage-point shift of employees from low to high WFH feasibility is associated with a mean labour income increase of about EUR 259 (about 1%) and a Gini index increase of about 0.004 (unconditional effect, p<0.05); effects shrink but remain significant on inequality once demographic/job covariates are controlled (unconditional partial effect)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity"]
  - text: "The wage premium from higher WFH feasibility is highly unequal: it is much larger for male employees (+EUR 473 UE, +EUR 234 UPE) than female (+EUR 111 UE, near-zero/negative UPE), and larger for older (51-64, +EUR 496 UE) and graduated employees (+EUR 411 UE) than for younger/non-graduated employees, with the highest premium (~EUR 500, +1.7%) at the 8th income decile."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity"]
  - text: "Employees in Italian provinces with above-median COVID-19 infection incidence would benefit more from increased WFH feasibility than those in less-infected provinces (mean income effect +EUR 330 vs +EUR 193 unconditional; +EUR 137 vs +EUR 47 with covariates), and an inverse-probability-weighting robustness check confirms high WFH feasibility raises mean income by 3.5% overall, rising to 16.3% at the top decile."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "Italian employees aged 25-64 (self-employed excluded) drawn from the 2018 INAPP-PLUS labour survey merged with occupation-level WFH feasibility scores from the 2013 Italian Survey of Professions (ICP)"
  where: ["Italy"]
  when: "2018 (INAPP-PLUS survey wave); WFH feasibility index from 2013 ICP survey; COVID-19 infection data 24 Feb-5 May 2020"
  n: 14307
  sector: ["other"]
  sample_notes: >
    INAPP-PLUS is a stratified random CATI survey of ~45,000 working-age Italians per wave;
    analysis sample restricted to employed, non-self-employed individuals aged 25-64 with no
    missing values (14,307 of 45,000). Findings are specific to pre-pandemic Italian labour-
    market structure and a hypothetical 'employee-shares swap' counterfactual, not observed
    post-pandemic outcomes; robustness checks (self-employed included, different thresholds,
    unweighted, IPW) confirm main results.
limitation:
  primary: "The core analysis is a counterfactual simulation (hypothetical swap of shares of employees between WFH feasibility levels using pre-pandemic 2018/2013 data), not a measurement of actual post-pandemic WFH adoption or its realized income effects."
  others:
    - "WFH feasibility is an occupation-level task index (whether a job COULD be done remotely), not actual remote-work status or intensity of individual employees, so it is a proxy rather than a direct measure of remote work."
    - "Findings are specific to the Italian labour market and regulatory context (very low pre-pandemic telework prevalence, ~1%) and may not generalize to countries with different WFH norms or labour institutions."
    - "Analysis excludes self-employed workers and is limited to formally employed workers aged 25-64, omitting groups (students, informal workers, gig workers) that may face different WFH-inequality dynamics."
risk_of_bias: "low"
relevance_to_project: >
  Provides quantitative evidence that expanding remote-work feasibility is not
  distributionally neutral: it systematically advantages male, older, more educated, and
  already higher-paid workers, which is directly relevant to SNH's interest in how
  remote/hybrid work policy can inadvertently widen inequality alongside its social-
  connection effects, and supports the case for pairing remote-work expansion with
  compensating supports (childcare, training) rather than treating WFH access as an
  unambiguous wellbeing win.
tags:
  topic: ["remote-work", "wellbeing"]
  method: ["cross-sectional", "secondary-data"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Working from Home and Income Inequality Risks of a New Normal with COVID-19/Working from Home and Income Inequality Risks of a New Normal with COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Working from Home and Income Inequality Risks of a New Normal with COVID-19.pdf"
  notes: null
