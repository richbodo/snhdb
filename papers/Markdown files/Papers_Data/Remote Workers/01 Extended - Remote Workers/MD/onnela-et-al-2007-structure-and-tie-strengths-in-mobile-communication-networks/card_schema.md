id: "onnela-2007-structure-and-tie-strengths-in-mobile"
title: "Structure and tie strengths in mobile communication networks"
authors:
  - "Onnela, J.-P."
  - "Saramäki, J."
  - "Hyvönen, J."
  - "Szabó, G."
  - "Lazer, D."
  - "Kaski, K."
  - "Kertész, J."
  - "Barabási, A.-L."
year: 2007
doi: "10.1073/pnas.0610245104"
venue: {type: "journal", name: "Proceedings of the National Academy of Sciences", volume: 104, issue: 18, pages: "7332-7336"}
citation: "Onnela et al. (2007). Structure and tie strengths in mobile communication networks. Proceedings of the National Academy of Sciences, 104(18), 7332-7336. https://doi.org/10.1073/pnas.0610245104"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  Analyzing 18 weeks of anonymized mobile-phone call records covering roughly 20% of an
  entire country's population (4.6 million people, 7.0 million reciprocated-call ties), the
  authors show that tie strength (aggregate call duration) is systematically coupled to
  local network structure: strong ties sit inside tightly-knit communities and weak ties
  bridge between them, confirming Granovetter's strength-of-weak-ties hypothesis at societal
  scale. They further show this coupling makes the network robust to losing its strongest
  ties but catastrophically fragile to losing its weakest ones, and that it slows
  information diffusion by dynamically trapping news inside communities rather than letting
  it flow globally.
claims:
  - text: "Topological overlap (share of mutual friends) increases with tie strength for approximately 95% of links, meaning strong ties cluster within communities and weak ties disproportionately form the bridges connecting distinct communities — the first society-level empirical confirmation of the strength-of-weak-ties hypothesis."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["communication", "social-presence"]
    predictors: ["network-structure"]
  - text: "Removing the weakest ties (by strength or by overlap) causes the giant component to disintegrate via a phase transition at a critical fraction f_c ≈ 0.80 (weight-based) or 0.62 (overlap-based) of links removed, whereas removing the strongest ties first only produces gradual shrinkage with no collapse — the opposite of the pattern typically seen for hubs in technological/biological networks."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["network-resilience"]
    predictors: ["network-structure"]
  - text: "In diffusion simulations, information spread significantly faster through a control network with all tie strengths set equal than through the real weighted network, where it instead became dynamically trapped inside communities (rapid local spread followed by plateaus); most individuals first received novel information via intermediate-strength ties, indicating both very weak and very strong ties are comparatively ineffective conduits for new information."
    evidence: "modelling"
    support_strength: "moderate"
    outcomes: ["communication"]
    predictors: ["network-structure"]
population:
  who: "Subscribers of a single national mobile-phone operator, reconstructed into an undirected call graph (link = at least one reciprocated pair of calls) covering an estimated 20% of the country's entire population, of whom about 90% held a mobile subscription; giant component includes 84.1% of the 4.6 million nodes."
  where: []
  when: "18-week window of call-detail records (exact calendar dates and country not disclosed in the article, published 2007)"
  n: 4600000
  sector: ["general-population"]
  sample_notes: >
    The country is not named (likely withheld for confidentiality with the telecom partner);
    results were checked for saturation against two- and three-month subsamples with little
    difference. Only reciprocated call pairs are counted as ties, which the authors argue
    filters out one-off/unknown-caller contacts but also excludes one-directional or non-
    mutual relationships and all non-phone communication channels (email, face-to-face,
    landline).
limitation:
  primary: "The network is built purely from mobile call-duration data from one operator in one undisclosed country, so it may not capture the full structure of participants' social ties (email, in-person, landline contact are all excluded) and generalizability to other countries, time periods, or communication modes is untested."
  others:
    - "Tie strength is operationalized solely as aggregated call duration, collapsing structurally different relationship types (family, romantic, work, service) into a single scalar measure."
    - "The information-diffusion results come from a simplified simulation (transmission probability proportional to call duration) rather than observed real-world diffusion of an actual message."
    - "As an observational, non-experimental network analysis, the study establishes structural correlation between tie strength and topology, not causal mechanisms."
risk_of_bias: "low"
relevance_to_project: >
  Provides the foundational, population-scale evidentiary basis for treating tie strength
  and network position (weak bridging ties vs. strong within-community ties) as distinct
  structural resources with different functions — directly informing how SNH work should
  model and measure social-support networks, weak-tie/bridge relationships, and community
  structure rather than treating 'connection' as a single undifferentiated quantity.
tags:
  topic: ["community-health", "social-support", "measurement", "methodology"]
  method: ["secondary-data", "modelling"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks.pdf"
  notes: null
