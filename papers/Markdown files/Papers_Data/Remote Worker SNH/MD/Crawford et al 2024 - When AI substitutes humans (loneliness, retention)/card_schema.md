id: "crawford-2024-when-artificial-intelligence-substitutes-humans-in"
title: "When artificial intelligence substitutes humans in higher education: the cost of loneliness, student success, and retention"
authors:
  - "Crawford, Joseph"
  - "Allen, Kelly-Ann"
  - "Pani, Bianca"
  - "Cowling, Michael"
year: 2024
doi: "10.1080/03075079.2024.2326956"
venue: {type: "journal", name: "Studies in Higher Education", volume: 49, issue: 5, pages: "883-897"}
citation: "Crawford et al. (2024). When artificial intelligence substitutes humans in higher education: the cost of loneliness, student success, and retention. Studies in Higher Education, 49(5), 883-897. https://doi.org/10.1080/03075079.2024.2326956"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  A structural equation modelling study of 387 university students finds that perceiving
  ChatGPT as a source of social support is associated with lower perceived social support
  from friends/family, greater loneliness, and (indirectly, via social support, wellbeing,
  and belonging) worse self-reported academic performance and higher intention to leave
  university. AI usage itself had no significant direct effect on grades or retention; the
  negative effects only emerged for students who felt socially supported by AI rather than
  by people. The authors interpret this as evidence of a human-to-AI 'substitution effect'
  with costs to student wellbeing, belonging, and persistence.
claims:
  - text: "In the best-fitting SEM model treating AI and human social support as independent constructs, greater perceived social support from AI was associated with lower perceived social support from other people, and AI usage itself was not a significant predictor of human social support (Model 2, CFI=.99, TLI=.99, RMSEA=.002)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["social-support"]
    predictors: ["ai-usage"]
  - text: "Social support from friends/family was associated with reduced loneliness, whereas students reporting greater AI-based social support reported higher loneliness; social support mediated the relationship between AI usage and loneliness."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support", "ai-usage"]
  - text: "AI usage had no significant direct effect on self-reported GPA or intention to leave university (Model 3, all paths p>.05), but showed a significant indirect effect: students who felt socially supported by AI (versus by other people) reported lower academic performance and greater intention to leave, mediated through social support, wellbeing, and sense of belonging."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["retention", "performance", "sense-of-belonging"]
    predictors: ["social-support"]
population:
  who: "University students (undergraduate, postgraduate, and doctoral), 18+, self-selected survey respondents"
  where: ["United Kingdom", "Australia", "United States", "Germany", "other countries (unspecified, 30.5%)"]
  when: "2023 (within ~9 months of ChatGPT's public release; single online survey wave, ~3-month recruitment window)"
  n: 387
  sector: ["higher-education"]
  sample_notes: >
    Convenience and geographic-stratified sampling via Qualtrics; target n=385 for a 95% CI
    assuming a 235M global student population. Of 512 who began, 5 excluded for non-consent,
    117 for <50% completion, 2 for ineligibility, leaving 387 (SE=2.55%). Sample skewed
    female (67.4%) and postgraduate (57.6%); AI-usage scale had only modest reliability
    (alpha=.60) due to self-reported short-text inputs requiring manual parsing.
limitation:
  primary: "Cross-sectional, single-timepoint self-report design cannot establish causal direction for the hypothesized AI-substitution effect, and the authors note belonging/loneliness fluctuate daily, meaning a one-time measure may not capture the true dynamics being modeled."
  others:
    - "Convenience/self-selected sampling with a female- and postgraduate-skewed sample limits generalizability across student populations."
    - "The AI-usage measure (self-reported conversation counts, replies, and duration) had only modest internal reliability (alpha=.60) and required manual text parsing."
    - "Data were collected within the first nine months of ChatGPT's public availability, so findings may not generalize to more mature AI tools or longer-term usage patterns."
risk_of_bias: "medium"
relevance_to_project: >
  This is a direct empirical test of the 'AI as human-support substitute' mechanism central
  to SNH's concern about AI companion/chatbot tools: it operationalizes a parallel AI-
  social-support construct alongside validated human social-support, loneliness, belonging,
  and retention measures, and finds a measurable trade-off (more AI-perceived support tracks
  with less human-perceived support and more loneliness), informing how SNH should evaluate
  AI-mediated support tools for isolated remote workers rather than assuming AI support is a
  neutral or additive substitute for human connection.
tags:
  topic: ["loneliness", "social-support", "wellbeing", "measurement", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["university-students", "higher-education"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Crawford et al 2024 - When AI substitutes humans (loneliness, retention)/Crawford et al 2024 - When AI substitutes humans (loneliness, retention).md"
  pdf: "papers/Remote Worker SNH/Crawford et al 2024 - When AI substitutes humans (loneliness, retention).pdf"
  notes: null
