id: "demerouti-2001-the-job-demands-resources-model-of"
title: "The job demands-resources model of burnout."
authors:
  - "Demerouti, Evangelia"
  - "Bakker, Arnold B."
  - "Nachreiner, Friedhelm"
  - "Schaufeli, Wilmar B."
year: 2001
doi: "10.1037/0021-9010.86.3.499"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 86, issue: 3, pages: "499-512"}
citation: "Demerouti et al. (2001). The job demands-resources model of burnout.. Journal of Applied Psychology, 86(3), 499-512. https://doi.org/10.1037/0021-9010.86.3.499"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This foundational study tests the job demands-resources (JD-R) model of burnout across 374
  employees in 21 job positions spanning human services (teachers, nurses), industry
  (assembly-line workers), and transport (air traffic controllers). Using both self-reports
  and independent observer ratings of working conditions, it finds that job demands predict
  exhaustion while job resources predict disengagement, and validates the two-factor
  Oldenburg Burnout Inventory (OLBI) as invariant across occupations, extending burnout
  research beyond the human services. The paper's core theoretical move is separating
  exhaustion (driven by workload) from disengagement (driven by resource scarcity) as
  distinct pathways rather than a single burnout continuum.
claims:
  - text: "Job demands were strongly and positively related to exhaustion (self-report gamma = .91, p < .05) but not to disengagement (gamma = .07, ns), while job resources were strongly and negatively related to disengagement (gamma = -.72, p < .05) but not to exhaustion (gamma = .04, ns); the model explained 82% of variance in exhaustion and 52% in disengagement."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["workload", "social-support", "autonomy"]
  - text: "Observer ratings of job conditions (independent of employee self-reports) replicated the same pattern: job demands to exhaustion and job resources to disengagement were both significant and in the predicted direction, and models restricted to only these two paths fit the data as well as more complex alternatives, arguing against pure common-method bias."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout"]
    predictors: ["workload", "social-support"]
  - text: "Confirmatory factor analyses showed the two-factor structure of the Oldenburg Burnout Inventory (exhaustion and disengagement, r = .39 between factors) was invariant (equal factor loadings) across human service, transport, and industry occupational groups (total N = 352), supporting burnout as a construct that generalizes beyond human-service work."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout"]
    predictors: ["workload", "sampling-method"]
population:
  who: "374 employees across 21 job positions in northern Germany: teachers and nurses (human services), assembly-line/production and control-room workers (industry), and air traffic controllers (transport)"
  where: ["Germany"]
  when: null
  n: 374
  sector: ["healthcare", "manufacturing", "transportation", "education"]
  sample_notes: >
    Recruited via 12 organizations after informational meetings; 56% questionnaire response
    rate (54-62% across subsamples); not randomly sampled from the universe of jobs, but
    deliberately heterogeneous across occupation types; a subset of 21 job prototypes was
    independently rated by trained observers (interrater reliabilities .87-.96) to cross-
    validate self-report findings.
limitation:
  primary: "Cross-sectional design means the demands-to-exhaustion and resources-to-disengagement relationships cannot be interpreted causally; the authors explicitly call for longitudinal and quasi-experimental designs to confirm the causal structure."
  others:
    - "Non-random, convenience sampling of organizations and job positions limits generalizability, though heterogeneity across occupation types partly offsets this."
    - "Self-report and observer-rating scales for individual working conditions used only 1-3 items each, limiting internal-consistency reliability of specific job-demand/resource measures."
    - "Observer-rating analyses used the job (N=21) rather than individual as the unit of analysis, which is underpowered for structural equation modeling and the authors flag results as exploratory/indicative only."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational burnout-mechanism paper for the SNH project: it gives a validated,
  parsimonious causal model (workload/demands -> exhaustion; lack of social/organizational
  resources -> disengagement) that can structure how the project separates 'overwork'
  burnout from 'disconnection/cynicism' burnout in remote and open-source contexts, and
  supports treating supervisor support and job control as protective resources distinct from
  workload reduction.
tags:
  topic: ["burnout", "wellbeing", "measurement", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["healthcare-workers", "manufacturing-workers", "mixed-occupations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout.pdf"
  notes: null
