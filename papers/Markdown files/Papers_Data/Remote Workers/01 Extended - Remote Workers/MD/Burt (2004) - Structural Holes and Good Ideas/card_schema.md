id: "burt-2022-structural-holes-and-good-ideas"
title: "Structural holes and good ideas"
authors:
  - "Burt, Ronald S."
year: 2022
doi: "10.4337/9781789909432.00030"
venue: {type: "book", name: "Handbook of Sociological Science", volume: null, issue: null, pages: "372-422"}
citation: "Burt (2022). Structural holes and good ideas. Handbook of Sociological Science, 372-422. https://doi.org/10.4337/9781789909432.00030"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Burt tests whether brokerage across structural holes provides a 'vision advantage' by
  studying 673 supply-chain managers at a large American electronics company, combining a
  network survey (name generators/interpreters) with company personnel records on salary,
  evaluations, and promotions. Managers whose discussion networks bridged disconnected
  groups (low network constraint) were paid more, evaluated more positively, promoted more
  often, and had their improvement ideas rated as more valuable, more likely to be expressed
  and discussed, and less likely to be dismissed than managers embedded in dense, closed
  cliques. Burt argues the mechanism is informational: brokers see a wider diversity of
  practice and opinion, giving them raw material for good ideas, but a follow-up check found
  brokers' ideas mostly circulated back to their same close contacts rather than diffusing
  across the organization, so brokerage did not reduce the underlying fragmentation.
claims:
  - text: "Idea value rated by two senior judges was strongly, negatively associated with a manager's network constraint (closed, dense network) net of rank, age, education, business unit, and location (b = -.694, SE = .144, on log network constraint; model R^2 = .15); managers with networks spanning structural holes produced ideas judged substantially more valuable."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure"]
  - text: "Network constraint predicted whether an idea was ever expressed and whether it was dismissed: managers in denser, more closed networks were far more likely to have no idea recorded at all (b = -2.356, SE = .243) and, among those who did offer an idea, more likely to have it dismissed by both judges (b = .972, SE = .281); overall 32% of ideas were dismissed and dismissal was concentrated among high-constraint managers (43% of the most-constrained tier vs. 14% of the least-constrained)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["communication", "performance"]
    predictors: ["network-structure"]
  - text: "Brokerage was rewarded organizationally: at senior manager and executive ranks, lower network constraint predicted significantly higher salary relative to peers (e.g., -$681 per point of constraint for executives, t = 5.5); the odds of a two-year 'outstanding' evaluation were roughly double for low-constraint managers (.32) versus high-constraint managers (.16); and the probability of promotion or an above-average raise was .68 for brokers versus .28 for managers confined to a dense clique."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "retention"]
    predictors: ["network-structure"]
population:
  who: "673 managers running the supply chain in 2001 for one of America's largest electronics companies; network-survey data available for 455 respondents (68% response), idea data drawn from those 455."
  where: ["United States"]
  when: "2001 (network survey), with salary/evaluation/promotion data spanning the six months before and after)"
  n: 673
  sector: ["private-sector", "electronics-manufacturing", "corporate-management"]
  sample_notes: >
    Single-firm convenience sample (one large electronics company's supply-chain function);
    68% completed the network survey, with a logit check showing respondents and
    nonrespondents differed only in that recently promoted managers were slightly more
    likely to respond; idea-value ratings came from just two senior-manager judges; 193
    supply-chain managers (29%) were social isolates never cited as a discussion partner.
limitation:
  primary: "Single-company, single-industry, largely cross-sectional design cannot establish that brokerage causes good ideas rather than reflecting reverse causation (able/valued managers get sought out as brokers) or unmeasured ability; Burt explicitly notes the association 'cannot be causal' from networks alone."
  others:
    - "Idea value was judged by only two senior managers using a 1-5 scale, an inherently subjective and organization-specific standard of 'good idea' (though Burt tests and rules out some rating biases)."
    - "Network constraint is computed only from each manager's immediate (one-step) discussion network, which Burt himself shows upwardly biases constraint scores relative to using the full network."
    - "Findings are specific to one bureaucratic, functionally-siloed supply-chain organization with unusually high baseline network constraint (mean ~68-81 points vs. ~28-49 in Burt's other manager samples), limiting generalizability."
risk_of_bias: "medium"
relevance_to_project: >
  A foundational empirical demonstration that a person's position in the informal
  communication network (bridging vs. closed/redundant ties) predicts whether their ideas
  get voiced, taken seriously, and rewarded — directly informing SNH's interest in how
  network structure and isolation shape engagement, help-seeking, and voice, and offering a
  concrete measure (network constraint) and outcome set (idea expression, idea dismissal,
  evaluation, promotion) that could be adapted to study remote-worker or open-source-
  maintainer social capital.
tags:
  topic: ["collaboration", "isolation", "productivity", "measurement"]
  method: ["survey", "cross-sectional", "secondary-data"]
  population: ["managers", "corporate", "us-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Burt (2004) - Structural Holes and Good Ideas/Burt (2004) - Structural Holes and Good Ideas.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Burt (2004) - Structural Holes and Good Ideas.pdf"
  notes: null
