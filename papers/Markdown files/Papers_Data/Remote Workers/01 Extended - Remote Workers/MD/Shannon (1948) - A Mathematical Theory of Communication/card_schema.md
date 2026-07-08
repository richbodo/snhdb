id: "shannon-1948-a-mathematical-theory-of-communication"
title: "A Mathematical Theory of Communication"
authors:
  - "Shannon, C. E."
year: 1948
doi: "10.1002/j.1538-7305.1948.tb00917.x"
venue: {type: "journal", name: "Bell System Technical Journal", volume: 27, issue: 4, pages: "623-656"}
citation: "Shannon (1948). A Mathematical Theory of Communication. Bell System Technical Journal, 27(4), 623-656. https://doi.org/10.1002/j.1538-7305.1948.tb00917.x"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  Shannon's 1948 paper founds information theory, defining information quantitatively via
  entropy and proving that reliable transmission is possible up to a channel's capacity
  despite noise (the noisy-channel coding theorem), while transmission above capacity
  necessarily incurs error. It also derives the capacity of a bandwidth-limited Gaussian
  channel (C = W log2(1 + P/N)) and shows how statistical redundancy in a source (e.g.,
  English text) can be exploited for efficient coding. For the SNH corpus it functions as a
  foundational reference rather than a study of remote work or wellbeing: it supplies the
  formal vocabulary (entropy, redundancy, channel capacity, noise) that later empirical work
  on communication and network structure implicitly draws on.
claims:
  - text: "Proves the noisy-channel coding theorem: for a channel of capacity C, messages can be encoded and transmitted at any rate R < C with arbitrarily small error probability given sufficiently long coding, whereas any attempt to transmit at a rate above C necessarily produces a positive error rate that cannot be reduced below some fixed threshold."
    evidence: "theory"
    support_strength: "very-strong"
    outcomes: ["communication"]
    predictors: ["network-structure"]
  - text: "Defines entropy H = -Σ p_i log p_i as the unique measure of the information/uncertainty produced by a discrete source (derived from axioms of continuity, monotonicity, and additivity), and demonstrates that natural sources such as English text carry substantial statistical redundancy (on the order of 50%) that can be removed by proper encoding without loss of information."
    evidence: "theory"
    support_strength: "very-strong"
    outcomes: ["communication"]
    predictors: ["redundancy"]
  - text: "Derives the capacity of a continuous channel with bandwidth W perturbed by white Gaussian noise of power N as C = W log2((P+N)/N) bits per second (the Shannon-Hartley law), establishing the fundamental trade-off among bandwidth, signal power, and noise for any communication channel, discrete or continuous."
    evidence: "theory"
    support_strength: "very-strong"
    outcomes: ["communication"]
    predictors: ["signal-noise-ratio"]
population:
  who: "Not applicable: a mathematical/engineering theory paper with no human sample, participants, or organizational population."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No empirical sample; the paper analyzes abstract stochastic sources, discrete/continuous
    channels, and idealized noise models (e.g., synthetic letter-sequence sources, English-
    text statistics used as illustrative examples).
limitation:
  primary: "Purely mathematical/engineering treatment of the technical problem of signal transmission; it explicitly excludes the semantic and human/psychological dimensions of communication, so it says nothing directly about isolation, belonging, collaboration quality, or wellbeing."
  others:
    - "Key results (e.g., the coding theorem) are asymptotic, holding in the limit of long block lengths, and abstract away real-world constraints such as latency, cost, and human interpretation of messages."
    - "Assumes a fixed, known probabilistic model of source and channel, which does not map cleanly onto the dynamic, context-dependent communication patterns of remote teams or online communities."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Supplies the formal information-theoretic constructs (entropy, redundancy, channel
  capacity, signal-to-noise trade-offs) that underlie later quantitative approaches to
  measuring communication bandwidth, information loss, and channel richness in remote-work
  and online-community research; useful as a conceptual reference when the project wants to
  justify or interpret entropy- or capacity-based measures of communication quality rather
  than as a source of empirical SNH findings.
tags:
  topic: ["measurement", "methodology", "social-presence"]
  method: ["theory"]
  population: ["not-applicable"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Shannon (1948) - A Mathematical Theory of Communication/Shannon (1948) - A Mathematical Theory of Communication.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Shannon (1948) - A Mathematical Theory of Communication.pdf"
  notes: null
