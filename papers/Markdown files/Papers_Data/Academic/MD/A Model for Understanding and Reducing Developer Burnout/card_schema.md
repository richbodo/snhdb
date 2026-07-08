id: "trinkenreich-2023-a-model-for-understanding-and-reducing"
title: "A Model for Understanding and Reducing Developer Burnout"
authors:
  - "Trinkenreich, Bianca"
  - "Stol, Klaas-Jan"
  - "Steinmacher, Igor"
  - "Gerosa, Marco A."
  - "Sarma, Anita"
  - "Lara, Marcelo"
  - "Feathers, Michael"
  - "Ross, Nicholas"
  - "Bishop, Kevin"
year: 2023
doi: "10.1109/icse-seip58684.2023.00010"
venue: {type: "conference", name: "2023 IEEE/ACM 45th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)", volume: null, issue: null, pages: "48-60"}
citation: "Trinkenreich et al. (2023). A Model for Understanding and Reducing Developer Burnout. 2023 IEEE/ACM 45th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 48-60. https://doi.org/10.1109/icse-seip58684.2023.00010"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A large-scale survey of 3,281 software delivery team members at Globant tested a
  structural equation model linking Generative Organizational Culture to Burnout through
  three mediators (Sense of Belonging, Climate for Learning, Inclusiveness) and Work
  Satisfaction. A generative, psychologically-safe culture was positively associated with
  belonging, learning climate, and inclusiveness, which in turn predicted work satisfaction,
  which was negatively associated with burnout; multigroup analysis further showed
  inclusiveness mattered twice as much for women's satisfaction as men's, and learning
  climate mattered for non-leaders but not leaders.
claims:
  - text: "Generative Organizational Culture was positively associated with Sense of Belonging (B=.48), Climate for Learning (B=.54), and Inclusiveness (B=.45), and Work Satisfaction was negatively associated with Burnout (B=-.29), all p<.001."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "sense-of-belonging", "job-satisfaction"]
    predictors: ["organizational-culture", "psychological-safety", "inclusiveness"]
  - text: "Sense of Belonging (B=.24), Climate for Learning (B=.22), and Inclusiveness (B=.12) each had a positive, significant association with Work Satisfaction (p<.001), which in turn showed a reverse association with Burnout."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "burnout"]
    predictors: ["sense-of-belonging", "inclusiveness", "leadership-style"]
  - text: "Multigroup analysis found the Organizational Culture to Inclusiveness link was stronger for women (B=.53) than men (B=.41), women were twice as satisfied by an inclusive team as men (B=.20 vs .10), Climate for Learning predicted Work Satisfaction for non-leaders but not for leaders (B=.22 vs .08 n.s.), and none of Hofstede's six national-culture dimensions significantly moderated the Work Satisfaction-Burnout link in the full sample, though high Masculinity reduced burnout for men specifically."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction"]
    predictors: ["inclusiveness", "leadership-style", "organizational-culture"]
population:
  who: "Software delivery team members (developers, QA, PMs, and other roles) at Globant, a large multinational IT services company"
  where: ["Colombia", "Argentina", "India", "Mexico", "Uruguay", "Chile", "Peru", "USA", "Brazil", "Spain", "Belarus"]
  when: null
  n: 3281
  sector: ["software-industry", "it-services"]
  sample_notes: >
    Online questionnaire distributed via corporate email/Globant Glow to internal staff;
    10,566 initial responses reduced to 3,281 complete responses (69% dropped for missing
    data). Sample is 74.8% men / 25.2% women, majority non-leadership roles, single company
    so generalizability outside Globant is unverified.
limitation:
  primary: "Cross-sectional survey design means all hypothesized relationships are associational, not causal; the authors themselves note it is easier to argue culture drives satisfaction than the reverse but cannot rule it out."
  others:
    - "Single-company sample (Globant only) limits external validity; effects may not generalize to other organizations or industries."
    - "Burnout was measured with only two Likert items (a pragmatic shortcut) rather than a validated multi-item burnout inventory, and national culture was approximated by country of residence rather than individuals' actual cultural values."
    - "Only current employees were surveyed; those who already left due to burnout are not represented, limiting inference about turnover."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a quantitative, large-n model (n=3,281) for how organizational culture and
  specific mediators (belonging, inclusiveness, learning climate) translate into work
  satisfaction and reduced burnout, and shows the pathway differs by gender and leadership
  role -- directly useful for the SNH project's design of belonging/inclusiveness
  interventions and for choosing which mediating constructs to measure or target in
  remote/hybrid team health tooling.
tags:
  topic: ["burnout", "job-satisfaction", "psychological-safety", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["software-developers", "tech-industry"]
source:
  markdown: "Papers_Data/Academic/MD/A Model for Understanding and Reducing Developer Burnout/A Model for Understanding and Reducing Developer Burnout.md"
  pdf: "papers/Academic/A Model for Understanding and Reducing Developer Burnout.pdf"
  notes: null
