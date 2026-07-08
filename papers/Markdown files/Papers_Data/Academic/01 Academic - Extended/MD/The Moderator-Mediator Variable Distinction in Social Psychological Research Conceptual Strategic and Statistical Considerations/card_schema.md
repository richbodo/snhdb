id: "baron-1986-the-moderator-mediator-variable-distinction-in"
title: "The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations."
authors:
  - "Baron, Reuben M."
  - "Kenny, David A."
year: 1986
doi: "10.1037//0022-3514.51.6.1173"
venue: {type: "journal", name: "Journal of Personality and Social Psychology", volume: 51, issue: 6, pages: "1173-1182"}
citation: "Baron et al. (1986). The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations.. Journal of Personality and Social Psychology, 51(6), 1173-1182. https://doi.org/10.1037//0022-3514.51.6.1173"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This is Baron and Kenny's (1986) foundational methodological article distinguishing
  moderator variables (which change the strength or direction of a predictor-outcome
  relation via an interaction term) from mediator variables (which causally transmit a
  predictor's effect on an outcome). It lays out regression-based procedures for testing
  each -- including the three-equation causal-steps test of mediation and Sobel's
  significance test for the indirect effect -- and shows how the two can be combined in a
  single path model (mediated moderation, moderated mediation). It contributes the standard
  statistical toolkit the SNH project needs whenever it asks whether a variable like social
  support explains (mediates) versus merely conditions (moderates) an effect on outcomes
  such as burnout or turnover.
claims:
  - text: "Formally distinguishes a moderator effect (a significant interaction term, e.g. the product XZ in a regression of Y on X, Z, and XZ, indicating the X-Y relation changes strength or direction as a function of Z) from a mediator effect (a three-variable causal chain in which X significantly predicts mediator M [Path a], M significantly predicts Y controlling for X [Path b], and the direct X-Y relation [Path c] is reduced -- ideally to non-significance -- once M is controlled), and specifies different regression procedures depending on whether the third variable is categorical or continuous."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["mediation-moderation"]
    predictors: ["network-structure"]
  - text: "To establish mediation, prescribes estimating three regression equations (M on X; Y on X; Y on both X and M): mediation requires X to affect M, X to affect Y, and M to affect Y controlling for X, with the X-to-Y coefficient shrinking (ideally to zero) once M is added; provides Sobel's (1982) approximate standard error for the indirect effect ab as sqrt(b^2*sa^2 + a^2*sb^2 + sa^2*sb^2)."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["mediation-moderation"]
    predictors: ["mediation-moderation"]
  - text: "Warns that measurement error in the mediator systematically biases estimates -- underestimating the mediator's true effect and overestimating the independent variable's direct effect on the outcome -- and that unmodeled feedback (the outcome causing the presumed mediator) can invalidate a simple regression-based mediation test, motivating multiple-indicator latent-variable structural equation modeling (e.g., LISREL) or two-stage least squares as remedies."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["measurement"]
    predictors: ["mediation-moderation"]
population:
  who: "Not an empirical study of a sample; a statistical/conceptual treatise addressed to social psychology researchers, illustrated throughout with secondary examples drawn from published studies (e.g., stress and control, crowding, attitude-behavior and trait-behavior research)."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No original data collection or participants; all substantive examples (e.g., Glass &
    Singer 1972 on noise stress, Fishbein & Ajzen's theory of reasoned action, Langer &
    Saegert 1977 on crowding) are drawn from prior published literature purely to illustrate
    the moderator/mediator distinction.
limitation:
  primary: "Offers no original empirical data; its causal-steps approach to testing mediation (judging mediation by whether the direct path becomes non-significant once the mediator is added) has since been shown by later methodological work to have low statistical power and to conflate absence of a significant direct effect with absence of mediation, and is now largely superseded by bootstrapped indirect-effect tests."
  others:
    - "Sobel's test for the indirect effect assumes multivariate normality and asymptotic sample sizes, performing poorly in small samples."
    - "Guidance on ruling out reverse causation or omitted-variable confounding in mediation tests is limited to a brief pointer toward Smith's (1982) two-stage least squares method, not a general solution."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Supplies the canonical statistical framework the SNH project should use when testing
  whether a variable like social support, loneliness, or team cohesion mediates (versus
  merely moderates) the relation between remote-work intensity and outcomes such as burnout
  or turnover -- e.g., the three-regression mediation test, Sobel's indirect-effect
  significance test, and criteria for when a third variable should be modeled as an
  interaction term rather than a causal intermediary in the project's SNH outcome models.
tags:
  topic: ["methodology", "measurement"]
  method: ["theory", "statistical-methods"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The Moderator-Mediator Variable Distinction in Social Psychological Research Conceptual Strategic and Statistical Considerations/The Moderator-Mediator Variable Distinction in Social Psychological Research Conceptual Strategic and Statistical Considerations.md"
  pdf: "papers/Academic/01 Academic - Extended/The Moderator-Mediator Variable Distinction in Social Psychological Research Conceptual Strategic and Statistical Considerations.pdf"
  notes: null
