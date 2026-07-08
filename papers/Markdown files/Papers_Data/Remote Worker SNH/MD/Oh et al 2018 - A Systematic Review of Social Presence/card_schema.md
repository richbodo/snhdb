id: "oh-2018-a-systematic-review-of-social-presence"
title: "A Systematic Review of Social Presence: Definition, Antecedents, and Implications"
authors:
  - "Oh, Catherine S."
  - "Bailenson, Jeremy N."
  - "Welch, Gregory F."
year: 2018
doi: "10.3389/frobt.2018.00114"
venue: {type: "journal", name: "Frontiers in Robotics and AI", volume: 5, issue: null, pages: null}
citation: "Oh et al. (2018). A Systematic Review of Social Presence: Definition, Antecedents, and Implications. Frontiers in Robotics and AI, 5. https://doi.org/10.3389/frobt.2018.00114"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This systematic review synthesizes 233 findings from 152 studies on the antecedents of
  social presence (the felt sense of 'being with' a real other) in computer-mediated and
  virtual-reality communication. It organizes predictors into immersive/technological
  qualities (modality, visual representation, interactivity, haptics, audio, depth cues),
  contextual factors (physical proximity, identity cues, presence of others, personality of
  the virtual other), and individual differences (demographics, psychological traits), and
  argues that more social presence is not always better since it can backfire for socially
  anxious people or in vulnerable/disliked-partner contexts. For SNH design purposes it is a
  map of which communication-medium features reliably raise or fail to raise the subjective
  feeling of co-presence between remote interactants.
claims:
  - text: "Across the studies reviewed, behavioral realism (e.g., mutual gaze, nodding, blushing, other responsive nonverbal cues) was one of the most consistent positive predictors of social presence, more so than photographic/anthropomorphic visual realism, which showed mixed effects."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["social-presence", "communication"]
    predictors: ["embodiment", "network-structure"]
  - text: "Interactivity, haptic feedback (positive in 9 of 10 identified studies), depth cues/stereoscopy, and audio quality were consistently positively associated with social presence, whereas general modality (e.g., text vs. audio vs. video) and display quality showed weaker or mixed effects."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["social-presence"]
    predictors: ["embodiment", "network-structure"]
  - text: "Higher social presence is not uniformly beneficial: individuals high in social anxiety or communication apprehension, and interactions with vulnerable or disliked communication partners, showed evidence of worse outcomes (e.g., worse speech performance, escalated negative attitudes, more verbal aggression) at higher levels of social presence, and less socially oriented people report feeling less social presence overall."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["social-presence", "wellbeing", "communication"]
    predictors: ["psychological-safety", "sense-of-belonging"]
population:
  who: "152 empirical studies (233 separate findings) on antecedents of social presence in computer-mediated and virtual-reality communication, drawn from journals and conference proceedings in virtual environments/CMC research; study participants were predominantly convenience/student samples in lab experiments interacting with avatars, agents, or remote human partners."
  where: ["USA", "Netherlands", "UK", "Germany", "Korea", "New Zealand", "Canada", "other countries (multi-national corpus)"]
  when: null
  n: 152
  sector: ["academic-research", "technology"]
  sample_notes: >
    Included studies were identified via targeted journal/conference archive review plus
    keyword database searches (EBSCO, PsycNET, ISPR Telepresence Literature Refshare, Google
    Scholar); no formal study-quality appraisal was conducted (the authors explicitly note
    they assumed each included study's findings were true and correct), and sample sizes per
    predictor varied widely, limiting confidence in null findings.
limitation:
  primary: "No quantitative meta-analysis or systematic quality/risk-of-bias appraisal was performed across the 152 included studies; heterogeneous social-presence measures across studies limit direct comparability of effect directions reported in the summary tables."
  others:
    - "Most included studies used lab-based convenience samples (often students) in short, artificial interaction tasks, limiting ecological validity for real-world remote work or long-term relationships."
    - "The review excludes theoretically adjacent constructs (e.g., plausibility illusion) that could explain some findings, and does not address actual (vs. perceived) agency of communication partners."
    - "Many reviewed studies used older, lower-fidelity VR/CMC technology, so findings may not generalize to current video-call, avatar, or immersive platforms."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs which features of remote/virtual communication tools (video presence,
  avatars with behavioral realism like gaze and reactive expressions, interactivity, audio
  quality) are most likely to raise felt co-presence in distributed teams, and cautions SNH
  designers that maximizing social presence is not universally good — it can worsen
  experience for socially anxious remote workers or in already-strained relationships,
  arguing for tunable/optional presence levels in collaboration tools rather than a single
  'richer is always better' design.
tags:
  topic: ["remote-work", "social-presence", "measurement", "collaboration", "methodology"]
  method: ["review-systematic", "secondary-data"]
  population: ["lab-experiment-samples", "cmc-vr-users"]
source:
  markdown: "Papers_Data/Remote Worker SNH/MD/Oh et al 2018 - A Systematic Review of Social Presence/Oh et al 2018 - A Systematic Review of Social Presence.md"
  pdf: "papers/Remote Worker SNH/Oh et al 2018 - A Systematic Review of Social Presence.pdf"
  notes: null
