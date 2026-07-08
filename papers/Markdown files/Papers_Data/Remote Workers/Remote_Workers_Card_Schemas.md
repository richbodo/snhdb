# Card Schemas - Remote Workers

<!-- GENERATED FILE - do not edit. Source of truth is each paper's
     MD/<paper>/card_schema.md. Regenerate with:
     python3 tools/audit/build_combined_cards.py -->

id: "gierveld-2006-a-6-item-scale-for-overall"
title: "A 6-Item Scale for Overall, Emotional, and Social Loneliness"
authors:
  - "Gierveld, Jenny De Jong"
  - "Tilburg, Theo Van"
year: 2006
doi: "10.1177/0164027506289723"
venue: {type: "journal", name: "Research on Aging", volume: 28, issue: 5, pages: "582-598"}
citation: "Gierveld et al. (2006). A 6-Item Scale for Overall, Emotional, and Social Loneliness. Research on Aging, 28(5), 582-598. https://doi.org/10.1177/0164027506289723"
article_type: "methods"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  The authors shortened the 11-item De Jong Gierveld Loneliness Scale to a 6-item version (3
  emotional + 3 social loneliness items) and tested it via confirmatory factor analysis on
  two independent Dutch survey samples plus the original construction sample. The two-factor
  emotional/social structure held up with high factor loadings and excellent model fit,
  reliability (alpha .70-.76) and congruent validity (correlations of .93-.95 with the full
  11-item scale) were strong, and associations with known determinants of loneliness
  (partner status, health) closely paralleled the original scale, making the short form a
  practical substitute for large surveys.
claims:
  - text: "Confirmatory factor analysis supported the postulated two-factor (emotional/social) structure of the 6-item scale in both test datasets: NKPS (n=7,244) and RHS (n=3,260), with item factor loadings ranging .54-.74, a modest correlation between latent factors (.42-.53), comparative fit index of .99, and standardized root mean square residual of .02-.04 in each sample."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["loneliness"]
    predictors: ["sampling-method"]
  - text: "The 6-item scale showed good internal reliability across three independent samples: Cronbach's alpha of .70-.76 for the full 6-item scale, .67-.74 for the 3-item emotional subscale, and .70-.73 for the 3-item social subscale, with no gains from dropping any item and no differentiation by age group."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["sampling-method"]
  - text: "Congruent validity was high: the 6-item scale correlated .93-.95 with the original 11-item scale across surveys, and correlations of the short scale with known determinants of loneliness (absence of a partner: r=.19-.26; poorer subjective health: r=.22-.24) closely paralleled the 11-item scale's correlations with the same determinants."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support"]
population:
  who: "Dutch general-population survey respondents across three studies: NESTOR-LSN (older adults born 1903-1937, n=3,987-4,494), the Netherlands Kinship Panel Study (adults 18-79, n=7,244-8,154), and the Regional Health Services survey (adults 21-99, n=3,260-4,659)."
  where: ["Netherlands"]
  when: "1992-2004 (data collection across the three constituent surveys)"
  n: null
  sector: ["general-population"]
  sample_notes: >
    Three separate probability-based Dutch samples with response rates of 62% (NESTOR-LSN),
    45% (NKPS), and 72% (RHS); NKPS response was notably lower in urbanized regions and
    underrepresented young men living with parents and women living alone, with weighting
    available but not applied in this methodological analysis.
limitation:
  primary: "The 6-item scale was tested only as embedded within the full 11-item instrument (administered alongside the other 5 items), so its psychometric performance when fielded entirely on its own, and in telephone-only administration, remains unverified."
  others:
    - "All data came from self-administered or interviewer-collected questionnaires in the Netherlands only; cross-national and cross-mode generalizability is asserted but not directly tested in this study."
    - "Validity was assessed via correlation with only two determinants (partner status, subjective health), a narrow validation criterion set."
    - "The samples are general-population and skew toward older/mixed-age Dutch adults, not workplace or remote-work populations relevant to the SNH project."
risk_of_bias: "low"
relevance_to_project: >
  This paper validates a short, low-burden loneliness measure that separately scores
  emotional loneliness (missing an intimate relationship) and social loneliness (missing a
  wider network) -- a distinction the SNH project can use to design measurement instruments
  that differentiate whether remote-worker interventions should target close relational
  support versus broader community/team belonging.
tags:
  topic: ["loneliness", "measurement", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/A 6-Item Scale for Overall, Emotional, and Social Loneliness/A 6-Item Scale for Overall, Emotional, and Social Loneliness.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/A 6-Item Scale for Overall, Emotional, and Social Loneliness.pdf"
  notes: null

---

id: "obrien-2007-a-caution-regarding-rules-of-thumb"
title: "A Caution Regarding Rules of Thumb for Variance Inflation Factors"
authors:
  - "O’brien, Robert M."
year: 2007
doi: "10.1007/s11135-006-9018-6"
venue: {type: "journal", name: "Quality &amp; Quantity", volume: 41, issue: 5, pages: "673-690"}
citation: "O’brien (2007). A Caution Regarding Rules of Thumb for Variance Inflation Factors. Quality &amp; Quantity, 41(5), 673-690. https://doi.org/10.1007/s11135-006-9018-6"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  O'Brien argues that popular rules of thumb for the Variance Inflation Factor (VIF of 4 or
  10) misidentify 'serious' multi-collinearity because they ignore other factors that
  jointly determine the variance of a regression coefficient: the variance explained in the
  dependent variable (R2y), sample size, and the variance of the predictor itself. Using
  algebraic derivation and hypothetical comparison scenarios, the paper shows that
  regression coefficients with VIF values of 20 or 40 can be more precisely estimated
  (larger t-values, narrower confidence intervals) than a baseline model with a low VIF of
  1.25, once R2y and n are taken into account. It concludes that automatically dropping
  variables, combining them into indices, or using ridge regression solely because VIF
  exceeds a threshold can do more harm than the collinearity itself, unless motivated by
  theory.
claims:
  - text: "In an illustrative comparison, a regression coefficient with VIF = 40, R2y = 0.95, and n = 1,585 had a t-value of 7.35, versus t = 3.00 for a baseline model with VIF = 1.25, R2y = 0.40, and n = 100 -- i.e., the model with far higher VIF produced a more precisely estimated, more statistically significant coefficient."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["multicollinearity", "sample-size", "variance-explained"]
  - text: "Widely cited VIF thresholds (rule of 4 or rule of 10, e.g., from Menard 1995, Neter et al. 1989, Hair et al. 1995, and Marquardt 1970) are used in practice as blanket indicators of 'serious' multi-collinearity without regard to sample size, the variance explained by the model, or the variance of the predictor of interest, leading researchers and reviewers to question results that are statistically solid."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["multicollinearity"]
  - text: "Common remedies for high VIF -- dropping a correlated independent variable, combining variables into a single index, or applying ridge regression -- can introduce specification error or biased estimates unless theoretically motivated, because dropping a variable changes what the remaining coefficient actually represents (no longer controlling for the dropped variable)."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["statistical-inference"]
    predictors: ["model-specification"]
population:
  who: "Not an empirical study of human subjects; a mathematical/analytical demonstration using hypothetical baseline and comparison OLS regression scenarios (Table I) aimed at social-science researchers who use multiple regression"
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No sample; illustrative numerical scenarios (R2i, R2y, n, VIF combinations) are
    constructed to demonstrate algebraic relationships, not drawn from real data.
limitation:
  primary: "The paper is a purely analytical demonstration using hypothetical baseline and comparison regression scenarios rather than empirical data, so how well its illustrative parameter combinations match any given real-world analysis is left to the reader to judge."
  others:
    - "Addresses only ordinary least squares linear regression; does not extend the argument to logistic, multilevel, or other regression frameworks common in social/organizational research."
    - "Assumes correctly specified models and unbiased estimators; does not address interactions between collinearity and omitted-variable bias or measurement error."
risk_of_bias: "not-applicable"
relevance_to_project: >
  SNH survey-based regression models often include correlated predictors (e.g., workload,
  isolation, social support, technostress) that can produce high VIF values; this paper is a
  methodological reference cautioning the project against automatically dropping, combining,
  or ridge-regressing such predictors based on VIF thresholds alone, and instead
  interpreting collinearity diagnostics jointly with sample size and model R2 when analyzing
  SNH survey data.
tags:
  topic: ["methodology", "measurement"]
  method: ["analytical"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/A Caution Regarding Rules of Thumb for Variance Inflation Factors/A Caution Regarding Rules of Thumb for Variance Inflation Factors.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/A Caution Regarding Rules of Thumb for Variance Inflation Factors.pdf"
  notes: null

---

id: "grenny-2017-a-study-of-1-100-employees"
title: "A Study of 1,100 Employees Found That Remote Workers Feel Shunned and Left Out"
authors:
  - "Grenny, Joseph"
  - "Maxfield, David"
year: 2017
doi: null
venue: {type: "other", name: "Harvard Business Review", volume: null, issue: null, pages: null}
citation: "Grenny et al. (2017). A Study of 1,100 Employees Found That Remote Workers Feel Shunned and Left Out. Harvard Business Review."
article_type: "empirical"
method: {design: "cross-sectional-survey", approach: "survey", evidence_level: "low", preregistered: false}
gist: >
  Reporting on an original poll of 1,153 employees (52% working from home at least some of
  the time), this HBR practitioner article finds that remote workers are more likely than
  on-site colleagues to feel left out, mistreated, and undermined by coworkers, and that
  workplace conflicts they experience drag on longer and hit productivity, costs, deadlines,
  morale, stress, and retention harder. Drawing on over 800 open-ended responses, the
  authors distill seven practices used by managers who are especially good at keeping remote
  employees connected and trusted.
claims:
  - text: "Remote employees are more likely than on-site colleagues to feel that coworkers say bad things behind their backs, make changes to projects without telling them, lobby against them, or fail to fight for their priorities."
    evidence: "Survey of 1,153 employees comparing remote vs. on-site respondents' perceptions of being excluded or mistreated."
    support_strength: "weak"
    outcomes: ["isolation"]
    predictors: ["remote-work-intensity"]
  - text: "Among remote team members who encountered a common workplace conflict, 84% said the concern dragged on for a few days or more, and 47% said it dragged on for weeks or more."
    evidence: "Self-reported conflict-resolution timelines from the same survey sample."
    support_strength: "weak"
    outcomes: ["collaboration"]
    predictors: ["remote-work-intensity"]
  - text: "From open-ended responses of over 800 informants describing managers especially good at leading remote teams, the authors identify seven recurring practices, the most common being frequent, consistent check-ins (cited by 46% of respondents) and insisting on face-to-face or voice-to-voice contact (cited by 25%)."
    evidence: "Qualitative coding of open-text survey responses into best-practice categories with reported endorsement percentages."
    support_strength: "weak"
    outcomes: ["communication"]
    predictors: ["leadership-style"]
population:
  who: "Employees polled about remote and on-site work experiences, plus open-ended nominations of effective remote-team managers"
  where: []
  when: "2017"
  n: 1153
  sector: ["mixed/unspecified"]
  sample_notes: >
    Survey fielded by VitalSmarts (Grenny and Maxfield's firm); no methodology detail
    (sampling frame, response rate, statistical tests) is reported in this practitioner
    summary.
limitation:
  primary: "No peer review or methodological transparency: the article omits sampling method, response rate, statistical significance testing, and full survey instrument, and best-practice percentages come from self-reported nominations rather than controlled comparison."
  others:
    - "Cross-sectional self-report data cannot establish causality between remote status and feeling excluded."
    - "Conducted by a corporate training vendor (VitalSmarts) with a commercial interest in remote-team leadership training."
risk_of_bias: "high"
relevance_to_project: >
  Directly evidences the SNH project's core concern that remote work intensity predicts
  feelings of exclusion and slower-resolving interpersonal conflict, and offers a
  practitioner-derived set of manager behaviors (frequent check-ins, face-time, explicit
  expectations, availability, relationship-building) that map to social-support and
  inclusiveness interventions.
tags:
  topic: ["remote-work", "isolation", "collaboration"]
  method: ["survey"]
  population: ["knowledge-workers", "remote-teams"]
source:
  markdown: "Papers_Data/Remote Workers/MD/A Study of 1100 Employees Found That Remote Workers Feel Shunned and Left Out - HBR 2017/A Study of 1100 Employees Found That Remote Workers Feel Shunned and Left Out - HBR 2017.md"
  pdf: "papers/Remote Workers/A Study of 1100 Employees Found That Remote Workers Feel Shunned and Left Out - HBR 2017.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "mohd-2024-a-study-on-remote-working-of"
title: "A Study on Remote Working of Employee Motivation and Productivity"
authors:
  - "Mohd Safri, Shahrizal"
  - "Azizi Salleh, Muhammad Amiruddin"
  - "Mohd Salleh, Muhammad Syafiq"
year: 2024
doi: "10.6007/ijarbss/v14-i8/21645"
venue: {type: "journal", name: "International Journal of Academic Research in Business and Social Sciences", volume: 14, issue: 8, pages: null}
citation: "Mohd Safri et al. (2024). A Study on Remote Working of Employee Motivation and Productivity. International Journal of Academic Research in Business and Social Sciences, 14(8). https://doi.org/10.6007/ijarbss/v14-i8/21645"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  A survey of 101 Malaysian employees, interns, freelancers, and fresh graduates finds that
  those with remote-work experience report significantly higher motivation and productivity
  than those without, and situates this within Self-Determination Theory (autonomy, work-
  life balance) as the mechanism. A companion literature synthesis catalogs remote work's
  double-edged effects: gains in autonomy, cost savings, and reduced social anxiety, offset
  by physical-health strain, home-energy costs, and technical/cybersecurity friction (VPN,
  Wi-Fi, background noise) that the authors argue erode motivation and productivity.
claims:
  - text: "Employees who had prior remote-work experience reported significantly higher motivation (M=4.11, SD=0.54) than those without such experience (M=3.73, SD=0.61); independent-samples t(98)=3.14, p=.00."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["job-engagement", "job-satisfaction"]
    predictors: ["remote-work-intensity", "autonomy"]
  - text: "Employees with remote-work experience reported significantly higher self-rated productivity (M=4.07, SD=0.60) than those without (M=3.79, SD=0.63); t(98)=2.09, p=.04, supporting the study's hypothesis of a significant remote-work/productivity correlation."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Narrative synthesis reports remote work as double-edged: autonomy and eliminated commuting free up roughly one extra hour daily and reduce social anxiety for some workers, while a Nexthink survey cited found 38% of remote employees had VPN access problems, 37% Wi-Fi issues, and a noise study found 42% experienced excessive ambient noise during virtual meetings, both linked to added stress and reduced focus."
    evidence: "review-scoping"
    support_strength: "weak"
    outcomes: ["stress", "wellbeing", "technostress"]
    predictors: ["autonomy", "technostress", "work-life-balance"]
population:
  who: "101 employees, interns, freelancers, and fresh graduates across various business sectors, individually surveyed about their perceptions and experiences of remote work"
  where: ["Malaysia"]
  when: null
  n: 101
  sector: ["mixed-sectors"]
  sample_notes: >
    Respondents recruited via the authors' professional networks, relatives, and friends and
    reached through social media, course networking platforms, and personal messages;
    described as 'simple random sampling' but is functionally a convenience/snowball sample.
    Response rate not reported; only 4-item scales used for motivation and productivity
    (alpha=.76 and .81 respectively).
limitation:
  primary: "Cross-sectional, self-report design with a small convenience sample (n=101) recruited through personal networks precludes causal inference and limits generalizability despite being labeled random sampling."
  others:
    - "Motivation and productivity measured with short 4-item, non-validated scales rather than established psychometric instruments."
    - "The literature review draws on a wide mix of peer-reviewed studies, trade press, and unrelated theoretical sources (e.g., Strength of Weak Ties, McKinsey explainers) without critical appraisal of source quality or relevance."
    - "No control for confounding variables (e.g., job role, tenure, household composition) in the motivation/productivity comparisons."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a small primary-data data point (t-tests, n=101) that remote-work experience
  correlates with higher self-reported motivation and productivity, and links this to
  autonomy and work-life balance per Self-Determination Theory -- useful corroborating
  evidence for SNH's autonomy/boundary-management design levers, though its convenience
  sample and thin literature synthesis mean it should be weighted as low-to-moderate
  evidence rather than a primary source.
tags:
  topic: ["remote-work", "work-life-balance", "technostress", "wellbeing", "job-engagement"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/A Study on Remote Working of Employee Motivation and Productivity/A Study on Remote Working of Employee Motivation and Productivity.md"
  pdf: "papers/Remote Workers/A Study on Remote Working of Employee Motivation and Productivity.pdf"
  notes: null

---

id: "ab-2017-discriminant-validity-assessment-use-of-fornell"
title: "Discriminant Validity Assessment: Use of Fornell &amp; Larcker criterion versus HTMT Criterion"
authors:
  - "Ab Hamid, M R"
  - "Sami, W"
  - "Mohmad Sidek, M H"
year: 2017
doi: "10.1088/1742-6596/890/1/012163"
venue: {type: "journal", name: "Journal of Physics: Conference Series", volume: 890, issue: null, pages: "012163"}
citation: "Ab Hamid et al. (2017). Discriminant Validity Assessment: Use of Fornell &amp; Larcker criterion versus HTMT Criterion. Journal of Physics: Conference Series, 890, 012163. https://doi.org/10.1088/1742-6596/890/1/012163"
article_type: "methods"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "low", preregistered: false}
gist: >
  This paper re-analyzes a 429-respondent PLS-SEM dataset (six latent constructs:
  leadership, culture, productivity, employee, stakeholder, university performance) to
  compare two discriminant-validity tests. The Fornell-Larcker criterion judged all six
  constructs acceptably discriminant, but the newer, more conservative heterotrait-monotrait
  (HTMT) ratio flagged 8 of 15 construct pairs as problematic, revealing multicollinearity
  the older test missed. The authors argue HTMT should be the preferred criterion for
  validating reflective measurement models in survey-based SEM research.
claims:
  - text: "Using the Fornell-Larcker criterion, all six latent constructs (leadership, culture, productivity, employee, stakeholder, university performance) showed acceptable discriminant validity, with only two near-threshold violations: productivity-employee (difference of 0.009) and productivity-stakeholder (difference of 0.007), both judged negligible."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
  - text: "Applying the HTMT0.85 criterion to the same dataset flagged 8 of the 15 construct pairs (e.g., culture-productivity, culture-employee, culture-stakeholder, productivity-employee, productivity-stakeholder, productivity-university performance, employee-stakeholder, stakeholder-university performance) as lacking discriminant validity, indicating multicollinearity that the Fornell-Larcker test failed to detect."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
  - text: "The authors conclude that HTMT is a stricter and more sensitive test than either Fornell-Larcker or cross-loading assessment, and that the six-construct survey instrument used in this study needs to be revised and re-evaluated because it did not meet the more conservative HTMT standard."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["discriminant-validity"]
    predictors: ["sampling-method"]
population:
  who: "429 respondents from a prior survey used to empirically validate a value-based excellence model for higher education institutions (HEIs), originally collected by Ab Hamid (2012) and reused here for a methods demonstration."
  where: ["Malaysia"]
  when: "2012 (original data collection); reanalyzed 2017"
  n: 429
  sector: ["higher-education"]
  sample_notes: >
    Data reused from a prior doctoral/empirical study of leadership, culture, productivity,
    employee, stakeholder, and university-performance constructs in Malaysian HEIs; no
    missing data reported, but this article gives no information on the original sampling
    method or response rate.
limitation:
  primary: "The comparison of validity criteria rests on a single reused dataset from one higher-education context, so it cannot establish how often Fornell-Larcker and HTMT would diverge across other populations, sectors, or measurement models."
  others:
    - "No information is given in this article about the original sampling method, response rate, or representativeness of the 429 respondents."
    - "The paper only tests one HTMT threshold (0.85) without robustness checks against the alternative 0.90 threshold it mentions."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a technical methods reference on assessing discriminant validity in PLS-SEM survey
  instruments, not a substantive SNH finding; it is relevant if the project validates its
  own latent-construct measures (e.g., belonging, isolation, burnout scales) via reflective
  PLS-SEM models, since it warns that the commonly used Fornell-Larcker criterion can pass
  constructs that a stricter HTMT test flags as insufficiently distinct.
tags:
  topic: ["methodology", "measurement"]
  method: ["survey", "secondary-data"]
  population: ["higher-education"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Ab Hamid et al. (2017) - Discriminant Validity Assessment - Use of Fornell & Larcker Criterion versus HTMT Criterion.pdf"
  notes: null

---

id: "allen-2015-how-effective-is-telecommuting-assessing-the"
title: "How Effective Is Telecommuting? Assessing the Status of Our Scientific Findings"
authors:
  - "Allen, Tammy D."
  - "Golden, Timothy D."
  - "Shockley, Kristen M."
year: 2015
doi: "10.1177/1529100615593273"
venue: {type: "journal", name: "Psychological Science in the Public Interest", volume: 16, issue: 2, pages: "40-68"}
citation: "Allen et al. (2015). How Effective Is Telecommuting? Assessing the Status of Our Scientific Findings. Psychological Science in the Public Interest, 16(2), 40-68. https://doi.org/10.1177/1529100615593273"
article_type: "review"
method: {design: "review-narrative", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  This landmark narrative review synthesizes several decades of quantitative and qualitative
  telecommuting research, showing that most effects on job attitudes and performance are
  real but small and moderated by the amount of time spent working remotely: job
  satisfaction and coworker relationship quality follow a curvilinear pattern that turns
  negative at high telecommuting intensity, while professional and social isolation
  (reported by 62% of teleworkers in a 24-country poll) is a recurring cost linked to
  reduced job performance and higher turnover intent among heavy telecommuters. The authors
  argue that the dominant cross-sectional, single-source study designs in this literature
  preclude firm causal conclusions and that 'dosage' (extent of telecommuting) is the single
  most important, underused variable for interpreting mixed findings. For the SNH project,
  it offers a well-cited, effect-size-anchored map of where remote-work intensity trades off
  social connection against individual-level benefits.
claims:
  - text: "The relationship between telecommuting intensity and job satisfaction is curvilinear -- satisfaction rises with telecommuting up to roughly 15.1 hours per week and then plateaus -- and high-intensity telecommuting (2.5+ days/week) is meta-analytically associated with worse coworker relationship quality (r = -.19, 95% CI [-.30, -.08]) versus no effect under low-intensity arrangements (r = .03, 95% CI [.01, .07])."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "collaboration"]
    predictors: ["remote-work-intensity"]
  - text: "In an online poll of 11,383 workers across 24 countries, 62% reported that telecommuting was socially isolating and 50% feared it could harm their promotion chances; professional isolation among telecommuters is linked in primary studies to poorer job performance and greater turnover intentions, with the performance penalty stronger among those who telecommute more extensively."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "performance", "turnover"]
    predictors: ["remote-work-intensity", "isolation"]
  - text: "Across multiple meta-analyses, telecommuting status shows small but statistically reliable associations with outcomes: higher job satisfaction (r = .09), lower work-role stress (r = -.11), lower turnover intentions (r = -.08), and higher supervisor-rated (but not self-rated) job performance (r = .18 vs. r = .01), alongside a small negative association with work interfering with family (r = -.08 to -.16 depending on the meta-analysis)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress", "turnover", "performance"]
    predictors: ["remote-work-intensity"]
population:
  who: "Not a primary study: a narrative synthesis of empirical and meta-analytic telecommuting/telework research spanning psychology, management, information systems, transportation, and communication literatures, covering individual employees, supervisors, and firm-level samples."
  where: ["United States", "multiple countries (global polls and international meta-analyses)"]
  when: "Literature reviewed through 2015"
  n: null
  sector: ["general-workforce"]
  sample_notes: >
    Synthesizes dozens of primary studies and several meta-analyses of widely varying
    quality; underlying designs are overwhelmingly cross-sectional and single-source,
    definitions of 'telecommuting' vary across studies, and only two known field experiments
    exist, limiting causal inference throughout the base literature.
limitation:
  primary: "Most of the underlying primary literature the review synthesizes is cross-sectional and single-source, so the associations it reports between telecommuting and outcomes like satisfaction, performance, isolation, and turnover cannot support strong causal claims."
  others:
    - "Inconsistent, non-standardized definitions and operationalizations of telecommuting across the reviewed studies limit comparability of findings."
    - "Very few experimental or longitudinal studies exist (only two known field experiments), so dosage and directionality effects remain uncertain."
    - "The authors note research on telecommuting's effects on societal/community ties, health behaviors, and knowledge sharing is sparse or underexamined."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's core tension between remote-work flexibility and social
  connection: it quantifies how telecommuting intensity, not telecommuting per se, drives
  isolation, degraded coworker relationships, and knowledge-sharing loss, and proposes a
  moderate-telecommuting 'sweet spot' plus technology/policy levers (socially rich
  communication tools, structured face-to-face touchpoints, supervisor support) the project
  can use when designing interventions that balance flexibility with belonging.
tags:
  topic: ["remote-work", "isolation", "job-satisfaction", "collaboration", "work-life-balance"]
  method: ["secondary-data", "review-narrative"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Allen et al. (2015) - How Effective is Telecommuting - Assessing the Status of Our Scientific Findings/Allen et al. (2015) - How Effective is Telecommuting - Assessing the Status of Our Scientific Findings.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Allen et al. (2015) - How Effective is Telecommuting - Assessing the Status of Our Scientific Findings.pdf"
  notes: null

---

id: "herbsleb-2003-an-empirical-study-of-speed-and"
title: "An empirical study of speed and communication in globally distributed software development"
authors:
  - "Herbsleb, J.D."
  - "Mockus, A."
year: 2003
doi: "10.1109/tse.2003.1205177"
venue: {type: "journal", name: "IEEE Transactions on Software Engineering", volume: 29, issue: 6, pages: "481-494"}
citation: "Herbsleb et al. (2003). An empirical study of speed and communication in globally distributed software development. IEEE Transactions on Software Engineering, 29(6), 481-494. https://doi.org/10.1109/tse.2003.1205177"
article_type: "empirical"
method: {design: "mixed-methods", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Herbsleb and Mockus analyze change-management data and two employee surveys from two
  geographically distributed telecommunications software departments to explain why cross-
  site work takes longer. Distributed modification requests took about 2.5 times as long to
  complete as same-site ones in both departments, and statistical (graphical) modeling
  showed this delay was not explained by task size or complexity but was mediated almost
  entirely by the larger number of people distributed tasks required. Survey data further
  show that distributed social networks are smaller, communicate less frequently, are harder
  to navigate to find expertise, and feel less like a cohesive 'team' than co-located
  networks, and the paper argues these network deficiencies are the mechanism that pulls
  extra people into distributed work and thereby causes delay.
claims:
  - text: "Distributed modification requests (MRs) took about 2.5 times as long to complete as same-site MRs in both organizations studied: Department A averaged 5 days (single-site) vs 12.7 days (distributed, p<0.001); Department B averaged 7 days vs 18 days (p<0.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "productivity"]
    predictors: ["network-structure", "remote-work-intensity"]
  - text: "In multiple regression and graphical (covariance-selection) models, the number of people involved in an MR was the strongest and most consistent predictor of completion interval, and the distributed/same-site variable had no significant direct effect on interval once other factors were controlled -- distributed work increased delay only indirectly, by requiring more people."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "productivity"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Survey data (Department A, n=92-98, response rates 60-83%) showed distributed social networks were smaller (mean 4.9-4.8 remote contacts vs 16.0-7.6 local, p<.0001), communicated far less frequently, and were rated significantly harder to identify/contact experts within than local networks; workers also reported significantly less 'team' feeling and less help received (though not less help given) from remote vs local colleagues (p<.0001), while perceived disagreement about task priorities did not differ by site (not significant)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "sense-of-belonging", "communication"]
    predictors: ["network-structure", "team-cohesion", "social-support"]
population:
  who: "Software engineers and managers in two distributed telecommunications departments of a single company: Department A (UK, Germany, two India sites, ~40-75 people/site) and Department B (Midwestern US and Ireland, ~30-60 people/site); MR analysis covers 2,227 (Dept A) and 4,974 (Dept B) modification requests over 2.5-3.5 years; survey analysis covers Department A only (98 of 117 invited in 1998, 83% response; 96 of 160 invited in 1999, 60% response)."
  where: ["United Kingdom", "Germany", "India", "United States", "Ireland"]
  when: "July 1997 to July 1999 (change data); surveys administered November 1998 and June 1999"
  n: 96
  sector: ["technology", "software-industry"]
  sample_notes: >
    Two-organization replication design strengthens generalizability of the MR-interval
    finding, but survey data come only from Department A (Department B could not be surveyed
    due to organizational changes), and all data are from a single company in the telecom
    software domain.
limitation:
  primary: "The proposed causal mechanisms linking specific social-network deficiencies (H1-H5) to the need for more people on distributed MRs are explicitly labeled speculative by the authors -- the survey supports the existence of network differences, but the paper does not directly test that these differences cause the added-people effect."
  others:
    - "Single-company, single-industry (telecom software) setting limits generalizability to other organizational or distributed-work arrangements (e.g., outsourcing)."
    - "Confounding factors such as cultural background, language, and differing site histories could explain reduced 'teamness' and communication differences instead of (or in addition to) geographic distribution per se."
    - "CM system data only capture people who formally opened MRs or committed code deltas, undercounting informal help such as advice-giving that does not leave a system trace."
risk_of_bias: "low"
relevance_to_project: >
  Provides a rigorously replicated, quantitative mechanism -- smaller, less frequent,
  harder-to-navigate distributed social networks force more people into a task, which drives
  delay -- directly relevant to designing SNH interventions (e.g., expertise-finding tools,
  presence/awareness features, liaison roles) intended to substitute for the informal, co-
  located communication that remote and distributed teams lack. Also offers a validated
  survey instrument (network size, communication frequency, teamness/help items) usable to
  measure social network health in distributed teams.
tags:
  topic: ["remote-work", "collaboration", "productivity", "community-health"]
  method: ["mixed-methods", "secondary-data", "survey"]
  population: ["software-engineers", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/An_empirical_study_of_speed_and_communication_in_globally_distributed_software_development.pdf"
  notes: null

---

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

---

id: "appley-1977-beyond-culture"
title: "Beyond Culture"
authors:
  - "Appley, Dee G."
year: 1977
doi: "10.1177/002188637701300414"
venue: {type: "journal", name: "The Journal of Applied Behavioral Science", volume: 13, issue: 4, pages: "579-581"}
citation: "Appley (1977). Beyond Culture. The Journal of Applied Behavioral Science, 13(4), 579-581. https://doi.org/10.1177/002188637701300414"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  This is a book review (from a 'From the Bookshelf' review section) of Edward T. Hall's
  1977 anthropology book Beyond Culture. The reviewer, Dee G. Appley, summarizes Hall's
  arguments about high-context vs. low-context cultures, monochronic vs. polychronic time,
  the largely unconscious nature of cultural conditioning, and his critique of Western
  education and bureaucratic organization as incompatible with evolved human needs for
  small-group, peer-based learning. It contributes an anthropological, non-empirical
  touchstone (e.g., an ideal group size of eight to twelve) rather than any tested finding.
claims:
  - text: "Hall argues, from tracing human ancestry and primate behavior, that the ideal group size for learning and social cohesion is eight to twelve people, and that most modern educational and organizational structures violate this natural limit."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["collaboration", "sense-of-belonging"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Hall distinguishes high-context (HC) and low-context (LC) cultures, arguing that mismatched monochronic vs. polychronic time-space frames of reference between cultures produce systematic intercultural misunderstandings."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["communication"]
    predictors: ["organizational-culture"]
  - text: "Hall asserts that unconscious cultural 'binds' and action chains outnumber conscious ones by roughly 1000 to 1, so most of the behavior driving cross-cultural friction operates below awareness and typically requires outside help to surface."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["communication"]
    predictors: ["organizational-culture"]
population:
  who: "Not a study of human subjects; this is a review essay about a trade/academic book (Beyond Culture) drawing on the author Edward T. Hall's career as a cultural anthropologist observing cross-cultural and organizational settings."
  where: []
  when: "1977"
  n: null
  sector: ["academic"]
  sample_notes: >
    No sample, data collection, or methodology beyond the reviewer's reading and synthesis
    of Hall's book; the book itself is described as a mix of anecdote and assertion rather
    than reported data.
limitation:
  primary: "The source is a book review of a non-empirical, anecdote- and assertion-based anthropology book; it relays Hall's claims (e.g., ideal group size, HC/LC culture, the 1000-to-1 unconscious ratio) without any data, sample, or verifiable methodology."
  others:
    - "The review reflects one reviewer's interpretive framing of Hall's arguments, not an independent evaluation of evidence"
    - "Published in 1977; the cultural and organizational concepts are not tested against contemporary remote-work or digital-community contexts"
risk_of_bias: "high"
relevance_to_project: >
  Hall's oft-cited claim (relayed here) that the ideal group size for cohesion and peer
  learning is eight to twelve people, and his critique of bureaucratic structures as
  antithetical to human social needs, are anthropological touchstones relevant to SNH team-
  size and community-structure design choices, but the project should treat them as
  theoretical priors rather than empirical evidence.
tags:
  topic: ["collaboration", "community-health"]
  method: ["theory"]
  population: ["organizational-settings", "cross-cultural"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Appley (1977) - Review of Beyond Culture by Edward T. Hall/Appley (1977) - Review of Beyond Culture by Edward T. Hall.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Appley (1977) - Review of Beyond Culture by Edward T. Hall.pdf"
  notes: null

---

id: "argote-2000-knowledge-transfer-a-basis-for-competitive"
title: "Knowledge Transfer: A Basis for Competitive Advantage in Firms"
authors:
  - "Argote, Linda"
  - "Ingram, Paul"
year: 2000
doi: "10.1006/obhd.2000.2893"
venue: {type: "journal", name: "Organizational Behavior and Human Decision Processes", volume: 82, issue: 1, pages: "150-169"}
citation: "Argote et al. (2000). Knowledge Transfer: A Basis for Competitive Advantage in Firms. Organizational Behavior and Human Decision Processes, 82(1), 150-169. https://doi.org/10.1006/obhd.2000.2893"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This concluding article of a special issue proposes a 'knowledge reservoirs' framework in
  which organizational knowledge is embedded in members, tools, and tasks and in the
  subnetworks formed by combining them (e.g., member-member, member-task, member-tool).
  Synthesizing empirical studies of firms, franchises, and lab groups, the authors argue
  that interactions among people are the hardest knowledge to transfer to a new context
  because people vary more across sites than tools or tasks do, whereas knowledge embedded
  in tools and task sequences transfers relatively quickly. Because people are more similar
  within than between organizations, this makes knowledge embedded in people-involving
  subnetworks a durable source of competitive advantage: it transfers internally but resists
  leaking to competitors.
claims:
  - text: "In a manufacturing plant that added a second shift staffed mostly by new members using the same tools and task sequences as the first shift, the second shift reached a productivity level in a couple of weeks that had taken the first shift many months to achieve, because knowledge was embedded in the task-tool network rather than in individuals (Epple, Argote, & Murphy, 1996)."
    evidence: "case-study"
    support_strength: "moderate"
    outcomes: ["productivity", "collaboration"]
    predictors: ["network-structure"]
  - text: "Transactive memory systems (shared knowledge of 'who knows what') developed by one group did not transfer when a different set of members was substituted in; membership change was harmful when the new member's skills did not fit the existing member-task and member-tool network, and imposing a division of labor on an already-established dyad hurt its performance while the same imposition improved performance in a newly formed dyad (Moreland, Argote, & Krishnan, 1996; Devadas & Argote, 1995; Wegner, Erber, & Raymond, 1991)."
    evidence: "experiment"
    support_strength: "moderate"
    outcomes: ["collaboration", "performance"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Knowledge transferred more readily across organizational units embedded in a shared superordinate network than across independent units: fast-food stores benefited from other stores in the same franchise but not from stores in different franchises, and hotels benefited from the experience of local hotels in the same chain but not from nonlocal hotels in the same chain (Darr, Argote, & Epple, 1995; Baum & Ingram, 1998)."
    evidence: "secondary-data"
    support_strength: "moderate"
    outcomes: ["performance", "productivity"]
    predictors: ["network-structure", "organizational-culture"]
population:
  who: "Not an original empirical sample; a theoretical synthesis drawing on findings from prior empirical studies of organizational units (manufacturing plants with shift changes, fast-food franchise stores, hotel chains, student business-simulation groups, R&D/engineering transfers, and lab-based dyads/small groups)."
  where: ["United States"]
  when: "Cites studies from roughly 1977-2000"
  n: null
  sector: ["manufacturing", "hospitality", "service", "academic-lab"]
  sample_notes: >
    No new data collected; the article organizes and reinterprets results from roughly a
    dozen previously published empirical studies (several from the same special issue)
    rather than sampling a population directly.
limitation:
  primary: "As a conceptual synthesis rather than a new empirical test, the framework is illustrated with selectively chosen supporting studies rather than being systematically or quantitatively evaluated against disconfirming evidence."
  others:
    - "Underlying studies vary widely in method, unit of analysis, and era, making the strength of evidence for any single proposition (e.g., in-group vs. between-group transfer) uneven."
    - "Focuses on firm-level, in-person, co-located knowledge transfer (plants, franchises, hotel chains) and does not address distributed or remote/virtual work contexts directly."
risk_of_bias: "not-applicable"
relevance_to_project: >
  The 'knowledge reservoirs' framework and its transactive-memory evidence (who-knows-what
  breaks down when membership/network changes) directly inform how the SNH project should
  think about onboarding and knowledge continuity in distributed/open-source teams: person-
  embedded knowledge (mentoring relationships, tacit team know-how) is the least portable
  and most vulnerable to disruption from turnover or remote fragmentation, while tool- and
  process-embedded knowledge travels more easily and could be a design lever (documentation,
  runbooks) to offset loss of in-person transactive memory.
tags:
  topic: ["collaboration", "productivity", "remote-work", "community-health"]
  method: ["theory", "literature-synthesis"]
  population: ["teams", "organizations", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Argote & Ingram (2000) - Knowledge Transfer - A Basis for Competitive Advantage in Firms/Argote & Ingram (2000) - Knowledge Transfer - A Basis for Competitive Advantage in Firms.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Argote & Ingram (2000) - Knowledge Transfer - A Basis for Competitive Advantage in Firms.pdf"
  notes: null

---

id: "ashforth-2000-all-in-a-day-s-work"
title: "All in a Day's Work: Boundaries and Micro Role Transitions"
authors:
  - "Ashforth, Blake E."
  - "Kreiner, Glen E."
  - "Fugate, Mel"
year: 2000
doi: "10.2307/259305"
venue: {type: "journal", name: "The Academy of Management Review", volume: 25, issue: 3, pages: "472"}
citation: "Ashforth et al. (2000). All in a Day's Work: Boundaries and Micro Role Transitions. The Academy of Management Review, 25(3), 472. https://doi.org/10.2307/259305"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  Ashforth, Kreiner, and Fugate develop a 'boundary theory' of everyday micro role
  transitions (e.g., the daily commute, telecommuting, moving between meetings) built around
  a segmentation-integration continuum defined by role-boundary flexibility/permeability and
  role-identity contrast. They argue that highly segmented roles reduce blurring between
  roles but make crossing boundaries more effortful (often requiring rites of passage),
  whereas highly integrated roles lower transition difficulty but increase blurring and
  vulnerability to interruptions, requiring ongoing 'boundary work' to maintain. The
  framework, illustrated repeatedly with home-based and telecommuting examples, offers a
  vocabulary for how remote/hybrid workers negotiate and defend home-work boundaries.
claims:
  - text: "Highly segmented roles (inflexible, impermeable boundaries; high contrast between role identities) reduce role blurring but increase the magnitude and difficulty of the transition itself, so crossing between segmented roles (e.g., commuting from home to work) is typically facilitated by personal or collective 'rites of passage' (Propositions 2-3)."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management"]
  - text: "Highly integrated roles (flexible, permeable boundaries; low contrast between identities) lower the magnitude of transitions but increase role blurring and susceptibility to unwanted interruptions, so the central challenge shifts from crossing boundaries to creating and maintaining them (Propositions 4-6) -- a dynamic the authors apply directly to home-based and telecommuting workers."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management", "remote-work-intensity"]
  - text: "Citing Kirchmeyer's (1995) survey of Canadian managers, the authors note that organizational practices symbolizing respect for employees' non-work lives (e.g., flexible schedules, alternative work arrangements) were positively associated with organizational commitment, while practices explicitly enforcing segmentation of work and non-work were negatively associated with commitment."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["retention", "job-satisfaction"]
    predictors: ["organizational-culture", "boundary-management"]
population:
  who: "Not an empirical study of a bounded sample; a conceptual/theoretical article illustrated throughout with secondary examples (telecommuters, home-based workers, managers, prison inmates, athletes, salespeople) drawn from prior published research and case anecdotes."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    Theoretical/conceptual paper (Academy of Management Review). No primary data collection,
    sample, or response rate; propositions are developed from and illustrated by secondary
    literature and anecdotal quotations rather than tested.
limitation:
  primary: "The propositions are entirely theoretical and, by the authors' own admission in the Future Research section, had not yet been empirically tested at time of publication."
  others:
    - "Relies heavily on illustrative anecdotes and secondary citations rather than original data, so support strength for any given proposition varies widely and is not systematically assessed."
    - "Focuses on 'micro' recurring transitions and explicitly brackets macro transitions (promotions, retirement), limiting direct generalizability to major career/role changes."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Provides the foundational segmentation-integration vocabulary (role-boundary
  flexibility/permeability, role-identity contrast, boundary work vs. rites of passage) that
  SNH can use to design and evaluate remote-worker boundary-management interventions --
  e.g., whether to help remote/hybrid workers segment (reduce blurring, add transition
  rituals) or better manage integration (reduce interruption-driven confusion) to protect
  wellbeing and work-life balance.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing"]
  method: ["theory"]
  population: ["remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Ashforth et al. (2000) - All in a Days Work - Boundaries and Micro Role Transitions/Ashforth et al. (2000) - All in a Days Work - Boundaries and Micro Role Transitions.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Ashforth et al. (2000) - All in a Days Work - Boundaries and Micro Role Transitions.pdf"
  notes: null

---

id: "baddeley-2012-working-memory-theories-models-and-controversies"
title: "Working Memory: Theories, Models, and Controversies"
authors:
  - "Baddeley, Alan"
year: 2012
doi: "10.1146/annurev-psych-120710-100422"
venue: {type: "journal", name: "Annual Review of Psychology", volume: 63, issue: 1, pages: "1-29"}
citation: "Baddeley (2012). Working Memory: Theories, Models, and Controversies. Annual Review of Psychology, 63(1), 1-29. https://doi.org/10.1146/annurev-psych-120710-100422"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Baddeley presents an autobiographical, narrative review of the development of his
  multicomponent working-memory (M-WM) model -- central executive, phonological loop, visuo-
  spatial sketchpad, and episodic buffer -- tracing it from its 1974 origins through decades
  of refinement, and weighs it against rival single-system and computational alternatives
  (Cowan's embedded-processes model, Engle's individual-differences approach, Oberauer,
  ACT-R). It reports specific quantitative results underpinning the framework, such as
  strong phonological-similarity effects on serial recall and dual-task studies showing
  working memory is distributed across subsystems rather than a single bottleneck, and
  surveys applied uses of the model, from identifying children with working-memory deficits
  to early Alzheimer's detection. For the SNH project this is background cognitive-
  psychology theory on attentional/working-memory capacity, not direct evidence about remote
  work, isolation, or wellbeing.
claims:
  - text: "In serial-recall experiments, recall accuracy was about 80% correct for phonologically dissimilar word sequences versus only about 10% correct for phonologically similar sequences, while semantic similarity produced a much smaller effect (71% vs 65% correct), supporting separate short-term phonological and long-term semantic storage systems (Baddeley 1966a,b)."
    evidence: "lab-experiment"
    support_strength: "strong"
    outcomes: ["memory-performance"]
    predictors: ["stimulus-similarity"]
  - text: "In dual-task studies, requiring participants to hold and recall spoken digit sequences while performing a concurrent grammatical-reasoning task slowed response times roughly linearly with digit-sequence length, but disruption was far from catastrophic (about 50% slowing at the heaviest load) and error rates stayed roughly constant near 5%, evidence against a single unitary short-term store and for a multicomponent working-memory system (Baddeley & Hitch 1974)."
    evidence: "lab-experiment"
    support_strength: "strong"
    outcomes: ["cognitive-performance"]
    predictors: ["cognitive-load", "attentional-capacity"]
  - text: "The multicomponent working-memory framework has been translated into practical measurement tools, including a working-memory assessment used to identify school-age children at risk of learning difficulties (Gathercole & Alloway 2008) and dual-task performance measures used for early detection of Alzheimer's disease (Kaschel et al. 2009; Logie et al. 2004)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["assessment-validity"]
    predictors: ["working-memory-capacity"]
population:
  who: "No single sample; a narrative synthesis of ~50 years of laboratory working-memory research, mostly conducted by the author's own labs, spanning healthy adults, amnesic and Korsakoff patients, school-age children, and older/Alzheimer's populations."
  where: ["United Kingdom"]
  when: null
  n: null
  sector: []
  sample_notes: >
    Not an empirical study with its own sample; it is an invited autobiographical/prefatory
    review chapter for Annual Review of Psychology, citing dozens of the author's and
    others' prior experiments rather than reporting new data collection.
limitation:
  primary: "This is a self-authored narrative history of one theoretical program rather than a systematic review; the author explicitly describes the account as 'partial, as opposed to impartial' and acknowledges omitting relevant work."
  others:
    - "No independent quantitative synthesis (e.g., meta-analysis) of the cited findings is provided"
    - "Focuses almost entirely on laboratory studies of memory and attention in general/clinical populations, not on real-world remote-work, organizational, or occupational contexts"
risk_of_bias: "high"
relevance_to_project: >
  Provides the underlying cognitive-psychology theory of working-memory/attentional capacity
  (central executive, phonological loop, visuo-spatial sketchpad, episodic buffer) that
  could ground SNH hypotheses about why frequent context-switching, notification load, and
  multitasking in remote/hybrid work tax limited attentional resources and contribute to
  technostress or cognitive fatigue, though the paper itself makes no claims about remote
  work, isolation, or wellbeing.
tags:
  topic: ["measurement", "methodology"]
  method: ["review-narrative", "theory"]
  population: ["general-population", "clinical-samples", "children", "older-adults"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Baddeley (2012) - Working Memory - Theories Models and Controversies/Baddeley (2012) - Working Memory - Theories Models and Controversies.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Baddeley (2012) - Working Memory - Theories Models and Controversies.pdf"
  notes: null

---

id: "bakker-2007-the-job-demandsresources-model-state-of"
title: "The Job Demands‐Resources model: state of the art"
authors:
  - "Bakker, Arnold B."
  - "Demerouti, Evangelia"
year: 2007
doi: "10.1108/02683940710733115"
venue: {type: "journal", name: "Journal of Managerial Psychology", volume: 22, issue: 3, pages: "309-328"}
citation: "Bakker et al. (2007). The Job Demands‐Resources model: state of the art. Journal of Managerial Psychology, 22(3), 309-328. https://doi.org/10.1108/02683940710733115"
article_type: "review"
method: {design: "review-scoping", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This state-of-the-art review lays out the Job Demands-Resources (JD-R) model, arguing that
  any job's characteristics can be sorted into demands (which drain energy and predict
  exhaustion/health problems) and resources (which fuel motivation and predict
  engagement/commitment), and that resources also buffer the harmful effect of demands on
  strain, especially when demands are high. It synthesizes results from a series of Dutch
  and Finnish organizational studies (call centers, home care, teaching, dentistry, higher
  education) showing dual pathways to burnout versus engagement and interaction effects
  between specific demands and resources. It closes with practical guidance for using the
  model diagnostically (qualitative interviews plus tailored survey) in organizational
  interventions.
claims:
  - text: "Among 1,000 employees at a large higher-education institute, the combination of high job demands (work overload, emotional demands, physical demands, work-home interference) and low job resources (autonomy, feedback, social support, quality supervisor relationship) significantly predicted burnout (exhaustion and cynicism); high resources buffered the effect of high demands."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["social-support", "autonomy", "workload"]
  - text: "In a call-center study (Bakker et al., 2003a), job demands (work pressure, computer problems, emotional demands, task changes) predicted health problems that in turn predicted sickness absence, while job resources (social support, supervisory coaching, feedback, time control) predicted dedication and organizational commitment that in turn predicted lower turnover intentions -- supporting two distinct psychological pathways."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "burnout", "job-engagement"]
    predictors: ["social-support", "workload", "leadership-style"]
  - text: "Interaction effects between demands and resources were common but not universal: a study of Finnish dentists found 17 of 40 tested demand-resource interactions (40%) were significant in boosting work engagement under high workload, while a study of Finnish teachers found 14 of 18 interactions (78%) significant, with supervisor support, innovativeness, and appreciation buffering the effect of pupil misbehavior on engagement."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "burnout"]
    predictors: ["social-support", "leadership-style", "workload"]
population:
  who: "Narrative synthesis of the author's own and colleagues' empirical JD-R studies across multiple occupational samples: call-center employees, home-care workers, nutrition-production employees, teachers, dentists, and higher-education staff."
  where: ["Netherlands", "Finland", "Sweden"]
  when: "Studies cited span roughly 2000-2006"
  n: null
  sector: ["office", "healthcare", "education", "customer-service"]
  sample_notes: >
    This is a theoretical/review paper, not a single primary study; individual studies cited
    range from small clinical/teacher samples to a 37,291-employee Dutch dataset (Van
    Veldhoven et al., 2005) and a 1,000-employee higher-education sample (Bakker et al.,
    2005). Most underlying studies rely on self-report cross-sectional or short-longitudinal
    designs from the authors' own research program, limiting independence and
    generalizability of the synthesis.
limitation:
  primary: "As the review itself acknowledges, most JD-R evidence rests on subjective self-report measures of both demands/resources and outcomes, inflating common-method-variance concerns and leaving interaction effects to be detected less consistently than main effects."
  others:
    - "The review synthesizes largely the authors' own program of studies rather than an independent or systematic literature search, so selection and confirmation bias are plausible."
    - "Most cited studies are cross-sectional; the paper notes only a handful of longitudinal or reversed-causation studies, so causal direction between demands/resources and strain/motivation remains under-tested."
risk_of_bias: "medium"
relevance_to_project: >
  The JD-R model is a core theoretical scaffold for SNH: it frames social support,
  supervisor relationship quality, and autonomy as job resources that both directly fuel
  engagement/commitment and buffer burnout under high workload, which is directly applicable
  to designing remote-work and open-source community interventions that add social-support
  and autonomy resources to offset technostress and workload-driven exhaustion.
tags:
  topic: ["burnout", "job-engagement", "wellbeing", "social-support", "psychological-safety"]
  method: ["theory", "review"]
  population: ["knowledge-workers", "service-workers", "educators"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Bakker & Demerouti (2007) - The Job Demands-Resources Model - State of the Art/Bakker & Demerouti (2007) - The Job Demands-Resources Model - State of the Art.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Bakker & Demerouti (2007) - The Job Demands-Resources Model - State of the Art.pdf"
  notes: null

---

id: "bakker-2008-work-engagement-an-emerging-concept-in"
title: "Work engagement: An emerging concept in occupational health psychology"
authors:
  - "Bakker, Arnold B."
  - "Schaufeli, Wilmar B."
  - "Leiter, Michael P."
  - "Taris, Toon W."
year: 2008
doi: "10.1080/02678370802393649"
venue: {type: "journal", name: "Work &amp; Stress", volume: 22, issue: 3, pages: "187-200"}
citation: "Bakker et al. (2008). Work engagement: An emerging concept in occupational health psychology. Work &amp; Stress, 22(3), 187-200. https://doi.org/10.1080/02678370802393649"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This position paper synthesizes the emerging literature on work engagement (vigour,
  dedication, absorption), distinguishing it from burnout and workaholism, and reviewing
  evidence that job resources (autonomy, feedback, social support) and personal resources
  (self-efficacy, optimism, resilience) predict engagement, which in turn predicts
  performance and customer outcomes. It closes with a research agenda calling for
  daily/diary designs, intervention studies, and clarity on the long-term (possibly
  negative) consequences of sustained high engagement.
claims:
  - text: "Job resources are consistently positively associated with work engagement across samples; in a study of over 2000 Finnish teachers, job control, information, supervisory support, innovative climate, and social climate all related positively to engagement, and a 1-year longitudinal study of Dutch managers found increases in social support, autonomy, learning opportunities, and feedback predicted Time 2 engagement after controlling for baseline levels."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["social-support", "autonomy", "leadership-style"]
  - text: "Job resources become more motivationally salient under high job demands: among Finnish dentists, 17 of 40 tested interactions (43%) were significant, showing skill variability boosted engagement under high workload; among Finnish teachers, 14 of 18 interactions (78%) were significant, with supervisor support and organizational climate buffering the negative effect of pupil misbehaviour on engagement."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["workload", "leadership-style", "organizational-culture"]
  - text: "Work engagement is linked to performance: engaged employees receive higher colleague ratings on in-role and extra-role performance, and a study across 100+ Spanish hotel/restaurant units found organizational resources and engagement predicted service climate, which in turn predicted employee performance and customer loyalty; a diary study in a Greek fast-food chain found daily engagement predicted daily objective financial returns."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["performance", "job-engagement"]
    predictors: ["social-support", "autonomy"]
population:
  who: "Not a primary study; synthesizes findings from multiple occupational samples including Dutch employees, Finnish teachers and dentists, South African police officers, Dutch technicians and school principals, Turkish bank managers, and Spanish/Greek hospitality workers"
  where: ["Netherlands", "Finland", "South Africa", "Turkey", "Spain", "Greece"]
  when: null
  n: null
  sector: ["education", "healthcare", "hospitality", "public-safety", "corporate", "mixed"]
  sample_notes: >
    Narrative/position paper (special issue introduction) that cites primary studies without
    a systematic search or inclusion protocol; sample sizes and designs vary widely across
    the cited studies (from qualitative interviews with 15 workers to cross-sectional
    surveys of ~2000 teachers).
limitation:
  primary: "As a narrative position paper rather than a systematic review, study selection is not protocol-driven and is authored largely by researchers (Bakker, Schaufeli) who developed the central measurement instrument (UWES), raising selection and confirmation-bias concerns."
  others:
    - "Most underlying evidence at the time was cross-sectional, limiting causal claims about job/personal resources driving engagement."
    - "The paper explicitly flags unresolved measurement debates (three-factor vs. overall UWES score; role of absorption) that limit comparability across cited studies."
    - "Almost no intervention research existed at time of writing, so claims about how to increase engagement are speculative rather than evidence-based."
risk_of_bias: "medium"
relevance_to_project: >
  This foundational review supplies the SNH project's core predictor vocabulary for
  engagement and burnout (social support, autonomy, feedback, supervisory coaching, self-
  efficacy, optimism, resilience) and the job demands-resources framing that motivates why
  remote/OSS community interventions targeting social support and autonomy should move
  engagement and, downstream, performance and retention.
tags:
  topic: ["job-engagement", "burnout", "wellbeing", "measurement"]
  method: ["review-narrative"]
  population: ["knowledge-workers", "mixed-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Bakker et al. (2008) - Work Engagement - An Emerging Concept in Occupational Health Psychology/Bakker et al. (2008) - Work Engagement - An Emerging Concept in Occupational Health Psychology.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Bakker et al. (2008) - Work Engagement - An Emerging Concept in Occupational Health Psychology.pdf"
  notes: null

---

id: "baumeister-2017-the-need-to-belong-desire-for"
title: "The Need to Belong: Desire for Interpersonal Attachments as a Fundamental Human Motivation"
authors:
  - "Baumeister, Roy F."
  - "Leary, Mark R."
year: 2017
doi: "10.4324/9781351153683-3"
venue: {type: "book", name: "Interpersonal Development", volume: null, issue: null, pages: "57-89"}
citation: "Baumeister et al. (2017). The Need to Belong: Desire for Interpersonal Attachments as a Fundamental Human Motivation. Interpersonal Development, 57-89. https://doi.org/10.4324/9781351153683-3"
article_type: "theory"
method: {design: "review-narrative", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Baumeister and Leary synthesize decades of social and personality psychology research to
  argue that a 'need to belong' -- frequent, affectively positive interaction within a
  stable, caring relational bond -- is a fundamental, largely universal human motivation on
  par with hunger. They show belongingness deprivation is linked to worse physical and
  mental health, more behavioral pathology (from eating disorders to suicide), and disrupted
  cognition and emotion, while relationships offering only interaction or only a bond
  (without both) yield merely partial satisfaction.
claims:
  - text: "Mental hospital admission rates are at least 3 and possibly up to 22 times higher among divorced people than among married people, with rates highest among divorced/separated, intermediate among never-married, and lowest among married individuals across the reviewed studies."
    evidence: "review-narrative"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health", "isolation"]
    predictors: ["social-support", "isolation"]
  - text: "Married cancer patients survived significantly better than unmarried patients even after controlling for timing of diagnosis, likelihood of receiving treatment, and smoking, and married people show consistently lower all-cause mortality (including fatal heart attacks, tuberculosis, and cancer) than divorced, single, or widowed people."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["wellbeing", "mental-health"]
    predictors: ["social-support", "isolation"]
  - text: "People who have a stable relational bond but little interaction (e.g., prisoners, commuter-marriage spouses, noncustodial parents) and people who have frequent interaction without a stable caring bond (e.g., prostitutes with clients) each report only partial satisfaction, indicating belongingness requires both frequent positive interaction and a perceived enduring bond of mutual concern."
    evidence: "review-narrative"
    support_strength: "low"
    outcomes: ["wellbeing", "loneliness"]
    predictors: ["social-support", "sense-of-belonging"]
population:
  who: "No single sample; a narrative synthesis of findings from dozens of social/personality psychology, sociology, and medical studies of the general human population (students, married couples, prisoners, combat veterans, patients, children, cult members, prostitutes, etc.)."
  where: ["United States", "mixed Western countries"]
  when: "Cited studies span roughly the 1930s through 1994"
  n: null
  sector: []
  sample_notes: >
    Narrative literature review with no independent data collection or documented systematic
    search protocol; the ~300 cited primary studies vary widely in sample size, design
    rigor, and population, and are drawn overwhelmingly from Western (mostly U.S.) contexts.
limitation:
  primary: "The authors themselves note that most of the supporting evidence is correlational rather than experimental, so causal direction (social bonds causing health/adjustment benefits versus unhealthy or maladjusted people being excluded from bonds) is frequently underdetermined."
  others:
    - "The literature search was not systematic or preregistered, creating risk of selective emphasis on confirming evidence, which the authors partly address via a dedicated counterexamples section."
    - "Evidence is drawn overwhelmingly from Western, largely U.S. samples, limiting support for the claim of cross-cultural universality."
    - "Some sub-hypotheses (e.g., the necessity of mutuality, the precise want-versus-need distinction) rest on sparse, indirect, or methodologically weak evidence by the authors' own admission."
risk_of_bias: "medium"
relevance_to_project: >
  This is the foundational theoretical grounding for treating belonging, isolation, and
  loneliness as core SNH constructs rather than secondary concerns; its two-component model
  (frequent positive interaction plus a perceived stable, mutually caring bond) directly
  informs why remote-work and open-source interventions must target relationship quality and
  continuity, not just interaction frequency, to reduce isolation and support wellbeing.
tags:
  topic: ["isolation", "loneliness", "social-support", "wellbeing", "mental-health", "community-health"]
  method: ["review-narrative", "secondary-data"]
  population: ["general-adult-population", "married-couples"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Baumeister & Leary (1995) - The Need to Belong - Desire for Interpersonal Attachments as a Fundamental Human Motivation/Baumeister & Leary (1995) - The Need to Belong - Desire for Interpersonal Attachments as a Fundamental Human Motivation.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Baumeister & Leary (1995) - The Need to Belong - Desire for Interpersonal Attachments as a Fundamental Human Motivation.pdf"
  notes: null

---

id: "bentley-2016-the-role-of-organisational-support-in"
title: "The role of organisational support in teleworker wellbeing: A socio-technical systems approach"
authors:
  - "Bentley, T.A."
  - "Teo, S.T.T."
  - "McLeod, L."
  - "Tan, F."
  - "Bosua, R."
  - "Gloet, M."
year: 2016
doi: "10.1016/j.apergo.2015.07.019"
venue: {type: "journal", name: "Applied Ergonomics", volume: 52, issue: null, pages: "207-215"}
citation: "Bentley et al. (2016). The role of organisational support in teleworker wellbeing: A socio-technical systems approach. Applied Ergonomics, 52, 207-215. https://doi.org/10.1016/j.apergo.2015.07.019"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a socio-technical systems framework, this study surveyed 804 New Zealand teleworkers
  across 28 organisations and modeled (via PLS-SEM) how organisational social support and
  teleworker-specific support relate to job satisfaction, psychological strain, and social
  isolation. Organisational social support reduced social isolation and psychological strain
  and increased job satisfaction, with social isolation partially mediating the support-
  outcome relationships; effects of organisational support on isolation and satisfaction
  were stronger for low-intensity than hybrid teleworkers, while teleworker-specific support
  did not significantly reduce isolation.
claims:
  - text: "Organisational social support was significantly related to job satisfaction (path=0.40, t=10.02, p<.001), reduced psychological strain (path=-0.28, t=6.09, p<.001), and reduced social isolation (path=-0.46, t=11.49, p<.001) in the full sample (n=804)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress", "isolation"]
    predictors: ["social-support"]
  - text: "Social isolation partially mediated the relationship between organisational social support and both job satisfaction (indirect effect=0.10, 95% CI 0.06-0.14) and psychological strain (indirect effect=0.04, 95% CI 0.03-0.06), and was itself negatively related to job satisfaction (path=-0.14) and positively related to psychological strain (path=0.20)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress", "isolation"]
    predictors: ["social-support", "isolation"]
  - text: "Teleworker-specific support (manager support, manager trust, ICT support) was positively related to job satisfaction (path=0.25, p<.001) but was not significantly related to social isolation (path=-0.02, ns), and organisational social support's effects on social isolation and job satisfaction were significantly stronger for low-intensity teleworkers (path=-0.39/0.48) than hybrid teleworkers (path=-0.60/0.23) despite the larger overall isolation-reduction effect in the hybrid subsample."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "isolation"]
    predictors: ["social-support", "remote-work-intensity"]
population:
  who: "Teleworking employees across 28 New Zealand knowledge-work organisations (financial/insurance, education, professional/technical services, media/telecom, and other sectors), split into low-intensity (1-7 hrs/week remote, n=509) and hybrid (8+ hrs/week remote, n=295) subsamples"
  where: ["New Zealand"]
  when: null
  n: 804
  sector: ["finance", "education", "technology", "public-sector", "healthcare", "other"]
  sample_notes: >
    Recruited via New Zealand Work Research Institute, HRINZ, and Cisco NZ partner networks;
    28 of 45 invited organisations agreed to participate; online survey distributed via
    employer email, so response rate among individual employees is unreported; only 6% of
    respondents teleworked more than 3 days/week, limiting power to detect effects of very
    high-intensity telework; 47% female, mean age 30.9, mostly full-time (87%) and non-
    managerial (58%).
limitation:
  primary: "Cross-sectional, correlational design means causal direction among support, social isolation, strain, and satisfaction cannot be established."
  others:
    - "Very few respondents (6%) teleworked more than 3 days/week, so the sample cannot speak to effects of high-intensity telework where negative outcomes are theorized to be strongest."
    - "Reliance on self-report perceptual measures for both predictors and outcomes raises common-method variance concerns."
    - "Informal telework arrangements (only 22% had written agreements) may limit generalizability to organisations with formalized remote-work policies."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative path-model evidence, with effect sizes, that organisational and
  supervisor social support reduces professional/social isolation among remote workers and
  that this isolation reduction is a key mechanism (partial mediator) linking support to job
  satisfaction and reduced psychological strain -- directly informing which support levers
  (peer/supervisor support vs. technical/manager-specific telework support) the SNH project
  should prioritize, and suggesting effects may differ by remote-work intensity.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "social-support", "job-satisfaction"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Bentley et al. (2016) - The Role of Organisational Support in Teleworker Wellbeing/Bentley et al. (2016) - The Role of Organisational Support in Teleworker Wellbeing.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Bentley et al. (2016) - The Role of Organisational Support in Teleworker Wellbeing.pdf"
  notes: null

---

id: "bordia-2004-uncertainty-during-organizational-change-types-consequences"
title: "Uncertainty During Organizational Change: Types, Consequences, and Management Strategies"
authors:
  - "Bordia, Prashant"
  - "Hobman, Elizabeth"
  - "Jones, Elizabeth"
  - "Gallois, Cindy"
  - "Callan, Victor J."
year: 2004
doi: "10.1023/b:jobu.0000028449.99127.f7"
venue: {type: "journal", name: "Journal of Business and Psychology", volume: 18, issue: 4, pages: "507-532"}
citation: "Bordia et al. (2004). Uncertainty During Organizational Change: Types, Consequences, and Management Strategies. Journal of Business and Psychology, 18(4), 507-532. https://doi.org/10.1023/b:jobu.0000028449.99127.f7"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using survey data from 877 employees of an Australian public-sector organization
  undergoing restructuring, this study tests a structural equation model in which job-
  related uncertainty undermines employees' sense of control, which in turn drives
  psychological strain. It finds that participation in decision-making (PDM) reduces
  structural and job-related uncertainty and boosts control, whereas top-down management
  communication (QCC) only reduces strategic-level uncertainty, suggesting participatory
  strategies are needed to address the uncertainties that matter most to individual well-
  being during change.
claims:
  - text: "Job-related uncertainty was negatively related to feelings of control, and control fully mediated the effect of uncertainty on psychological strain; job-related uncertainty (M=4.13) was significantly higher than both strategic (M=3.85, t(876)=5.79, p<.001) and structural uncertainty (M=3.35, t(876)=15.66, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "uncertainty"]
    predictors: ["autonomy", "organizational-culture"]
  - text: "In the final SEM model (N=877, good fit: CFI=.97, RMSEA=.038), participation in decision-making (PDM) was negatively related to structural and job-related uncertainty (but not strategic uncertainty), positively related to feelings of control, and negatively related to psychological strain."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "uncertainty"]
    predictors: ["autonomy", "inclusiveness"]
  - text: "Quality of change communication (QCC) was negatively related only to strategic uncertainty; contrary to predictions it had no significant relationship with structural or job-related uncertainty, indicating one-way management communication does not resolve the uncertainties most proximal to employees."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["uncertainty", "communication"]
    predictors: ["leadership-style"]
population:
  who: "Employees of an Australian state government department undergoing internal restructuring (demerger, relocation, new CEO and business strategy); surveys mailed to all 1283 staff, 877 returned (68.4% response rate), 53% female."
  where: ["Australia"]
  when: null
  n: 877
  sector: ["public-sector"]
  sample_notes: >
    Whole-organization mailed survey with a strong 68.4% response rate; however it is a
    single public-sector organization undergoing a specific type of change (demerger plus
    government transition), so generalizability of content (though not mechanism) to
    private-sector or remote-work change contexts is uncertain. A supplementary check found
    only moderate agreement (r=.38-.40) between employee-reported QCC/PDM and an independent
    HR manager's ratings across 8 work units.
limitation:
  primary: "Cross-sectional, single-timepoint survey design means the hypothesized causal ordering (uncertainty -> control -> strain) cannot be confirmed despite good SEM fit indices; the authors explicitly note causal inferences cannot be drawn."
  others:
    - "The job-related uncertainty scale had low internal consistency (alpha=.68) and was reduced to only two items in the final measurement model."
    - "Conducted in one public-sector organization, limiting generalizability of the specific change content (though the authors argue the psychological mechanism should generalize)."
    - "Self-report measures of management communication and participation showed only moderate correlation with independent manager ratings, suggesting some perceptual/common-method bias."
risk_of_bias: "medium"
relevance_to_project: >
  Offers an empirically validated mechanism -- perceived control mediating the link between
  change-related uncertainty and psychological strain -- that is directly transferable to
  SNH work on remote/hybrid transitions and organizational disruption. It also gives a
  concrete, evidence-based design lever: participatory decision-making, not top-down
  communication alone, is what reduces the job-level uncertainty and strain that most affect
  individual well-being, informing which intervention type the project should prioritize for
  uncertainty/change-related distress.
tags:
  topic: ["wellbeing", "methodology", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["public-sector", "office-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Bordia et al. (2004) - Uncertainty During Organizational Change - Types Consequences and Management Strategies/Bordia et al. (2004) - Uncertainty During Organizational Change - Types Consequences and Management Strategies.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Bordia et al. (2004) - Uncertainty During Organizational Change - Types Consequences and Management Strategies.pdf"
  notes: null

---

id: "brayfield-1951-an-index-of-job-satisfaction"
title: "An index of job satisfaction."
authors:
  - "Brayfield, Arthur H."
  - "Rothe, Harold F."
year: 1951
doi: "10.1037/h0055617"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 35, issue: 5, pages: "307-311"}
citation: "Brayfield et al. (1951). An index of job satisfaction.. Journal of Applied Psychology, 35(5), 307-311. https://doi.org/10.1037/h0055617"
article_type: "commentary"
method: {design: "review-scoping", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  This document is not the Brayfield & Rothe (1951) article itself but an annotated-
  bibliography column ('Researcher's Bookshelf') from an early-1950s nursing-service-
  administration journal, listing roughly ten personnel-management, industrial-engineering,
  and safety-research publications for nurse researchers. One two-sentence entry describes
  Brayfield & Rothe's Journal of Applied Psychology article as introducing an 18-item 'job
  satisfaction blank' that the annotator characterizes as an attitude scale of high validity
  and reliability. The rest of the column covers unrelated topics (time-and-motion study,
  accident-reduction data collection, work sampling, research administration controls) and
  contributes no primary data of its own.
claims:
  - text: "Brayfield & Rothe's (1951) 18-item 'job satisfaction blank' is described by the annotator as an attitude scale of high validity and reliability for measuring job satisfaction, though no statistics are given in this secondhand summary."
    evidence: "review-scoping"
    support_strength: "weak"
    outcomes: ["job-satisfaction"]
    predictors: ["sampling-method"]
  - text: "Barnes' Work Measurement Project is reported to have collected time-study data from roughly 5,000 workers across more than 350 industrial organizations in the US and Canada to develop productivity standards."
    evidence: "review-scoping"
    support_strength: "weak"
    outcomes: ["productivity"]
    predictors: ["workload"]
  - text: "A 'work sampling' (ratio-delay) method was applied in a State University of Iowa hospital study to determine how nursing employees allocate their time, illustrating an early productivity-measurement application in a healthcare setting."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["productivity"]
    predictors: ["workload"]
population:
  who: "A curated reading list of ~10 mid-20th-century personnel/industrial-engineering and nursing-administration publications (books, journal articles, manuals) aimed at nurse researchers and hospital administrators; not itself a study sample."
  where: ["United States"]
  when: "1946-1952"
  n: null
  sector: ["healthcare"]
  sample_notes: >
    This is an editor/librarian-curated bibliography column ('Researcher's Bookshelf'), not
    primary research; each entry is a secondhand 1-3 sentence annotation, not the full text
    of the source it describes.
limitation:
  primary: "The file is a secondhand, two-sentence bibliographic annotation of the Brayfield & Rothe scale embedded within a larger unrelated reading list, not the original 1951 article, so no methodology, item content, or validity/reliability statistics for the scale are actually reported here."
  others:
    - "The markdown conversion under this paper's folder name does not match Brayfield & Rothe's actual article text; it is a different, misfiled document (a 1950s nursing-journal bibliography column) that only briefly mentions the paper."
    - "Most of the column concerns industrial engineering, time study, and workplace-safety literature with no direct bearing on social network health constructs."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This fragment is useful only as a historical pointer confirming that Brayfield & Rothe's
  (1951) 18-item Job Satisfaction Blank was already recognized by the early 1950s as a
  validated job-satisfaction measure; since the actual article text is not present in this
  file, the SNH project should source the original Journal of Applied Psychology paper
  separately for scale items and psychometrics rather than citing this bibliography entry as
  evidence.
tags:
  topic: ["job-satisfaction", "measurement", "methodology"]
  method: ["review-scoping"]
  population: ["healthcare-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Brayfield & Rothe (1951) - An Index of Job Satisfaction/Brayfield & Rothe (1951) - An Index of Job Satisfaction.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Brayfield & Rothe (1951) - An Index of Job Satisfaction.pdf"
  notes: null

---

id: "brewer-1979-in-group-bias-in-the-minimal"
title: "In-group bias in the minimal intergroup situation: A cognitive-motivational analysis."
authors:
  - "Brewer, Marilynn B."
year: 1979
doi: "10.1037/0033-2909.86.2.307"
venue: {type: "journal", name: "Psychological Bulletin", volume: 86, issue: 2, pages: "307-324"}
citation: "Brewer (1979). In-group bias in the minimal intergroup situation: A cognitive-motivational analysis.. Psychological Bulletin, 86(2), 307-324. https://doi.org/10.1037/0033-2909.86.2.307"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Brewer's 1979 Psychological Bulletin review synthesizes roughly two decades of minimal-
  intergroup-situation experiments to show that in-group favoritism emerges from the mere
  act of categorizing people into groups, independent of competition, face-to-face
  interaction, or rational self-interest, and that the amount of bias tracks the salience of
  the group boundary rather than the content of the distinction. It also finds that bias is
  driven mainly by inflated evaluation of the in-group rather than derogation of the out-
  group, and that minority or lower-status groups display heightened in-group favoritism
  relative to majority/high-status groups.
claims:
  - text: "In-group bias is best predicted by the salience of the in-group/out-group distinction rather than by the degree of competition or interdependence per se; once category salience is established, further variation in similarity or cooperative/competitive structure adds little bias. In one cited study, mean in-group-minus-out-group evaluative rating differences rose from -1.5 at 0% in-group wins to 8.3 at 50% wins to 14.5 at 100% wins (Kahn & Ryen, 1972), showing bias tracks perceived group success once the boundary is salient."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging", "collaboration"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Across the majority of studies that reported in-group and out-group ratings separately, increases in bias were attributable to enhanced evaluation of the in-group while out-group ratings remained relatively constant, indicating in-group bias is driven more by in-group favoritism than by hostility or derogation toward the out-group."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging"]
    predictors: ["team-cohesion", "inclusiveness"]
  - text: "Minimal-group (Tajfel-type) allocation studies show reliable in-group favoritism even without face-to-face interaction, anonymity of membership, or any rational utilitarian benefit to the subject; Brewer & Silver (1978) found a majority of subjects chose point distributions that maximized the in-group member's relative gain over the out-group member even when this reduced the in-group member's own absolute payoff."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["collaboration", "sense-of-belonging"]
    predictors: ["network-structure", "team-cohesion"]
population:
  who: "Not a single sample: a narrative review of roughly 40 experimental social-psychology studies (mostly 1960s-1978) on intergroup differentiation, using primarily college-age or adult laboratory groups, plus one field experiment with 11-year-old boys (Sherif's Robbers Cave) and a large-scale ethnic-attitude survey."
  where: ["United States", "United Kingdom", "Europe", "East Africa"]
  when: "circa 1960-1978"
  n: null
  sector: []
  sample_notes: >
    Aggregates dozens of independent lab experiments (typically small groups of N=2-8
    members per condition, often college students or schoolchildren) plus a handful of
    field/survey studies; no single sample size applies to the review as a whole, and it is
    a narrative rather than meta-analytic synthesis.
limitation:
  primary: "The reviewed evidence base relies overwhelmingly on artificial, short-duration laboratory groups (often college students or schoolchildren) with trivial, randomly assigned, or arbitrary group memberships, limiting generalizability to enduring real-world organizational or remote-work teams."
  others:
    - "Narrative rather than systematic or meta-analytic synthesis, so study selection, weighting, and effect-size pooling are not fully transparent or reproducible."
    - "Many source studies report only net in-group-minus-out-group difference scores, obscuring whether effects stem from in-group enhancement, out-group derogation, or both."
    - "Findings are drawn mostly from Western (US/UK/European) undergraduate and laboratory populations, with limited field or cross-cultural validation beyond one East African ethnocentrism survey."
risk_of_bias: "medium"
relevance_to_project: >
  Supplies the classic cognitive-motivational mechanism -- categorization salience, not
  competition or interaction -- behind in-group cohesion and out-group distancing, directly
  relevant to designing distributed/remote sub-team and community boundaries so that
  beneficial in-group belonging and cohesion are preserved while destructive out-group bias
  between teams, orgs, or contributor factions is minimized.
tags:
  topic: ["collaboration", "community-health", "measurement", "methodology"]
  method: ["review-narrative"]
  population: ["laboratory-groups", "college-students", "cross-cultural"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Brewer (1979) - In-Group Bias in the Minimal Intergroup Situation - A Cognitive-Motivational Analysis/Brewer (1979) - In-Group Bias in the Minimal Intergroup Situation - A Cognitive-Motivational Analysis.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Brewer (1979) - In-Group Bias in the Minimal Intergroup Situation - A Cognitive-Motivational Analysis.pdf"
  notes: null

---

id: "brooks-2020-the-psychological-impact-of-quarantine-and"
title: "The Psychological Impact of Quarantine and How to Reduce It: Rapid Review of the Evidence"
authors:
  - "Brooks, Samantha K."
  - "Webster, Rebecca K."
  - "Smith, Louise E."
  - "Woodland, Lisa"
  - "Wessely, Simon"
  - "Greenberg, Neil"
  - "Rubin, G. James"
year: 2020
doi: "10.2139/ssrn.3532534"
venue: {type: "journal", name: "SSRN Electronic Journal", volume: null, issue: null, pages: null}
citation: "Brooks et al. (2020). The Psychological Impact of Quarantine and How to Reduce It: Rapid Review of the Evidence. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3532534"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This rapid review synthesizes 24 studies (across ten countries, spanning SARS, Ebola,
  H1N1, MERS, and equine influenza outbreaks) on the psychological impact of quarantine,
  finding consistently negative effects including post-traumatic stress symptoms, confusion,
  anger, and stigma, some persisting years afterward. The authors identify longer quarantine
  duration, infection fears, boredom, inadequate supplies and information, financial loss,
  and stigma as key stressors, and derive concrete mitigation recommendations: keep
  quarantine as short as scientifically justified, communicate clearly, ensure supplies, and
  enable remote social connection.
claims:
  - text: "Longer quarantine duration was consistently linked to worse mental health: those quarantined more than 10 days had significantly higher post-traumatic stress symptoms than those quarantined fewer than 10 days, and duration predicted post-traumatic stress symptoms, avoidance behaviours, and anger across three separate studies."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["stress", "mental-health"]
    predictors: ["isolation"]
  - text: "Quarantined individuals faced significant stigma and financial harm: quarantined health-care workers were significantly more likely than non-quarantined peers to report stigmatisation and rejection from their neighbourhoods, and household income below CAN$40,000 was associated with significantly higher post-traumatic stress and depressive symptoms."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["mental-health", "stress"]
    predictors: ["social-support"]
  - text: "Quarantine exposure had large comparative effects: mean post-traumatic stress scores were four times higher in quarantined children than non-quarantined children, and 28% of quarantined parents (27/98) met criteria for a trauma-related disorder versus 6% (17/299) of non-quarantined parents; effects on depression and alcohol dependence/abuse were still detectable up to 3 years post-quarantine in health-care workers."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["mental-health", "stress"]
    predictors: ["isolation"]
population:
  who: "24 primary studies of people placed under outbreak-related quarantine or isolation (hospital/health-care staff, general public, students, parents and children, horse owners), synthesized in this rapid review"
  where: ["Canada", "USA", "China", "Taiwan", "Hong Kong", "Australia", "South Korea", "Senegal", "Liberia", "Sierra Leone", "Sweden"]
  when: "Primary studies published through 2019, reviewing quarantine experiences from the 2003 SARS outbreak through the 2014-16 Ebola and 2015 MERS outbreaks"
  n: 24
  sector: ["healthcare"]
  sample_notes: >
    Included studies were peer-reviewed, in English or Italian, and required at least 24
    hours of non-hospital quarantine with mental-health data; screened from 3166 initial
    hits. Most included studies were cross-sectional with modest samples; only one followed
    participants longitudinally, and few directly compared quarantined versus non-
    quarantined groups, limiting causal inference and generalizability (e.g., some samples
    were undergraduate students).
limitation:
  primary: "As a rapid review conducted under time pressure during the emerging coronavirus outbreak, the authors did not perform formal quality appraisal of the included studies."
  others:
    - "Restricted to English/Italian peer-reviewed publications, excluding potentially relevant grey literature"
    - "Underlying primary studies were mostly cross-sectional with small samples and heterogeneous outcome measures, making cross-study comparison difficult"
    - "Recommendations are derived mainly from small-group/facility-based quarantine and may not directly generalize to large-scale city-wide lockdowns"
risk_of_bias: "medium"
relevance_to_project: >
  This review's stressor taxonomy (duration, inadequate information, inadequate supplies,
  boredom, stigma, financial loss) and its explicit recommendation to 'activate your social
  network, albeit remotely' via phone/internet to offset isolation directly informs SNH
  interventions for physically or socially isolated remote workers, including time-boxing
  isolation periods, proactive communication, and structured remote social-support
  mechanisms (e.g., peer support lines).
tags:
  topic: ["isolation", "mental-health", "wellbeing", "social-support", "burnout"]
  method: ["review-scoping", "secondary-data"]
  population: ["healthcare-workers", "general-public", "quarantined-populations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Brooks et al. (2020) - The Psychological Impact of Quarantine and How to Reduce It - Rapid Review of the Evidence/Brooks et al. (2020) - The Psychological Impact of Quarantine and How to Reduce It - Rapid Review of the Evidence.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Brooks et al. (2020) - The Psychological Impact of Quarantine and How to Reduce It - Rapid Review of the Evidence.pdf"
  notes: null

---

id: "burt-2022-structural-holes-and-good-ideas"
title: "Structural holes and good ideas"
authors:
  - "Burt, Ronald S."
year: 2022
doi: "10.4337/9781789909432.00030"
venue: {type: "book", name: "Handbook of Sociological Science", volume: null, issue: null, pages: "372-422"}
citation: "Burt (2022). Structural holes and good ideas. Handbook of Sociological Science, 372-422. https://doi.org/10.4337/9781789909432.00030"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Burt tests whether brokerage across structural holes provides a 'vision advantage' by
  studying 673 supply-chain managers at a large American electronics company, combining a
  network survey (name generators/interpreters) with company personnel records on salary,
  evaluations, and promotions. Managers whose discussion networks bridged disconnected
  groups (low network constraint) were paid more, evaluated more positively, promoted more
  often, and had their improvement ideas rated as more valuable, more likely to be expressed
  and discussed, and less likely to be dismissed than managers embedded in dense, closed
  cliques. Burt argues the mechanism is informational: brokers see a wider diversity of
  practice and opinion, giving them raw material for good ideas, but a follow-up check found
  brokers' ideas mostly circulated back to their same close contacts rather than diffusing
  across the organization, so brokerage did not reduce the underlying fragmentation.
claims:
  - text: "Idea value rated by two senior judges was strongly, negatively associated with a manager's network constraint (closed, dense network) net of rank, age, education, business unit, and location (b = -.694, SE = .144, on log network constraint; model R^2 = .15); managers with networks spanning structural holes produced ideas judged substantially more valuable."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure"]
  - text: "Network constraint predicted whether an idea was ever expressed and whether it was dismissed: managers in denser, more closed networks were far more likely to have no idea recorded at all (b = -2.356, SE = .243) and, among those who did offer an idea, more likely to have it dismissed by both judges (b = .972, SE = .281); overall 32% of ideas were dismissed and dismissal was concentrated among high-constraint managers (43% of the most-constrained tier vs. 14% of the least-constrained)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["communication", "performance"]
    predictors: ["network-structure"]
  - text: "Brokerage was rewarded organizationally: at senior manager and executive ranks, lower network constraint predicted significantly higher salary relative to peers (e.g., -$681 per point of constraint for executives, t = 5.5); the odds of a two-year 'outstanding' evaluation were roughly double for low-constraint managers (.32) versus high-constraint managers (.16); and the probability of promotion or an above-average raise was .68 for brokers versus .28 for managers confined to a dense clique."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "retention"]
    predictors: ["network-structure"]
population:
  who: "673 managers running the supply chain in 2001 for one of America's largest electronics companies; network-survey data available for 455 respondents (68% response), idea data drawn from those 455."
  where: ["United States"]
  when: "2001 (network survey), with salary/evaluation/promotion data spanning the six months before and after)"
  n: 673
  sector: ["private-sector", "electronics-manufacturing", "corporate-management"]
  sample_notes: >
    Single-firm convenience sample (one large electronics company's supply-chain function);
    68% completed the network survey, with a logit check showing respondents and
    nonrespondents differed only in that recently promoted managers were slightly more
    likely to respond; idea-value ratings came from just two senior-manager judges; 193
    supply-chain managers (29%) were social isolates never cited as a discussion partner.
limitation:
  primary: "Single-company, single-industry, largely cross-sectional design cannot establish that brokerage causes good ideas rather than reflecting reverse causation (able/valued managers get sought out as brokers) or unmeasured ability; Burt explicitly notes the association 'cannot be causal' from networks alone."
  others:
    - "Idea value was judged by only two senior managers using a 1-5 scale, an inherently subjective and organization-specific standard of 'good idea' (though Burt tests and rules out some rating biases)."
    - "Network constraint is computed only from each manager's immediate (one-step) discussion network, which Burt himself shows upwardly biases constraint scores relative to using the full network."
    - "Findings are specific to one bureaucratic, functionally-siloed supply-chain organization with unusually high baseline network constraint (mean ~68-81 points vs. ~28-49 in Burt's other manager samples), limiting generalizability."
risk_of_bias: "medium"
relevance_to_project: >
  A foundational empirical demonstration that a person's position in the informal
  communication network (bridging vs. closed/redundant ties) predicts whether their ideas
  get voiced, taken seriously, and rewarded — directly informing SNH's interest in how
  network structure and isolation shape engagement, help-seeking, and voice, and offering a
  concrete measure (network constraint) and outcome set (idea expression, idea dismissal,
  evaluation, promotion) that could be adapted to study remote-worker or open-source-
  maintainer social capital.
tags:
  topic: ["collaboration", "isolation", "productivity", "measurement"]
  method: ["survey", "cross-sectional", "secondary-data"]
  population: ["managers", "corporate", "us-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Burt (2004) - Structural Holes and Good Ideas/Burt (2004) - Structural Holes and Good Ideas.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Burt (2004) - Structural Holes and Good Ideas.pdf"
  notes: null

---

id: "feldman-2012-can-hope-be-changed-in-90"
title: "Can Hope be Changed in 90 Minutes? Testing the Efficacy of a Single-Session Goal-Pursuit Intervention for College Students"
authors:
  - "Feldman, David B."
  - "Dreher, Diane E."
year: 2012
doi: "10.1007/s10902-011-9292-4"
venue: {type: "journal", name: "Journal of Happiness Studies", volume: 13, issue: 4, pages: "745-759"}
citation: "Feldman et al. (2012). Can Hope be Changed in 90 Minutes? Testing the Efficacy of a Single-Session Goal-Pursuit Intervention for College Students. Journal of Happiness Studies, 13(4), 745-759. https://doi.org/10.1007/s10902-011-9292-4"
article_type: "empirical"
method: {design: "rct", approach: "experiment", evidence_level: "moderate", preregistered: false}
gist: >
  96 college students were randomly assigned to a single 90-minute hope-based goal-mapping
  and visualization intervention, a progressive muscle relaxation intervention, or no
  treatment. Immediate post-test gains in hope, purpose in life, and vocational calling
  faded by one-month follow-up, but participants in the hope condition reported
  significantly greater progress on their self-nominated goal at one month than either
  control group, an effect limited to goals rated highly personally important. Hope levels
  prospectively predicted goal progress but did not statistically mediate the intervention's
  effect, suggesting the brief intervention's benefit operated partly through mechanisms
  other than self-reported hope (e.g., a practice/rehearsal effect).
claims:
  - text: "Relative to relaxation controls, the hope intervention produced significant condition x time interactions from pre- to post-test on hope pathways (F(1,64)=9.67, p=.003, partial eta^2=.13), hope agency (F(1,64)=4.72, p=.03, partial eta^2=.07), purpose in life (F(1,65)=4.34, p=.04, partial eta^2=.06), and vocational identity (F(1,65)=4.06, p=.05, partial eta^2=.06); these gains were not maintained at one-month follow-up."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["wellbeing", "job-satisfaction"]
    predictors: ["hope", "intervention"]
  - text: "At one-month follow-up, hope-intervention participants reported significantly more progress on their self-nominated goal than relaxation and no-treatment controls (F(2,36)=5.70, p=.01, partial eta^2=.24), but only among those who had rated the goal as personally important; condition had no effect on goal progress for low-importance goals (F(2,29)=.69, p=.54)."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["hope", "intervention"]
  - text: "Goal-specific hope prospectively predicted one-month goal progress (pathways r(39)=.31, p=.03; agency r(39)=.28, p=.04), but a Sobel test found no significant mediation of the intervention-goal progress relationship by hope (Z=1.12, p=.26), meaning the intervention's effect on goal attainment was largely unexplained by measured hope."
    evidence: "rct"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["hope"]
population:
  who: "96 undergraduate introductory-psychology students (27 male, 69 female) at a private university in Northern California, mean age 18.71 (SD=.85)"
  where: ["United States"]
  when: "not reported (published 2011)"
  n: 96
  sector: ["higher-education"]
  sample_notes: >
    Convenience sample recruited from an introductory psychology subject pool for course
    credit; predominantly Caucasian (67 of 96); 24.7% attrition at one-month follow-up, not
    differing significantly by condition; no-treatment control group completed only pre-test
    and follow-up measures, not post-test.
limitation:
  primary: "The same researchers delivered both the hope and relaxation interventions, creating potential researcher-allegiance effects, and the no-treatment control group did not complete post-test measures, restricting some analyses to hope-vs-relaxation comparisons only."
  others:
    - "Goal progress was measured with a single self-report item, subject to reporting bias, with no objective corroboration of attainment."
    - "Immediate gains in hope, purpose, and vocational calling were not sustained at one-month follow-up, and hope did not mediate the intervention's downstream effect on goal progress, leaving the causal mechanism unresolved."
    - "Narrow, non-clinical convenience sample of mostly Caucasian introductory-psychology undergraduates limits generalizability to other populations."
risk_of_bias: "medium"
relevance_to_project: >
  Offers experimental evidence that a very brief, low-cost, single-session goal-
  mapping/visualization intervention can produce a measurable increase in goal pursuit a
  month later, relevant to SNH's search for lightweight, scalable interventions to boost
  motivation and engagement among isolated or disengaged remote workers; the failure of hope
  to mediate the effect also cautions against assuming a single psychological construct
  fully explains why brief interventions work when designing and evaluating similar
  programs.
tags:
  topic: ["wellbeing", "mental-health", "measurement"]
  method: ["rct", "survey"]
  population: ["college-students", "united-states"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Can Hope be Changed in 90 Minutes_ Testing the Efficacy of a Single-Session Goal-Pursuit Intervention for College Students/Can Hope be Changed in 90 Minutes_ Testing the Efficacy of a Single-Session Goal-Pursuit Intervention for College Students.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Can Hope be Changed in 90 Minutes_ Testing the Efficacy of a Single-Session Goal-Pursuit Intervention for College Students.pdf"
  notes: null

---

id: "iacus-2012-causal-inference-without-balance-checking-coarsened"
title: "Causal Inference without Balance Checking: Coarsened Exact Matching"
authors:
  - "Iacus, Stefano M."
  - "King, Gary"
  - "Porro, Giuseppe"
year: 2012
doi: "10.1093/pan/mpr013"
venue: {type: "journal", name: "Political Analysis", volume: 20, issue: 1, pages: "1-24"}
citation: "Iacus et al. (2012). Causal Inference without Balance Checking: Coarsened Exact Matching. Political Analysis, 20(1), 1-24. https://doi.org/10.1093/pan/mpr013"
article_type: "methods"
method: {design: "theory", approach: "modelling", evidence_level: "reference", preregistered: false}
gist: >
  The paper introduces Coarsened Exact Matching (CEM), a nonparametric preprocessing method
  for observational causal inference that bounds covariate imbalance, model dependence, and
  estimation error ex ante rather than requiring iterative post hoc balance checking. Using
  Monte Carlo simulation and a canonical job-training benchmark data set, the authors show
  CEM dominates propensity-score, Mahalanobis, and genetic matching on bias, variance, RMSE,
  and imbalance reduction, while being far faster and more robust to measurement error. Its
  contribution to the SNH project is purely methodological: a candidate tool for
  strengthening causal inference in future observational remote-work or community-health
  analyses, not substantive findings about social connection or wellbeing.
claims:
  - text: "In 5000 Monte Carlo replications based on the Lalonde/Dehejia-Wahba job-training data, CEM reduced RMSE of the treatment-effect estimate by 93% relative to the raw (unmatched) data (RMSE 111.38 vs 1622.63) and eliminated 99.8% of bias, outperforming Mahalanobis matching (RMSE 1077.20), propensity-score matching (1058.28), and genetic matching (505.55)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["estimation-bias"]
    predictors: ["sampling-method"]
  - text: "Across 5000 simulated perturbations of an earnings variable (to test robustness to measurement error), CEM preserved 95.3% of treated units and 97.7% of control units in the matched set, compared to roughly 70-81% for propensity-score, Mahalanobis, and genetic matching."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement-error"]
    predictors: ["sampling-method"]
  - text: "In an empirical illustration on the Lalonde observational data, CEM reduced multivariate imbalance (L1) by 17.47% (0.977 to 0.806) and achieved exact zero mean-difference balance on all binary/categorical covariates (marital status, no-degree, race, unemployment indicators), whereas propensity-score matching reduced imbalance only 2.48% and left substantial residual imbalance on those same covariates."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["covariate-balance"]
    predictors: ["sampling-method"]
population:
  who: "Not a human-subjects study of remote work or SNH outcomes; illustrative data are Monte Carlo simulations and the canonical Lalonde (1986) National Supported Work Demonstration job-training benchmark, combining 297 experimental treated participants with 2,490 PSID observational control units."
  where: ["USA"]
  when: "Original NSW/PSID data from the 1970s-80s; paper published 2012"
  n: 2787
  sector: ["labor-market"]
  sample_notes: >
    This is a statistics/econometrics methods paper, not an SNH empirical study; the
    'sample' is a standard causal-inference benchmark data set (job-training earnings) used
    only to demonstrate the matching algorithm's statistical properties.
limitation:
  primary: "The method is demonstrated only on a canonical econometric benchmark (job-training earnings data) and simulations, not on any social-network-health, remote-work, isolation, or wellbeing outcome, so it offers no substantive SNH evidence, only a candidate analytic tool."
  others:
    - "Simulation results depend on a specific nonlinear data-generating process chosen to replicate a prior benchmark (Diamond and Sekhon 2005) and may not generalize to all covariate structures encountered in SNH data."
    - "CEM's imbalance reduction trades off against matched sample size (e.g., 176 of 297 treated units retained in the empirical example), which can reduce statistical power."
    - "Results and comparisons come entirely from the method's own developers with no independent replication reported in this paper."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Offers a matching method (CEM) that SNH researchers could adopt to strengthen causal
  claims from observational remote-work or community data (e.g., estimating effects of an
  intervention on burnout, turnover, or isolation) while avoiding the iterative balance-
  checking failures common with propensity-score matching; relevant as a methodological
  reference for future SNH causal analyses rather than as substantive evidence.
tags:
  topic: ["methodology", "measurement"]
  method: ["theory", "secondary-data"]
  population: ["labor-market-participants"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Causal Inference without Balance Checking_  Coarsened Exact Matching/Causal Inference without Balance Checking_  Coarsened Exact Matching.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Causal Inference without Balance Checking_  Coarsened Exact Matching.pdf"
  notes: null

---

id: "morrison-2020-challenges-and-barriers-in-virtual-teams"
title: "Challenges and barriers in virtual teams: a literature review"
authors:
  - "Morrison-Smith, Sarah"
  - "Ruiz, Jaime"
year: 2020
doi: "10.1007/s42452-020-2801-5"
venue: {type: "journal", name: "SN Applied Sciences", volume: 2, issue: 6, pages: null}
citation: "Morrison-Smith et al. (2020). Challenges and barriers in virtual teams: a literature review. SN Applied Sciences, 2(6). https://doi.org/10.1007/s42452-020-2801-5"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  A Kitchenham-style systematic literature review of 255 studies (identified via Google
  Scholar search plus citation snowballing) synthesizing the collaboration challenges faced
  by virtual teams. The review organizes challenges into five categories - geographical,
  temporal, and perceived distance, plus team configuration and worker diversity - and finds
  that distance-driven erosion of awareness, trust, and informal/face-to-face communication
  is the central mechanism degrading virtual-team cohesion and performance. It translates
  these findings into four groupware design implications: supporting common ground,
  facilitating communication, providing work transparency, and building lightweight,
  familiar technology.
claims:
  - text: "Synthesizing Olson and Olson's decade-spanning body of work, the review identifies ten recurring distance-related challenges to virtual collaboration - reduced awareness of colleagues, diminished motivational sense of presence, difficulty establishing trust, uneven technical competence, inadequate technical infrastructure, mismatched nature of work, absent explicit management, weak common ground, competitive (vs. cooperative) culture, and misaligned incentives - as the recurring factors driving virtual-team dysfunction."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "remote-work-intensity"]
  - text: "Trust is consistently harder to establish and maintain in geographically dispersed teams than co-located ones, with lasting downstream effects: corroded task coordination, decreased willingness to communicate, fewer members taking initiative, less feedback exchange, and increased perceived risk; the effect is most pronounced early in a project and tapers as the collaboration matures."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication", "sense-of-belonging"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Loss of informal, face-to-face contact (which accounts for up to 75 minutes of a typical co-located workday) reduces virtual teams' sense of cohesion and personal rapport and lowers affective commitment; unaddressed isolation is linked to declining contribution and participation as disengaged members further withdraw from the team."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "sense-of-belonging", "job-engagement"]
    predictors: ["remote-work-intensity", "social-support"]
population:
  who: "255 empirical, technical, and review papers on virtual/distributed team collaboration, identified via a systematic Google Scholar search (first 10 pages per query, ~1200 candidates screened) plus citation snowballing; predominantly HCI/CSCW and distributed software development literature."
  where: []
  when: null
  n: 255
  sector: ["technology", "knowledge-work"]
  sample_notes: >
    Included papers had to concern collaboration, contain empirical evidence, and report
    generalizable findings; excluded non-English papers, non-peer-reviewed work (e.g.,
    master's theses), off-topic papers, and duplicates. Single search engine (Google
    Scholar) used as the primary discovery tool rather than multiple bibliographic
    databases; concept saturation reported after ~8-9 result pages per query.
limitation:
  primary: "Reliance on Google Scholar as the sole systematic search engine (supplemented by snowballing) rather than triangulating across multiple bibliographic databases risks missing relevant studies and introduces selection bias despite the otherwise well-documented protocol."
  others:
    - "Synthesizes findings across highly heterogeneous virtual-team contexts (distributed software teams, scientific collaborations, general knowledge work) without meta-analytic pooling of effect sizes, leaving many conclusions narrative and several contradictory findings across primary studies explicitly unresolved (flagged as open questions)."
    - "No formal risk-of-bias or quality appraisal of the 255 included primary studies is reported."
risk_of_bias: "medium"
relevance_to_project: >
  Maps the specific mechanisms - erosion of awareness, trust, and informal contact under
  distance - by which remote and distributed work degrades belonging, cohesion, and
  engagement, giving the SNH project a synthesized causal chain from geographic/temporal
  distance to isolation. Its four design implications, especially 'provide mechanisms for
  work transparency' to counter feelings of disconnection and invisibility, are directly
  usable as concrete design requirements for SNH interventions targeting remote-worker
  isolation.
tags:
  topic: ["remote-work", "collaboration", "isolation", "social-support", "hybrid-work"]
  method: ["review-systematic"]
  population: ["remote-workers", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Challenges and Barriers in Virtual Teams - A Literature Review/Challenges and Barriers in Virtual Teams - A Literature Review.md"
  pdf: "papers/Remote Workers/Challenges and Barriers in Virtual Teams - A Literature Review.pdf"
  notes: null

---

id: "chuang-2024-information-quality-work-family-conflict-loneliness"
title: "Information quality, work-family conflict, loneliness, and well-being in remote work settings"
authors:
  - "Chuang, Ya-Ting"
  - "Chiang, Hua-Ling"
  - "Lin, An-Pan"
year: 2024
doi: "10.1016/j.chb.2024.108149"
venue: {type: "journal", name: "Computers in Human Behavior", volume: 154, issue: null, pages: "108149"}
citation: "Chuang et al. (2024). Information quality, work-family conflict, loneliness, and well-being in remote work settings. Computers in Human Behavior, 154, 108149. https://doi.org/10.1016/j.chb.2024.108149"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a three-wave survey of 462 Taiwanese work-from-home employees during the pandemic,
  this study finds that information accuracy reduces work-family conflict (which in turn
  lowers well-being) while information timeliness reduces loneliness (which also mediates
  well-being), consistent with a job demands-resources framing where timeliness and accuracy
  each act primarily as resources. Information timeliness and accuracy also moderate each
  other's effects, and loneliness has the strongest overall association with well-being
  among the mediators tested. The study contributes a novel information-quality lens
  (accuracy vs. timeliness) to the remote-work literature on work-family conflict,
  loneliness, and well-being.
claims:
  - text: "Information timeliness was negatively related to loneliness (β = -0.22, p < .01), and loneliness mediated the relationship between information timeliness and well-being with an indirect effect of 0.19 (95% CI 0.11-0.27)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "wellbeing"]
    predictors: ["communication"]
  - text: "Information accuracy was negatively related to work-family conflict (β = -0.15, p < .01), and work-family conflict mediated the relationship between information accuracy and well-being with an indirect effect of 0.08 (95% CI 0.03-0.13)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["communication"]
  - text: "Both information timeliness (β = 0.14-0.16, p < .05) and information accuracy (β = 0.16-0.17, p < .05) positively predicted well-being directly, and information accuracy moderated the timeliness-loneliness link (β = -0.09, p < .05) while timeliness moderated the accuracy-work-family-conflict link (β = 0.08, p < .05); neither information variable significantly affected family-work conflict."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing", "loneliness", "work-life-balance"]
    predictors: ["communication"]
population:
  who: "Work-from-home employees at listed companies and public universities in Taiwan, recruited via a market research firm"
  where: ["Taiwan"]
  when: "mid-2021 (during Taiwan's COVID-19 remote-work advocacy period)"
  n: 462
  sector: ["mixed", "administrative", "technology"]
  sample_notes: >
    517 consented, 462 completed all three survey waves (89% retention); 74% female, mean
    age 38.8, 54.5% married, 46.3% with children; sample was pandemic-induced (largely
    involuntary) teleworkers rather than traditional voluntary remote workers, limiting
    generalizability.
limitation:
  primary: "The sample consisted of employees forced into remote work by pandemic policy rather than typical voluntary teleworkers, limiting generalizability to standard remote-work populations."
  others:
    - "All measures are self-reported across time-lagged surveys, raising common-method and self-report bias concerns despite the three-wave design."
    - "Design is correlational (not experimental), so causal claims about information quality's effects cannot be firmly established."
    - "The study frames information quality only as a resource and does not test its potential downside as a demand (e.g., information overload), which the authors flag as a gap."
risk_of_bias: "medium"
relevance_to_project: >
  Gives the SNH project a concrete, testable mechanism for loneliness mitigation in remote
  work: timely (not just accurate) organizational communication is specifically linked to
  reduced loneliness and, through that pathway, to well-being, suggesting communication-
  cadence interventions (e.g., prompt updates, responsive channels) as a distinct lever from
  general informational support.
tags:
  topic: ["remote-work", "loneliness", "wellbeing", "work-life-balance", "communication"]
  method: ["survey", "longitudinal", "mediation-moderation"]
  population: ["remote-workers", "taiwan", "teleworkers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Chuang et al. (2024) - Information Quality, Work-Family Conflict, Loneliness, and Well-Being in Remote Work Settings/Chuang et al. (2024) - Information Quality, Work-Family Conflict, Loneliness, and Well-Being in Remote Work Settings.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Chuang et al. (2024) - Information Quality, Work-Family Conflict, Loneliness, and Well-Being in Remote Work Settings.pdf"
  notes: null

---

id: "clark-2000-work-family-border-theory-a-new"
title: "Work/Family Border Theory: A New Theory of Work/Family Balance"
authors:
  - "Clark, Sue Campbell"
year: 2000
doi: "10.1177/0018726700536001"
venue: {type: "journal", name: "Human Relations", volume: 53, issue: 6, pages: "747-770"}
citation: "Clark (2000). Work/Family Border Theory: A New Theory of Work/Family Balance. Human Relations, 53(6), 747-770. https://doi.org/10.1177/0018726700536001"
article_type: "theory"
method: {design: "theory", approach: "interview", evidence_level: "speculative", preregistered: false}
gist: >
  Clark introduces work/family border theory, arguing that work and home are distinct
  cultural domains separated by physical, temporal, and psychological borders that people
  actively negotiate as daily 'border-crossers.' Building the theory from a personal
  journal, 15 in-depth interviews, and a related 150-person survey (Clark & Farmer, 1998),
  the article proposes eight testable propositions linking border strength, permeability,
  flexibility, blending, central participation, and border-keeper support (e.g.,
  supervisors, spouses) to work/family balance. It contributes a boundary-management
  vocabulary and mechanism-level hypotheses rather than confirmatory empirical evidence.
claims:
  - text: "In the companion 150-person survey (Clark & Farmer, 1998), employees rated their workplace cultures as more formal, more hierarchical, less collective, less intimate, more doing-oriented, and more money-based than their home cultures, indicating a systematic cultural gap between the two domains."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance"]
    predictors: ["organizational-culture", "boundary-management"]
  - text: "Employees who reported greater cultural difference between work and home also reported communicating less with supervisors about their home lives, suggesting domain dissimilarity suppresses cross-border communication that could otherwise mitigate conflict."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "communication"]
    predictors: ["organizational-culture", "boundary-management"]
  - text: "The theory formalizes eight propositions, including that weak (permeable, flexible) borders facilitate balance when work and home domains are culturally similar, whereas strong borders are needed for balance when domains differ sharply, and that high supervisor/spouse 'other-domain awareness' and commitment predict greater work/family balance."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["work-life-balance"]
    predictors: ["social-support", "boundary-management"]
population:
  who: "15 U.S. adults in full-time employment with significant family responsibilities (diverse in age, marital/family status, job flexibility, ethnicity, gender, income), interviewed to build the theory; theory also draws on a separate 150-person survey of employed adults with work and family responsibilities (Clark & Farmer, 1998)."
  where: ["United States"]
  when: null
  n: 15
  sector: []
  sample_notes: >
    Interviewees were convenience-sampled contacts of the author and two research
    assistants, deliberately chosen for challenging work/family situations rather than
    representativeness; no response rate or sampling frame reported. The supporting
    150-person survey (Clark & Farmer, 1998) is an unpublished/conference paper, not
    independently verifiable in this corpus copy.
limitation:
  primary: "The theory's empirical grounding rests on a small (n=15), non-representative convenience sample of interviewees and an unpublished companion survey, with none of the eight propositions themselves tested within this article."
  others:
    - "Qualitative interview and coding methodology is described only impressionistically, with no coding scheme, inter-rater reliability, or transcript excerpts beyond illustrative anecdotes."
    - "As a theory-building paper it offers no effect sizes or hypothesis tests for its central claims about border strength and balance."
risk_of_bias: "high"
relevance_to_project: >
  Border theory supplies the SNH project's core vocabulary for boundary management in
  remote/hybrid work -- domain permeability, flexibility, blending, and border-keeper
  support -- directly informing how to design and measure interventions (e.g., supervisor
  training, communication norms) aimed at reducing work/family conflict and its downstream
  effects on isolation, stress, and burnout among remote workers.
tags:
  topic: ["work-life-balance", "remote-work", "social-support", "wellbeing", "methodology"]
  method: ["theory", "qualitative", "interview"]
  population: ["knowledge-workers", "dual-earner-parents"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Clark (2000) - Work-Family Border Theory - A New Theory of Work-Family Balance/Clark (2000) - Work-Family Border Theory - A New Theory of Work-Family Balance.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Clark (2000) - Work-Family Border Theory - A New Theory of Work-Family Balance.pdf"
  notes: null

---

id: "cole-2003-testing-mediational-models-with-longitudinal-data"
title: "Testing Mediational Models With Longitudinal Data: Questions and Tips in the Use of Structural Equation Modeling."
authors:
  - "Cole, David A."
  - "Maxwell, Scott E."
year: 2003
doi: "10.1037/0021-843x.112.4.558"
venue: {type: "journal", name: "Journal of Abnormal Psychology", volume: 112, issue: 4, pages: "558-577"}
citation: "Cole et al. (2003). Testing Mediational Models With Longitudinal Data: Questions and Tips in the Use of Structural Equation Modeling.. Journal of Abnormal Psychology, 112(4), 558-577. https://doi.org/10.1037/0021-843x.112.4.558"
article_type: "methods"
method: {design: "methods", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  Cole and Maxwell extend Baron and Kenny's cross-sectional mediation framework to
  longitudinal structural equation modeling, mathematically demonstrating that cross-
  sectional estimates of mediational paths are biased except under narrow, rarely-met
  conditions (e.g., X and M equally stable over time), and that measurement error, wave-
  spacing, and 'half-longitudinal' designs systematically distort indirect-effect estimates.
  They propose a five-step SEM procedure (test the measurement model, test for added
  components/omitted confounds, test for omitted paths, test stationarity, then estimate
  overall direct/indirect effects) for rigorously testing whether a mediator explains a
  causal chain over time.
claims:
  - text: "Cross-sectional correlations accurately reproduce true longitudinal mediational path coefficients (a and b) only under narrow, rarely-satisfied conditions (e.g., a or b equal zero, or X and M are exactly equally stable over time); outside these conditions cross-sectional data systematically over- or underestimate the longitudinal mediation effect."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
  - text: "When the mediator (M) is measured with random error, path a and path b are both underestimated while the residual direct effect c is spuriously overestimated (e.g., in a worked example, reliability of .5 in M drops path b from .80 to .30 while inflating c from .00 to .47), meaning unreliable mediator measures make full mediation look like partial or no mediation."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
  - text: "The magnitude of estimated mediational (indirect) effects depends heavily on the time lag between waves of data collection: only an assessment interval of exactly the causally-optimal lag (1I) yields unbiased time-specific effects, and researchers should instead sum 'overall' indirect effects across all valid tracings between the first and last wave rather than relying on a single time-specific ab product, since longer or mismatched lags can badly misrepresent the true mediated effect."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["network-structure"]
population:
  who: "Not an empirical study of human participants; a methodological/statistical article illustrating structural equation modeling procedures with algebraic derivations and one hypothetical numeric worked example (arbitrary path coefficients), drawing on examples from the clinical/psychopathology literature (e.g., Andrews 1995, Trull 2001, Tein et al. 2000) to illustrate common design flaws."
  where: []
  when: null
  n: null
  sector: ["academic"]
  sample_notes: >
    No primary data collection; this is a statistical methods/tutorial paper with a
    hypothetical illustrative model, not a study with a sample.
limitation:
  primary: "The proposed five-step approach and 'overall effect' framework require at least three (ideally more) waves of multi-measure longitudinal data with empirically pre-established optimal time lags between waves, conditions rarely met in real studies, and the authors note no general test of statistical significance for overall indirect effects (beyond the 3-wave case) had yet been developed at time of writing."
  others:
    - "Recommendations assume linear, stationary causal processes and observational (non-experimental) designs; the authors explicitly caveat that randomized experimental manipulation of the mediator provides more compelling causal evidence than any SEM correction of observational data."
    - "The worked numerical example uses arbitrary illustrative path coefficients rather than real data, so its magnitudes are pedagogical, not empirical estimates."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a core methodological reference for any SNH analysis that models a mediator (e.g.,
  loneliness or social support) between a predictor (e.g., remote-work intensity) and an
  outcome (e.g., burnout, turnover): it warns against 'half-longitudinal' designs, single-
  wave mediator measurement, and mismatched survey-wave spacing, and gives a concrete five-
  step SEM checklist for defensibly testing such mediation claims in panel/longitudinal SNH
  survey data.
tags:
  topic: ["methodology", "measurement"]
  method: ["longitudinal", "structural-equation-modeling"]
  population: ["methodology"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Cole & Maxwell (2003) - Testing Mediational Models With Longitudinal Data - Questions and Tips in the Use of Structural Equation Modeling.pdf"
  notes: null

---

id: "sanusi-2023-communication-challenges-and-strategies-in-remote"
title: "Communication Challenges and Strategies in Remote Work Settings"
authors:
  - "Sanusi, Bernice Oluwalanu"
  - "Ola, Oluwawapelumi Iyinoluwa"
  - "Adaramola, Ebernezer Toba"
year: 2023
doi: null
venue: {type: "other", name: "ResearchGate (self-archived manuscript, Redeemer's University / Bowen University)", volume: null, issue: null, pages: null}
citation: "Sanusi et al. (2023). Communication Challenges and Strategies in Remote Work Settings. ResearchGate (self-archived manuscript, Redeemer's University / Bowen University)."
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low", preregistered: false}
gist: >
  A descriptive survey of 384 respondents in Osogbo, Nigeria found people were largely
  satisfied with their current remote-communication tools (WhatsApp, Zoom, Telegram,
  Facebook Messenger, Google Chat) yet rarely used video conferencing for team meetings, and
  rated six specific communication problems (lack of non-verbal cues, communication
  overload, misunderstanding, lack of visual context, technical issues,
  accountability/monitoring) as widespread. The paper frames these as barriers requiring
  both tool selection and communication-norm strategies, and respondents also endorsed a
  wishlist of additional tools (VR/AR, interactive whiteboards, emotion-recognition tools)
  to improve remote collaboration.
claims:
  - text: "Respondents reported high satisfaction with current remote-collaboration tools/platforms (47.3% highly satisfied, 19% satisfied; combined ~66%), even though 63.3% used video conferencing for team meetings only to a low or very low extent."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity"]
  - text: "All six surveyed communication challenges were endorsed as significant (Likert means below the 2.51 acceptance threshold, grand mean 1.76): Technical Issues (1.52), Misunderstanding/miscommunication (1.61), Lack of Visual Context (1.73), Accountability and Monitoring (1.81), Lack of Non-Verbal Cues (1.89), and Communication Overload (1.96)."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["communication", "collaboration"]
    predictors: ["remote-work-intensity", "technostress"]
  - text: "Respondents indicated a need for additional technological tools to enhance remote collaboration (grand mean 2.09, below the acceptance threshold), most strongly favoring VR/AR tools (mean 1.61), Interactive Whiteboard Tools (1.70), and Emotion Recognition Tools (1.65)."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity"]
population:
  who: "384 residents of Osogbo, Nigeria, recruited by convenience sampling and judged capable of intelligently discussing remote work; the paper does not confirm respondents were themselves current remote workers."
  where: ["Nigeria"]
  when: "2023"
  n: 384
  sector: []
  sample_notes: >
    400 questionnaires distributed, 384 returned and usable (96% return rate); sample size
    derived via Taro Yamane's formula from an assumed population of 750,000, but selection
    was convenience-based (research assistants distributing questionnaires in one city)
    rather than random, and no screening criterion confirming remote-work status is
    described.
limitation:
  primary: "Convenience sampling of general Osogbo residents, without verifying respondents were actual remote workers, undermines the generalizability of findings framed as being about 'remote workers'."
  others:
    - "Single-country, single-city, cross-sectional design precludes causal or longitudinal claims about communication challenges or tool effectiveness."
    - "Findings rest entirely on closed-ended Likert items summarized as means/percentages, with no inferential statistics, correlation, or regression analysis."
    - "No triangulation with qualitative data or objective usage logs to corroborate self-reported satisfaction and challenge ratings."
risk_of_bias: "high"
relevance_to_project: >
  Provides a simple, if methodologically weak, ranked inventory of perceived remote-
  communication pain points (non-verbal-cue loss, overload, misunderstanding, technical
  issues, accountability/monitoring) and desired tooling (VR/AR, emotion-recognition,
  advanced video conferencing) that the SNH project can use as a candidate list when scoping
  which collaboration-tool features might reduce miscommunication-driven isolation, while
  treating the specific percentages as low-confidence given the convenience sample.
tags:
  topic: ["remote-work", "collaboration", "technostress", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["nigeria", "convenience-sample"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Communication Challenges and Strategies in Remote Work Settings/Communication Challenges and Strategies in Remote Work Settings.md"
  pdf: "papers/Remote Workers/Communication Challenges and Strategies in Remote Work Settings.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "suortti-2024-communicative-tensions-in-remote-work-during"
title: "Communicative Tensions in Remote Work During the COVID-19 Pandemic"
authors:
  - "Suortti, Camilla"
  - "Sivunen, Anu"
year: 2024
doi: "10.1177/08933189231199052"
venue: {type: "journal", name: "Management Communication Quarterly", volume: 38, issue: 2, pages: "386-412"}
citation: "Suortti et al. (2024). Communicative Tensions in Remote Work During the COVID-19 Pandemic. Management Communication Quarterly, 38(2), 386-412. https://doi.org/10.1177/08933189231199052"
article_type: "empirical"
method: {design: "qualitative", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Analyzing 3,880 open-ended survey responses (1,289 coded units) from 569 knowledge workers
  across three Nordic organizations in the first months of pandemic remote work, this study
  uses contrapuntal analysis to identify nine intertwined communicative tensions clustered
  into task-, process-, and relationship-oriented interactions. It finds that communication
  technology functions simultaneously as an enabler and a hindrance across all three
  categories, and that these tensions entangle with one another rather than existing
  independently, most notably relationship-oriented tensions (41% of coded units) tied to
  loneliness, isolation, and eroding team spirit. The paper argues that managing these
  entangled tensions, rather than resolving them, is key to supporting employee well-being
  in remote work.
claims:
  - text: "Relationship-oriented tensions accounted for 41% of the 1,289 coded analysis units (529 units), more than task-oriented (24%, 304 units) or process-oriented (35%, 456 units) tensions, with the largest single subtension being increased versus decreased opportunity to form and maintain social relationships (266 units, 50% of relationship-oriented units)."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "loneliness", "sense-of-belonging", "communication"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Respondents reported that reduced face-to-face contact and technology-mediated-only interaction produced feelings of isolation and loneliness and a distancing from the work community, even as some respondents simultaneously reported feeling closer to previously distant colleagues via video meetings."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["loneliness", "isolation", "sense-of-belonging", "wellbeing"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Communication technology was found to be simultaneously an enabler and a hindrance of interaction across all three tension categories (task, process, relationship), and this technology-mediated tension entangled with and amplified the other identified tensions rather than operating independently."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration", "communication", "job-engagement"]
    predictors: ["remote-work-intensity", "technostress"]
population:
  who: "Knowledge workers (teachers, researchers, and other professionals) at three Nordic research and education organizations, surveyed after 1-2 months of mandatory full-time remote work"
  where: ["Finland (Nordic countries)"]
  when: "April-May 2020"
  n: 569
  sector: ["education", "research", "knowledge-work"]
  sample_notes: >
    Open-ended online survey; 569 respondents (166/253/150 across the three organizations)
    produced 3,880 open-ended responses, coded into 1,289 analysis units. Mean respondent
    age 43 (range 19-67); 61% female, 36% male, 2% unreported. Authors note the sample was
    relatively privileged (reliable home internet/equipment), which limits generalizability
    to less-resourced remote workers.
limitation:
  primary: "Sample is drawn from privileged, well-resourced Nordic knowledge workers with stable home internet access at the very start of the pandemic, limiting generalizability to other populations, sectors, or later/prolonged remote-work periods."
  others:
    - "Cross-sectional, single-timepoint survey design cannot capture how tensions evolve over time; authors explicitly call for longitudinal or diary-study follow-up."
    - "Qualitative contrapuntal/thematic coding by two researchers introduces interpretive subjectivity, though authors report iterative discussion of codes."
    - "Data collected via short open-ended text responses (mean 26 words) rather than interviews, limiting depth of individual accounts."
risk_of_bias: "medium"
relevance_to_project: >
  Directly evidences the mechanism by which forced full-time remote work generates
  loneliness and isolation (relationship-oriented tensions, 41% of coded data) even while
  some workers report new or deepened connections, supporting SNH's contention that remote-
  work social health outcomes are bidirectional/tension-laden rather than uniformly
  negative. Also supplies concrete, quotable practitioner recommendations (longer meetings
  with buffer time for small talk, dedicated non-work channels) relevant to designing
  interventions.
tags:
  topic: ["remote-work", "isolation", "loneliness", "wellbeing", "collaboration", "social-support"]
  method: ["qualitative", "survey"]
  population: ["knowledge-workers", "education-sector"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Communicative Tensions in Remote Work During the COVID-19 Pandemic/Communicative Tensions in Remote Work During the COVID-19 Pandemic.md"
  pdf: "papers/Remote Workers/Communicative Tensions in Remote Work During the COVID-19 Pandemic.pdf"
  notes: null

---

id: "tong-2007-consolidated-criteria-for-reporting-qualitative-research"
title: "Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups"
authors:
  - "Tong, A."
  - "Sainsbury, P."
  - "Craig, J."
year: 2007
doi: "10.1093/intqhc/mzm042"
venue: {type: "journal", name: "International Journal for Quality in Health Care", volume: 19, issue: 6, pages: "349-357"}
citation: "Tong et al. (2007). Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups. International Journal for Quality in Health Care, 19(6), 349-357. https://doi.org/10.1093/intqhc/mzm042"
article_type: "methods"
method: {design: "design-report", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This paper introduces COREQ, a 32-item checklist for reporting in-depth interviews and
  focus-group studies in health research, built by consolidating 76 candidate items drawn
  from 22 existing checklists and major-journal author guidelines into three domains:
  research team and reflexivity, study design, and analysis and findings. It does not report
  new empirical findings about any social or health outcome; it is a methodological tool
  intended to make qualitative studies more transparent and easier to critically appraise,
  explicitly modeled on CONSORT for trials. For the SNH corpus, it functions as the field-
  standard rubric against which the rigor of qualitative interview/focus-group papers (e.g.,
  remote-worker isolation or maintainer-burnout studies) can be judged.
claims:
  - text: "The authors extracted 76 candidate reporting items from 22 published checklists (identified via Medline 1966-2006, CINAHL 1982-2006, Cochrane/Campbell protocols, and journal author/reviewer guidelines) and consolidated them, after removing duplicate and ambiguous items and adding two new items, into a 32-item COREQ checklist organized into three domains."
    evidence: "design-report"
    support_strength: "moderate"
    outcomes: ["reporting-quality"]
    predictors: ["sampling-method"]
  - text: "Across the 22 source checklists, the most frequently included reporting items concerned sampling method, setting of data collection, method of data collection, respondent validation of findings, method of recording data, description of derivation of themes, and inclusion of supporting quotations."
    evidence: "design-report"
    support_strength: "moderate"
    outcomes: ["reporting-quality"]
    predictors: ["sampling-method"]
  - text: "At the time of publication the authors acknowledged there was no empirical evidence that adopting COREQ would improve reporting quality, but drew an analogy to CONSORT, QUOROM, and other checklists that were subsequently shown to improve reporting quality once adopted by journals."
    evidence: "design-report"
    support_strength: "speculative"
    outcomes: ["reporting-quality"]
    predictors: ["intervention"]
population:
  who: "Not a human-subjects study: the 'sample' is 22 published checklists/guidelines for appraising or reporting qualitative research plus author/reviewer guidelines from five major biomedical journals (BMJ, JAMA, Lancet, Annals of Internal Medicine, NEJM), from which 76 reporting items were extracted."
  where: ["Australia (author institution)"]
  when: "Checklists identified via searches through April 2006 (Medline from 1966, CINAHL from 1982)"
  n: null
  sector: ["healthcare", "academia"]
  sample_notes: >
    No participants or primary data; this is a methods/tool-development paper synthesizing
    prior checklists, not an empirical study of people. Search was limited to two databases
    plus grey-literature/reference-list snowballing and journal guideline review.
limitation:
  primary: "The 32-item checklist was assembled by non-systematic consensus among the three authors from existing checklist items, with no empirical test at publication showing that using COREQ actually improves the quality or completeness of qualitative reporting."
  others:
    - "Scope is limited to interviews and focus groups; it does not address other qualitative methods such as ethnography, observation, or document analysis."
    - "The underlying literature search covered only Medline and CINAHL plus reference-list/guideline snowballing, current only to April 2006, so newer checklists or emerging reporting norms are not reflected."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Much of the SNH corpus relies on interview and focus-group studies of remote-worker
  isolation, maintainer burnout, and belonging; COREQ is the standard rubric the project can
  use to assess how transparently those qualitative sources report sampling, reflexivity,
  and analysis, and it is a checklist the project should itself follow if it conducts
  original qualitative interviews on social network health.
tags:
  topic: ["methodology", "measurement", "qualitative-research"]
  method: ["qualitative", "methods-development"]
  population: ["academia", "healthcare"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Consolidated criteria for reporting qualitative research (COREQ)_ a 32-item checklist for interviews and focus groups/Consolidated criteria for reporting qualitative research (COREQ)_ a 32-item checklist for interviews and focus groups.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Consolidated criteria for reporting qualitative research (COREQ)_ a 32-item checklist for interviews and focus groups.pdf"
  notes: null

---

id: "mheidly-2020-coping-with-stress-and-burnout-associated"
title: "Coping With Stress and Burnout Associated With Telecommunication and Online Learning"
authors:
  - "Mheidly, Nour"
  - "Fares, Mohamad Y."
  - "Fares, Jawad"
year: 2020
doi: "10.3389/fpubh.2020.574969"
venue: {type: "journal", name: "Frontiers in Public Health", volume: 8, issue: null, pages: null}
citation: "Mheidly et al. (2020). Coping With Stress and Burnout Associated With Telecommunication and Online Learning. Frontiers in Public Health, 8. https://doi.org/10.3389/fpubh.2020.574969"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This narrative review synthesizes literature on how the COVID-19-driven surge in
  telecommunication (teleconferencing, telecommuting, and online learning) contributed to
  stress, digital eye strain, and burnout, and argues that telecommunication-related strain
  compounds with other pandemic stressors (quarantine, job insecurity, disrupted schooling)
  to worsen mental health outcomes. It closes with eight practical coping recommendations
  (e.g., more breaks between sessions, podcast-based audio-only alternatives to video calls,
  yoga/mindfulness practices, and peer sharing in online communities) but explicitly
  concludes that evidence linking smart-device use to psychological harm remains equivocal
  and under-researched in the general population.
claims:
  - text: "Personality traits moderate telecommunication-related burnout: studies cited found extroverted individuals were more associated with telecommuting burnout, whereas introverted individuals reported facing telecommunication-induced stress more easily/manageably."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["burnout", "stress"]
    predictors: ["remote-work-intensity"]
  - text: "Excessive e-mail use is identified as an antecedent of employee burnout via information overload and the stress of continuously responding to messages, drawing on prior organizational studies (Barley et al. 2011; Estévez-Mujica & Quintane 2018)."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["burnout", "stress"]
    predictors: ["workload", "technostress"]
  - text: "Quarantine duration was linked to worse psychological outcomes: individuals quarantined more than 10 days were more likely to report post-traumatic stress symptoms than those quarantined for shorter periods (citing Brooks et al. 2020), and lockdown-driven inability to socialize was associated with reports of separation anxiety, boredom, and suicidal thoughts."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["stress", "isolation", "suicidal-ideation"]
    predictors: ["isolation"]
population:
  who: "Not an original sample; a narrative synthesis of secondary literature (surveys, cohort studies, other reviews) covering students, telecommuting/office employees, adolescents, healthcare workers, and the general public affected by the COVID-19-era shift to telecommunication and online learning"
  where: []
  when: "Literature published up to mid/late 2020, framed around the COVID-19 pandemic period"
  n: null
  sector: ["education", "remote-work", "healthcare"]
  sample_notes: >
    No original data collection or systematic search protocol described; sources were
    selectively cited (news reports, government notices, and a mix of empirical studies and
    prior reviews) rather than gathered via a reproducible systematic-review methodology.
limitation:
  primary: "The review is non-systematic (no stated search strategy, inclusion criteria, or quality appraisal), so the evidence base is a selective synthesis rather than a rigorously sampled one, and the authors themselves state that evidence on smart-device use and mental health remains equivocal."
  others:
    - "Most of the eight coping recommendations (podcasts, breaks, yoga, awareness campaigns) are proposed by the authors without direct empirical testing of their effectiveness for telecommunication-specific burnout."
    - "Focus is tightly bound to the acute COVID-19 lockdown context (2020), limiting generalizability to later, more routinized remote-work/hybrid-work arrangements."
    - "No primary data on the general working population's stress/burnout levels were collected; the authors note research on the general population (versus healthcare workers) is lacking."
risk_of_bias: "medium"
relevance_to_project: >
  Offers a ready-made menu of low-cost coping interventions (session breaks, audio/podcast
  substitution for video calls, mindfulness practices, peer sharing in online communities)
  that the SNH project can consider for remote-worker burnout mitigation, and flags email
  overload and personality traits (extroversion/introversion) as candidate predictors of
  telecommunication burnout worth measuring in SNH surveys.
tags:
  topic: ["remote-work", "burnout", "mental-health", "technostress", "wellbeing"]
  method: ["review"]
  population: ["remote-workers", "students", "general-population"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Coping With Stress and Burnout Associated With Telecommunication and Online Learning/Coping With Stress and Burnout Associated With Telecommunication and Online Learning.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Coping With Stress and Burnout Associated With Telecommunication and Online Learning.pdf"
  notes: null

---

id: "oseghale-2024-covid-19-working-from-home-and"
title: "Covid-19, working from home and work–life boundaries: the role of personality in work–life boundary management"
authors:
  - "Oseghale, O. Raphael"
  - "Pepple, Dennis"
  - "Brookes, Michael"
  - "Lee, Alex"
  - "Alaka, Hafiz"
  - "Nyantakyiwaa, Akua"
  - "Mokhtar, Ajlaa"
year: 2024
doi: "10.1080/09585192.2024.2422013"
venue: {type: "journal", name: "The International Journal of Human Resource Management", volume: 35, issue: 21, pages: "3556-3592"}
citation: "Oseghale et al. (2024). Covid-19, working from home and work–life boundaries: the role of personality in work–life boundary management. The International Journal of Human Resource Management, 35(21), 3556-3592. https://doi.org/10.1080/09585192.2024.2422013"
article_type: "empirical"
method: {design: "mixed-methods", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This exploratory sequential mixed-methods study of 41 UK academics forced into mandatory
  WFH during Covid-19 combined semi-structured interviews with IPIP Big Five personality
  scores to link personality traits to boundary-management style. Conscientious and
  introverted academics used integration and coped best via careful planning and high
  emotional stability, extroverts used a newly described 'volleying' style and struggled
  with isolation from colleagues, and neurotic academics largely failed to manage boundaries
  at all, with several quitting their jobs. The study extends boundary theory by adding a
  fourth boundary-management style, 'quitter', and argues boundary-management interventions
  must be personalized by personality type rather than one-size-fits-all.
claims:
  - text: "Academics high in conscientiousness and introversion coped better with mandatory WFH and predominantly used an integration boundary-management style, enabled by high emotional stability, careful planning, and effective communication with family members to minimize social interruptions."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["boundary-management", "isolation"]
  - text: "Nearly all 18 extroverted academics interviewed used a 'volleying' boundary-management style (segmenting non-timetabled work in favor of family, integrating timetabled work), driven by low emotional stability and difficulty tolerating isolation from colleagues; this reverses prior pre-Covid findings that extroverts manage boundaries better than introverts."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "isolation", "stress"]
    predictors: ["boundary-management", "social-support"]
  - text: "Neurotic academics did almost no boundary management and were the most adversely affected personality group: 4 of 6 neurotic interviewees resigned their jobs during the pandemic due to excessive worry and pressure, leading the authors to propose a new fourth boundary-management style, 'quitter', alongside segmentation, integration, and volleying."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["turnover", "burnout", "mental-health"]
    predictors: ["boundary-management", "workload"]
population:
  who: "UK higher-education academics (lecturers, senior/principal lecturers, professors) who transitioned to mandatory remote teaching during the Covid-19 lockdown"
  where: ["United Kingdom"]
  when: "Interviews conducted May-July 2020"
  n: 41
  sector: ["academia", "higher-education"]
  sample_notes: >
    50 semi-structured interviews conducted (purposive + snowball sampling across old and
    new UK universities), data saturation reported at 40 interviews; IPIP personality
    questionnaire administered to all 50 interviewees with a 100% response rate, but only 41
    of 50 personality-test scores corroborated the interview-derived personality codes, so 9
    were excluded from the final matched sample. Self-selected academic network sample;
    authors note this limits external validity/generalizability beyond UK higher education.
limitation:
  primary: "Small, occupation-specific sample (41 UK academics, cross-sectional) limits generalizability of personality-boundary management associations to other sectors, countries, or time periods, and the authors explicitly call for larger-scale surveys to test these relationships."
  others:
    - "Personality-behavior matching relied partly on subjective interview coding cross-checked against a psychometric scale with a low KMO sample-adequacy value (<0.6), indicating the personality-scale factor structure should be interpreted cautiously given the small n."
    - "Study captures the acute, mandatory-lockdown phase of WFH (2020) and authors note findings may not generalize to 'new normal'/post-pandemic hybrid work where home offices, childcare, and social outlets are more established."
    - "Findings on neuroticism and job quitting are based on a very small subgroup (6 neurotic interviewees, 4 resignations), limiting statistical confidence in the 'quitter' style as a generalizable pattern."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a personality-differentiated model of how remote/WFH isolation affects boundary
  management, burnout, and turnover risk (notably a 'quitter' pattern among neurotic/high-
  anxiety remote workers and a volleying/isolation-distress pattern among extroverts),
  directly informing SNH's design questions around personalized wellbeing interventions and
  early-warning signals for withdrawal or attrition in remote and distributed teams.
tags:
  topic: ["remote-work", "work-life-balance", "burnout", "mental-health", "isolation"]
  method: ["qualitative", "mixed-methods"]
  population: ["academia", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Covid-19  working from home and work life boundaries  the role of personality in work life boundary management/Covid-19  working from home and work life boundaries  the role of personality in work life boundary management.md"
  pdf: "papers/Remote Workers/Covid-19  working from home and work life boundaries  the role of personality in work life boundary management.pdf"
  notes: null

---

id: "day-1994-measurement-design-and-analysis-an-integrated"
title: "Measurement, Design and Analysis: An Integrated Approach."
authors:
  - "Day, Simon"
  - "Pedhazur, E. J."
  - "Schmelkin, L. Pedhazur"
year: 1994
doi: "10.2307/2348155"
venue: {type: "journal", name: "The Statistician", volume: 43, issue: 4, pages: "608"}
citation: "Day et al. (1994). Measurement, Design and Analysis: An Integrated Approach.. The Statistician, 43(4), 608. https://doi.org/10.2307/2348155"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This is a critical book review by Simon Day of Pedhazur and Schmelkin's 'Measurement,
  Design and Analysis: An Integrated Approach' (1991), published in the Journal of the Royal
  Statistical Society's book-reviews section. The reviewer argues the book's three parts
  (Measurement, Design, Analysis) are cross-referenced rather than truly integrated, praises
  Part 1 on measurement scales, validation, and reliability, but finds Part 2 on design thin
  on classical experimental-design topics like blocking and factorial designs. It offers no
  original data or SNH-relevant findings; it is a methodological-textbook appraisal aimed at
  social scientists choosing a measurement/design/analysis reference.
claims:
  - text: "The reviewer judges Part 1 ('Measurement'), covering scales of measurement, validation, and reliability, to merit wide readership among researchers despite its deceptively simple presentation."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The reviewer finds Part 2 ('Design') lacking in classical experimental-design content (e.g., blocking, factorial experiments), instead emphasizing artefacts/pitfalls in research and quasi-experimental versus non-experimental (observational) study distinctions."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The reviewer concludes the book fails to achieve genuine 'integration' across its three sections, functioning instead as three loosely cross-referenced texts, and recommends students consult multiple targeted sources rather than this single 800+ page volume."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
population:
  who: "Not a study of human subjects; this is a book review whose subject (Pedhazur & Schmelkin's textbook) targets social-science graduate students and researchers as its intended audience."
  where: []
  when: null
  n: null
  sector: ["academia"]
  sample_notes: >
    No sample; this is a single reviewer's (Simon Day, Lilly Research Centre) critical
    appraisal of a research-methods textbook, appearing alongside two other unrelated book
    reviews on the same journal page (survival analysis; factor analysis in natural
    sciences).
limitation:
  primary: "This is an opinion-based book review with no original empirical data, sample, or SNH-relevant measures; it cannot support substantive claims about social network health, remote work, or wellbeing."
  others:
    - "The markdown conversion is truncated mid-sentence partway through an unrelated adjacent review (Applied Factor Analysis in the Natural Sciences), indicating incomplete OCR capture of the source page."
    - "Reflects a single reviewer's subjective assessment of a 1991 textbook, with no independent verification of the critique's fairness or accuracy."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Not SNH evidence itself, but a critical appraisal of a foundational
  measurement/design/analysis methods textbook (Pedhazur & Schmelkin) that SNH researchers
  might otherwise cite for guidance on scale validation, reliability, or quasi-experimental
  design; the review flags that its design-methods coverage is thinner than expected, which
  is a useful caveat before relying on it for SNH study design choices.
tags:
  topic: ["methodology", "measurement"]
  method: ["theory"]
  population: ["academic-researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Day (1994) - Review of Measurement Design and Analysis - An Integrated Approach/Day (1994) - Review of Measurement Design and Analysis - An Integrated Approach.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Day (1994) - Review of Measurement Design and Analysis - An Integrated Approach.pdf"
  notes: null

---

id: "demerouti-2001-the-job-demands-resources-model-of"
title: "The job demands-resources model of burnout."
authors:
  - "Demerouti, Evangelia"
  - "Bakker, Arnold B."
  - "Nachreiner, Friedhelm"
  - "Schaufeli, Wilmar B."
year: 2001
doi: "10.1037/0021-9010.86.3.499"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 86, issue: 3, pages: "499-512"}
citation: "Demerouti et al. (2001). The job demands-resources model of burnout.. Journal of Applied Psychology, 86(3), 499-512. https://doi.org/10.1037/0021-9010.86.3.499"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This foundational study tests the job demands-resources (JD-R) model of burnout across 374
  employees in 21 job positions spanning human services (teachers, nurses), industry
  (assembly-line workers), and transport (air traffic controllers). Using both self-reports
  and independent observer ratings of working conditions, it finds that job demands predict
  exhaustion while job resources predict disengagement, and validates the two-factor
  Oldenburg Burnout Inventory (OLBI) as invariant across occupations, extending burnout
  research beyond the human services. The paper's core theoretical move is separating
  exhaustion (driven by workload) from disengagement (driven by resource scarcity) as
  distinct pathways rather than a single burnout continuum.
claims:
  - text: "Job demands were strongly and positively related to exhaustion (self-report gamma = .91, p < .05) but not to disengagement (gamma = .07, ns), while job resources were strongly and negatively related to disengagement (gamma = -.72, p < .05) but not to exhaustion (gamma = .04, ns); the model explained 82% of variance in exhaustion and 52% in disengagement."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["workload", "social-support", "autonomy"]
  - text: "Observer ratings of job conditions (independent of employee self-reports) replicated the same pattern: job demands to exhaustion and job resources to disengagement were both significant and in the predicted direction, and models restricted to only these two paths fit the data as well as more complex alternatives, arguing against pure common-method bias."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout"]
    predictors: ["workload", "social-support"]
  - text: "Confirmatory factor analyses showed the two-factor structure of the Oldenburg Burnout Inventory (exhaustion and disengagement, r = .39 between factors) was invariant (equal factor loadings) across human service, transport, and industry occupational groups (total N = 352), supporting burnout as a construct that generalizes beyond human-service work."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout"]
    predictors: ["workload", "sampling-method"]
population:
  who: "374 employees across 21 job positions in northern Germany: teachers and nurses (human services), assembly-line/production and control-room workers (industry), and air traffic controllers (transport)"
  where: ["Germany"]
  when: null
  n: 374
  sector: ["healthcare", "manufacturing", "transportation", "education"]
  sample_notes: >
    Recruited via 12 organizations after informational meetings; 56% questionnaire response
    rate (54-62% across subsamples); not randomly sampled from the universe of jobs, but
    deliberately heterogeneous across occupation types; a subset of 21 job prototypes was
    independently rated by trained observers (interrater reliabilities .87-.96) to cross-
    validate self-report findings.
limitation:
  primary: "Cross-sectional design means the demands-to-exhaustion and resources-to-disengagement relationships cannot be interpreted causally; the authors explicitly call for longitudinal and quasi-experimental designs to confirm the causal structure."
  others:
    - "Non-random, convenience sampling of organizations and job positions limits generalizability, though heterogeneity across occupation types partly offsets this."
    - "Self-report and observer-rating scales for individual working conditions used only 1-3 items each, limiting internal-consistency reliability of specific job-demand/resource measures."
    - "Observer-rating analyses used the job (N=21) rather than individual as the unit of analysis, which is underpowered for structural equation modeling and the authors flag results as exploratory/indicative only."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational burnout-mechanism paper for the SNH project: it gives a validated,
  parsimonious causal model (workload/demands -> exhaustion; lack of social/organizational
  resources -> disengagement) that can structure how the project separates 'overwork'
  burnout from 'disconnection/cynicism' burnout in remote and open-source contexts, and
  supports treating supervisor support and job control as protective resources distinct from
  workload reduction.
tags:
  topic: ["burnout", "wellbeing", "measurement", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["healthcare-workers", "manufacturing-workers", "mixed-occupations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Demerouti et al. (2001) - The Job Demands-Resources Model of Burnout.pdf"
  notes: null

---

id: "dingel-2020-how-many-jobs-can-be-done"
title: "How Many Jobs Can be Done at Home?"
authors:
  - "Dingel, Jonathan"
  - "Neiman, Brent"
year: 2020
doi: "10.3386/w26948"
venue: {type: "report", name: null, volume: null, issue: null, pages: null}
citation: "Dingel et al. (2020). How Many Jobs Can be Done at Home?.. https://doi.org/10.3386/w26948"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Dingel and Neiman classify nearly 1,000 US occupations as feasible or infeasible to
  perform entirely from home using O*NET Work Context and Generalized Work Activities survey
  items (e.g., outdoor work, physical activity, public-facing tasks), then merge this
  classification with BLS employment and wage data and, for 85 other countries, ILO
  employment data. They find 37% of US jobs (46% of wages) can be done entirely at home,
  that this share rises steeply with a country's per-capita income, and that within the US
  it correlates strongly with metro-area education and income levels. The paper supplies the
  widely-used structural measure of "who can work remotely at all," as distinct from who
  actually does.
claims:
  - text: "37% of jobs in the United States can be performed entirely at home, accounting for 46% of all US wages, with sharp variation by occupation (near 100% for computer/math and legal occupations, near 0% for construction, food service, and production occupations)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Applying the classification to 85 other countries via ILO employment data shows lower-income economies have a far lower share of feasible work-from-home jobs; countries with per-capita GDP below one-third of the US level have roughly half as many WFH-feasible jobs (e.g., under 25% in Mexico and Turkey vs. over 40% in Sweden and the UK)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["remote-work-intensity"]
    predictors: ["remote-work-intensity"]
  - text: "Across the 100 largest US metropolitan areas, the share of jobs that can be done at home is strongly positively correlated with median household income (r=0.53) and share of residents with a college degree (r=0.71), and negatively correlated with homeownership rate (r=-0.31) and share of residents who are white (r=-0.12)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["remote-work-intensity"]
    predictors: ["remote-work-intensity", "sampling-method"]
population:
  who: "Nearly 1,000 US occupational categories (SOC codes) classified via O*NET survey responses (median ~25-26 respondents per question per occupation), merged with BLS 2018 Occupational Employment Statistics; classification then applied to occupational employment counts in 85 additional countries via ILO data."
  where: ["United States", "85 other countries (via ILO/ISCO mapping)"]
  when: "O*NET release 24.2; BLS 2018 Occupational Employment Statistics; ILO employment data for 2015 or later; analysis conducted mid-2020"
  n: null
  sector: []
  sample_notes: >
    Not a survey of individual workers; it is an occupation-level classification covering
    essentially the full US labor force by SOC code, cross-walked to 2-digit ISCO codes for
    international comparison. Authors validate the O*NET-derived classification against an
    independent manual assignment (85% agreement). Classification is estimated using US
    task/context data and extrapolated to other countries without adjusting for how
    occupations differ in content across economies.
limitation:
  primary: "The occupational feasibility classification is built entirely from US O*NET data and then mechanically applied to other countries, ignoring that the same occupation title may involve different tasks, technology, and infrastructure access across economies with different income levels."
  others:
    - "Measures theoretical/structural feasibility (an upper bound), not actual remote-work behavior; the paper itself notes far fewer workers report actually working entirely from home than the classification implies."
    - "Binary rule-based classification can misclassify specific occupations (e.g., 98% of teachers coded as WFH-feasible despite the practical difficulty of remote teaching)."
risk_of_bias: "low"
relevance_to_project: >
  Provides the standard structural measure of which occupations/sectors are even capable of
  remote work, letting the SNH project frame remote-work findings by feasibility and
  stratify by socioeconomic access (higher-income, higher-education occupations and metro
  areas have much greater WFH feasibility), which matters for interpreting who is exposed to
  remote-work-related isolation or connection effects versus who is structurally excluded
  from remote work.
tags:
  topic: ["remote-work", "measurement", "methodology"]
  method: ["secondary-data", "cross-sectional"]
  population: ["general-workforce", "cross-national"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Dingel & Neiman (2020) - How Many Jobs Can Be Done at Home.pdf"
  notes: null

---

id: "song-2018-does-telework-stress-employees-out-a"
title: "Does Telework Stress Employees Out? A Study on Working at Home and Subjective Well-Being for Wage/Salary Workers"
authors:
  - "Song, Younghwan"
  - "Gao, Jia"
year: 2018
doi: "10.2139/ssrn.3301758"
venue: {type: "journal", name: "SSRN Electronic Journal", volume: null, issue: null, pages: null}
citation: "Song et al. (2018). Does Telework Stress Employees Out? A Study on Working at Home and Subjective Well-Being for Wage/Salary Workers. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3301758"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using individual fixed-effects models on 11,793 diary-day activity episodes from 3,962 US
  wage/salary workers in the 2010/2012/2013 American Time Use Survey Well-Being Modules,
  this paper finds that working at home has a net negative effect on instantaneous
  subjective well-being rather than the stress-relief benefit often claimed for telework.
  Bringing work home on weekdays is associated with lower happiness, and telework (on both
  weekdays and weekends/holidays) is associated with higher stress relative to working in
  the workplace, with effects concentrated among parents, especially fathers.
claims:
  - text: "In fixed-effects models, bringing work home on weekdays is associated with a 0.330-point drop in happiness (p<.05) relative to working in the workplace, and telework on weekdays is associated with a 0.298-point increase in stress (p<.05), on a 0-6 instantaneous affect scale."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "stress"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Telework on weekends/holidays is also associated with higher stress (0.494-point increase, p<.05) relative to working in the workplace, indicating no measurable stress benefit from working at home even outside normal business hours; the study finds no significant beneficial effect of any form of homeworking on any well-being measure."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["remote-work-intensity"]
  - text: "Effects are heterogeneous by parental status and gender: fathers bringing work home on weekdays report 0.585-point lower happiness, 0.350-point higher pain, and 0.314-point higher sadness (all p<.05), and 0.500-point higher stress when teleworking; mothers report lower stress but higher tiredness when bringing work home weekdays and lower happiness when teleworking weekdays, while childless workers show little difference on weekdays but childless females report higher stress (0.901, p<.05) when teleworking on weekends/holidays."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing", "work-life-balance"]
    predictors: ["boundary-management", "remote-work-intensity"]
population:
  who: "Full-time, non-self-employed US wage/salary workers aged 18-65 who reported at least one work episode on their diary day"
  where: ["United States"]
  when: "2010, 2012, and 2013 (American Time Use Survey Well-Being Modules)"
  n: 3962
  sector: ["general-workforce"]
  sample_notes: >
    11,793 activity episodes (up to 3 per respondent) from 3,962 respondents after dropping
    missing data and single-episode respondents; nationally representative ATUS sampling
    frame but very small subsamples for bringing-work-home episodes (as few as 51-179),
    especially in gender/parental-status subgroup analyses, limiting power for those
    breakdowns; only one respondent per household interviewed, so no couples in the sample.
limitation:
  primary: "Telework vs. bringing-work-home is inferred indirectly from commuting patterns rather than asked directly, so some episodes (especially on weekends/holidays) are likely misclassified between the two homeworking types."
  others:
    - "Individual fixed-effects models cannot rule out unobserved confounders that vary across the small number of within-day episodes, even though many activity-level controls are included."
    - "Subsample sizes for bringing-work-home episodes are very small (e.g., 51 weekend episodes), producing wide confidence intervals for several heterogeneity estimates."
    - "Findings are specific to full-time wage/salary workers and instantaneous (episode-level) affect on a single diary day, which may not generalize to sustained remote-work experience or to self-employed/gig workers."
risk_of_bias: "low"
relevance_to_project: >
  Provides quasi-causal (fixed-effects) evidence that remote/telework is associated with
  higher momentary stress and that informal after-hours homework reduces happiness, directly
  informing the SNH project's design assumption that flexibility alone does not guarantee
  well-being and that boundary-management supports (childcare, defined work hours,
  workspace) may be needed to offset telework's stress costs, particularly for parents.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing", "measurement"]
  method: ["fixed-effects", "secondary-data", "quantitative"]
  population: ["remote-workers", "parents", "gender-differences"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Does Telework Stress Employees Out_ A Study on Working at Home and Subjective Well‐Being for Wage_Salary Workers/Does Telework Stress Employees Out_ A Study on Working at Home and Subjective Well‐Being for Wage_Salary Workers.md"
  pdf: null
  notes: null

---

id: "berger-2023-does-work-life-boundary-management-improve"
title: "Does work-life boundary management improve work-life balance for remote workers: A critically appraised topic"
authors:
  - "Berger, Danyelle L"
year: 2023
doi: "10.28953/2375-8643.1128"
venue: {type: "journal", name: "Engaged Management ReView", volume: 7, issue: 1, pages: null}
citation: "Berger (2023). Does work-life boundary management improve work-life balance for remote workers: A critically appraised topic. Engaged Management ReView, 7(1). https://doi.org/10.28953/2375-8643.1128"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This critically appraised topic (CAT) synthesizes five peer-reviewed studies (interview
  samples as small as 11, survey samples as large as ~7,000) on whether managing
  work/personal-life boundaries improves work-life balance for remote workers. It concludes
  that both firm, ongoing boundary management and occasional, employee-initiated temporary
  permeation of those boundaries are associated with better work-life balance, whereas
  failing to manage boundaries -- often driven by 'always-on' technology or unfamiliarity
  with flexible schedules -- is associated with worse work-life balance and, in one study,
  higher attrition.
claims:
  - text: "In 3 of the 5 reviewed studies, remote workers who established and maintained strict boundaries between work and personal time reported improved work-life balance and better integration of the two domains (Grant et al. 2013; Moore 2006; Irawanto et al. 2021)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "job-satisfaction"]
    predictors: ["boundary-management"]
  - text: "Two studies found that allowing temporary, employee-initiated permeation of work/personal boundaries -- to address childcare, eldercare, or other personal needs -- also improved work-life balance, via the flexibility remote work affords (Bellmann & Hübler 2021; Pillai & Prasad 2023)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["boundary-management", "autonomy"]
  - text: "All five studies found that non-management of work/personal boundaries -- driven by 'always-on' technology access, family distractions in the home, or lack of experience with non-fixed schedules -- negatively affected work-life balance; one study linked the added stress of managing this boundary to increased attrition among remote workers (Pillai & Prasad 2023)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "turnover", "stress"]
    predictors: ["boundary-management", "technostress"]
population:
  who: "Five peer-reviewed empirical studies (qualitative, mixed-methods, and quantitative) on remote/telework workers' work-life boundary management, selected via systematic database search (Business Source Ultimate, SCOPUS) and MMAT quality appraisal."
  where: ["United Kingdom", "India", "England", "Europe", "Indonesia"]
  when: null
  n: null
  sector: ["cross-sector"]
  sample_notes: >
    Underlying studies' samples range from 11 interviewed UK remote workers to ~7,000 survey
    respondents across private-sector European companies; no included study was U.S.-based.
    Only 5 of 59 candidate articles met inclusion criteria (peer-reviewed, English, full-
    text, published since 2003, keyword 'work-life balance'), so the evidence base is narrow
    and narratively (not meta-analytically) synthesized by a single author.
limitation:
  primary: "As a single-author critically appraised topic drawing on only 5 heterogeneous studies (varying designs, countries, and sample sizes from 11 to ~7,000) with no meta-analytic pooling, the synthesis offers limited precision and generalizability."
  others:
    - "No included study was based in the United States, limiting applicability to that context."
    - "No independent second reviewer is described for study screening, coding, or theme extraction, raising risk of single-rater bias."
    - "The author notes no studies found a negative effect of boundary management, flagging this as a possible gap in the underlying literature rather than confirmed absence of harm."
risk_of_bias: "medium"
relevance_to_project: >
  Provides synthesized evidence that it is boundary-management behavior -- not remote-work
  status per se -- that predicts work-life balance, supporting SNH design choices that favor
  flexible-but-intentional boundary-setting features (e.g., allowing deliberate, employee-
  controlled temporary overlap) over rigid always-separate or always-available defaults.
tags:
  topic: ["remote-work", "work-life-balance", "methodology"]
  method: ["review-systematic", "mixed-methods"]
  population: ["remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Does Work-Life Boundary Management Improve Work-Life Balance for Remote Workers - A Critically Appraised Topic/Does Work-Life Boundary Management Improve Work-Life Balance for Remote Workers - A Critically Appraised Topic.md"
  pdf: "papers/Remote Workers/Does Work-Life Boundary Management Improve Work-Life Balance for Remote Workers - A Critically Appraised Topic.pdf"
  notes: null

---

id: "bloom-2015-does-working-from-home-work-evidence"
title: "Does Working from Home Work? Evidence from a Chinese Experiment *"
authors:
  - "Bloom, Nicholas"
  - "Liang, James"
  - "Roberts, John"
  - "Ying, Zhichun Jenny"
year: 2015
doi: "10.1093/qje/qju032"
venue: {type: "journal", name: "The Quarterly Journal of Economics", volume: 130, issue: 1, pages: "165-218"}
citation: "Bloom et al. (2015). Does Working from Home Work? Evidence from a Chinese Experiment *. The Quarterly Journal of Economics, 130(1), 165-218. https://doi.org/10.1093/qje/qju032"
article_type: "empirical"
method: {design: "rct", approach: "experiment", evidence_level: "very-strong", preregistered: false}
gist: >
  This is the landmark Ctrip field experiment (Bloom, Liang, Roberts, and Ying, QJE 2015):
  249 call-center volunteers were randomized by odd/even birthdate to work from home four
  days a week or stay fully office-based for nine months. Home working raised performance
  13% (9% from more minutes worked per shift via fewer breaks/sick days, 4% from more calls
  per minute in a quieter environment), cut attrition by half, and raised self-reported
  satisfaction, but cut promotion rates conditional on performance by roughly half. When
  Ctrip later let everyone choose their location, over half of participants switched (many
  citing loneliness), and selection effects nearly doubled the measured gain to 22%.
claims:
  - text: "Working from home increased overall employee performance by 13% (0.232 SD, p<0.01) during the nine-month RCT, with 9.2% coming from more minutes worked per shift (fewer breaks, sick days, and late starts) and about 3.3-4% from more calls handled per minute, attributed to a quieter home environment."
    evidence: "rct"
    support_strength: "very-strong"
    outcomes: ["productivity", "performance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Attrition among home workers fell to 17% versus 35% for the office-based control group over the experimental period (about a 50% relative reduction), and home workers reported significantly higher satisfaction, more positive attitude, and less work exhaustion on weekly surveys."
    evidence: "rct"
    support_strength: "very-strong"
    outcomes: ["turnover", "retention", "job-satisfaction", "burnout"]
    predictors: ["remote-work-intensity"]
  - text: "Working from home was associated with about a 50% lower promotion rate conditional on performance, and after the experiment ended over half of treatment-group volunteers and two-thirds of control-group volunteers who could freely choose declined to work from home, most citing loneliness and lack of social contact as the reason."
    evidence: "rct"
    support_strength: "strong"
    outcomes: ["turnover", "loneliness", "sense-of-belonging"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "996 call-center order-takers/placers/correctors in the airfare and hotel departments of Ctrip's Shanghai call center (a NASDAQ-listed, 16,000-employee Chinese travel agency); 249 volunteers who met eligibility (6+ months tenure, home broadband, private room) were randomized 131 treatment / 118 control."
  where: ["China"]
  when: "December 2010-August 2011 (nine-month experiment), with performance/attrition/promotion data followed through September 2012 and a follow-up survey in May 2013"
  n: 249
  sector: ["call-center", "travel-industry", "corporate"]
  sample_notes: >
    51% of the 994 eligible employees volunteered for WFH; randomization was by odd/even
    birthdate in a public lottery. Treatment/control balance was good (only 1 of 18
    characteristics differed at 5%, joint F-test p=.466). Findings are specific to a single
    large Chinese firm's routinized, individually-monitored call-center job and may not
    generalize to work requiring teamwork or less quantifiable output.
limitation:
  primary: "External validity is limited to highly routinized, individually monitored, easily quantified jobs (call-center work) at a single firm with an unusually comprehensive performance-tracking system; the authors explicitly caution the results may not extend to jobs requiring teamwork or in-person collaboration."
  others:
    - "Compliance with assigned WFH status was imperfect (80-90% of treatment group actually worked from home), so estimates are intention-to-treat rather than pure treatment-on-the-treated."
    - "Differential attrition (worse performers in the control group were more likely to quit) likely biases the estimated treatment effect downward, per the authors' own bounding analysis, though this does not undermine the main findings."
    - "Loneliness/isolation is documented only via employees' stated reasons for switching back to the office and satisfaction surveys, not a validated loneliness or social-support instrument."
risk_of_bias: "low"
relevance_to_project: >
  This is a rare randomized-controlled-trial-quality causal estimate that remote work can
  raise both productivity and satisfaction while measurably increasing loneliness and
  reducing promotion visibility -- directly informing the SNH project's core tension between
  remote-work benefits and social-connection/career-visibility costs, and giving a
  quantified, RCT-grade baseline (halved attrition, reduced promotion, loneliness-driven
  reselection) for any design or measurement work on remote-worker social health.
tags:
  topic: ["remote-work", "job-satisfaction", "productivity", "loneliness", "isolation"]
  method: ["rct"]
  population: ["call-center-workers", "china", "corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/DOES WORKING FROM HOME WORK_ EVIDENCE FROM  A CHINESE EXPERIMENT.pdf"
  notes: null

---

id: "dourish-1992-awareness-and-coordination-in-shared-workspaces"
title: "Awareness and coordination in shared workspaces"
authors:
  - "Dourish, Paul"
  - "Bellotti, Victoria"
year: 1992
doi: "10.1145/143457.143468"
venue: {type: "conference", name: "Proceedings of the 1992 ACM conference on Computer-supported cooperative work  - CSCW '92", volume: null, issue: null, pages: "107-114"}
citation: "Dourish et al. (1992). Awareness and coordination in shared workspaces. Proceedings of the 1992 ACM conference on Computer-supported cooperative work  - CSCW '92, 107-114. https://doi.org/10.1145/143457.143468"
article_type: "empirical"
method: {design: "case-study", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  The paper reports a video-based observational case study of ShrEdit, a synchronous shared-
  editor used by four groups of designers working in separate, video/audio-linked locations
  on a 90-minute design task. It argues that 'passive shared feedback' -- seeing
  collaborators' text input directly in the shared workspace, with no explicit roles,
  annotations, or informational messaging -- let groups fluidly shift between independent
  and tightly coordinated work, self-organize authorship conventions, and maintain low-
  overhead mutual awareness, avoiding costs the authors identify in role-restrictive and
  informational CSCW systems like Quilt, PREP, and GROVE.
claims:
  - text: "Groups using ShrEdit's unstructured shared workspace (no roles, access control, or explicit annotation) were nonetheless able to negotiate and adapt their individual contributions to the group's context, moving opportunistically between concurrent independent work, loose coordination, and tightly focused joint discussion, relying on passive observation of each other's typed input plus concurrent speech."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration", "communication", "social-presence"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Explicit awareness features built into ShrEdit ('find' and 'track,' which let a user jump to or continuously mirror a collaborator's view) were rarely used; in debriefing, designers said this was due to interface clumsiness, and instead relied on asking aloud where others were or on informally devised conventions (e.g., an indexing/indentation scheme) to locate and interpret each other's work."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure"]
  - text: "Without any imposed role structure, one group spontaneously assigned each participant a personally 'owned' shared window that only they could type into but everyone could read, and warned each other before editing sections seen as another's work -- illustrating that awareness of authorship and dynamic role negotiation emerged bottom-up from the shared, visible workspace rather than from formal system-enforced roles."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration"]
    predictors: ["team-cohesion", "network-structure"]
population:
  who: "Four groups of three professional/experienced designers each (all with prior experience working together), placed in separate locations linked by audio/video to simulate remote collaboration, using the ShrEdit shared text editor for a 90-minute open-ended design task (plus two 20-minute practice tasks) followed by a debriefing interview"
  where: []
  when: null
  n: 12
  sector: ["software-development", "hci-research"]
  sample_notes: >
    Very small, non-random convenience sample (4 groups, 12 designers total, ShrEdit study
    run in collaboration with Judy and Gary Olson); country/institution and exact study
    dates not stated in this conversion, only the paper's 1992 publication venue (CSCW '92).
    Analysis restricted to video-recorded behavior on the final design problem plus
    qualitative debriefing comments, with no reported inter-rater reliability or coding
    scheme detail.
limitation:
  primary: "Findings rest on a very small, non-randomly-sampled set of 4 designer groups (12 people) using one specific 1992-era synchronous editor on one lab-assigned design task, which limits generalizability to real distributed/remote work settings and to modern asynchronous collaboration tools."
  others:
    - "The competing systems (Quilt, PREP, GROVE) are discussed conceptually from the literature, not empirically tested head-to-head against ShrEdit, so the claimed superiority of 'shared feedback' is argued rather than directly measured."
    - "No systematic coding methodology, inter-rater reliability, or quantitative outcome measures are reported for the video analysis; conclusions are drawn from illustrative transcript excerpts and debriefing quotes."
    - "The 'remote' condition simulated separation via audio/video links in a controlled study, which differs materially from real-world distributed teams with asynchronous schedules, varying tools, and organizational context."
risk_of_bias: "high"
relevance_to_project: >
  This is a foundational CSCW paper arguing that low-effort, passively-observed 'shared
  feedback' in a common workspace supports mutual awareness and coordination more cheaply
  than explicit role assignment or informational messaging -- directly relevant to designing
  lightweight presence/awareness signals (e.g., activity feeds, live cursors, status
  indicators) meant to reduce coordination overhead and isolation for distributed/remote
  teams without imposing rigid process structure.
tags:
  topic: ["collaboration", "remote-work", "social-presence", "methodology"]
  method: ["case-study", "qualitative"]
  population: ["knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Dourish & Bellotti (1992) - Awareness and Coordination in Shared Workspaces/Dourish & Bellotti (1992) - Awareness and Coordination in Shared Workspaces.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Dourish & Bellotti (1992) - Awareness and Coordination in Shared Workspaces.pdf"
  notes: null

---

id: "dourish-1992-portholes"
title: "Portholes"
authors:
  - "Dourish, Paul"
  - "Bly, Sara"
year: 1992
doi: "10.1145/142750.142982"
venue: {type: "conference", name: "Proceedings of the SIGCHI conference on Human factors in computing systems  - CHI '92", volume: null, issue: null, pages: "541-547"}
citation: "Dourish et al. (1992). Portholes. Proceedings of the SIGCHI conference on Human factors in computing systems  - CHI '92, 541-547. https://doi.org/10.1145/142750.142982"
article_type: "empirical"
method: {design: "case-study", approach: "ethnography", evidence_level: "weak", preregistered: false}
gist: >
  Describes Portholes, a 1992 CSCW media-space system that shares regularly-updated snapshot
  images (plus e-mail/audio 'snippet' links) between two distributed Xerox research sites to
  support passive awareness of remote colleagues. Based on informal field observation plus a
  3-day diary/questionnaire with the system's early users, the authors report that people
  used Portholes both as a lightweight information tool (checking colleague availability,
  predicting free time) and as a shared community space (informal 'sightings', personal
  audio snippets), and that use coincided with increased informal, unprompted cross-site
  communication and a reported sense of connection despite few prior direct interactions
  between the two sites.
claims:
  - text: "Of 15 users asked to log Portholes use over a 3-day period and complete a questionnaire, 11 responded, and all but one reported using the pvc and/or edison clients at least a few times a day during that period."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["social-presence", "collaboration"]
    predictors: ["network-structure"]
  - text: "Users described two main modes of use -- Portholes as an information tool (quickly checking a remote colleague's availability to avoid wasted visits/calls) and Portholes as a community (seeing colleagues arrive/leave, sharing whimsical audio 'snippets', 'feeling some connection' to people at the remote site), including one exchange where a Saturday worker messaged 'It's nice to know I'm not completely alone!'"
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["sense-of-belonging", "isolation", "communication"]
    predictors: ["social-support"]
  - text: "Authors report that informal, unprompted cross-site communication among the ~22 distributed users (10 at PARC, 12 at EuroPARC) increased after Portholes deployment, and server statistics collected four months after the initial questionnaire indicated participants remained regular users."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["communication", "collaboration"]
    predictors: ["network-structure", "embodiment"]
population:
  who: "Members of two linked media-space research groups using the Portholes awareness system: 10 users at Xerox PARC (Palo Alto) and 12 at Rank Xerox EuroPARC (Cambridge, UK); a 15-person subset was asked to diary/answer a questionnaire, of whom 11 responded."
  where: ["USA", "UK"]
  when: "1991-1992"
  n: 22
  sector: ["technology"]
  sample_notes: >
    Convenience sample of the researchers' own colleagues and lab members who were early
    adopters of an in-house prototype; questionnaire response rate 11/15; authors are also
    the system's designers, so evaluation is informal, anecdotal, and self-selected rather
    than a controlled study.
limitation:
  primary: "Extremely small, self-selected sample (22 total users, 11 questionnaire respondents) evaluated with informal/anecdotal field observations and a short 3-day diary period, with no control condition or validated outcome measures, so claims about awareness fostering community are suggestive rather than demonstrated."
  others:
    - "Authors are also the system's designers and site colleagues of the participants, creating potential evaluator/social-desirability bias."
    - "No standardized measures of loneliness, belonging, or wellbeing were used -- evidence is qualitative quotes and usage anecdotes."
    - "Early-stage prototype with reliability problems (unreliable images, slow updates) that participants themselves flagged as limiting use, confounding assessment of the awareness concept itself."
risk_of_bias: "high"
relevance_to_project: >
  A foundational CSCW paper for the SNH project's interest in ambient/passive-awareness
  features (presence indicators, activity feeds) as a design lever for reducing remote-
  worker isolation: it offers early qualitative evidence that low-bandwidth awareness of
  distributed colleagues can increase informal communication and produce a subjective 'sense
  of community,' but with weak methodological rigor that should temper how strongly the
  project cites it as causal evidence.
tags:
  topic: ["remote-work", "social-presence", "community-health", "isolation", "collaboration"]
  method: ["qualitative", "case-study"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Dourish & Bly (1992) - Portholes - Supporting Awareness in a Distributed Work Group.pdf"
  notes: null

---

id: "duxbury-1994-work-family-conflict"
title: "Work-Family Conflict"
authors:
  - "DUXBURY, LINDA"
  - "HIGGINS, CHRISTOPHER"
  - "LEE, CATHERINE"
year: 1994
doi: "10.1177/019251394015003006"
venue: {type: "journal", name: "Journal of Family Issues", volume: 15, issue: 3, pages: "449-466"}
citation: "DUXBURY et al. (1994). Work-Family Conflict. Journal of Family Issues, 15(3), 449-466. https://doi.org/10.1177/019251394015003006"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a large Canadian survey of 1,989 dual-income and single-parent employees with
  children ages 6-12, this study tests whether gender, family type, and perceived control
  predict role overload and work-family interference. Perceived control (drawn from
  Karasek's job strain model) was the strongest and most consistent predictor: low-control
  individuals had significantly higher overload and interference regardless of time actually
  spent in work or family roles. Women reported more overload and more work-to-family
  interference than men despite spending fewer hours at work, and single parents did not
  differ from married parents on overload or family-to-work interference, contradicting the
  rational (time-based) model of work-family conflict.
claims:
  - text: "Individuals with low perceived control had significantly higher levels of role overload [F(1,1981)=113.0, p<.001], work-to-family interference [F(1,1981)=87.3, p<.001], and family-to-work interference [F(1,1981)=79.4, p<.001] than those with high control, despite similar time spent in work and family roles."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["autonomy", "workload"]
  - text: "Women had significantly higher role overload than men, F(1,1981)=66.8, p<.001, and significantly higher work-to-family interference, F(1,1981)=7.1, p<.01 -- the latter opposite the hypothesized direction and contrary to the rational (hours-based) model, since women spent fewer hours in work activities than men."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["workload"]
  - text: "Single parents did not differ from married/dual-income parents in role overload or family-to-work interference (both hypotheses unsupported), and time-use data showed single parents spent the same total hours in work and family activities as married parents, undercutting the assumption that single parenthood inherently increases role demands."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["workload"]
population:
  who: "Full-time employed Canadian parents (federal public-sector and large private-sector organizations) with children aged 6-12 living at home full-time; married/dual-income and single-parent, male and female"
  where: ["Canada"]
  when: null
  n: 1989
  sector: ["public-sector", "private-sector", "general-workforce"]
  sample_notes: >
    Drawn from a larger 20,836-respondent Canadian work-family survey (56% average response
    rate across 7 government departments and 37 private organizations); restricted to 1,989
    respondents meeting full-time employment and child-age criteria. Male single parents
    were a relatively small subgroup (n=107 combined low/high control), noted by the authors
    as a limitation.
limitation:
  primary: "The perceived-control measure was not a validated instrument -- four items were extracted from Cohen, Kamarck & Mermelstein's (1983) perceived stress scale rather than a purpose-built control scale, and its reliability (alpha=.61) fell below acceptable standards even as a dichotomized independent variable."
  others:
    - "Interference subscales had relatively low Cronbach's alphas (.67 and .69), below Nunnally's .7 guideline for exploratory research."
    - "Small number of male single parents limited power for some subgroup comparisons."
    - "Cross-sectional design (1994, pre-remote-work era) cannot establish causal direction between control and conflict, and findings on a 1990s Canadian salaried workforce may not generalize to contemporary remote/hybrid work arrangements."
risk_of_bias: "low"
relevance_to_project: >
  Directly supports the SNH project's emphasis on autonomy/control as a protective factor:
  it shows perceived control over work and family demands predicts role strain and
  interference independent of actual time invested, which is a mechanism-level rationale for
  designing remote/hybrid work policies (flexible scheduling, autonomy over when/where work
  happens) rather than assuming reduced hours alone will lower burnout or work-life
  conflict.
tags:
  topic: ["work-life-balance", "wellbeing"]
  method: ["cross-sectional", "survey"]
  population: ["general-workforce", "parents"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/duxbury-et-al-1994-work-family-conflict-a-comparison-by-gender-family-type-and-perceived-control/duxbury-et-al-1994-work-family-conflict-a-comparison-by-gender-family-type-and-perceived-control.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/duxbury-et-al-1994-work-family-conflict-a-comparison-by-gender-family-type-and-perceived-control.pdf"
  notes: null

---

id: "eby-2005-work-and-family-research-in-io"
title: "Work and family research in IO/OB: Content analysis and review of the literature (1980–2002)"
authors:
  - "Eby, Lillian T."
  - "Casper, Wendy J."
  - "Lockwood, Angie"
  - "Bordeaux, Chris"
  - "Brinley, Andi"
year: 2005
doi: "10.1016/j.jvb.2003.11.003"
venue: {type: "journal", name: "Journal of Vocational Behavior", volume: 66, issue: 1, pages: "124-197"}
citation: "Eby et al. (2005). Work and family research in IO/OB: Content analysis and review of the literature (1980–2002). Journal of Vocational Behavior, 66(1), 124-197. https://doi.org/10.1016/j.jvb.2003.11.003"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This monograph content-analyzes 190 empirical work-family (WF) studies published in 14
  IO/OB journals from 1980-2002, coding each for study focus, direction of hypothesized
  effects, and predictor/criterion/mediator variables, then presents a narrative review
  organized into nine topical clusters (conflict, work role stress, work-family assistance
  programs including on-site childcare and work-at-home arrangements, work schedules,
  relocation, career outcomes, gender, dual-earner couples, cross-domain relationships). It
  concludes that IO/OB WF research is dominated by a conflict paradigm, under-theorized, and
  has largely neglected non-spouse sources of support and coping, offering an agenda for
  future research rather than new primary data.
claims:
  - text: "Across the reviewed studies, work-to-family conflict was consistently found to be more prevalent and more heavily studied than family-to-work conflict, and domain-specific spillover effects (work-to-work, family-to-family) were stronger and more consistent than cross-domain effects."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["workload", "boundary-management"]
  - text: "Only about 28% of the 170 predictive studies tested mediated relationships, and while work role stress and health/wellness were frequently studied, sources of support beyond spouse support (e.g., coworker, supervisor, and organizational support) were rarely examined -- a gap the authors explicitly flag despite an extensive literature linking support and coping to stress outcomes."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["social-support", "organizational-culture"]
  - text: "The two identified studies of work-at-home/telecommuting arrangements found mixed effects: supplemental computer-based work-at-home users reported greater task variety and job involvement but also higher role overload, stress, and work-family interference than non-users (Duxbury et al., 1996), while telecommuting satisfaction and self-reported productivity were positively related to supervisor technical/emotional support and favorable views of the performance-evaluation system, but more time spent telecommuting related to lower productivity (Hartman et al., 1991)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction", "productivity", "stress"]
    predictors: ["social-support", "remote-work-intensity", "leadership-style"]
population:
  who: "190 empirical (data-based) work-family studies published between 1980 and 2002 in 14 IO/OB journals (e.g., Journal of Vocational Behavior, Journal of Organizational Behavior, Journal of Applied Psychology, Academy of Management Journal); included both hypothesis/model-testing (n=170) and exploratory (n=20) studies with a work-domain and a family-domain variable."
  where: ["mixed, predominantly United States, with some international samples (e.g., Israel, Australia, United Kingdom, expatriate/international-relocation samples)"]
  when: "1980-2002"
  n: 190
  sector: ["mixed"]
  sample_notes: >
    Population is the corpus of published studies itself, not individual human subjects;
    underlying primary studies varied widely in sample type (nurses, managers, dual-earner
    couples, expatriates, etc.). Search was limited to IO/OB journals via PsycINFO/ABInform
    plus manual cross-referencing; theoretical articles, pure scale-development papers, and
    prior literature reviews were excluded from the 190.
limitation:
  primary: "This is a narrative content-analytic review, not a meta-analysis -- it catalogs which variables and relationships were studied but does not synthesize or compare effect sizes across studies, limiting quantitative comparability."
  others:
    - "Search restricted to 14 IO/OB journals, so WF findings published in family-studies, sociology, or counseling-psychology outlets are excluded and likely fill some of the 'gaps' the authors identify."
    - "Did not systematically catalog sample demographics, response rates, or methodological rigor of the 190 reviewed studies, limiting assessment of generalizability and risk of bias in the underlying literature."
    - "Coding of predictors/criteria/mediators into 18 meta-themes and 80 sub-themes involved subjective categorization by two raters, which could shift emphasis in the reported frequencies."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a 20-year baseline map of what IO/OB work-family research has and has not
  studied, explicitly identifying under-researched constructs --
  coworker/supervisor/organizational support, coping, and telecommuting -- that are central
  to the SNH project's remote-worker design questions; its early Duxbury et al. (1996) and
  Hartman et al. (1991) findings on work-at-home stress, overload, and supervisor-support
  effects are a useful historical anchor for how telecommuting/remote-work support
  mechanisms have been measured.
tags:
  topic: ["remote-work", "work-life-balance", "social-support", "methodology"]
  method: ["literature-review", "content-analysis"]
  population: ["dual-earner-couples", "working-parents", "organizational-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Eby et al. (2005) - Work and Family Research in IO-OB - Content Analysis and Review of the Literature 1980-2002/Eby et al. (2005) - Work and Family Research in IO-OB - Content Analysis and Review of the Literature 1980-2002.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Eby et al. (2005) - Work and Family Research in IO-OB - Content Analysis and Review of the Literature 1980-2002.pdf"
  notes: null

---

id: "luangnikone-2021-employee-motivation-in-remote-work-intrinsic"
title: "Employee Motivation in Remote Work: Intrinsic Motivation and Self-Efficacy's Role in Employee Motivation for Remote Environments"
authors:
  - "Luangnikone Davis, Jawan"
  - "Mo, Kevin"
year: 2021
doi: null
venue: {type: "thesis", name: "Linköping University", volume: null, issue: null, pages: null}
citation: "Luangnikone Davis et al. (2021). Employee Motivation in Remote Work: Intrinsic Motivation and Self-Efficacy's Role in Employee Motivation for Remote Environments. Linköping University."
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  This bachelor's thesis uses seven semi-structured interviews with engineers at two U.S.
  companies (an agile, autonomy-supportive 'Sim Co.' and a hierarchical, deadline-driven
  'Mech Co.') that shifted to full remote work during COVID-19 to examine
  intrinsic/extrinsic motivation (via self-determination theory) and self-efficacy. It finds
  intrinsic motivation (autonomy and competence) was strengthened by remote work while
  relatedness weakened, extrinsic incentives mattered less than task interest, and project
  burnout plus blurred work-life boundaries emerged as the main threats to motivation, with
  self-efficacy shifting mainly through reduced vicarious-experience opportunities and
  altered physiological/emotional states.
claims:
  - text: "Across both companies, employees reported that remote work increased perceived autonomy and (via a newly identified 'remote working competence' of concise communication, channel-switching, and self-motivation) competence, but weakened relatedness, with employees at the more controlling company (Mech Co.) describing distaste for inflexible deadlines and frequent evaluations versus employees at the more autonomy-supportive company (Sim Co.) integrating company values into personal identity (integrated regulation)."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["job-engagement", "sense-of-belonging", "communication"]
    predictors: ["autonomy", "leadership-style", "organizational-culture"]
  - text: "Extrinsic motivators (monetary incentives, overtime pay, formal deadlines) had minimal effect on motivation when a project itself was uninteresting to the employee, and interviewees at both firms reported that inherent interest in the work, not incentives, was the primary driver of remote task engagement."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["job-engagement"]
    predictors: ["autonomy", "workload"]
  - text: "Two sources of amotivation recurred across interviews — project disinterest and project burnout — with burnout attributed to the blurring of professional and personal life in remote settings; separately, self-efficacy shifted mainly through two of Bandura's four components: vicarious experience declined (fewer opportunities to observe/shadow colleagues remotely) while physiological/emotional states generally improved (lower reported stress), with performance accomplishment and social persuasion largely unchanged from in-office experience."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["burnout", "work-life-balance", "stress"]
    predictors: ["workload", "boundary-management", "remote-work-intensity"]
population:
  who: "Seven engineers (four at an IT/agile engineering firm 'Sim Co.', three at a mechanical engineering firm 'Mech Co.') who transitioned to full remote work in March 2020 due to COVID-19; recruited via direct email outreach (bottom-up, not through management)."
  where: ["United States"]
  when: "2021 (interviews conducted for a Spring 2021 thesis; respondents' remote transition began March 2020)"
  n: 7
  sector: ["engineering", "manufacturing", "information-technology"]
  sample_notes: >
    Very small, non-random, convenience sample of two U.S. engineering companies; one
    interviewee (of seven) was female; one interview was not audio-recorded (notes only) at
    the participant's request; authors explicitly caution against generalizing beyond the
    engineering industry.
limitation:
  primary: "Extremely small (n=7), non-random sample from only two companies in one industry (U.S. engineering), explicitly acknowledged by the authors as limiting generalizability beyond that context."
  others:
    - "Qualitative, researcher-interpreted verbatim coding with no inter-rater reliability check reported, raising risk of interpretive bias."
    - "Cross-sectional retrospective self-report shortly after a forced (not voluntary) transition to remote work, so findings may reflect early-pandemic adjustment rather than stable long-term remote-work motivation patterns."
    - "No comparison group of in-office (never-remote) employees; comparisons to office work rely on interviewees' recollections rather than measured baseline data."
risk_of_bias: "high"
relevance_to_project: >
  Offers a qualitative, mechanism-level account of how remote autonomy and reduced
  supervision can raise intrinsic motivation (autonomy, competence) while eroding
  relatedness/connectedness, and identifies project burnout plus blurred work-life
  boundaries as the main threats to remote worker motivation — useful for grounding SNH
  design hypotheses about which levers (autonomy support vs. relatedness-building
  interventions) matter most for remote worker wellbeing, though the small sample means it
  should inform hypothesis generation rather than serve as strong evidence.
tags:
  topic: ["remote-work", "job-engagement", "burnout", "work-life-balance"]
  method: ["qualitative", "interview"]
  population: ["engineers", "united-states", "covid-19-transition"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Employee Motivation in Remote Work - Intrinsic Motivation and Self-Efficacy in Remote Environments - Bachelor Thesis/Employee Motivation in Remote Work - Intrinsic Motivation and Self-Efficacy in Remote Environments - Bachelor Thesis.md"
  pdf: "papers/Remote Workers/Employee Motivation in Remote Work - Intrinsic Motivation and Self-Efficacy in Remote Environments - Bachelor Thesis.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "jamsen-2022-employees-perceptions-of-relational-communication-in"
title: "Employees’ perceptions of relational communication in full-time remote work in the public sector"
authors:
  - "Jämsen, Rasa"
  - "Sivunen, Anu"
  - "Blomqvist, Kirsimarja"
year: 2022
doi: "10.1016/j.chb.2022.107240"
venue: {type: "journal", name: "Computers in Human Behavior", volume: 132, issue: null, pages: "107240"}
citation: "Jämsen et al. (2022). Employees’ perceptions of relational communication in full-time remote work in the public sector. Computers in Human Behavior, 132, 107240. https://doi.org/10.1016/j.chb.2022.107240"
article_type: "empirical"
method: {design: "qualitative", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  An open-ended survey of 1,091 Finnish public sector employees during the first wave of
  COVID-19 full-time remote work identified 17 aspects of relational communication that
  changed, mentioned 956 times overall; 86% of mentions described remote work as a challenge
  to relational communication (lost coffee-break and hallway encounters, longing for
  coworkers, loneliness, isolation, reduced social support) versus 14% describing it as an
  opportunity (technology-enabled inclusion, more equal communication, control over
  interaction volume). Respondents clustered into three profiles - challenge (80%),
  opportunity (13%), and ambivalent (7%) - and none of the measured individual
  characteristics (gender, age, tenure, org size, leadership role, prior remote experience)
  distinguished which profile a person fell into.
claims:
  - text: "Of 956 total mentions of relational-communication change across 606 respondents, 86% (819 mentions) described remote work as a challenge to relational communication (e.g., loss of spontaneous encounters, informal breaks, longing for coworkers, loneliness/isolation, decreased social support), while only 14% (137 mentions) described it as an opportunity."
    evidence: "qualitative"
    support_strength: "moderate"
    outcomes: ["isolation", "loneliness", "social-presence", "wellbeing"]
    predictors: ["social-support", "remote-work-intensity", "sense-of-belonging"]
  - text: "Respondents split into three profiles: 487 (80% of the 606 who mentioned relational communication) found remote work purely a challenge, 76 (13%) found it purely an opportunity, and 43 (7%) reported ambivalent, mixed experiences of both challenge and opportunity."
    evidence: "qualitative"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging", "wellbeing", "communication"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "None of the measured individual characteristics (gender, age, tenure, organization size, leadership position, children in household, prior remote-work experience) differentiated which relational-communication profile respondents fell into; all characteristics were represented across all three groups in proportions similar to the full sample."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["job-engagement", "sense-of-belonging"]
    predictors: ["sampling-method", "remote-work-intensity"]
population:
  who: "Full-time Finnish public sector employees (government services, municipalities, semi-governmental organizations) with virtually no prior remote-work experience, who completed an open-ended online survey during the first wave of the COVID-19 pandemic"
  where: ["Finland"]
  when: "April 2020"
  n: 1091
  sector: ["public-sector"]
  sample_notes: >
    1,205 total respondents; 1,091 full-time public-sector employees retained for analysis.
    Recruited via press release, social media, and distribution through participating
    governmental organizations and labor unions; anonymous, self-selected convenience
    sample. 75% female, mean age 46, mean tenure 11 years; 91% had worked remotely no more
    than 2 days/week pre-pandemic. Of the 1,091, 606 (56%) mentioned relational-
    communication aspects and were the basis for the profile analysis; the questionnaire did
    not directly ask about relational communication (themes were data-driven/inductive).
limitation:
  primary: "Cross-sectional, single-timepoint data collected during an acute pandemic crisis makes it impossible to separate effects of the abrupt forced transition to remote work and general COVID-19 anxiety/stress from effects of remote work itself, and precludes tracking how perceptions evolved as remote work became routine."
  others:
    - "Self-selected, anonymous convenience sample recruited via press release and organizational distribution lists, with no response-rate data, limiting representativeness."
    - "Sample restricted to Finnish public-sector employees with minimal prior remote-work experience, limiting generalizability to other sectors (e.g., tech/startup employees) or to voluntary/hybrid remote-work arrangements."
    - "Relational communication themes were identified inductively from responses to unrelated open-ended questions rather than measured with validated instruments, so relative importance of the 17 aspects cannot be statistically weighted."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a large-sample, real-world account of which specific mechanisms (loss of
  spontaneous/informal encounters, coffee-break rituals, raised threshold to contact
  colleagues, reduced supervisor support) drive perceived isolation and loneliness when work
  shifts fully remote, and identifies technology-mediated small-group/breakout tools as a
  partial mitigation - directly informs SNH intervention design around replacing informal,
  unplanned interaction channels in remote and hybrid settings.
tags:
  topic: ["remote-work", "isolation", "loneliness", "social-support", "wellbeing", "community-health"]
  method: ["qualitative", "survey"]
  population: ["public-sector", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Employees Perceptions of Relational Communication in Full-Time Remote Work in the Public Sector/Employees Perceptions of Relational Communication in Full-Time Remote Work in the Public Sector.md"
  pdf: "papers/Remote Workers/Employees Perceptions of Relational Communication in Full-Time Remote Work in the Public Sector.pdf"
  notes: null

---

id: "jones-2022-factors-contributing-to-workplace-isolation-in"
title: "Factors Contributing to Workplace Isolation in Remote Workers"
authors:
  - "Jones, Yvette"
year: 2022
doi: null
venue: {type: "thesis", name: "Trevecca Nazarene University", volume: null, issue: null, pages: null}
citation: "Jones (2022). Factors Contributing to Workplace Isolation in Remote Workers. Trevecca Nazarene University."
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low", preregistered: false}
gist: >
  This doctoral dissertation surveyed U.S. remote workers (final analytic samples ranging
  from n=170 to n=229) using the Workplace Isolation Scale, Supervisory Support Scale, and
  Communication Satisfaction Questionnaire in a one-time online snowball-sample survey. It
  found moderate-to-strong negative correlations between workplace isolation and both
  supervisory support (r=.436, p<.001) and communication satisfaction (r=.591, p<.001),
  meaning isolation was lower when workers perceived more supervisor support and better
  communication, but found no relationship between isolation and tenure/length of time
  worked remotely (r=.032, ns). It contributes a direct empirical test of two modifiable
  organizational levers (supervisor support, communication quality) against workplace
  isolation in a large post-pandemic remote-worker sample.
claims:
  - text: "A Pearson r correlation between workplace isolation (M=52.29, SD=12.03) and supervisory support (M=22.34, SD=10.11) showed a significant, moderate, negative relationship, r(185)=.436, p<.001: as perceived supervisory support increased, workplace isolation decreased."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["isolation"]
    predictors: ["leadership-style", "social-support"]
  - text: "Workplace isolation and communication satisfaction (M=116.16, SD=47.30) were strongly and negatively correlated, r(169)=.591, p<.001, indicating that higher communication satisfaction was associated with markedly lower workplace isolation; supervisory support and communication satisfaction were themselves strongly positively correlated, r(169)=.616, p<.001."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["isolation", "communication"]
    predictors: ["social-support"]
  - text: "No significant relationship was found between workplace isolation and length of time worked remotely, r(201)=.032; among the 229 respondents (83% female), 65.5% began working remotely due to COVID-19, and respondents were almost evenly split on intent to return to office (47.6% no vs 45.9% yes)."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["isolation"]
    predictors: ["remote-work-intensity"]
population:
  who: "Adult (18+) remote workers employed in the United States or U.S. territories, recruited via the researcher's professional/personal networks using snowball sampling"
  where: ["United States"]
  when: "2022"
  n: 229
  sector: ["mixed/unspecified"]
  sample_notes: >
    Convenience/snowball sample distributed via SurveyMonkey; heavily skewed female (83% vs
    9.6% male, 7.4% no answer); job role 58.1% non-supervisory, 35.4% supervisory; mean age
    47.9 (SD=9.98, range 21-78); no pilot test was run before fielding, contributing to
    incomplete responses and variable degrees of freedom (n=170-229) across analyses;
    demographic items lacked non-binary/not-applicable response options and omitted race.
limitation:
  primary: "Correlational, single-timepoint, self-report design with a convenience/snowball sample cannot establish causal direction between supervisory support, communication satisfaction, and workplace isolation, and generalizability is limited by a demographically skewed (83% female), U.S.-only, unpiloted online survey."
  others:
    - "Survey was lengthy (three combined instruments plus demographics) and unpiloted, producing item non-response and shrinking analytic n for individual correlations (n=169-201) well below the total 229 respondents."
    - "Sample was drawn during the COVID-19 pandemic (66% began remote work due to COVID), which may have altered baseline isolation levels relative to voluntary, pre-pandemic remote work populations."
    - "Demographic questionnaire omitted race/ethnicity and used a binary gender item, limiting the ability to examine or rule out demographic confounds."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, validated-instrument evidence (Workplace Isolation Scale,
  Supervisory Support Scale, Communication Satisfaction Questionnaire) that supervisor
  support and communication quality are two of the more directly manageable organizational
  predictors of workplace isolation, supporting SNH's focus on communication cadence and
  supervisory training as intervention targets, while its null tenure finding cautions
  against assuming isolation risk rises simply with longer remote tenure.
tags:
  topic: ["remote-work", "isolation", "social-support", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Factors Contributing to Workplace Isolation in Remote Workers - Doctoral Dissertation/Factors Contributing to Workplace Isolation in Remote Workers - Doctoral Dissertation.md"
  pdf: "papers/Remote Workers/Factors Contributing to Workplace Isolation in Remote Workers - Doctoral Dissertation.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "faulds-2021-the-work-from-home-trend-an"
title: "The work-from-home trend: An interview with Brian Kropp"
authors:
  - "Faulds, David J."
  - "Raju, P.S."
year: 2021
doi: "10.1016/j.bushor.2020.10.005"
venue: {type: "journal", name: "Business Horizons", volume: 64, issue: 1, pages: "29-35"}
citation: "Faulds et al. (2021). The work-from-home trend: An interview with Brian Kropp. Business Horizons, 64(1), 29-35. https://doi.org/10.1016/j.bushor.2020.10.005"
article_type: "commentary"
method: {design: "qualitative", approach: "interview", evidence_level: "weak", preregistered: false}
gist: >
  This is a Business Horizons 'Executive Focus' interview with Gartner chief of research
  Brian Kropp, who summarizes Gartner survey data on the COVID-19-driven work-from-home
  shift. Kropp reports that remote work rose from about 10% full-time in 2019 to near-
  universal during spring 2020 and is projected to settle near 20% full-time remote / 28%
  hybrid / 50% office, and he argues remote employees show more loneliness, isolation,
  weaker social ties, longer workdays, and higher turnover risk than office-based peers,
  alongside employer gains in real estate savings and talent-pool breadth.
claims:
  - text: "Employees who predominantly work from home are described as 'dramatically more likely to quit' than office-based employees, attributed to the loss of informal social connection with coworkers (no shared lunches, coffee breaks, or happy hours) and a different view of outside job opportunities."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["turnover", "isolation"]
    predictors: ["social-support", "remote-work-intensity"]
  - text: "Remote employees reportedly experience 'much greater loneliness,' 'much greater isolation,' and fewer social connections than office workers; one cited survey found the work day increased by 48.5 minutes and involved about 13% more meetings for remote workers, alongside reduced physical activity (fewer tracked daily steps)."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["loneliness", "isolation", "wellbeing"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Employer adoption of AI-based employee monitoring technology for remote workers rose sharply during the pandemic, from about 16% of surveyed companies in April 2020 to 26% by June and roughly a third by August 2020; remote employees also received more negative corrective feedback than office workers despite similar performance scores in 2019 data."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["job-engagement", "turnover"]
    predictors: ["organizational-culture", "leadership-style"]
population:
  who: "Not a study of a defined sample; the interviewee (Gartner's chief of research) summarizes aggregated, unnamed Gartner survey data collected from HR executives, business leaders, CFOs, heads of real estate, and employees at Gartner's corporate clients."
  where: ["United States"]
  when: "2019-2020 (COVID-19 pandemic period)"
  n: null
  sector: ["mixed-sectors"]
  sample_notes: >
    No sample sizes, sampling methods, or citations are given for any of the statistics
    quoted; all figures are asserted verbally by a single interviewee describing internal,
    proprietary Gartner research rather than documented in the article itself.
limitation:
  primary: "The piece is a secondhand, conversational summary of an executive's recollection of proprietary Gartner survey findings, with no methodological detail (sample sizes, sampling procedures, question wording, or citations), so quoted statistics (e.g., +48.5 minute workday, quit-likelihood claims, monitoring-adoption percentages) cannot be independently verified."
  others:
    - "Single informant's expert opinion rather than an original peer-reviewed empirical study"
    - "No statistical tests, confidence intervals, or comparison groups reported for any claim"
    - "Interview format is not a systematic review of the literature; claims may reflect Gartner's commercial framing of remote-work trends"
risk_of_bias: "high"
relevance_to_project: >
  Despite weak evidentiary grounding, the interview articulates a specific mechanism
  relevant to SNH design: loss of informal, unplanned social contact (lunches, coffee,
  hallway conversation) among remote workers is framed as a direct driver of loneliness,
  isolation, and ultimately turnover, which supports designing interventions that recreate
  low-friction casual social contact for distributed teams rather than only formal
  collaboration tools.
tags:
  topic: ["remote-work", "hybrid-work", "isolation", "loneliness", "turnover"]
  method: ["qualitative"]
  population: ["remote-workers", "hr-executives"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Faulds & Raju (2021) - The Work-From-Home Trend - An Interview with Brian Kropp/Faulds & Raju (2021) - The Work-From-Home Trend - An Interview with Brian Kropp.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Faulds & Raju (2021) - The Work-From-Home Trend - An Interview with Brian Kropp.pdf"
  notes: null

---

id: "buonomo-2024-feeling-supported-as-a-remote-worker"
title: "Feeling Supported as a Remote Worker: The Role of Support from Leaders and Colleagues and Job Satisfaction in Promoting Employees’ Work–Life Balance"
authors:
  - "Buonomo, Ilaria"
  - "De Vincenzi, Clara"
  - "Pansini, Martina"
  - "D’Anna, Francesco"
  - "Benevene, Paula"
year: 2024
doi: "10.3390/ijerph21060770"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 21, issue: 6, pages: "770"}
citation: "Buonomo et al. (2024). Feeling Supported as a Remote Worker: The Role of Support from Leaders and Colleagues and Job Satisfaction in Promoting Employees’ Work–Life Balance. International Journal of Environmental Research and Public Health, 21(6), 770. https://doi.org/10.3390/ijerph21060770"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a structural equation model of 635 Italian remote workers, this study found that
  colleague support was linked to work-life balance entirely through job satisfaction (a
  full mediating effect), while leader support showed no significant association with either
  job satisfaction or work-life balance. The findings suggest that for remote workers, peer-
  level social support functions as a resource that builds job satisfaction, which in turn
  shapes work-life balance, whereas conventional supervisor support does not translate the
  same way in remote settings.
claims:
  - text: "Job satisfaction fully mediated the relationship between colleague support and work-life balance in a structural equation model (chi-square(22)=68.923, p=0.00, CFI=0.973, TLI=0.955, RMSEA=0.059, SRMR=0.030); the direct path from colleague support to work-life balance was non-significant (beta=-0.111, ns) while the indirect path via job satisfaction was significant (beta=0.352, p<0.01)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "job-satisfaction"]
    predictors: ["social-support", "job-satisfaction"]
  - text: "Leader (supervisor) support showed no significant direct or indirect association with work-life balance and no significant association with job satisfaction, disconfirming three of the study's five hypotheses (H1b, H2b, H5), in contrast to colleague support which was significantly linked to both."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "work-life-balance"]
    predictors: ["leadership-style", "social-support"]
  - text: "Colleague support and leader support were positively correlated with each other (r=0.541, p<0.001), and colleague support correlated more strongly with job satisfaction (r=0.323, p<0.001) and work-life balance (r=0.209, p<0.001) than leader support did (r=0.197 and r=0.157 respectively, both p<0.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "work-life-balance"]
    predictors: ["social-support", "leadership-style"]
population:
  who: "635 Italian remote/hybrid workers (able to work both remotely and on-site, no direct customer/patient contact), 61% female, mean age 46.7 (SD=11), mean organizational tenure 15.13 years"
  where: ["Italy"]
  when: null
  n: 635
  sector: ["research", "finance", "energy", "legal-services", "public-administration"]
  sample_notes: >
    Convenience sample recruited via questionnaire under ethics approval (LUMSA University
    protocol 4/2022); excluded front-line/customer-facing roles; single-country, largely
    service-sector and public-administration sample limits generalizability; several single-
    item or two/three-item COPSOQ-adapted measures (work-life balance measured with only one
    item).
limitation:
  primary: "Cross-sectional design with self-reported measures precludes causal inference about the mediation pathway and is subject to common-method and social-desirability bias."
  others:
    - "Work-life balance was measured with a single item, and colleague support's composite reliability (CR=0.685) fell just below the conventional 0.70 threshold."
    - "Sample drawn from a single country (Italy) and predominantly service-based/public-administration sectors, limiting generalizability."
    - "Other plausible influences on work-life balance (technology use, workload, home environment) were not modeled."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH design question of which support channel to prioritize for
  remote-worker well-being: it provides SEM evidence that peer/colleague support (not
  supervisor support) drives work-life balance via job satisfaction, suggesting
  community/peer-connection features may matter more than manager-facing interventions for
  this outcome pathway.
tags:
  topic: ["remote-work", "work-life-balance", "social-support", "job-satisfaction"]
  method: ["cross-sectional", "survey"]
  population: ["remote-workers", "italy", "mixed-sector"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Feeling Supported as a Remote Worker - Support from Leaders Colleagues and Job Satisfaction in Promoting Work-Life Balance/Feeling Supported as a Remote Worker - Support from Leaders Colleagues and Job Satisfaction in Promoting Work-Life Balance.md"
  pdf: "papers/Remote Workers/Feeling Supported as a Remote Worker - Support from Leaders Colleagues and Job Satisfaction in Promoting Work-Life Balance.pdf"
  notes: null

---

id: "montanez-2024-fighting-loneliness-on-remote-teams"
title: "Fighting Loneliness on Remote Teams"
authors:
  - "Montañez, Rachel"
year: 2024
doi: null
venue: {type: "other", name: "Harvard Business Review", volume: null, issue: null, pages: null}
citation: "Montañez (2024). Fighting Loneliness on Remote Teams. Harvard Business Review."
article_type: "commentary"
method: {design: "theory", approach: "other", evidence_level: "weak", preregistered: false}
gist: >
  This short Harvard Business Review piece argues that remote work's lack of in-person
  community leaves some employees feeling isolated and lonely, and that this loneliness
  translates into workplace stress and reduced job performance. It frames loneliness and
  isolation as a broader public-health epidemic and cites a specific economic cost figure
  for absenteeism tied to stress and loneliness among U.S. employers, positioning community-
  building as the central remedy for remote and hybrid teams.
claims:
  - text: "Absenteeism attributed to stress and loneliness costs U.S. employers an estimated $154 billion annually, per a 2022 article in the Journal of Organizational Effectiveness: People and Performance cited by the author."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["loneliness", "stress", "productivity"]
    predictors: ["isolation", "loneliness"]
  - text: "Remote work's reduced access to in-person community is described as a central driver of employee isolation and loneliness, which in turn is said to significantly impact job performance."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["isolation", "loneliness", "performance"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "General remote-working employees; no original study sample, only aggregate/secondary workforce statistics referenced by the author"
  where: ["United States"]
  when: "2024 article citing a 2022 secondary statistic"
  n: null
  sector: ["general-workforce"]
  sample_notes: >
    This is a short practitioner/magazine piece with no original data collection; the corpus
    copy is a paywalled fragment (~1,800 characters, mostly the article's opening and a
    summary teaser marked 'more'), so most of the full article's content and recommendations
    are not captured here.
limitation:
  primary: "The corpus copy is a paywalled stub containing only the article's introduction and summary teaser, not the full text, so its arguments and any recommendations cannot be fully evaluated."
  others:
    - "No original empirical research is presented; the piece relies on a single secondary statistic cited without methodological detail"
    - "Journalistic/practitioner commentary, not peer-reviewed research"
risk_of_bias: "high"
relevance_to_project: >
  Useful as a practitioner-facing motivating statistic (the $154B absenteeism cost of
  stress/loneliness) for framing remote-team loneliness as a costly organizational problem,
  and as an example of how HBR frames community-building as the intervention lever for
  remote-team isolation, though the corpus copy lacks the article's substantive
  recommendations.
tags:
  topic: ["remote-work", "loneliness", "isolation", "wellbeing", "community-health"]
  method: ["secondary-data"]
  population: ["remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Fighting Loneliness on Remote Teams - HBR March 2024/Fighting Loneliness on Remote Teams - HBR March 2024.md"
  pdf: "papers/Remote Workers/Fighting Loneliness on Remote Teams - HBR March 2024.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "gajendran-2007-the-good-the-bad-and-the"
title: "The good, the bad, and the unknown about telecommuting: Meta-analysis of psychological mediators and individual consequences."
authors:
  - "Gajendran, Ravi S."
  - "Harrison, David A."
year: 2007
doi: "10.1037/0021-9010.92.6.1524"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 92, issue: 6, pages: "1524-1541"}
citation: "Gajendran et al. (2007). The good, the bad, and the unknown about telecommuting: Meta-analysis of psychological mediators and individual consequences.. Journal of Applied Psychology, 92(6), 1524-1541. https://doi.org/10.1037/0021-9010.92.6.1524"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  This meta-analysis of 46 field studies (N = 12,883 employees) tests a theoretical
  framework in which telecommuting affects distal outcomes through three psychological
  mediators: perceived autonomy, work-family conflict, and relationship quality with
  supervisors/coworkers. Telecommuting showed small but generally beneficial effects on job
  satisfaction, turnover intent, role stress, and supervisor-rated (not self-rated)
  performance, and did not damage supervisor relationships or perceived career prospects,
  contradicting a widely assumed 'telecommuting paradox.' However, high-intensity
  telecommuting (more than 2.5 days/week) uniquely worsened coworker relationship quality
  while amplifying the beneficial reduction in work-family conflict, showing that social
  costs are concentrated in high-intensity arrangements rather than telecommuting per se.
claims:
  - text: "Across 46 studies, telecommuting had no overall detrimental effect on relationship quality with supervisors (corrected r = .12, k=14, n=2,888, 95% CI .08-.15) and was essentially unrelated to coworker relationship quality overall (corrected r = .003, k=14, n=3,269, 95% CI -.03 to .03), disconfirming the hypothesized 'relational impoverishment' from reduced face-to-face contact."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["collaboration", "isolation"]
    predictors: ["remote-work-intensity", "social-presence"]
  - text: "Telecommuting intensity moderated relational harm: coworker relationship quality was unaffected under low-intensity telecommuting (r = .03, 95% CI -.01 to .07) but significantly worsened under high-intensity telecommuting of more than 2.5 days/week (r = -.19, 95% CI -.30 to -.08), Qb = 14.52, p < .01; supervisor relationships were unaffected by intensity (Qb = 0.11, ns)."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["isolation", "collaboration"]
    predictors: ["remote-work-intensity"]
  - text: "Telecommuting was associated with higher perceived autonomy (corrected r = .22), lower work-family conflict (corrected r = -.13, stronger for high-intensity arrangements, r = -.16 vs r = -.05 for low-intensity), higher job satisfaction (corrected r = .10), lower turnover intent (corrected r = -.10), lower role stress (corrected r = -.13), and higher supervisor-rated performance (corrected r = .19), though self-rated performance showed no relationship (corrected r = .01); perceived autonomy was the strongest mediating mechanism, fully mediating the job satisfaction effect."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["job-satisfaction", "turnover", "stress", "performance"]
    predictors: ["autonomy", "remote-work-intensity"]
population:
  who: "46 field studies of employed telecommuters/distributed workers (comparing telecommuters to conventional-arrangement employees, or varying telecommuting levels), drawn from management, psychology, information systems, and other literatures; typical telecommuter was a manager or IT/sales-marketing professional, mean age 39, 49% women on average"
  where: []
  when: null
  n: 12883
  sector: ["general-workforce"]
  sample_notes: >
    27 published articles and 19 unpublished dissertations from ~212 candidate works
    screened; average original-study response rate 51%; almost all primary studies were
    cross-sectional/nonexperimental with a single wave of data collection, no randomized
    field experiments; k (number of contributing studies) varied by outcome from 4 to 28.
limitation:
  primary: "All 46 underlying primary studies were nonexperimental, mostly cross-sectional single-wave designs with no randomized field experiments, so causal direction (e.g., self-selection into telecommuting by employees already having good supervisor relationships or high performance) cannot be ruled out."
  others:
    - "Sparse reporting of key moderators (voluntariness, task interdependence, job type, technology used) in primary studies meant these could not be tested even though they are theoretically important."
    - "Effects are measured only at the individual level; team- or unit-level consequences of coworker relationship deterioration under high-intensity telecommuting were not directly examined."
    - "Several key relationships (e.g., work-family conflict, coworker relationship quality, performance measures) showed significant heterogeneity (Q statistics), indicating unmodeled moderators beyond intensity, gender, and experience."
risk_of_bias: "low"
relevance_to_project: >
  Directly informs the SNH project's core design tension between remote-work flexibility and
  social connection: it provides quantitative evidence that telecommuting itself does not
  erode supervisor or coworker ties, but that high-intensity telecommuting (>2.5 days/week)
  specifically degrades coworker relationship quality, suggesting SNH interventions should
  target social-connection supports for high-intensity remote workers rather than assuming
  all remote work carries equal isolation risk, and that perceived autonomy is the key
  psychological lever mediating most benefits.
tags:
  topic: ["remote-work", "collaboration", "work-life-balance", "job-satisfaction", "isolation"]
  method: ["review-systematic", "secondary-data"]
  population: ["general-workforce", "managers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Gajendran & Harrison (2007) - The Good the Bad and the Unknown About Telecommuting/Gajendran & Harrison (2007) - The Good the Bad and the Unknown About Telecommuting.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Gajendran & Harrison (2007) - The Good the Bad and the Unknown About Telecommuting.pdf"
  notes: null

---

id: "andrews-1995-structural-holes-the-social-structure-of"
title: "Structural Holes: The Social Structure of Competition."
authors:
  - "Andrews, Steven B."
  - "Burt, Ronald S."
year: 1995
doi: "10.2307/2393644"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 40, issue: 2, pages: "355"}
citation: "Andrews et al. (1995). Structural Holes: The Social Structure of Competition.. Administrative Science Quarterly, 40(2), 355. https://doi.org/10.2307/2393644"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This is a 1995 Administrative Science Quarterly review-symposium piece by Steven B.
  Andrews critiquing Ronald Burt's book Structural Holes: The Social Structure of
  Competition. Andrews summarizes Burt's argument that 'structural autonomy' — occupying
  network positions rich in unconnected 'structural holes' among one's contacts — predicts
  access to information, managerial promotion, and market profit, and situates the book
  within economic sociology, organizational behavior, and population ecology. He also raises
  a pointed concern for social-support-minded network researchers: Burt's instrumental,
  competition-focused framing treats affective ties as a strategic byproduct of alleviating
  structural constraint, which may not fit relationships built for support rather than
  exchange.
claims:
  - text: "Burt reports that managers who span 'structural holes' (bridging otherwise unconnected contacts, i.e. 'social frontiers') show higher rates of promotion, an empirical finding from his organizational data presented in chapter 4 of the reviewed book."
    evidence: "theory"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "retention"]
    predictors: ["network-structure"]
  - text: "In Burt's market-exchange data, actors whose networks exhibit structural autonomy (holes among contacts that prevent those contacts from forming a coalition) capture profits above the level predicted by ordinary supply-and-demand, which Burt uses as evidence that network structure directly shapes economic outcomes."
    evidence: "theory"
    support_strength: "low-to-moderate"
    outcomes: ["performance"]
    predictors: ["network-structure"]
  - text: "Andrews argues that Burt's instrumental/competitive framing of network optimization is in tension with social-support scholarship, because treating affective ties as strategic responses to structural constraint risks obscuring the distinct role non-instrumental, supportive relationships play in identity formation and wellbeing."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["sense-of-belonging", "wellbeing"]
    predictors: ["social-support", "network-structure"]
population:
  who: "Not an original empirical sample — the document reviews Ronald Burt's book, whose two illustrative studies involved corporate managers (promotion analysis) and buyer-supplier firms (market-profit analysis)."
  where: ["United States"]
  when: null
  n: null
  sector: ["corporate-sector"]
  sample_notes: >
    This is a book review, not primary research; the population above describes the two
    studies Burt reports in the reviewed book as summarized secondhand by the reviewer, with
    no sample sizes or response rates given in this document.
limitation:
  primary: "As a review/commentary, this document reports Burt's findings and arguments secondhand through the reviewer's summary rather than presenting original data, methods, or effect sizes from the underlying studies."
  others:
    - "Centers on an instrumental/competitive theory of networks that the reviewer himself flags as poorly suited to affective, support-oriented ties central to SNH concerns."
    - "Contains no discussion of remote work, isolation, or mental-health outcomes specifically; relevance is only through general structural-holes/brokerage network theory."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Offers a critical secondary read of structural-holes/brokerage theory (Burt 1992), a
  foundational network-structure concept relevant to how SNH might measure bridging
  positions and information/career access, while the reviewer's warning against conflating
  instrumental and affective ties directly bears on how the project should distinguish
  competitive network measures from social-support measures.
tags:
  topic: ["collaboration", "social-support", "measurement", "methodology"]
  method: ["theory", "commentary"]
  population: ["managers", "corporate-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Gladwin (1981) - Review of Cultures Consequences - International Differences in Work-Related Values/Gladwin (1981) - Review of Cultures Consequences - International Differences in Work-Related Values.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Gladwin (1981) - Review of Cultures Consequences - International Differences in Work-Related Values.pdf"
  notes: null

---

id: "gladwin-1981-culture-s-consequences-international-differences-in"
title: "Culture's Consequences: International Differences in Work-Related Values"
authors:
  - "Gladwin, Thomas N."
  - "Hofstede, Geert"
year: 1981
doi: "10.2307/257651"
venue: {type: "journal", name: "The Academy of Management Review", volume: 6, issue: 4, pages: "681"}
citation: "Gladwin et al. (1981). Culture's Consequences: International Differences in Work-Related Values. The Academy of Management Review, 6(4), 681. https://doi.org/10.2307/257651"
article_type: "commentary"
method: {design: "book-review", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This is a book-review section from the October 1981 Academy of Management Review,
  containing three separate reviews. The most substantive, by Thomas N. Gladwin, assesses
  Geert Hofstede's 'Culture's Consequences,' summarizing its four empirically derived cross-
  national work-value dimensions (power distance, uncertainty avoidance, individualism,
  masculinity) drawn from a 117,000-questionnaire, 40-country employee survey at two time
  points (1968, 1972). A second review (by James B. Thurman) covers Pennings's study of
  interlocking corporate directorates and financial performance, and a third (unattributed,
  cut off mid-text) begins reviewing a book on R&D management. Its main contribution to the
  corpus is Hofstede's foundational framework for how national culture shapes management
  style, participation, and individualism-versus-collectivism in organizational life.
claims:
  - text: "Hofstede derived four dimensions of national work-related values (power distance, uncertainty avoidance, individualism, masculinity) from a survey of 117,000 questionnaires collected from 88,000 employees of a single multinational firm across 67 countries (40 analyzed); high power-distance nations (e.g., Mexico, the Philippines) showed greater centralization and less participative management, while high-individualism nations (e.g., US, Australia) showed more calculative, less loyalty-based involvement with organizations."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture", "leadership-style"]
  - text: "Comparing survey waves from 1968 and 1972, Hofstede found no convergence between countries' cultural profiles over the four-year period, but did find some worldwide shifts, including decreasing power distance and increasing individualism."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture"]
  - text: "In the reviewed Pennings study of interlocking directorates (1969-1970 data), positive correlations were found between number of board interlocks and organizational earnings, profitability, and growth, but the reviewer notes these are cross-sectional correlations that are explicitly not causal, and highlights Pennings's own alternative hypothesis that business acumen, not interlocks, explains higher firm effectiveness."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "productivity"]
    predictors: ["network-structure"]
population:
  who: "Employees of a pseudonymous ('HERMES') US-based multinational high-technology firm surveyed on work values (Hofstede's study); separately, financial and non-financial US corporations analyzed for board interlocks (Pennings's study, reviewed in the same issue)."
  where: ["United States", "multi-country (67 surveyed, 40 analyzed)"]
  when: "1968 and 1972 (Hofstede survey waves); 1969-1970 (Pennings interlock data)"
  n: 88000
  sector: ["technology", "corporate"]
  sample_notes: >
    This document is itself a review/commentary, not the primary study; population details
    are as reported secondhand by the reviewers. Hofstede's 88,000 respondents were host-
    national employees of one company, not a general population sample; representativeness
    is limited to that firm's workforce across countries. The third review in this file is
    truncated mid-sentence (conversion artifact or original page cutoff).
limitation:
  primary: "The carded document is a compilation of book reviews, not primary research; its reported findings on Hofstede's and Pennings's studies are secondhand summaries filtered through reviewers' space-constrained interpretations rather than verifiable primary data."
  others:
    - "Pennings's interlock findings are explicitly correlational and cross-sectional, not causal, as the reviewer himself cautions."
    - "Hofstede's data (1968-1972) predate remote/digital work by decades, limiting direct applicability to contemporary distributed-work contexts."
    - "The file is truncated mid-sentence during the third (Stephanou) review, indicating an incomplete document."
risk_of_bias: "high"
relevance_to_project: >
  Hofstede's power-distance and individualism dimensions, summarized here, offer a
  foundational cross-cultural lens for interpreting why participative management, autonomy
  expectations, and help-seeking/collaboration norms may differ systematically across the
  national cultures represented in a distributed or remote workforce, informing how the
  project should account for cultural variance when designing social-support interventions.
tags:
  topic: ["remote-work", "collaboration", "methodology"]
  method: ["survey", "longitudinal"]
  population: ["corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Gladwin-AcademyManagementReview-1981/Gladwin-AcademyManagementReview-1981.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Gladwin-AcademyManagementReview-1981.pdf"
  notes: null

---

id: "bilderback-2024-global-perspectives-on-redefining-workplace-presence"
title: "Global perspectives on redefining workplace presence: the impact of remote work on organizational culture"
authors:
  - "Bilderback, Stephanie"
  - "Kilpatrick, Matthew D."
year: 2024
doi: "10.1108/jeet-08-2024-0023"
venue: {type: "journal", name: "Journal of Ethics in Entrepreneurship and Technology", volume: 4, issue: 1, pages: "62-72"}
citation: "Bilderback et al. (2024). Global perspectives on redefining workplace presence: the impact of remote work on organizational culture. Journal of Ethics in Entrepreneurship and Technology, 4(1), 62-72. https://doi.org/10.1108/jeet-08-2024-0023"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This conceptual paper argues that remote work forces organizations to redefine 'workplace
  presence' away from physical visibility toward engagement and outcomes, synthesizing prior
  literature and six management theories (Kotter's 8-Step Change Model, Competing Values
  Framework, Social Exchange Theory, Role Theory, Self-Determination Theory, Equity Theory)
  into a practical framework for sustaining culture, belonging, and productivity in
  distributed teams. It illustrates the framework with four secondary case studies (Twitter,
  Older Adults Technology Services, Anara Fashion Fusion, Middle East College) and
  highlights 'presence bias' -- the tendency to equate visibility with productivity -- as a
  specific threat to fair performance evaluation of remote employees.
claims:
  - text: "Physical separation from colleagues in remote work is linked to isolation, disconnection, and reduced motivation and commitment, which organizations must counter with deliberate virtual social events, informal chat groups, and recognition programs to sustain a sense of belonging and engagement (drawing on Wang et al., 2020 and Dinh et al., 2021)."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["isolation", "sense-of-belonging", "job-engagement"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "'Presence bias' -- the tendency to equate office visibility with productivity -- is argued to be exacerbated in remote settings, causing less visible remote or flexible-schedule employees to be perceived as less productive or committed regardless of actual output, which requires shifting performance evaluation to results-based metrics."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["performance"]
    predictors: ["remote-work-intensity", "organizational-culture"]
  - text: "Across four illustrative case organizations (Twitter, Older Adults Technology Services, Anara Fashion Fusion, Middle East College), successful remote transitions shared common practices -- regular virtual check-ins, transparent leadership communication, flexible scheduling, and recognition programs -- credited with maintaining team cohesion and a sense of community despite physical separation."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration", "sense-of-belonging", "job-engagement"]
    predictors: ["leadership-style", "team-cohesion"]
population:
  who: "Not an empirical sample: a conceptual/narrative synthesis of prior peer-reviewed literature plus four secondary organizational case studies (Twitter; Older Adults Technology Services; Anara Fashion Fusion; Middle East College) reported in other authors' publications."
  where: []
  when: null
  n: null
  sector: ["technology", "nonprofit", "apparel-manufacturing", "higher-education"]
  sample_notes: >
    No primary data collection or original sample; the four case studies are secondhand
    summaries drawn from other researchers' published accounts rather than first-hand
    investigation by this paper's authors, and no systematic search protocol is described
    for the literature synthesized.
limitation:
  primary: "The paper is a conceptual synthesis with no original empirical data collection, systematic review protocol, or independent testing of its claims -- conclusions rest on narrative integration of prior literature and secondhand case study summaries."
  others:
    - "Case studies are drawn from other authors' publications and are illustrative rather than verified or comparable across a common methodology."
    - "No explicit literature search strategy is reported, raising risk of selective citation supporting the authors' framework."
risk_of_bias: "high"
relevance_to_project: >
  Useful for the SNH project as a synthesis map linking reduced physical co-presence to
  isolation and diminished sense of belonging, and for naming 'presence bias' as a concrete
  mechanism by which remote/distributed contributors (directly analogous to open-source
  maintainers) can be undervalued despite equal output -- both relevant to designing fairer
  engagement and recognition signals for remote and OSS communities.
tags:
  topic: ["remote-work", "hybrid-work", "isolation", "job-engagement", "wellbeing"]
  method: ["theory", "case-study"]
  population: ["knowledge-workers", "organizations-multi-sector"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Global Perspectives on Redefining Workplace Presence - The Impact of Remote Work on Organizational Culture/Global Perspectives on Redefining Workplace Presence - The Impact of Remote Work on Organizational Culture.md"
  pdf: "papers/Remote Workers/Global Perspectives on Redefining Workplace Presence - The Impact of Remote Work on Organizational Culture.pdf"
  notes: null

---

id: "golden-2006-telecommuting-s-differential-impact-on-work"
title: "Telecommuting's differential impact on work-family conflict: Is there no place like home?"
authors:
  - "Golden, Timothy D."
  - "Veiga, John F."
  - "Simsek, Zeki"
year: 2006
doi: "10.1037/0021-9010.91.6.1340"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 91, issue: 6, pages: "1340-1350"}
citation: "Golden et al. (2006). Telecommuting's differential impact on work-family conflict: Is there no place like home?. Journal of Applied Psychology, 91(6), 1340-1350. https://doi.org/10.1037/0021-9010.91.6.1340"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Surveying 454 professional-level telecommuters at a single large high-tech firm, the
  authors find telecommuting has a differential, bidirectional impact on work-family
  conflict: more extensive telecommuting is associated with lower work-to-family conflict
  (WFC) but higher family-to-work conflict (FWC), consistent with a resource-depletion
  trade-off rather than full work-family integration. Job autonomy and scheduling
  flexibility moderate the telecommuting-WFC link (in partly unexpected directions), while
  household size moderates the telecommuting-FWC link, indicating that contextual moderators
  operate in domain-specific ways.
claims:
  - text: "Extent of telecommuting (hours/week working from home) was negatively related to work-to-family conflict (beta = -.27, p < .001) and positively related to family-to-work conflict (beta = .19, p < .001), supporting a differential rather than uniform impact of telecommuting on work-family conflict."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Job autonomy moderated the telecommuting-WFC relationship in a partly unexpected direction (beta = .15, p < .001): telecommuters with high autonomy showed no significant decline in WFC with more telecommuting (b = -.01, ns), whereas those with low autonomy showed a significant WFC reduction (b = -.03, p < .05)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["autonomy", "remote-work-intensity"]
  - text: "Household size moderated the telecommuting-FWC relationship as predicted (beta = .12, p < .01): among telecommuters with large households, more extensive telecommuting was associated with significantly higher FWC (b = .03, p < .05), while for those with small households the extent of telecommuting had no significant effect on FWC."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["remote-work-intensity", "boundary-management"]
population:
  who: "Professional-level telecommuters (college-educated) at one large U.S. high-tech firm (34,000+ employees, 12,610 telecommuters), splitting work time between office and home"
  where: ["United States"]
  when: null
  n: 454
  sector: ["technology"]
  sample_notes: >
    Random 10% sample (1,261) of the firm's telecommuters invited via email from a senior
    executive; 454 usable responses, 36% response rate. 65% men/35% women (mirroring the
    broader telecommuter population per ITAC 2001), 54% married, average age 37, average
    tenure telecommuting 4 years, averaging 18.9 hrs/week telecommuting out of a 45-hr
    workweek. Single-firm, single-industry sample limits generalizability.
limitation:
  primary: "Cross-sectional, correlational, self-report design from a single source at one time point precludes causal inference and cannot rule out reverse/reciprocal causality (e.g., individuals may adjust telecommuting extent based on existing conflict levels) or common method variance."
  others:
    - "Single-organization, single-industry (high-tech) sample of professional-level employees may not generalize to other sectors, non-professional telecommuters, or fully remote (non-hybrid) workers."
    - "No baseline measure of work-family conflict prior to starting telecommuting, so only relative associations (not absolute benefits/costs) of telecommuting could be assessed."
    - "Study does not measure potential offsetting benefits such as work-family enrichment or positive spillover, so the net welfare implications of the WFC/FWC trade-off remain unaddressed."
risk_of_bias: "medium"
relevance_to_project: >
  Offers a well-powered (N=454) empirical benchmark on a core boundary-management mechanism
  relevant to remote/hybrid worker SNH: extensive telecommuting reduces work-to-family
  conflict but increases family-to-work conflict, and this trade-off is shaped by autonomy,
  scheduling flexibility, and household size. Useful evidence base for designing remote-work
  policies or interventions that target boundary-management support (e.g., scheduling
  flexibility) rather than assuming remote work uniformly improves work-life balance.
tags:
  topic: ["remote-work", "hybrid-work", "work-life-balance"]
  method: ["survey", "cross-sectional"]
  population: ["professionals", "technology-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Golden et al. (2006) - Telecommuting Differential Impact on Work-Family Conflict/Golden et al. (2006) - Telecommuting Differential Impact on Work-Family Conflict.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Golden et al. (2006) - Telecommuting Differential Impact on Work-Family Conflict.pdf"
  notes: null

---

id: "golden-2008-the-impact-of-professional-isolation-on"
title: "The impact of professional isolation on teleworker job performance and turnover intentions: Does time spent teleworking, interacting face-to-face, or having access to communication-enhancing technology matter?"
authors:
  - "Golden, Timothy D."
  - "Veiga, John F."
  - "Dino, Richard N."
year: 2008
doi: "10.1037/a0012722"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 93, issue: 6, pages: "1412-1421"}
citation: "Golden et al. (2008). The impact of professional isolation on teleworker job performance and turnover intentions: Does time spent teleworking, interacting face-to-face, or having access to communication-enhancing technology matter?. Journal of Applied Psychology, 93(6), 1412-1421. https://doi.org/10.1037/a0012722"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using matched survey data from 261 professional teleworkers and their supervisors at one
  large high-tech firm, the authors develop and validate a 7-item professional isolation
  measure and find it lowers supervisor-rated job performance but, contrary to hypothesis,
  lowers rather than raises turnover intentions. The negative isolation-performance link is
  amplified by more time spent teleworking and buffered by more face-to-face interaction,
  while isolation's (counterintuitive) turnover-reducing effect is strengthened by extensive
  teleworking and by limited access to communication-enhancing technology.
claims:
  - text: "Professional isolation was significantly negatively related to supervisor-rated job performance (beta = -.13, p < .05; delta R2 = .02, p < .05)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["isolation"]
  - text: "Contrary to the hypothesized positive relationship, professional isolation was significantly negatively related to turnover intentions (beta = -.27, p < .001; delta R2 = .07, p < .001) -- the most isolated teleworkers reported the lowest, not highest, intention to leave."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["isolation"]
  - text: "Time spent teleworking amplified isolation's negative effect on performance (beta = -.16, p < .05) and its effect on lowering turnover intentions (beta = -.34, p < .001); face-to-face interaction buffered the negative isolation-performance link (beta = .21, p < .01) but did not moderate turnover intentions; access to communication-enhancing technology did not moderate performance but did moderate (reduce) isolation's turnover-lowering effect (beta = .22, p < .001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "turnover"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "261 professional-level teleworkers matched with their direct supervisors (522 supervisors contacted) at one large U.S. high-tech corporation with an established telework program"
  where: ["United States"]
  when: null
  n: 261
  sector: ["technology", "corporate"]
  sample_notes: >
    Single-firm design (80,000-employee company); supervisor response rate 26% of 2,000
    contacted, employee response rate 50% of those invited by their supervisor; only 16% of
    the firm's workforce teleworked. Teleworkers averaged 39 years old, 64% male,
    teleworking 60% of the workweek for ~40 months on average; supervisors averaged 43 years
    old, 70% male. Single-company sample limits generalizability across organizational
    telework cultures.
limitation:
  primary: "Cross-sectional correlational design precludes causal inference; the authors explicitly note reverse or reciprocal causality (e.g., low performance causing isolation) cannot be ruled out."
  others:
    - "Single-organization sample (one telework-friendly high-tech firm) limits generalizability to organizations with different telework policies or cultures."
    - "No comparison group of non-teleworkers in the main sample (only a small ancillary pilot sample of 56 non-teleworkers was used post hoc to compare isolation levels)."
    - "Turnover intentions and job performance measures rely on self-report (isolation, turnover intentions) and single supervisor ratings (performance), not objective outcomes."
risk_of_bias: "medium"
relevance_to_project: >
  Provides one of the first validated multi-item measures of professional isolation (7
  items, alpha = .89, convergent with UCLA Loneliness Scale r = .74) that the SNH project
  can adapt for measuring isolation among remote workers, and its counterintuitive finding
  -- that isolation reduces rather than increases turnover intentions, especially for heavy
  teleworkers -- is an important caution against assuming isolation straightforwardly drives
  attrition; it should inform how SNH designs frame isolation's downstream organizational
  risks (performance loss without a turnover 'canary').
tags:
  topic: ["remote-work", "isolation", "job-engagement", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Golden et al. (2008) - Impact of Professional Isolation on Teleworker Job Performance and Turnover Intentions/Golden et al. (2008) - Impact of Professional Isolation on Teleworker Job Performance and Turnover Intentions.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Golden et al. (2008) - Impact of Professional Isolation on Teleworker Job Performance and Turnover Intentions.pdf"
  notes: null

---

id: "granovetter-1983-the-strength-of-weak-ties-a"
title: "The Strength of Weak Ties: A Network Theory Revisited"
authors:
  - "Granovetter, Mark"
year: 1983
doi: "10.2307/202051"
venue: {type: "journal", name: "Sociological Theory", volume: 1, issue: null, pages: "201"}
citation: "Granovetter (1983). The Strength of Weak Ties: A Network Theory Revisited. Sociological Theory, 1, 201. https://doi.org/10.2307/202051"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Granovetter revisits his 1973 'Strength of Weak Ties' (SWT) thesis by synthesizing roughly
  a decade of empirical and theoretical follow-up work, arguing the evidence broadly
  supports the core claim that weak ties (not strong ones) disproportionately act as bridges
  linking otherwise disconnected clusters, and that this bridging role drives information
  diffusion, job mobility, and integration of large, differentiated social systems. He also
  elaborates an 'excursus on the strength of strong ties,' showing strong ties dominate
  under conditions of economic insecurity, urgent need, or low socioeconomic status, while
  weak ties matter most for reaching novel information and connecting socially distant
  groups. The paper closes by noting the verification evidence is encouraging but
  incomplete, partly because it is not from a systematic or unbiased sample of studies.
claims:
  - text: "Friedkin's (1980) survey of 97 biology faculty found all 11 identified 'local bridges' in the network were weak ties, even though only 69% of all ties were weak (binomial test p=0.017); interdepartmental (intergroup) ties were weak 77% of the time versus 65% for intradepartmental ties (p=0.002), directly confirming SWT's bridging prediction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["communication"]
    predictors: ["network-structure"]
  - text: "Lin, Ensel, and Vaughn (1981) found weak ties raised occupational status attainment mainly indirectly, through the status of the contact reached: 76.2% of weak ties used for a first job connected respondents to high-status informants versus only 28.9% of strong ties (70.7% vs. 42.9% for current job), so weak ties' advantage depended on whom they connected to, not tie strength alone."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["occupational-attainment"]
    predictors: ["network-structure", "social-support"]
  - text: "Ericksen and Yancey's (1980) regression on a Philadelphia probability sample (n=1,780) found weak ties used for job-finding had a significant negative net effect on income overall, but a significant weak-tie x education interaction reversed this: weak ties reduced income among the poorly educated but the effect grew progressively more positive with more education."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["income"]
    predictors: ["network-structure", "social-support"]
population:
  who: "Not a single primary sample: a narrative synthesis of ~15 independent empirical and theoretical studies (job seekers, university faculty, kibbutz members, corporate directors, school peer groups, hospital staff, protest-group recruits, ghetto and shantytown residents) used to test or extend the 1973 weak-ties hypothesis."
  where: ["USA", "Canada", "Israel", "Germany"]
  when: "1962-1981 (data collection periods of the cited studies)"
  n: null
  sector: ["academia", "corporate", "healthcare", "community", "education"]
  sample_notes: >
    Studies were located mainly through personal contact with authors or their citation of
    Granovetter's original SWT paper -- a non-random, confirmation-prone sampling procedure
    that the author himself flags as a threat to unbiased verification of the theory.
limitation:
  primary: "The review's evidence base was assembled through citation tracing and personal contacts rather than systematic search, so studies where the weak-ties hypothesis was considered and rejected are structurally underrepresented, biasing the synthesis toward confirmation."
  others:
    - "Several cited studies (Coser, Boorman, Fine and Kleinman, Chubin, Karweit et al.) are purely theoretical and contribute no new empirical data."
    - "Operational definitions of 'weak' vs. 'strong' tie differ substantially across the cited studies (frequency of contact, mutual vs. one-sided reporting, kin/friend/acquaintance categories), limiting direct comparability."
    - "All cited studies are cross-sectional or static network snapshots; Granovetter explicitly calls for dynamic, longitudinal study of how bridging ties form and change over time."
risk_of_bias: "high"
relevance_to_project: >
  This is the canonical statement and empirical stress-test of the weak-ties/bridging
  mechanism that underlies SNH's interest in cross-group information flow, integration, and
  belonging: it gives a concrete evidence basis for designing remote/OSS communities with
  enough loosely-connected 'bridging' contacts across teams (to prevent fragmentation and
  speed information/idea diffusion) while recognizing strong ties remain the primary channel
  for support under stress, job insecurity, or economic precarity -- a distinction directly
  relevant to when to design for weak-tie breadth versus strong-tie support depth.
tags:
  topic: ["community-health", "collaboration", "social-support", "methodology"]
  method: ["review-narrative", "cross-sectional"]
  population: ["academia", "corporate", "community"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Granovetter-StrengthWeakTies-1983/Granovetter-StrengthWeakTies-1983.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Granovetter-StrengthWeakTies-1983.pdf"
  notes: null

---

id: "locke-2003-grounded-theory-in-management-research"
title: "Grounded Theory in Management Research"
authors:
  - "Locke, Karen"
year: 2003
doi: "10.4135/9780857024428"
venue: {type: "other", name: null, volume: null, issue: null, pages: null}
citation: "Locke (2003). Grounded Theory in Management Research.. https://doi.org/10.4135/9780857024428"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This is the introduction plus Chapter 1 of Karen Locke's SAGE monograph on grounded theory
  in management research. It traces the five historical 'moments' of qualitative research
  (traditional, modernist, blurred genres, crisis of representation, double crisis) and
  shows that grounded theory has been claimed by, and practiced within, all three major
  paradigms of management and organization studies—modernist, interpretive, and postmodern.
  It also distinguishes grounded theory from neighboring qualitative traditions (action
  research, case study, ethnography) and argues that narrow citation practices have left
  much of the method's methodological richness under-recognized in the field.
claims:
  - text: "Glaser and Strauss's original grounded theory is often classified within the modernist moment of qualitative research, yet management and organization scholars have applied it within modernist (e.g., Eisenhardt 1989; Ross and Staw 1993), interpretive (e.g., Gioia and Chittipeddi 1991), and postmodern (e.g., Covaleski et al. 1998) studies alike, showing that paradigm affiliation is set by individual researchers' commitments rather than by the method's own logic."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["methodological-rigor"]
    predictors: ["grounded-theory", "research-paradigm"]
  - text: "Grounded theory is characterized as most closely aligned with case-study and ethnographic traditions—sharing a modest stance toward prior theory and an iterative, narrowing data-collection/analysis cycle—while differing from action research's commitments to organizational transformation and to partnering with research subjects in the change process."
    evidence: "theory"
    support_strength: "moderate"
    outcomes: ["theory-development"]
    predictors: ["grounded-theory", "qualitative-methods"]
  - text: "Despite grounded theory's canonical, widely-cited status in management research, Locke argues scholars commonly cite only the 1967 Glaser and Strauss monograph or the later, more formulaic Strauss and Corbin (1990/1998) accounts, overlooking more than 30 years of methodological elaboration across sociology, nursing, education, and psychology and producing fragmented, superficial applications of the approach."
    evidence: "theory"
    support_strength: "low-to-moderate"
    outcomes: ["methodological-rigor"]
    predictors: ["grounded-theory", "research-paradigm"]
population:
  who: "Not an empirical study of human subjects; this chapter characterizes the published qualitative-research literature in management and organization studies (action research, case study, ethnography, and grounded theory exemplars) and the disciplinary history of qualitative methods."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    This corpus copy is a partial conversion: it contains the book's front matter,
    Introduction, and Chapter 1 in full, followed directly by the complete back-of-book
    reference list (~200 entries); Chapters 2 through 7, which cover grounded theory's
    actual coding, sampling, and analytic procedures in management studies, are absent from
    this markdown file.
limitation:
  primary: "The markdown conversion available in this corpus omits Chapters 2-7, i.e. the operational chapters describing grounded theory's actual research practices, evolution, and application to management studies; only the historical/paradigmatic framing chapter is present."
  others:
    - "As a methodological monograph it makes no original empirical claims about SNH outcomes; its value is purely as a methods reference."
    - "Reflects a single scholar's (Karen Locke's) interpretive synthesis of the grounded theory tradition rather than a systematic review of GT applications."
risk_of_bias: "not-applicable"
relevance_to_project: >
  For SNH qualitative work on remote-worker and open-source community experiences (e.g.,
  maintainer burnout, isolation, belonging), this chapter supplies the paradigmatic
  vocabulary and design rationale for choosing and defending a grounded-theory approach over
  case-study or ethnographic designs when analyzing interview or community-artifact data.
tags:
  topic: ["methodology", "measurement"]
  method: ["qualitative", "theory"]
  population: ["academic-researchers", "management-scholars"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Grounded Theory in Management Research/Grounded Theory in Management Research.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Grounded Theory in Management Research.pdf"
  notes: null

---

id: "hickin-2021-the-effectiveness-of-psychological-interventions-for"
title: "The effectiveness of psychological interventions for loneliness: A systematic review and meta-analysis"
authors:
  - "Hickin, Nisha"
  - "Käll, Anton"
  - "Shafran, Roz"
  - "Sutcliffe, Sebastian"
  - "Manzotti, Grazia"
  - "Langan, Dean"
year: 2021
doi: "10.1016/j.cpr.2021.102066"
venue: {type: "journal", name: "Clinical Psychology Review", volume: 88, issue: null, pages: "102066"}
citation: "Hickin et al. (2021). The effectiveness of psychological interventions for loneliness: A systematic review and meta-analysis. Clinical Psychology Review, 88, 102066. https://doi.org/10.1016/j.cpr.2021.102066"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: true}
gist: >
  This PRISMA-guided systematic review and meta-analysis of 31 RCTs (N=3959) of
  psychological interventions for loneliness across the lifespan found that, pooled across
  28 studies (N=3039), interventions significantly reduced loneliness relative to control
  conditions with a small-to-medium effect (Hedges' g=0.43, 95% CI 0.18-0.68), though
  heterogeneity was substantial (I2=89.55%). Neither CBT-vs-other classification, risk-of-
  bias rating, participant age, nor percentage female moderated effectiveness, while a
  finer-grained breakdown by therapy type (CBT, mindfulness, integrative, social skills,
  social identity, gratitude, reminiscence) showed borderline-significant variation, with
  reminiscence and social identity approaches showing the largest effects. The paper argues
  psychological interventions work by targeting the cognitive/perceptual mechanisms
  (hypervigilance to social threat, negative self-image) that maintain chronic loneliness,
  distinct from interventions that merely increase social contact quantity.
claims:
  - text: "Across 28 RCTs (N=3039), psychological interventions significantly reduced loneliness compared to control groups, yielding a small-to-medium pooled effect (Hedges' g=0.43, 95% CI 0.18-0.68, p<0.001), with substantial heterogeneity across studies (T2=0.49, Q=228.60, p<0.001, I2=89.55%)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["loneliness", "mental-health"]
    predictors: ["intervention"]
  - text: "Type of psychological intervention was not a significant moderator when dichotomized as CBT vs. non-CBT (I2=0, p=0.60), but a 7-category breakdown by therapy type showed borderline-significant variation in effect size (Qb=11.99, df=6, p=0.06), with reminiscence and social identity approach interventions outperforming CBT."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["loneliness"]
    predictors: ["intervention"]
  - text: "Risk-of-bias rating (p=0.84, I2=0%), participant age (Qb=0.02, p=0.74), and percentage of female participants (Qb=0.17, p=0.68) were all non-significant moderators of intervention effectiveness, and an Egger's test found no significant publication bias (p=0.19) despite some funnel-plot asymmetry."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["intervention", "sampling-method"]
population:
  who: "31 RCTs of psychological interventions for loneliness spanning the lifespan (children through older adults), drawn from five databases (Ovid Embase, Ovid Medline, PsycINFO, Web of Science, CINAHL); 28 of the 31 studies (total N=3039, overall review N=3959) were pooled in the meta-analysis"
  where: ["USA", "Iran", "China", "Taiwan", "Netherlands", "Sweden", "South Africa", "Australia", "Japan", "Palestine", "Israel", "UK", "Canada", "Italy"]
  when: "published 2003-2020; literature search conducted November 2019, updated November 2020"
  n: 3959
  sector: ["healthcare", "general-population"]
  sample_notes: >
    Included study sample sizes ranged 17-817 (M=127.71) with mean dropout 10.45% (range
    0-45.4%); only 61% of studies had follow-up data; populations were heterogeneous
    (children, students, older adults, clinical/HIV/cancer/ASD populations) and mostly did
    not report ethnicity; PROSPERO-registered protocol (CRD42019153376) with two independent
    coders (97.2% and 81.55% agreement at screening/full-text stages).
limitation:
  primary: "The review only included psychological interventions, so it cannot compare their efficacy against community-based or social-contact interventions for loneliness, and many included studies did not distinguish transient from chronic loneliness or require participants to be lonely at baseline."
  others:
    - "Substantial unexplained heterogeneity (I2=89.55%) across included studies limits confidence in the pooled effect size."
    - "Several included studies had small samples without power calculations and high attrition (up to 45.4%) without adequate missing-data analysis."
    - "Only 61% of studies collected follow-up data, and follow-up lengths varied, making it impossible to assess durability of effects."
risk_of_bias: "low"
relevance_to_project: >
  Provides the strongest available effect-size benchmark (g=0.43) for
  psychological/cognitive-behavioral interventions targeting loneliness directly, useful for
  calibrating expectations for any SNH intervention aimed at cognitive/perceptual mechanisms
  of loneliness (vs. interventions that just increase contact quantity); also flags that
  intervention type, age, and gender are not reliable moderators, so design choices should
  not assume these matter.
tags:
  topic: ["loneliness", "mental-health", "wellbeing", "methodology"]
  method: ["review-systematic", "secondary-data"]
  population: ["general-population", "clinical-population", "cross-lifespan"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Hickin et al. (2021) - The Effectiveness of Psychological Interventions for Loneliness - A Systematic Review and Meta-Analysis/Hickin et al. (2021) - The Effectiveness of Psychological Interventions for Loneliness - A Systematic Review and Meta-Analysis.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Hickin et al. (2021) - The Effectiveness of Psychological Interventions for Loneliness - A Systematic Review and Meta-Analysis.pdf"
  notes: null

---

id: "hobfoll-2018-conservation-of-resources-in-the-organizational"
title: "Conservation of Resources in the Organizational Context: The Reality of Resources and Their Consequences"
authors:
  - "Hobfoll, Stevan E."
  - "Halbesleben, Jonathon"
  - "Neveu, Jean-Pierre"
  - "Westman, Mina"
year: 2018
doi: "10.1146/annurev-orgpsych-032117-104640"
venue: {type: "journal", name: "Annual Review of Organizational Psychology and Organizational Behavior", volume: 5, issue: 1, pages: "103-128"}
citation: "Hobfoll et al. (2018). Conservation of Resources in the Organizational Context: The Reality of Resources and Their Consequences. Annual Review of Organizational Psychology and Organizational Behavior, 5(1), 103-128. https://doi.org/10.1146/annurev-orgpsych-032117-104640"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This Annual Review article, co-authored by COR theory's originator, restates the theory's
  four principles and three corollaries (primacy of resource loss, resource investment, the
  gain paradox, and the desperation principle; resource caravans and caravan passageways)
  and then surveys post-2014 organizational research testing and extending the theory,
  including the crossover model by which stress, engagement, and specific resources (e.g.,
  self-esteem, self-efficacy) transmit between partners, coworkers, leaders and followers,
  and across cultures. It contributes an integrative framework for why resource loss
  (isolation, exhaustion, unsupportive environments) spirals faster and harder than resource
  gain, and why organizational 'passageways' (supportive versus undermining conditions)
  determine whether individuals and teams can build resilience and engagement.
claims:
  - text: "In a diary/longitudinal couples study, positive states crossed over between intimate partners: daily work engagement (vigor, dedication) transferred from one partner to the other specifically on days with more frequent interaction (Bakker & Xanthopoulou 2009), and performance self-esteem at Time 1 predicted change in a partner's self-esteem at Time 2 when the partner had low baseline self-esteem (Neff et al. 2013b)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["job-engagement", "wellbeing"]
    predictors: ["social-support", "team-cohesion"]
  - text: "In a study of several hundred Japanese employees followed over 12 months (Allen et al. 2016), higher job embeddedness (a resource tied to social networking) buffered the probability of turnover caused by increasing abusive supervision, but this protective effect came at the cost of employees' physical health."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["turnover", "stress"]
    predictors: ["network-structure", "social-support", "leadership-style"]
  - text: "A three-wave longitudinal study of over 16,000 Finnish firefighters and professionals spanning roughly 10 years (Toker & Biron 2012; Airila et al. 2014) found that regular physical activity and job/personal resources (relationships with others, self-esteem) protected against job burnout and depression, with the resource-work-ability relationship fully mediated by work engagement."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["burnout", "depression", "performance"]
    predictors: ["social-support", "intervention"]
population:
  who: "Not a primary study: a narrative synthesis of organizational-psychology research testing Conservation of Resources (COR) theory, drawing on primary studies of professionals, firefighters, healthcare workers, athletes, couples, teams, and job seekers."
  where: ["USA", "Finland", "Israel", "China", "Netherlands", "Spain", "Switzerland", "Japan", "Singapore", "Belgium", "multi-country"]
  when: "Primary studies cited mostly published 2007-2017; review published 2018"
  n: null
  sector: ["mixed-sectors"]
  sample_notes: >
    Aggregate narrative review, not a single sample; no PRISMA-style systematic search
    protocol is reported, so study selection and inclusion criteria are not reproducible,
    and the underlying studies vary in design (cross-sectional survey, diary, longitudinal
    panel) and sample size (from small couple diary studies to a 16,000+ professional
    cohort).
limitation:
  primary: "As a narrative (non-systematic) literature review co-authored by the theory's originator, study selection is not documented via a reproducible search protocol, creating risk of confirmatory citation bias toward findings that support COR theory."
  others:
    - "Individual cited studies vary widely in design quality (cross-sectional survey, diary, longitudinal panel) and are not critically appraised or weighted within the review."
    - "Most underlying primary studies rely on self-report survey measures, raising common-method-variance concerns the review does not address."
    - "The cross-cultural section leans heavily on Hofstede's individualism/collectivism framework, a taxonomy criticized elsewhere in the literature for oversimplifying cultural variation."
risk_of_bias: "medium"
relevance_to_project: >
  COR theory's crossover model and resource-caravan/passageway concepts give the project a
  mechanism for how organizational support, leader engagement, and work-family resources
  propagate positive states (engagement, self-efficacy) across teams and into workers' home
  lives, or conversely how unsupportive 'passageways' accelerate resource-loss spirals into
  burnout and turnover -- directly informing how SNH interventions should target upstream
  organizational conditions rather than only individual coping.
tags:
  topic: ["burnout", "job-engagement", "wellbeing", "social-support", "methodology"]
  method: ["review"]
  population: ["knowledge-workers", "cross-cultural", "organizational"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Hobfoll et al. (2018) - Conservation of Resources in the Organizational Context - The Reality of Resources and Their Consequences/Hobfoll et al. (2018) - Conservation of Resources in the Organizational Context - The Reality of Resources and Their Consequences.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Hobfoll et al. (2018) - Conservation of Resources in the Organizational Context - The Reality of Resources and Their Consequences.pdf"
  notes: null

---

id: "holt-2015-loneliness-and-social-isolation-as-risk"
title: "Loneliness and Social Isolation as Risk Factors for Mortality"
authors:
  - "Holt-Lunstad, Julianne"
  - "Smith, Timothy B."
  - "Baker, Mark"
  - "Harris, Tyler"
  - "Stephenson, David"
year: 2015
doi: "10.1177/1745691614568352"
venue: {type: "journal", name: "Perspectives on Psychological Science", volume: 10, issue: 2, pages: "227-237"}
citation: "Holt-Lunstad et al. (2015). Loneliness and Social Isolation as Risk Factors for Mortality. Perspectives on Psychological Science, 10(2), 227-237. https://doi.org/10.1177/1745691614568352"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  This meta-analytic review pools 70 independent prospective studies (3,407,134
  participants, ~7-year average follow-up) and finds that social isolation, loneliness, and
  living alone each independently and comparably predict earlier mortality, with fully-
  adjusted odds ratios of 1.29, 1.26, and 1.32 respectively. Objective and subjective
  isolation measures did not differ in predictive strength, and the risk was actually larger
  for adults under 65 than for older adults, challenging the assumption that isolation is
  chiefly an old-age problem. The authors argue the magnitude of this risk rivals well-
  established mortality risk factors like obesity and smoking, and call for social
  isolation/loneliness to be treated as a public health priority.
claims:
  - text: "Across fully adjusted statistical models controlling for health status and other confounds, weighted average odds ratios for mortality were 1.29 for social isolation, 1.26 for loneliness, and 1.32 for living alone, corresponding to 26-32% increased likelihood of death, with no significant difference among the three measures."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness", "social-support"]
  - text: "Risk from social deficits was moderated by age: studies with average participant age under 65 had larger effect sizes (OR = 1.57 adjusted, 1.92 unadjusted) than studies with participants over 75 (OR = 1.14 adjusted, 1.28 unadjusted), indicating isolation and loneliness are more predictive of death in midlife than in old age."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness"]
  - text: "Unadjusted effect sizes were significantly larger than fully adjusted ones (p < .001), and studies that failed to exclude terminally ill or already-declining participants at baseline showed inflated risk estimates (OR = 1.95 vs. 1.38), underscoring the importance of controlling for reverse causality via prior health status when estimating the isolation-mortality link."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["mortality"]
    predictors: ["isolation", "loneliness", "social-support"]
population:
  who: "70 independent prospective cohort/longitudinal studies (January 1980-February 2014) of adults with quantitative mortality outcomes as a function of social isolation, loneliness, or living alone"
  where: ["Europe", "North America", "Asia", "Australia", "multiple regions"]
  when: "1980-2014 (studies with initial data collection averaging 1993)"
  n: 3407134
  sector: ["public-health", "clinical", "community"]
  sample_notes: >
    63% community (normal population) samples, 37% patients with a medical condition; mean
    participant age 66.0 at intake, mean follow-up 7.1 years; 24% of studies had average age
    <=59, only 9% <50; high between-study heterogeneity (I2 = 97.8%); publication bias
    checks (Egger's test, fail-safe N = 1,268, trim-and-fill) found no evidence of missing
    studies.
limitation:
  primary: "Extremely high heterogeneity across included studies (I2 = 97.8%) means pooled effect sizes mask substantial variability, and causality cannot be confirmed despite prospective designs and covariate adjustment."
  others:
    - "Very few studies measured both objective isolation and loneliness in the same sample, so direct within-study comparisons of their relative/synergistic effects remain rare and largely untested."
    - "Marital status was not coded as a moderator despite being plausibly confounded with both age and living-alone status, limiting interpretation of the age-moderation finding."
    - "Most data still come from older-adult samples (only 24% averaged age <=59), so conclusions about younger and midlife adults rest on a comparatively small subset of studies."
risk_of_bias: "low"
relevance_to_project: >
  This is a foundational, high-N quantification of the health stakes of isolation and
  loneliness that the SNH project can cite to justify prioritizing connection and belonging
  interventions; the finding that midlife/working-age adults (not just the elderly) show the
  largest mortality risk from isolation directly supports targeting remote and hybrid
  workers, not just retirees, in SNH design and measurement choices.
tags:
  topic: ["isolation", "loneliness", "wellbeing", "mental-health", "community-health"]
  method: ["review-systematic", "secondary-data"]
  population: ["older-adults", "general-population", "community-samples"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/holt-lunstad-et-al-2015-loneliness-and-social-isolation-as-risk-factors-for-mortality-a-meta-analytic-review.pdf"
  notes: null

---

id: "counts-2021-how-remote-work-affects-our-communication"
title: "How Remote Work Affects Our Communication and Collaboration"
authors:
  - "Counts, Laura"
year: 2021
doi: null
venue: {type: "other", name: "Greater Good Magazine (UC Berkeley)", volume: null, issue: null, pages: null}
citation: "Counts (2021). How Remote Work Affects Our Communication and Collaboration. Greater Good Magazine (UC Berkeley)."
article_type: "commentary"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This Greater Good Magazine news piece reports on a quasi-experimental
  Microsoft/MIT/Berkeley study of over 61,000 U.S. employees that used the company's abrupt
  COVID-19 work-from-home mandate to isolate the causal effects of full-time remote work on
  communication metadata. It summarizes findings that remote work made collaboration
  networks more siloed, shifted communication toward asynchronous channels, and modestly
  reduced meeting hours, with implications for hybrid-work policy design.
claims:
  - text: "Company-wide remote work caused workers to spend about 25% less time collaborating with colleagues across formal and informal business groups compared to pre-pandemic levels, and workers added new collaborators more slowly."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
  - text: "Remote work shifted communication from synchronous to asynchronous modes (more time on email and instant messaging, less time in person, on the phone, or on video calls), while also increasing communication frequency within workers' existing inner network."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["communication", "collaboration"]
    predictors: ["remote-work-intensity", "network-structure"]
  - text: "Remote work caused total hours spent in meetings to decrease by about 5%, suggesting the widely reported pandemic-era rise in meeting load was driven by other pandemic-related factors rather than remote work itself."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["communication", "collaboration"]
    predictors: ["remote-work-intensity"]
population:
  who: "Over 61,000 U.S.-based Microsoft information workers, studied through anonymized metadata on emails, instant messages, calls, meetings, and working hours before and after a company-wide COVID-19 work-from-home mandate."
  where: ["United States"]
  when: "Pre-pandemic period through the 2020 Microsoft work-from-home mandate"
  n: 61000
  sector: ["technology"]
  sample_notes: >
    Sample is limited to one large technology firm's U.S. workforce; the mandate allowed
    comparison of employees already remote pre-pandemic against those who newly shifted
    online, matched on role, managerial status, business group, and tenure. This document is
    journalism summarizing the original Nature Human Behaviour study (Yang et al., 2021),
    not the primary paper itself.
limitation:
  primary: "This is a secondary science-journalism summary of a peer-reviewed study rather than the primary source, so full statistical detail, confidence intervals, and methodological nuance are not presented."
  others:
    - "Findings come from a single large technology company and may not generalize to other industries, smaller firms, or non-U.S. contexts."
    - "The pandemic context (school closures, caregiving, stress) complicates isolating pure remote-work effects, though the authors attempted to control for this via comparison groups."
risk_of_bias: "medium"
relevance_to_project: >
  Summarizes large-scale, quasi-experimental evidence that shifting to full-time remote work
  causally shrinks and siloes collaboration networks and pushes communication toward
  asynchronous channels, directly informing the SNH project's concern that remote/hybrid
  policy choices can erode weak-tie network structure and cross-group belonging.
tags:
  topic: ["remote-work", "hybrid-work", "collaboration", "social-presence"]
  method: ["longitudinal", "secondary-data", "measurement"]
  population: ["knowledge-workers", "tech-sector", "us-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/How Remote Work Affects Our Communication and Collaboration - Greater Good Berkeley 2021/How Remote Work Affects Our Communication and Collaboration - Greater Good Berkeley 2021.md"
  pdf: "papers/Remote Workers/How Remote Work Affects Our Communication and Collaboration - Greater Good Berkeley 2021.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "jaiswal-2024-impact-of-employee-well-being-on"
title: "Impact of employee well-being on performance in the context of crisis-induced remote work: role of boundary control and professional isolation"
authors:
  - "Jaiswal, Akanksha"
  - "Prabhakaran, Neethu"
year: 2024
doi: "10.1108/er-08-2022-0384"
venue: {type: "journal", name: "Employee Relations: The International Journal", volume: 46, issue: 1, pages: "115-132"}
citation: "Jaiswal et al. (2024). Impact of employee well-being on performance in the context of crisis-induced remote work: role of boundary control and professional isolation. Employee Relations: The International Journal, 46(1), 115-132. https://doi.org/10.1108/er-08-2022-0384"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  In a survey of 218 full-time employees at large Indian IT/ITeS firms during crisis-induced
  remote work, employee well-being significantly predicted task performance, and this link
  was strengthened when boundary control was high and professional isolation was low. A
  significant three-way interaction among well-being, boundary control, and professional
  isolation on performance shows these two contextual factors jointly, not just
  independently, shape how well-being translates into performance during forced remote work.
claims:
  - text: "Employee well-being (WHO-5) significantly predicted task performance during remote work (beta = 0.276, t = 4.09, p < .001); the overall regression model was significant (F = 6.38, p < .001, df = 3, 214)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "wellbeing"]
    predictors: ["remote-work-intensity"]
  - text: "Boundary control moderated the well-being-performance link: it had a direct positive effect on performance (coeff = 0.23, p = .003) and a significant interaction with well-being (coeff = 0.21, p = .003), such that the well-being-to-performance effect was strongest (4.05) when boundary control was high."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance"]
    predictors: ["boundary-management", "wellbeing"]
  - text: "Professional isolation had a significant negative direct effect on performance (coeff = -0.17, p = .043) and correlated negatively with well-being (r = -0.30, p < .01) and performance (r = -0.16, p < .05); the three-way interaction of well-being, boundary control, and professional isolation on performance was significant (p = .010), explaining an additional 3.56% of variance, with the weakest well-being-performance link (2.85) when isolation was high and boundary control low."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "isolation"]
    predictors: ["isolation", "boundary-management"]
population:
  who: "Full-time employees with 5+ years' work experience at large Indian information technology and IT-enabled services (IT/ITeS) organisations, working remotely or hybrid during/after COVID-19"
  where: ["India"]
  when: null
  n: 218
  sector: ["technology", "corporate"]
  sample_notes: >
    Purposive (non-probability) sample; 300 employees contacted, 218 responded (72.6%
    response rate); self-report survey via Google Forms; 56% male, majority aged 31-40 and
    married; 62% hybrid, 27% fully remote, 11% office-based; Harman's single-factor test
    found 30.93% variance (below 50% CMB threshold).
limitation:
  primary: "Small sample size and cross-sectional design preclude causal claims and limit confidence in the moderation findings; the authors themselves flag this as their chief limitation."
  others:
    - "Single-country (Indian IT sector) sample limits generalisability to other cultural or industry contexts."
    - "All measures are self-report, raising common method bias risk despite procedural remedies and a Harman's test."
    - "Only two moderators (boundary control, professional isolation) examined; other plausible contextual factors like communication quality were not tested."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a validated professional-isolation scale (Golden et al. 2008, 7 items) and
  boundary-control scale (Kossek et al. 2012) with evidence that isolation directly
  suppresses performance and blunts the benefit of well-being, giving the SNH project both
  measurement instruments and a mechanism (boundary control x isolation interaction) for why
  remote-work interventions should jointly target boundary-setting support and
  belonging/connection, not well-being alone.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "work-life-balance"]
  method: ["survey", "cross-sectional", "moderation-analysis"]
  population: ["it-sector", "india", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Impact of Employee Well-Being on Performance in Crisis-Induced Remote Work - Boundary Control and Professional Isolation/Impact of Employee Well-Being on Performance in Crisis-Induced Remote Work - Boundary Control and Professional Isolation.md"
  pdf: "papers/Remote Workers/Impact of Employee Well-Being on Performance in Crisis-Induced Remote Work - Boundary Control and Professional Isolation.pdf"
  notes: null

---

id: "tarafdar-2010-impact-of-technostress-on-end-user"
title: "Impact of Technostress on End-User Satisfaction and Performance"
authors:
  - "Tarafdar, Monideepa"
  - "Tu, Qiang"
  - "Ragu-Nathan, T. S."
year: 2010
doi: "10.2753/mis0742-1222270311"
venue: {type: "journal", name: "Journal of Management Information Systems", volume: 27, issue: 3, pages: "303-334"}
citation: "Tarafdar et al. (2010). Impact of Technostress on End-User Satisfaction and Performance. Journal of Management Information Systems, 27(3), 303-334. https://doi.org/10.2753/mis0742-1222270311"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Survey of 233 ICT end users in two public-sector organizations tests a structural model in
  which five technostress creators (techno-overload, techno-invasion, techno-complexity,
  techno-insecurity, techno-uncertainty) reduce end-user satisfaction with the technology
  they use and their productivity/innovation performance on ICT-mediated tasks. It also
  shows that organizational mechanisms enabling user involvement in ICT development and
  support for innovation/experimentation weaken technostress creators and boost satisfaction
  and performance, both directly and by offsetting stress. The paper extends technostress
  research beyond general psychological/behavioral strain into the specific domain of end-
  user computing outcomes (satisfaction, productivity, innovation).
claims:
  - text: "Technostress creators had a significant negative direct effect on end-user performance (standardized path coefficient = -0.33, p < 0.01) and a significant negative effect on end-user satisfaction (-0.18, p < 0.05)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "job-satisfaction", "stress"]
    predictors: ["technostress", "workload"]
  - text: "Involvement facilitation reduced technostress creators (path = -0.17, p < 0.05) and increased end-user satisfaction (0.18, p < 0.05); innovation support increased involvement facilitation (0.56, p < 0.01) and end-user satisfaction (0.24, p < 0.01), showing organizational mechanisms can offset technostress."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress"]
    predictors: ["inclusiveness", "autonomy", "organizational-culture"]
  - text: "End-user satisfaction positively predicted end-user performance (path = 0.18, p < 0.05), so technostress creators also depressed performance indirectly through reduced satisfaction, in addition to their direct negative effect on performance."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "job-satisfaction"]
    predictors: ["technostress"]
population:
  who: "233 ICT end users (mostly clerical/administrative and middle-management staff) at two U.S. public-sector organizations"
  where: ["United States"]
  when: "2006-2007"
  n: 233
  sector: ["public-sector", "human-services"]
  sample_notes: >
    Non-random convenience sample; organizations chosen via authors' contacts. Self-selected
    respondents (questionnaires provided only on request), 88.2% response rate among those
    who requested a questionnaire (73% of all employees e-mailed). Sample skewed 78% female,
    highly tenured (95% >5 years' work experience). Single-sector (government) design limits
    generalizability.
limitation:
  primary: "Non-random, self-selected sample from only two government organizations chosen through the authors' personal contacts, likely biased toward respondents who already perceived high technostress."
  others:
    - "Cross-sectional survey design cannot establish causal direction despite the structural path model."
    - "End-user performance was measured via self-reported perceptions rather than independent supervisor/peer assessment, introducing subjective bias."
    - "Findings are from public-sector organizations only; generalization to other sectors (e.g., private-sector or remote/distributed work) requires caution."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a validated construct and measurement model for 'technostress creators'
  (overload, invasion, complexity, insecurity, uncertainty) with quantified links to
  satisfaction and productivity, useful for SNH work on technostress and remote-work
  intensity as predictors of wellbeing/performance; also evidences that involvement
  facilitation and innovation-support mechanisms are actionable organizational interventions
  that reduce technostress and its negative effects.
tags:
  topic: ["technostress", "remote-work", "wellbeing", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["office-workers", "public-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Impact of Technostress on End-User Satisfaction and Performance/Impact of Technostress on End-User Satisfaction and Performance.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Impact of Technostress on End-User Satisfaction and Performance.pdf"
  notes: null

---

id: "salanova-2013-the-dark-side-of-technologies-technostress"
title: "The dark side of technologies: Technostress among users of information and communication technologies"
authors:
  - "Salanova, Marisa"
  - "Llorens, Susana"
  - "Cifre, Eva"
year: 2013
doi: "10.1080/00207594.2012.680460"
venue: {type: "journal", name: "International Journal of Psychology", volume: 48, issue: 3, pages: "422-436"}
citation: "Salanova et al. (2013). The dark side of technologies: Technostress among users of information and communication technologies. International Journal of Psychology, 48(3), 422-436. https://doi.org/10.1080/00207594.2012.680460"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This study surveys 1072 ICT users (675 non-intensive, 397 intensive) to test whether
  technostress is composed of two distinct psychological experiences: technostrain (anxiety,
  fatigue, scepticism, inefficacy) and technoaddiction (excessive/compulsive ICT use).
  Confirmatory factor analyses support a four-factor technostrain structure and a related
  but separate technoaddiction dimension, and regression analyses show job demands
  (overload, role ambiguity, mobbing) increase both, while job/personal resources (autonomy,
  social support, transformational leadership, mental/emotional competences) mostly reduce
  them. Notably, social support shows a double-edged effect: it lowers fatigue but increases
  feelings of inefficacy, suggesting help-seeking around technology use can carry a
  competence cost.
claims:
  - text: "Confirmatory multigroup factor analysis supported a four-factor structure of technostrain (anxiety, fatigue, scepticism, inefficacy) that fit significantly better than a one-factor model (delta chi-square(12)=3102.04, p<.001), holding across both non-intensive and intensive ICT user samples."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "burnout"]
    predictors: ["technostress"]
  - text: "Job demands positively predicted technostrain and technoaddiction: work overload, role ambiguity, and mobbing predicted both, while mobbing was the strongest single predictor of anxiety (beta=.122 to .207, p<.05 to p<.001) across samples; lack of job resources (autonomy, transformational leadership, ICT facilitators) and lack of personal resources (mental competence) predicted technostrain specifically."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "anxiety", "burnout"]
    predictors: ["workload", "leadership-style", "autonomy"]
  - text: "Social support showed an ambivalent effect: it was negatively associated with fatigue (beta=-.090, p<.05) but positively associated with inefficacy (beta=.114, p<.01), i.e., more social support reduced exhaustion but increased feelings of technological inefficacy, interpreted via reciprocity/equity theory as a cost of needing to be helped."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "anxiety"]
    predictors: ["social-support"]
population:
  who: "Spanish ICT users in workplace settings, split into non-intensive users (ICT as one tool among others) and intensive users (ICT as the core, daily tool, working in a fully virtual educational organization)"
  where: ["Spain"]
  when: null
  n: 1072
  sector: ["education", "mixed-occupations"]
  sample_notes: >
    Two convenience samples: 675 non-intensive users (52% women, mean age 34, mixed
    occupations across technical/supervisory/managerial/blue-collar roles) and 397 intensive
    users (62% women, age undisclosed by the employer for anonymity reasons, all from one
    virtual-services educational organization). Not randomly sampled; intensive-user sample
    drawn from a single organization limits generalizability.
limitation:
  primary: "Cross-sectional self-report design precludes causal inference about whether job demands/resources cause technostress or vice versa, and both predictor and outcome measures share method (self-report)."
  others:
    - "The intensive-user sample is drawn from a single virtual-services educational organization, limiting generalizability of the technoaddiction findings."
    - "Age data for the intensive-user sample was withheld by the employer, preventing full demographic comparison between groups."
    - "Technoaddiction's hypothesized two-factor (excessive/compulsive) structure was not confirmed; only a single dimension was found, partially disconfirming the theoretical model."
risk_of_bias: "medium"
relevance_to_project: >
  Provides validated measurement scales and a demands-resources framework (RED model) for
  technostress/technostrain/technoaddiction that the SNH project can borrow for measuring
  technology-driven burnout and anxiety in remote/hybrid workers, and its finding that
  social support can paradoxically increase feelings of inefficacy is a caution for
  designing peer-support or help-seeking interventions around technology use.
tags:
  topic: ["technostress", "burnout", "remote-work", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["ict-users", "office-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Int J Psychol - 2012 - Salanova - The dark side of technologies  Technostress among users of information and communication/Int J Psychol - 2012 - Salanova - The dark side of technologies  Technostress among users of information and communication.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Int J Psychol - 2012 - Salanova - The dark side of technologies  Technostress among users of information and communication.pdf"
  notes: null

---

id: "ferrara-2022-investigating-the-role-of-remote-working"
title: "Investigating the Role of Remote Working on Employees’ Performance and Well-Being: An Evidence-Based Systematic Review"
authors:
  - "Ferrara, Bruna"
  - "Pansini, Martina"
  - "De Vincenzi, Clara"
  - "Buonomo, Ilaria"
  - "Benevene, Paula"
year: 2022
doi: "10.3390/ijerph191912373"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 19, issue: 19, pages: "12373"}
citation: "Ferrara et al. (2022). Investigating the Role of Remote Working on Employees’ Performance and Well-Being: An Evidence-Based Systematic Review. International Journal of Environmental Research and Public Health, 19(19), 12373. https://doi.org/10.3390/ijerph191912373"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This PRISMA-guided systematic review synthesizes 20 peer-reviewed papers (2010-2021, pre-
  COVID) on how remote/telework affects employees' well-being and performance, finding
  consistently mixed effects: teleworking generally raises job satisfaction, engagement, and
  reduces work-life conflict, but also elevates stress, technostress, role ambiguity, and
  family-to-work conflict in a substantial subset of studies. The review argues the
  intensity of telework and the presence of organizational and colleague support, not remote
  work per se, drive whether outcomes are positive or negative, and calls for organizational
  strategies (training, boundary-management skills, culture) to shape telework's effects.
claims:
  - text: "Across the 20 included studies, teleworkers frequently reported higher job satisfaction, work engagement, and organizational commitment, often mediated by lower work-life conflict from more time at home, while one study (Suh & Lee 2017) found the opposite: higher telework intensity was linked to higher strain and lower job satisfaction."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "job-engagement", "work-life-balance"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Lack of colleague/organizational support during teleworking strengthened the link between telework and stress/burnout symptoms; Fonner and Roloff (2012) found high ICT-based connectivity during telework was associated with lower organizational identification and higher stress from interruptions."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["stress", "burnout", "sense-of-belonging"]
    predictors: ["social-support", "remote-work-intensity", "technostress"]
  - text: "Findings on work-life balance and physical/mental health were heterogeneous and sometimes contradictory: some studies found teleworking lowered time pressure, work-to-home conflict, pain, and fatigue, while others (including a longitudinal study) found higher work-family conflict, fatigue, and stress with increasing telework time, with effects moderated by employees' ability to manage work/private-life boundaries (Grant et al. 2013) and by organizational support (Bentley et al. 2016)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress", "wellbeing"]
    predictors: ["boundary-management", "remote-work-intensity", "social-support"]
population:
  who: "20 peer-reviewed empirical papers (quantitative, qualitative, and mixed-methods) on remote/tele-workers published 2010-2021, spanning varied organization types (private, public, voluntary, IT, academia, government) and sample sizes ranging from N=11 to N=100,457"
  where: ["EU", "US", "mixed/international (unspecified in several included studies)"]
  when: "2010-2021 (search conducted May 2021-June 2022; explicitly excludes COVID-era-focused papers)"
  n: 20
  sector: ["mixed", "IT", "public-sector", "academia"]
  sample_notes: >
    Review of pre-selected literature, not a primary sample; included studies vary widely in
    sample size, organization type, and telework definition (several report organization
    type or definition as 'not specified'). Deliberately excludes COVID-19-specific studies
    and grey literature (e.g., organizational reports), which the authors flag as a
    limitation.
limitation:
  primary: "The review explicitly excludes COVID-19-related papers, so it captures only pre-pandemic remote-work dynamics and cannot speak to the intensified, often involuntary telework arrangements that became common from 2020 onward."
  others:
    - "Grey literature (e.g., organizational reports) was excluded, potentially omitting practically relevant findings not published in peer-reviewed journals."
    - "Included studies use inconsistent definitions of telework/remote work and often fail to report organization type, which limits comparability across findings."
    - "As a narrative synthesis rather than a meta-analysis, the review cannot quantify pooled effect sizes across the heterogeneous outcomes reported."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's core hypothesis that remote-work outcomes (isolation,
  stress, satisfaction) are contingent on moderators like organizational/colleague support
  and boundary-management skill rather than remote work itself, supporting design choices
  that target support and boundary-management interventions over blanket remote/in-office
  policy.
tags:
  topic: ["remote-work", "wellbeing", "work-life-balance", "technostress", "job-satisfaction"]
  method: ["review-systematic", "secondary-data"]
  population: ["knowledge-workers", "mixed-sector", "teleworkers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Investigating the Role of Remote Working on Employees Performance and Well-Being - An Evidence-Based Systematic Review/Investigating the Role of Remote Working on Employees Performance and Well-Being - An Evidence-Based Systematic Review.md"
  pdf: "papers/Remote Workers/Investigating the Role of Remote Working on Employees Performance and Well-Being - An Evidence-Based Systematic Review.pdf"
  notes: null

---

id: "bailey-2002-a-review-of-telework-research-findings"
title: "A review of telework research: findings, new directions, and lessons for the study of modern work"
authors:
  - "Bailey, Diane E."
  - "Kurland, Nancy B."
year: 2002
doi: "10.1002/job.144"
venue: {type: "journal", name: "Journal of Organizational Behavior", volume: 23, issue: 4, pages: "383-400"}
citation: "Bailey et al. (2002). A review of telework research: findings, new directions, and lessons for the study of modern work. Journal of Organizational Behavior, 23(4), 383-400. https://doi.org/10.1002/job.144"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This narrative review synthesizes roughly 80 empirical telework studies (plus ~50 essays)
  from the 1980s-2001 around three questions: who teleworks, why, and what happens when they
  do. The authors find demographic predictors of who teleworks are inconsistent across
  studies, but work-related factors (manager's willingness, self-perceived job suitability)
  are the strongest predictors; commonly assumed motives like commute reduction and
  childcare do not hold up empirically; and there is little convincing evidence that
  telework raises job satisfaction or productivity once self-report bias is accounted for. A
  central methodological argument is that because most teleworkers work remotely only a few
  days a month, individual-level outcomes like social isolation may be overstated in the
  literature because researchers implicitly assume full-time remote work.
claims:
  - text: "Across large-sample models (e.g., >500 public-agency workers), work-related factors such as manager's willingness, workplace interaction, and self-perceived job suitability are the strongest predictors of who actually teleworks, outweighing demographic traits; commute time/distance is not predictive of telework preference or frequency in several large studies, and family-balance motives are undermined by evidence that women do not dominate teleworking populations."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: []
    predictors: ["remote-work-intensity", "leadership-style", "boundary-management"]
  - text: "Reported productivity and job-satisfaction gains among teleworkers rest almost entirely on self-report data from self-selected volunteers (e.g., 75% of interviewed teleworkers report being more effective at home, a rate roughly matching the volunteer rate for telework itself), and some studies find teleworkers conflate 'more productive' with simply working more hours (40-48% report increased hours), so the review concludes there is little clear evidence telework increases job satisfaction or productivity."
    evidence: "review-narrative"
    support_strength: "low-to-moderate"
    outcomes: ["productivity", "job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Because most teleworkers work remotely only a few days per month (e.g., average 5-6 days/month in one 163-person sample; only 11 of 563 employees teleworked 3+ days/week in another), studies of part-time telework find little impact on social/professional isolation or communication: teleworkers are not excluded from office communication networks and show no difference in communication frequency, channel use, or perceived communication problems compared to office-based colleagues (Belanger 1999a; Duxbury & Neufeld 1999)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["isolation", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "The literature itself: more than 80 peer-reviewed empirical telework studies plus 50+ essays, spanning organizational behavior, transportation, urban planning, information science, law, and sociology"
  where: ["United States", "Europe", "Finland", "Singapore"]
  when: "approximately 1975-2001"
  n: null
  sector: ["knowledge-work", "clerical-office", "public-sector", "mixed"]
  sample_notes: >
    This is a narrative synthesis of prior primary studies (surveys, case studies, a growing
    minority of hypothesis-driven/model-building studies), not a primary data collection;
    underlying studies vary widely in sample size (single digits to 600+), sampling method,
    and rigor, and the review does not describe a formal systematic search or inclusion
    protocol.
limitation:
  primary: "The review is narrative rather than systematic (no stated search strategy, inclusion criteria, or quality-appraisal protocol), so conclusions reflect the authors' synthesis of a self-selected literature rather than a reproducible systematic review."
  others:
    - "Much of the underlying empirical base relies on self-report productivity/satisfaction data from self-selected teleworker volunteers, which the authors themselves flag as biased."
    - "Published in 2002 and covering studies through 2001, so it predates broadband-era, pandemic-era, and fully-remote (as opposed to part-time telework) research contexts relevant to modern remote work."
    - "The authors note much of the primary literature they review is atheoretical and methodologically weak (small samples, poor construct definitions of 'teleworker')."
risk_of_bias: "medium"
relevance_to_project: >
  Directly cautions the SNH project against assuming remote-work isolation effects
  generalize from part-time/occasional telework research: the review's core finding is that
  low telework frequency likely moderates or negates individual-level isolation and
  communication effects, which matters for interpreting older isolation studies and for
  designing measures that capture remote-work intensity/frequency rather than binary remote-
  vs-office status. It also warns that self-report productivity/satisfaction claims in
  telework research are confounded with self-selection and hours worked, a measurement
  caveat relevant to SNH's own outcome instruments.
tags:
  topic: ["remote-work", "isolation", "methodology", "job-satisfaction", "productivity"]
  method: ["literature-review"]
  population: ["remote-workers", "knowledge-workers", "clerical-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/J Organ Behavior - 2002 - Bailey - A review of telework research  findings  new directions  and lessons for the study of/J Organ Behavior - 2002 - Bailey - A review of telework research  findings  new directions  and lessons for the study of.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/J Organ Behavior - 2002 - Bailey - A review of telework research  findings  new directions  and lessons for the study of.pdf"
  notes: null

---

id: "cooper-2002-telecommuting-professional-isolation-and-employee-development"
title: "Telecommuting, professional isolation, and employee development in public and private organizations"
authors:
  - "Cooper, Cecily D."
  - "Kurland, Nancy B."
year: 2002
doi: "10.1002/job.145"
venue: {type: "journal", name: "Journal of Organizational Behavior", volume: 23, issue: 4, pages: "511-532"}
citation: "Cooper et al. (2002). Telecommuting, professional isolation, and employee development in public and private organizations. Journal of Organizational Behavior, 23(4), 511-532. https://doi.org/10.1002/job.145"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Using grounded theory on 93 semi-structured interviews (telecommuters, their supervisors,
  and non-telecommuting colleagues) at two private high-tech firms and two city governments,
  the study finds that telecommuters' professional isolation is inseparable from three
  employee-development activities they miss when off-site: interpersonal networking,
  informal learning, and mentoring. Private-sector respondents valued these informal
  channels far more than public-sector respondents and were correspondingly more worried
  that telecommuting would hurt career development, a difference the authors attribute to
  the public sector's more formalized, rule-based promotion systems that reduce reliance on
  informal access.
claims:
  - text: "82% of private-sector supervisors and 75% of private-sector telecommuters expressed concern that telecommuting impedes interpersonal networking, compared with only 15% of public-sector supervisors and 15% of public-sector telecommuters."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "collaboration"]
    predictors: ["remote-work-intensity", "organizational-culture"]
  - text: "53% of private-sector supervisors raised mentoring concerns for telecommuters versus 0% of public-sector supervisors, and public-sector employees relied much more heavily on formal channels (journals, scheduled meetings, formal training) rather than informal mentoring or learning."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation"]
    predictors: ["peer-mentoring", "organizational-culture", "community-engagement"]
  - text: "No consistent directional relationship was found between telecommuting frequency and professional isolation: non-telecommuters and supervisors believed lower telecommuting frequency reduces isolation, whereas telecommuters themselves reported limiting their own telecommuting frequency out of fear of becoming professionally isolated."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["isolation"]
    predictors: ["remote-work-intensity"]
population:
  who: "93 employees (37 telecommuters, 30 supervisors, 25 non-telecommuting co-workers) interviewed in triads at two publicly-traded high-tech firms and two city governments with formally sanctioned telecommuting programs"
  where: ["United States"]
  when: "1997-1999"
  n: 93
  sector: ["technology", "government", "private-sector", "public-sector"]
  sample_notes: >
    Purposive sample of four organizations chosen because they had established, management-
    supported telecommuting programs (not representative of informal or unsanctioned
    telecommuting); private-sector respondents recruited via HR contacts, public-sector via
    telecommuting-program administrators; all contacted individuals agreed to participate.
limitation:
  primary: "Grounded-theory design draws on only four organizations with formally sanctioned, management-endorsed telecommuting programs, limiting generalizability to informal or unsupported telecommuting arrangements, and cannot cleanly separate sector, telecommuting frequency, and job-task type as confounding explanations for the public/private differences observed."
  others:
    - "Findings rest on self-reported perceptions of isolation and development opportunities rather than objective outcomes such as promotion rates or validated isolation scales."
    - "Public-sector employees telecommuted markedly less often than private-sector employees, confounding the sector comparison with a frequency effect."
    - "Cross-sectional interview design (1997-1999) cannot establish the temporal/causal direction between professional isolation and telecommuting frequency; authors explicitly frame results as propositions for future positivist testing."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a mechanism-level account of remote-worker professional isolation, decomposing it
  into loss of interpersonal networking, informal learning, and mentoring, and shows that
  organizational formalization (structured promotion systems, scheduled check-ins, written
  reporting like the 'telecommute diary') can buffer isolation even under infrequent in-
  person contact. This informs SNH intervention design by suggesting that formal substitutes
  for informal channels (structured mentoring, mandatory meetings) may reduce professional
  isolation for distributed workers independent of raw telecommuting frequency.
tags:
  topic: ["remote-work", "isolation", "community-health", "social-support"]
  method: ["qualitative", "interview"]
  population: ["remote-workers", "public-sector", "private-sector", "technology"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/J Organ Behavior - 2002 - Cooper - Telecommuting  professional isolation  and employee development in public and private/J Organ Behavior - 2002 - Cooper - Telecommuting  professional isolation  and employee development in public and private.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/J Organ Behavior - 2002 - Cooper - Telecommuting  professional isolation  and employee development in public and private.pdf"
  notes: null

---

id: "schaufeli-2004-job-demands-job-resources-and-their"
title: "Job demands, job resources, and their relationship with burnout and engagement: a multi‐sample study"
authors:
  - "Schaufeli, Wilmar B."
  - "Bakker, Arnold B."
year: 2004
doi: "10.1002/job.248"
venue: {type: "journal", name: "Journal of Organizational Behavior", volume: 25, issue: 3, pages: "293-315"}
citation: "Schaufeli et al. (2004). Job demands, job resources, and their relationship with burnout and engagement: a multi‐sample study. Journal of Organizational Behavior, 25(3), 293-315. https://doi.org/10.1002/job.248"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This multi-sample study of 1,698 Dutch employees across four service organizations tests
  and confirms a Job Demands-Resources (JD-R) model in which burnout and engagement are
  distinct, moderately negatively correlated states (sharing 10-25% of variance) with
  different predictors and consequences. Burnout is driven mainly by high job demands and
  mediates the path to health problems, while engagement is driven exclusively by job
  resources and mediates the path to (lower) turnover intention, implying that reducing
  demands and boosting resources require separate intervention strategies rather than a
  single fix.
claims:
  - text: "Burnout and engagement loaded on two separate, moderately negatively correlated latent factors (correlations ranging from -0.38 to -0.51 across the four samples) rather than one bipolar dimension, with professional efficacy loading on the engagement factor rather than burnout."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["sense-of-belonging"]
  - text: "Job demands (workload, emotional demands) were the dominant predictor of burnout, which fully mediated the relationship between job demands and self-reported health problems; the effort-driven energetic process explained substantially more variance (mean 48% in burnout, range 29-72%) than the motivational process (mean 27% in engagement)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "wellbeing"]
    predictors: ["workload", "technostress"]
  - text: "Job resources (performance feedback, social support from colleagues, supervisory coaching) predicted engagement, which mediated the relationship between resources and (low) turnover intention; only in one of four samples was there a significant direct effect of resources on turnover intention (0.30), and cross-links between resources and burnout, and burnout and turnover intention, were comparatively weak."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "turnover"]
    predictors: ["social-support", "leadership-style"]
population:
  who: "Employees from four Dutch service organizations: an insurance company (N=381), an occupational health and safety service (N=202), a pension fund company (N=507), and a home-care institution (N=608); total N=1698."
  where: ["Netherlands"]
  when: "2001"
  n: 1698
  sector: ["insurance/finance", "occupational-health-services", "home-care/healthcare"]
  sample_notes: >
    Paper-and-pencil surveys distributed at work with return envelopes; response rates
    ranged from 47% (home-care, management-initiated survey) to 83% (pension fund). Sample 4
    (home care, 97% female, mostly part-time) diverged structurally from the other three
    samples, likely due to gender/work-hours composition rather than measurement non-
    invariance.
limitation:
  primary: "Cross-sectional design precludes causal inference despite the model being drawn with directional arrows; the authors explicitly call for longitudinal replication to test whether job demands/resources at Time 1 predict burnout/engagement at Time 2 and outcomes at Time 3."
  others:
    - "Relies exclusively on self-report measures for both predictors and outcomes, raising common-method-variance and negative-affectivity confound concerns (though the authors argue the literature suggests these are unlikely to fully account for observed relationships)."
    - "Structural relationships and factor loadings were not invariant across all four samples; Sample 4 (home care, nearly all-female, part-time workforce) diverged notably from the other three, limiting generalizability of exact parameter estimates."
    - "Only a narrow set of job demands (workload, emotional demands) and resources (feedback, social support, coaching) were measured, so it is untested whether other demand/resource types would replicate the pattern."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational JD-R model paper establishing that burnout and engagement are
  distinct constructs with separable predictors (demands drive burnout/health harm;
  resources drive engagement/retention), directly informing SNH's framework for
  distinguishing 'reduce isolation/overload' interventions from 'build social
  support/belonging' interventions as separate levers rather than one continuum, and
  supporting social support/coaching as resources specifically tied to engagement and
  turnover reduction.
tags:
  topic: ["burnout", "job-engagement", "wellbeing", "job-satisfaction"]
  method: ["survey", "cross-sectional", "structural-equation-modeling"]
  population: ["office-workers", "healthcare-workers", "finance-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/J Organ Behavior - 2004 - Schaufeli - Job demands  job resources  and their relationship with burnout and engagement  a/J Organ Behavior - 2004 - Schaufeli - Job demands  job resources  and their relationship with burnout and engagement  a.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/J Organ Behavior - 2004 - Schaufeli - Job demands  job resources  and their relationship with burnout and engagement  a.pdf"
  notes: null

---

id: "miyake-2021-job-stress-and-loneliness-among-remote"
title: "Job stress and loneliness among remote workers"
authors:
  - "Miyake, Fuyu"
  - "Odgerel, Chimed-Ochir"
  - "Hino, Ayako"
  - "Ikegami, Kazunori"
  - "Nagata, Tomohisa"
  - "Tateishi, Seiichiro"
  - "Tsuji, Mayumi"
  - "Matsuda, Shinya"
  - "Ishimaru, Tomohiro"
year: 2021
doi: "10.1101/2021.05.31.21258062"
venue: {type: "preprint", name: null, volume: null, issue: null, pages: null}
citation: "Miyake et al. (2021). Job stress and loneliness among remote workers.. https://doi.org/10.1101/2021.05.31.21258062"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This nationwide Japanese survey of 4,052 remote desk workers during the COVID-19 pandemic
  found that working remotely 4+ days per week was moderately associated with loneliness
  (AOR=1.60), while low co-worker support (AOR=4.06) and low supervisor support (AOR=2.49)
  were strongly associated with loneliness. High psychological job demands were also linked
  to loneliness (AOR=2.04), but decision latitude was not, suggesting that social support
  from colleagues matters more for preventing remote-work loneliness than the sheer amount
  of remote work or job control.
claims:
  - text: "Remote workers with low co-worker support had far greater odds of feeling lonely than those with high co-worker support (AOR=4.06, 95% CI 2.82-5.84, P<0.001), the strongest predictor in the model."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support"]
  - text: "Low supervisor support was also strongly associated with loneliness (AOR=2.49, 95% CI 1.79-3.47, P<0.001), though the association was weaker than for co-worker support."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support", "leadership-style"]
  - text: "Frequency of remote work (4+ days/week vs. 1 day/week) was moderately associated with loneliness (AOR=1.60, 95% CI 1.04-2.46, P=0.033), and high psychological job demands were associated with greater loneliness (AOR=2.04, 95% CI 1.39-2.99, P<0.001), while decision latitude showed no significant association."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["remote-work-intensity", "workload"]
population:
  who: "Full-time Japanese desk workers doing remote work during the COVID-19 pandemic, recruited from a larger nationwide internet survey (CORoNaWork Project)"
  where: ["Japan"]
  when: "December 2020"
  n: 4052
  sector: ["general-workforce"]
  sample_notes: >
    Subsample of 4,052 remote desk workers drawn from 27,036 eligible respondents (33,087
    originally sampled) via cluster sampling stratified by sex, job type, and region based
    on COVID-19 incidence data; online self-administered survey, so generalizability to non-
    internet users is limited; loneliness measured with a single UCLA Loneliness Scale item
    (yes/no), which is a coarse binary measure.
limitation:
  primary: "Cross-sectional design precludes causal inference; reverse causality (e.g., lonely workers avoiding remote work, or vice versa) cannot be ruled out, though authors argue employees had limited choice over telework frequency during the pandemic."
  others:
    - "Loneliness assessed via a single yes/no question rather than a validated multi-item scale, limiting measurement precision and only capturing presence/absence rather than severity."
    - "Internet-based sampling and voluntary participation raise generalizability concerns, and the pandemic context (state-of-emergency conditions, forced telework) may limit applicability to routine/non-crisis remote work."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantified, adjusted effect sizes showing that co-worker and supervisor support
  are far stronger predictors of remote-worker loneliness than remote-work frequency itself,
  directly informing SNH's prioritization of peer/manager support interventions over simply
  limiting remote-work days as a loneliness-prevention lever.
tags:
  topic: ["remote-work", "loneliness", "social-support", "isolation", "mental-health"]
  method: ["cross-sectional", "survey"]
  population: ["remote-workers", "japan", "desk-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Job Stress and Loneliness Among Remote Workers/Job Stress and Loneliness Among Remote Workers.md"
  pdf: "papers/Remote Workers/Job Stress and Loneliness Among Remote Workers.pdf"
  notes: null

---

id: "tesluk-1997-influences-of-organizational-culture-and-climate"
title: "Influences of Organizational Culture and Climate on Individual Creativity"
authors:
  - "TESLUK, PAUL E."
  - "FARR, JAMES L."
  - "KLEIN, STEPHANIE R."
year: 1997
doi: "10.1002/j.2162-6057.1997.tb00779.x"
venue: {type: "journal", name: "The Journal of Creative Behavior", volume: 31, issue: 1, pages: "27-41"}
citation: "TESLUK et al. (1997). Influences of Organizational Culture and Climate on Individual Creativity. The Journal of Creative Behavior, 31(1), 27-41. https://doi.org/10.1002/j.2162-6057.1997.tb00779.x"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  This paper presents an integrative conceptual framework distinguishing organizational
  culture (deep-seated beliefs and values) from climate (shared perceptions of policies and
  practices) and argues that both jointly shape individual creativity, with culture
  operating through socialization and climate operating through five perceived dimensions
  (goal emphasis, means emphasis, reward orientation, task support, socioemotional support)
  tied to specific HR practices. It draws on Nystrom's (1990) qualitative study of a Swedish
  chemical manufacturer to illustrate how divisional differences in risk-tolerance,
  leadership, and structure produce markedly different creative climates. The authors
  conclude that because culture is harder and slower to change than climate, sustained
  organizational creativity requires coordinated long-term culture-change strategies
  (visionary leadership, selective hiring/attrition, resocialization) alongside more
  immediately adjustable climate practices.
claims:
  - text: "Nystrom's (1990) qualitative case study of four divisions of a single Swedish chemical manufacturing firm found large differences in culture and climate for creativity tied to strategic orientation, structure, and leadership: the least innovative division emphasized profit/survival with little risk-taking, the most innovative division emphasized change, risk-taking, and competitiveness while deprioritizing quality/efficiency and customer orientation, and the second most creative division combined creativity with strong customer orientation and internal cooperation (incremental innovation)."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["performance", "collaboration"]
    predictors: ["organizational-culture", "leadership-style"]
  - text: "The proposed framework specifies climate for creativity as multidimensional, comprising five dimensions (goal emphasis, means emphasis, reward orientation, task support, socioemotional support) adapted from Kopelman et al. (1990), each mapped to concrete organizational practices such as mission statements, cross-functional teams, non-hierarchical evaluation of ideas, resource/training support, and risk-tolerant supervisory styles that avoid punishing well-intentioned failures."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["performance"]
    predictors: ["organizational-culture", "leadership-style", "psychological-safety"]
  - text: "The authors argue culture operates at a deeper, more abstract level than climate and is therefore slower and harder to intentionally change; because climate reflects aggregate perceptions of current practices it is comparatively more directly modifiable, while durable culture change requires longer-term strategies such as visionary leadership, selective attraction-selection-attrition of employees, and resocialization toward 'creative individualism.'"
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["performance"]
    predictors: ["organizational-culture", "leadership-style", "autonomy"]
population:
  who: "Conceptual/integrative review synthesizing organizational behavior literature on culture, climate, and individual creativity; its main illustrative empirical example is Nystrom's (1990) qualitative study of four divisions within one Swedish chemical manufacturing firm, alongside secondary case examples (a hospital system's response to a doctors' strike, and a frozen-foods company's founding story)."
  where: ["Sweden", "United States"]
  when: null
  n: null
  sector: ["manufacturing", "healthcare"]
  sample_notes: >
    This is a narrative/conceptual review, not an empirical study of a defined sample; it
    synthesizes prior theory and a small number of secondary case studies (notably Nystrom's
    1990 four-division case study) rather than collecting new data, so no formal sampling,
    response rate, or representativeness information applies.
limitation:
  primary: "The authors themselves state the model and its propositions are 'necessarily speculative at this time due to the relative lack of existing empirical research' directly testing organizational culture and climate effects on individual creativity."
  others:
    - "Relies heavily on a single small qualitative case study (four divisions of one firm) as its main empirical illustration, limiting generalizability."
    - "No original data collection, systematic review methodology, or effect-size reporting -- it is a narrative/conceptual synthesis rather than a systematic review."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Offers a transferable, operational framework for translating team culture into a concrete,
  multidimensional climate (goal emphasis, means emphasis, reward orientation, task support,
  socioemotional support) that SNH interventions could adapt as measurable levers --
  socioemotional support and tolerance for failure map onto psychological-safety and
  belonging mechanisms relevant to remote-worker and OSS-maintainer wellbeing, even though
  the paper's own focus is creativity rather than social connection per se.
tags:
  topic: ["psychological-safety", "collaboration", "productivity"]
  method: ["theory", "review-narrative"]
  population: ["general-workforce", "manufacturing"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Journal of Creative Behavior - 2011 - TESLUK - Influences of Organizational Culture and Climate on Individual Creativity/Journal of Creative Behavior - 2011 - TESLUK - Influences of Organizational Culture and Climate on Individual Creativity.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Journal of Creative Behavior - 2011 - TESLUK - Influences of Organizational Culture and Climate on Individual Creativity.pdf"
  notes: null

---

id: "kaplan-2010-users-of-the-world-unite-the"
title: "Users of the world, unite! The challenges and opportunities of Social Media"
authors:
  - "Kaplan, Andreas M."
  - "Haenlein, Michael"
year: 2010
doi: "10.1016/j.bushor.2009.09.003"
venue: {type: "journal", name: "Business Horizons", volume: 53, issue: 1, pages: "59-68"}
citation: "Kaplan et al. (2010). Users of the world, unite! The challenges and opportunities of Social Media. Business Horizons, 53(1), 59-68. https://doi.org/10.1016/j.bushor.2009.09.003"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  Kaplan and Haenlein define Social Media as internet applications built on Web 2.0 that
  enable user-generated content, and propose a classification scheme along two theoretical
  dimensions -- social presence/media richness and self-presentation/self-disclosure -- that
  sorts applications into six types: collaborative projects, blogs, content communities,
  social networking sites, virtual game worlds, and virtual social worlds. Drawing on
  corporate case examples (Dell, Starbucks, Nokia, Burger King), the article derives ten
  practical recommendations for organizations engaging with these platforms, organized
  around 'using media' and 'being social.' For the SNH project it offers a conceptual
  vocabulary for distinguishing how different online platforms vary in the intimacy,
  richness, and self-disclosure they afford -- directly relevant to choosing or designing
  tools meant to sustain remote-worker social connection.
claims:
  - text: "The authors classify six Social Media types along two theoretical axes: social presence/media richness (low to high: collaborative projects and blogs < content communities and social networking sites < virtual game and social worlds) and self-presentation/self-disclosure, arguing richer, more synchronous media produce greater social influence between communication partners."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["social-presence", "communication"]
    predictors: ["network-structure"]
  - text: "Illustrative corporate cases are used to argue Social Media adoption can generate measurable business value, e.g., Dell reported roughly $1 million in incremental revenue attributed to Twitter-based sales alerts, while Burger King's 'Whopper Sacrifice' Facebook campaign led over 20,000 users to delete 233,906 friends in exchange for free hamburgers before Facebook shut the app down over privacy concerns."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "community-engagement"]
  - text: "The article argues virtual social worlds (e.g., Second Life) uniquely allow unrestricted self-presentation because, unlike virtual game worlds governed by strict role rules, they impose no behavioral constraints beyond basic physical laws, and that with increased usage intensity residents' avatar behavior increasingly mirrors real-life behavior."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["social-presence"]
    predictors: ["embodiment"]
population:
  who: "No defined empirical sample; a conceptual/theory article illustrated with corporate case examples (e.g., Dell, Starbucks, Nokia, Burger King, IBM) and platform usage statistics drawn from industry reports (Forrester, Jupiter Research, Pew)."
  where: []
  when: null
  n: null
  sector: ["technology", "marketing", "cross-sector"]
  sample_notes: >
    Not a study of a population; examples are anecdotal corporate cases selected to
    illustrate the classification framework and advice, not systematically sampled or
    evaluated.
limitation:
  primary: "The article is a conceptual/opinion piece with no systematic data collection or empirical testing; its claims about business outcomes rest entirely on selectively chosen, uncorroborated anecdotal examples rather than controlled analysis."
  others:
    - "The classification framework (social presence x self-disclosure) is asserted rather than empirically validated against user data."
    - "Industry statistics (Forrester, Jupiter Research adoption/market-size figures) are cited without methodological detail, and some 2009-era figures (e.g., mobile market growth projections) are now outdated."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Its social-presence/self-disclosure classification of platform types gives the SNH project
  a conceptual vocabulary for reasoning about which kinds of social media or collaboration
  tools afford richer versus thinner connection, directly informing decisions about which
  channels to design or recommend for sustaining remote-worker social presence and
  belonging.
tags:
  topic: ["social-presence", "community-health", "collaboration", "remote-work", "measurement"]
  method: ["theory"]
  population: ["organizations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Kaplan & Haenlein (2010) - Users of the World, Unite! The Challenges and Opportunities of Social Media/Kaplan & Haenlein (2010) - Users of the World, Unite! The Challenges and Opportunities of Social Media.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Kaplan & Haenlein (2010) - Users of the World, Unite! The Challenges and Opportunities of Social Media.pdf"
  notes: null

---

id: "kazekami-2020-mechanisms-to-improve-labor-productivity-by"
title: "Mechanisms to improve labor productivity by performing telework"
authors:
  - "Kazekami, Sachiko"
year: 2020
doi: "10.1016/j.telpol.2019.101868"
venue: {type: "journal", name: "Telecommunications Policy", volume: 44, issue: 2, pages: "101868"}
citation: "Kazekami (2020). Mechanisms to improve labor productivity by performing telework. Telecommunications Policy, 44(2), 101868. https://doi.org/10.1016/j.telpol.2019.101868"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using two-wave panel data from the Japanese Panel Study of Employment Dynamics (2017-2018)
  and fixed-effect and difference-in-differences models, this study traces the mechanisms by
  which telework raises labor productivity in Japan. It finds an inverted-U relationship
  between weekly telework hours and productivity, shows that the productivity gain runs
  mainly through increased life satisfaction (not happiness or work satisfaction), and shows
  telework is most valuable for workers with long or crowded commutes, even though it also
  raises the stress of balancing work and domestic chores.
claims:
  - text: "For continuing teleworkers, each additional weekly telework hour raised labor productivity by about ¥160 (~US$1.48) per hour (β=0.0160, p<.05), but the squared telework-hours term was significantly negative (β=-0.000392, p<.05), indicating productivity gains reverse once telework hours become too high."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Telework significantly increased life satisfaction, happiness, and work satisfaction (order-logit coefficients on 1-5 dissatisfaction scales: life satisfaction β=-0.897***, work satisfaction β=-1.240***, happiness β=-0.839***), but only life satisfaction significantly fed through to raise labor productivity (β=-0.00464, p<.10); happiness and work satisfaction had no significant productivity effect."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "job-satisfaction", "wellbeing"]
    predictors: ["remote-work-intensity"]
  - text: "The productivity benefit of telework was concentrated among long or crowded commuters: telework hours significantly raised productivity for workers commuting more than 60 minutes (β=0.0184-0.0201, p<.01) and for those commuting by crowded train/bus (β=0.0249-0.0252, p<.01), but had no significant effect for workers with commutes under 60 minutes or who commuted by car, bicycle, or foot."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["remote-work-intensity"]
population:
  who: "Japanese regular employees aged under 60 from the Japanese Panel Study of Employment Dynamics; roughly 9,200 regular employees answered each year, with telework subsamples of 219 (started telework), 291 (continued telework), and 171 (stopped telework)"
  where: ["Japan"]
  when: "January 2017 and January 2018 (covering 2016-2017 employment)"
  n: 9200
  sector: ["general-workforce"]
  sample_notes: >
    Nationally representative online panel benchmarked to the Labor Force Survey for
    gender/age/employment-type/region distribution, but the teleworker subsamples analyzed
    in the productivity mechanism models are small (171-291 workers), and only regular (not
    non-regular) employees under 60 are included.
limitation:
  primary: "Telework subsamples are small (171-291 workers) and most teleworkers telework only a few hours per week, so the study cannot establish effects for full-time or high-frequency telework, and results for workers who start or stop telework are often statistically inconclusive."
  others:
    - "Fixed-effect and difference-in-differences designs reduce but do not eliminate self-selection into telework as an alternative explanation"
    - "The trivial-duties/interruption-avoidance mechanism produced counterintuitive, often insignificant results, weakening that part of the causal story"
    - "Findings are specific to Japan's telework norms, commuting patterns, and family-care policy context, limiting generalizability"
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, panel-data evidence that telework's productivity payoff is
  nonlinear (too many telework hours erode it) and operates through life satisfaction and
  commute-stress relief rather than through happiness or job discretion, which is directly
  useful for calibrating SNH guidance on remote-work intensity and for choosing which
  wellbeing measures (life satisfaction vs. happiness) actually track productivity outcomes.
tags:
  topic: ["remote-work", "productivity", "wellbeing", "work-life-balance"]
  method: ["longitudinal", "secondary-data"]
  population: ["japan", "office-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Kazekami (2020) - Mechanisms to Improve Labor Productivity by Performing Telework.pdf"
  notes: null

---

id: "koopmans-2012-development-of-an-individual-work-performance"
title: "Development of an individual work performance questionnaire"
authors:
  - "Koopmans, Linda"
  - "Bernaards, Claire"
  - "Hildebrandt, Vincent"
  - "van Buuren, Stef"
  - "van der Beek, Allard J."
  - "de Vet, Henrica C.W."
year: 2012
doi: "10.1108/17410401311285273"
venue: {type: "journal", name: "International Journal of Productivity and Performance Management", volume: 62, issue: 1, pages: "6-28"}
citation: "Koopmans et al. (2012). Development of an individual work performance questionnaire. International Journal of Productivity and Performance Management, 62(1), 6-28. https://doi.org/10.1108/17410401311285273"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This study develops and field-tests the Individual Work Performance Questionnaire (IWPQ),
  a generic self-report measure of task performance, contextual performance, adaptive
  performance, and counterproductive work behavior (CWB). Using factor analysis and Rasch
  analysis on a representative sample of 1,181 Dutch workers, the authors found that a
  three-dimensional structure (task, contextual, CWB) fit the data better than the original
  four-dimensional model, with adaptive performance collapsing into contextual performance.
  The result is a short, generic, psychometrically validated instrument for measuring
  individual work performance across occupational sectors, useful whenever an SNH study
  needs a validated outcome measure for performance rather than a bespoke one.
claims:
  - text: "Factor analysis did not support the hypothesized four-dimensional IWP framework; instead a generic three-dimensional structure (task performance, contextual performance, and counterproductive work behavior) was confirmed across blue, pink, and white collar occupational sectors, with adaptive performance items loading onto contextual performance rather than forming a separate dimension."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "productivity"]
    predictors: ["sampling-method"]
  - text: "Rasch analysis produced generic short scales with good model fit and acceptable reliability: person separation index (PSI) ranged from 0.78 (task performance, 4 items) to 0.85 (contextual performance) and 0.84 (CWB, 5 items) when tested at a sample size of 200, though item-trait chi-square statistics showed misfit at the full sample size of 1,181 due to statistical power."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "productivity"]
    predictors: ["sampling-method"]
  - text: "Differential item functioning (DIF) was detected between occupational sectors (e.g., 'result-oriented working' was harder for blue collar workers) and between genders (e.g., 'working efficiently' and a CWB item were easier for males), but DIF plots indicated these effects were of little practical relevance, supporting valid comparisons of IWPQ scores across sectors, gender, and age groups."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["sampling-method"]
population:
  who: "1,181 Dutch workers (49.5% female) recruited via an internet panel, spanning blue collar (n=368), pink collar (n=421), and white collar (n=392) occupational sectors, ages 18-65+"
  where: ["Netherlands"]
  when: "June 2011"
  n: 1181
  sector: ["mixed-occupations"]
  sample_notes: >
    Recruited through a paid internet panel (financial reward for participation), described
    as 'representative' of Dutch workers but self-selected into a panel; a separate
    54-person pilot sample (TNO/VU researchers, secretary, nurse, manager) was used for item
    refinement and think-aloud testing before the main field test.
limitation:
  primary: "The IWPQ is validated only against self-report; it has not been shown to generalize to managerial or peer ratings, which are known to correlate only weakly (r=0.19-0.44) with self-ratings and to show different factor structures due to leniency and halo effects."
  others:
    - "Most respondents scored near the ceiling on task performance and near the floor on CWB items, indicating the scale lacks enough difficult items to discriminate among high performers or detect change at the high end of the range."
    - "Item-trait chi-square fit statistics were significant (indicating misfit) at the full sample size of 1,181 and only became non-significant when the sample was artificially reduced to 200, raising questions about how much of the 'good fit' claim depends on this adjustment."
    - "Cross-sectional design with no test of predictive or discriminant validity against external criteria; construct validity and sensitivity to change are flagged by the authors as needing future research."
risk_of_bias: "low"
relevance_to_project: >
  Provides a short, generic, psychometrically validated self-report instrument (IWPQ) for
  individual work performance that SNH studies could adopt as an outcome measure when
  testing whether isolation, remote-work intensity, or social support interventions affect
  task performance, contextual performance, or counterproductive work behavior, instead of
  building an ad hoc performance scale.
tags:
  topic: ["measurement", "productivity", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Koopmans et al. (2013) - Development of an Individual Work Performance Questionnaire/Koopmans et al. (2013) - Development of an Individual Work Performance Questionnaire.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Koopmans et al. (2013) - Development of an Individual Work Performance Questionnaire.pdf"
  notes: null

---

id: "kossek-2012-worknonwork-boundary-management-profiles-a-person"
title: "Work–nonwork boundary management profiles: A person-centered approach"
authors:
  - "Kossek, Ellen Ernst"
  - "Ruderman, Marian N."
  - "Braddy, Phillip W."
  - "Hannum, Kelly M."
year: 2012
doi: "10.1016/j.jvb.2012.04.003"
venue: {type: "journal", name: "Journal of Vocational Behavior", volume: 81, issue: 1, pages: "112-128"}
citation: "Kossek et al. (2012). Work–nonwork boundary management profiles: A person-centered approach. Journal of Vocational Behavior, 81(1), 112-128. https://doi.org/10.1016/j.jvb.2012.04.003"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using two samples of managers (N=278, N=313), the authors validate a new multi-scale
  measure of work-nonwork boundary management (cross-role interruption behaviors in both
  directions, work and family identity centrality, and perceived boundary control) via
  confirmatory factor analysis, then use K-means cluster analysis on the combined sample to
  identify six boundary-management profiles. Profiles with low perceived boundary control
  (Work Warriors, Overwhelmed Reactors) had consistently worse work-family outcomes than
  high-control profiles (Family Guardians, Fusion Lovers, Dividers, Nonwork Eclectics),
  regardless of whether individuals were integrators or segmenters. The paper's central
  contribution is that feeling in control of boundary crossings matters more for wellbeing
  than the direction or amount of work-nonwork blending itself.
claims:
  - text: "K-means cluster analysis on the combined sample (N=591) identified six distinct boundary-management profiles differentiated by symmetry/direction of cross-role interruption behaviors, work vs. family identity centrality, and perceived boundary control (e.g., Work Warriors, Overwhelmed Reactors, Family Guardians, Fusion Lovers, Dividers, Nonwork Eclectics), partially replicating and extending prior qualitative typologies."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["boundary-management", "autonomy"]
  - text: "The two low-boundary-control clusters (Work Warriors, Overwhelmed Reactors) scored significantly worse than high-control clusters on nearly every outcome: highest work-family conflict (F=41.52, p<.001, eta-squared=.26), lowest work-schedule fit (F=34.48, eta-squared=.23), highest psychological distress (F=13.11, eta-squared=.10), lowest time adequacy (F=26.33, eta-squared=.18), and higher intention to turnover (F=8.57, eta-squared=.07) than the Dividers cluster."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "stress", "work-life-balance", "job-satisfaction"]
    predictors: ["autonomy", "boundary-management"]
  - text: "Perceived boundary control was the single strongest and most consistent criterion-related predictor among the five validated scales, negatively correlated with intention to turnover (r=-.21 to -.28, p<.01) and psychological distress (r=-.22 to -.41, p<.01), and positively correlated with work-schedule fit (r=.50-.51, p<.01) and time adequacy (r=.45-.48, p<.01) across both samples."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "stress", "work-life-balance"]
    predictors: ["autonomy", "boundary-management"]
population:
  who: "Practicing managers and professionals (mostly upper-middle to executive level) attending leadership development courses at a U.S. management education center, in two separate samples used for scale development and cross-validation."
  where: ["United States"]
  when: null
  n: 591
  sector: ["corporate", "management"]
  sample_notes: >
    Convenience samples of managers self-selected into leadership training (sample 1 n=278,
    sample 2 n=313, collected several months apart); predominantly Caucasian (75-82%),
    married (72-78%), and employed by large multinational corporations, limiting
    generalizability to non-managerial workers, smaller/family firms, hourly employees, or
    non-U.S. contexts.
limitation:
  primary: "Cross-sectional design across both samples precludes causal inference between boundary-management characteristics and work-family outcomes; all relationships are correlational."
  others:
    - "Sample restricted to U.S. managers/professionals in large multinational corporations recruited from leadership-training programs, not representative of hourly workers, entrepreneurs, small/family firms, or non-U.S. populations."
    - "All measures are self-report, raising (though partially mitigated) common-method-bias concerns; no data from spouses, supervisors, or performance records."
    - "The cross-sectional design could not detect the 'volleying' (alternating integrator/separator) style found in prior qualitative work, since capturing style-switching requires longitudinal or experience-sampling data."
risk_of_bias: "medium"
relevance_to_project: >
  Introduces and validates the Work-Life Indicator, a measurable construct of 'perceived
  boundary control' distinct from integration/segmentation preference, and shows via a six-
  profile typology that control over work-nonwork boundary crossings (not the amount or
  direction of blending) is what predicts lower distress, turnover intention, and conflict —
  directly relevant to designing remote-work boundary-management interventions and to
  selecting or adapting a measure of boundary control for SNH studies of hybrid/remote
  workers.
tags:
  topic: ["work-life-balance", "remote-work", "burnout", "measurement", "methodology"]
  method: ["cross-sectional", "survey"]
  population: ["managers", "corporate-employees"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Kossek et al. (2012) - Work-Nonwork Boundary Management Profiles - A Person-Centered Approach/Kossek et al. (2012) - Work-Nonwork Boundary Management Profiles - A Person-Centered Approach.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Kossek et al. (2012) - Work-Nonwork Boundary Management Profiles - A Person-Centered Approach.pdf"
  notes: null

---

id: "leigh-2017-an-overview-of-systematic-reviews-on"
title: "An overview of systematic reviews on the public health consequences of social isolation and loneliness"
authors:
  - "Leigh-Hunt, N."
  - "Bagguley, D."
  - "Bash, K."
  - "Turner, V."
  - "Turnbull, S."
  - "Valtorta, N."
  - "Caan, W."
year: 2017
doi: "10.1016/j.puhe.2017.07.035"
venue: {type: "journal", name: "Public Health", volume: 152, issue: null, pages: "157-171"}
citation: "Leigh-Hunt et al. (2017). An overview of systematic reviews on the public health consequences of social isolation and loneliness. Public Health, 152, 157-171. https://doi.org/10.1016/j.puhe.2017.07.035"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This systematic overview of reviews (a review of reviews) synthesizes 40 systematic
  reviews and 3 meta-syntheses on the public health consequences of social isolation and
  loneliness, assessed for quality with AMSTAR and GRADE. It finds strong, consistent
  evidence linking both social isolation and loneliness to increased all-cause mortality,
  and social isolation specifically to cardiovascular disease and depression, while evidence
  for other physical health outcomes, health behaviours, and socio-economic consequences is
  sparse or low quality. It also catalogues 62 different self-report instruments used across
  the field, highlighting a major measurement-fragmentation problem for anyone trying to
  compare or pool isolation/loneliness studies.
claims:
  - text: "Two meta-analyses of cohort studies found social isolation associated with increased all-cause mortality (OR 1.29, 95% CI 1.06-1.56) and loneliness similarly associated (OR 1.26, 95% CI 1.04-1.53), with living alone at OR 1.32 (95% CI 1.14-1.53); the similarity between loneliness and isolation odds ratios suggests no clear difference between subjective and objective measures for this outcome."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["mental-health"]
    predictors: ["isolation", "loneliness"]
  - text: "The evidence base was strongest for cardiovascular disease: a meta-analysis found an increased relative risk of 1.5 (95% CI 1.2-1.9) for high social isolation, and reviews found stronger social relationships associated with a 50% increased likelihood of survival after myocardial infarction, with the highest-isolation individuals having two to three times the risk of post-MI mortality."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["wellbeing"]
    predictors: ["isolation", "social-support"]
  - text: "For mental health, large and diverse social networks with high-quality relationships protected against depression (including post-stroke depression), low sense of belonging was associated with higher risk of suicidal ideation and attempts, and loneliness/low social participation were associated with increased dementia incidence in two longitudinal-study reviews; evidence for physical health conditions beyond cardiovascular disease (cancer, health behaviours, COPD) was comparatively weak and inconsistent."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["depression", "suicidal-ideation", "mental-health"]
    predictors: ["isolation", "loneliness", "sense-of-belonging", "social-support"]
population:
  who: "40 systematic reviews (10 with meta-analysis) plus 3 meta-syntheses of observational studies on social isolation and loneliness, spanning ages from adolescents to older adults across general and clinical populations"
  where: ["mostly developed-world countries (UK, USA, Canada, Australia, Netherlands, and others); one review from outside the developed world"]
  when: "included reviews published 2000-2015; database search covered 1950-2016"
  n: 90
  sector: ["public-health", "healthcare"]
  sample_notes: >
    90 papers screened (40 systematic reviews, 47 non-systematic reviews, 3 meta-syntheses)
    from 8 databases; primary systematic reviews sourced mostly single-country (8 multi-
    country), age range unreported in 12 reviews, gender proportions unreported in 22
    reviews; most systematic reviews were AMSTAR-rated low-to-moderate quality, with GRADE
    evidence quality also mostly low-to-moderate; 62 different, largely non-standardized
    self-report measurement scales were used across included reviews, limiting
    comparability.
limitation:
  primary: "Underlying studies are almost entirely observational with few longitudinal designs, so causality between social isolation/loneliness and health outcomes cannot be established despite strong associations."
  others:
    - "Restricted to English-language reviews from mostly developed countries, limiting generalizability elsewhere."
    - "No reviews addressed health-economic or wider socio-economic consequences, or developmental/educational outcomes in children."
    - "Extreme heterogeneity in measurement (62 different self-report scales) across included reviews undermines direct comparison of effect sizes."
risk_of_bias: "medium"
relevance_to_project: >
  Provides the strongest available systematic evidence base for treating social isolation
  and loneliness as upstream population-health risk factors (mortality, cardiovascular
  disease, depression, suicidal ideation) that the SNH project can cite when justifying
  prevention/intervention framing for remote-worker isolation; its catalogue of 62 disparate
  loneliness/isolation measurement instruments is directly useful for choosing or critiquing
  SNH's own measurement approach.
tags:
  topic: ["isolation", "loneliness", "mental-health", "suicide-prevention", "measurement"]
  method: ["review-systematic", "secondary-data"]
  population: ["general-population", "older-adults", "adolescents"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Leigh-Hunt et al. (2017) - An Overview of Systematic Reviews on the Public Health Consequences of Social Isolation and Loneliness/Leigh-Hunt et al. (2017) - An Overview of Systematic Reviews on the Public Health Consequences of Social Isolation and Loneliness.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Leigh-Hunt et al. (2017) - An Overview of Systematic Reviews on the Public Health Consequences of Social Isolation and Loneliness.pdf"
  notes: null

---

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

---

id: "walz-2024-lonely-work-home-the-impact-of"
title: "Lonely@Work@Home? The impact of work/home demands and support on workplace loneliness during remote work"
authors:
  - "Walz, Timo"
  - "Kensbock, Julia M."
  - "de Jong, Simon B."
  - "Kunze, Florian"
year: 2024
doi: "10.1016/j.emj.2023.05.001"
venue: {type: "journal", name: "European Management Journal", volume: 42, issue: 5, pages: "767-778"}
citation: "Walz et al. (2024). Lonely@Work@Home? The impact of work/home demands and support on workplace loneliness during remote work. European Management Journal, 42(5), 767-778. https://doi.org/10.1016/j.emj.2023.05.001"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A two-wave survey of 232 German remote-working employees during the COVID-19 pandemic
  finds that job demands increase workplace loneliness indirectly through work-to-home
  interference, and home demands increase workplace loneliness indirectly through home-to-
  work interference. Job support buffers the job-demands pathway (weaker indirect effect at
  high job support), but home support does not significantly buffer the home-demands
  pathway, though follow-up analyses suggest job support can also alleviate loneliness
  stemming from home demands. The study integrates JD-R theory, conservation-of-resources
  theory, and social exchange theory to explain workplace loneliness as arising from
  resource depletion that limits employees' capacity to invest in social exchange
  relationships at work.
claims:
  - text: "Job demands were positively associated with work-to-home interference (B=.49, p<.001), and work-to-home interference was positively associated with workplace loneliness (B=.25, p<.001); the indirect effect of job demands on workplace loneliness via work-to-home interference was significant (effect=.12, 95% CI [0.05, .20]), while the direct effect was not significant."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "isolation"]
    predictors: ["workload", "boundary-management"]
  - text: "Home demands were positively associated with home-to-work interference (B=.32, p<.001), which was positively associated with workplace loneliness (B=.16, p<.05); the indirect effect was significant (effect=.05, 95% CI [0.01, .10])."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "isolation"]
    predictors: ["workload", "boundary-management"]
  - text: "Job support significantly moderated the indirect job-demands-to-loneliness pathway via work-to-home interference (interaction B=-.20, p<.05; index of moderated mediation=-0.05, 95% CI [-0.10, -0.01]), with a stronger indirect effect at low job support (B=.15) than high job support (B=.08); home support did not significantly moderate the home-demands pathway (interaction B=.03, n.s.)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support", "boundary-management"]
population:
  who: "German white-collar remote-working employees recruited via the respondi panel across sectors including banking, logistics, and telecommunications"
  where: ["Germany"]
  when: "May 2020 (two waves, one week apart, during the COVID-19 pandemic)"
  n: 232
  sector: ["mixed", "banking", "logistics", "telecommunications"]
  sample_notes: >
    964 panel members invited; wave 1 n=337 valid responses (response rate 34.96%); wave 2
    retention n=245 (72.70%); 13 excluded for missing data, final analytic n=232. Only
    employees spending >=50% of time working from home included. Average age 43.07, 46.46%
    women, average 89.23% of time spent working from home.
limitation:
  primary: "Although demand and loneliness measures were temporally split across two waves to reduce common-method bias, the one-week lag is short and reverse causality (loneliness increasing perceived demands) cannot be fully ruled out despite robustness checks against reverse mediation."
  others:
    - "Single-country (Germany), pandemic-era convenience panel sample recruited via a commercial survey service, limiting generalizability to other cultural or non-crisis remote-work contexts."
    - "Energy-depletion mechanisms (time-, strain-, and behavior-based interference) were measured only indirectly via aggregate interference scales, not decomposed into their specific sub-processes."
    - "Data are not publicly available, limiting independent verification of the reported effects."
risk_of_bias: "low"
relevance_to_project: >
  Provides a validated causal pathway (job/home demands -> work-home interference ->
  workplace loneliness) with effect sizes directly relevant to designing SNH interventions
  for remote workers, and empirically shows that job-side social support (not home-side
  support) is the more effective lever for buffering loneliness arising from both work and
  home demands, informing where the project should target support interventions.
tags:
  topic: ["remote-work", "loneliness", "work-life-balance", "social-support", "isolation"]
  method: ["survey", "longitudinal", "quantitative"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Lonely at Work at Home - Impact of Work Home Demands and Support on Workplace Loneliness During Remote Work/Lonely at Work at Home - Impact of Work Home Demands and Support on Workplace Loneliness During Remote Work.md"
  pdf: "papers/Remote Workers/Lonely at Work at Home - Impact of Work Home Demands and Support on Workplace Loneliness During Remote Work.pdf"
  notes: null

---

id: "malone-1994-the-interdisciplinary-study-of-coordination"
title: "The interdisciplinary study of coordination"
authors:
  - "Malone, Thomas W."
  - "Crowston, Kevin"
year: 1994
doi: "10.1145/174666.174668"
venue: {type: "journal", name: "ACM Computing Surveys", volume: 26, issue: 1, pages: "87-119"}
citation: "Malone et al. (1994). The interdisciplinary study of coordination. ACM Computing Surveys, 26(1), 87-119. https://doi.org/10.1145/174666.174668"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Malone and Crowston synthesize computer science, economics, organization theory, and
  biology into a unified 'coordination theory,' defining coordination as the process of
  managing dependencies among activities and cataloguing generic dependency types (shared
  resources, producer/consumer, simultaneity, task/subtask) alongside the coordination
  processes used to manage each. Drawing on formal models and case examples, the survey
  argues that information technology's main effect is to lower coordination costs, which can
  substitute for existing coordination, increase the total amount of coordination performed,
  or enable entirely new 'coordination-intensive' organizational structures such as
  adhocracies and smaller, more market-mediated firms. It also surfaces the 'discretionary
  database' incentive problem in cooperative-work tools, where individual users benefit from
  viewing shared information without needing to contribute it, illustrated by a consulting
  firm's underused Lotus Notes deployment.
claims:
  - text: "Formal queuing-theory models of alternative task-assignment mechanisms (Malone & Smith) showed a three-way tradeoff: centralized schemes had the lowest coordination costs but were most vulnerable to processor/actor failure; decentralized markets were least vulnerable to failure but had high coordination costs; decentralized 'product hierarchies' had low coordination costs but incurred high production costs from unused capacity."
    evidence: "modelling"
    support_strength: "moderate"
    outcomes: ["productivity", "collaboration"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "Citing econometric analysis of the U.S. economy from 1975-1985 (Brynjolfsson et al. 1994), the authors report that greater use of information technology is correlated with decreases in both firm size and vertical integration; as an illustrative case, the share of airline reservations booked through travel agents (versus calling airlines directly) rose from 35% to 70% after computerized reservation systems were introduced."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["productivity"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "Cooperative-work tools built around 'discretionary databases' (e.g., shared calendars, Lotus Notes) create a free-rider equilibrium: users can obtain full benefit from viewing shared information without contributing to it, so rational individual incentives can drive contribution toward zero; a case study of a large consulting firm (Orlikowski 1992) found employees rewarded for being the individual 'expert' were reluctant to post their knowledge into a shared database that would erode that status."
    evidence: "case-study"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration", "help-seeking"]
    predictors: ["organizational-culture", "psychological-safety"]
population:
  who: "Not an original empirical sample: a narrative synthesis across computer science, economics, organization theory, and biology literature, illustrated with cited empirical studies such as Danziger et al.'s survey of computerization decisions in 42 U.S. local governments and Orlikowski's case study of a consulting firm's groupware deployment."
  where: ["USA"]
  when: "Literature synthesized spans roughly 1950s-1994; illustrative cited empirical studies date from 1975-1992"
  n: null
  sector: ["technology", "corporate", "government"]
  sample_notes: >
    As a theoretical survey (ACM Computing Surveys, 1994), the paper has no independent
    sample of its own; any n's, response rates, or representativeness belong to the
    individual cited primary studies (e.g., Malone & Smith's formal models, Danziger et
    al.'s 42-government dataset) and are not independently verifiable from this document.
limitation:
  primary: "As a 1994 theoretical synthesis, its predictions about IT's organizational effects (smaller firms, more markets, adhocracies) are speculative extrapolations from early formal models and small case examples that predate cloud computing, social media, distributed version control, and modern remote/open-source tooling, limiting direct applicability to today's virtual work contexts."
  others:
    - "Relies heavily on selective anecdotes and single-organization case examples (e.g., one consulting firm's Lotus Notes use) rather than a systematic empirical review."
    - "No explicit literature-search or study-selection methodology is described, so coverage of each contributing discipline may be uneven or biased toward the authors' own prior work (frequently self-cited)."
risk_of_bias: "medium"
relevance_to_project: >
  Establishes the foundational 'coordination theory' vocabulary (managing dependencies via
  shared-resource, producer/consumer, simultaneity, and task/subtask processes) that later
  open-source and distributed-work research builds on, and its analysis of the
  'discretionary database' free-rider problem in cooperative-work tools directly foreshadows
  the incentive and psychological-safety challenges the SNH project faces in designing tools
  that encourage remote workers and OSS contributors to share knowledge rather than free-
  ride on others' contributions.
tags:
  topic: ["collaboration", "remote-work", "open-source", "methodology"]
  method: ["theory", "secondary-data"]
  population: ["organizations", "distributed-teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Malone & Crowston (1994) - The Interdisciplinary Study of Coordination.pdf"
  notes: null

---

id: "perrigino-2020-managing-remote-workers-during-quarantine-insights"
title: "Managing remote workers during quarantine: Insights from organizational research on boundary management"
authors:
  - "Perrigino, Matthew B."
  - "Raveendhran, Roshni"
year: 2020
doi: "10.1177/237946152000600211"
venue: {type: "journal", name: "Behavioral Science &amp; Policy", volume: 6, issue: 2, pages: "87-94"}
citation: "Perrigino et al. (2020). Managing remote workers during quarantine: Insights from organizational research on boundary management. Behavioral Science &amp; Policy, 6(2), 87-94. https://doi.org/10.1177/237946152000600211"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "low", preregistered: false}
gist: >
  This evidence-based management commentary synthesizes organizational research on work-home
  boundary management into an actionable 'assess-create-support' framework for managers of
  employees forced to work from home during the COVID-19 quarantine. It distinguishes
  'separator' and 'integrator' boundary preferences and translates prior empirical findings
  (on breaks, after-hours communication, and supervisor role-modeling) into concrete
  managerial actions intended to protect remote workers' well-being and performance rather
  than generating new data.
claims:
  - text: "Prior research cited in the article shows job performance worsens, job satisfaction decreases, and family-related problems increase when employees struggle to manage boundaries between work and home roles."
    evidence: "theory"
    support_strength: "low"
    outcomes: ["job-satisfaction", "performance", "work-life-balance"]
    predictors: ["boundary-management"]
  - text: "During the pandemic shift to forced work-from-home, employees were reported to be working up to three hours longer each day, with days blurring together and weekend time increasingly consumed by work and family obligations."
    evidence: "theory"
    support_strength: "low"
    outcomes: ["work-life-balance", "burnout"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Citing prior studies, the article argues responding to or sending late-night work communications leads to feelings of depletion and impaired next-day engagement, and that informal managerial support is more influential than formal organizational work-life policies in helping employees maintain work-life balance."
    evidence: "theory"
    support_strength: "low"
    outcomes: ["job-engagement", "work-life-balance"]
    predictors: ["leadership-style", "boundary-management"]
population:
  who: "Not an empirical study; the target audience is managers and organizational leaders of employees suddenly working from home due to COVID-19 quarantine, with recommendations synthesized from ~55 cited organizational-behavior studies."
  where: []
  when: null
  n: null
  sector: ["general-workforce"]
  sample_notes: >
    No original sample; this is a practitioner-facing synthesis/framework article drawing on
    prior published research (references 1-55), published in Behavioral Science & Policy's
    COVID-19 issue in 2020.
limitation:
  primary: "The article presents no new empirical data or original analysis; all claims are secondhand syntheses of cited studies, several of which are news articles or blog posts rather than peer-reviewed research."
  others:
    - "Recommendations are framed as universally applicable managerial actions without testing their effectiveness in the COVID-19 remote-work context specifically."
    - "The separator/integrator boundary-preference framework is asserted rather than validated within this piece."
risk_of_bias: "high"
relevance_to_project: >
  Offers a concrete, citable framework (assess-create-support) and specific mechanisms --
  after-hours communication norms, synchronous vs. asynchronous tool choice, manager role-
  modeling, and separator/integrator boundary preferences -- that the SNH project can draw
  on when designing interventions or manager guidance to reduce remote-worker isolation and
  burnout.
tags:
  topic: ["remote-work", "work-life-balance", "burnout", "wellbeing"]
  method: ["theory"]
  population: ["remote-workers", "managers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Managing Remote Workers During Quarantine - Insights from Organizational Research on Boundary Management/Managing Remote Workers During Quarantine - Insights from Organizational Research on Boundary Management.md"
  pdf: "papers/Remote Workers/Managing Remote Workers During Quarantine - Insights from Organizational Research on Boundary Management.pdf"
  notes: null

---

id: "edwards-2000-mechanisms-linking-work-and-family-clarifying"
title: "Mechanisms Linking Work and Family: Clarifying the Relationship between Work and Family Constructs"
authors:
  - "Edwards, Jeffrey R."
  - "Rothbard, Nancy P."
year: 2000
doi: "10.2307/259269"
venue: {type: "journal", name: "The Academy of Management Review", volume: 25, issue: 1, pages: "178"}
citation: "Edwards et al. (2000). Mechanisms Linking Work and Family: Clarifying the Relationship between Work and Family Constructs. The Academy of Management Review, 25(1), 178. https://doi.org/10.2307/259269"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This 2000 Academy of Management Review theory paper argues that the six commonly cited
  work-family linking mechanisms (spillover, compensation, segmentation, resource drain,
  congruence, work-family conflict) have been described in vague, metaphoric terms that
  block rigorous empirical testing. Edwards and Rothbard respecify each mechanism as a
  causal relationship between specific work and family constructs, cross-classified by the
  sign (positive/negative/null), causal structure (direct/indirect/spurious), and
  intentionality of the relationship. The resulting framework exposes gaps in the existing
  literature (e.g., no prior mechanism describes a negative spurious relationship) and
  offers theoretical building blocks for constructing more complete causal models of the
  work-family interface, illustrated with an integrated model combining mood spillover,
  compensation, and segmentation.
claims:
  - text: "Spillover is respecified as a positive relationship between a work construct and a corresponding family construct (mood, values, skills, or behavior); it is typically unintentional when it operates through cognitive/motivational processes (e.g., mood spillover, behavior embedded as habits) but becomes intentional when people deliberately manage expressed mood, transfer skills, or apply behaviors to meet role expectations in both domains."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["boundary-management"]
  - text: "Compensation is specified as a negative, direct, intentional relationship: decreased satisfaction or rewards in one domain (work or family) prompts the person to actively reallocate involvement (time, attention, importance) or pursue rewards in the other domain, distinguishing 'supplemental' compensation (offsetting insufficient rewards) from 'reactive' compensation (offsetting excess negative experiences)."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["work-life-balance"]
    predictors: ["boundary-management", "autonomy"]
  - text: "Cross-classifying six linking mechanisms by sign x causal structure x intent (Table 1) shows that segmentation and resource drain are intentional buffering/direct-transfer processes while strain-based and behavior-based conflict are largely unintentional, and reveals theoretically 'empty cells' in the literature (e.g., no described negative spurious relationship, such as one arising from traditional gender-role socialization) that point to unexamined work-family linkages."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["work-life-balance"]
    predictors: ["boundary-management", "sense-of-belonging"]
population:
  who: "N/A - theoretical/conceptual article; no empirical sample, it synthesizes and respecifies existing work-family research at the individual level of analysis"
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No primary data collected. The article is a conceptual respecification of prior work-
    family literature (individual-level focus only; couple, family-system, organizational,
    and cultural levels are explicitly excluded from scope).
limitation:
  primary: "Purely theoretical: the respecified linking mechanisms (sign, causal structure, intent) are illustrative propositions the authors did not empirically test, so their validity as depicted causal models awaits future empirical verification."
  others:
    - "Restricted to the individual level of analysis, excluding dual-earner-couple, family-system, organizational, and cultural-level dynamics of the work-family interface."
    - "Emphasizes psychological/intent-based mechanisms, giving limited attention to social, organizational, and societal forces (e.g., workplace policy, cultural norms) that also shape work-family linkages."
    - "Figures are illustrative simplifications (e.g., only unidirectional work-to-family causal flow shown per figure) that the authors note can be reversed or elaborated, meaning the published models are not comprehensive."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Provides a causal taxonomy (spillover vs. compensation vs. segmentation vs. resource drain
  vs. conflict, each with sign/structure/intent) that the SNH project can use to sharpen how
  it operationalizes work-life-balance and boundary-management constructs in remote-worker
  surveys and interventions, rather than treating 'work-family interference' as a single
  undifferentiated predictor.
tags:
  topic: ["work-life-balance", "remote-work", "methodology", "measurement"]
  method: ["theory"]
  population: ["working-adults"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Mechanisms Linking Work and Family_ Clarifying the Relationship between Work and Family Constructs/Mechanisms Linking Work and Family_ Clarifying the Relationship between Work and Family Constructs.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Mechanisms Linking Work and Family_ Clarifying the Relationship between Work and Family Constructs.pdf"
  notes: null

---

id: "dennis-2008-media-tasks-and-communication-processes-a"
title: "Media, Tasks, and Communication Processes: A Theory of Media Synchronicity1"
authors:
  - "Dennis, Alan R."
  - "Fuller, Robert M."
  - "Valacich, Joseph S."
year: 2008
doi: "10.2307/25148857"
venue: {type: "journal", name: "MIS Quarterly", volume: 32, issue: 3, pages: "575-600"}
citation: "Dennis et al. (2008). Media, Tasks, and Communication Processes: A Theory of Media Synchronicity1. MIS Quarterly, 32(3), 575-600. https://doi.org/10.2307/25148857"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Dennis, Fuller, and Valacich revise and formalize media synchronicity theory (MST),
  arguing that communication performance hinges on matching media capabilities to two
  underlying communication processes -- conveyance (transmitting diverse new information)
  and convergence (agreeing on shared meaning) -- rather than to task type as media richness
  theory assumed. They identify five media capabilities (transmission velocity, parallelism,
  symbol sets, rehearsability, reprocessability) that jointly determine a medium's capacity
  to support synchronicity, propose that convergence benefits from high-synchronicity media
  while conveyance benefits from low-synchronicity media, and show that this finer-grained
  lens resolves several null or reversed findings from prior media-richness experiments. The
  theory also predicts that as individuals become more familiar with each other, the task,
  and the medium, their need for high-synchronicity media declines over time.
claims:
  - text: "Reinterpreting six prior media-richness experiments (Rice and Shook 1990; Kinney and Watson 1992; Markus 1994; Dennis and Kinney 1998; Burke and Chidambaram 1999; Mennecke et al. 2000) through MST's five media capabilities explains results media richness theory could not, e.g., higher-level managers successfully using 'lean' e-mail for equivocal tasks, and distributed teams using synchronous electronic media outperforming face-to-face teams on a complex task."
    evidence: "theory"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration", "performance"]
    predictors: ["media-synchronicity"]
  - text: "Core proposition (P1a/b): communication performance improves when convergence processes (reaching shared meaning) use higher-synchronicity media and when conveyance processes (transmitting large volumes of new information) use lower-synchronicity media, implying that using several media in combination outperforms relying on one 'rich' medium for an entire task."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["collaboration", "performance"]
    predictors: ["media-synchronicity"]
  - text: "Familiarity with the task, media, and collaborators reduces the need for high-synchronicity media over time (P7): novel, unfamiliar teams need more convergence and thus more high-synchronicity media, while familiar teams with shared mental models can perform as well or better with lower-synchronicity media -- consistent with Fuller and Dennis's finding that high-synchronicity media aided decision-making performance only for novel, not familiar, tasks."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["collaboration", "performance"]
    predictors: ["media-synchronicity", "team-cohesion"]
population:
  who: "No new human sample was collected; the paper is a theoretical synthesis that reinterprets findings from prior lab and field studies of dyads, small groups, and managers communicating via computer-mediated and traditional media."
  where: ["United States"]
  when: null
  n: null
  sector: ["technology", "academic"]
  sample_notes: >
    Theoretical/conceptual paper with no primary data collection of its own. Its claims are
    grounded in reinterpretation of previously published experiments and field studies
    (predominantly lab studies with student subjects and some organizational field studies
    of managers), not in a defined sampled population.
limitation:
  primary: "The revised theory (propositions P1-P7) has not itself been empirically tested in complete form -- the authors note that none of the ~30-70 studies citing the original 1999 version tested the full theory, and this 2008 revision is validated only by post-hoc reinterpretation of studies designed to test a different theory (media richness theory), not by new confirmatory data."
  others:
    - "Explicit boundary conditions exclude deceptive communication and situations where some participants intend to manipulate rather than jointly build genuine shared understanding."
    - "The reinterpretation of prior studies in Table 3 is retrospective and selective ('a sample of studies'), which creates risk of confirmation bias in how well MST is shown to fit past results."
risk_of_bias: "not-applicable"
relevance_to_project: >
  For the SNH project's design of remote/hybrid work communication tools, this theory gives
  a principled basis for choosing and combining media (chat, video, async docs) depending on
  whether the goal is conveying information or converging on shared understanding, and
  predicts that mismatched media-synchronicity choices (e.g., all-async tools for tasks
  needing convergence) can degrade communication performance and, by extension, team
  cohesion and collaboration in distributed teams.
tags:
  topic: ["remote-work", "collaboration", "social-presence", "methodology"]
  method: ["theory", "analytical"]
  population: ["organizational-teams", "students"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Media, Tasks, and Communication Processes_ A Theory of Media Synchronicity/Media, Tasks, and Communication Processes_ A Theory of Media Synchronicity.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Media, Tasks, and Communication Processes_ A Theory of Media Synchronicity.pdf"
  notes: null

---

id: "malinowski-2015-mindfulness-at-work-positive-affect-hope"
title: "Mindfulness at Work: Positive Affect, Hope, and Optimism Mediate the Relationship Between Dispositional Mindfulness, Work Engagement, and Well-Being"
authors:
  - "Malinowski, Peter"
  - "Lim, Hui Jia"
year: 2015
doi: "10.1007/s12671-015-0388-5"
venue: {type: "journal", name: "Mindfulness", volume: 6, issue: 6, pages: "1250-1262"}
citation: "Malinowski et al. (2015). Mindfulness at Work: Positive Affect, Hope, and Optimism Mediate the Relationship Between Dispositional Mindfulness, Work Engagement, and Well-Being. Mindfulness, 6(6), 1250-1262. https://doi.org/10.1007/s12671-015-0388-5"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using structural equation modeling on survey data from 299 full-time employees, this study
  finds that dispositional mindfulness (measured as four facets) predicts work engagement
  and psychological well-being, and that this relationship is mediated by positive job-
  related affect and by two facets of psychological capital, hope and optimism. The facet
  non-reacting to inner experience emerged as the mindfulness component most central to
  these outcomes, directly and indirectly influencing engagement, well-being, hope, and
  optimism, while acting-with-awareness played no role and self-efficacy/resiliency did not
  influence the outcomes at all.
claims:
  - text: "A partial-mediation model (model 2) fit the data significantly better than a strict serial full-mediation model (model 1) (chi-square difference test significant, p<0.001; model 2 CFI=0.900, RMSEA=0.056 vs model 1 CFI=0.879, RMSEA=0.062), indicating mindfulness affects work engagement and well-being both directly and via positive affect/psychological capital rather than through one strict causal chain."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "wellbeing"]
    predictors: ["hope"]
  - text: "The mindfulness facet non-reacting (ability to observe distressing thoughts/emotions without automatic response) was the single most influential predictor, exerting direct and indirect (via positive affect, hope, optimism) effects on work engagement and well-being, whereas acting-with-awareness had no significant role and self-efficacy/resiliency did not predict either outcome."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "wellbeing"]
    predictors: ["hope"]
  - text: "Mindfulness's effect on work engagement was fully indirect (via positive affect and hope), while its effect on well-being was partial mediation (direct effect of non-reacting plus indirect paths through positive affect, hope, and optimism), supporting Broaden-and-Build theory that positive affect expands psychological resources that in turn boost engagement and well-being."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "wellbeing"]
    predictors: ["hope"]
population:
  who: "299 full-time working adults (123 male, 176 female; mean age 40.1) from public, private, non-profit, and volunteer sectors, roughly half self-identified meditators"
  where: ["UK", "other Western countries (36-country Western classification)"]
  when: null
  n: 299
  sector: ["mixed-general-workforce"]
  sample_notes: >
    Convenience sample recruited via university/social media posts, email lists, and
    meditation-center mailing lists; self-selected online survey with a prize-draw
    incentive; 8 participants excluded as multivariate outliers leaving N=291 for analysis;
    sample skews toward meditators/mindfulness-interested individuals, limiting
    generalizability.
limitation:
  primary: "Cross-sectional design means all reported mediation pathways are correlational; no causal claims about mindfulness improving engagement or well-being can be made without experimental or longitudinal replication."
  others:
    - "Self-selected convenience sample recruited partly through meditation networks likely over-represents people already interested in or practicing mindfulness, biasing estimates of dispositional mindfulness effects."
    - "All measures are self-report questionnaires completed in a single session, raising (though partially mitigated via SEM) common-method-variance concerns."
    - "Several structural paths were added post hoc based on modification indices, so the final 'best-fitting' model is exploratory and needs confirmatory replication."
risk_of_bias: "medium"
relevance_to_project: >
  Identifies non-reactivity to distressing thoughts/emotions (a specific mindfulness skill)
  and psychological resources like hope and optimism as mechanisms linking an individual-
  level trait to work engagement and well-being, which is directly relevant to designing
  worker-facing interventions (e.g., mindfulness or hope-building programs) intended to
  reduce burnout and improve engagement in remote/distributed teams.
tags:
  topic: ["wellbeing", "job-engagement", "burnout", "mental-health"]
  method: ["survey", "cross-sectional"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Mindfulness at Work_ Positive Affect, Hope, and Optimism Mediate the Relationship Between Dispositional Mindfulness, Work Engagement, and Well-Being/Mindfulness at Work_ Positive Affect, Hope, and Optimism Mediate the Relationship Between Dispositional Mindfulness, Work Engagement, and Well-Being.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Mindfulness at Work_ Positive Affect, Hope, and Optimism Mediate the Relationship Between Dispositional Mindfulness, Work Engagement, and Well-Being.pdf"
  notes: null

---

id: "netemeyer-1996-development-and-validation-of-workfamily-conflict"
title: "Development and validation of work–family conflict and family–work conflict scales."
authors:
  - "Netemeyer, Richard G."
  - "Boles, James S."
  - "McMurrian, Robert"
year: 1996
doi: "10.1037/0021-9010.81.4.400"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 81, issue: 4, pages: "400-410"}
citation: "Netemeyer et al. (1996). Development and validation of work–family conflict and family–work conflict scales.. Journal of Applied Psychology, 81(4), 400-410. https://doi.org/10.1037/0021-9010.81.4.400"
article_type: "methods"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This paper develops and validates two short, five-item self-report scales that separately
  measure work-family conflict (WFC) and family-work conflict (FWC) as distinct constructs,
  using confirmatory factor analysis across three independent samples (teachers, small
  business owners, and real estate salespeople). The scales showed adequate internal
  consistency (alpha .82-.90), discriminant validity between WFC and FWC, and predicted
  correlations with burnout, job tension, job satisfaction, organizational commitment,
  turnover intention, life satisfaction, and depression. It contributes a compact,
  psychometrically validated instrument that the SNH project can reuse to measure how work
  demands spill into home life (and vice versa) as a driver of burnout and disengagement.
claims:
  - text: "Confirmatory factor analysis supported a two-factor WFC/FWC structure over a one-factor model in all three samples (e.g., Sample 1: two-factor GFI=.92, CFI=.96 vs one-factor GFI=.60, CFI=.65; chi-square difference tests all p<.01), and construct reliabilities/coefficient alphas ranged from .82 to .90 across samples."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction"]
    predictors: ["workload", "boundary-management"]
  - text: "WFC was significantly and positively correlated with burnout (Maslach Burnout Inventory, r=.38 to .56 across samples) and job tension (r=.43 to .58), and was more strongly correlated with burnout, job tension, and hours worked than FWC was, while FWC was more strongly correlated with self-efficacy and sales performance than WFC in the salesperson sample."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction", "turnover"]
    predictors: ["workload", "boundary-management"]
  - text: "Across samples, the mean WFC score was significantly higher than the mean FWC score (e.g., Sample 1: WFC M=15.42 vs FWC M=9.99, t(178)=11.33, p<.01), indicating workers experienced work interfering with family life more than the reverse; WFC and FWC were also positively correlated with physical symptomology, depression (ATQ), and turnover-intention/job-search measures, and negatively correlated with life satisfaction and relationship satisfaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["depression", "turnover", "wellbeing"]
    predictors: ["workload", "boundary-management"]
population:
  who: "Three separate US working-adult samples: elementary/high-school teachers and administrators, small business owners, and real estate salespeople, all recruited by mail survey in a large southeastern US city"
  where: ["United States"]
  when: null
  n: 530
  sector: ["education", "small-business", "sales-real-estate"]
  sample_notes: >
    Sample 1: 182 of 224 mailed surveys returned (81% response); Sample 2: 162 of 298 (54%
    response); Sample 3: 186 of 700 (27% response). All three are convenience/mail samples
    from a single southeastern US metro area, limiting generalizability across regions and
    occupations; self-report, cross-sectional, single-timepoint design for all validity
    correlations.
limitation:
  primary: "Design is nonexperimental and entirely self-report/cross-sectional, so only associations between WFC/FWC and other constructs at one point in time can be established, not causal direction."
  others:
    - "The five-item scales use a unidimensional (general demand/time/strain blended) conceptualization rather than separating time-based and strain-based conflict, which some researchers argue is a richer multidimensional structure."
    - "All three samples are drawn from a single southeastern US city and a narrow set of occupations (teachers, small business owners, salespeople), so validation across broader occupational and geographic contexts is still needed."
risk_of_bias: "low"
relevance_to_project: >
  This is a foundational, widely-cited psychometric instrument (the Netemeyer WFC/FWC
  scales) that the SNH project can adopt or adapt to measure boundary-management strain and
  work-home spillover as a predictor of burnout, isolation, and turnover intention in
  remote/hybrid workers, where blurred home-work boundaries are a central mechanism.
tags:
  topic: ["burnout", "work-life-balance", "measurement", "job-satisfaction"]
  method: ["survey", "cross-sectional"]
  population: ["knowledge-workers", "sales-workers", "educators"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Netemeyer et al. (1996) - Development and Validation of Work-Family Conflict and Family-Work Conflict Scales/Netemeyer et al. (1996) - Development and Validation of Work-Family Conflict and Family-Work Conflict Scales.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Netemeyer et al. (1996) - Development and Validation of Work-Family Conflict and Family-Work Conflict Scales.pdf"
  notes: null

---

id: "ter-2015-flexible-work-designs-and-employee-wellbeing"
title: "Flexible work designs and employee well‐being: examining the effects of resources and demands"
authors:
  - "ter Hoeven, Claartje L."
  - "van Zoonen, Ward"
year: 2015
doi: "10.1111/ntwe.12052"
venue: {type: "journal", name: "New Technology, Work and Employment", volume: 30, issue: 3, pages: "237-255"}
citation: "ter Hoeven et al. (2015). Flexible work designs and employee well‐being: examining the effects of resources and demands. New Technology, Work and Employment, 30(3), 237-255. https://doi.org/10.1111/ntwe.12052"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using the Job Demands-Resources model, this study of 999 Dutch employees tests whether
  flexible work designs (FWDs: schedule, location, and communication-technology flexibility)
  affect well-being through opposing resource and demand pathways. Structural equation
  modeling shows FWDs improve positive-affect well-being via work/life balance, job
  autonomy, and communication effectiveness, but simultaneously undermine it via increased
  interruptions; unpredictability and work intensification were not significant mediators.
  The resource pathways (work/life balance, autonomy) were significantly stronger than the
  interruption-demand pathway, indicating FWD benefits generally outweigh this cost for
  motivational well-being.
claims:
  - text: "FWDs had significant positive indirect effects on employee well-being through work/life balance (b*=0.104, p=0.002), job autonomy (b*=0.132, p=0.001), and communication effectiveness (b*=0.015, p=0.014); FWDs had a significant negative indirect effect through increased interruptions (b*=-0.017, p=0.004), while indirect effects through unpredictability and work intensification were non-significant."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "job-engagement"]
    predictors: ["autonomy", "work-life-balance", "communication"]
  - text: "Post hoc contrasts showed the indirect effect through work/life balance was significantly stronger than the effect through interruptions (b*=0.087, 95% CI [.052,.124], p=0.001), and likewise the autonomy pathway was significantly stronger than the interruptions pathway (b*=0.115, 95% CI [.075,.164], p=0.001); the communication-effectiveness and interruptions pathways did not differ significantly, indicating balanced opposing mediation there. The full model explained 29.4% of variance in employee well-being."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing"]
    predictors: ["autonomy", "work-life-balance", "technostress"]
  - text: "Contrary to hypothesis, unpredictability of work developments was not negatively associated with well-being through the FWD pathway (b*=0.002, p=0.463, ns), and work intensification also showed no significant mediating effect (b*=-0.003, p=0.253, ns); the authors argue self-chosen overwork and challenge-demand framing may explain the absence of these expected negative pathways."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["wellbeing", "stress"]
    predictors: ["workload", "technostress"]
population:
  who: "Dutch employees working at least 20 hours/week in organizations with 50+ employees, recruited via a commercial online panel; a second independent Dutch worker sample was used for scale cross-validation"
  where: ["Netherlands"]
  when: null
  n: 999
  sector: ["general-workforce"]
  sample_notes: >
    Web-based voluntary/anonymous survey via a data collection firm; 1,005 recruited, 6
    removed for incomplete data or self-employment, leaving n=999 (43% female, mean age
    42.94, 36% higher education, 27% managers); sample described as representative of the
    Dutch workforce on hours worked. A second cross-validation sample (n=404) used to
    validate previously untested scales (FWDs, interruptions, unpredictability).
limitation:
  primary: "Cross-sectional self-report design cannot establish causal direction between FWDs and well-being, despite the authors' supplementary comparison of alternative/reversed models suggesting the hypothesized direction fits better."
  others:
    - "All measures came from same-day online self-reports, raising common method bias concerns (estimated 10.9-13.7%), with no supervisor/colleague or objective corroboration."
    - "Well-being was operationalized narrowly as positive affect (a motivational component), so findings may not generalize to health-related outcomes like burnout or exhaustion, which the authors note could reverse the resource/demand balance found here."
    - "Several scales (FWDs, interruptions, unpredictability) were newly constructed for this study rather than fully validated prior to use, though cross-validated on a second sample."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's remote/flexible-work design decisions by quantifying
  which specific mechanisms (autonomy, work/life balance, communication effectiveness vs.
  interruptions) drive well-being outcomes under flexible work arrangements, and shows that
  interruption-related demands, not unpredictability or work intensification, are the
  primary risk factor to design against.
tags:
  topic: ["remote-work", "wellbeing", "work-life-balance", "technostress"]
  method: ["cross-sectional", "survey"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/New Technol Work Employ - 2015 - Hoeven - Flexible work designs and employee well‐being  examining the effects of resources/New Technol Work Employ - 2015 - Hoeven - Flexible work designs and employee well‐being  examining the effects of resources.md"
  pdf: null
  notes: null

---

id: "felstead-2017-assessing-the-growth-of-remote-working"
title: "Assessing the growth of remote working and its consequences for effort, well‐being and work‐life balance"
authors:
  - "Felstead, Alan"
  - "Henseke, Golo"
year: 2017
doi: "10.1111/ntwe.12097"
venue: {type: "journal", name: "New Technology, Work and Employment", volume: 32, issue: 3, pages: "195-212"}
citation: "Felstead et al. (2017). Assessing the growth of remote working and its consequences for effort, well‐being and work‐life balance. New Technology, Work and Employment, 32(3), 195-212. https://doi.org/10.1111/ntwe.12097"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using UK Labour Force Survey data (1981-2015) and the Skills and Employment Survey (2001,
  2006, 2012), this study finds that only about a third of the growth in remote working is
  explained by compositional shifts toward the knowledge economy, flexible employment, and
  workforce demographics, meaning roughly two-thirds of the growth is a genuine detachment
  of work from place. It also tests the 'win-win' narrative empirically: remote workers
  report significantly higher work effort, organisational commitment, enthusiasm, and job
  satisfaction than otherwise-identical office-based workers, but these gains come paired
  with significantly worse work-home spillover (more difficulty switching off and
  unwinding), supporting both social exchange theory and border theory simultaneously.
claims:
  - text: "Around two-thirds of the increase in remote working cannot be explained by compositional factors (knowledge economy, flexible employment, demographic change); e.g. for working remotely at least one day/week, unexplained annual growth remained 0.141 percentage points (vs 0.219 raw), a 64.4% residual after controls (p<.001)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: []
    predictors: ["remote-work-intensity"]
  - text: "Remote workers show significantly higher work effort than fixed-location workers: 39.0% of remote workers said working extra unpaid hours was 'very true' vs 24.1% of office-based workers; regression-adjusted effects on working hard, working beyond formal hours, and voluntary effort were all significant (b=0.267, p<.001 for extra hours)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "productivity"]
    predictors: ["remote-work-intensity"]
  - text: "Remote working is associated with significantly higher organisational commitment (b=0.056***), enthusiasm (b=0.081***), and overall job satisfaction (b=0.128***), but also significantly higher work-home spillover/inability to switch off (b=0.151***), net of controls for occupation, industry, region, and demographics -- i.e. benefits and costs occur together, not as a tradeoff-free win-win."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "work-life-balance", "wellbeing"]
    predictors: ["remote-work-intensity", "boundary-management"]
population:
  who: "UK employees and self-employed workers aged 20-59 in paid work; Labour Force Survey (LFS) pooled 1981 and 1992-2015 spring quarters, and Skills and Employment Survey (SES) 2001/2006/2012 waves"
  where: ["United Kingdom"]
  when: "1981-2015 (LFS trend data); 2001, 2006, 2012 (SES outcome data)"
  n: 1146778
  sector: ["general-workforce"]
  sample_notes: >
    LFS is a large nationally representative labour market survey (~45,000 workers per
    quarter); SES samples were 4,470 (2001), 7,787 (2006), and 3,200 (2012) workers, pooled
    for regression analysis (N=~12,111-13,088 per outcome model). Both are established,
    weighted, nationally representative UK surveys, giving stronger external validity than
    the small organisational case studies the authors critique.
limitation:
  primary: "Remote working is measured via categorical work-location survey questions rooted in a home/work binary, which cannot capture partial-day home work, working 'on the move', or variable use of the conventional workplace -- likely underestimating true prevalence and misclassifying heterogeneous remote-work arrangements."
  others:
    - "Associations are ceteris paribus correlations from cross-sectional regressions, not causal estimates; unobserved selection (e.g. who chooses/is offered remote work) could drive both remote-work status and outcomes."
    - "'Remote working' is treated as a fairly homogeneous category despite covering very different arrangements (full home-based, hybrid, mobile/on-the-move workers)."
risk_of_bias: "low"
relevance_to_project: >
  Provides large-scale, nationally representative UK evidence that remote work's benefits
  (commitment, enthusiasm, job satisfaction) and its costs (work-home spillover, inability
  to switch off) are not mutually exclusive but co-occur -- directly informing SNH's need to
  design boundary-management supports alongside, not instead of, engagement/retention
  interventions for remote workers.
tags:
  topic: ["remote-work", "work-life-balance", "job-satisfaction", "job-engagement"]
  method: ["survey", "secondary-data", "longitudinal"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/New Technol Work Employ - 2017 - Felstead - Assessing the growth of remote working and its consequences for effort/New Technol Work Employ - 2017 - Felstead - Assessing the growth of remote working and its consequences for effort.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/New Technol Work Employ - 2017 - Felstead - Assessing the growth of remote working and its consequences for effort .pdf"
  notes: null

---

id: "olson-1983-remote-office-work"
title: "Remote office work"
authors:
  - "Olson, Margrethe H."
year: 1983
doi: "10.1145/358061.358068"
venue: {type: "journal", name: "Communications of the ACM", volume: 26, issue: 3, pages: "182-187"}
citation: "Olson (1983). Remote office work. Communications of the ACM, 26(3), 182-187. https://doi.org/10.1145/358061.358068"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "weak", preregistered: false}
gist: >
  Olson's 1983 exploratory interview study of 32 organizational employees who worked at home
  (plus their managers) identifies job characteristics (defined deliverables, low
  interactivity, autonomy over pace) and individual traits (self-discipline, bargaining
  power, preference for fewer social contacts) associated with workable remote arrangements.
  It also raises, as open research questions rather than tested findings, the effects of
  remote work on supervision, long-term career visibility, and social isolation from
  professional peers.
claims:
  - text: "Jobs performed successfully at home shared common characteristics across the sample: minimal physical/equipment requirements (only 14 of 32 needed a terminal), individual control over work pace, well-defined deliverables and milestones, a need for sustained concentration, and a relatively low or 'batchable' need for communication with the central office."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["productivity", "performance"]
    predictors: ["autonomy", "workload"]
  - text: "23 of 32 interviewees felt they had bargaining power (via specialized skills or proven loyalty) that let them negotiate the work-at-home arrangement; 12 of 32 cited family caregiving needs as their primary reason for choosing it; and the subset with few social contacts outside work and family reported fewer problems with isolation or concentration than the rest of the group."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["isolation", "job-satisfaction"]
    predictors: ["autonomy", "social-support"]
  - text: "Managers reported that employees with electronic-mail access had daily contact with and monitoring by their supervisors, versus much less frequent contact for those without it, making remote supervision easier; separately, nearly half of interviewees said working at home worsened physical habits (eating more, drinking more coffee, smoking more)."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["communication", "wellbeing"]
    predictors: ["remote-work-intensity", "boundary-management"]
population:
  who: "32 organizational employees working at home on a regular basis (clerical, professional, and managerial roles) plus 8 of their managers, drawn from companies running pilot work-at-home programs and one software subcontracting firm"
  where: ["United States"]
  when: "1981-1982 (Diebold Automated Office Program study)"
  n: 32
  sector: ["office-services", "technology", "insurance"]
  sample_notes: >
    Convenience sample recruited through employer pilot programs and one contract software
    firm; all participants were already voluntarily work-at-home, so the sample is biased
    toward workers and arrangements perceived as successful. 20 women, 12 men; semi-
    structured telephone interviews of ~30 minutes with employees and ~1 hour with managers;
    no response-rate or representativeness data given.
limitation:
  primary: "Exploratory, non-random convenience sample of 32 employees drawn from a handful of pilot programs and one contract firm, with no comparison group, statistical testing, or validated measures — conclusions are qualitative impressions, not generalizable estimates."
  others:
    - "Relies on brief self-report telephone interviews (about 30 minutes per employee) and researcher interpretation rather than observed behavior or outcome data."
    - "Sample is limited to employees already selected into voluntary, employer-sponsored pilot programs, likely over-representing satisfied and successful cases."
    - "1983 technology and workforce context (pre-internet, pre-videoconferencing, dictation/paper-based tools) limits direct generalizability to contemporary remote and hybrid work."
risk_of_bias: "high"
relevance_to_project: >
  One of the earliest empirical treatments of remote-work isolation: it explicitly names
  contact with professional peers and social isolation as an unresolved risk of work-at-home
  arrangements, and links low-communication job design plus preference for solitude to who
  copes well remotely — a foundational reference point for how the SNH project frames
  isolation, belonging, and boundary management as design problems for remote workers.
tags:
  topic: ["remote-work", "isolation", "work-life-balance", "wellbeing"]
  method: ["qualitative", "interview"]
  population: ["remote-workers", "office-workers", "early-telework"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Olson (1983) - Remote Office Work - Changing Work Patterns in Space and Time/Olson (1983) - Remote Office Work - Changing Work Patterns in Space and Time.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Olson (1983) - Remote Office Work - Changing Work Patterns in Space and Time.pdf"
  notes: null

---

id: "onnela-2007-structure-and-tie-strengths-in-mobile"
title: "Structure and tie strengths in mobile communication networks"
authors:
  - "Onnela, J.-P."
  - "Saramäki, J."
  - "Hyvönen, J."
  - "Szabó, G."
  - "Lazer, D."
  - "Kaski, K."
  - "Kertész, J."
  - "Barabási, A.-L."
year: 2007
doi: "10.1073/pnas.0610245104"
venue: {type: "journal", name: "Proceedings of the National Academy of Sciences", volume: 104, issue: 18, pages: "7332-7336"}
citation: "Onnela et al. (2007). Structure and tie strengths in mobile communication networks. Proceedings of the National Academy of Sciences, 104(18), 7332-7336. https://doi.org/10.1073/pnas.0610245104"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  Analyzing 18 weeks of anonymized mobile-phone call records covering roughly 20% of an
  entire country's population (4.6 million people, 7.0 million reciprocated-call ties), the
  authors show that tie strength (aggregate call duration) is systematically coupled to
  local network structure: strong ties sit inside tightly-knit communities and weak ties
  bridge between them, confirming Granovetter's strength-of-weak-ties hypothesis at societal
  scale. They further show this coupling makes the network robust to losing its strongest
  ties but catastrophically fragile to losing its weakest ones, and that it slows
  information diffusion by dynamically trapping news inside communities rather than letting
  it flow globally.
claims:
  - text: "Topological overlap (share of mutual friends) increases with tie strength for approximately 95% of links, meaning strong ties cluster within communities and weak ties disproportionately form the bridges connecting distinct communities — the first society-level empirical confirmation of the strength-of-weak-ties hypothesis."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["communication", "social-presence"]
    predictors: ["network-structure"]
  - text: "Removing the weakest ties (by strength or by overlap) causes the giant component to disintegrate via a phase transition at a critical fraction f_c ≈ 0.80 (weight-based) or 0.62 (overlap-based) of links removed, whereas removing the strongest ties first only produces gradual shrinkage with no collapse — the opposite of the pattern typically seen for hubs in technological/biological networks."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["network-resilience"]
    predictors: ["network-structure"]
  - text: "In diffusion simulations, information spread significantly faster through a control network with all tie strengths set equal than through the real weighted network, where it instead became dynamically trapped inside communities (rapid local spread followed by plateaus); most individuals first received novel information via intermediate-strength ties, indicating both very weak and very strong ties are comparatively ineffective conduits for new information."
    evidence: "modelling"
    support_strength: "moderate"
    outcomes: ["communication"]
    predictors: ["network-structure"]
population:
  who: "Subscribers of a single national mobile-phone operator, reconstructed into an undirected call graph (link = at least one reciprocated pair of calls) covering an estimated 20% of the country's entire population, of whom about 90% held a mobile subscription; giant component includes 84.1% of the 4.6 million nodes."
  where: []
  when: "18-week window of call-detail records (exact calendar dates and country not disclosed in the article, published 2007)"
  n: 4600000
  sector: ["general-population"]
  sample_notes: >
    The country is not named (likely withheld for confidentiality with the telecom partner);
    results were checked for saturation against two- and three-month subsamples with little
    difference. Only reciprocated call pairs are counted as ties, which the authors argue
    filters out one-off/unknown-caller contacts but also excludes one-directional or non-
    mutual relationships and all non-phone communication channels (email, face-to-face,
    landline).
limitation:
  primary: "The network is built purely from mobile call-duration data from one operator in one undisclosed country, so it may not capture the full structure of participants' social ties (email, in-person, landline contact are all excluded) and generalizability to other countries, time periods, or communication modes is untested."
  others:
    - "Tie strength is operationalized solely as aggregated call duration, collapsing structurally different relationship types (family, romantic, work, service) into a single scalar measure."
    - "The information-diffusion results come from a simplified simulation (transmission probability proportional to call duration) rather than observed real-world diffusion of an actual message."
    - "As an observational, non-experimental network analysis, the study establishes structural correlation between tie strength and topology, not causal mechanisms."
risk_of_bias: "low"
relevance_to_project: >
  Provides the foundational, population-scale evidentiary basis for treating tie strength
  and network position (weak bridging ties vs. strong within-community ties) as distinct
  structural resources with different functions — directly informing how SNH work should
  model and measure social-support networks, weak-tie/bridge relationships, and community
  structure rather than treating 'connection' as a single undifferentiated quantity.
tags:
  topic: ["community-health", "social-support", "measurement", "methodology"]
  method: ["secondary-data", "modelling"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/onnela-et-al-2007-structure-and-tie-strengths-in-mobile-communication-networks.pdf"
  notes: null

---

id: "orlikowski-2002-knowing-in-practice-enacting-a-collective"
title: "Knowing in Practice: Enacting a Collective Capability in Distributed Organizing"
authors:
  - "Orlikowski, Wanda J."
year: 2002
doi: "10.1287/orsc.13.3.249.2776"
venue: {type: "journal", name: "Organization Science", volume: 13, issue: 3, pages: "249-273"}
citation: "Orlikowski (2002). Knowing in Practice: Enacting a Collective Capability in Distributed Organizing. Organization Science, 13(3), 249-273. https://doi.org/10.1287/orsc.13.3.249.2776"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Based on 78 interviews at 'Kappa,' a globally distributed multinational software firm, the
  paper identifies five recurring organizational practices (sharing identity, interacting
  face to face, aligning effort, learning by doing, supporting participation) through which
  distributed teams enact a collective 'knowing how' to coordinate complex global product
  development across temporal, geographic, cultural, and political boundaries. Crucially, it
  documents that each practice has a dual nature: the very practices that build coordination
  and cohesion also generate SNH-relevant costs, including burnout from travel-intensive
  face-to-face bonding, organizational groupthink from shared identity, turnover risk
  despite heavy investment in employee development, and fragmentation/conflict from
  participatory inclusion.
claims:
  - text: "Extensive face-to-face interaction, used deliberately to build trust and social networks across Kappa's 15 globally distributed development units, produced significant burnout risk: HR managers flagged burnout from travel, 'many VOS project members reported increased stress and decreased family time,' and one project manager described emotional exhaustion severe enough that he temporarily swapped roles with a colleague for several months because he 'wasn't sleeping at nights.'"
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "stress", "work-life-balance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "A strong shared 'Kappa way' organizational identity, reinforced through common training and socialization across 30 nationalities and 15 sites, fostered cooperation, trust, loyalty, and a sense of belonging ('everyone feels connected... part of this big family'), but was also identified by members and the researcher as producing organizational groupthink and rigidity that constrained Kappa's ability to shift to new (Internet-based, object-oriented) development paradigms."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["sense-of-belonging", "collaboration"]
    predictors: ["organizational-culture", "community-engagement"]
  - text: "Investment in individual skill development, career mentoring by dedicated 'competence managers,' and a no-layoff, error-tolerant culture were credited by employees with building job security and loyalty ('here I know I have job security'), yet senior executives reported this investment was becoming insufficient to prevent talent loss as Internet startups offered more lucrative compensation and equity packages."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["retention", "turnover", "job-satisfaction"]
    predictors: ["peer-mentoring", "organizational-culture"]
population:
  who: "78 interviewees (software engineers, support staff, local unit managers, project managers, senior executives) at 'Kappa,' a large multinational systems-software company, representing about 10% of personnel involved in its flagship distributed product (VOS)"
  where: ["Netherlands (HQ)", "multiple countries across 5 continents (15 development units total; fieldwork covered 5 DUs plus HQ)"]
  when: "1998 (six months of fieldwork)"
  n: 78
  sector: ["technology", "software"]
  sample_notes: >
    Purposive/theoretical sampling of engineers, support staff, managers, and executives
    across five of Kappa's 15 globally distributed development units plus headquarters;
    interviews lasted 45 minutes to 3+ hours, almost all taped and transcribed; data
    collection and coding were iterative/exploratory (grounded-theory style). The author
    explicitly notes she was unable to directly observe project activities, so findings rest
    on self-report interview data and documentation rather than ethnographic observation.
limitation:
  primary: "Single-case, exploratory qualitative field study of one highly successful multinational (a positive outlier), relying on retrospective self-report interviews rather than direct observation of work practices, which the author herself flags as a limitation."
  others:
    - "No comparison group or less-successful organization studied, so it is unclear whether the identified practices are causal or merely correlated with Kappa's success."
    - "Findings on burnout, turnover, and groupthink are anecdotal/illustrative quotes rather than measured rates or systematic outcome data."
    - "Company and location names are disguised, limiting independent verification of context."
risk_of_bias: "medium"
relevance_to_project: >
  Offers an early, empirically grounded account of how distributed-team practices that build
  social network health (face-to-face bonding, shared identity, participatory inclusion,
  career investment) simultaneously generate SNH risks (travel-driven burnout, groupthink,
  turnover, decision fragmentation) -- directly useful for the project's design tradeoffs
  around how much in-person contact, identity-building, and inclusive participation to
  engineer into remote/distributed team practices without producing burnout or rigidity.
tags:
  topic: ["remote-work", "collaboration", "burnout", "work-life-balance", "community-health"]
  method: ["qualitative", "case-study"]
  population: ["software-engineers", "distributed-teams", "multinational-corporation"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/orlikowski-2002-knowing-in-practice-enacting-a-collective-capability-in-distributed-organizing/orlikowski-2002-knowing-in-practice-enacting-a-collective-capability-in-distributed-organizing.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/orlikowski-2002-knowing-in-practice-enacting-a-collective-capability-in-distributed-organizing.pdf"
  notes: null

---

id: "bareket-2023-out-of-sight-but-not-out"
title: "Out of sight but not out of mind: The role of loneliness and hope in remote work and in job engagement"
authors:
  - "Bareket-Bojmel, Liad"
  - "Chernyak-Hai, Lily"
  - "Margalit, Malka"
year: 2023
doi: "10.1016/j.paid.2022.111955"
venue: {type: "journal", name: "Personality and Individual Differences", volume: 202, issue: null, pages: "111955"}
citation: "Bareket-Bojmel et al. (2023). Out of sight but not out of mind: The role of loneliness and hope in remote work and in job engagement. Personality and Individual Differences, 202, 111955. https://doi.org/10.1016/j.paid.2022.111955"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A survey of 349 US/UK employees found that remote work does not uniformly reduce job
  engagement; instead, loneliness moderates the relationship, with remote work predicting
  significantly lower engagement only for employees with moderate or high loneliness, not
  for those with low loneliness. A moderated-mediation model further showed that among
  highly lonely employees, remote work was positively associated with hope, which in turn
  predicted higher job engagement, suggesting hope as a resource that can offset engagement
  loss in this vulnerable group. The authors argue this challenges the blanket assumption
  that remote work harms engagement and instead points to loneliness-targeted and hope-
  building interventions as the design lever.
claims:
  - text: "Loneliness significantly moderated the relationship between remote work and job engagement (b = -0.04, SE = 0.01, beta = -0.11, p = .01); simple slopes showed remote work significantly and negatively predicted job engagement for employees with high loneliness (b = -0.08, beta = -0.23, p < .001) and moderate loneliness (b = -0.04, beta = -0.12, p = .01), but not for those with low loneliness (b = -0.001, p = .96)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["loneliness", "remote-work-intensity"]
  - text: "Among employees with high loneliness, remote work significantly predicted higher hope (b = 0.09, SE = 0.03, beta = 0.19, p = .006), and hope significantly predicted job engagement (b = 0.41, beta = 0.57, p < .001); a bootstrapped moderated-mediation index (0.02, 95% CI [0.002, 0.04]) confirmed hope mediated the remote work-engagement link specifically at high loneliness levels, with no significant mediation at average or low loneliness."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["hope", "loneliness", "remote-work-intensity"]
  - text: "Hope and loneliness were strongly negatively correlated (r = -0.46, p < .001), and loneliness was negatively correlated with job engagement (r = -0.27, p < .001), while remote work days showed no significant zero-order correlation with either job engagement (r = -0.07) or hope (r = 0.05), indicating loneliness -- not remote work per se -- is the key risk factor."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["loneliness", "hope"]
population:
  who: "349 employees (170 men, 177 women, 2 other) from the US and UK, employed at least 20 hours/week (excluding freelancers), recruited via the Prolific online platform"
  where: ["United States", "United Kingdom"]
  when: null
  n: 349
  sector: ["general-workforce"]
  sample_notes: >
    Recruited via Prolific with high-reputation filter (>=95% prior approval rate); 51 of
    400 initial respondents excluded for failing prescreening/attention checks. 61% UK, 33%
    US, 6% other nationality; ages 21-69 (M=38.81, SD=9.95); 69% worked remotely at least
    one day/week, 35% fully remote (5 days), 31% fully office-based -- sample skewed toward
    high-frequency remote workers, limiting generalizability to low/no remote-work contexts.
limitation:
  primary: "Cross-sectional, single-sample correlational design (all self-report) precludes causal inference and raises common method variance concerns, though procedural safeguards (anonymity, separated question blocks, attention checks) were used to mitigate this."
  others:
    - "Unequal representation across remote-work intensity, with a disproportionate share working fully remote (5 days/week), limiting power to detect effects at intermediate remote-work levels."
    - "Remote work was measured with a single item (days worked remotely) rather than a validated multidimensional measure, and burnout was not assessed despite being theoretically relevant."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs SNH design by identifying loneliness as the moderating variable that
  determines whether remote work harms engagement, and hope as a candidate intervention
  target/mediator that can protect engagement specifically among lonely remote workers --
  supporting a targeted (not blanket) intervention design for remote-worker social network
  health.
tags:
  topic: ["remote-work", "loneliness", "job-engagement", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement.md"
  pdf: "papers/Remote Workers/Out of sight but not out of mind- The role of loneliness and hope in remote work and in job engagement.pdf"
  notes: null

---

id: "parker-2014-beyond-motivation-job-and-work-design"
title: "Beyond Motivation: Job and Work Design for Development, Health, Ambidexterity, and More"
authors:
  - "Parker, Sharon K."
year: 2014
doi: "10.1146/annurev-psych-010213-115208"
venue: {type: "journal", name: "Annual Review of Psychology", volume: 65, issue: 1, pages: "661-691"}
citation: "Parker (2014). Beyond Motivation: Job and Work Design for Development, Health, Ambidexterity, and More. Annual Review of Psychology, 65(1), 661-691. https://doi.org/10.1146/annurev-psych-010213-115208"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This Annual Review of Psychology article synthesizes work-design research, arguing that
  the dominant motivational paradigm (the Job Characteristics Model and its descendants) is
  necessary but insufficient for today's jobs. Parker proposes that work design should also
  be evaluated for its effects on employee learning and cognitive/identity/moral
  development, on physical and mental health via the demand-control and job demands-
  resources models, and on organizations' ability to achieve control and flexibility
  simultaneously (ambidexterity, enabling bureaucracy, high-reliability organizing). It
  closes with a call for multilevel, longitudinal, and configurational research designs
  rather than single-job-characteristic regression studies.
claims:
  - text: "In Humphrey et al.'s (2007) meta-analysis of 259 studies, motivational work characteristics (variety, autonomy, feedback, significance, identity) explained 34% of the variance in job satisfaction, with social characteristics (e.g., social support) explaining a further 17% and contextual characteristics 4%; core characteristics also related to growth satisfaction, internal work motivation, organizational commitment, coworker satisfaction, burnout, and role perceptions."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["job-satisfaction", "burnout", "turnover"]
    predictors: ["autonomy", "social-support"]
  - text: "A review of 19 longitudinal studies (De Lange et al. 2003) found that about two-thirds showed negative strain effects of high job demands (especially on psychological well-being and sickness absence), but only roughly half showed a main effect of job control on subsequent health outcomes, and support for the classic demand-control interaction (high demands + high control = no strain) was judged unconvincing across multiple reviews."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["wellbeing", "mental-health", "stress"]
    predictors: ["workload", "autonomy"]
  - text: "Kirkman et al. (2004) found that team empowerment was a stronger predictor of virtual team effectiveness when teams met face-to-face less often, suggesting empowerment/autonomy becomes more important, not less, as team interaction becomes more remote and less physically co-located."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["autonomy", "network-structure"]
population:
  who: "No single sample; a narrative synthesis of work/organizational-psychology studies and meta-analyses cited selectively by the author (e.g., a 259-study meta-analysis by Humphrey et al. 2007; a 19-study longitudinal review by De Lange et al. 2003; individual field/quasi-experiments such as Grant et al. 2007 and Parker et al. 2013)."
  where: ["United States", "United Kingdom", "Netherlands", "Sweden", "Norway", "multi-country Europe"]
  when: "Underlying literature cited spans roughly 1957-2014"
  n: null
  sector: ["general-workforce", "manufacturing", "healthcare", "public-safety", "professional-services"]
  sample_notes: >
    This is a review article, not a primary study; no defined sampling frame or systematic
    search protocol is described, so included studies reflect the author's selection rather
    than an exhaustive or reproducible corpus.
limitation:
  primary: "This is a narrative (non-systematic) single-author review: studies were selectively chosen to illustrate arguments rather than identified via a reproducible search-and-screen protocol, so it cannot support formal effect-size or prevalence claims."
  others:
    - "Direct evidence on remote/virtual/distributed work design is minimal in the article, limited to a few passing citations (e.g., Kirkman et al. 2004 on virtual teams, and mentions of teleworking and 'working from home') rather than being a focal topic."
    - "Much of the cited primary evidence is cross-sectional; the author repeatedly notes that longitudinal and quasi-experimental support for core hypotheses (e.g., the demand-control interaction) is weaker and more inconsistent than the cross-sectional literature suggests."
    - "As a single-author Annual Review piece, theoretical framing and emphasis (e.g., ambidexterity, enabling bureaucracy) reflect the author's own research programme and prior publications."
risk_of_bias: "medium"
relevance_to_project: >
  Provides the job/work-design theoretical backbone (autonomy, social support as a job
  resource, job demands-resources model) that the SNH project can draw on when designing
  remote-work roles and interventions to reduce strain and burnout; its finding that team
  empowerment matters more, not less, when teams meet face-to-face less often (Kirkman et
  al. 2004) directly supports designing for autonomy and psychological empowerment in
  distributed/remote teams as a lever against isolation-related performance loss.
tags:
  topic: ["remote-work", "wellbeing", "burnout", "mental-health", "collaboration", "methodology"]
  method: ["review-narrative", "secondary-data"]
  population: ["general-workforce", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Parker (2014) - Beyond Motivation - Job and Work Design for Development Health Ambidexterity and More/Parker (2014) - Beyond Motivation - Job and Work Design for Development Health Ambidexterity and More.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Parker (2014) - Beyond Motivation - Job and Work Design for Development Health Ambidexterity and More.pdf"
  notes: null

---

id: "pelled-1999-exploring-the-black-box-an-analysis"
title: "Exploring the Black Box: An Analysis of Work Group Diversity, Conflict and Performance"
authors:
  - "Pelled, Lisa Hope"
  - "Eisenhardt, Kathleen M."
  - "Xin, Katherine R."
year: 1999
doi: "10.2307/2667029"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 44, issue: 1, pages: "1-28"}
citation: "Pelled et al. (1999). Exploring the Black Box: An Analysis of Work Group Diversity, Conflict and Performance. Administrative Science Quarterly, 44(1), 1-28. https://doi.org/10.2307/2667029"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This field study of 45 electronics-division work teams tests an intervening-process model
  in which demographic diversity shapes cognitive task performance through two distinct
  routes: task conflict and emotional conflict. Functional-background diversity was the key
  driver of task conflict, which in turn improved performance, while race, tenure, and (in
  the opposite direction) age diversity drove emotional conflict, which had no significant
  effect on performance. Task routineness and group longevity moderated most diversity-
  conflict links, showing the diversity-to-performance 'black box' is more differentiated
  than prior single-pathway models assumed.
claims:
  - text: "Functional background diversity was the strongest driver of intragroup task conflict (beta = 1.08, p < .05), while race, gender, and age diversity showed no significant association with task conflict, supporting the hypothesis that job-related diversity attributes matter most for task conflict."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Race diversity (beta = .81, p < .05) and tenure diversity (beta = 1.76, p < .01) were positively associated with emotional conflict, while age diversity was negatively associated with emotional conflict (beta = -3.43, p < .05), and gender diversity showed no significant effect even across multiple sensitivity analyses (alternative heterogeneity indices, proportion measures, and skewness dummies)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Task conflict was positively associated with manager-rated cognitive task performance (beta = .30, p < .05), whereas emotional conflict showed no significant relationship with performance; task and emotional conflict were themselves positively correlated (r = .48, p < .01), and both were moderated by task routineness and group longevity (e.g., diversity-conflict associations weakened once groups passed longevity thresholds of roughly 0.66-1.14 years)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["team-cohesion", "workload"]
population:
  who: "Members of 45 co-located work teams (average size ~10) from the electronics divisions of three major corporations, engaged in process-improvement and product-design projects of moderate-to-high cognitive complexity"
  where: ["United States"]
  when: null
  n: 317
  sector: ["technology", "manufacturing"]
  sample_notes: >
    317 of 443 distributed team-member questionnaires returned (73% average team response
    rate); performance ratings obtained from 41 of 45 team managers; sample is field-based
    but modest in team count (N=45 teams), limiting statistical power; one site (Site B) had
    a distinct, more conservative/bureaucratic culture and was controlled for.
limitation:
  primary: "Cross-sectional design precludes causal interpretation of the diversity-conflict-performance chain; the study measures associations at a single point in time, not change over time."
  others:
    - "Sample size of 45 teams limits statistical power, especially for detecting interaction/moderator effects and full mediation."
    - "Some predictor variables (e.g., age diversity) had limited variance across teams, likely attenuating estimated effects."
    - "Full mediation (a direct diversity-to-performance link) was not established, so the proposed process model is only partially confirmed by the data."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a well-controlled field test showing that diversity's effects on team functioning
  are not uniform: only certain diversity types (functional background, race, tenure, age)
  translate into conflict, and only task conflict (not emotional conflict) predicts
  performance — evidence relevant to designing cross-functional or demographically diverse
  remote/OSS teams so that task disagreement is channeled productively while emotional
  conflict from race/tenure/age differences is actively managed, especially early in a
  team's life before longevity effects dampen it.
tags:
  topic: ["collaboration", "community-health"]
  method: ["cross-sectional", "survey"]
  population: ["corporate-teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/pelled-et-al-1999-exploring-the-black-box-an-analysis-of-work-group-diversity-conflict-and-performance/pelled-et-al-1999-exploring-the-black-box-an-analysis-of-work-group-diversity-conflict-and-performance.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/pelled-et-al-1999-exploring-the-black-box-an-analysis-of-work-group-diversity-conflict-and-performance.pdf"
  notes: null

---

id: "podsakoff-2003-common-method-biases-in-behavioral-research"
title: "Common method biases in behavioral research: A critical review of the literature and recommended remedies."
authors:
  - "Podsakoff, Philip M."
  - "MacKenzie, Scott B."
  - "Lee, Jeong-Yeon"
  - "Podsakoff, Nathan P."
year: 2003
doi: "10.1037/0021-9010.88.5.879"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 88, issue: 5, pages: "879-903"}
citation: "Podsakoff et al. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies.. Journal of Applied Psychology, 88(5), 879-903. https://doi.org/10.1037/0021-9010.88.5.879"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "strong", preregistered: false}
gist: >
  This is the field-defining critical review of common method variance (CMV) in behavioral
  research: it catalogs the mechanisms by which shared measurement method (rather than the
  constructs themselves) inflates or deflates observed relationships between self-reported
  predictor and criterion variables, and evaluates the procedural and statistical remedies
  available to control for it. Drawing on Cote and Buckley's (1987) meta-analysis of 70
  multitrait-multimethod studies, the authors show method variance typically accounts for
  roughly a quarter of measure variance and can shift observed correlations dramatically,
  then systematically critique widely used fixes (Harman's single-factor test, marker-
  variable and partial-correlation techniques, latent-method-factor CFA models) as
  individually insufficient. For the SNH corpus, which relies heavily on single-source self-
  report surveys of remote workers (loneliness, burnout, belonging, engagement measured via
  the same instrument), this paper is the standard reference for assessing whether a given
  study's design adequately guards against common method bias.
claims:
  - text: "Meta-analytic evidence across 70 multitrait-multimethod construct validation studies indicates that, on average, about 26.3% of the variance in a typical research measure is attributable to systematic method variance rather than the construct of interest, ranging from 15.8% in marketing to 30.5% in education studies; attitude measures average 40.7% method variance versus 22.5% for job performance measures."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "wellbeing"]
    predictors: ["sampling-method"]
  - text: "Studies contrasting relationships estimated with versus without common method variance controlled found that, on average, method-contaminated analyses explained approximately 35% of variance in a relationship versus approximately 11% when method variance was controlled, and method effects can either inflate or deflate (not just inflate) observed correlations depending on the correlation between methods."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "performance"]
    predictors: ["sampling-method"]
  - text: "Commonly used post hoc statistical remedies have serious limitations: Harman's single-factor test provides no statistical control and becomes less conservative as the number of variables increases; the marker-variable/partial-correlation technique fails to control for major CMV sources like implicit theories and consistency motif and wrongly assumes method bias only inflates (never deflates) relationships; and even latent single-method-factor CFA approaches assume the method factor does not interact with trait constructs, an assumption that is often untested."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
population:
  who: "Not an empirical sample; the review synthesizes findings from prior multitrait-multimethod (MTMM) meta-analyses (notably Cote & Buckley 1987's 70 construct-validation studies) and dozens of methodological/statistical studies in psychology, marketing, management, and education."
  where: []
  when: null
  n: null
  sector: ["academic"]
  sample_notes: >
    No primary data collection by the authors; population is the set of published MTMM and
    method-bias studies cited throughout the article, spanning multiple disciplines and
    decades up to 2002.
limitation:
  primary: "As a narrative (non-systematic) critical review, it does not report a reproducible search/inclusion protocol, so coverage of the method-bias literature, while extensive, is not guaranteed to be exhaustive or free of selection bias."
  others:
    - "The quantitative estimates of method variance (e.g., 26.3% average) come from a single meta-analytic source (Cote & Buckley, 1987) whose generalizability across all research domains and construct types is uncertain."
    - "The paper is prescriptive/methodological rather than substantive: it makes no claims about any specific social, organizational, or health outcome, only about measurement artifact risk in self-report research designs."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This paper is the standard citation for justifying (or critiquing) survey design choices
  across the SNH corpus, most of which relies on single-source, same-instrument self-reports
  of loneliness, isolation, burnout, and belonging alongside self-reported predictors like
  social support or workload; it directly informs whether such studies' correlational
  findings should be discounted for common method bias and what procedural safeguards
  (temporal/proximal/methodological separation, respondent anonymity, improved item wording)
  a well-designed SNH survey should adopt.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-narrative", "analytical"]
  population: ["general"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Podsakoff et al. (2003) - Common Method Biases in Behavioral Research - A Critical Review.pdf"
  notes: null

---

id: "reagans-2003-network-structure-and-knowledge-transfer-the"
title: "Network Structure and Knowledge Transfer: The Effects of Cohesion and Range"
authors:
  - "Reagans, Ray"
  - "McEvily, Bill"
year: 2003
doi: "10.2307/3556658"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 48, issue: 2, pages: "240-267"}
citation: "Reagans et al. (2003). Network Structure and Knowledge Transfer: The Effects of Cohesion and Range. Administrative Science Quarterly, 48(2), 240-267. https://doi.org/10.2307/3556658"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using dyadic survey and network data from 102 employees (1,330 dyads) at a contract R&D
  firm, this study shows that social cohesion (dense third-party ties around a relationship)
  and network range (ties spanning distinct expertise areas) each ease knowledge transfer
  above and beyond the effect of tie strength alone. The findings decouple tie strength from
  network structure, showing cohesion and range make independent, complementary
  contributions rather than the benefits of one coming at the expense of the other, and that
  both effects are nonlinear (diminishing returns beyond a point).
claims:
  - text: "Social cohesion (network density, indirect structural constraint) had a significant positive effect on ease of knowledge transfer even after controlling for tie strength, friendship, and advice-seeking (model 6 coefficient 6.3, p<.01; effect held with fixed effects for individuals)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Network range (diversity of ties across expertise areas) independently increased ease of knowledge transfer (model 7 coefficient .74, p<.05), and this range effect did not vary with knowledge codifiability, contradicting the assumption that boundary-spanning ties matter only for simple/codified knowledge."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure"]
  - text: "Tie strength positively predicted ease of transfer (model 4, p<.01), but its apparent interaction with knowledge tacitness weakened and effectively disappeared once network density and range were added to the model, indicating that prior findings attributing tacit-knowledge transfer benefits to strong ties were partly capturing network structure effects (tie strength and density correlated r=.38)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication"]
    predictors: ["network-structure", "social-support"]
population:
  who: "102 employees (scientists, engineers, and staff, mostly holding master's/doctoral degrees) at a 113-person contract R&D materials-science consulting firm in the American Midwest"
  where: ["United States"]
  when: null
  n: 102
  sector: ["private-sector-rd", "engineering-consulting"]
  sample_notes: >
    Onsite survey with 92% response rate (104/113 employees), 84% full completion; network
    data combined sociometric (fixed roster) and egocentric (free recall) name-generator
    techniques; final analytic sample was 1,330 non-independent dyads from 102 respondents
    after excluding missing data, analyzed with individual fixed effects to address network
    autocorrelation.
limitation:
  primary: "Single-firm, single-industry (R&D consulting) cross-sectional design limits generalizability, and although network measures used multi-respondent data to reduce single-source bias, the dependent variable (ease of transfer) and some predictors came from the same survey respondent."
  others:
    - "Cannot fully rule out that the network diversity effect reflects unmeasured individual absorptive capacity rather than network-structure-induced framing/perspective-taking behavior, though individual fixed effects and knowledge-breadth controls partially address this."
    - "Measures 'ease of transfer' as perceived by the knowledge source only, not actual transfer outcomes or recipient-reported ease."
    - "Data are from 2003 (pre-digital-collaboration-tools era) in a co-located, in-person work setting, limiting direct applicability to distributed/remote work network structures."
risk_of_bias: "low"
relevance_to_project: >
  Provides a validated, quantitative distinction between tie strength, social cohesion, and
  network range as separate levers for easing knowledge/help transfer among colleagues --
  directly informs how the SNH project might design or measure network structure
  interventions (e.g., encouraging cross-team/cross-community ties) rather than only
  strengthening individual dyadic relationships to improve collaboration and reduce
  isolation.
tags:
  topic: ["collaboration", "community-health", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "engineers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/reagans-mcevily-2003-network-structure-and-knowledge-transfer-the-effects-of-cohesion-and-range.pdf"
  notes: null

---

id: "shirmohammadi-2022-remote-work-and-work-life-balance"
title: "Remote work and work-life balance: Lessons learned from the covid-19 pandemic and suggestions for HRD practitioners"
authors:
  - "Shirmohammadi, Melika"
  - "Au, Wee Chan"
  - "Beigi, Mina"
year: 2022
doi: "10.1080/13678868.2022.2047380"
venue: {type: "journal", name: "Human Resource Development International", volume: 25, issue: 2, pages: "163-181"}
citation: "Shirmohammadi et al. (2022). Remote work and work-life balance: Lessons learned from the covid-19 pandemic and suggestions for HRD practitioners. Human Resource Development International, 25(2), 163-181. https://doi.org/10.1080/13678868.2022.2047380"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This integrative literature review synthesizes 40 empirical studies (published March
  2020-August 2021) plus nine pre-pandemic reviews on remote work and work-life balance,
  using person-environment fit theory to structure the analysis. It identifies four
  recurring misfits between the promised benefits of remote work and workers' pandemic-era
  experiences: flextime vs. work intensification, flexplace vs. home space limitations,
  technological feasibility vs. technostress/isolation, and family-friendliness vs.
  intensified housework/care burdens. The authors translate these misfit themes into
  practical suggestions for HRD practitioners on offering, preparing for, and sustaining
  remote work arrangements.
claims:
  - text: "Communication with colleagues and supervisors mediated through ICTs during pandemic remote work led to feelings of professional isolation and loneliness, because virtual social interactions were lower quality and produced less closeness between peers, which in turn contributed to stress and reduced productivity."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["isolation", "loneliness", "stress", "productivity"]
    predictors: ["technostress", "social-presence", "communication"]
  - text: "Working from home increased work hours and intensified workload during the pandemic because employers expected employees to be 'always online' and respond immediately, and constant/excessive supervisor monitoring negatively affected remote workers' productivity and created work-family conflict."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "productivity", "burnout"]
    predictors: ["workload", "leadership-style", "boundary-management"]
  - text: "Across the reviewed studies, most additional pandemic-era housework and childcare was handled by women even as men took on somewhat more childcare responsibility, and intensified domestic/care demands (worsened by space limitations in the home) reduced remote workers' ability to concentrate on work tasks and lowered work-life balance."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["workload", "boundary-management"]
population:
  who: "40 peer-reviewed empirical studies (quantitative 72%, qualitative 23%, mixed-methods 5%) on work-life balance while working from home during COVID-19, plus 9 supplementary pre-pandemic literature reviews/meta-analyses on remote work and flexible work arrangements"
  where: ["United States", "Italy", "India", "Australia", "China", "France", "Netherlands", "Canada", "Spain", "Israel", "United Kingdom", "Germany", "Lithuania", "Romania", "Greece", "Turkey", "Iceland", "Ireland", "Singapore", "Ghana", "Argentina"]
  when: "March 2020-August 2021 (data collection window of included studies); search conducted in Web of Science Core Collection"
  n: 40
  sector: ["cross-sector"]
  sample_notes: >
    Studies selected via SPIDER framework from a larger dataset originally collected for
    another project; required peer-reviewed empirical status, COVID-19-era data, focus on
    work-life interface while working from home, and an internal quality rating above 3/5.
    80% of included studies focused on a single country, 6 spanned multiple countries, 2 did
    not specify location; selection and quality-rating process is not independently
    verifiable and introduces potential selection bias.
limitation:
  primary: "As a thematic/integrative review rather than a systematic review with formal risk-of-bias appraisal or meta-analytic effect pooling, the four-theme framework aggregates heterogeneous study designs, measures, and populations into broad narrative patterns, limiting precision about effect sizes or causal direction."
  others:
    - "The authors note most included pandemic studies did not report the theory informing their design, limiting the review's ability to draw firm theoretical conclusions beyond the person-environment fit framework the authors themselves imposed."
    - "Findings reflect an acute crisis period (mandatory, involuntary, abrupt remote work under stay-home orders) and may not generalize to voluntary, well-resourced, non-crisis remote or hybrid work arrangements."
    - "Inclusion criteria required an internal team quality rating above 3/5, a subjective screening step whose reliability is not reported."
risk_of_bias: "medium"
relevance_to_project: >
  Directly evidences the isolation/loneliness-via-technostress mechanism (ICT-mediated
  communication producing lower-quality, less-close peer interaction) that the SNH project
  treats as a core remote-work risk pathway, and offers concrete HRD-practitioner
  interventions (regular check-ins, virtual informal social spaces, boundary-setting
  policies, peer/mentoring network development) that map onto candidate SNH design levers
  for maintainer/remote-worker social health.
tags:
  topic: ["remote-work", "isolation", "work-life-balance", "technostress", "wellbeing", "burnout"]
  method: ["review-scoping", "secondary-data"]
  population: ["remote-workers", "cross-sector"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Remote work and work-life balance  Lessons learned from the covid-19 pandemic and suggestions for HRD practitioners/Remote work and work-life balance  Lessons learned from the covid-19 pandemic and suggestions for HRD practitioners.md"
  pdf: "papers/Remote Workers/Remote work and work-life balance  Lessons learned from the covid-19 pandemic and suggestions for HRD practitioners.pdf"
  notes: null

---

id: "sandelowski-2000-combining-qualitative-and-quantitative-sampling-data"
title: "Combining Qualitative and Quantitative Sampling, Data Collection, and Analysis Techniques in Mixed-Method Studies"
authors:
  - "Sandelowski, Margarete"
year: 2000
doi: "10.1002/1098-240x(200006)23:3<246::aid-nur9>3.0.co;2-h"
venue: {type: "journal", name: "Research in Nursing &amp; Health", volume: 23, issue: 3, pages: "246-255"}
citation: "Sandelowski (2000). Combining Qualitative and Quantitative Sampling, Data Collection, and Analysis Techniques in Mixed-Method Studies. Research in Nursing &amp; Health, 23(3), 246-255. https://doi.org/10.1002/1098-240x(200006)23:3<246::aid-nur9>3.0.co;2-h"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methods essay argues that mixed-method combination happens at the technique level
  (sampling, data collection, analysis), not the paradigm level, so qualitative and
  quantitative techniques can be validly combined regardless of a researcher's
  epistemological stance. It maps out concrete combination strategies -- criterion, random
  purposeful, and stratified purposeful sampling; instruments used for description,
  validation, elicitation, and profiling; and the 'quantitizing' and 'qualitizing' data-
  transformation processes -- organized into seven design templates serving the purposes of
  triangulation, complementarity, or development.
claims:
  - text: "Data collection and analysis techniques are not intrinsically linked to a research paradigm or method: the same techniques (e.g., interviews, standardized instruments, grounded theory) can be used from a positivist or a constructivist viewing position, with the mix of techniques revealing the researcher's viewing position rather than dictating it."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["mixed-methods-integration"]
    predictors: ["sampling-method"]
  - text: "The paper proposes seven mixed-method design templates (e.g., QUAL>quan, QUAN>qual, quan>QUAL, Qual>Quan>Qual, a multi-wave Quan/Qual design) that combine qualitative and quantitative components sequentially, concurrently, or iteratively for three purposes: triangulation (corroboration/convergent validation), complementarity (fuller elaboration of results), and development (using one technique's results to guide the next)."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["mixed-methods-integration"]
    predictors: ["sampling-method"]
  - text: "Purposeful and probability sampling can be combined in at least three ways: criterion sampling (using instrument scores to select typical, extreme, or intense cases for follow-up qualitative data collection), random purposeful sampling (random selection within score-defined strata when the information-rich pool is too large for exhaustive purposeful sampling), and stratified purposeful sampling (deliberately filling sampling cells to capture maximal variation on preselected parameters, illustrated with a 16-cell caregiving-dyad design)."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["mixed-methods-integration"]
    predictors: ["sampling-method"]
population:
  who: "Not an empirical study of a defined population; a methodological essay illustrating combination techniques with brief published examples (e.g., couples awaiting infertility treatment/adoption, elderly hip-fracture patients, women weighing hormone replacement therapy, nonresponders to a cholesterol-screening reminder letter)."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No original sample; illustrations are drawn from the author's own prior nursing research
    and a handful of cited health-services studies, chosen to demonstrate technique
    combinations rather than to test a hypothesis.
limitation:
  primary: "As a conceptual/methodological essay rather than an empirical study, its taxonomy of combination techniques is argued and illustrated with brief published examples rather than tested, validated, or compared empirically against alternative frameworks."
  others:
    - "Illustrative examples are drawn selectively from the author's own prior work and a small number of other studies, so the seven templates function as a proposed taxonomy rather than an empirically derived or exhaustive typology."
    - "Written in 1999-2000 for a nursing/health-services audience, predating later mixed-methods consensus frameworks (e.g., Creswell) and current qualitative-data-analytics software, so some terminology and tooling context is dated."
risk_of_bias: "not-applicable"
relevance_to_project: >
  SNH research routinely needs to combine survey/telemetry-style measures (e.g., loneliness
  or burnout scales, commit/message activity) with interview or open-text data on
  maintainers and remote workers; this paper's design templates (e.g., using survey scores
  to trigger purposeful follow-up interviews, or 'quantitizing' interview themes into
  codable variables) offer a concrete playbook for structuring that triangulation and for
  justifying sampling choices in mixed-methods SNH studies.
tags:
  topic: ["methodology", "measurement"]
  method: ["mixed-methods"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Research in Nursing   Health - 2000 - Sandelowski - Combining Qualitative and Quantitative Sampling  Data Collection  and/Research in Nursing   Health - 2000 - Sandelowski - Combining Qualitative and Quantitative Sampling  Data Collection  and.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Research in Nursing   Health - 2000 - Sandelowski - Combining Qualitative and Quantitative Sampling  Data Collection  and.pdf"
  notes: null

---

id: "gladwin-1981-culture-s-consequences-international-differences-in"
title: "Culture's Consequences: International Differences in Work-Related Values"
authors:
  - "Gladwin, Thomas N."
  - "Hofstede, Geert"
year: 1981
doi: "10.2307/257651"
venue: {type: "journal", name: "The Academy of Management Review", volume: 6, issue: 4, pages: "681"}
citation: "Gladwin et al. (1981). Culture's Consequences: International Differences in Work-Related Values. The Academy of Management Review, 6(4), 681. https://doi.org/10.2307/257651"
article_type: "commentary"
method: {design: "book-review", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This is a scholarly book review of Geert Hofstede's 'Culture's Consequences' (1980), in
  which reviewer Thomas N. Gladwin summarizes and praises Hofstede's landmark analysis of
  117,000 employee-attitude questionnaires from a single U.S.-based multinational ('HERMES')
  across 40 countries. The review recounts Hofstede's four empirically derived national-
  culture dimensions — power distance, uncertainty avoidance, individualism, and masculinity
  — and their implications for organizational structure, management style, and cross-
  cultural convergence over time. It contributes an early, well-regarded synthesis of cross-
  national predictors of workplace practices rather than any new data of its own.
claims:
  - text: "Hofstede's survey of roughly 117,000 questionnaires from 88,000 employees of one multinational firm across 40 countries yielded four national-culture dimensions (power distance, uncertainty avoidance, individualism, masculinity); high power-distance nations such as Mexico and the Philippines showed greater centralization, taller hierarchies, and less participative management."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["collaboration", "communication"]
    predictors: ["organizational-culture", "leadership-style"]
  - text: "The power-distance and individualism indices were strongly negatively correlated across nations, and the four dimensions combined to form eight country clusters (e.g., More Developed Latin, Anglo, Nordic) predicted to require different, culturally-fitted management approaches."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture", "network-structure"]
  - text: "Comparing survey waves from 1968 and 1972, Hofstede found no convergence between countries' cultural profiles over the four-year period, but did observe world-wide shifts such as decreasing power distance and increasing individualism."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture"]
population:
  who: "Not the review's own sample: it describes Hofstede's original study population, employees of one unnamed U.S.-based high-technology multinational (pseudonym 'HERMES'), surveyed on demographics, satisfaction, perceptions, and goals/beliefs."
  where: ["40 countries (of 67 originally surveyed), multinational corporate workforce"]
  when: "Survey data collected 1968 and 1972; review published 1981"
  n: 88000
  sector: ["private-sector"]
  sample_notes: >
    This document is itself a ~2,200-word book review, not the primary study, so all
    population details are second-hand as reported by the reviewer; the original survey
    covered 67 countries but only 40 were retained in the book for data stability.
limitation:
  primary: "This is a secondary source (a brief published book review), not the original empirical study, so it offers only the reviewer's summary and opinion rather than verifiable methods, statistics, or raw findings."
  others:
    - "The underlying study's country-level dimension scores rest on cross-sectional correlations with geographic/economic indicators, which cannot establish causal origins of cultural differences."
    - "Data are decades old (1968/1972) from a single multinational firm, limiting generalizability to today's distributed/remote workforce and to non-corporate contexts."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Hofstede's dimensions (power distance, individualism, uncertainty avoidance, masculinity),
  as recounted in this review, offer an early empirical basis for expecting
  national/cultural context to moderate participative management, hierarchy, and
  collaboration norms — relevant to SNH design questions about how culture might shape
  social support expectations and collaboration practices in globally distributed remote
  teams.
tags:
  topic: ["remote-work", "collaboration", "methodology"]
  method: ["commentary"]
  population: ["cross-cultural", "private-sector"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Reviewed Work(s)_ Culture_s Consequences_ International Differences in Work-Related Values by Geert Hofstede/Reviewed Work(s)_ Culture_s Consequences_ International Differences in Work-Related Values by Geert Hofstede.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Reviewed Work(s)_ Culture_s Consequences_ International Differences in Work-Related Values by Geert Hofstede.pdf"
  notes: null

---

id: "karasek-1979-job-demands-job-decision-latitude-and"
title: "Job Demands, Job Decision Latitude, and Mental Strain: Implications for Job Redesign"
authors:
  - "Karasek, Robert A."
year: 1979
doi: "10.2307/2392498"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 24, issue: 2, pages: "285"}
citation: "Karasek (1979). Job Demands, Job Decision Latitude, and Mental Strain: Implications for Job Redesign. Administrative Science Quarterly, 24(2), 285. https://doi.org/10.2307/2392498"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Karasek develops and tests the job demand-control ("job strain") model using national
  survey data from the U.S. Quality of Employment Survey (1972) and the Swedish Level of
  Living Survey (1968, 1974). He finds it is the combination of low decision latitude and
  high job demands, not either factor alone, that predicts mental strain (exhaustion,
  depression), pill consumption, sick days, and job/life dissatisfaction, and that
  longitudinal Swedish data show symptom changes track changes in job strain over time. The
  paper's central policy implication is that redesigning work to increase workers' decision
  latitude can reduce strain without necessarily reducing organizational output.
claims:
  - text: "Workers with jobs combining high psychological job demands and low decision latitude ('high strain' jobs) showed the highest rates of exhaustion and depression in both countries; across deciles of job strain, depression prevalence ranged from 43% to 17% in the U.S. and 30% to 11% in Sweden, with standardized risk ratios up to 1.46 (p<.01)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["depression", "stress", "mental-health"]
    predictors: ["workload", "autonomy"]
  - text: "Job strain was strongly associated with job and life dissatisfaction: workers in the top job-strain decile reported roughly six times the severe dissatisfaction of workers in the bottom decile (interaction terms significant at p<.001), with a secondary dissatisfaction peak also found among 'passive' (low-demand, low-control) jobs."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "stress"]
    predictors: ["workload", "autonomy"]
  - text: "Using longitudinal Swedish panel data (1968-1974), increases in job strain (rising demands with declining decision latitude) were associated with increases in exhaustion and depression symptoms over the same period, and improvements in job strain were associated with symptom decline, supporting a causal rather than purely selection-based interpretation of the demand-control relationship."
    evidence: "longitudinal"
    support_strength: "low-to-moderate"
    outcomes: ["depression", "stress", "mental-health"]
    predictors: ["workload", "autonomy"]
population:
  who: "Employed male workers from two national surveys: the U.S. Quality of Employment Survey 1972 (ages 20-65) and the Swedish Level of Living Survey 1968 and 1974 (ages 18-66); analysis restricted to men only."
  where: ["United States", "Sweden"]
  when: "1968-1974"
  n: 1926
  sector: ["cross-industry"]
  sample_notes: >
    Two nationally representative surveys: U.S. stratified housing-unit sample (76% response
    rate, N approx. 911-950); Swedish random population sample (85-92% response rates, N
    approx. 1,896-1,926, longitudinal with re-interview in 1974). Analysis excludes women
    because the author judged that work-housework interaction complicated the model for
    female workers; this materially limits generalizability.
limitation:
  primary: "The analysis is restricted entirely to male workers, so the model's applicability to women (a stated but untested exclusion) is unknown."
  others:
    - "Job demands and decision latitude measures are broad composite scales that cannot distinguish specific types of demand or discretion (e.g., time pacing vs. skill use vs. policy influence)."
    - "The core test is cross-sectional; although a longitudinal Swedish subsample strengthens causal inference, most reported associations (U.S. data, Table 2/3) remain correlational and rely on self-reported symptoms."
    - "The model does not address social relations at the work-group or organizational level, only individual-level job content."
risk_of_bias: "medium"
relevance_to_project: >
  This is the foundational statement of the job demand-control (Karasek) model, which
  underlies how the SNH project should think about workload and autonomy as joint predictors
  of burnout, exhaustion, and dissatisfaction rather than as independent factors -- directly
  informing design choices around giving remote workers decision latitude/autonomy as a
  buffer against high-demand periods rather than only reducing workload itself.
tags:
  topic: ["burnout", "wellbeing", "job-satisfaction", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["male-workers", "cross-national"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Robert A. Karasek-JobDemandsJob-1979/Robert A. Karasek-JobDemandsJob-1979.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Robert A. Karasek-JobDemandsJob-1979.pdf"
  notes: null

---

id: "rothbard-2001-enriching-or-depleting-the-dynamics-of"
title: "Enriching or Depleting? The Dynamics of Engagement in Work and Family Roles"
authors:
  - "Rothbard, Nancy P."
year: 2001
doi: "10.2307/3094827"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 46, issue: 4, pages: "655-684"}
citation: "Rothbard (2001). Enriching or Depleting? The Dynamics of Engagement in Work and Family Roles. Administrative Science Quarterly, 46(4), 655-684. https://doi.org/10.2307/3094827"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using structural equation modeling on survey data from 790 university employees, this
  study tests a non-recursive model in which engagement (attention plus absorption) in work
  and family roles produces emotional responses that in turn spill over to affect engagement
  in the other role. It finds evidence for both depletion and enrichment, but the pattern is
  highly conditional on gender and direction: depletion ran only from work to family and
  only for women, while enrichment ran from work to family for men but from family to work
  for women, and overall far more work-family linkages existed for women than for men.
claims:
  - text: "Depletion (negative affect from one role reducing engagement in the other) was supported only in the work-to-family direction and only for women: for women, work negative affect significantly decreased family attention (β = -.27), whereas for men the same path was null (β = .01); no evidence of depletion existed in the family-to-work direction for either gender."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["loneliness", "boundary-management"]
  - text: "Enrichment (positive affect from one role increasing engagement in the other) was asymmetric by gender and direction: for men, work positive affect increased family attention (β = .17) but was unrelated for women (β = -.06); for women, family positive affect increased work absorption (β = .28, full-sample β = .19) but was unrelated for men (β = .00)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "work-life-balance"]
    predictors: ["sense-of-belonging", "boundary-management"]
  - text: "Women showed a compensation pattern rather than depletion from family to work: family negative affect was positively associated with work absorption for women (β = .14) but unrelated for men (β = .04), and overall many more significant work-family linkages emerged for women than for men, limiting the model's generalizability across gender."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management", "workload"]
population:
  who: "Employees at a large U.S. public university, stratified by age, gender, and job type (professional/administrative, clerical, faculty, hospital staff, nurses, maintenance, and other roles)"
  where: ["United States"]
  when: "January 1998"
  n: 790
  sector: ["higher-education", "mixed-occupational"]
  sample_notes: >
    Mailed survey to 1,310 employees; 790 returned (about 60% response rate); final analytic
    sample N=684 after listwise handling. Sample skewed female (68% vs. 58% in initial
    sampling frame) and 90% Caucasian; single-organization design limits generalizability to
    other employers or to a fully gender-balanced workforce.
limitation:
  primary: "Cross-sectional self-report data used to test a reciprocal (non-recursive) causal model, so the directional work→family and family→work paths are inferred via instrumental variables rather than observed over time."
  others:
    - "Single-organization (one university) sample with long tenure and presumably high job security/flexibility, which may underrepresent depletion relative to other, less flexible workplaces."
    - "All measures are self-report from the same respondents, raising common-method-variance concerns, though the authors argue the divergent attention/absorption findings and high scale reliabilities mitigate this."
    - "Strong gender asymmetries mean the overall model fits women's experience better than men's, limiting generalizability of a single unified model across genders."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a theoretically grounded, emotion-based mechanism (positive/negative affect as
  the link between attention+absorption in one role and engagement in another) that the SNH
  project can borrow when modeling how remote workers' emotional spillover between work and
  home/community roles drives disengagement or renewed engagement, and it flags gender as a
  key moderator to check for in remote-work social-health measurement.
tags:
  topic: ["work-life-balance", "wellbeing", "job-engagement"]
  method: ["survey", "cross-sectional"]
  population: ["higher-education", "mixed-occupational"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/rothbard-2001-enriching-or-depleting-the-dynamics-of-engagement-in-work-and-family-roles/rothbard-2001-enriching-or-depleting-the-dynamics-of-engagement-in-work-and-family-roles.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/rothbard-2001-enriching-or-depleting-the-dynamics-of-engagement-in-work-and-family-roles.pdf"
  notes: null

---

id: "ryan-2000-self-determination-theory-and-the-facilitation"
title: "Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being."
authors:
  - "Ryan, Richard M."
  - "Deci, Edward L."
year: 2000
doi: "10.1037//0003-066x.55.1.68"
venue: {type: "journal", name: "American Psychologist", volume: 55, issue: 1, pages: "68-78"}
citation: "Ryan et al. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.. American Psychologist, 55(1), 68-78. https://doi.org/10.1037//0003-066x.55.1.68"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "strong", preregistered: false}
gist: >
  This is the canonical statement of self-determination theory (SDT), synthesizing decades
  of experimental and field research to argue that human motivation, self-regulation, and
  well-being depend on satisfaction of three innate psychological needs: competence,
  autonomy, and relatedness. It integrates cognitive evaluation theory (conditions that
  support versus undermine intrinsic motivation) and organismic integration theory (how
  extrinsically motivated behavior is internalized along a continuum from amotivation to
  fully integrated regulation), and shows that thwarting these needs produces alienation,
  diminished motivation, and psychopathology across domains including work, education,
  health care, and sport. It closes by arguing that basic-need support is a general
  principle for designing social environments that optimize performance and well-being.
claims:
  - text: "Employees' reported satisfaction of the needs for autonomy, competence, and relatedness in the workplace predicted both their job performance and their well-being (Baard, Deci, & Ryan, 1998)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "wellbeing"]
    predictors: ["autonomy", "sense-of-belonging"]
  - text: "Placing strong relative importance on intrinsic aspirations (affiliation, personal growth, community) was positively associated with well-being indicators (self-esteem, self-actualization, lower depression and anxiety), whereas emphasis on extrinsic aspirations (wealth, fame, image) was negatively related to these indicators; the pattern replicated in a Russian sample, and attainment of extrinsic goals conferred little well-being benefit in a longitudinal study (Sheldon & Kasser, 1998)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "depression", "anxiety"]
    predictors: ["intrinsic-aspirations"]
  - text: "Within-person daily fluctuations in satisfaction of the autonomy and competence needs predicted within-person fluctuations in mood, vitality, physical symptoms, and self-esteem (Sheldon, Reis, & Ryan, 1996), and independent daily variation in all three basic needs (autonomy, competence, relatedness) predicted daily well-being (Reis et al., in press)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing", "stress"]
    predictors: ["autonomy", "sense-of-belonging"]
population:
  who: "No single sample: a narrative theoretical synthesis drawing on the authors' program of experimental, field, and survey studies spanning children, students, employees, patients, nursing-home residents, and athletes."
  where: ["United States", "Russia"]
  when: null
  n: null
  sector: ["education", "healthcare", "workplace-general"]
  sample_notes: >
    This is a review/theory article, not a primary study with its own sample; cited studies
    vary widely in design (lab experiments, field surveys, daily-diary designs) and rigor,
    and several are cited as unpublished manuscripts or in-press works current to the year
    2000.
limitation:
  primary: "As a narrative theoretical review rather than a single empirical study, the paper aggregates findings from many disparate studies chosen to illustrate SDT's three-need framework, without formal systematic-review or meta-analytic methodology applied across the whole body of evidence it cites."
  others:
    - "Much of the underlying evidence base is laboratory experiments on intrinsic motivation, which may not generalize directly to complex real-world remote-work or online-community settings."
    - "Some cited supporting studies (e.g., Baard, Deci, & Ryan, 1998) were unpublished manuscripts at time of citation."
risk_of_bias: "medium"
relevance_to_project: >
  SDT's three basic needs (autonomy, competence, and especially relatedness/belonging)
  supply the SNH project's core mechanism for why social connection at work and in
  communities drives motivation, engagement, and well-being, and why thwarting relatedness
  (isolation, controlling management, lack of autonomy support) produces alienation and
  burnout; the paper is the foundational citation for using 'autonomy' and 'sense-of-
  belonging' as predictors in the corpus vocabulary.
tags:
  topic: ["wellbeing", "mental-health", "job-engagement", "burnout", "psychological-safety"]
  method: ["theory", "experiment"]
  population: ["students", "employees", "general-population"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Ryan & Deci (2000) - Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being/Ryan & Deci (2000) - Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Ryan & Deci (2000) - Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being.pdf"
  notes: null

---

id: "milliken-1996-searching-for-common-threads-understanding-the"
title: "Searching for Common Threads: Understanding the Multiple Effects of Diversity in Organizational Groups"
authors:
  - "Milliken, Frances J."
  - "Martins, Luis L."
year: 1996
doi: "10.2307/258667"
venue: {type: "journal", name: "The Academy of Management Review", volume: 21, issue: 2, pages: "402"}
citation: "Milliken et al. (1996). Searching for Common Threads: Understanding the Multiple Effects of Diversity in Organizational Groups. The Academy of Management Review, 21(2), 402. https://doi.org/10.2307/258667"
article_type: "review"
method: {design: "review-scoping", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Milliken and Martins (1996) synthesize 34 empirical management studies (1989-1994) on how
  diversity in group composition -- race/ethnicity, gender, age, tenure, education,
  functional and occupational background -- affects individual, group, and organizational
  outcomes at the board, top-management-team, and task-group levels. They argue diversity
  operates through four mediating processes (affective, cognitive, communication, symbolic)
  and find a consistent pattern: diversity on observable, demographic attributes tends to
  depress social integration, satisfaction, and retention while diversity on underlying,
  skill-based attributes tends to produce cognitive/innovation benefits at some coordination
  cost. The paper proposes an integrative model and names a systemic 'tendency of groups and
  organizations to drive out diversity' unless actively managed.
claims:
  - text: "Across studies of race, gender, and age diversity, individuals who differ from the majority of their work unit or supervisor consistently show lower psychological commitment, higher absenteeism, higher turnover intentions/turnover, and lower supervisor-rated performance (e.g., Tsui, Egan, & O'Reilly, 1992; Cummings, Zhou, & Oldham, 1993; O'Reilly, Caldwell, & Barnett, 1989)."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["turnover", "retention", "job-satisfaction"]
    predictors: ["team-cohesion", "organizational-culture"]
  - text: "Diversity in skill-based attributes (education, functional background, occupational background) is associated with cognitive/performance benefits for top management teams and project teams -- e.g., greater administrative innovation, more frequent external communication, and higher ROI/sales growth in some samples -- but also with larger 'process losses' and reduced social integration in others (Ancona & Caldwell, 1992; Bantel & Jackson, 1989; Smith et al., 1994)."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "collaboration", "communication"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Diversity in organizational/group tenure is linked to lower social integration and higher turnover (O'Reilly et al., 1989; Wagner, Pfeffer, & O'Reilly, 1984), but a longitudinal lab study (Watson, Kumar, & Michaelsen, 1993) found the negative affective/performance gap between homogeneous and diverse groups narrowed and reversed on some measures after the group had worked together for several time periods."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["turnover", "sense-of-belonging"]
    predictors: ["team-cohesion", "sense-of-belonging"]
population:
  who: "34 empirical management studies (1989-1994) examining diversity effects on boards of directors, top management teams, and organizational task groups/dyads; underlying samples range from small lab groups of undergraduates to tens of thousands of rater-ratee pairs in military and corporate settings"
  where: ["United States", "Netherlands", "Australia", "Japan"]
  when: "1989-1994 (studies reviewed); published 1996"
  n: null
  sector: []
  sample_notes: >
    This is a narrative literature review, not a primary study, so there is no single
    sample; included studies span banking, oil and food industries, law firms, government
    offices, hospitals, manufacturing, and military settings, drawn from 13 management
    journals plus snowball-sampled citations. The authors state it is not an exhaustive
    review and note some diversity types (e.g., functional diversity and affective/turnover
    outcomes) had no studies at all as of the review date.
limitation:
  primary: "It is a narrative (non-systematic) review with no formal search protocol, quality appraisal, or meta-analytic pooling of effect sizes, so the 'common threads' identified are qualitative syntheses that mix study designs, measures, and levels of analysis (individual, dyad, group, organization) of varying rigor."
  others:
    - "Most underlying studies are US samples studied in a societal context where white men are the traditional majority group, limiting generalizability of findings (e.g., about which groups diversity harms most) to other cultural contexts."
    - "Findings for several diversity types (e.g., functional background and affective/turnover outcomes, personality/values diversity) rest on only one or two underlying studies, so 'consistent patterns' claimed for those areas are thin."
    - "The review cannot separate whether effects attributed to observable attributes (race, gender) are driven by those attributes themselves or by correlated underlying attributes (values, socioeconomic background) -- a confound the authors themselves flag as unresolved."
risk_of_bias: "medium"
relevance_to_project: >
  This foundational review supplies the SNH project's mechanism-level vocabulary for how
  team/organizational composition affects turnover, social integration, and belonging --
  directly relevant to designing distributed and open-source teams where demographic and
  tenure heterogeneity (e.g., newcomers, geographically dispersed contributors) could
  trigger the same 'drive out diversity' dynamic via reduced social integration, and to the
  finding that negative affective costs of diversity can attenuate with sustained group
  tenure, suggesting onboarding/retention interventions should target early-tenure
  integration specifically.
tags:
  topic: ["collaboration", "job-satisfaction", "methodology"]
  method: ["review-scoping", "analytical"]
  population: ["organizational-groups", "top-management-teams", "task-groups"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Searching for Common Threads_ Understanding the Multiple Effects of Diversity in Organizational Groups/Searching for Common Threads_ Understanding the Multiple Effects of Diversity in Organizational Groups.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Searching for Common Threads_ Understanding the Multiple Effects of Diversity in Organizational Groups.pdf"
  notes: null

---

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

---

id: "sherony-2002-coworker-exchange-relationships-between-coworkers-leader"
title: "Coworker exchange: Relationships between coworkers, leader-member exchange, and work attitudes."
authors:
  - "Sherony, Kathryn M."
  - "Green, Stephen G."
year: 2002
doi: "10.1037/0021-9010.87.3.542"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 87, issue: 3, pages: "542-548"}
citation: "Sherony et al. (2002). Coworker exchange: Relationships between coworkers, leader-member exchange, and work attitudes.. Journal of Applied Psychology, 87(3), 542-548. https://doi.org/10.1037/0021-9010.87.3.542"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Surveying 110 coworker dyads at two U.S. organizations, this study finds that the
  similarity of two coworkers' leader-member exchange (LMX) relationships with their shared
  supervisor predicts the quality of their coworker exchange (CWX) relationship with each
  other, consistent with balance theory. It also finds that, controlling for LMX, greater
  diversity in an employee's CWX relationships across coworkers is associated with lower
  organizational commitment (but not lower job satisfaction), suggesting that unevenness in
  peer relationship quality, not just average quality, carries an attitudinal cost.
claims:
  - text: "The interaction of two coworkers' LMX scores with their shared supervisor significantly predicted the quality of their dyadic coworker exchange (CWX): overall model F(3,106)=6.54, p<.001, adjusted R2=.13, with a significant LMX interaction term (standardized coefficient=1.42, p=.04); CWX was highest when both coworkers had similarly high or similarly low LMX with the supervisor."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "sense-of-belonging"]
    predictors: ["leadership-style", "network-structure", "team-cohesion"]
  - text: "After controlling for LMX, greater diversity (coefficient of variation) in an employee's coworker-exchange relationships was negatively related to organizational commitment (standardized coefficient=-0.31, p<.01) but was not significantly related to job satisfaction, in a regression using 66 employees who rated multiple coworkers."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["retention", "job-satisfaction"]
    predictors: ["social-support", "team-cohesion"]
  - text: "Contrary to Hypothesis 3, the interaction of average CWX quality and CWX diversity did not significantly predict either job satisfaction (standardized coefficient=-1.00, ns) or organizational commitment (standardized coefficient=-0.21, ns), indicating overall average CWX level did not moderate the diversity effect on work attitudes."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction", "retention"]
    predictors: ["team-cohesion", "social-support"]
population:
  who: "Employees in work groups of 3-9 reporting to the same manager at a Chicago-area engineering company and a health services facility in eastern Iowa; analyses used 110 complete coworker dyads drawn from 67 usable respondents (of 69 returned surveys)."
  where: ["United States"]
  when: "data collected circa 2000-2001 (published 2002)"
  n: 110
  sector: ["engineering", "healthcare"]
  sample_notes: >
    63.3% survey response rate (69 of ~109 employees), with 67 usable responses yielding 110
    complete dyads (95% of original work groups represented); nonrespondents were rated by
    coworkers as having significantly lower-quality CWX relationships than respondents
    (M=3.28 vs 3.57, p<.05), a documented response bias; work-attitude analyses used a
    smaller subsample of 66 employees who rated multiple coworkers.
limitation:
  primary: "CWX, LMX, and work-attitude measures were all same-source self-reports collected in a single survey, raising common-method/same-source bias concerns for the observed associations."
  others:
    - "Small sample size (110 dyads; only 66 employees in the work-attitude/diversity analyses) limited statistical power, particularly for the null Hypothesis 3 test."
    - "Respondents had significantly higher-quality coworker relationships than nonrespondents, so results may not generalize to less-engaged employees."
    - "Job satisfaction was measured with a single-item scale, which may have restricted the ability to detect effects on that outcome."
risk_of_bias: "medium"
relevance_to_project: >
  Offers early dyadic-level evidence that peer (coworker) relationship quality is partly a
  structural byproduct of each person's relationship with a shared leader, and that
  diversity/unevenness in an employee's coworker relationships independently predicts
  organizational commitment even after controlling for leader-relationship quality. This is
  directly useful for the SNH project's thinking about how network structure and variance in
  relationship quality across a person's ties (not just average support level) shape
  belonging and retention outcomes, distinct from isolation per se.
tags:
  topic: ["collaboration", "community-health", "job-satisfaction", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["office-workers", "healthcare-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Sherony & Green (2002) - Coworker Exchange - Relationships Between Coworkers, Leader-Member Exchange, and Work Attitudes/Sherony & Green (2002) - Coworker Exchange - Relationships Between Coworkers, Leader-Member Exchange, and Work Attitudes.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Sherony & Green (2002) - Coworker Exchange - Relationships Between Coworkers, Leader-Member Exchange, and Work Attitudes.pdf"
  notes: null

---

id: "bednar-2020-socio-technical-perspectives-on-smart-working"
title: "Socio-Technical Perspectives on Smart Working: Creating Meaningful and Sustainable Systems"
authors:
  - "Bednar, Peter M."
  - "Welch, Christine"
year: 2020
doi: "10.1007/s10796-019-09921-1"
venue: {type: "journal", name: "Information Systems Frontiers", volume: 22, issue: 2, pages: "281-298"}
citation: "Bednar et al. (2020). Socio-Technical Perspectives on Smart Working: Creating Meaningful and Sustainable Systems. Information Systems Frontiers, 22(2), 281-298. https://doi.org/10.1007/s10796-019-09921-1"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  This conceptual paper argues that 'smart working' (framed against a shift from Industry
  4.0 to Industry 5.0) is being pursued in two contradictory modes: a coercive, efficiency-
  driven mode exemplified by Amazon's patented warehouse tracking bracelet, and a genuinely
  socio-technical mode that attends to individual sense-making, contextual dependencies, and
  employee desire-for-use. The authors contend that sustainable, meaningful smart-work
  systems require human-centred, second-order socio-technical design rather than technology-
  first implementation or top-down 'best practice' benchmarking, and reframe the manager's
  role from 'architect of context' to 'cultivator' of conditions for employee-driven job
  crafting and collaboration.
claims:
  - text: "The paper documents that Amazon's staff-worn warehouse bracelet is publicly described by the company as freeing employees' hands and saving time, but its registered US patent describes its purpose as 'radio frequency-based tracking of a worker's hands to monitor performance of inventory tasks,' illustrating a coercive rather than empowering application of smart-working technology."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["wellbeing", "stress"]
    predictors: ["leadership-style", "organizational-culture"]
  - text: "The paper argues that proponents of smart working acknowledge employees may experience increased isolation under distributed/mobile work arrangements, while claiming (without strong substantiation, per the authors) that collaborative and mobile technologies can offset this by supporting team-working and innovation."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["isolation", "collaboration"]
    predictors: ["remote-work-intensity", "team-cohesion"]
  - text: "Drawing on socio-technical systems theory (Checkland; Bednar and Welch), the paper contends that top-down 'best practice' standardization (e.g., the UK Government's Smart Working Code of Practice) creates an internal paradox with stated aims of flexibility and empowerment, and that sustainable design instead requires supporting individual 'desire-for-use,' job crafting, and contextual sense-making."
    evidence: "theory"
    support_strength: "speculative"
    outcomes: ["job-satisfaction", "job-engagement"]
    predictors: ["autonomy", "organizational-culture"]
population:
  who: "Not an empirical sample; this is a conceptual/theoretical essay that draws on secondary literature and illustrative case vignettes (Amazon's warehouse tracking bracelet patent, the UK Automobile Association's outsourcing restructuring, Indian smart energy grid policy, and a fashion company case labelled 'Alfa') plus CIPD and UK Government policy reports to build a socio-technical argument about 'smart working' under Industry 4.0/5.0."
  where: ["UK", "India"]
  when: null
  n: null
  sector: ["technology", "manufacturing"]
  sample_notes: >
    No primary data collection; illustrative cases are hand-selected to support the argument
    rather than systematically sampled or reviewed.
limitation:
  primary: "The paper is a conceptual/theoretical essay with no primary data collection or systematic evidence review; claims about employee isolation, sense-making, and organizational outcomes are asserted through selectively chosen illustrative anecdotes and literature synthesis rather than tested empirically."
  others:
    - "Illustrative case examples (Amazon bracelet, UK AA restructuring, Indian smart grids, the 'Alfa' fashion company) are not systematically sampled and may be cherry-picked to fit the authors' pre-existing socio-technical framework."
    - "The proposed contemporary socio-technical design approach (summarized in Fig. 2) is not operationalized or empirically tested for its effect on sustainability, wellbeing, or performance outcomes."
risk_of_bias: "high"
relevance_to_project: >
  Offers a socio-technical design lens for evaluating remote/smart-work technology choices
  in terms of whether they support employee autonomy, sense-making, and collaboration
  (contrasted with coercive monitoring tools like the Amazon bracelet), which is directly
  relevant to SNH's question of how tooling and management design for distributed teams
  shape isolation and engagement, not just productivity. It also names the isolation-versus-
  connectivity trade-off in remote/mobile work as an under-substantiated claim that the SNH
  project could test more rigorously.
tags:
  topic: ["remote-work", "collaboration", "wellbeing", "isolation", "job-satisfaction", "technostress"]
  method: ["theory", "case-study"]
  population: ["knowledge-workers", "manufacturing"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Socio-Technical Perspectives on Smart Working_ Creating Meaningful and Sustainable Systems/Socio-Technical Perspectives on Smart Working_ Creating Meaningful and Sustainable Systems.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Socio-Technical Perspectives on Smart Working_ Creating Meaningful and Sustainable Systems.pdf"
  notes: null

---

id: "sonnentag-2007-the-recovery-experience-questionnaire-development-and"
title: "The Recovery Experience Questionnaire: Development and validation of a measure for assessing recuperation and unwinding from work."
authors:
  - "Sonnentag, Sabine"
  - "Fritz, Charlotte"
year: 2007
doi: "10.1037/1076-8998.12.3.204"
venue: {type: "journal", name: "Journal of Occupational Health Psychology", volume: 12, issue: 3, pages: "204-221"}
citation: "Sonnentag et al. (2007). The Recovery Experience Questionnaire: Development and validation of a measure for assessing recuperation and unwinding from work.. Journal of Occupational Health Psychology, 12(3), 204-221. https://doi.org/10.1037/1076-8998.12.3.204"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This paper develops and validates the Recovery Experience Questionnaire, showing via
  confirmatory factor analysis across three studies (total N=991, calibration and cross-
  validation subsamples) that off-job recovery from work stress is best captured by four
  distinct experiences: psychological detachment, relaxation, mastery, and control. In a
  nomological-net study (N=271), job stressors (especially time pressure) were negatively
  related to detachment, relaxation, and control, and all four recovery experiences
  correlated with better psychological well-being (fewer health complaints, less emotional
  exhaustion, higher life satisfaction), with psychological detachment showing the strongest
  links to impaired well-being. It contributes a short, reliable 16-item measurement tool
  for the underlying mechanisms by which time off work restores wellbeing.
claims:
  - text: "Confirmatory factor analysis supported a four-factor structure of recovery experiences (psychological detachment, relaxation, mastery, control) over one-, two-, and three-factor alternatives, with acceptable fit in both calibration (chi2=317.15, df=98, CFI=.97, RMSEA=.069) and cross-validation samples (chi2=403.60, df=98, CFI=.96, RMSEA=.082); the resulting 16-item scales had good internal consistency (alphas .79-.85)."
    evidence: "cross-sectional"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "Job stressors were negatively related to recovery experiences: time pressure was negatively related to psychological detachment, relaxation, and control (but not mastery); role ambiguity and situational constraints were negatively related to detachment and control; hours of overtime were negatively related to detachment and relaxation."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress"]
    predictors: ["workload", "technostress"]
  - text: "Recovery experiences were negatively related to indicators of impaired well-being (health complaints, emotional exhaustion, depressive symptoms, need for recovery, sleep problems) and positively related to life satisfaction; psychological detachment and control showed the strongest associations, while correlations of recovery experiences with coping style and personality (except emotional stability) were generally low and non-significant."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "burnout", "job-satisfaction"]
    predictors: ["boundary-management", "workload"]
population:
  who: "Employees from a broad range of German public and private-sector organizations (public administration, schools, call centers, hospitals, nursing homes, retail, insurance, etc.); Study 2 full sample and Study 3 nomological-net subsamples drawn from this pool"
  where: ["Germany"]
  when: null
  n: 991
  sector: ["public-administration", "education", "healthcare", "service"]
  sample_notes: >
    Study 2: 1409 contacted by mail plus 420 contacted in person; 991 questionnaires
    returned (54.6% overall response rate), randomly split into calibration and cross-
    validation subsamples of N=465 each after listwise deletion for missing data. Study 3
    nomological-net subsamples were smaller (N=134 and N=137, mostly local public
    administration employees) and did not cover all predictor/outcome variables in both
    subsamples, limiting power for the coping and personality analyses. Sample was 71%
    women, mean age 38.3 (SD 12.3).
limitation:
  primary: "All data are cross-sectional self-report, so no causal inferences can be drawn about the direction of relations between job stressors, recovery experiences, and well-being."
  others:
    - "The four recovery experiences may not capture all relevant dimensions (e.g., positive affective valence or social connectedness during off-job time were not included as separate constructs)."
    - "Study 3 nomological-net subsamples were relatively small (N=134, N=137), so non-significant correlations (e.g., for coping and personality) should be interpreted cautiously."
    - "Relaxation and control latent factors were highly correlated (r as high as .71), raising some question about their discriminant validity despite fit statistics favoring a four-factor model."
risk_of_bias: "low"
relevance_to_project: >
  Provides a short, validated, reusable measurement instrument (the RECQ) for the specific
  off-job mechanisms — psychological detachment, relaxation, mastery, control — through
  which remote/hybrid workers recover from job stressors and protect wellbeing; directly
  usable for SNH surveys or diary studies assessing boundary-management and recovery as
  levers against burnout and technostress from job stressors like time pressure and
  overtime.
tags:
  topic: ["wellbeing", "burnout", "measurement", "work-life-balance", "technostress"]
  method: ["survey", "cross-sectional"]
  population: ["remote-work", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Sonnentag & Fritz (2007) - The Recovery Experience Questionnaire - Development and Validation/Sonnentag & Fritz (2007) - The Recovery Experience Questionnaire - Development and Validation.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Sonnentag & Fritz (2007) - The Recovery Experience Questionnaire - Development and Validation.pdf"
  notes: null

---

id: "sorge-1983-culture-s-consequences-international-differences-in"
title: "Culture's Consequences: International Differences in Work-Related Values."
authors:
  - "Sorge, Arndt"
  - "Hofstede, Geert"
year: 1983
doi: "10.2307/2393017"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 28, issue: 4, pages: "625"}
citation: "Sorge et al. (1983). Culture's Consequences: International Differences in Work-Related Values.. Administrative Science Quarterly, 28(4), 625. https://doi.org/10.2307/2393017"
article_type: "commentary"
method: {design: "book-review", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  This is Arndt Sorge's 1983 Administrative Science Quarterly book review of Geert
  Hofstede's Culture's Consequences (1980), which analyzed roughly 116,000 employee
  questionnaires from a single multinational corporation ('HERMES') across 40 countries in
  1968 and 1972 to derive four dimensions of national culture: power distance, uncertainty
  avoidance, individualism, and masculinity. Sorge praises the book's data richness and its
  integrated cross-dimension cluster analysis of national/organizational fit, but warns that
  Hofstede's chapter-ending correlations with national statistics (health, crime, climate)
  overreach the data, and that concepts like uncertainty avoidance conflate distinct
  constructs while resting on one company's non-representative national samples.
claims:
  - text: "Hofstede's study distributed approximately 116,000 questionnaires to employees of one multinational company in 40 countries, collected around 1968 and again around 1972, yielding four derived dimensions of national culture: power distance, uncertainty avoidance, individualism, and masculinity."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture"]
  - text: "The reviewer argues that country-level cultural scores are confounded by the representativeness problem: employees of one company (HERMES) in each country may be a non-comparable selection relative to the national population, and the company's personnel policy may itself vary by country."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["collaboration"]
    predictors: ["sampling-method", "organizational-culture"]
  - text: "The reviewer identifies chapter 7's integrated analysis combining two cultural dimensions simultaneously (e.g., uncertainty avoidance x power distance, producing clusters of cultural affinity linked to management style) as the book's most convincing contribution, in contrast to the more speculative single-dimension chapter conclusions correlating culture scores with national health, crime, and climate statistics."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["collaboration"]
    predictors: ["organizational-culture", "network-structure"]
population:
  who: "Not a primary study population; the reviewed book's sample was employees of one undisclosed multinational corporation ('HERMES', widely understood to be IBM) surveyed in 40 countries."
  where: ["multiple countries (40, unspecified in the review)"]
  when: "Underlying survey data collected circa 1968 and circa 1972; review published 1983"
  n: 116000
  sector: ["corporate"]
  sample_notes: >
    This document is a book review, not a primary study; N and sample details refer to the
    reviewed book (Hofstede 1980), and the reviewer himself flags that the single-company
    sample may not be representative of each country's general population or workforce.
limitation:
  primary: "This document is a secondary commentary (a book review), not original empirical research, so its 'findings' are the reviewer's critical assessment of another author's work rather than new data."
  others:
    - "The review itself provides no quantitative detail beyond what it reports from Hofstede's book, limiting its independent evidentiary value."
    - "The markdown conversion bundles fragments of two adjacent, unrelated book reviews (one on labor-market discrimination, one beginning on Industrial Democracy in Europe) around the core Hofstede review, which could cause misattribution if read out of context."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is background commentary on Hofstede's cross-national culture dimensions (power
  distance, individualism, uncertainty avoidance) rather than SNH-specific evidence; it is
  only tangentially useful for the project as historical context if cross-cultural or cross-
  national comparisons of remote/distributed teams are ever needed, and should not be cited
  as direct evidence on isolation, loneliness, or burnout.
tags:
  topic: ["methodology", "measurement"]
  method: ["review", "secondary-data"]
  population: ["corporate-employees", "multinational"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Sorge-AdministrativeScienceQuarterly-1983/Sorge-AdministrativeScienceQuarterly-1983.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Sorge-AdministrativeScienceQuarterly-1983.pdf"
  notes: null

---

id: "spector-2006-method-variance-in-organizational-research"
title: "Method Variance in Organizational Research"
authors:
  - "Spector, Paul E."
year: 2006
doi: "10.1177/1094428105284955"
venue: {type: "journal", name: "Organizational Research Methods", volume: 9, issue: 2, pages: "221-232"}
citation: "Spector (2006). Method Variance in Organizational Research. Organizational Research Methods, 9(2), 221-232. https://doi.org/10.1177/1094428105284955"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Spector argues that common method variance (CMV) -- the widely accepted claim that
  correlations among variables measured with the same self-report survey are automatically
  inflated -- is a 'methodological urban legend' rather than an established empirical fact.
  Reviewing meta-analyses and monomethod-versus-multimethod comparisons, he shows that
  candidate biasing variables (social desirability, negative affectivity, acquiescence)
  produce only small, inconsistent, construct-specific correlation distortion rather than a
  universal method-driven inflation, and he recommends abandoning the term CMV in favor of
  construct-specific analysis of measurement bias plus targeted design and statistical
  controls.
claims:
  - text: "In Boswell, Boudreau, and Dunford's (2004) study of 5 self-report turnover-process variables from the same questionnaire (n = 1,601), 4 of 10 (40%) correlations among the variables were nonsignificant and the largest significant correlation was only .20, despite power sufficient to detect correlations as small as .07 -- contradicting the assumption that CMV automatically produces a baseline of inflated correlations among monomethod self-report measures."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover", "job-satisfaction"]
    predictors: ["sampling-method"]
  - text: "Moorman and Podsakoff's (1992) meta-analysis of 36 samples (33 studies) linking social desirability to nine organizational variables found a mean correlation of only .05 (range .01-.17), with four of nine confidence intervals including zero, and a follow-up study found most partial correlations controlling for social desirability differed from zero-order correlations by no more than .02-.04 -- indicating social desirability is not a universal source of correlation inflation."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["sampling-method", "social-desirability-bias"]
  - text: "Crampton and Wagner's (1994) analysis of over 40,000 correlations from 581 articles, comparing 143 monomethod versus multimethod variable-pair correlations, found monomethod correlations were significantly higher in only 26.6% of cases, lower in 11.2%, and not significantly different in 62.2% of cases, refuting the idea that using a single method (e.g., self-report) universally inflates observed relationships."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "performance"]
    predictors: ["sampling-method"]
population:
  who: "Not an original empirical sample; a critical synthesis of prior organizational-research studies and meta-analyses on method variance, including Boswell et al. (2004, n=1,601), Moorman & Podsakoff (1992, 36 samples/33 studies), Ones et al. (1996), and Crampton & Wagner (1994, 581 articles)."
  where: []
  when: "Literature reviewed spans 1959-2004"
  n: null
  sector: []
  sample_notes: >
    This is a conceptual/methodological essay (an invited AOM conference paper expanded into
    a journal article), not a primary data collection; the 'sample' is the set of prior
    published organizational-behavior studies and meta-analyses the author re-analyzes and
    cites as evidence.
limitation:
  primary: "As a narrative argumentative essay rather than a systematic or pre-registered review, the selection and emphasis of supporting studies is not governed by a transparent, replicable search protocol and may be susceptible to the author's own confirmation bias against the CMV consensus he is critiquing."
  others:
    - "Relies heavily on comparisons between monomethod and multimethod (or partialled) correlations as evidence of 'no bias,' but the author himself notes multimethod data are not necessarily more valid, so absence of inflation could reflect attenuation in the comparison method rather than absence of CMV."
    - "Focuses on a narrow set of candidate biasing variables (social desirability, negative affectivity, acquiescence) and organizational-behavior constructs; findings may not generalize to other self-report domains, such as loneliness or social-support scales used in SNH research."
risk_of_bias: "medium"
relevance_to_project: >
  SNH research leans heavily on single-occasion self-report surveys of loneliness,
  isolation, social support, burnout, and job satisfaction; this paper is directly relevant
  evidence for whether such monomethod self-report findings should be discounted as
  automatically inflated by common method variance, and supports treating bias risk on a
  construct-by-construct basis (with targeted design/statistical controls) rather than
  dismissing SNH self-report findings wholesale.
tags:
  topic: ["methodology", "measurement", "job-satisfaction"]
  method: ["theory", "secondary-data"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/spector-2006-method-variance-in-organizational-research-truth-or-urban-legend.pdf"
  notes: null

---

id: "hooper-2008-structural-equation-modelling-guidelines-for-determining"
title: "Structural Equation Modelling: Guidelines for Determining Model Fit"
authors:
  - "Hooper, Daire"
  - "Coughlan, Joseph"
  - "Mullen, Michael R."
year: 2008
doi: null
venue: {type: "journal", name: "The Electronic Journal of Business Research Methods, 6(1), 53-60", volume: null, issue: null, pages: null}
citation: "Hooper et al. (2008). Structural Equation Modelling: Guidelines for Determining Model Fit. The Electronic Journal of Business Research Methods, 6(1), 53-60."
article_type: "methods"
method: {design: "review-scoping", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methods paper synthesizes decades of statistical debate on how to assess model fit in
  structural equation modelling (SEM), reviewing absolute, incremental, and parsimony fit
  indices (chi-square, RMSEA, GFI/AGFI, SRMR, NFI/NNFI, CFI, PGFI/PNFI). It converges on a
  concrete reporting recommendation -- always report the chi-square statistic with df and p,
  plus RMSEA with its confidence interval, SRMR, CFI, and one parsimony index -- and warns
  against 'index shopping' for whichever statistic makes a poorly-fitting model look
  acceptable. For the SNH project it functions as a citable methodological standard for any
  quantitative SEM work (e.g. modelling how loneliness, social support, or burnout predict
  turnover) done within or cited by the corpus.
claims:
  - text: "Best-practice reporting for SEM model fit is to include the Chi-Square statistic with its degrees of freedom and p-value, the RMSEA with its confidence interval, the SRMR, the CFI, and one parsimony fit index such as the PNFI, because these are the indices found least sensitive to sample size, model misspecification, and parameter estimates."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["sample-size"]
  - text: "Consensus threshold recommendations from the reviewed literature: RMSEA close to .06 or a stringent upper limit of .07 indicates good fit, SRMR values below .08 are acceptable, and CFI/NNFI values of .95 or greater are indicative of good model fit (Hu and Bentler, 1999)."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["threshold-criteria"]
  - text: "The Model Chi-Square test is highly sensitive to sample size: it nearly always rejects the model when large samples are used, but lacks statistical power to discriminate good from poor fitting models when samples are small, limiting its use as a standalone fit measure."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["model-fit"]
    predictors: ["sampling-method"]
population:
  who: "Not an empirical human-subjects study; it is a methodological synthesis aimed at researchers across the social sciences who use structural equation modelling, drawing on statistics and simulation literature from 1974-2007."
  where: []
  when: null
  n: null
  sector: ["academic-research"]
  sample_notes: >
    No primary data were collected; the paper is a narrative review/synthesis of prior
    statistical and simulation studies on SEM fit indices, so there is no sample, response
    rate, or representativeness to assess.
limitation:
  primary: "As a non-systematic narrative synthesis of the fit-index literature (not a formal systematic or scoping review with a documented search protocol), the selection and weighting of which studies and thresholds to foreground reflects the authors' judgment."
  others:
    - "The paper itself notes that many recommended cut-off values (e.g. for RMSEA, CFI) lack universal consensus and have shifted substantially over time, so the 'guidelines' it distills are contingent rather than fixed statistical facts."
    - "Published in 2008, so it does not reflect SEM fit-index methodology debates from the subsequent 15+ years."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This is a standard methodological reference for judging model fit in structural equation
  modelling; it is relevant to the SNH project as a citable statistical standard whenever
  the corpus's own or cited quantitative studies use SEM to model relationships among
  constructs like loneliness, isolation, social support, burnout, or turnover, so that
  reported fit statistics can be evaluated against consensus thresholds.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-scoping"]
  population: ["researchers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Structural Equation Modelling_ Guidelines for Determining Model F/Structural Equation Modelling_ Guidelines for Determining Model F.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Structural Equation Modelling_ Guidelines for Determining Model F.pdf"
  notes: "no-doi: journal article"

---

id: "charalampous-2019-systematically-reviewing-remote-e-workers-well"
title: "Systematically reviewing remote e-workers’ well-being at work: a multidimensional approach"
authors:
  - "Charalampous, Maria"
  - "Grant, Christine A."
  - "Tramontano, Carlo"
  - "Michailidis, Evie"
year: 2019
doi: "10.1080/1359432x.2018.1541886"
venue: {type: "journal", name: "European Journal of Work and Organizational Psychology", volume: 28, issue: 1, pages: "51-73"}
citation: "Charalampous et al. (2019). Systematically reviewing remote e-workers’ well-being at work: a multidimensional approach. European Journal of Work and Organizational Psychology, 28(1), 51-73. https://doi.org/10.1080/1359432x.2018.1541886"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: true}
gist: >
  This systematic review synthesizes 63 quantitative, qualitative, and mixed-methods studies
  (1995-2017, N=37,553 across single studies) on how remote e-working relates to knowledge
  workers' well-being, organized around a five-dimension model (affective, cognitive,
  social, professional, psychosomatic). It finds the most evidence for affective, social,
  and professional well-being, and comparatively little for cognitive and psychosomatic
  well-being, with social/professional isolation, loss of colleague interaction, and threats
  to career visibility recurring as the main negative findings alongside generally positive
  effects on job satisfaction and autonomy.
claims:
  - text: "Across ten studies examining affective and social well-being together, low social support was linked to worse affective outcomes: extent of working from home increased emotional exhaustion through low social support, and social support depletion under high remote-work intensity was likewise tied to emotional exhaustion, while organizational support reduced social isolation and thereby raised job satisfaction."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction", "isolation"]
    predictors: ["social-support", "remote-work-intensity", "isolation"]
  - text: "The review reports that none of the 63 included studies examined all five well-being dimensions at once, and only 26 examined more than one dimension jointly, with the affective, social, and professional dimensions studied far more often than the cognitive and psychosomatic dimensions -- an evidence gap the authors flag explicitly."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["wellbeing", "isolation"]
    predictors: ["remote-work-intensity"]
  - text: "Qualitative case studies found that remote e-workers frequently felt isolated and 'apart', with established trusted workplace relationships strained by remote arrangements, and that professional isolation was linked in included studies to reduced teleworker job performance and higher turnover intentions unless offset by face-to-face interaction or communication-enhancing technology."
    evidence: "qualitative"
    support_strength: "moderate"
    outcomes: ["isolation", "turnover", "performance"]
    predictors: ["remote-work-intensity", "social-support"]
population:
  who: "63 primary studies (quantitative, qualitative, mixed-methods, plus 3 meta-analyses) of knowledge workers (excluding manual labour, self-employed/freelance, and disabled employees) engaged in remote e-working, published 1995-2017"
  where: ["UK", "US", "Australia", "Germany", "multiple other countries (international representation)"]
  when: "1995-2017 (search executed via PROSPERO-registered protocol from Feb 2016)"
  n: 37553
  sector: ["knowledge-work", "mixed-industry"]
  sample_notes: >
    Systematic search of 7 databases (3082 records) narrowed via PRISMA-P protocol to 63
    eligible studies; quality appraised with the Mixed Methods Appraisal Tool (MMAT), all
    included studies scoring >=50%; narrative synthesis only (meta-analysis not feasible due
    to construct heterogeneity).
limitation:
  primary: "Time-bounded inclusion window (1995-2017, peer-reviewed English-language only) means the synthesis could omit earlier or later relevant evidence and could reach different conclusions if the window shifted."
  others:
    - "Excludes self-employed, freelance, and disabled remote workers, so findings may not generalize to those populations."
    - "No meta-analysis was possible due to heterogeneous well-being operationalizations across studies, limiting quantitative pooling of effect sizes."
    - "Most included primary studies are cross-sectional, constraining causal claims about remote work's effect on well-being dimensions."
risk_of_bias: "low"
relevance_to_project: >
  Directly informs the SNH project's choice of a multidimensional well-being framework
  (affective/cognitive/social/professional/psychosomatic) and its evidence base on remote-
  work isolation: it flags social and professional isolation, loss of informal colleague
  contact, and reduced career visibility as the primary negative mechanisms, and
  organizational/peer social support as the key protective lever -- while also identifying
  cognitive and psychosomatic well-being as under-studied gaps the project's own research
  could target.
tags:
  topic: ["remote-work", "wellbeing", "isolation", "social-support", "job-satisfaction", "methodology"]
  method: ["review-systematic", "secondary-data"]
  population: ["knowledge-workers", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Systematically reviewing remote e-workers  well-being at work  a multidimensional approach/Systematically reviewing remote e-workers  well-being at work  a multidimensional approach.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Systematically reviewing remote e-workers  well-being at work  a multidimensional approach.pdf"
  notes: null

---

id: "ferguson-2024-team-and-communication-impacts-of-remote"
title: "Team and communication impacts of remote work for complex aerospace system development"
authors:
  - "Ferguson, Sharon"
  - "van Velzen, Eric"
  - "Olechowski, Alison"
year: 2024
doi: "10.1002/sys.21716"
venue: {type: "journal", name: "Systems Engineering", volume: 27, issue: 1, pages: "199-213"}
citation: "Ferguson et al. (2024). Team and communication impacts of remote work for complex aerospace system development. Systems Engineering, 27(1), 199-213. https://doi.org/10.1002/sys.21716"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  Semi-structured interviews with 12 remote-working engineers at a single aerospace
  corporation found that the tightly coupled, complex nature of Complex Aerospace System
  Development (CASD) work made remote work especially disruptive to informal communication,
  design feedback speed, supplier/customer hardware demonstrations, interpersonal
  relationship maintenance, conceptual design work, and hardware testing coordination. The
  near-total loss of unplanned 'watercooler' communication was identified as the central
  driver of downstream harms to trust, onboarding, and collaboration in tightly coupled
  teams, while a previously geographically-distributed team saw improved cohesion from full
  remote adoption of Slack/Zoom.
claims:
  - text: "Participants reported that informal, unplanned communication ('watercooler' conversations) almost disappeared during remote work, and this loss was described as the primary driver of slower design feedback, weaker onboarding/tacit-knowledge transfer for new hires, and reduced awareness of other teams' work."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["team-cohesion", "remote-work-intensity"]
  - text: "All participants reported negative impacts of remote work on teamwork and interpersonal relationships (loss of socialization opportunities, cameras-off norms during calls, harder onboarding of new hires), though one team that was already geographically distributed pre-pandemic reported improved team dynamics after full remote adoption of Slack and Zoom."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["sense-of-belonging", "collaboration"]
    predictors: ["team-cohesion", "remote-work-intensity"]
  - text: "10 of 12 participants wanted to continue some form of remote work going forward (typically a hybrid of 2-3 in-office days), despite reporting substantial communication and relationship-maintenance challenges specific to tightly coupled, hardware-dependent aerospace engineering work (e.g., verifying supplier drawings, demonstrating hardware to customers, conceptual whiteboard-style design)."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["job-satisfaction", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "12 engineers (Mechanical, Electrical, Aerospace, Systems Engineering; 8 men, 4 women; mix of junior to senior) working remotely at one major aerospace corporation on Complex Aerospace System Development projects"
  where: []
  when: "interviews conducted 7-11 months into a COVID-19-driven remote work period (single organization, region unspecified)"
  n: 12
  sector: ["aerospace-engineering", "remote-work"]
  sample_notes: >
    Single-organization, single-industry convenience sample; 10 of 12 participants
    recommended by their department manager (with instructions to vary seniority, gender,
    prior remote-work experience), 2 more snowball-selected; women comprised only one-third
    of the sample, which the authors flag as a representativeness limitation; no response-
    rate data given since selection was manager-nominated rather than open recruitment.
limitation:
  primary: "Exploratory qualitative design with a small (n=12), single-company, single-industry sample limits generalizability; the authors explicitly note women's perspectives may be underrepresented and that company-specific effects cannot be separated from CASD-specific effects."
  others:
    - "Study focused on challenges of remote work rather than benefits, likely skewing findings toward negative impacts."
    - "Interviews captured only near-term (7-11 month) effects after participants had already adapted routines; longer-term effects of sustained remote work were not observed."
    - "Relies on retrospective self-report, memory, and salience rather than objective performance measures."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a detailed, mechanism-level account of how loss of informal/unplanned
  communication in remote work degrades trust, shared understanding, onboarding, and cross-
  team collaboration in tightly coupled work -- directly informing SNH's interest in which
  forms of casual/ambient interaction (not just scheduled meetings) most need to be
  preserved or redesigned for remote and hybrid teams, including via chosen communication
  platforms and 'virtual watercooler' interventions.
tags:
  topic: ["remote-work", "collaboration", "social-presence", "wellbeing"]
  method: ["qualitative", "interview"]
  population: ["aerospace-engineering", "remote-work"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Systems Engineering - 2023 - Ferguson - Team and communication impacts of remote work for complex aerospace system/Systems Engineering - 2023 - Ferguson - Team and communication impacts of remote work for complex aerospace system.md"
  pdf: "papers/Remote Workers/Systems Engineering - 2023 - Ferguson - Team and communication impacts of remote work for complex aerospace system.pdf"
  notes: null

---

id: "snyder-2002-target-article-hope-theory-rainbows-in"
title: "TARGET ARTICLE: Hope Theory: Rainbows in the Mind"
authors:
  - "Snyder, C. R."
year: 2002
doi: "10.1207/s15327965pli1304_01"
venue: {type: "journal", name: "Psychological Inquiry", volume: 13, issue: 4, pages: "249-275"}
citation: "Snyder (2002). TARGET ARTICLE: Hope Theory: Rainbows in the Mind. Psychological Inquiry, 13(4), 249-275. https://doi.org/10.1207/s15327965pli1304_01"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  Snyder's target article defines hope as the combination of pathways thinking (perceived
  capacity to generate routes to goals) and agency thinking (perceived motivation to use
  those routes), differentiates it from optimism, self-efficacy, self-esteem, and problem-
  solving theories, and synthesizes a decade of correlational and quasi-experimental
  research showing high-hope people outperform low-hope people in academics, athletics,
  physical health, psychological adjustment, and psychotherapy outcomes. It also examines
  how hope is learned and lost (neglect, abuse, bereavement, job loss, trauma) and
  systematically rebuts the 'false hope' critique, arguing hope is neutral about goal
  content but calibrates realistically to feedback rather than producing delusion.
claims:
  - text: "Higher dispositional hope is consistently associated with less loneliness, more perceived social support, and stronger bonds with friends and extended family, while low-hope people are described as lonely, fearful of interpersonal closeness, and unforgiving; in laboratory interaction tasks, people gravitate toward high-hope and away from low-hope partners (Sympson, 1999; Barnum et al., 1998; Kwon, 2002; Cheavens et al., 2000)."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["loneliness", "sense-of-belonging"]
    predictors: ["hope", "social-support"]
  - text: "In a 6-year longitudinal study of 200 college students, Hope Scale scores taken at the start of the first semester significantly predicted higher cumulative GPA (2.85 for high-hope vs. 2.43 for low-hope students), higher graduation rates, and lower attrition, even after controlling for entrance examination scores."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "retention"]
    predictors: ["hope"]
  - text: "Reanalyzing a psychotherapy-outcome meta-analysis that controlled for placebo expectancy (Barker, Funk, & Houston, 1988), the agency component of hope accounted for a .47 SD treatment effect and the pathways component for .55 SD, yielding a combined hope-attributable effect size of 1.02 SD across therapy modalities."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["mental-health", "wellbeing"]
    predictors: ["hope", "intervention"]
population:
  who: "Not a single sample: a first-person narrative synthesis by the theory's originator of dozens of his own and colleagues' studies across the 1990s, spanning grade-school through college students, athletes, psychiatric inpatients/outpatients, medical patients (cancer, burns, spinal cord injury, arthritis, asthma), Vietnam veterans, and community adults."
  where: ["United States"]
  when: "1980s-2002"
  n: null
  sector: ["education", "healthcare", "clinical-psychology", "sport-psychology"]
  sample_notes: >
    Aggregates results from the author's Trait Hope Scale, State Hope Scale, and Children's
    Hope Scale validation and correlational studies; no unified sample or reproducible
    study-selection protocol is described except for the one cited psychotherapy meta-
    analysis (Barker et al., 1988).
limitation:
  primary: "As the originator of hope theory, Snyder is a non-neutral reviewer summarizing decades of his own lab's supportive findings in narrative rather than systematic or meta-analytic form, so the evidentiary base is not independently replicated or reproducibly selected."
  others:
    - "Most cited findings are correlational, so directional/causal claims that hope drives academic, health, and social outcomes rather than resulting from them are largely inferential."
    - "Individual study sample sizes, recruitment methods, and response rates are not reported in this article, only aggregated point estimates and correlations."
    - "The rebuttal of the 'false hope' critique leans heavily on clinical anecdote and post hoc reasoning, with only two formal empirical tests (Kwon, 2000, 2002) directly designed to test the hypothesis."
risk_of_bias: "high"
relevance_to_project: >
  Establishes hope (agency + pathways thinking) as a measurable, trainable construct with
  validated scales (Trait/State/Children's Hope Scale) that correlates with lower
  loneliness, stronger perceived social support, and better psychological adjustment, giving
  the SNH project a candidate mechanism and existing measurement tools for designing and
  evaluating belonging- or resilience-focused interventions for remote workers and community
  members.
tags:
  topic: ["wellbeing", "loneliness", "social-support", "mental-health", "measurement", "suicide-prevention"]
  method: ["theory", "review-scoping"]
  population: ["college-students", "clinical-patients", "children", "general-adults"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/TARGET ARTICLE  Hope Theory  Rainbows in the Mind/TARGET ARTICLE  Hope Theory  Rainbows in the Mind.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/TARGET ARTICLE  Hope Theory  Rainbows in the Mind.pdf"
  notes: null

---

id: "fonner-2012-testing-the-connectivity-paradox-linking-teleworkers"
title: "Testing the Connectivity Paradox: Linking Teleworkers' Communication Media Use to Social Presence, Stress from Interruptions, and Organizational Identification"
authors:
  - "Fonner, Kathryn L."
  - "Roloff, Michael E."
year: 2012
doi: "10.1080/03637751.2012.673000"
venue: {type: "journal", name: "Communication Monographs", volume: 79, issue: 2, pages: "205-231"}
citation: "Fonner et al. (2012). Testing the Connectivity Paradox: Linking Teleworkers' Communication Media Use to Social Presence, Stress from Interruptions, and Organizational Identification. Communication Monographs, 79(2), 205-231. https://doi.org/10.1080/03637751.2012.673000"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Surveying 89 high-intensity teleworkers and 104 office-based employees, this study tests
  Leonardi et al.'s (2010) connectivity paradox using multigroup path analysis.
  Communication media use was largely unrelated to perceived social presence, but most media
  (face-to-face, videoconferencing, instant messaging, email) significantly increased
  teleworkers' stress from interruptions, which in turn strongly and negatively predicted
  organizational identification (much more strongly than social presence predicted it
  positively). The pattern held only partially for office-based employees, whose
  interruption stress was not linked to their identification, suggesting teleworkers are
  uniquely vulnerable to connectivity's downside.
claims:
  - text: "Among teleworkers, communication media use was significantly related to stress from interruptions but not to social presence: face-to-face (beta=.16, p<.006), videoconferencing (beta=.15, p<.042), instant messaging (beta=.37, p<.001), and email (beta=.14, p<.003) all increased stress from interruptions, while none of the five media significantly predicted social presence."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "social-presence"]
    predictors: ["technostress"]
  - text: "Teleworkers' stress from interruptions was strongly negatively related to organizational identification (beta=-.39, p<.001) and this effect was significantly larger in magnitude than the positive effect of social presence on identification (beta=.25, p<.001); significant indirect paths ran from face-to-face, instant messaging, and email use to lower identification via interruption stress."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-engagement", "stress"]
    predictors: ["technostress", "social-support"]
  - text: "Teleworkers reported significantly less stress from interruptions than office-based employees, and similar (not lower) levels of social presence and organizational identification; but for office-based employees, interruption stress was unrelated to organizational identification (beta=.18, ns), unlike for teleworkers, indicating the connectivity paradox's identification-damaging effect is specific to high-intensity telework."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["isolation", "job-engagement"]
    predictors: ["remote-work-intensity"]
population:
  who: "High-intensity teleworkers (working remotely at least 3 days/week, physically isolated from colleagues) and office-based employees (collocated at least 3 days/week), recruited via snowball sampling from personal/alumni contacts and two telework-focused websites"
  where: ["United States"]
  when: null
  n: 193
  sector: ["mixed-sectors"]
  sample_notes: >
    89 teleworkers, 104 office-based employees; convenience/snowball sample, not randomly
    selected; teleworkers were significantly older, longer-tenured, and more often married
    with children than office-based comparisons, so groups differ on demographics as well as
    work arrangement.
limitation:
  primary: "Cross-sectional self-report design precludes causal inference; the authors note plausible reverse-causal or reciprocal pathways (e.g., stronger identification could reduce perceived interruption stress rather than the reverse)."
  others:
    - "Non-random, self-selected snowball sample of high-intensity teleworkers only, limiting generalizability to other telework arrangements or intensities."
    - "Did not measure whether telework was voluntary, prior collocated work experience, or team geographic dispersion, all of which could confound the modeled relationships."
    - "Social presence measure showed no significant links to any communication medium, a null result the authors flag as possibly reflecting an incomplete measurement model rather than a true absence of effect."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's model of remote-work connectivity as a double-edged
  mechanism: frequent mediated communication does not reliably build teleworkers' sense of
  social presence/belonging, but it does reliably raise interruption-driven stress, and that
  stress -- not lack of connection -- is what erodes organizational identification. This
  argues for design interventions (protected focus time, connectivity norms, phone over
  IM/email for reducing stress) rather than simply maximizing communication frequency to
  combat remote-worker isolation.
tags:
  topic: ["remote-work", "technostress", "social-presence", "job-engagement"]
  method: ["survey", "cross-sectional"]
  population: ["teleworkers", "office-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Testing the Connectivity Paradox  Linking Teleworkers  Communication Media Use to Social Presence  Stress from Interruptions  and Organizational Ident/Testing the Connectivity Paradox  Linking Teleworkers  Communication Media Use to Social Presence  Stress from Interruptions  and Organizational Ident.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Testing the Connectivity Paradox  Linking Teleworkers  Communication Media Use to Social Presence  Stress from Interruptions  and Organizational Ident.pdf"
  notes: null

---

id: "l-2022-the-effects-of-remote-work-on"
title: "The effects of remote work on collaboration among information workers"
authors:
  - "L, Yang"
  - "D, Holtz"
  - "S, Jaffe"
  - "S, Suri"
  - "S, Sinha"
  - "J, Weston"
  - "C, Joyce"
  - "N, Shah"
  - "K, Sherman"
  - "B, Hecht"
  - "J, Teevan"
year: 2022
doi: "10.1530/ey.19.15.13"
venue: {type: "journal", name: "Yearbook of Paediatric Endocrinology", volume: null, issue: null, pages: null}
citation: "L et al. (2022). The effects of remote work on collaboration among information workers. Yearbook of Paediatric Endocrinology. https://doi.org/10.1530/ey.19.15.13"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  Using a natural experiment created by Microsoft's company-wide COVID-19 work-from-home
  mandate, this study analyzes six months of telemetry data (email, IM, calls, calendars)
  from 61,182 US employees to causally estimate how firm-wide remote work reshapes
  collaboration networks and communication. It finds that remote work made collaboration
  networks more static and siloed—reducing cross-group and bridging ties while increasing
  time spent with strong ties—and shifted communication from synchronous (meetings, calls)
  toward asynchronous (email, IM) channels, patterns the authors argue plausibly impede the
  flow of new information across the organization.
claims:
  - text: "Firm-wide remote work decreased the number of bridging ties (ties spanning structural holes) by 0.09FV (P<0.001) and the share of collaboration time spent with bridging ties by 0.41FV (P<0.001), while decreasing cross-group ties by 0.04FV and cross-group time share by 0.26FV, indicating networks became more siloed."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
  - text: "Firm-wide remote work decreased scheduled meeting hours by 0.16FV (P<0.001) and net synchronous video/audio communication by 0.05FV (P=0.006), while increasing emails sent by 0.08FV (P<0.001) and instant messages sent by 0.50FV (P<0.001), a shift from synchronous toward asynchronous communication."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["communication", "collaboration"]
    predictors: ["remote-work-intensity"]
  - text: "Remote work made collaboration networks more static: the number of connections churned per month fell by 0.05FV (P=0.006) and connections added fell by 0.04FV (P=0.015), with the share of time spent with newly added ties dropping by 0.29FV (P<0.001), reducing opportunities to benefit from new or reactivated ties."
    evidence: "longitudinal"
    support_strength: "strong"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "61,182 US Microsoft employees (excluding senior leadership and teams handling highly sensitive data), spanning software/hardware engineering, marketing, and business operations roles"
  where: ["United States"]
  when: "December 2019 - June 2020"
  n: 61182
  sector: ["technology", "corporate"]
  sample_notes: >
    Single large US tech firm (Microsoft); natural experiment from the company-wide COVID-19
    WFH mandate (March-April 2020); sample reweighted via coarsened exact matching (CEM)
    comparing pre-pandemic remote vs. office workers; final remote:non-remote ratio 1:4.6;
    excludes senior leadership and non-US employees.
limitation:
  primary: "Results are drawn from a single large US technology firm (Microsoft) over a short three-month post-mandate window, so generalizability to other sectors, countries, firm sizes, or long-term (rather than pandemic-onset) remote work is uncertain."
  others:
    - "Productivity and innovation outcomes were not directly measured, only inferred from network and communication changes."
    - "Causal identification depends on untestable identifying assumptions (parallel trends, exogeneity, additive separability of ego/collaborator/COVID effects)."
    - "Cannot fully disentangle remote-work effects from other concurrent COVID-19 disruptions (e.g., caregiving, stress) despite the difference-in-differences design's attempt to do so."
risk_of_bias: "low"
relevance_to_project: >
  Provides causal, large-N evidence that mandated full-time remote work directly reduces
  bridging- and weak-tie collaboration and increases network fragmentation and staticness—a
  core mechanism-level finding for SNH's argument that remote/hybrid work design must
  actively counteract siloing (e.g., via engineered cross-group touchpoints) rather than
  assume ties translate unchanged online.
tags:
  topic: ["remote-work", "hybrid-work", "collaboration", "productivity", "measurement"]
  method: ["quasi-experimental", "secondary-data", "longitudinal"]
  population: ["tech-workers", "remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Effects of Remote Work on Collaboration Among Information Workers/The Effects of Remote Work on Collaboration Among Information Workers.md"
  pdf: "papers/Remote Workers/The Effects of Remote Work on Collaboration Among Information Workers.pdf"
  notes: null

---

id: "fostervold-2024-the-hidden-costs-of-working-from"
title: "The hidden costs of working from home: examining loneliness, role overload, and the role of social support during and beyond the COVID-19 lockdown"
authors:
  - "Fostervold, Knut Inge"
  - "Ulleberg, Pål"
  - "Nilsen, Odd Viggo"
  - "Halberg, Anne Marie"
year: 2024
doi: "10.3389/forgp.2024.1380051"
venue: {type: "journal", name: "Frontiers in Organizational Psychology", volume: 2, issue: null, pages: null}
citation: "Fostervold et al. (2024). The hidden costs of working from home: examining loneliness, role overload, and the role of social support during and beyond the COVID-19 lockdown. Frontiers in Organizational Psychology, 2. https://doi.org/10.3389/forgp.2024.1380051"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using two large waves of survey data from a Norwegian public-sector organization (N=6,918
  during the 2021 COVID-19 lockdown; N=6,576 two years later in 2023), this study models
  days-per-week working from home (WFH) as a predictor of loneliness, with role overload as
  a mediator and coworker social support as a moderator. More WFH days predicted more
  loneliness both directly and indirectly via role overload, and this effect weakened but
  persisted after the lockdown ended. Counterintuitively, employees with higher social
  support showed a steeper (not weaker) rise in role overload and loneliness as WFH days
  increased, reversing the expected buffering effect of support.
claims:
  - text: "Number of days WFH was directly and positively associated with loneliness (β = 0.121, p < 0.001) and indirectly associated with loneliness via increased role overload (β = 0.008, 95% CI [0.005, 0.010]); both relationships were significantly weaker after the lockdown than during it (interaction β = −0.040, p < 0.001 for the direct path)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "isolation"]
    predictors: ["remote-work-intensity"]
  - text: "Higher coworker social support was generally linked to lower role overload (β = −0.082, p < 0.001) and markedly lower loneliness (β = −0.402, p < 0.001), but a significant Support × Days-WFH interaction (β = 0.025, p < 0.05) showed the indirect WFH→loneliness effect via role overload was stronger at high support (b = 0.005) than at low support (b = 0.002) — the opposite of a classic buffering effect."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "burnout"]
    predictors: ["social-support", "remote-work-intensity"]
  - text: "Mean loneliness fell significantly from during-lockdown (M=2.26) to post-lockdown (M=2.06, d=0.24), while mean role overload stayed essentially unchanged (M=3.21 at both time points) even though average WFH days dropped from 3.16 to 1.75 (d=0.79), indicating loneliness reduction was not fully explained by reduced WFH intensity alone."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["loneliness", "burnout"]
    predictors: ["remote-work-intensity"]
population:
  who: "Employees of a large Norwegian public-sector organization (municipal/county administration), surveyed via an internal work-environment questionnaire; dental healthcare workers excluded as they could not work remotely"
  where: ["Norway"]
  when: "January 2021 (COVID-19 lockdown) and January 2023 (post-lockdown), 12,021 valid observations from 9,827 employees"
  n: 12021
  sector: ["public-sector", "government"]
  sample_notes: >
    Two cross-sectional waves nested within a partially overlapping cohort (2,194 employees
    responded both times, 7,633 only once); 6.1% of observations excluded for missing
    predictor data; highly educated sample (68.2% >3 years university); sensitivity checks
    found minimal differences between single- and dual-time respondents, and Harman's
    single-factor test indicated common method bias was not a major concern.
limitation:
  primary: "All measures are self-reported cross-sectional-per-wave survey data (not true panel with repeated measures on the same individuals throughout), raising common method variance concerns despite a Harman's test that found no major issue."
  others:
    - "No data on household composition (living alone vs. with others), which could confound or moderate the WFH-loneliness link during lockdown."
    - "Loneliness, role overload, and social support are each measured with only 3-4 short Likert items, limiting construct nuance."
    - "Sample is a single highly-educated Norwegian public-sector organization, limiting generalizability to other sectors, countries, or less-educated workforces."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, moderated-mediation evidence that higher WFH intensity increases
  loneliness partly through role overload, and delivers a counterintuitive finding that
  coworker social support can amplify rather than buffer this effect at high WFH intensity —
  directly relevant to designing remote-work social-support interventions and cautioning
  against assuming support always protects against isolation.
tags:
  topic: ["remote-work", "loneliness", "social-support", "wellbeing", "hybrid-work"]
  method: ["survey", "longitudinal"]
  population: ["public-sector", "norway"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Hidden Costs of Working from Home - Loneliness Role Overload and Social Support During and Beyond COVID-19 Lockdown/The Hidden Costs of Working from Home - Loneliness Role Overload and Social Support During and Beyond COVID-19 Lockdown.md"
  pdf: "papers/Remote Workers/The Hidden Costs of Working from Home - Loneliness Role Overload and Social Support During and Beyond COVID-19 Lockdown.pdf"
  notes: null

---

id: "van-2022-the-impact-of-remote-work-and"
title: "The impact of remote work and mediated communication frequency on isolation and psychological distress"
authors:
  - "Van Zoonen, Ward"
  - "Sivunen, Anu E."
year: 2022
doi: "10.1080/1359432x.2021.2002299"
venue: {type: "journal", name: "European Journal of Work and Organizational Psychology", volume: 31, issue: 4, pages: "610-621"}
citation: "Van Zoonen et al. (2022). The impact of remote work and mediated communication frequency on isolation and psychological distress. European Journal of Work and Organizational Psychology, 31(4), 610-621. https://doi.org/10.1080/1359432x.2021.2002299"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A three-wave cross-lagged panel survey of Finnish employees during the COVID-19 pandemic
  finds that remote work frequency increases perceived physical isolation over time, while
  frequency of mediated (ICT) communication with colleagues reduces it, and that these two
  effects are independent rather than interacting. The study also finds a reciprocal,
  bidirectional relationship between isolation and psychological distress: isolation
  predicts later distress and distress also predicts later isolation, supporting a 'strain-
  effect' alongside the more commonly hypothesized 'stressor-effect.'
claims:
  - text: "Remote work frequency at T1 significantly increased isolation at T2 (B = 0.121, 95% CI [.022, .218], p = .024), and remote work at T2 increased isolation at T3 (B = 0.187, 95% CI [.080, .294], p = .001), supporting the hypothesis that remote work frequency drives later isolation."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation"]
    predictors: ["remote-work-intensity"]
  - text: "Mediated communication frequency reduced isolation across waves (T1->T2: B = -0.155, 95% CI [-.260, -.051], p = .005; T2->T3: B = -0.131, 95% CI [-.253, -.018], p = .022), but did not moderate the remote-work-to-isolation effect (interaction ns at both lags), indicating remote work and communication frequency act as independent, opposing predictors of isolation rather than interacting."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation", "communication"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Isolation and psychological distress showed a reciprocal cross-lagged relationship: isolation at T1 increased distress at T2 (B = 0.032, p = .030) and isolation at T2 increased distress at T3 (B = 0.030, p = .050), while distress at T1 also increased isolation at T2 (B = 0.142, p = .050) and distress at T2 increased isolation at T3 (B = 0.204, p = .003); remote work's effect on distress at T3 and mediated communication's effect on distress were both significant indirect (mediated-through-isolation) effects."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["isolation", "mental-health", "stress"]
    predictors: ["remote-work-intensity", "isolation"]
population:
  who: "Finnish employees recruited via convenience sampling (labour unions, ministries) during the first COVID-19 lockdown, surveyed across three waves; analytic sample completed all three waves"
  where: ["Finland"]
  when: "March 2020 - October 2020"
  n: 1164
  sector: ["public-administration", "professional-services", "information-communications", "education", "manufacturing"]
  sample_notes: >
    Initial T1 response 5,452; T2 response rate 34.76% of T1 (59.5% of invited, n=1,895); T3
    response rate 21.35% of T1 (61.42% of invited, n=1,164 retained for analysis).
    Predominantly female (76.6%), mean age 46.45, mean tenure 11.07 years; only 11.7%
    managers. Little's MCAR test indicated missingness was not completely at random, though
    non-response analyses found no significant differences in study constructs or model
    relationships between panel completers and dropouts.
limitation:
  primary: "Isolation was measured only as physical/perceived-separation isolation using a 4-item scale adapted from Orhan et al. (2016); other dimensions of isolation (informational, professional, social) that prior work shows can behave differently were not assessed."
  others:
    - "Unequal time lags between waves (short T1-T2, longer T2-T3, driven by pandemic timeline logistics rather than theory) complicate comparison of effect sizes across lags."
    - "No measures of task interdependence, perceived autonomy/control, or how synchronously vs. asynchronously the communication technologies were actually used."
    - "Strict longitudinal measurement invariance could not be established, limiting comparison of latent factor means across waves; all measures were self-reported at every wave, raising (though empirically mitigated) common-method-bias concerns."
risk_of_bias: "medium"
relevance_to_project: >
  Provides longitudinal, causally-ordered (cross-lagged) evidence that remote work frequency
  and ICT communication frequency have independent, opposing effects on physical isolation,
  and that isolation and psychological distress reinforce each other bidirectionally over
  time -- directly informing SNH's choice of isolation/distress measures and its rationale
  for prioritizing communication-frequency interventions (e.g., structured check-ins) as a
  distinct lever from simply reducing remote-work days.
tags:
  topic: ["remote-work", "isolation", "mental-health", "wellbeing"]
  method: ["longitudinal", "survey", "cross-lagged-panel"]
  population: ["remote-workers", "finland", "general-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The impact of remote work and mediated communication frequency on isolation and psychological distress/The impact of remote work and mediated communication frequency on isolation and psychological distress.md"
  pdf: "papers/Remote Workers/The impact of remote work and mediated communication frequency on isolation and psychological distress.pdf"
  notes: null

---

id: "ghar-2025-the-impact-of-remote-work-on"
title: "The Impact of Remote Work on Team Collaboration and Communication"
authors:
  - "Ghar, Sayan"
year: 2025
doi: "10.2139/ssrn.5258200"
venue: {type: "journal", name: "SSRN Electronic Journal", volume: null, issue: null, pages: null}
citation: "Ghar (2025). The Impact of Remote Work on Team Collaboration and Communication. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.5258200"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  This DBA thesis uses semi-structured interviews with 20 IT professionals in Kolkata,
  India, analyzed via thematic analysis, grounded theory, and content (NVivo) coding, to
  examine how remote work reshapes team collaboration and communication. It finds that
  remote work raises individual productivity and flexibility but simultaneously produces
  isolation, loss of spontaneous informal interaction, and decreased morale, synthesizing
  these tensions into a grounded theory the author labels 'Balancing Flexibility and Team
  Cohesion.' The thesis concludes that hybrid work models with scheduled in-office days are
  the participants' preferred mitigation strategy.
claims:
  - text: "NVivo content analysis of the 20 interview transcripts found 'Collaboration Challenges' was the most frequently coded theme (12 mentions), ahead of Productivity (10), Flexibility (9), Communication Tools (7), and Job Satisfaction (6)."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity"]
  - text: "Grounded theory analysis (open, axial, selective coding) produced a core theory, 'Balancing Flexibility and Team Cohesion': remote work increased individual productivity and work-life balance but generated feelings of isolation, loss of spontaneous informal communication, and decreased morale/engagement among team members."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["isolation", "productivity", "job-satisfaction"]
    predictors: ["remote-work-intensity", "team-cohesion"]
  - text: "Participants expressed a consistent preference for hybrid work models with regular in-office days as a strategy to sustain team cohesion and informal interaction while retaining remote work's flexibility benefits."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration", "job-satisfaction"]
    predictors: ["team-cohesion", "remote-work-intensity"]
population:
  who: "20 purposively sampled IT sector employees (software engineers, IT project managers, business analysts) working remotely"
  where: ["India"]
  when: null
  n: 20
  sector: ["technology"]
  sample_notes: >
    Non-random, purposive sample of 20 employees drawn from a single IT hub (Sector V, Salt
    Lake, Kolkata); the employer's name is withheld for confidentiality; no response-rate or
    demographic breakdown reported; single-country, single-sector convenience sample.
limitation:
  primary: "Small purposive sample (n=20) from a single IT sector location in Kolkata, India severely limits generalizability to other sectors, regions, or organizational contexts."
  others:
    - "Qualitative self-report interview data is subject to social-desirability and single-researcher interpretive bias, with no independent coder reported"
    - "Cross-sectional, short-term design captures only a single snapshot and cannot address long-term effects of remote work on team dynamics"
    - "No demographic breakdown (age, gender, tenure) of participants is reported alongside the findings"
risk_of_bias: "medium"
relevance_to_project: >
  The grounded-theory finding that isolation and reduced informal interaction were the top
  coded collaboration challenges (ahead of productivity gains) directly supports the SNH
  project's emphasis on informal-communication and belonging mechanisms as levers for
  remote-team health, and its hybrid-model recommendation is a concrete design lever worth
  weighing against stronger-evidence sources.
tags:
  topic: ["remote-work", "collaboration", "isolation", "job-satisfaction", "hybrid-work"]
  method: ["qualitative", "interview"]
  population: ["it-sector", "india", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Impact of Remote Work on Team Collaboration and Communication - DBA Thesis/The Impact of Remote Work on Team Collaboration and Communication - DBA Thesis.md"
  pdf: "papers/Remote Workers/The Impact of Remote Work on Team Collaboration and Communication - DBA Thesis.pdf"
  notes: null

---

id: "wu-2024-the-impact-of-remote-work-on"
title: "The Impact of Remote Work on Workplace Loneliness During and after COVID-19: A Literature Review"
authors:
  - "Wu, Xinyi"
year: 2024
doi: "10.54254/2753-7064/39/20242253"
venue: {type: "journal", name: "Communications in Humanities Research", volume: 39, issue: 1, pages: "250-257"}
citation: "Wu (2024). The Impact of Remote Work on Workplace Loneliness During and after COVID-19: A Literature Review. Communications in Humanities Research, 39(1), 250-257. https://doi.org/10.54254/2753-7064/39/20242253"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This literature review synthesizes 13 empirical studies (Jan 2020-Jul 2024) on remote work
  and workplace loneliness, finding that early cross-sectional studies showed no direct link
  between remote work extent and loneliness, but later studies found remote work exacerbates
  loneliness through reduced face-to-face interaction. It identifies social support
  (supervisor and coworker), communication technologies, job demands, and job control as the
  key factors moderating whether remote work translates into loneliness, and argues the
  evidence base is limited by an absence of longitudinal designs.
claims:
  - text: "Miyake et al. found high psychological job demands were significantly associated with increased work loneliness among Japanese desk workers (AOR = 2.04, 95% CI: 1.39-2.99, P < 0.001), and employees remote 4+ days/week had marginally higher odds of loneliness (AOR = 1.23, 95% CI: 0.99-5.84, P = 0.066) than less-frequent remote workers."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["workload", "remote-work-intensity"]
  - text: "Rund's cross-sectional survey of German employees found no significant relationship between extent of remote work and loneliness (b = 24.03, SE = 14.26, p = 0.09), but loneliness at work was negatively associated with job-related subjective well-being (b = -0.50, SE = 0.15, p = 0.00), and supervisor support mitigated the negative effects of remote work."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness", "wellbeing"]
    predictors: ["remote-work-intensity", "leadership-style"]
  - text: "Across multiple included studies, low co-worker/supervisor support, high technostress, ineffective communication, and low job control were consistently linked to greater workplace loneliness, while higher social support, richer communication technology use, and greater job control buffered loneliness and supported job engagement and well-being in remote work settings."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["loneliness", "job-engagement", "wellbeing"]
    predictors: ["social-support", "technostress", "autonomy", "communication"]
population:
  who: "13 empirical studies of remote/hybrid employees (e.g., German employees, Japanese desk workers, Jakarta workers, Norwegian workers, UK healthcare workers) published between January 2020 and July 2024"
  where: ["Germany", "Japan", "Indonesia", "Norway", "United Kingdom"]
  when: "January 2020-July 2024"
  n: null
  sector: ["general-workforce", "healthcare"]
  sample_notes: >
    Narrative review of 13 studies selected from an initial 62 records via title/abstract
    and full-text screening (databases: PubMed, Web of Science, Google Scholar); most
    included studies are cross-sectional, and the review does not report a pooled N or
    conduct meta-analysis or formal quality appraisal.
limitation:
  primary: "Nearly all included primary studies are cross-sectional, so the review cannot establish the long-term/causal trajectory of remote work's effect on workplace loneliness."
  others:
    - "No formal risk-of-bias or quality appraisal of included studies is reported, and screening/synthesis appear narrative rather than systematic-with-meta-analysis."
    - "Findings across the 13 studies are mixed (some show no direct remote-work-loneliness link, others show a significant positive link), and the review does not quantitatively reconcile this heterogeneity."
risk_of_bias: "medium"
relevance_to_project: >
  Directly maps the moderators the SNH project should target for remote-worker loneliness
  interventions -supervisor/coworker social support, communication-technology quality, job
  demands, and job control- and flags that most underlying evidence is cross-sectional,
  reinforcing the project's need for longitudinal or intervention-based validation of any
  design responses.
tags:
  topic: ["remote-work", "loneliness", "isolation", "social-support", "job-engagement"]
  method: ["review-systematic", "secondary-data"]
  population: ["general-workforce", "healthcare"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Impact of Remote Work on Workplace Loneliness During and After COVID-19 - A Literature Review/The Impact of Remote Work on Workplace Loneliness During and After COVID-19 - A Literature Review.md"
  pdf: "papers/Remote Workers/The Impact of Remote Work on Workplace Loneliness During and After COVID-19 - A Literature Review.pdf"
  notes: null

---

id: "anderson-2015-the-impact-of-telework-on-emotional"
title: "The impact of telework on emotional experience: When, and for whom, does telework improve daily affective well-being?"
authors:
  - "Anderson, Amanda J."
  - "Kaplan, Seth A."
  - "Vega, Ronald P."
year: 2015
doi: "10.1080/1359432x.2014.966086"
venue: {type: "journal", name: "European Journal of Work and Organizational Psychology", volume: 24, issue: 6, pages: "882-897"}
citation: "Anderson et al. (2015). The impact of telework on emotional experience: When, and for whom, does telework improve daily affective well-being?. European Journal of Work and Organizational Psychology, 24(6), 882-897. https://doi.org/10.1080/1359432x.2014.966086"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Using a within-person daily-diary design with 102 US federal employees surveyed across
  four workdays, this study finds that teleworking days are associated with more positive
  job-related affect and less negative job-related affect than office days, though the main
  effects are modest in size. More importantly, these affective benefits are not uniform:
  openness to experience, trait rumination, and especially social connectedness outside of
  work moderate whether an employee benefits emotionally from teleworking, while sensation
  seeking showed no moderating effect.
claims:
  - text: "On days when teleworking (vs. working in the office), employees reported significantly more positive job-related affect (gamma = .15, p < .05) and significantly less negative job-related affect (gamma = -.23, p < .05), though effect sizes were described by the authors as modest."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing", "job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Social connectedness outside of the workplace strongly moderated telework's affective benefits: the telework-positive affect relationship became more positive as outside social connectedness increased (gamma = .75, p < .001), and the telework-negative affect relationship became more negative (i.e., more beneficial) as outside social connectedness increased (gamma = -.73, p < .01)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing", "isolation"]
    predictors: ["social-support", "isolation"]
  - text: "Trait rumination weakened the positive-affect benefit of teleworking (gamma = -.38, p < .01), and openness to experience strengthened it (gamma = .74, p < .05), while sensation seeking did not significantly moderate either affect relationship, indicating telework's emotional payoff depends on individual differences rather than being universal."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing"]
    predictors: ["remote-work-intensity"]
population:
  who: "102 employees of a large US federal government agency who had signed telework agreements to work from home at least once per pay period (business operations/contract-support roles); recruited from an initial pool of 702 invited employees"
  where: ["United States"]
  when: null
  n: 102
  sector: ["government"]
  sample_notes: >
    Response/participation rate was low (102 of 702 invited, ~14.5%); non-respondents could
    not be compared to respondents on demographics; single organization with an unusually
    favorable, liberal telework policy, limiting generalizability to less telework-
    supportive organizations. Sample was 50% female, ages 25-65 spread across bands; average
    tenure teleworking ~3 years, ~2.88 telework days/week.
limitation:
  primary: "Single-organization sample with a strongly pro-telework culture and no random assignment to telework (employees self-selected into telework agreements), limiting causal inference and generalizability to organizations less supportive of remote work."
  others:
    - "Low participation rate (102 of 702 invited) with no way to compare respondents to non-respondents, raising representativeness concerns."
    - "Sensation-seeking scale had weak internal consistency (initial alpha = .48, improved to .66 only after dropping an item) and the sample likely had restricted range on this trait."
    - "Affect was measured with only 10 of 30 JAWS items and over just 4 days, and specific work events (the proposed AET mechanism) were not directly measured."
risk_of_bias: "medium"
relevance_to_project: >
  Provides within-person quantitative evidence that social connectedness outside of work is
  a key buffer/amplifier of telework's affective benefits, directly informing the SNH
  project's hypothesis that off-work social support networks moderate remote-work wellbeing
  outcomes and that interventions may need to target employees low in outside social
  connectedness or high in rumination.
tags:
  topic: ["remote-work", "wellbeing", "social-support", "isolation"]
  method: ["longitudinal", "survey"]
  population: ["government-employees", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The impact of telework on emotional experience  When  and for whom  does telework improve daily affective well-being/The impact of telework on emotional experience  When  and for whom  does telework improve daily affective well-being.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The impact of telework on emotional experience  When  and for whom  does telework improve daily affective well-being .pdf"
  notes: null

---

id: "jamaludin-2023-the-relationship-between-remote-work-and"
title: "The Relationship between Remote Work and Job Satisfaction: The Mediating Role of Perceived Autonomy"
authors:
  - "Jamaludin, Nor Lelawati"
  - "Kamal, Sakinah Ahmad"
year: 2023
doi: "10.22610/imbr.v15i3(si).3453"
venue: {type: "journal", name: "Information Management and Business Review", volume: 15, issue: "3(SI)", pages: "10-22"}
citation: "Jamaludin et al. (2023). The Relationship between Remote Work and Job Satisfaction: The Mediating Role of Perceived Autonomy. Information Management and Business Review, 15(3(SI)), 10-22. https://doi.org/10.22610/imbr.v15i3(si).3453"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This cross-sectional survey of 185 employees at a Malaysian oil and gas company found that
  remote work was significantly and positively related to job satisfaction, and that
  perceived autonomy fully mediated this relationship: once autonomy was accounted for, the
  direct effect of remote work on job satisfaction became non-significant (Sobel z = 3.95, p
  < .001). It extends autonomy-mediation findings from prior telework research into an
  understudied, high-risk, largely on-site industrial sector, suggesting that scheduling,
  decision-making, and work-method autonomy are the operative mechanism through which remote
  arrangements improve satisfaction, not remote access per se.
claims:
  - text: "Remote work had a significant, positive relationship with job satisfaction, r(168) = .16, p < .05, and in regression accounted for 9% of the variance in job satisfaction, R2 = .09, R2adj = .08, F(1,179) = 16.56, p < .01."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Perceived autonomy fully mediated the relationship between remote work and job satisfaction: remote work predicted perceived autonomy (R2 = .10, F(1,170) = 18.91, p < .001), autonomy predicted job satisfaction (beta = .56, t = 8.20, p < .001), and the direct path from remote work to job satisfaction became non-significant once autonomy was included (Sobel z = 3.95, p < .001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity", "autonomy"]
  - text: "Remote work correlated moderately and positively with perceived autonomy, r(168) = .32, p < .01, and perceived autonomy correlated strongly and positively with job satisfaction, r(168) = .55, p < .01 -- the strongest bivariate relationship in the study."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["autonomy"]
population:
  who: "Full-time employees with remote-work experience at one oil and gas company in Kuala Lumpur, Malaysia, drawn from various departments"
  where: ["Malaysia"]
  when: null
  n: 185
  sector: ["oil-gas", "corporate"]
  sample_notes: >
    Convenience sampling from a single organization (estimated population ~765); analytic
    sample sizes varied across tests (n=168-179) due to listwise handling of missing data;
    ages 22-65 (M=33.44, SD=10.87), 60.5% female, 33.5% male, .5% other; response rate not
    reported.
limitation:
  primary: "Reliance on self-report measures for job satisfaction and perceived autonomy risks common-method bias and social-desirability distortion."
  others:
    - "Single organization in a single industry (oil and gas, Malaysia) limits generalizability to other sectors and countries."
    - "Convenience sampling rather than probability sampling undermines representativeness claims made for the findings."
    - "Cross-sectional design cannot support the causal/mediational language used to describe the results despite the Baron & Kenny/Sobel mediation framework."
risk_of_bias: "medium"
relevance_to_project: >
  Provides evidence that perceived autonomy (scheduling, decision-making, work-method) is
  the mechanism through which remote work improves job satisfaction rather than remote
  access alone, which is directly relevant to SNH intervention design: giving remote workers
  real autonomy over schedule and method may matter more than remote-work availability
  itself for wellbeing outcomes, even in an industrial, largely on-site sector.
tags:
  topic: ["remote-work", "job-satisfaction", "wellbeing"]
  method: ["survey", "cross-sectional", "mediation-analysis"]
  population: ["employees", "oil-gas-industry", "malaysia"]
source:
  markdown: "Papers_Data/Remote Workers/MD/The Relationship between Remote Work and Job Satisfaction - The Mediating Role of Perceived Autonomy/The Relationship between Remote Work and Job Satisfaction - The Mediating Role of Perceived Autonomy.md"
  pdf: "papers/Remote Workers/The Relationship between Remote Work and Job Satisfaction - The Mediating Role of Perceived Autonomy.pdf"
  notes: null

---

id: "eisinga-2013-the-reliability-of-a-two-item"
title: "The reliability of a two-item scale: Pearson, Cronbach, or Spearman-Brown?"
authors:
  - "Eisinga, Rob"
  - "Grotenhuis, Manfred te"
  - "Pelzer, Ben"
year: 2013
doi: "10.1007/s00038-012-0416-3"
venue: {type: "journal", name: "International Journal of Public Health", volume: 58, issue: 4, pages: "637-642"}
citation: "Eisinga et al. (2013). The reliability of a two-item scale: Pearson, Cronbach, or Spearman-Brown?. International Journal of Public Health, 58(4), 637-642. https://doi.org/10.1007/s00038-012-0416-3"
article_type: "methods"
method: {design: "theory", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  This methodological note derives and simulates reliability estimates for two-item scales
  under classical test theory, comparing the Pearson inter-item correlation, Cronbach's
  coefficient alpha, and the Spearman-Brown split-half formula. Using worked numerical
  examples and 1.6x10^9 simulated parameter combinations across parallel, tau-equivalent,
  and congeneric measurement models, the authors show that alpha is unbiased only under the
  restrictive tau-equivalence assumption and otherwise underestimates true reliability,
  whereas Spearman-Brown is on average less biased and always >= alpha. It concludes that
  when researchers must use a two-item scale, the Spearman-Brown coefficient (not Pearson r
  or alpha) should be reported.
claims:
  - text: "Cronbach's alpha is an unbiased estimator of a two-item scale's true reliability only when the items are at least essentially tau-equivalent; when items are congeneric (unequal factor loadings), alpha substantially underestimates true reliability even as inter-item correlation grows (e.g., a simulated example gives alpha = 0.441 versus true reliability r^2_tauY = 0.690)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The Spearman-Brown split-half coefficient (rho = 2r/(1+r)) is never lower than, and is almost always higher than, coefficient alpha for a two-item scale, and across simulations it is on average less biased than alpha, especially as inter-item correlation increases; the authors recommend it as the most appropriate reliability statistic for two-item scales."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
  - text: "The raw Pearson correlation between the two items is not an adequate reliability estimate for the composite two-item scale; it instead reflects the reliability of a single item (e.g., in a parallel-measures example, Pearson r = 0.640 while true scale reliability equals 0.780)."
    evidence: "theory"
    support_strength: "strong"
    outcomes: ["measurement"]
    predictors: ["sampling-method"]
population:
  who: "No human sample; a statistical/methodological demonstration using worked numerical examples and simulated data spanning parallel, tau-equivalent, essentially tau-equivalent, and congeneric two-item measurement models under classical test theory."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    Simulation generated all combinations of four loading/error parameters equidistant in
    [0,1] at .005 intervals (1.6x10^9 combinations); no empirical dataset or human
    respondents are used, so representativeness is not applicable.
limitation:
  primary: "The analysis is purely analytical/simulation-based and does not test the recommendations against real survey data, so its conclusions about bias apply to the idealized measurement models rather than to any specific empirical two-item scale."
  others:
    - "The authors explicitly note there is no statistical way to test the tau-equivalence or local-independence assumptions with only two items, so applied researchers cannot verify which measurement model their own two-item scale actually satisfies."
    - "The paper is a technical note that assumes readers already accept two-item scales are used out of necessity; it does not evaluate substantive social-network-health constructs directly."
risk_of_bias: "not-applicable"
relevance_to_project: >
  SNH surveys frequently rely on short (often two-item) measures of constructs like
  loneliness, social support, or burnout for time-constrained remote-worker samples; this
  paper gives a concrete, evidence-based rule (report Spearman-Brown rather than Cronbach's
  alpha or raw Pearson r) for computing and reporting the reliability of any such
  abbreviated scale used in the project's instruments.
tags:
  topic: ["measurement", "methodology"]
  method: ["theory", "analytical"]
  population: ["not-applicable"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The reliability of a two-item scale_ Pearson, Cronbach, or Spearman-Brown_.pdf"
  notes: null

---

id: "hansen-1999-the-search-transfer-problem-the-role"
title: "The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge across Organization Subunits"
authors:
  - "Hansen, Morten T."
year: 1999
doi: "10.2307/2667032"
venue: {type: "journal", name: "Administrative Science Quarterly", volume: 44, issue: 1, pages: "82-111"}
citation: "Hansen (1999). The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge across Organization Subunits. Administrative Science Quarterly, 44(1), 82-111. https://doi.org/10.2307/2667032"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Studying 120 new-product development projects across 41 divisions of a large electronics
  company, Hansen shows that weak interunit ties help project teams search for useful
  knowledge elsewhere in the organization but impede the transfer of that knowledge once
  found, especially when it is complex (noncodified and interdependent). Weak ties speed up
  project completion when the knowledge to be moved is simple and codified, but slow
  projects down when the knowledge is highly noncodified and dependent on other components,
  because transfer of complex knowledge requires the frequent, two-way interaction
  characteristic of strong ties. The paper resolves a discrepancy between weak-tie network
  theory and product-innovation research on tight coupling by showing both are right under
  different knowledge-complexity conditions.
claims:
  - text: "Tie weakness has a significant positive effect on project completion rate when knowledge to be transferred is highly codified and independent (main effect of tie weakness = 1.329, p < .01), supporting Hypothesis 1 that weak interunit ties speed up projects transferring simple knowledge."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "sampling-method"]
  - text: "Tie weakness interacts negatively with knowledge complexity: the noncodified x weakness interaction (-0.343, p<.10) and dependent x weakness interaction (-0.193, p<.10) show that as knowledge becomes more noncodified and interdependent, the benefit of weak ties dampens and turns negative, supporting Hypothesis 2 that weak ties slow completion when complex knowledge must be transferred."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure"]
  - text: "The positive effect of weak ties on completion time persisted after controlling for two direct measures of network redundancy (structural equivalence, proportion density) and for reciprocity, indicating weak ties are beneficial primarily because they are cheaper to maintain (lower search costs) rather than because they simply provide access to nonredundant contacts."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["collaboration", "performance"]
    predictors: ["network-structure", "social-support"]
population:
  who: "Project managers and R&D managers for 120 new-product development projects (54 with a cross-division knowledge transfer event analyzed in the main model) across 41 operating divisions of one large multinational electronics and computing company"
  where: ["United States", "Europe", "Asia", "Australia"]
  when: "1993-1995 (network data lagged one year prior to each project's start)"
  n: 120
  sector: ["technology", "manufacturing"]
  sample_notes: >
    Single-company field study; 100% response from 41 R&D managers on the network survey and
    85% response (120 of 147 projects) from project managers; main hazard-rate analysis
    restricted to the 54 projects that reported an interdivisional transfer event, with a
    separate check on the 66 that did not; author notes the firm studied is likely more
    densely networked than typical multiunit firms, which he argues biases results
    conservatively.
limitation:
  primary: "Findings are confined to a single company studied over a short window, and generalizability to less densely networked or non-electronics firms is untested."
  others:
    - "Outcome measure is limited to project completion time; effects on cost, quality, or degree of innovation were not directly assessed."
    - "Study captures only formal/regular interdivisional (group-level) ties, not personal cross-unit relationships or other channels (databases, e-mail, headquarters intervention) that project teams may also have used to find and move knowledge."
    - "Knowledge complexity ratings came solely from the project manager, so inter-rater reliability of the noncodified/dependent knowledge measures could not be tested."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational network-structure paper for the SNH project's core design tension:
  it gives quantitative evidence that weak ties (low-frequency, low-closeness relationships)
  are not uniformly good for collaboration/knowledge-sharing outcomes, and that the right
  network structure depends on task complexity — directly informing decisions about when a
  remote/distributed team should invest in cultivating strong-tie relationships (for
  complex, tacit knowledge transfer) versus rely on lighter-touch weak-tie connectors (for
  simple information search), a distinction relevant to designing onboarding, mentoring, and
  cross-team bridging mechanisms in remote and open-source communities.
tags:
  topic: ["remote-work", "collaboration", "community-health", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "organizations"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/The Search-Transfer Problem_ The Role of Weak Ties in Sharing Knowledge across Organization Subunits.pdf"
  notes: null

---

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

---

id: "jaiswal-2022-theorizing-employee-stress-well-being-resilience"
title: "Theorizing Employee Stress, Well-being, Resilience and Boundary Management in the Context of Forced Work from Home During COVID-19"
authors:
  - "Jaiswal, Akanksha"
  - "Gupta, Simran"
  - "Prasanna, Sai"
year: 2022
doi: "10.1177/22779779221100281"
venue: {type: "journal", name: "South Asian Journal of Business and Management Cases", volume: 11, issue: 2, pages: "86-104"}
citation: "Jaiswal et al. (2022). Theorizing Employee Stress, Well-being, Resilience and Boundary Management in the Context of Forced Work from Home During COVID-19. South Asian Journal of Business and Management Cases, 11(2), 86-104. https://doi.org/10.1177/22779779221100281"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Based on in-depth interviews with 30 experienced professionals in India's technology-
  enabled sectors during forced work-from-home in COVID-19, this study uses Gioia
  methodology to build a data structure of four aggregate dimensions: stress due to work
  disruptions, threats to employee well-being, boundary violation, and employee resilience.
  It extends boundary theory and the theory of cognitive adaptation to argue that
  involuntary WFH shifts boundary management from an individual prerogative into an
  organizationally-nested process, and that employees who lost social contact and blurred
  work-family boundaries nonetheless developed resilience through digital adoption,
  upskilling, and adaptation to hybrid work.
claims:
  - text: "Employees reported a distinct 'lack of social relations' dimension: they missed office chats, lunch breaks, and informal colleague contact, described work as feeling 'robotic,' and experienced reduced team spirit, team bonding, and sense of belongingness, alongside job-related loneliness and professional/social isolation that undermined self-efficacy and organizational identity."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "loneliness", "sense-of-belonging", "mental-health"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Forced WFH produced 'boundary violation' as a distinct dimension: work hours and days became fluid (calls at 10pm, weekend 'half hour' calls that stretched on), managers and colleagues were perceived as inconsiderate of employees' personal time, and work-home role conflict was common (e.g., interrupting calls to answer doors, juggling home-schooling and elder care), consistent with an emergent 'alternating' boundary management style rather than pure segmentation or integration."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "stress", "burnout"]
    predictors: ["boundary-management", "remote-work-intensity", "organizational-culture"]
  - text: "Despite stress and boundary violation, employees showed resilience through faster digital adoption, adaptation to new work methods (with 22 of 30 preferring a future hybrid mode versus only 2 preferring full WFH and 6 on-site), self-driven upskilling, and flexible-timing-driven quality-of-life gains (more family time, revived hobbies), framed as evidence of cognitive adaptation (meaning, mastery, self-enhancement) rather than mere coping."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "wellbeing", "job-engagement"]
    predictors: ["intervention", "autonomy", "boundary-management"]
population:
  who: "30 experienced professionals (3+ years tenure, min. 1.5 years pre-pandemic office tenure) working in technology-enabled sectors (IT, banking/insurance, consultancy, telecom) in India, recruited via purposive sampling"
  where: ["India"]
  when: "May-June 2021"
  n: 30
  sector: ["technology", "banking-finance", "consultancy"]
  sample_notes: >
    Purposive, non-random sample skewed male (19/30) and under-40 (25/30); all respondents
    worked in technology-enabled industries able to WFH, excluding manufacturing and other
    non-remote-eligible sectors; single-country, single-timepoint interview study reaching
    claimed theoretical saturation.
limitation:
  primary: "Single-country (India), cross-sectional qualitative design with a small purposive sample (n=30) confined to technology-enabled sectors, limiting generalizability to other industries, geographies, and work arrangements."
  others:
    - "Retrospective self-report interviews about a prolonged, evolving pandemic period are subject to recall and framing bias."
    - "No comparison group of voluntary/pre-pandemic remote workers, so claims about the effects of 'forced' versus chosen WFH rest on interpretation rather than direct contrast."
    - "Authors' own theoretical framing (boundary theory, cognitive adaptation) shapes coding categories, a common limitation of Gioia-methodology inductive analysis."
risk_of_bias: "medium"
relevance_to_project: >
  Directly documents the isolation/loneliness and belonging-erosion mechanisms of forced
  remote work (lack of social relations, job-related loneliness, reduced team bonding)
  alongside the boundary-violation and resilience/adaptation pathways the SNH project cares
  about, and offers a concrete measure candidate (Gioia-derived dimensions: work disruption
  stress, well-being threats, boundary violation, resilience) plus a real-world data point
  that 73% of this sample preferred hybrid work post-pandemic.
tags:
  topic: ["remote-work", "isolation", "loneliness", "wellbeing", "work-life-balance", "burnout"]
  method: ["qualitative", "interview"]
  population: ["technology-sector", "india", "knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Theorizing Employee Stress Well-Being Resilience and Boundary Management in the Context of Forced Remote Work/Theorizing Employee Stress Well-Being Resilience and Boundary Management in the Context of Forced Remote Work.md"
  pdf: "papers/Remote Workers/Theorizing Employee Stress Well-Being Resilience and Boundary Management in the Context of Forced Remote Work.pdf"
  notes: null

---

id: "eddleston-2017-toward-understanding-remote-workers-management-of"
title: "Toward Understanding Remote Workers’ Management of Work–Family Boundaries: The Complexity of Workplace Embeddedness"
authors:
  - "Eddleston, Kimberly A."
  - "Mulki, Jay"
year: 2017
doi: "10.1177/1059601115619548"
venue: {type: "journal", name: "Group &amp; Organization Management", volume: 42, issue: 3, pages: "346-387"}
citation: "Eddleston et al. (2017). Toward Understanding Remote Workers’ Management of Work–Family Boundaries: The Complexity of Workplace Embeddedness. Group &amp; Organization Management, 42(3), 346-387. https://doi.org/10.1177/1059601115619548"
article_type: "empirical"
method: {design: "mixed-methods", approach: "interview", evidence_level: "moderate", preregistered: false}
gist: >
  This multi-method study of remote workers (52 interviews, then a 299-respondent survey)
  finds that working solely from home does not reduce work-family conflict the way part-time
  telecommuting research suggests; instead, work-family integration increases both family-
  to-work conflict (FWC, beta=.81) and work-to-family conflict (WFC, beta=.61), and an
  inability to disengage from work increases WFC (beta=.21) and job stress (beta=.16), which
  in turn raises job stress (beta=.54). The authors coin 'workplace embeddedness' to
  describe how the home becomes fused with the work role for full-time remote workers, and
  show the harm of integration and of not disengaging is gendered: high integration hurts
  men's WFC more, while inability to disengage hurts women's WFC more.
claims:
  - text: "In the survey study, work-family integration was positively related to family-to-work conflict (beta=.81, t=6.72) and work-to-family conflict (beta=.61, t=5.63), contradicting the assumption that integration eases conflict for full-time remote (vs. part-time telecommuting) workers."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management", "remote-work-intensity"]
  - text: "Inability to disengage from work was positively related to work-to-family conflict (beta=.21, t=3.06) and, in an alternate model, to job stress (beta=.16, t=2.41), but was not significantly related to family-to-work conflict (beta=.05, t=0.22); WFC in turn predicted job stress (beta=.54, t=6.84) while FWC did not (beta=.01, ns)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["boundary-management", "autonomy"]
  - text: "Gender moderated two paths: high work-family integration was more harmful to men's WFC than women's (chi-square diff=4.09, p=.05), while high inability to disengage from work significantly increased women's WFC but had little effect on men's (chi-square diff=4.25). In interviews, 56% of women (16/28) vs. 10% of men (2/24) reported spouses/partners not respecting work-family boundaries, and 69% of men used segmentation to minimize conflict."
    evidence: "mixed-methods"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management"]
population:
  who: "Full-time (35+ hr/week) home-based remote workers in sales, marketing, customer service, IT, and PR in the United States; Study 1 = 52 semi-structured interviewees (32 female) at a large global firm plus referrals; Study 2 = 299 survey respondents (132 female, 161 male) from a technology company and an online firm with home-based sales/service staff"
  where: ["United States"]
  when: null
  n: 299
  sector: ["sales", "customer-service", "technology"]
  sample_notes: >
    Study 1 used purposeful/snowball sampling (34 initial employees via a sales manager,
    plus referrals and industry contacts) rather than random sampling, limiting
    generalizability; Study 2 achieved 315 survey responses in 2 weeks with 299 usable after
    excluding incomplete responses, drawn from two organizations to broaden
    generalizability, but respondents were screened to require 35+ hours/week working from
    home so findings may not generalize to part-time telecommuters or other job functions.
limitation:
  primary: "Study 2's survey data are cross-sectional, so the proposed causal paths (integration and inability to disengage causing conflict and stress) cannot be confirmed as causal; the authors explicitly call for longitudinal replication."
  others:
    - "Study 1's qualitative sample used non-random, targeted/snowball sampling from a small number of organizations, introducing possible selection bias."
    - "Findings are drawn from specific organizations and job functions (largely sales/service) in the US and may not generalize to remote workers in other roles, sectors, or cultures."
    - "Structural equation models are acknowledged to have statistically equivalent alternative specifications, though the authors argue this is mitigated by grounding the model in the qualitative findings."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs SNH's understanding of how always-on/boundaryless remote work erodes
  work-life balance and raises stress: the 'workplace embeddedness' construct and the
  finding that integration (not just remote-work intensity) drives conflict suggests
  boundary-management interventions (training workers/managers to protect off-hours) may
  matter more for SNH design than simply enabling flexibility, and the gender-moderated
  effects flag a need for gender-aware intervention design.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing"]
  method: ["mixed-methods", "survey", "interview"]
  population: ["remote-workers", "sales-employees"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Toward Understanding Remote Workers Management of Work-Family Boundaries - The Complexity of Workplace Flexibility/Toward Understanding Remote Workers Management of Work-Family Boundaries - The Complexity of Workplace Flexibility.md"
  pdf: "papers/Remote Workers/Toward Understanding Remote Workers Management of Work-Family Boundaries - The Complexity of Workplace Flexibility.pdf"
  notes: null

---

id: "triandis-1988-individualism-and-collectivism-cross-cultural-perspectives"
title: "Individualism and collectivism: Cross-cultural perspectives on self-ingroup relationships."
authors:
  - "Triandis, Harry C."
  - "Bontempo, Robert"
  - "Villareal, Marcelo J."
  - "Asai, Masaaki"
  - "Lucca, Nydia"
year: 1988
doi: "10.1037/0022-3514.54.2.323"
venue: {type: "journal", name: "Journal of Personality and Social Psychology", volume: 54, issue: 2, pages: "323-338"}
citation: "Triandis et al. (1988). Individualism and collectivism: Cross-cultural perspectives on self-ingroup relationships.. Journal of Personality and Social Psychology, 54(2), 323-338. https://doi.org/10.1037/0022-3514.54.2.323"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Across three studies with U.S., Japanese, and Puerto Rican samples, Triandis and
  colleagues show that individualism-collectivism at the cultural level and allocentrism-
  idiocentrism at the individual level are multidimensional, domain-specific constructs
  rather than a single global trait, and that allocentric individuals report more and
  better-quality social support while idiocentric individuals report more loneliness. The
  paper argues self-construal and ingroup orientation, not just national culture, predict
  social support and loneliness, and that collectivist effects appear only for specific
  ingroups and specific behaviors rather than uniformly across all relationships.
claims:
  - text: "In Study 3 (Illinois and Puerto Rico student samples), allocentrism correlated positively with social support and negatively with loneliness in both cultures: number of relatives cited as providing support correlated -.48 (p<.001) with loneliness in Illinois versus -.23 (p<.05) in Puerto Rico, and satisfaction with social support correlated -.48 (p<.001) in Illinois versus -.31 (p<.01) in Puerto Rico."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["social-support", "sense-of-belonging"]
  - text: "In Study 2, the hypothesis that collectivist-culture members (Japan) would uniformly conform more, feel more similar to ingroups, and subordinate personal goals to ingroup goals more than individualist-culture members (Illinois) was supported for only 19 of 138 cross-cultural comparisons (p<.01); 105 showed no difference and 14 showed the Illinois sample to be more collectivist, indicating collectivism effects are specific to particular ingroups and domains rather than global."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging"]
    predictors: ["network-structure", "inclusiveness"]
  - text: "In Study 1 (U.S. sample, N=300), factor analysis of idiocentrism items yielded three factors -- Self-Reliance With Competition (35.2% of variance), Concern for Ingroup (13.7%), and Distance From Ingroups -- and a higher-order analysis indicated that Subordination of Ingroup Goals to Personal Goals is the most important overarching component of U.S. individualism."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["sense-of-belonging"]
    predictors: ["autonomy", "cultural-orientation"]
population:
  who: "U.S. (Illinois), Japanese, and Puerto Rican university students (plus one older Japanese adult subsample), recruited across three separate studies to measure allocentrism-idiocentrism, ingroup attention/conformity, social support, and loneliness."
  where: ["United States", "Japan", "Puerto Rico"]
  when: "mid-1980s (data collection preceding 1988 publication; exact dates not reported)"
  n: null
  sector: ["academic"]
  sample_notes: >
    Convenience samples from psychology subject pools at each site: Study 1 N=300 U.S.
    students; Study 2 N=91 Illinois, 97 Puerto Rico, 150 Japanese students plus 106 older
    Japanese adults (total Japan N=256); Study 3 N=99 Illinois and 97 Puerto Rico, with
    partial overlap with the Study 2 Puerto Rico sample. No response rates reported; the
    authors themselves flag that Japanese and Puerto Rican students may be atypically
    individualistic relative to the general population in each culture.
limitation:
  primary: "All three studies rely on convenience samples of university students (plus one small older-adult Japanese subsample), which the authors themselves note may not represent adult collectivism/individualism in Japan or Puerto Rico, limiting generalizability of the cultural comparisons."
  others:
    - "Cross-sectional, self-report, correlational design cannot establish causal direction between allocentrism, social support, and loneliness."
    - "Translation/back-translation of instruments across English, Japanese, and Spanish may introduce measurement non-equivalence, and Japanese respondents showed a scale-midpoint response bias requiring standardization before comparison."
    - "Factor structures and effect sizes varied substantially across samples and studies, indicating the individualism-collectivism/allocentrism-idiocentrism constructs are unstable and context-dependent rather than fixed, uniform traits."
risk_of_bias: "medium"
relevance_to_project: >
  Establishes a foundational, quantified link between an individual-difference trait
  (allocentrism, or ingroup-oriented self-construal) and both social support (positively)
  and loneliness (negatively), directly relevant to SNH's interest in what predicts
  loneliness and perceived support. It also warns that cultural and individual variation in
  ingroup orientation is domain- and relationship-specific, cautioning against one-size-
  fits-all social-support or community-engagement interventions for a culturally diverse
  remote workforce.
tags:
  topic: ["loneliness", "social-support", "wellbeing", "community-health", "measurement", "methodology"]
  method: ["survey", "cross-sectional"]
  population: ["students", "cross-cultural"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Triandis et al. (1988) - Individualism and Collectivism - Cross-Cultural Perspectives on Self-Ingroup Relationships/Triandis et al. (1988) - Individualism and Collectivism - Cross-Cultural Perspectives on Self-Ingroup Relationships.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Triandis et al. (1988) - Individualism and Collectivism - Cross-Cultural Perspectives on Self-Ingroup Relationships.pdf"
  notes: null

---

id: "flores-nd-understanding-the-challenges-of-remote-working"
title: "Understanding The Challenges Of Remote Working And It's Impact To Workers"
authors:
  - "Flores, Marivic F."
year: null
doi: null
venue: {type: "other", name: "Pamantasan ng Lungsod ng Maynila, College of Business and Government Management", volume: null, issue: null, pages: null}
citation: "Flores (None). Understanding The Challenges Of Remote Working And It's Impact To Workers. Pamantasan ng Lungsod ng Maynila, College of Business and Government Management."
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "weak", preregistered: false}
gist: >
  A descriptive survey of 43 remote workers at a single Philippine outsourcing firm (Pearson
  People Services) finds email is the dominant communication channel, that working
  independently and balancing work/home priorities are the top self-rated remote-work
  skills, and that flexible hours and better work-life balance are the most valued benefits.
  The same respondents rank collaborating/communicating with others as the single biggest
  challenge and separating work from home life as the hardest part of remote work, echoing
  relational-impoverishment concerns from telecommuting theory.
claims:
  - text: "Collaborating/communicating with others was the most frequently cited challenge of remote work (53.49% of respondents), followed by making technology work (44.19%) and finding information (34.88%)."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["collaboration", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
  - text: "Separating work and home life was rated the most difficult aspect of remote working, followed by developing relationships with work colleagues and having one's performance fairly evaluated."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["work-life-balance", "isolation"]
    predictors: ["boundary-management", "remote-work-intensity"]
  - text: "More flexible hours (83.72%) and better work-life balance (76.74%) were the two most valued benefits of remote work, ahead of greater control over one's time (69.77%) and job productivity/satisfaction (53.49%)."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["work-life-balance", "job-satisfaction"]
    predictors: ["autonomy", "remote-work-intensity"]
population:
  who: "43 remote employees across departments of Pearson People Services, a single company, selected by random sampling"
  where: ["Philippines"]
  when: null
  n: 43
  sector: ["business-process-outsourcing"]
  sample_notes: >
    Single-organization convenience/random sample of 43 respondents via researcher-
    constructed questionnaire; purely descriptive frequency/percentage analysis with no
    inferential statistics, response rate not reported, no validated measurement instrument
    described.
limitation:
  primary: "Small single-employer sample (n=43) analyzed only with descriptive frequencies/rankings, so findings cannot be generalized beyond this company or tested for statistical significance."
  others:
    - "Self-report questionnaire of unstated validation, susceptible to social-desirability and recall bias."
    - "No comparison group of in-office workers, so 'challenges' and 'benefits' are respondents' subjective rankings rather than measured outcomes."
risk_of_bias: "high"
relevance_to_project: >
  Provides a concrete, ranked picture of what remote workers themselves flag as hardest --
  collaboration/communication breakdowns and blurred work/home boundaries -- which is
  directly useful for prioritizing which SNH interventions (structured communication
  channels, boundary-setting supports) to design and evaluate first, even though the
  evidence base here is thin.
tags:
  topic: ["remote-work", "work-life-balance", "isolation", "collaboration"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Understanding the Challenges of Remote Working and Its Impact on Workers/Understanding the Challenges of Remote Working and Its Impact on Workers.md"
  pdf: "papers/Remote Workers/Understanding the Challenges of Remote Working and Its Impact on Workers.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "mutzel-2019-uzzi-spiro-2005-collaboration-and-creativity"
title: "Uzzi/Spiro (2005): Collaboration and Creativity: The Small World Problem"
authors:
  - "Mützel, Sophie"
year: 2019
doi: "10.1007/978-3-658-21742-6_127"
venue: {type: "book", name: "Netzwerkforschung", volume: null, issue: null, pages: "539-541"}
citation: "Mützel (2019). Uzzi/Spiro (2005): Collaboration and Creativity: The Small World Problem. Netzwerkforschung, 539-541. https://doi.org/10.1007/978-3-658-21742-6_127"
article_type: "empirical"
method: {design: "longitudinal", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Analyzing the complete network of artists who created Broadway musicals from 1945 to 1989,
  the authors show that a team's embeddedness in a 'small world' network (high clustering
  plus short path length, summarized as a small-world quotient Q) has a curvilinear,
  inverted-U relationship with both the financial and artistic success of the shows its
  members produce. Moderate connectivity and cohesion among collaborators lets novel
  material circulate with enough trust to be used, but past a threshold the same
  connectivity homogenizes the pool of ideas and rewards conventional over fresh material,
  so both under- and over-connected creative networks underperform relative to an
  intermediate 'bliss point.'
claims:
  - text: "The relationship between network small-worldliness (Q) and a musical's financial success is an inverted U: at the estimated optimum (Q about 2.6) the probability of a hit is about 2.5 times greater than at the lowest observed Q (about 1.4), and the probability of a flop drops by about 20%; both the linear and squared Q terms are significant in ordered probit models (p<.05) controlling for production size, theater location, economic conditions, and team network position."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "Artistic success (average critics' reviews) shows the same curvilinear pattern: shows are about 3 times more likely to be an artistic success at the bliss point (Q about 2.3) than at the lowest level of Q, and season-level measures (percentage of hits, percentage of rave reviews, average critics' score) also peak at intermediate Q, with the linear Q term positive and the squared term negative (p<.05) across all models."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
  - text: "The penalty for too little connectivity/cohesion is larger than the penalty for too much: about 80-85% of the season-years fall to the left of the performance-maximizing bliss point, indicating underconnected small-world structure is the more common and more costly condition; team-level network variables (closeness centrality, structural holes) added about 12 percentage points of explained variance (R2) beyond economic and talent controls in the financial-success model."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "collaboration"]
    predictors: ["network-structure", "team-cohesion"]
population:
  who: "All 2,092 freelance creative artists (composers, lyricists, librettists, choreographers, directors, producers) who worked on Broadway musicals, including 49 shows that died in preproduction"
  where: ["United States (Broadway, New York City)"]
  when: "1945-1989"
  n: 2092
  sector: ["creative-industries"]
  sample_notes: >
    Population data (not a sample) reconstructed from archival Playbill-derived directories
    (Bloom 1996; Green 1996; Simas 1987) covering 474 new musicals; complete financial-
    outcome data for 442 shows, critics'-review data for only 315-321 shows because
    systematic review scoring (Suskin 1990, 1997) is unavailable for 1982-1989, shrinking
    the artistic-success sample.
limitation:
  primary: "Entirely observational archival network data from a single industry (Broadway musical theater, 1945-1989) with no experimental manipulation of network structure, so the causal interpretation of the small-world/performance relationship rests on statistical controls rather than random assignment."
  others:
    - "Findings generalize a specific bipartite-team production context; the authors explicitly flag as open questions whether the same curvilinear pattern holds for other team-based domains (R&D labs, project teams, boards, science coauthorship) that the SNH project cares about."
    - "Network position (structural holes, repeated ties, small-world Q) is used as a proxy for the actual flow of creative material/information between teams, which is never directly observed or measured."
    - "Critics'-review data are unavailable after 1981, cutting the artistic-success sample roughly in half and limiting later-period inference."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a quantitative, transferable framework (the small-world quotient Q, balancing
  connectivity and cohesion) showing that team/community network structure has a curvilinear
  rather than 'more is always better' relationship with collaborative performance --
  directly informs how the SNH project might think about optimal levels of connectivity and
  cohesion in remote or open-source teams rather than simply maximizing ties or closeness.
tags:
  topic: ["collaboration", "productivity", "community-health", "methodology"]
  method: ["longitudinal", "secondary-data"]
  population: ["creative-industries", "teams"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Uzzi & Spiro (2005) - Collaboration and Creativity - The Small World Problem.pdf"
  notes: null

---

id: "voydanoff-1998-home-and-work-negotiating-boundaries-through"
title: "Home and Work: Negotiating Boundaries through Everyday Life"
authors:
  - "Voydanoff, Patricia"
  - "Nippert-Eng, Christena E."
year: 1998
doi: "10.2307/2654783"
venue: {type: "journal", name: "Contemporary Sociology", volume: 27, issue: 2, pages: "153"}
citation: "Voydanoff et al. (1998). Home and Work: Negotiating Boundaries through Everyday Life. Contemporary Sociology, 27(2), 153. https://doi.org/10.2307/2654783"
article_type: "commentary"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  This is Patricia Voydanoff's book review of Christena Nippert-Eng's 'Home and Work:
  Negotiating Boundaries through Everyday Life' (1996), summarizing the book's integration-
  segmentation continuum for how people manage the boundary between home and work. The
  review reports that boundary management style is shaped by workplace type (bureaucratic
  units push toward segmenting, 'greedy' units toward integrating, discretionary workplaces
  allow individual choice), by occupational norms, and by home-side expectations from
  spouses and children, with integrating occupations concentrated among higher-status
  professionals/managers and segmenting occupations disproportionately held by women.
  Voydanoff praises the book's analysis but flags its treatment of gender as underdeveloped.
claims:
  - text: "Workplace organizational culture predicts boundary-management style: bureaucratic work units encourage segmenting, 'greedy' work units engender integration, and discretionary workplaces facilitate individual choice, though this pattern is not consistent across all levels of an organization (a bureaucratic department can contain greedy work groups)."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["work-life-balance"]
    predictors: ["organizational-culture", "boundary-management"]
  - text: "Integrating occupations (blending home and work) are concentrated among professionals and managers, while women are disproportionately found in lower-status segmenting occupations, linking boundary-management style to occupational status and gender stratification."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["work-life-balance"]
    predictors: ["organizational-culture", "boundary-management"]
  - text: "Segmentors and integrators face a trade-off: segmentors have less discretion at work and more difficulty transitioning between home and work realms, but are free of the 'greediness' associated with integration, such as work-based interruptions at home and long, unpredictable work hours."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["boundary-management"]
population:
  who: "As reported in the reviewed book: 72 employees (scientists, personnel administrators, and machinists) at a major research laboratory in the northeastern United States, spanning several hierarchical levels and diverse life-course/family situations, all living with at least one significant other."
  where: ["United States"]
  when: null
  n: 72
  sector: ["other"]
  sample_notes: >
    This document is a book review, not the primary study; sample details (72 interviewees
    plus informal discussions and site visits) are taken second-hand from the reviewer's
    account of Nippert-Eng's book rather than verified against the original methodology. The
    markdown conversion also concatenates an unrelated adjacent book review from the same
    journal issue.
limitation:
  primary: "This is a secondary source (a short scholarly book review), not original empirical research, so all findings are filtered through the reviewer's summary and cannot be checked for methodological detail such as response rate or interview protocol."
  others:
    - "The underlying study drew on a single research laboratory, limiting generalizability of the integration-segmentation patterns."
    - "The reviewer explicitly notes the reviewed book's treatment of gender as a limited/underdeveloped part of its analysis of home-work boundary constraints."
risk_of_bias: "medium"
relevance_to_project: >
  Nippert-Eng's integration-segmentation continuum and the concept of 'boundary work' are
  foundational to how the SNH project can model boundary-management as a predictor of work-
  life balance and stress for remote/hybrid workers, and this review highlights
  organizational culture (bureaucratic vs. 'greedy' vs. discretionary) as a lever that could
  inform intervention or policy design.
tags:
  topic: ["work-life-balance", "remote-work"]
  method: ["qualitative", "case-study"]
  population: ["knowledge-workers"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Voydanoff (1998) - Review of Home and Work - Negotiating Boundaries through Everyday Life by Christena Nippert-Eng/Voydanoff (1998) - Review of Home and Work - Negotiating Boundaries through Everyday Life by Christena Nippert-Eng.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Voydanoff (1998) - Review of Home and Work - Negotiating Boundaries through Everyday Life by Christena Nippert-Eng.pdf"
  notes: null

---

id: "molino-2020-wellbeing-costs-of-technology-use-during"
title: "Wellbeing Costs of Technology Use during Covid-19 Remote Working: An Investigation Using the Italian Translation of the Technostress Creators Scale"
authors:
  - "Molino, Monica"
  - "Ingusci, Emanuela"
  - "Signore, Fulvio"
  - "Manuti, Amelia"
  - "Giancaspro, Maria Luisa"
  - "Russo, Vincenzo"
  - "Zito, Margherita"
  - "Cortese, Claudio G."
year: 2020
doi: "10.3390/su12155911"
venue: {type: "journal", name: "Sustainability", volume: 12, issue: 15, pages: "5911"}
citation: "Molino et al. (2020). Wellbeing Costs of Technology Use during Covid-19 Remote Working: An Investigation Using the Italian Translation of the Technostress Creators Scale. Sustainability, 12(15), 5911. https://doi.org/10.3390/su12155911"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Two self-report studies of Italian workers (N=878; N=749) validate a brief Italian
  translation of the Technostress Creators Scale (techno-overload, techno-invasion, techno-
  complexity) and then use it to model technostress during the Covid-19 lockdown. Structural
  equation modeling shows workload predicts all three techno-stressors, techno-invasion
  drives work-family conflict which in turn drives behavioural stress, and techno-
  overload/techno-complexity relate directly to stress. Remote working itself was linked to
  higher workload, techno-overload and techno-invasion, but lower work-family conflict and
  behavioural stress directly, illustrating a 'paradox' where flexibility both helps and
  harms wellbeing.
claims:
  - text: "Workload was positively associated with all three techno-stress creators (techno-invasion, techno-overload, and more weakly techno-complexity) and with work-family conflict; techno-invasion in turn predicted work-family conflict (standardized indirect effect for techno-invasion -> WFC -> behavioural stress = 0.10, 95% CI 0.04-0.11, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "stress"]
    predictors: ["workload", "technostress"]
  - text: "Techno-overload and techno-complexity showed direct positive relationships with behavioural stress (SEM model fit: CFI=0.96, TLI=0.95, RMSEA=0.06), while techno-invasion's effect on stress was fully mediated by work-family conflict; the model explained 15% of variance in behavioural stress and 38% in work-family conflict."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["technostress", "workload"]
  - text: "Remote working (controlling variable) was positively correlated with workload, techno-overload and techno-invasion (rs = .13 to .29, p<.01), yet showed a direct negative relationship with work-family conflict and behavioural stress, even as significant positive indirect paths to stress ran through workload and the techno-stressors -- a mixed 'remote work paradox' pattern."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["remote-work-intensity", "technostress"]
population:
  who: "Italian workers recruited via convenience sampling to complete an online self-report survey; Study 1 (scale validation) N=878, Study 2 (Covid-19 emergency investigation) N=749, roughly split between remote and traditional workers."
  where: ["Italy"]
  when: "Study 2 data collected April 2020 during Covid-19 lockdown; Study 1 timing not separately specified but conducted around the same period"
  n: 749
  sector: ["mixed-sectors"]
  sample_notes: >
    Convenience samples recruited online; heterogeneous across tertiary, professional
    services, education, secondary, health, and primary sectors. Authors explicitly caution
    results cannot be generalized to the Italian population given the non-random recruitment
    method.
limitation:
  primary: "Cross-sectional design precludes causal inference about the modeled paths between workload, technostress, work-family conflict and behavioural stress."
  others:
    - "All measures were self-reported by the same respondents at the same time, raising common-method-bias risk (though Harman's single-factor test ruled out a single dominant factor)."
    - "Convenience sampling with heterogeneous sectors limits generalizability to the broader Italian workforce."
    - "Only 3 of the 5 established technostress creators (excluding techno-insecurity and techno-uncertainty) were measured, and emotional distress specific to the pandemic emergency was not assessed."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a validated, short measurement instrument (11-item techno-
  overload/invasion/complexity scale) and an empirical model linking workload and remote-
  work intensity to technostress, work-family conflict and behavioural stress -- directly
  useful for the SNH project's measurement toolkit and for understanding how remote-work
  flexibility can simultaneously reduce and (via workload/technostress pathways) increase
  wellbeing risk.
tags:
  topic: ["remote-work", "technostress", "wellbeing", "work-life-balance", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["knowledge-workers", "italy"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Wellbeing Costs of Technology Use during Covid-19 Remote Working_ An Investigation Using the Italian Translation of the Technostress Creators Scale/Wellbeing Costs of Technology Use during Covid-19 Remote Working_ An Investigation Using the Italian Translation of the Technostress Creators Scale.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Wellbeing Costs of Technology Use during Covid-19 Remote Working_ An Investigation Using the Italian Translation of the Technostress Creators Scale.pdf"
  notes: null

---

id: "fonner-2010-why-teleworkers-are-more-satisfied-with"
title: "Why Teleworkers are More Satisfied with Their Jobs than are Office-Based Workers: When Less Contact is Beneficial"
authors:
  - "Fonner, Kathryn L."
  - "Roloff, Michael E."
year: 2010
doi: "10.1080/00909882.2010.513998"
venue: {type: "journal", name: "Journal of Applied Communication Research", volume: 38, issue: 4, pages: "336-361"}
citation: "Fonner et al. (2010). Why Teleworkers are More Satisfied with Their Jobs than are Office-Based Workers: When Less Contact is Beneficial. Journal of Applied Communication Research, 38(4), 336-361. https://doi.org/10.1080/00909882.2010.513998"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Comparing 89 high-intensity teleworkers (working remotely 3+ days/week) to 103 office-
  based employees, this study finds teleworkers report significantly higher job
  satisfaction, and uses multiple mediation and path analysis to show why: teleworkers
  experience less work-life conflict, less stress from meetings/interruptions, and less
  perceived organizational politics, with work-life conflict emerging as the strongest and
  most robust mediator of the telework-satisfaction link. Contrary to the assumption that
  reduced face-to-face contact harms teleworkers, the paper argues restricted interaction
  filters out stressful and political aspects of collocated work rather than causing
  isolation, though teleworkers also exchange information significantly less frequently.
claims:
  - text: "High-intensity teleworkers (working remotely at least 3 days/week) reported significantly greater job satisfaction than office-based employees, with a significant direct effect (B = 0.62, SE = 0.19, p < .01) and total effect (B = 0.82, SE = 0.23, p < .001) of telework on satisfaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Work-life conflict was the most influential and most consistent mediator: teleworkers reported significantly lower work-life conflict than office-based employees (B = -0.56, p < .05), and work-life conflict was significantly negatively related to job satisfaction (B = -0.21, p < .001), with the indirect path remaining significant in both the preliminary mediation model and the final revised path model (95% CI .000 to .075)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "work-life-balance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Teleworkers exchanged information with colleagues significantly less frequently than office-based employees (B = -0.79, p < .001), and reported perceiving significantly less general organizational politics (B = -0.42/-0.41, p < .05), which in the final path model mediated satisfaction via a chain from reduced general politics to reduced 'going along to get ahead' politics to higher satisfaction (95% CI .001 to .097); stress from meetings/interruptions and information exchange quality did not directly predict satisfaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "communication"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "Working adults in the US self-selecting as either high-intensity teleworkers (remote 3+ days/week, n=89) or office-based employees (collocated 3+ days/week, n=103), recruited via personal/alumni email contacts and two telework-focused websites (Telework Coalition, Gil Gordon Associates)"
  where: ["United States"]
  when: null
  n: 192
  sector: ["mixed"]
  sample_notes: >
    Convenience/snowball sample, not randomly selected; teleworkers were significantly
    older, had longer job and organizational tenure, and were more likely married with
    children than office-based employees (controlled for as covariates); self-report survey
    data; 11 participants excluded post-hoc for not meeting work-arrangement criteria; data
    collected as part of first author's dissertation, published 2010 but likely fielded
    several years earlier.
limitation:
  primary: "Non-random, self-selected convenience sample of high-intensity teleworkers and office workers with significant demographic differences between groups (age, tenure, marital/parental status), limiting representativeness and causal inference."
  others:
    - "Self-report measures may exaggerate teleworkers' satisfaction as a rationalization of their chosen flexible arrangement."
    - "Cross-sectional design cannot establish causal direction or rule out selection effects (who chooses to telework)."
    - "Only partial mediation was found and the initial path model fit poorly (CFI=.66); the revised model was derived post hoc via modification indices, raising overfitting concerns."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH question of whether reduced face-to-face/social contact among
  remote workers is inherently harmful: this study's mediation evidence suggests that for
  high-intensity teleworkers, reduced contact functions as a filter against work-life
  conflict, meeting/interruption stress, and organizational politics rather than producing
  isolation, which should inform how the project weighs 'less contact' against connectedness
  in its design and measurement choices.
tags:
  topic: ["remote-work", "job-satisfaction", "work-life-balance", "communication"]
  method: ["survey", "cross-sectional", "mediation-analysis"]
  population: ["remote-workers", "office-workers", "us-workforce"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Why Teleworkers are More Satisfied with Their Jobs than are Office-Based Workers  When Less Contact is Beneficial/Why Teleworkers are More Satisfied with Their Jobs than are Office-Based Workers  When Less Contact is Beneficial.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Why Teleworkers are More Satisfied with Their Jobs than are Office-Based Workers  When Less Contact is Beneficial.pdf"
  notes: null

---

id: "seinsche-2024-working-from-home-during-covid-19"
title: "Working from home during COVID-19: boundary management tactics and energy resources management strategies reported by public service employees in a qualitative study"
authors:
  - "Seinsche, Laura"
  - "Schubin, Kristina"
  - "Neumann, Jana"
  - "Pfaff, Holger"
year: 2024
doi: "10.1186/s12889-024-18744-y"
venue: {type: "journal", name: "BMC Public Health", volume: 24, issue: 1, pages: null}
citation: "Seinsche et al. (2024). Working from home during COVID-19: boundary management tactics and energy resources management strategies reported by public service employees in a qualitative study. BMC Public Health, 24(1). https://doi.org/10.1186/s12889-024-18744-y"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: true}
gist: >
  Based on 12 semi-structured telephone interviews with German public service employees
  roughly a year and a half into the COVID-19 pandemic, this study inductively and
  deductively codes the boundary-management tactics (communicative, physical, temporal,
  behavioral) and energy-management strategies (preventing exhaustion, physical exercise,
  healthy eating, working while sick) employees improvised to cope with mandatory work-from-
  home. It links these job-crafting tactics to the JD-R model and Hobfoll's Conservation of
  Resources theory, and surfaces a presenteeism risk: employees frequently kept working
  through mild illness at home rather than taking sick leave, partly out of collegial
  obligation and partly because on-site duty-of-care oversight from managers disappears in
  remote settings.
claims:
  - text: "Employees used four categories of boundary tactics consistent with Kreiner et al.'s (2009) taxonomy - communicative (e.g., negotiating availability, setting status in Teams/Skype, team-agreed 'no email after 8pm' norms), physical (e.g., separating workspace, taking walks), temporal (e.g., logging off, banking flexible time), and behavioral (e.g., flight-mode phone, daily task prioritization) - with new inductive sub-categories such as 'no tactic' and 'situation COVID-19' capturing cases where boundaries could not be maintained (e.g., unplanned doorbell interruptions)."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["boundary-management", "autonomy", "organizational-culture"]
  - text: "Energy-management strategies clustered into preventing exhaustion (e.g., power naps, lunch breaks, following one's own rhythm), physical exercise integrated into breaks (e.g., exercising during the freed-up commute time, walking while on calls), and healthy cooking, all framed as job resources that buffer job demands and support recovery consistent with the JD-R model and COR theory."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["wellbeing", "stress", "burnout"]
    predictors: ["boundary-management", "autonomy"]
  - text: "When sick, employees' decisions to work from home rather than take formal sick leave depended on self-assessed illness severity and a felt obligation of collegiality (being reachable for colleagues), and several participants explicitly worked through mild illness at home in ways they would not have on-site, which the authors interpret as evidence of an emerging presenteeism culture and 'interested self-endangerment' in remote work, exacerbated by managers' reduced ability to observe and send unwell employees home when remote."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["wellbeing", "burnout", "job-engagement"]
    predictors: ["boundary-management", "organizational-culture", "leadership-style"]
population:
  who: "12 public service (Öffentlicher Dienst) employees in Germany, purposively sampled for variation in gender, age, leadership position, job role, and WFH duration/agency implementation, all recruited from an earlier spring-2021 web survey"
  where: ["Germany"]
  when: "interviews conducted December 2021 to February 2022"
  n: 12
  sector: ["public-sector", "government"]
  sample_notes: >
    Small purposive sample skewed older (many participants over 50, mostly without children
    at home) and male (women underrepresented relative to the ~57% female share of German
    public service, partly reflecting women's underrepresentation in higher
    service/leadership roles); recruited from a prior survey's opt-in contacts, so likely
    self-selected toward those more comfortable with or interested in WFH; single time
    point, one year+ into the pandemic, so does not capture earlier acute-crisis
    experiences.
limitation:
  primary: "Small (n=12), non-representative, self-selected qualitative sample of one national public-sector workforce at one time point, limiting generalizability to other sectors, countries, or work arrangements (e.g., hybrid work)."
  others:
    - "Sample skews older and male relative to the German public-service workforce, and excludes employees who could not perform their jobs at all from home, introducing selection bias."
    - "Findings capture mandatory pandemic-era WFH rather than voluntary or hybrid arrangements, limiting transfer to post-pandemic hybrid contexts the authors themselves flag as a research gap."
    - "Interview quotes were translated from German to English by a single author, introducing potential translation/interpretation drift."
risk_of_bias: "low"
relevance_to_project: >
  Offers a concrete, empirically-grounded taxonomy of boundary-management and energy-
  management tactics (communicative, physical, temporal, behavioral) that SNH could use to
  structure remote-worker self-assessment tools or nudges, and flags a specific, actionable
  risk mechanism - remote presenteeism driven by loss of manager-observable duty-of-care and
  by team collegiality norms - as a target for intervention design (e.g., status-signaling
  defaults, explicit sick-leave norms for remote workers).
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing", "burnout"]
  method: ["qualitative", "interview"]
  population: ["public-sector", "germany", "remote-workers"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Working from Home During COVID-19 - Boundary Management Tactics and Energy Resources Management Strategies in Public Service/Working from Home During COVID-19 - Boundary Management Tactics and Energy Resources Management Strategies in Public Service.md"
  pdf: "papers/Remote Workers/Working from Home During COVID-19 - Boundary Management Tactics and Energy Resources Management Strategies in Public Service.pdf"
  notes: null

---

id: "adam-2019-workplace-isolation-occurring-in-remote-workers"
title: "Workplace Isolation Occurring in Remote Workers"
authors:
  - "Adam Hickman"
year: 2019
doi: null
venue: {type: "thesis", name: "Walden University", volume: null, issue: null, pages: null}
citation: "Adam Hickman (2019). Workplace Isolation Occurring in Remote Workers. Walden University."
article_type: "empirical"
method: {design: "qualitative-multiple-case-study", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  This 2019 Walden University dissertation used semistructured interviews with 21 remote
  customer-service workers across four company divisions, plus a review of training
  documentation, to explore how workplace isolation influences remote-employee performance.
  Using Emerson's social exchange theory as the conceptual framework, holistic and pattern
  coding surfaced eight emergent themes, including clear role expectations, unaffected peer-
  to-peer relationships, time-zone-driven isolation, and manager-employee communication
  gaps. Contrary to the reviewed literature, most participants reported that experienced
  isolation did not harm and sometimes improved their performance by removing distractions.
claims:
  - text: "All 21 participants (100%) reported that isolation occurs most when working on complex, independent tasks requiring more than an hour of focused attention."
    evidence: "Coded pattern from interview Question 6 (Emergent Theme 5/1), corroborated across all four divisions."
    support_strength: "low"
    outcomes: ["isolation"]
    predictors: ["workload"]
  - text: "15 of 21 participants (71%) said workplace isolation did not negatively affect their performance, and 9 (38%) said it improved focus by reducing workplace distractions, contradicting prior literature suggesting isolation impedes performance."
    evidence: "Coded pattern from interview Question 7 (Emergent Theme 6/5)."
    support_strength: "low"
    outcomes: ["performance", "isolation"]
    predictors: []
  - text: "Only 5 of 21 participants (24%) discussed their experience of workplace isolation with their manager, and typically only after it became a problem; 16 (76%) never raised it because they did not view it as an issue."
    evidence: "Coded pattern from interview Question 9 (Emergent Theme 7), interpreted through the social exchange conceptual framework."
    support_strength: "low"
    outcomes: ["help-seeking", "communication"]
    predictors: ["leadership-style"]
population:
  who: "21 remote employees (business development managers, software engineers, talent development specialists, product managers) across 4 divisions of one U.S. customer-service organization"
  where: ["United States"]
  when: "2019"
  n: 21
  sector: ["customer service", "technology/business services"]
  sample_notes: >
    Purposive sample of remote workers from four divisions of a single organization; 15 men
    and 6 women; interviews averaged 27 minutes each.
limitation:
  primary: "Single-organization, small purposive sample (n=21) with self-reported interview data limits generalizability and transferability beyond the studied customer-service company."
  others:
    - "Qualitative case-study design and researcher-as-instrument coding introduce potential for interpretive/researcher bias despite trustworthiness procedures."
    - "Findings that isolation did not harm performance rely entirely on participant self-report, with no objective performance measures triangulated against interview claims."
risk_of_bias: "high"
relevance_to_project: >
  Provides qualitative, worker-voiced evidence that remote-worker isolation is often self-
  managed and can coexist with (or even benefit) performance, while highlighting concrete
  organizational gaps -- inconsistent event communication, low manager-isolation dialogue,
  and missing remote-management training -- that SNH interventions could target.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "measurement"]
  method: ["qualitative", "case-study"]
  population: ["remote-workers", "customer-service"]
source:
  markdown: "Papers_Data/Remote Workers/MD/Workplace Isolation Occurring in Remote Workers/Workplace Isolation Occurring in Remote Workers.md"
  pdf: "papers/Remote Workers/Workplace Isolation Occurring in Remote Workers.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "xanthopoulou-2009-reciprocal-relationships-between-job-resources-personal"
title: "Reciprocal relationships between job resources, personal resources, and work engagement"
authors:
  - "Xanthopoulou, Despoina"
  - "Bakker, Arnold B."
  - "Demerouti, Evangelia"
  - "Schaufeli, Wilmar B."
year: 2009
doi: "10.1016/j.jvb.2008.11.003"
venue: {type: "journal", name: "Journal of Vocational Behavior", volume: 74, issue: 3, pages: "235-244"}
citation: "Xanthopoulou et al. (2009). Reciprocal relationships between job resources, personal resources, and work engagement. Journal of Vocational Behavior, 74(3), 235-244. https://doi.org/10.1016/j.jvb.2008.11.003"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using two-wave survey data (18 months apart) from 163 Dutch employees, this study tests
  whether job resources, personal resources, and work engagement relate reciprocally over
  time, drawing on Conservation of Resources theory. Structural equation modeling showed a
  fully reciprocal model fit the data far better than models allowing resources to predict
  engagement only, or engagement to predict resources only: job and personal resources each
  predicted later work engagement, engagement predicted later job and personal resources,
  and job resources and personal resources predicted each other. The findings support a
  self-reinforcing cycle among workplace resources and engagement rather than a simple one-
  directional causal chain, though absolute levels of resources and engagement did not
  increase over time.
claims:
  - text: "The reciprocal model (job resources, personal resources, and work engagement all mutually predicting each other over 18 months) fit the data significantly better than stability, resources-to-engagement-only, or engagement-to-resources-only models (chi-square=6.60, df=10, p=.762, CFI/IFI/TLI=1.00, RMSEA=.01), and explained 16% of variance in T2 job resources, 20% in T2 personal resources, and 21% in T2 work engagement."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["job-engagement", "wellbeing"]
    predictors: ["social-support", "autonomy"]
  - text: "T1 job resources (autonomy, social support, coaching, feedback, development opportunities; standardized path=.19, p<.01) and T1 personal resources (self-efficacy, organization-based self-esteem, optimism; path=.18, p<.01) each uniquely predicted T2 work engagement."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["social-support", "autonomy", "hope"]
  - text: "T1 work engagement predicted T2 job resources (path=.26, p<.001) and T2 personal resources (path=.23, p<.001), and job resources and personal resources also predicted each other reciprocally across time, indicating engaged employees actively mobilize or build both job and personal resources rather than only being a downstream outcome."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["job-engagement"]
    predictors: ["social-support", "hope"]
population:
  who: "Employees of a single electrical engineering and electronics company in the Netherlands, matched across two survey waves (three divisions: HR, Industry, Commercial/Economic Management)"
  where: ["Netherlands"]
  when: null
  n: 163
  sector: ["technology", "manufacturing"]
  sample_notes: >
    T1 N=540 of 1121 invited (48% response), T2 N=469 of 1016 invited (46% response); only
    163 employees participated in both waves (30% of T1 sample). Panel-loss analysis found
    no significant differences between the 163 retained and 377 dropouts on demographics or
    study variables. Final panel was 80% male, mean age 42, mean tenure 14 years.
limitation:
  primary: "All measures were self-report, raising common-method-variance concerns, though Harman's single-factor test and the longitudinal design partially mitigate this."
  others:
    - "Single organization with a relatively small matched panel (N=163) limits generalizability to other occupations and settings."
    - "Longitudinal design does not establish causality; an unmeasured third variable could produce the observed cross-lagged effects."
    - "The two-wave, ~18-month lag was chosen for pragmatic (legal reporting) reasons rather than derived from theory, and cannot distinguish cyclical maintenance from genuine gain spirals since mean levels of resources/engagement did not increase over time."
risk_of_bias: "medium"
relevance_to_project: >
  Provides longitudinal, quantitative evidence that social/job resources (notably social
  support and coaching) and personal resources (self-efficacy, optimism, self-esteem) form a
  reciprocal cycle with work engagement rather than a one-way antecedent-outcome chain —
  directly informing SNH's model that interventions boosting social support or belonging can
  both result from and further fuel engagement, useful for justifying feedback-loop rather
  than single-cause designs for remote-worker engagement interventions.
tags:
  topic: ["job-engagement", "wellbeing", "social-support"]
  method: ["longitudinal", "survey", "quantitative"]
  population: ["office-workers", "netherlands"]
source:
  markdown: "Papers_Data/Remote Workers/01 Extended - Remote Workers/MD/Xanthopoulou et al. (2009) - Reciprocal Relationships Between Job Resources, Personal Resources, and Work Engagement/Xanthopoulou et al. (2009) - Reciprocal Relationships Between Job Resources, Personal Resources, and Work Engagement.md"
  pdf: "papers/Remote Workers/01 Extended - Remote Workers/Xanthopoulou et al. (2009) - Reciprocal Relationships Between Job Resources, Personal Resources, and Work Engagement.pdf"
  notes: null
