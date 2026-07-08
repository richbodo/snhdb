id: "levin-2004-the-strength-of-weak-ties-you"
title: "The Strength of Weak Ties You Can Trust: The Mediating Role of Trust in Effective Knowledge Transfer"
authors:
  - "Levin, Daniel Z."
  - "Cross, Rob"
year: 2004
doi: "10.1287/mnsc.1030.0136"
venue: {type: "journal", name: "Management Science", volume: 50, issue: 11, pages: "1477-1490"}
citation: "Levin et al. (2004). The Strength of Weak Ties You Can Trust: The Mediating Role of Trust in Effective Knowledge Transfer. Management Science, 50(11), 1477-1490. https://doi.org/10.1287/mnsc.1030.0136"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Surveying 127 employees (400 usable dyadic observations) across a US pharmaceutical firm,
  a British bank, and a Canadian oil and gas company, the authors show that the well-known
  benefit of strong ties for receiving useful knowledge is actually explained by
  benevolence- and competence-based trust: once both trust dimensions are statistically
  controlled, the direct effect of tie strength flips and weak ties emerge as more useful (a
  suppression effect). Competence-based trust matters most when the knowledge being
  transferred is tacit rather than codified. The paper introduces the construct of 'trusted
  weak ties' -- low-closeness, high-trust relationships -- as the dyads that deliver the
  most useful knowledge of all, refining Granovetter's weak-tie argument by adding a
  relational trust mechanism.
claims:
  - text: "Strong ties had a positive, significant overall effect on receipt of useful knowledge (p = 0.006), but this effect disappeared -- and reversed sign to favor weak ties -- once benevolence-based (p < 0.001) and competence-based (p = 0.009) trust were entered as mediators, satisfying all four conditions for full mediation."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["social-support", "network-structure"]
  - text: "Competence-based trust interacted significantly with knowledge tacitness (p = 0.021): its effect on usefulness was strong for highly tacit knowledge (slope = 0.21, p = 0.006), only marginal for average-tacitness knowledge (slope = 0.11, p = 0.095), and essentially zero for fully codified/explicit knowledge (slope = 0.00, p = 0.993); benevolence-based trust showed no such interaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["social-support"]
  - text: "22% of the dyadic ties studied were 'trusted weak ties' (below-average tie strength but above-average on at least one trust dimension), which the model identifies as the relationships yielding the most useful knowledge overall; 18% were 'not fully trusted strong ties' that provided neither the relational nor the structural benefit."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "social-support"]
population:
  who: "Mid-level professionals in knowledge-intensive roles (R&D, financial modeling, oil exploration) across one division each of a pharmaceutical company, a bank, and an oil and gas company"
  where: ["United States", "United Kingdom", "Canada"]
  when: null
  n: 127
  sector: ["private-sector", "corporate"]
  sample_notes: >
    127 of 265 surveyed employees completed both survey parts (48% response rate); each
    respondent rated 4 knowledge-source relationships (2 most-helpful, 2 least-helpful),
    yielding 508 dyads reduced to 400 via listwise deletion (118 respondents). 61% male,
    median age early 40s, 47% held a graduate degree. No significant
    respondent/nonrespondent differences on available demographics; no significant
    interaction effects across the three firms, so data were pooled.
limitation:
  primary: "All predictor and outcome measures came from the knowledge seeker's own retrospective self-report, so trust, tie strength, and usefulness ratings could be contaminated by post-hoc rationalization or common-method bias, despite the authors' efforts (split survey timing, Harman's test, control variables) to mitigate this."
  others:
    - "Cross-sectional, correlational design cannot establish that trust or tie strength causally produced the knowledge outcomes, only that the associations and mediation pattern are consistent with the proposed model."
    - "Competence-based trust was measured generically rather than as domain-specific expertise, which the authors note may understate its true relevance to knowledge usefulness."
    - "Sample is limited to three large corporate divisions in knowledge-intensive white-collar work, limiting generalizability to other organizational forms (e.g., distributed open-source or small-team contexts)."
risk_of_bias: "medium"
relevance_to_project: >
  Gives the SNH project an empirically grounded mechanism -- competence- and benevolence-
  based trust -- for why some network ties (not just strong, high-frequency ones) deliver
  valuable knowledge and support, directly informing how to design for 'trusted weak ties'
  as a target relationship type in remote and distributed teams rather than optimizing
  solely for tie frequency or closeness.
tags:
  topic: ["collaboration", "social-support", "methodology"]
  method: ["survey", "cross-sectional"]
  population: ["knowledge-workers", "corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/levin-et-al-2004-the-strength-of-weak-ties-you-can-trust-the-mediating-role-of-trust-in-effective-knowledge-transfer/levin-et-al-2004-the-strength-of-weak-ties-you-can-trust-the-mediating-role-of-trust-in-effective-knowledge-transfer.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/levin-et-al-2004-the-strength-of-weak-ties-you-can-trust-the-mediating-role-of-trust-in-effective-knowledge-transfer.pdf"
  notes: null
