id: "dingel-2020-how-many-jobs-can-be-done"
title: "How Many Jobs Can be Done at Home?"
authors:
  - "Dingel, Jonathan"
  - "Neiman, Brent"
year: 2020
doi: "10.3386/w26948"
venue: {type: "report", name: null, volume: null, issue: null, pages: null}
citation: "Dingel et al. (2020). How Many Jobs Can be Done at Home?.. https://doi.org/10.3386/w26948"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Dingel and Neiman classify nearly 1,000 US occupations as feasible or infeasible to
  perform entirely from home using O*NET Work Context and Generalized Work Activities survey
  items (e.g., outdoor work, physical activity, public-facing tasks), then merge this
  classification with BLS employment and wage data and, for 85 other countries, ILO
  employment data. They find 37% of US jobs (46% of wages) can be done entirely at home,
  that this share rises steeply with a country's per-capita income, and that within the US
  it correlates strongly with metro-area education and income levels. The paper supplies the
  widely-used structural measure of "who can work remotely at all," as distinct from who
  actually does.
claims:
  - text: "37% of jobs in the United States can be performed entirely at home, accounting for 46% of all US wages, with sharp variation by occupation (near 100% for computer/math and legal occupations, near 0% for construction, food service, and production occupations)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Applying the classification to 85 other countries via ILO employment data shows lower-income economies have a far lower share of feasible work-from-home jobs; countries with per-capita GDP below one-third of the US level have roughly half as many WFH-feasible jobs (e.g., under 25% in Mexico and Turkey vs. over 40% in Sweden and the UK)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["remote-work-intensity"]
    predictors: ["remote-work-intensity"]
  - text: "Across the 100 largest US metropolitan areas, the share of jobs that can be done at home is strongly positively correlated with median household income (r=0.53) and share of residents with a college degree (r=0.71), and negatively correlated with homeownership rate (r=-0.31) and share of residents who are white (r=-0.12)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["remote-work-intensity"]
    predictors: ["remote-work-intensity", "sampling-method"]
population:
  who: "Nearly 1,000 US occupational categories (SOC codes) classified via O*NET survey responses (median ~25-26 respondents per question per occupation), merged with BLS 2018 Occupational Employment Statistics; classification then applied to occupational employment counts in 85 additional countries via ILO data."
  where: ["United States", "85 other countries (via ILO/ISCO mapping)"]
  when: "O*NET release 24.2; BLS 2018 Occupational Employment Statistics; ILO employment data for 2015 or later; analysis conducted mid-2020"
  n: null
  sector: []
  sample_notes: >
    Not a survey of individual workers; it is an occupation-level classification covering
    essentially the full US labor force by SOC code, cross-walked to 2-digit ISCO codes for
    international comparison. Authors validate the O*NET-derived classification against an
    independent manual assignment (85% agreement). Classification is estimated using US
    task/context data and extrapolated to other countries without adjusting for how
    occupations differ in content across economies.
limitation:
  primary: "The occupational feasibility classification is built entirely from US O*NET data and then mechanically applied to other countries, ignoring that the same occupation title may involve different tasks, technology, and infrastructure access across economies with different income levels."
  others:
    - "Measures theoretical/structural feasibility (an upper bound), not actual remote-work behavior; the paper itself notes far fewer workers report actually working entirely from home than the classification implies."
    - "Binary rule-based classification can misclassify specific occupations (e.g., 98% of teachers coded as WFH-feasible despite the practical difficulty of remote teaching)."
risk_of_bias: "low"
relevance_to_project: >
  Provides the standard structural measure of which occupations/sectors are even capable of
  remote work, letting the SNH project frame remote-work findings by feasibility and
  stratify by socioeconomic access (higher-income, higher-education occupations and metro
  areas have much greater WFH feasibility), which matters for interpreting who is exposed to
  remote-work-related isolation or connection effects versus who is structurally excluded
  from remote work.
tags:
  topic: ["remote-work", "measurement", "methodology"]
  method: ["secondary-data", "cross-sectional"]
  population: ["general-workforce", "cross-national"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home.pdf"
  notes: null
