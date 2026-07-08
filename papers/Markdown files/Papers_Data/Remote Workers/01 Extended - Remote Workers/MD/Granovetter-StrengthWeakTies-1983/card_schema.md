id: "granovetter-1983-the-strength-of-weak-ties-a"
title: "The Strength of Weak Ties: A Network Theory Revisited"
authors:
  - "Granovetter, Mark"
year: 1983
doi: "10.2307/202051"
venue: {type: "journal", name: "Sociological Theory", volume: 1, issue: null, pages: "201"}
citation: "Granovetter (1983). The Strength of Weak Ties: A Network Theory Revisited. Sociological Theory, 1, 201. https://doi.org/10.2307/202051"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Granovetter revisits his 1973 'Strength of Weak Ties' (SWT) thesis by synthesizing roughly
  a decade of empirical and theoretical follow-up work, arguing the evidence broadly
  supports the core claim that weak ties (not strong ones) disproportionately act as bridges
  linking otherwise disconnected clusters, and that this bridging role drives information
  diffusion, job mobility, and integration of large, differentiated social systems. He also
  elaborates an 'excursus on the strength of strong ties,' showing strong ties dominate
  under conditions of economic insecurity, urgent need, or low socioeconomic status, while
  weak ties matter most for reaching novel information and connecting socially distant
  groups. The paper closes by noting the verification evidence is encouraging but
  incomplete, partly because it is not from a systematic or unbiased sample of studies.
claims:
  - text: "Friedkin's (1980) survey of 97 biology faculty found all 11 identified 'local bridges' in the network were weak ties, even though only 69% of all ties were weak (binomial test p=0.017); interdepartmental (intergroup) ties were weak 77% of the time versus 65% for intradepartmental ties (p=0.002), directly confirming SWT's bridging prediction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["communication"]
    predictors: ["network-structure"]
  - text: "Lin, Ensel, and Vaughn (1981) found weak ties raised occupational status attainment mainly indirectly, through the status of the contact reached: 76.2% of weak ties used for a first job connected respondents to high-status informants versus only 28.9% of strong ties (70.7% vs. 42.9% for current job), so weak ties' advantage depended on whom they connected to, not tie strength alone."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["occupational-attainment"]
    predictors: ["network-structure", "social-support"]
  - text: "Ericksen and Yancey's (1980) regression on a Philadelphia probability sample (n=1,780) found weak ties used for job-finding had a significant negative net effect on income overall, but a significant weak-tie x education interaction reversed this: weak ties reduced income among the poorly educated but the effect grew progressively more positive with more education."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["income"]
    predictors: ["network-structure", "social-support"]
population:
  who: "Not a single primary sample: a narrative synthesis of ~15 independent empirical and theoretical studies (job seekers, university faculty, kibbutz members, corporate directors, school peer groups, hospital staff, protest-group recruits, ghetto and shantytown residents) used to test or extend the 1973 weak-ties hypothesis."
  where: ["USA", "Canada", "Israel", "Germany"]
  when: "1962-1981 (data collection periods of the cited studies)"
  n: null
  sector: ["academia", "corporate", "healthcare", "community", "education"]
  sample_notes: >
    Studies were located mainly through personal contact with authors or their citation of
    Granovetter's original SWT paper -- a non-random, confirmation-prone sampling procedure
    that the author himself flags as a threat to unbiased verification of the theory.
limitation:
  primary: "The review's evidence base was assembled through citation tracing and personal contacts rather than systematic search, so studies where the weak-ties hypothesis was considered and rejected are structurally underrepresented, biasing the synthesis toward confirmation."
  others:
    - "Several cited studies (Coser, Boorman, Fine and Kleinman, Chubin, Karweit et al.) are purely theoretical and contribute no new empirical data."
    - "Operational definitions of 'weak' vs. 'strong' tie differ substantially across the cited studies (frequency of contact, mutual vs. one-sided reporting, kin/friend/acquaintance categories), limiting direct comparability."
    - "All cited studies are cross-sectional or static network snapshots; Granovetter explicitly calls for dynamic, longitudinal study of how bridging ties form and change over time."
risk_of_bias: "high"
relevance_to_project: >
  This is the canonical statement and empirical stress-test of the weak-ties/bridging
  mechanism that underlies SNH's interest in cross-group information flow, integration, and
  belonging: it gives a concrete evidence basis for designing remote/OSS communities with
  enough loosely-connected 'bridging' contacts across teams (to prevent fragmentation and
  speed information/idea diffusion) while recognizing strong ties remain the primary channel
  for support under stress, job insecurity, or economic precarity -- a distinction directly
  relevant to when to design for weak-tie breadth versus strong-tie support depth.
tags:
  topic: ["community-health", "collaboration", "social-support", "methodology"]
  method: ["review-narrative", "cross-sectional"]
  population: ["academia", "corporate", "community"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Granovetter-StrengthWeakTies-1983/Granovetter-StrengthWeakTies-1983.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Granovetter-StrengthWeakTies-1983.pdf"
  notes: null
