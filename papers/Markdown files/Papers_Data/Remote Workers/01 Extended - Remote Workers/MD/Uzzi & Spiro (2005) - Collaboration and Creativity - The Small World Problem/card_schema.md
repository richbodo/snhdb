id: "mutzel-2019-uzzi-spiro-2005-collaboration-and-creativity"
title: "Uzzi/Spiro (2005): Collaboration and Creativity: The Small World Problem"
authors:
  - "Mützel, Sophie"
year: 2019
doi: "10.1007/978-3-658-21742-6_127"
venue: {type: "book", name: "Netzwerkforschung", volume: null, issue: null, pages: "539-541"}
citation: "Mützel (2019). Uzzi/Spiro (2005): Collaboration and Creativity: The Small World Problem. Netzwerkforschung, 539-541. https://doi.org/10.1007/978-3-658-21742-6_127"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Analyzing the complete network of artists who created Broadway musicals from 1945 to 1989,
  the authors show that a team's embeddedness in a 'small world' network (high clustering
  plus short path length, summarized as a small-world quotient Q) has a curvilinear,
  inverted-U relationship with both the financial and artistic success of the shows its
  members produce. Moderate connectivity and cohesion among collaborators lets novel
  material circulate with enough trust to be used, but past a threshold the same
  connectivity homogenizes the pool of ideas and rewards conventional over fresh material,
  so both under- and over-connected creative networks underperform relative to an
  intermediate 'bliss point.'
claims:
  - text: "The relationship between network small-worldliness (Q) and a musical's financial success is an inverted U: at the estimated optimum (Q about 2.6) the probability of a hit is about 2.5 times greater than at the lowest observed Q (about 1.4), and the probability of a flop drops by about 20%; both the linear and squared Q terms are significant in ordered probit models (p<.05) controlling for production size, theater location, economic conditions, and team network position."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Artistic success (average critics' reviews) shows the same curvilinear pattern: shows are about 3 times more likely to be an artistic success at the bliss point (Q about 2.3) than at the lowest level of Q, and season-level measures (percentage of hits, percentage of rave reviews, average critics' score) also peak at intermediate Q, with the linear Q term positive and the squared term negative (p<.05) across all models."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "The penalty for too little connectivity/cohesion is larger than the penalty for too much: about 80-85% of the season-years fall to the left of the performance-maximizing bliss point, indicating underconnected small-world structure is the more common and more costly condition; team-level network variables (closeness centrality, structural holes) added about 12 percentage points of explained variance (R2) beyond economic and talent controls in the financial-success model."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
population:
  who: "All 2,092 freelance creative artists (composers, lyricists, librettists, choreographers, directors, producers) who worked on Broadway musicals, including 49 shows that died in preproduction"
  where: ["United States (Broadway, New York City)"]
  when: "1945-1989"
  n: 2092
  sector: ["creative-industries"]
  sample_notes: >
    Population data (not a sample) reconstructed from archival Playbill-derived directories
    (Bloom 1996; Green 1996; Simas 1987) covering 474 new musicals; complete financial-
    outcome data for 442 shows, critics'-review data for only 315-321 shows because
    systematic review scoring (Suskin 1990, 1997) is unavailable for 1982-1989, shrinking
    the artistic-success sample.
limitation:
  primary: "Entirely observational archival network data from a single industry (Broadway musical theater, 1945-1989) with no experimental manipulation of network structure, so the causal interpretation of the small-world/performance relationship rests on statistical controls rather than random assignment."
  others:
    - "Findings generalize a specific bipartite-team production context; the authors explicitly flag as open questions whether the same curvilinear pattern holds for other team-based domains (R&D labs, project teams, boards, science coauthorship) that the SNH project cares about."
    - "Network position (structural holes, repeated ties, small-world Q) is used as a proxy for the actual flow of creative material/information between teams, which is never directly observed or measured."
    - "Critics'-review data are unavailable after 1981, cutting the artistic-success sample roughly in half and limiting later-period inference."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a quantitative, transferable framework (the small-world quotient Q, balancing
  connectivity and cohesion) showing that team/community network structure has a curvilinear
  rather than 'more is always better' relationship with collaborative performance --
  directly informs how the SNH project might think about optimal levels of connectivity and
  cohesion in remote or open-source teams rather than simply maximizing ties or closeness.
tags:
  topic: ["collaboration", "productivity", "community-health", "methodology"]
  method: ["longitudinal", "secondary-data"]
  population: ["creative-industries", "teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem.pdf"
  notes: null
