id: "world-2023-world-health-statistics-2023-monitoring-health"
title: "World Health Statistics 2023: Monitoring Health for the SDGs, Sustainable Development Goals"
authors:
  - "World Health Organization"
year: 2023
doi: null
venue: {type: "report", name: "World Health Organization", volume: null, issue: null, pages: null}
citation: "World Health Organization (2023). World Health Statistics 2023: Monitoring Health for the SDGs, Sustainable Development Goals. World Health Organization."
article_type: "review"
method: {design: "global-statistical-compendium", approach: "secondary-data", evidence_level: "reference", preregistered: false}
gist: >
  This is WHO's annual global health statistics report, compiling country-level indicators
  toward the health-related Sustainable Development Goals (SDGs) and WHO's 13th General
  Programme of Work. It covers mortality and disease trends (maternal/child mortality, NCDs,
  infectious disease, injuries and violence, environmental risks) and universal health
  coverage, with a dedicated section on suicide mortality trends and a briefer discussion of
  the global mental-disorder treatment gap. It is a reference compendium of population
  health statistics rather than a study of workplace or remote-work social dynamics.
claims:
  - text: "The global suicide mortality rate fell 29% between 2000 and 2019, from 13.0 to 9.2 deaths per 100,000 population; rates declined in all WHO regions except the Region of the Americas, where they rose 28%, while the European Region had both the largest decline (42%) and the highest 2019 rate (12.8 per 100,000)."
    evidence: "Global Health Estimates mortality data (2000-2019) compiled and reported by WHO"
    support_strength: "strong"
    outcomes: ["suicidal-ideation"]
    predictors: []
  - text: "Suicide accounted for 16% of all injury deaths globally in 2019 and more than 1 in 100 (1.3%) of all deaths; men and boys accounted for 69% of suicide deaths, and suicide was the third leading cause of death among girls and young women aged 15-29."
    evidence: "WHO Global Health Estimates injury and mortality data, 2019"
    support_strength: "strong"
    outcomes: ["suicidal-ideation"]
    predictors: []
  - text: "Only about one third of people with depression and 29% of people with psychosis globally receive formal mental health care, and mental, neurological and substance-use disorders accounted for 10% of the global disease burden (DALYs) and 25% of years lived with disability in 2019."
    evidence: "Cited secondary sources (WHO Mental Health Atlas 2020 and Global Burden of Disease 2019) synthesized in the report"
    support_strength: "moderate"
    outcomes: ["mental-health", "depression"]
    predictors: ["help-seeking"]
population:
  who: "Global population, all countries and WHO regions, disaggregated by sex and age group"
  where: ["Global"]
  when: "Primarily 2000-2021 (mortality/SDG indicator trends); some 2019 disease-burden estimates"
  n: null
  sector: ["public-health", "population-health"]
  sample_notes: >
    Country-reported vital registration and modelled estimates aggregated by WHO across all
    member states; not a primary study, no individual-level sample.
limitation:
  primary: "This is a statistical compendium synthesizing modelled national/regional estimates from many underlying sources, not primary research; individual estimates carry wide uncertainty intervals and depend on the quality of country reporting systems, which varies greatly especially in low- and middle-income countries."
  others:
    - "Contains almost nothing specific to remote work, workplace social dynamics, or online/community social network health, limiting direct relevance to the project beyond baseline mental-health/suicide epidemiology."
    - "Mental health and suicide content is a small fraction of a much larger report covering unrelated topics (maternal mortality, NCDs, infectious disease, climate change, health systems)."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Provides authoritative baseline global statistics on suicide mortality trends and the
  mental-health treatment gap that can contextualize (but not directly evidence) claims
  about isolation, loneliness, and mental health outcomes relevant to remote worker and
  community social-network health.
tags:
  topic: ["mental-health", "suicide-prevention"]
  method: ["secondary-data"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Mental Health/MD/World Health Statistics 2023/World Health Statistics 2023.md"
  pdf: "papers/Mental Health/World Health Statistics 2023.pdf"
  notes: "no-doi: confirmed none (manual review)"
