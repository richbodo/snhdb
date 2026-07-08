id: "lerner-2002-some-simple-economics-of-open-source"
title: "Some Simple Economics of Open Source"
authors:
  - "Lerner, Josh"
  - "Tirole, Jean"
year: 2002
doi: "10.1111/1467-6451.00174"
venue: {type: "journal", name: "The Journal of Industrial Economics", volume: 50, issue: 2, pages: "197-234"}
citation: "Lerner et al. (2002). Some Simple Economics of Open Source. The Journal of Industrial Economics, 50(2), 197-234. https://doi.org/10.1111/1467-6451.00174"
article_type: "theory"
method: {design: "case-study", approach: "analytical", evidence_level: "low", preregistered: false}
gist: >
  This 2002 paper by Lerner and Tirole uses labor-economics 'career concerns' theory and
  industrial-organization theory to explain why programmers contribute unpaid labor to open-
  source projects (Apache, Linux, Perl, Sendmail), arguing that the visibility of individual
  code contributions functions as a signal of talent that yields delayed career and
  reputational payoffs. Drawing on four project case studies (interviews plus secondary
  contributor-distribution data), the authors show open-source participation is highly
  unequal, with a small 'elite' core producing most of the code, and that early, prominent
  contributors frequently converted this signaling capital into commercial leadership roles.
  It offers an economic account of why decentralized volunteer communities sustain
  themselves and which governance features (modularity, credible leadership, transparent
  decision rules) prevent them from fragmenting or 'forking'.
claims:
  - text: "Contribution to open-source code is extremely concentrated: in an analysis of 25 million lines of code across 3,149 projects (~13,000 contributors), more than three-quarters of contributors made only one contribution and only 1 in 25 had more than five, yet the top decile of contributors accounted for 72% of all code contributed and the top two deciles for 81%."
    evidence: "secondary-data"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "community-engagement", "open-source-maintenance"]
  - text: "Apache's own developer community shows the same elitist pattern: the top 15 developers on the core Apache developers mailing list contributed 83% to 91% of changes, whereas bug/problem reports (a lower-effort form of participation) were distributed far less unequally."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["collaboration"]
    predictors: ["open-source-maintenance", "network-structure"]
  - text: "Prominent early open-source contributors frequently converted reputation built through visible, individually-attributable contributions into subsequent commercial roles (e.g., founding or leading venture-backed companies such as Sendmail Inc., Collab.Net, Sun Microsystems, Cygnus Solutions), consistent with a signaling/career-concerns account of participation motives rather than pure altruism."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["retention", "job-engagement"]
    predictors: ["community-engagement", "open-source-maintenance", "leadership-style"]
population:
  who: "Four purposively selected, high-profile open source software projects (Apache, Linux, Perl, Sendmail) and their founders/lead maintainers, studied via document review and interviews, plus secondary quantitative data on broader open-source contributor populations (e.g., a ~13,000-contributor, 3,149-project analysis and a study of Linux mailing-list posters)."
  where: ["United States", "Europe"]
  when: "Case interviews and analysis conducted circa 1999-2000; secondary datasets from 1999-2000; published 2002"
  n: null
  sector: ["open-source", "software-industry"]
  sample_notes: >
    Non-random, small sample of four projects chosen because they were already
    successful/prominent; the authors explicitly caution these are 'observations based on a
    small sample of successful projects' and that determining what causes success versus
    failure in an informal setting is difficult. Secondary contributor-distribution figures
    come from working papers with response-rate/representativeness not independently
    verifiable in this text.
limitation:
  primary: "The evidence base is four purposively selected, already-successful open source projects examined qualitatively, not a representative or random sample with variation in outcomes, so the proposed economic mechanisms (signaling, career concerns) are illustrated rather than causally tested."
  others:
    - "The paper is explicitly exploratory/agenda-setting theory-building, declining to construct formal statistical models or test hypotheses on large samples."
    - "Key contribution-inequality statistics are drawn from unpublished working papers (Ghosh & Prakash 2000; Dempsey et al. 1999) whose methodology is not independently verifiable here."
    - "Written in 2000-2002, prior to major shifts in OSS tooling, governance (e.g., GitHub-era platforms), and corporate open-source practice, limiting contemporary generalizability."
risk_of_bias: "high"
relevance_to_project: >
  The paper's signaling/career-concerns framework (visibility of contribution, peer
  recognition, 'ego gratification' as a delayed reward) offers a candidate mechanism for why
  remote and open-source contributors sustain unpaid or discretionary engagement, directly
  relevant to designing recognition and visibility features that support community health.
  Its finding of extreme core-periphery contribution inequality (a small elite doing most of
  the work) is directly relevant to understanding and mitigating maintainer burnout risk
  concentration in open-source communities.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "collaboration"]
  method: ["case-study", "secondary-data"]
  population: ["open-source-contributors", "software-industry"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/Some Simple Economics of Open Source/Some Simple Economics of Open Source.md"
  pdf: "papers/Articles/01 Articles - Extended/Some Simple Economics of Open Source.pdf"
  notes: null
