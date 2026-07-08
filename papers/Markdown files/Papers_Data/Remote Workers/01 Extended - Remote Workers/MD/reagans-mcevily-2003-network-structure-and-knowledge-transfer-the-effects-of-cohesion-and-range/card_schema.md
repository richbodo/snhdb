id: "reagans-2003-network-structure-and-knowledge-transfer-the"
title: "Network Structure and Knowledge Transfer: The Effects of Cohesion and Range"
authors:
  - "Reagans, Ray"
  - "McEvily, Bill"
year: 2003
doi: "10.2307/3556658"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 48, issue: 2, pages: "240-267"}
citation: "Reagans et al. (2003). Network Structure and Knowledge Transfer: The Effects of Cohesion and Range. Administrative Science Quarterly, 48(2), 240-267. https://doi.org/10.2307/3556658"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using dyadic survey and network data from 102 employees (1,330 dyads) at a contract R&D
  firm, this study shows that social cohesion (dense third-party ties around a relationship)
  and network range (ties spanning distinct expertise areas) each ease knowledge transfer
  above and beyond the effect of tie strength alone. The findings decouple tie strength from
  network structure, showing cohesion and range make independent, complementary
  contributions rather than the benefits of one coming at the expense of the other, and that
  both effects are nonlinear (diminishing returns beyond a point).
claims:
  - text: "Social cohesion (network density, indirect structural constraint) had a significant positive effect on ease of knowledge transfer even after controlling for tie strength, friendship, and advice-seeking (model 6 coefficient 6.3, p<.01; effect held with fixed effects for individuals)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Network range (diversity of ties across expertise areas) independently increased ease of knowledge transfer (model 7 coefficient .74, p<.05), and this range effect did not vary with knowledge codifiability, contradicting the assumption that boundary-spanning ties matter only for simple/codified knowledge."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure"]
  - text: "Tie strength positively predicted ease of transfer (model 4, p<.01), but its apparent interaction with knowledge tacitness weakened and effectively disappeared once network density and range were added to the model, indicating that prior findings attributing tacit-knowledge transfer benefits to strong ties were partly capturing network structure effects (tie strength and density correlated r=.38)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "social-support"]
population:
  who: "102 employees (scientists, engineers, and staff, mostly holding master's/doctoral degrees) at a 113-person contract R&D materials-science consulting firm in the American Midwest"
  where: ["United States"]
  when: null
  n: 102
  sector: ["private-sector-rd", "engineering-consulting"]
  sample_notes: >
    Onsite survey with 92% response rate (104/113 employees), 84% full completion; network
    data combined sociometric (fixed roster) and egocentric (free recall) name-generator
    techniques; final analytic sample was 1,330 non-independent dyads from 102 respondents
    after excluding missing data, analyzed with individual fixed effects to address network
    autocorrelation.
limitation:
  primary: "Single-firm, single-industry (R&D consulting) cross-sectional design limits generalizability, and although network measures used multi-respondent data to reduce single-source bias, the dependent variable (ease of transfer) and some predictors came from the same survey respondent."
  others:
    - "Cannot fully rule out that the network diversity effect reflects unmeasured individual absorptive capacity rather than network-structure-induced framing/perspective-taking behavior, though individual fixed effects and knowledge-breadth controls partially address this."
    - "Measures 'ease of transfer' as perceived by the knowledge source only, not actual transfer outcomes or recipient-reported ease."
    - "Data are from 2003 (pre-digital-collaboration-tools era) in a co-located, in-person work setting, limiting direct applicability to distributed/remote work network structures."
risk_of_bias: "low"
relevance_to_project: >
  Provides a validated, quantitative distinction between tie strength, social cohesion, and
  network range as separate levers for easing knowledge/help transfer among colleagues --
  directly informs how the SNH project might design or measure network structure
  interventions (e.g., encouraging cross-team/cross-community ties) rather than only
  strengthening individual dyadic relationships to improve collaboration and reduce
  isolation.
tags:
  topic: ["collaboration", "community-health", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "engineers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range.pdf"
  notes: null
