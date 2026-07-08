id: "fried-2015-depression-is-not-a-consistent-syndrome"
title: "Depression is not a consistent syndrome: An investigation of unique symptom patterns in the STAR*D study"
authors:
  - "Fried, Eiko I."
  - "Nesse, Randolph M."
year: 2015
doi: "10.1016/j.jad.2014.10.010"
venue: {type: "journal", name: "Journal of Affective Disorders", volume: 172, issue: null, pages: "96-102"}
citation: "Fried et al. (2015). Depression is not a consistent syndrome: An investigation of unique symptom patterns in the STAR*D study. Journal of Affective Disorders, 172, 96-102. https://doi.org/10.1016/j.jad.2014.10.010"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Analyzing baseline data from 3703 depressed outpatients in the STAR*D trial, the authors
  show that DSM-5 symptom-based diagnoses of major depressive disorder mask enormous
  heterogeneity: 1030 distinct symptom profiles emerged, nearly half endorsed by only a
  single person, and this heterogeneity persisted even after controlling for overall
  severity. The paper argues that summing symptoms into a single severity score obscures
  qualitatively different presentations of 'depression,' which may help explain inconsistent
  treatment-efficacy findings and motivates analyzing individual symptoms and their causal
  networks rather than relying on sum-scores alone.
claims:
  - text: "Among 3703 depressed outpatients in the STAR*D baseline sample, 1030 unique DSM-5 symptom profiles were identified; 864 profiles (83.9%) were endorsed by five or fewer participants and 501 (48.6%) by only one individual, with the single most common profile occurring in just 1.8% of the sample."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "depression"]
    predictors: ["symptom-profile-heterogeneity"]
  - text: "Restricting the analysis to 569 participants who all had the same overall symptom count (the sample median of 6) still produced 188 unique profiles, with 86.2% endorsed by five or fewer people and 51.6% endorsed by only one person, showing the heterogeneity is not merely an artifact of severity differences between patients."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "depression"]
    predictors: ["symptom-profile-heterogeneity"]
  - text: "The authors argue that because patients with identical sum-scores can share almost no symptoms in common, standard sum-score depression measures (e.g., HAM-D, BDI) likely misrepresent psychosocial impairment and may partly explain the field's difficulty documenting consistent antidepressant treatment efficacy."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health", "depression"]
    predictors: ["symptom-measurement-approach"]
population:
  who: "3703 nonpsychotic MDD outpatients (mean age 41.2, 63% female) enrolled in the first treatment stage of the STAR*D trial, all receiving citalopram; recruited via relatively inclusive criteria to be representative of treatment-seeking MDD patients"
  where: ["United States"]
  when: null
  n: 3703
  sector: []
  sample_notes: >
    Multisite NIH-sponsored RCT across 14 US institutions with broad inclusion criteria (age
    18-75, DSM-IV nonpsychotic MDD, HAM-D >=14) intended to maximize representativeness of
    real-world treatment-seeking depressed outpatients; excluded
    bipolar/psychotic/schizoaffective disorders, certain eating disorders, and treatment-
    refractory cases. Symptom data drawn from telephone-administered QIDS-16 during the
    first week of treatment.
limitation:
  primary: "Symptoms were dichotomized into present/absent from a 4-point severity scale to construct profiles, which likely inflates the apparent number of distinct profiles and discards within-symptom severity information."
  others:
    - "The QIDS-16 assesses most MDD symptoms with only a single item, so item wording could have biased which profiles emerged."
    - "Analysis was limited to 12 symptoms derived from the 9 DSM-5 criteria, likely underestimating true heterogeneity by excluding clinically relevant non-criterion symptoms such as anxiety, anger, and helplessness."
    - "Many participants had comorbid medical conditions and were taking other medications that may have influenced symptom presentation independent of depression itself."
risk_of_bias: "medium"
relevance_to_project: >
  This paper is a methodological caution rather than an SNH-specific study: it demonstrates
  that sum-score approaches to mental-health measurement (as commonly used in
  wellbeing/burnout surveys) can conflate qualitatively different experiences under one
  number, which is directly relevant to how the SNH project should design and interpret any
  depression, burnout, or distress screening instruments used with remote workers or
  maintainers.
tags:
  topic: ["mental-health", "measurement", "methodology"]
  method: ["cross-sectional", "secondary-data"]
  population: ["clinical-population", "adults"]
source:
  markdown: "Papers_Data/Mental Health/01 Mental Health - Extended/MD/Depression is Not a Consistent Syndrome An Investigation of Unique Symptom Patterns in the STAR-D Study/Depression is Not a Consistent Syndrome An Investigation of Unique Symptom Patterns in the STAR-D Study.md"
  pdf: "papers/Mental Health/01 Mental Health - Extended/Depression is Not a Consistent Syndrome An Investigation of Unique Symptom Patterns in the STAR-D Study.pdf"
  notes: null
