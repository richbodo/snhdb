id: "hansen-1999-the-search-transfer-problem-the-role"
title: "The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge across Organization Subunits"
authors:
  - "Hansen, Morten T."
year: 1999
doi: "10.2307/2667032"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 44, issue: 1, pages: "82-111"}
citation: "Hansen (1999). The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge across Organization Subunits. Administrative Science Quarterly, 44(1), 82-111. https://doi.org/10.2307/2667032"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Studying 120 new-product development projects across 41 divisions of a large electronics
  company, Hansen shows that weak interunit ties help project teams search for useful
  knowledge elsewhere in the organization but impede the transfer of that knowledge once
  found, especially when it is complex (noncodified and interdependent). Weak ties speed up
  project completion when the knowledge to be moved is simple and codified, but slow
  projects down when the knowledge is highly noncodified and dependent on other components,
  because transfer of complex knowledge requires the frequent, two-way interaction
  characteristic of strong ties. The paper resolves a discrepancy between weak-tie network
  theory and product-innovation research on tight coupling by showing both are right under
  different knowledge-complexity conditions.
claims:
  - text: "Tie weakness has a significant positive effect on project completion rate when knowledge to be transferred is highly codified and independent (main effect of tie weakness = 1.329, p < .01), supporting Hypothesis 1 that weak interunit ties speed up projects transferring simple knowledge."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "sampling-method"]
  - text: "Tie weakness interacts negatively with knowledge complexity: the noncodified x weakness interaction (-0.343, p<.10) and dependent x weakness interaction (-0.193, p<.10) show that as knowledge becomes more noncodified and interdependent, the benefit of weak ties dampens and turns negative, supporting Hypothesis 2 that weak ties slow completion when complex knowledge must be transferred."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure"]
  - text: "The positive effect of weak ties on completion time persisted after controlling for two direct measures of network redundancy (structural equivalence, proportion density) and for reciprocity, indicating weak ties are beneficial primarily because they are cheaper to maintain (lower search costs) rather than because they simply provide access to nonredundant contacts."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "performance"]
    predictors: ["network-structure", "social-support"]
population:
  who: "Project managers and R&D managers for 120 new-product development projects (54 with a cross-division knowledge transfer event analyzed in the main model) across 41 operating divisions of one large multinational electronics and computing company"
  where: ["United States", "Europe", "Asia", "Australia"]
  when: "1993-1995 (network data lagged one year prior to each project's start)"
  n: 120
  sector: ["technology", "manufacturing"]
  sample_notes: >
    Single-company field study; 100% response from 41 R&D managers on the network survey and
    85% response (120 of 147 projects) from project managers; main hazard-rate analysis
    restricted to the 54 projects that reported an interdivisional transfer event, with a
    separate check on the 66 that did not; author notes the firm studied is likely more
    densely networked than typical multiunit firms, which he argues biases results
    conservatively.
limitation:
  primary: "Findings are confined to a single company studied over a short window, and generalizability to less densely networked or non-electronics firms is untested."
  others:
    - "Outcome measure is limited to project completion time; effects on cost, quality, or degree of innovation were not directly assessed."
    - "Study captures only formal/regular interdivisional (group-level) ties, not personal cross-unit relationships or other channels (databases, e-mail, headquarters intervention) that project teams may also have used to find and move knowledge."
    - "Knowledge complexity ratings came solely from the project manager, so inter-rater reliability of the noncodified/dependent knowledge measures could not be tested."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational network-structure paper for the SNH project's core design tension:
  it gives quantitative evidence that weak ties (low-frequency, low-closeness relationships)
  are not uniformly good for collaboration/knowledge-sharing outcomes, and that the right
  network structure depends on task complexity — directly informing decisions about when a
  remote/distributed team should invest in cultivating strong-tie relationships (for
  complex, tacit knowledge transfer) versus rely on lighter-touch weak-tie connectors (for
  simple information search), a distinction relevant to designing onboarding, mentoring, and
  cross-team bridging mechanisms in remote and open-source communities.
tags:
  topic: ["remote-work", "collaboration", "community-health", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "organizations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits.pdf"
  notes: null
