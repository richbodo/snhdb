id: "karasek-1979-job-demands-job-decision-latitude-and"
title: "Job Demands, Job Decision Latitude, and Mental Strain: Implications for Job Redesign"
authors:
  - "Karasek, Robert A."
year: 1979
doi: "10.2307/2392498"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 24, issue: 2, pages: "285"}
citation: "Karasek (1979). Job Demands, Job Decision Latitude, and Mental Strain: Implications for Job Redesign. Administrative Science Quarterly, 24(2), 285. https://doi.org/10.2307/2392498"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Karasek develops and tests the job demand-control ("job strain") model using national
  survey data from the U.S. Quality of Employment Survey (1972) and the Swedish Level of
  Living Survey (1968, 1974). He finds it is the combination of low decision latitude and
  high job demands, not either factor alone, that predicts mental strain (exhaustion,
  depression), pill consumption, sick days, and job/life dissatisfaction, and that
  longitudinal Swedish data show symptom changes track changes in job strain over time. The
  paper's central policy implication is that redesigning work to increase workers' decision
  latitude can reduce strain without necessarily reducing organizational output.
claims:
  - text: "Workers with jobs combining high psychological job demands and low decision latitude ('high strain' jobs) showed the highest rates of exhaustion and depression in both countries; across deciles of job strain, depression prevalence ranged from 43% to 17% in the U.S. and 30% to 11% in Sweden, with standardized risk ratios up to 1.46 (p<.01)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["depression", "stress", "mental-health"]
    predictors: ["workload", "autonomy"]
  - text: "Job strain was strongly associated with job and life dissatisfaction: workers in the top job-strain decile reported roughly six times the severe dissatisfaction of workers in the bottom decile (interaction terms significant at p<.001), with a secondary dissatisfaction peak also found among 'passive' (low-demand, low-control) jobs."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress"]
    predictors: ["workload", "autonomy"]
  - text: "Using longitudinal Swedish panel data (1968-1974), increases in job strain (rising demands with declining decision latitude) were associated with increases in exhaustion and depression symptoms over the same period, and improvements in job strain were associated with symptom decline, supporting a causal rather than purely selection-based interpretation of the demand-control relationship."
    evidence: "longitudinal"
    support_strength: "low-to-moderate"
    outcomes: ["depression", "stress", "mental-health"]
    predictors: ["workload", "autonomy"]
population:
  who: "Employed male workers from two national surveys: the U.S. Quality of Employment Survey 1972 (ages 20-65) and the Swedish Level of Living Survey 1968 and 1974 (ages 18-66); analysis restricted to men only."
  where: ["United States", "Sweden"]
  when: "1968-1974"
  n: 1926
  sector: ["cross-industry"]
  sample_notes: >
    Two nationally representative surveys: U.S. stratified housing-unit sample (76% response
    rate, N approx. 911-950); Swedish random population sample (85-92% response rates, N
    approx. 1,896-1,926, longitudinal with re-interview in 1974). Analysis excludes women
    because the author judged that work-housework interaction complicated the model for
    female workers; this materially limits generalizability.
limitation:
  primary: "The analysis is restricted entirely to male workers, so the model's applicability to women (a stated but untested exclusion) is unknown."
  others:
    - "Job demands and decision latitude measures are broad composite scales that cannot distinguish specific types of demand or discretion (e.g., time pacing vs. skill use vs. policy influence)."
    - "The core test is cross-sectional; although a longitudinal Swedish subsample strengthens causal inference, most reported associations (U.S. data, Table 2/3) remain correlational and rely on self-reported symptoms."
    - "The model does not address social relations at the work-group or organizational level, only individual-level job content."
risk_of_bias: "medium"
relevance_to_project: >
  This is the foundational statement of the job demand-control (Karasek) model, which
  underlies how the SNH project should think about workload and autonomy as joint predictors
  of burnout, exhaustion, and dissatisfaction rather than as independent factors -- directly
  informing design choices around giving remote workers decision latitude/autonomy as a
  buffer against high-demand periods rather than only reducing workload itself.
tags:
  topic: ["burnout", "wellbeing", "job-satisfaction", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["male-workers", "cross-national"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Robert A. Karasek-JobDemandsJob-1979/Robert A. Karasek-JobDemandsJob-1979.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Robert A. Karasek-JobDemandsJob-1979.pdf"
  notes: null
