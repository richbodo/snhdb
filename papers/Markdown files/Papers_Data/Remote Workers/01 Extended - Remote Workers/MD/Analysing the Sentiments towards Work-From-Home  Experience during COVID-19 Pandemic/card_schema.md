id: "dubey-2020-analysing-the-sentiments-towards-work-from"
title: "Analysing the Sentiments towards Work-From-Home Experience during COVID-19 Pandemic"
authors:
  - "Dubey, Akash Dutt"
  - "Tripathi, Shreya"
year: 2020
doi: "10.24840/2183-0606_008.001_0003"
venue: {type: "journal", name: "Journal of Innovation Management", volume: 8, issue: 1, pages: null}
citation: "Dubey et al. (2020). Analysing the Sentiments towards Work-From-Home Experience during COVID-19 Pandemic. Journal of Innovation Management, 8(1). https://doi.org/10.24840/2183-0606_008.001_0003"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "weak", preregistered: false}
gist: >
  This study performed sentiment analysis on 100,000 English-language tweets containing
  #WorkFromHome or #WFH, collected between 15 March and 15 April 2020 during the early
  COVID-19 lockdowns. Using the NRC Emotion Lexicon and Syuzhet package, the authors found
  tweets skewed strongly positive (73.10% positive vs 26.10% negative) and were dominated by
  trust, anticipation, and joy rather than fear or sadness, suggesting a broadly welcoming
  public reaction to the sudden shift to remote work. It offers an early, descriptive
  snapshot of collective sentiment toward WFH rather than any individual-level or causal
  account of remote worker wellbeing.
claims:
  - text: "Of 100,000 tweets about work-from-home collected 15 March-15 April 2020, 73.10% carried positive sentiment versus 26.10% negative sentiment."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["wellbeing", "job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "The most common emotions expressed in WFH-related tweets were trust (24.03%), anticipation, and joy (16.45%), while fear (10.17%), sadness (8.60%), anger (6.69%) and disgust (4.32%) were comparatively rare."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["wellbeing", "stress"]
    predictors: ["remote-work-intensity"]
  - text: "Word-cloud analysis showed positive-emotion words (GOOD, BREAK, HOPE, LOVE, SHARE, HAPPY, SAFE, HOME, TEAM, MANAGE) dominated the discourse, while negative words like PANDEMIC, ISOLATE, and LATE clustered specifically around sadness."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["isolation", "wellbeing"]
    predictors: ["remote-work-intensity"]
population:
  who: "100,000 English-language Twitter/X posts mentioning #WorkFromHome or #WFH, worldwide (not individual workers directly surveyed)"
  where: []
  when: "15 March 2020 - 15 April 2020"
  n: 100000
  sector: ["cross-sector"]
  sample_notes: >
    Convenience sample of public tweets gathered via Twitter API using RTweet in R; retweets
    excluded to avoid duplication; restricted to English-language tweets only (acknowledged
    by authors as a limitation), so not representative of the global remote-workforce
    population, and tweet authorship/employment status is unverified.
limitation:
  primary: "The sample is limited to English-language tweets, which the authors themselves flag as a limitation that skews the sample toward English-speaking, Twitter-using populations and excludes non-English and non-Twitter-using workers globally."
  others:
    - "Sentiment/emotion classification via lexicon-based tools (NRC Emotion Lexicon, Syuzhet) is a coarse proxy for actual worker wellbeing and can misclassify sarcasm, context, or mixed sentiment."
    - "No demographic, occupational, or employment-status data on tweet authors, so findings cannot be linked to specific worker subgroups or work-from-home conditions."
    - "Short one-month observation window during the acute, novel phase of pandemic lockdowns limits generalizability to sustained or later-stage remote work experiences."
risk_of_bias: "high"
relevance_to_project: >
  Provides an early, large-N but low-precision signal that public sentiment toward the
  transition to remote work was net positive during the initial COVID-19 lockdown, which is
  useful as a contextual/historical data point but should not be treated as evidence about
  individual-level isolation, loneliness, or burnout risk in remote workers -- its lexicon-
  based sentiment scoring cannot substitute for validated wellbeing or social-support
  measures the SNH project would need.
tags:
  topic: ["remote-work", "wellbeing", "methodology"]
  method: ["cross-sectional", "secondary-data"]
  population: ["general-public", "social-media-users"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Analysing the Sentiments towards Work-From-Home  Experience during COVID-19 Pandemic/Analysing the Sentiments towards Work-From-Home  Experience during COVID-19 Pandemic.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Analysing the Sentiments towards Work-From-Home  Experience during COVID-19 Pandemic.pdf"
  notes: null
