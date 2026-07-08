id: "beland-2023-the-short-term-economic-consequences-of"
title: "The short-term economic consequences of COVID-19: Exposure to disease, remote work and government response"
authors:
  - "Beland, Louis-Philippe"
  - "Brodeur, Abel"
  - "Wright, Taylor"
year: 2023
doi: "10.1371/journal.pone.0270341"
venue: {type: "journal", name: "PLOS ONE", volume: 18, issue: 3, pages: "e0270341"}
citation: "Beland et al. (2023). The short-term economic consequences of COVID-19: Exposure to disease, remote work and government response. PLOS ONE, 18(3), e0270341. https://doi.org/10.1371/journal.pone.0270341"
article_type: "empirical"
method: {design: "quasi-experimental", approach: "secondary-data", evidence_level: "moderate", preregistered: true}
gist: >
  Using a pre-registered analysis plan and Current Population Survey microdata (Jan
  2016-June 2020, ~3 million observations) merged with O*NET occupational indexes, the
  authors find that COVID-19's labor-market damage was concentrated in occupations requiring
  close physical proximity to coworkers, while workers able to work remotely and those
  designated essential were significantly less likely to become unemployed. The remote-work
  and proximity indexes, more than disease-exposure or essential-worker status, also help
  explain why younger and minority workers fared worse during the pandemic, since these
  groups disproportionately hold jobs that cannot be done from home.
claims:
  - text: "After COVID-19 emerged, workers in occupations with higher physical proximity to coworkers were about 3 percentage points more likely to be unemployed than workers in lower-proximity occupations (124% of the post-COVID baseline unemployment increase), and proximity was the strongest single predictor of the change in occupational unemployment (R^2 = 0.223)."
    evidence: "quasi-experimental"
    support_strength: "moderate"
    outcomes: ["turnover", "job-engagement"]
    predictors: ["remote-work-intensity", "workload"]
  - text: "Workers in occupations more amenable to remote work were 1.7 percentage points less likely to be unemployed post-COVID (about 69% of the baseline increase), and essential workers were 2 percentage points less likely to be unemployed (about 83% of the baseline increase); both effects were statistically significant at the 1% level."
    evidence: "quasi-experimental"
    support_strength: "moderate"
    outcomes: ["turnover", "job-engagement"]
    predictors: ["remote-work-intensity"]
  - text: "Across demographic groups, the ability to work remotely was moderately associated with smaller increases in unemployment (R^2 = 0.1535), and the paper presents this as a likely explanation for why younger and minority workers had worse labor market outcomes during the pandemic, since these groups have lower access to remote-work-capable jobs."
    evidence: "quasi-experimental"
    support_strength: "low-to-moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity", "sampling-method"]
population:
  who: "US civilians aged 16-70 in the Current Population Survey (CPS), across all occupations, matched to O*NET occupational task indexes and state-level COVID-19 case/death data"
  where: ["United States"]
  when: "January 2016-June 2020 (COVID-19 period: February-June 2020)"
  n: 3158372
  sector: ["general-population", "cross-sector"]
  sample_notes: >
    CPS is a monthly household survey (~60,000 households); COVID-era response rates fell to
    70-73% (about 10-13 points below normal) due to closure of some call centers and phone-
    only interviewing; some unemployed workers were likely misclassified as 'employed but
    not at work,' biasing unemployment estimates downward (the authors estimate this
    understates the unemployment rate by roughly 0.9 percentage points).
limitation:
  primary: "The design is observational/correlational (not causal): occupational exposure, proximity, remote-work, and essential-worker indexes are fixed occupation-level characteristics merged onto individual CPS records, so estimates reflect associations across occupations and time rather than a randomized or strictly quasi-experimental identification of remote work's effect."
  others:
    - "BLS-documented misclassification of unemployed workers as 'employed but not at work' during March-June 2020 biases unemployment effect estimates downward."
    - "Wage estimates are likely confounded by compositional change (lower-wage workers being laid off first), which the authors themselves flag as an alternative explanation for observed wage increases."
    - "Findings are specific to the first wave of the US pandemic (through June 2020) and the pre-vaccine, early-lockdown period; generalization to later phases or other countries is not tested."
risk_of_bias: "low"
relevance_to_project: >
  Provides population-scale, pre-registered evidence that remote-work capacity was a major
  buffer against pandemic-era job loss, and that inability to work remotely (rather than
  disease exposure per se) drove worse labor-market outcomes for younger and minority
  workers -- useful macro-level evidence for the project's case that remote-work access is a
  structural determinant of economic and psychological security, not just a lifestyle
  preference.
tags:
  topic: ["remote-work", "hybrid-work"]
  method: ["secondary-data", "quasi-experimental"]
  population: ["general-population", "us-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The short-term economic consequences of COVID-19_ Exposure to disease, remote work and government response/The short-term economic consequences of COVID-19_ Exposure to disease, remote work and government response.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The short-term economic consequences of COVID-19_ Exposure to disease, remote work and government response.pdf"
  notes: null
