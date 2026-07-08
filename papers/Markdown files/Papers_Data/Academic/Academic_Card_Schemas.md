# Card Schemas - Academic

<!-- GENERATED FILE - do not edit. Source of truth is each paper's
     MD/<paper>/card_schema.md. Regenerate with:
     python3 tools/audit/build_combined_cards.py -->

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

---

id: "oakman-2020-a-rapid-review-of-mental-and"
title: "A rapid review of mental and physical health effects of working at home: how do we optimise health?"
authors:
  - "Oakman, Jodi"
  - "Kinsman, Natasha"
  - "Stuckey, Rwth"
  - "Graham, Melissa"
  - "Weale, Victoria"
year: 2020
doi: "10.1186/s12889-020-09875-z"
venue: {type: "journal", name: "BMC Public Health", volume: 20, issue: 1, pages: null}
citation: "Oakman et al. (2020). A rapid review of mental and physical health effects of working at home: how do we optimise health?. BMC Public Health, 20(1). https://doi.org/10.1186/s12889-020-09875-z"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This rapid review synthesizes 23 peer-reviewed studies (2007-2020) on the mental and
  physical health effects of working at home (WAH), finding ten distinct health outcomes
  (pain, self-reported health, safety, well-being, stress, depression, fatigue, quality of
  life, strain, happiness) whose direction depended heavily on organisational support,
  colleague support, social connectedness outside work, and work-family conflict. It reports
  a consistent gender asymmetry, with women less likely than men to experience improved
  health when WAH, and translates the findings into practice recommendations covering
  organisational, co-worker, technical, and boundary-management support for employers
  formalising WAH policies.
claims:
  - text: "Across the 23 included studies, the effect of WAH on health outcomes was strongly moderated by degree of organisational/manager support, colleague support, social connectedness outside of work, and level of work-to-family conflict; overall women were less likely than men to experience improved health outcomes when working at home."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["wellbeing", "stress", "mental-health"]
    predictors: ["social-support", "boundary-management", "remote-work-intensity"]
  - text: "In studies with gender-stratified analysis, males more often showed protective effects (e.g. Kim et al. 2020: WAH men had lower fatigue and stress; Gimenez-Nadal et al. 2020: male teleworkers had significantly lower pain, stress and tiredness than commuters, p<0.05), while women showed mixed or negative effects (e.g. women in the same Kim et al. study had lower stress but higher fatigue; Windeler et al. 2017 found women who teleworked had higher work exhaustion than office-based peers)."
    evidence: "review-systematic"
    support_strength: "low-to-moderate"
    outcomes: ["stress", "burnout", "wellbeing"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Physical health was addressed by only 3 of 23 studies versus 21 studies on mental health; of quantitative studies, risk-of-bias assessment rated 4 as high, 3 as moderate, and 13 as low risk, and the predominance of cross-sectional designs (20 of 23 studies, no RCTs) precluded any meta-analysis or causal conclusions."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["wellbeing", "stress"]
    predictors: ["sampling-method"]
population:
  who: "23 peer-reviewed studies of adult white-collar/professional employees regularly working at home during business hours (19 quantitative, 3 qualitative, 1 mixed-methods); individual study samples ranged from n=7 to n=9200"
  where: ["USA", "UK", "Australia", "New Zealand", "Japan", "Belgium", "South Africa", "Brazil", "Germany", "Netherlands"]
  when: "primary studies published 2007-2020, searched May 2020"
  n: null
  sector: ["government", "financial-services", "technology", "academia", "telecommunications", "logistics"]
  sample_notes: >
    1557 records screened, 21 met inclusion criteria plus 2 added via reference-list search
    (23 total); only one study examined mandatory full-time WAH, the rest covered
    voluntary/part-time arrangements, so findings predate and may not generalise to
    pandemic-mandated WAH.
limitation:
  primary: "20 of 23 included studies were cross-sectional (no RCTs, only one cohort/controlled before-after design), so the review's conclusions about organisational support and gender differences are correlational, not causal."
  others:
    - "Heterogeneity of health outcome measures across studies prevented meta-analysis, limiting synthesis to narrative review."
    - "Search restricted to English-language peer-reviewed journal articles in three databases; no grey literature was searched, which the authors note may explain the very low number of physical-health studies found."
    - "Only one included study examined mandatory (vs voluntary) WAH, so recommendations aimed at pandemic-era mandated WAH are extrapolated from largely voluntary-telework evidence."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's remote-worker design priorities by identifying
  organisational support, co-worker/colleague support, and social connectedness outside of
  work as the key moderators that determine whether WAH improves or harms mental health, and
  by flagging boundary-management and gendered work-family conflict as specific intervention
  targets for policy and tooling design.
tags:
  topic: ["remote-work", "wellbeing", "mental-health", "social-support", "burnout", "work-life-balance"]
  method: ["review-systematic", "secondary-data"]
  population: ["remote-workers", "white-collar", "gender-differences"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/A Rapid Review of Mental and Physical Health Effects of Working at Home How Do We Optimise Health/A Rapid Review of Mental and Physical Health Effects of Working at Home How Do We Optimise Health.md"
  pdf: "papers/Academic/01 Academic - Extended/A Rapid Review of Mental and Physical Health Effects of Working at Home How Do We Optimise Health.pdf"
  notes: null

---

id: "almeida-2024-a-snapshot-of-the-mental-health"
title: "A Snapshot of the Mental Health of Software Professionals"
authors:
  - "Almeida, Eduardo  Santana de"
  - "Nunes, Ingrid  Oliveira de"
  - "Oliveira, Raphael  Pereira de"
  - "Carvalho, Michelle  Larissa Luciano"
  - "Brunoni, André Russowsky"
  - "Rong, Shiyue"
  - "Ahmed, Iftekhar"
year: 2024
doi: "10.2139/ssrn.4849630"
venue: {type: "preprint", name: null, volume: null, issue: null, pages: null}
citation: "Almeida et al. (2024). A Snapshot of the Mental Health of Software Professionals.. https://doi.org/10.2139/ssrn.4849630"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A cross-sectional survey of 500 software professionals from 35 countries found that 30.2%
  had been diagnosed with a mental health disorder (past or current), with anxiety (20.6%)
  and depression (14.8%) most common, and that 25.2% scored as having moderately severe or
  severe depression on the PHQ-9. Using Spearman correlations, the study identifies work-
  nature, work-environment, and work-schedule factors (freelance work type, the test-
  engineer role, home-office work before COVID-19, unrealistic deadlines, abrupt task
  changes, and working more hours than expected) that are associated with a history of
  mental health disorders, while a healthy relationship with colleagues is associated with
  lower odds. It also documents that leisure, social, and family time dropped significantly
  during the COVID-19 pandemic and was already lower among professionals with a history of
  mental health disorders.
claims:
  - text: "30.2% (151/500) of software professionals reported being diagnosed with a mental health disorder in the past or currently; anxiety (20.6%, 103/500) and depression (14.8%, 74/500) were most common, and 25.2% (126/500) scored as moderately severe or severe depression on the PHQ-9, including 19.4% of those with no prior diagnosed history."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "depression", "anxiety"]
    predictors: []
  - text: "Freelance work type (Spearman rho=0.09, p=0.03) and the test-engineer role (rho=0.15, p=0.0004) were positively associated with a history of mental health disorders, while working for an organization was negatively associated (rho=-0.10, p=0.02); organization size and team size showed no significant correlation."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health"]
    predictors: ["remote-work-intensity", "workload"]
  - text: "Working more actual hours than expected (Cohen's d=-0.27 all respondents; -0.21 for those with mental health history), unrealistic deadlines, abruptly changed tasks, and pre-pandemic home-office work were each significantly correlated with a history of mental health disorders, whereas a strongly agreed healthy relationship with colleagues was associated with lower odds (rho=-0.10, p=0.02); leisure, social activity, hobby, and family time all declined significantly during COVID-19 (largest effect: social activities, Cohen's d=1.97)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "burnout", "work-life-balance"]
    predictors: ["workload", "remote-work-intensity", "team-cohesion", "boundary-management"]
population:
  who: "500 software professionals (developers, architects, project managers, test engineers, and others) recruited via social media, convenience sampling, and snowballing"
  where: ["Brazil", "Germany", "USA", "France", "31 other countries (35 total)"]
  when: "May-July 2021"
  n: 500
  sector: ["software-industry", "open-source", "private-organization", "freelance"]
  sample_notes: >
    Convenience/snowball sample skewed heavily toward Brazil (74.8%); 82% male; anonymous,
    self-selected, non-probability recruitment via authors' personal networks, so not
    representative of the global software workforce; 503 raw responses with 3 disqualified
    (2 non-consenting, 1 duplicate).
limitation:
  primary: "Convenience/snowball sampling via authors' personal networks and social media produces a non-representative, geographically skewed sample (nearly 75% Brazil, 82% male), limiting generalizability despite the large N."
  others:
    - "Cross-sectional design precludes causal claims about which work characteristics trigger mental health disorders versus merely co-occurring with them."
    - "Self-reported diagnosis history and PHQ-9 screening are not clinician-verified diagnoses."
    - "Many correlations, while statistically significant, have small effect sizes (rho often below 0.15), so practical significance is limited."
risk_of_bias: "medium"
relevance_to_project: >
  Provides base-rate evidence (30.2% disorder prevalence, 25.2% moderate-to-severe
  depression by PHQ-9) and specific workplace predictors (freelance status, unrealistic
  deadlines, abrupt task changes, excess hours, home-office work, colleague relationship
  quality) that the SNH project can use to prioritize which remote-work and community
  stressors to target with interventions, and to justify measuring colleague relationship
  quality and workload predictability as levers for wellbeing.
tags:
  topic: ["mental-health", "remote-work", "burnout", "work-life-balance", "wellbeing"]
  method: ["survey", "cross-sectional"]
  population: ["software-professionals", "open-source", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/MD/A Snapshot of the Mental Health of Software Professionals/A Snapshot of the Mental Health of Software Professionals.md"
  pdf: "papers/Academic/A Snapshot of the Mental Health of Software Professionals.pdf"
  notes: null

---

id: "wells-2023-a-systematic-review-of-the-impact"
title: "A Systematic Review of the Impact of Remote Working Referenced to the Concept of Work–Life Flow on Physical and Psychological Health"
authors:
  - "Wells, John"
  - "Scheibein, Florian"
  - "Pais, Leonor"
  - "Rebelo dos Santos, Nuno"
  - "Dalluege, C.- Andreas"
  - "Czakert, Jan Philipp"
  - "Berger, Rita"
year: 2023
doi: "10.1177/21650799231176397"
venue: {type: "journal", name: "Workplace Health &amp; Safety", volume: 71, issue: 11, pages: "507-521"}
citation: "Wells et al. (2023). A Systematic Review of the Impact of Remote Working Referenced to the Concept of Work–Life Flow on Physical and Psychological Health. Workplace Health &amp; Safety, 71(11), 507-521. https://doi.org/10.1177/21650799231176397"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "low-to-moderate", preregistered: true}
gist: >
  This PRISMA/PROSPERO-registered systematic review synthesizes 34 empirical studies (from
  830 screened, 2020-2021) on the physical and psychological health impacts of remote
  working during COVID-19, evaluating each finding's certainty with the GRADE approach. Most
  findings were rated low to very-low certainty due to cross-sectional designs, small
  samples, and inconsistent WFH measurement, while only a minority (reduced infection risk,
  reduced physical activity, increased sedentary/screen time) reached high certainty. The
  review argues for adopting a 'work-life flow' framework over strict work-life balance and
  recommends an expanded role for occupational health nurses in supporting remote workers'
  physical and psychological well-being.
claims:
  - text: "A minority of included studies reached high-certainty (GRADE) evidence: working from home was associated with reduced physical activity and increased sedentary behavior (e.g., sitting time 335.7 vs. 224.7 minutes in WFH vs. non-WFH groups; Fukushima et al., 2021) and increased screen time (McDowell et al., 2020), while telework was also associated with reduced risk of SARS-CoV-2 infection (Fischer et al., 2020)."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["wellbeing", "stress"]
    predictors: ["remote-work-intensity"]
  - text: "Moderate-certainty evidence found WFH was associated with increased loneliness and that loneliness predicted increased emotional exhaustion; perceived job autonomy was negatively correlated with loneliness, while higher workload was linked to greater work-home interference and exhaustion (Wang et al., 2020)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["loneliness", "burnout", "work-life-balance"]
    predictors: ["autonomy", "workload", "remote-work-intensity"]
  - text: "Switching off the camera or microphone during video meetings and higher perceived group belonging were associated (moderate certainty) with decreased videoconferencing fatigue, whereas WFH itself was linked to increased 'zoom fatigue' and vocal tract discomfort/dysphonia, with women and new employees particularly prone to video fatigue (Bennett et al., 2021; Shockley et al., 2021; Kenny, 2020)."
    evidence: "review-systematic"
    support_strength: "moderate"
    outcomes: ["stress", "sense-of-belonging"]
    predictors: ["sense-of-belonging", "remote-work-intensity"]
population:
  who: "34 empirical studies of remote/telework populations during the COVID-19 pandemic, including remote workers, general population subsets, healthcare workers, academic/education staff, parents/carers, and embassy staff; individual study samples ranged from n=4 to n=270,000."
  where: ["Europe", "North America", "Asia", "South America", "Africa", "Australia"]
  when: "2020-2021"
  n: 34
  sector: ["healthcare", "education", "general-workforce"]
  sample_notes: >
    830 records identified, 250 duplicates removed, 579 screened, 92 assessed for
    eligibility, 34 included; most studies were cross-sectional surveys (n=26) vs.
    longitudinal (n=8); English-language only, reviews/commentaries/single-case reports
    excluded.
limitation:
  primary: "Included studies were highly heterogeneous in design, population, and how WFH was operationalized, and most were rated low-to-very-low certainty by GRADE, so the review's synthesized findings warrant cautious interpretation."
  others:
    - "The short 2020-2021 timeframe captures only the acute pandemic phase, limiting generalizability to voluntary or long-term remote work."
    - "Exclusion of non-English-language studies and of reviews, commentaries, and single-case reports may have omitted relevant evidence."
    - "Only 3 of 34 included studies achieved high-certainty evidence ratings; most conclusions rest on low or very-low certainty single studies."
risk_of_bias: "low"
relevance_to_project: >
  Offers a GRADE-rated evidence map of WFH health impacts useful for calibrating confidence
  when citing individual remote-work studies elsewhere in the corpus, and documents a
  specific evidence chain (low job autonomy and high workload predicting increased
  loneliness and emotional exhaustion) directly relevant to SNH's isolation and burnout
  mechanisms in remote work design decisions.
tags:
  topic: ["remote-work", "isolation", "loneliness", "burnout", "wellbeing", "methodology"]
  method: ["review-systematic", "secondary-data"]
  population: ["remote-workers", "healthcare-workers", "general-population"]
source:
  markdown: "Papers_Data/Academic/MD/A Systematic Review of the Impact of Remote Working Referenced to the Concept of Work–Life Flow on Physical and Psychological Health/A Systematic Review of the Impact of Remote Working Referenced to the Concept of Work–Life Flow on Physical and Psychological Health.md"
  pdf: null
  notes: null

---

id: "wang-2021-achieving-effective-remote-working-during-the"
title: "Achieving Effective Remote Working During the COVID‐19 Pandemic: A Work Design Perspective"
authors:
  - "Wang, Bin"
  - "Liu, Yukun"
  - "Qian, Jing"
  - "Parker, Sharon K."
year: 2021
doi: "10.1111/apps.12290"
venue: {type: "journal", name: "Applied Psychology", volume: 70, issue: 1, pages: "16-59"}
citation: "Wang et al. (2021). Achieving Effective Remote Working During the COVID‐19 Pandemic: A Work Design Perspective. Applied Psychology, 70(1), 16-59. https://doi.org/10.1111/apps.12290"
article_type: "empirical"
method: {design: "mixed-methods", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Using 39 semi-structured interviews with Chinese remote workers in early 2020 (Study 1)
  followed by a cross-sectional survey of 522 Chinese employees working from home during
  COVID-19 (Study 2), the authors identify four remote-work challenges (work-home
  interference, ineffective communication, procrastination, loneliness) and show these are
  shaped by four virtual work characteristics (social support, job autonomy, monitoring,
  workload) plus workers' self-discipline. Social support emerged as the most broadly
  beneficial characteristic, negatively linked to all four challenges and, through them, to
  better performance and wellbeing, while workload and monitoring increased work-home
  interference and job autonomy unexpectedly reduced loneliness rather than work-home
  interference.
claims:
  - text: "Social support was negatively associated with all four remote-work challenges (procrastination b=-.17***, work-to-home interference b=-.27***, home-to-work interference b=-.16**, loneliness b=-.20***) and, via these mediators, was linked to higher self-reported performance, lower emotional exhaustion, and higher life satisfaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness", "wellbeing", "performance", "burnout"]
    predictors: ["social-support"]
  - text: "Workload (b=.38**) and monitoring (b=.22***) both increased work-to-home interference, which in turn predicted higher emotional exhaustion and lower life satisfaction; workload also reduced procrastination (b=-.18*), but monitoring did not, contrary to what interviewees expected."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "burnout", "wellbeing"]
    predictors: ["workload", "monitoring"]
  - text: "Job autonomy was negatively related to loneliness (b=-.18***) rather than to work-home interference as hypothesized, and self-discipline moderated two key paths: social support reduced procrastination only for less self-disciplined workers, while social support reduced loneliness only for more self-disciplined workers."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["loneliness"]
    predictors: ["autonomy", "self-discipline"]
population:
  who: "Study 1: 39 Chinese full-time employees (across education, IT, media, finance, etc.) forced to work from home in the early COVID-19 lockdown, interviewed via audio/video call. Study 2: 522 Chinese employees (271 female, 51.9%) working from home or recently returned to the office after doing so during the pandemic, recruited from a commercial online panel."
  where: ["China"]
  when: "February 2020 onward (early COVID-19 pandemic lockdown in mainland China)"
  n: 522
  sector: ["general-workforce"]
  sample_notes: >
    Study 2 participants recruited and paid via WJX, a Chinese online panel comparable to
    MTurk/Prolific (final analytic N=515-522 due to missing data); self-selected paid panel
    respondents, mean age ~32, 30.8% managers, mixed industries (IT 26.6%, education 15.5%,
    manufacturing 12.5%). Study 1 sample was small (n=39) and concentrated in mainland
    Chinese cities (15 from Beijing).
limitation:
  primary: "Study 2's cross-sectional, single-source (self-report) survey design cannot establish causality and is vulnerable to common method bias, as the authors themselves note."
  others:
    - "Both studies were conducted only in China, limiting generalizability to countries where remote work is more established and culturally normalized."
    - "Data were collected during an unusual early-pandemic lockdown context (mandatory, sudden remote work plus pandemic-specific stressors), which may not generalize to voluntary or steady-state remote/hybrid work."
    - "Monitoring, workload, and self-discipline measures were relatively brief/ad hoc scales (e.g., a 4-item checklist for monitoring), and the job-autonomy mean was unusually high, potentially reflecting a ceiling effect specific to this sample."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs which virtual work characteristics an SNH intervention should target:
  social support is shown to be the single most consistently protective factor against
  loneliness, work-home interference, and procrastination, while surveillance-style
  monitoring shows no upside and adds work-home interference costs. The self-discipline
  moderation results also suggest support-based interventions should be aimed especially at
  less self-disciplined remote workers to curb procrastination, while autonomy-based
  interventions may do more to reduce loneliness than monitoring or workload changes.
tags:
  topic: ["remote-work", "loneliness", "social-support", "wellbeing", "work-life-balance", "burnout"]
  method: ["mixed-methods", "cross-sectional"]
  population: ["remote-workers", "china"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Achieving Effective Remote Working During the COVID-19 Pandemic A Work Design Perspective/Achieving Effective Remote Working During the COVID-19 Pandemic A Work Design Perspective.md"
  pdf: "papers/Academic/01 Academic - Extended/Achieving Effective Remote Working During the COVID-19 Pandemic A Work Design Perspective.pdf"
  notes: null

---

id: "crowston-2006-assessing-the-health-of-open-source"
title: "Assessing the Health of Open Source Communities"
authors:
  - "Crowston, K."
  - "Howison, J."
year: 2006
doi: "10.1109/mc.2006.152"
venue: {type: "journal", name: "Computer", volume: 39, issue: 5, pages: "89-91"}
citation: "Crowston et al. (2006). Assessing the Health of Open Source Communities. Computer, 39(5), 89-91. https://doi.org/10.1109/mc.2006.152"
article_type: "commentary"
method: {design: "theory", approach: "analytical", evidence_level: "low", preregistered: false}
gist: >
  This practitioner-oriented IT Professional article by Crowston and Howison offers a
  framework for assessing FLOSS project health before contributing to or relying on a
  project, centered on an 'onion' model of concentric community roles (core developers,
  project leaders, codevelopers, active users). Drawing on the authors' own SourceForge
  research and prior motivation studies, it argues that healthy communities keep core teams
  small (rarely more than 10 developers), maintain a buffer of active users who shield core
  developers from routine support burden, and successfully manage leadership transitions. It
  gives IT professionals concrete signs to check (mailing lists, IRC tone, release
  management, leadership turnover) as proxies for community health and sustainability.
claims:
  - text: "Analysis of more than 100,000 SourceForge projects found that fewer than 1 percent have ever had more than 10 developers with commit access, indicating that small core teams (3-10 people) are typical and adequate even for successful FLOSS projects."
    evidence: "case-study"
    support_strength: "low-to-moderate"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "community-engagement"]
  - text: "Healthy FLOSS communities have an onion-shaped structure in which a wide circle of active users (testing releases, filing bug reports, answering setup questions) forms a buffer that protects core developers from burnout and from being overwhelmed by peripheral/passive users, as illustrated by a sociogram of bug-fixing interactions in the SquirrelMail project."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["burnout", "collaboration"]
    predictors: ["team-cohesion", "network-structure"]
  - text: "Citing prior survey research (Ghosh et al.; Lakhani and Wolf), the article reports that FLOSS contributor motivations are diverse and rank, in decreasing order of relevance: intellectual engagement, knowledge sharing, interest in the product itself, and ideology/reputation/community obligation, with reputation's importance rising the longer a participant has been involved."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-engagement"]
    predictors: ["community-engagement"]
population:
  who: "FLOSS open-source projects and their developer/leader/user communities in general, illustrated with the SourceForge project population and specific examples (Apache, Linux, Debian, Perl, SquirrelMail)"
  where: []
  when: null
  n: null
  sector: ["open-source"]
  sample_notes: >
    Not an original empirical study; it is a synthesis/practitioner-advice piece that cites
    the authors' own (then in-press) SourceForge analysis and other researchers' motivation
    surveys rather than presenting new primary data collection.
limitation:
  primary: "The article is a practitioner-oriented magazine synthesis, not a primary empirical study; its central statistic (the 1% figure) and other claims rely on citations to the authors' separate in-press work without methodological detail presented here."
  others:
    - "No original data collection or analysis is reported within the article itself"
    - "Recommendations (e.g., an ideal active-user buffer of 'one or two longer-term participants') are heuristic and anecdotal rather than statistically derived"
risk_of_bias: "high"
relevance_to_project: >
  Provides a concrete, reusable structural model (core developers / leaders / codevelopers /
  active users) for diagnosing open-source community health, and directly ties community
  structure to maintainer burnout by identifying the active-user buffer as a protective
  mechanism against core-developer burnout and support overload.
tags:
  topic: ["open-source", "maintainer-burnout", "community-health", "collaboration"]
  method: ["case-study", "secondary-data"]
  population: ["open-source-contributors", "software-developers"]
source:
  markdown: "Papers_Data/Academic/MD/Assessing the Health of Open Source Communities/Assessing the Health of Open Source Communities.md"
  pdf: "papers/Academic/Assessing the Health of Open Source Communities.pdf"
  notes: null

---

id: "moretti-2020-characterization-of-home-working-population-during"
title: "Characterization of Home Working Population during COVID-19 Emergency: A Cross-Sectional Analysis"
authors:
  - "Moretti, Antimo"
  - "Menna, Fabrizio"
  - "Aulicino, Milena"
  - "Paoletta, Marco"
  - "Liguori, Sara"
  - "Iolascon, Giovanni"
year: 2020
doi: "10.3390/ijerph17176284"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 17, issue: 17, pages: "6284"}
citation: "Moretti et al. (2020). Characterization of Home Working Population during COVID-19 Emergency: A Cross-Sectional Analysis. International Journal of Environmental Research and Public Health, 17(17), 6284. https://doi.org/10.3390/ijerph17176284"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This cross-sectional survey of 51 Italian administrative office workers who shifted to
  home working during the COVID-19 emergency found mixed self-perceived effects: many
  reported lower productivity but also lower stress and unchanged job satisfaction, while
  70.5% reported musculoskeletal pain (mostly low back and neck) linked to non-ergonomic
  home setups. Workers with pain reported significantly lower work engagement/job
  satisfaction than pain-free workers, and impaired interaction with colleagues was cited as
  the top disadvantage of home working alongside domestic distractions.
claims:
  - text: "Self-perceived productivity decreased for 39.2% and increased for 29.4% of home workers; stress decreased for 39.2% and increased for 33.3%; job satisfaction was unchanged for 51%, lower for 35.3%, and higher for 13.7% compared to office work."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["productivity", "stress", "job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "70.5% of home workers reported musculoskeletal pain, most frequently low back pain (41.2%) or neck pain (23.5%), attributed largely to non-ergonomic home equipment (e.g., 54.9% used a non-height-adjustable chair, no participant used a footstool); neck pain worsened in 50% of affected workers while low back pain remained unchanged in 47.6% of cases."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["wellbeing"]
    predictors: ["home-office-ergonomics", "remote-work-intensity"]
  - text: "Home workers without musculoskeletal pain reported significantly higher job satisfaction/work engagement (UWES-17 = 87.70 ± 9.10) than those with pain (74.86 ± 14.42), p = 0.009; impaired interaction with colleagues (41.2%) and domestic distractions (40.6%) were the most-cited disadvantages of home working."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction", "wellbeing"]
    predictors: ["musculoskeletal-pain", "isolation"]
population:
  who: "51 administrative office employees in Italy who transitioned to full-time mobile/home working at the start of the COVID-19 emergency (mean age 46.67 ± 11.26 years, 56.9% female)"
  where: ["Italy"]
  when: "2020 (COVID-19 emergency period, roughly first ~3 months of home working)"
  n: 51
  sector: ["administrative", "public-sector"]
  sample_notes: >
    Convenience sample recruited by phone from a single region (Campania); all held the same
    administrative-officer role, so findings may not generalize to other occupations,
    regions, or countries; no pre-COVID baseline or control group, only retrospective self-
    comparison to office work.
limitation:
  primary: "Small sample size (n=51) and cross-sectional design preclude causal inference and limit statistical power and generalizability."
  others:
    - "Geographically restricted to workers from a single Italian region (Campania)"
    - "Short exposure period (~3 months of remote work) likely understates cumulative musculoskeletal and mental-health effects of sustained home working"
    - "Outcomes (productivity, stress, MSK worsening) are retrospective self-report comparisons rather than objective or pre/post measures"
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantified evidence that 'impaired interaction with colleagues' is among the
  most-cited disadvantages of home working (41.2%), and that physical/musculoskeletal strain
  from poor home-office ergonomics is significantly associated with lower work engagement
  and job satisfaction (UWES) — useful for SNH models that link physical home-work
  conditions and reduced peer contact to wellbeing and engagement outcomes in remote
  workers.
tags:
  topic: ["remote-work", "wellbeing", "job-satisfaction", "isolation"]
  method: ["cross-sectional", "survey"]
  population: ["office-workers", "administrative-staff", "italy", "covid-19"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Characterization of Home Working Population during COVID-19 Emergency A Cross-Sectional Analysis/Characterization of Home Working Population during COVID-19 Emergency A Cross-Sectional Analysis.md"
  pdf: "papers/Academic/01 Academic - Extended/Characterization of Home Working Population during COVID-19 Emergency A Cross-Sectional Analysis.pdf"
  notes: null

---

id: "baumeister-1984-choking-under-pressure-self-consciousness-and"
title: "Choking under pressure: Self-consciousness and paradoxical effects of incentives on skillful performance."
authors:
  - "Baumeister, Roy F."
year: 1984
doi: "10.1037/0022-3514.46.3.610"
venue: {type: "journal", name: "Journal of Personality and Social Psychology", volume: 46, issue: 3, pages: "610-620"}
citation: "Baumeister (1984). Choking under pressure: Self-consciousness and paradoxical effects of incentives on skillful performance.. Journal of Personality and Social Psychology, 46(3), 610-620. https://doi.org/10.1037/0022-3514.46.3.610"
article_type: "empirical"
method: {design: "experiment", approach: "experiment", evidence_level: "moderate", preregistered: false}
gist: >
  Baumeister's classic six-experiment study on 'choking under pressure' shows that pressure
  (implicit competition, cash incentives, audience surveillance) degrades skilled motor
  performance by increasing conscious self-focused attention on one's own performance
  process, which disrupts otherwise automatic execution. Critically, individuals low in
  dispositional self-consciousness were more vulnerable to this pressure-induced choking
  than those habitually high in self-consciousness, who appeared better able to cope with
  evaluative pressure. The work establishes a mechanistic model linking incentives,
  surveillance, and self-focus to paradoxical performance decrements.
claims:
  - text: "Directing subjects' attention to their own hand movements (vs. the ball) produced significantly worse motor-skill performance across two lab pilots and a replication, e.g. F(1,19)=8.51, p<.01, supporting the model that self-focused attention on performance process disrupts skilled execution."
    evidence: "experiment"
    support_strength: "moderate"
    outcomes: ["performance", "stress"]
    predictors: ["self-focused-attention"]
  - text: "Under implicit competitive pressure from a confederate, low-self-consciousness subjects choked (scored much worse under high pressure than in a no-pressure control, t(33)=2.56, p<.02), while high-self-consciousness subjects showed a nonsignificant improvement, F(2,33)=3.99, p<.05 for the pressure x self-consciousness interaction."
    evidence: "experiment"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["self-consciousness", "peer-comparison"]
  - text: "A cash incentive for exceeding a performance criterion paradoxically caused choking on the first trial (low-self-consciousness subjects performed worse for cash than in a no-incentive control, t(33)=2.26, p<.05); a field study on arcade video-game players under evaluative surveillance found an average 25% performance drop from practice to pressure trials, t(12)=2.91, p<.02."
    evidence: "experiment"
    support_strength: "moderate"
    outcomes: ["performance", "stress"]
    predictors: ["incentive-pressure", "self-consciousness"]
population:
  who: "Undergraduate students at Case Western Reserve University (Experiments 1-5, roller-ball motor task) and customers at a shopping-mall video arcade aged 13+ (Experiment 6, video-game task)"
  where: ["United States"]
  when: null
  n: null
  sector: ["higher-education", "general-public"]
  sample_notes: >
    Six separate experiments with small per-cell samples (e.g., n=24 in Exp 3, n=40 in Exp
    4, n=37 in Exp 5, n=13 field subjects in Exp 6); Exp 4 restricted to male
    undergraduates; no total pooled N reported; deception/confederate paradigms used
    throughout, limiting ecological validity.
limitation:
  primary: "All lab studies used young undergraduate volunteers on artificial motor tasks (roll-up game) with small cell sizes, and the single field study (video arcade) had only 13 subjects, limiting generalizability to real workplace or community settings."
  others:
    - "The hypothesized causal chain (pressure -> increased self-focused attention -> disrupted automaticity) was never directly measured; the link between pressure and attentional self-focus is inferred, not tested."
    - "Several key effects were only marginally significant (e.g., Experiment 5 main effects at p<.12 and p<.10) and some effects appeared only on the first of two trials, raising interpretive caution."
    - "No preregistration; multiple experiments and subscale analyses (public/private self-consciousness) invite some risk of selective reporting typical of 1980s experimental psychology."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a mechanistic evidence base for why performance-based incentives, leaderboards,
  or visible peer/audience surveillance (e.g., public contribution metrics, visible activity
  dashboards in remote or open-source teams) can backfire and degrade performance for people
  not habitually self-conscious, informing decisions about how visible/evaluative to make
  performance feedback and incentive systems in community and workplace design.
tags:
  topic: ["wellbeing", "psychological-safety", "measurement"]
  method: ["experiment", "quantitative"]
  population: ["students", "general-population"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Choking Under Pressure Self-Consciousness and Paradoxical Effects of Incentives on Skillful Performance/Choking Under Pressure Self-Consciousness and Paradoxical Effects of Incentives on Skillful Performance.md"
  pdf: "papers/Academic/01 Academic - Extended/Choking Under Pressure Self-Consciousness and Paradoxical Effects of Incentives on Skillful Performance.pdf"
  notes: null

---

id: "hamouche-2023-covid-19-and-employees-mental-health"
title: "COVID-19 and employees’ mental health: stressors, moderators and agenda for organizational actions"
authors:
  - "Hamouche, Salima"
year: 2023
doi: "10.1108/eor-02-2023-0004"
venue: {type: "journal", name: "Emerald Open Research", volume: 1, issue: 2, pages: null}
citation: "Hamouche (2023). COVID-19 and employees’ mental health: stressors, moderators and agenda for organizational actions. Emerald Open Research, 1(2). https://doi.org/10.1108/eor-02-2023-0004"
article_type: "review"
method: {design: "review-narrative", approach: "secondary-data", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This narrative literature review synthesizes early COVID-19 and prior epidemic (SARS,
  Ebola) research to identify workplace stressors driving employee psychological distress
  and depression, organized into pandemic-period stressors (contagion fear, infobesity,
  quarantine, stigma, financial/job insecurity) and post-pandemic stressors (lingering
  stigma, financial loss). It maps three dimensions of moderators -- organizational,
  institutional, and individual -- and translates them into HR recommendations, notably
  identifying teleworking-induced social isolation as a specific mental-health risk to be
  actively managed rather than assumed benign.
claims:
  - text: "Teleworking, while protective for physical safety during a pandemic, can negatively affect employee mental health primarily because it increases social isolation, which is associated with elevated psychological distress and depression risk; blurred work/home boundaries further compound stress."
    evidence: "review-narrative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "mental-health", "stress"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Quarantined health care workers were significantly more likely to report exhaustion, anxiety when treating febrile patients, insomnia, irritability, low work performance, and poor concentration; income reduction during SARS predicted psychological disorder with an odds ratio of 25.0."
    evidence: "review-narrative"
    support_strength: "low"
    outcomes: ["stress", "mental-health"]
    predictors: ["workload", "isolation"]
  - text: "Stigma tied to infectious-disease outbreaks can persist for years: SARS survivors in one study reported ongoing stigmatization and social isolation from colleagues and employers up to four years after the outbreak, sustaining elevated stress and worsened mental health."
    evidence: "review-narrative"
    support_strength: "low"
    outcomes: ["isolation", "mental-health", "stress"]
    predictors: ["organizational-culture"]
population:
  who: "Not a primary study of a human sample; a general/narrative literature review of published studies (mostly on SARS, Ebola, and early 2020 COVID-19 outbreak) concerning employees and, especially, health care workers."
  where: []
  when: "Reviewed literature published through March 2020 (articles searched December 2019-March 2020, supplemented by earlier SARS/Ebola studies)"
  n: null
  sector: ["healthcare", "general-workforce"]
  sample_notes: >
    No original sample; search conducted in Google Scholar, Web of Science, and Semantic
    Scholar using coronavirus/COVID-19 + workplace/mental-health terms. Author acknowledges
    the review is non-systematic (narrative) and article selection may be subjective;
    underlying primary studies vary widely in design and rigor and are often about health
    care workers specifically, limiting generalizability to remote/knowledge workers.
limitation:
  primary: "The review is explicitly narrative rather than systematic, with author-acknowledged subjectivity in article selection and no formal quality appraisal of the underlying studies it synthesizes."
  others:
    - "Written in real time during the earliest weeks of the pandemic (by March 2020), so COVID-19-specific evidence was sparse and much of the argument leans on analogy to prior, differently-structured epidemics (SARS, Ebola)."
    - "No original data collection; conclusions about causal relationships (e.g., teleworking causing isolation-driven distress) are inferred from disparate secondary sources rather than tested directly."
    - "Individual-factor moderators (gender, age, education) are described as predictions extrapolated from general workplace mental-health literature rather than COVID-19-specific evidence, by the author's own admission."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's teleworking/remote-work risk model by identifying
  social isolation as the primary mechanism linking mandated remote work to psychological
  distress, and by proposing concrete organizational mitigations (continuous communication,
  virtual team meetings, employee assistance programs, manager training) that map onto SNH's
  social-support and belonging interventions.
tags:
  topic: ["remote-work", "mental-health", "isolation", "social-support", "wellbeing"]
  method: ["review-narrative", "secondary-data"]
  population: ["healthcare-workers", "general-workforce", "remote-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/COVID-19 and Employees Mental Health Stressors Moderators and Agenda for Organizational Actions/COVID-19 and Employees Mental Health Stressors Moderators and Agenda for Organizational Actions.md"
  pdf: "papers/Academic/01 Academic - Extended/COVID-19 and Employees Mental Health Stressors Moderators and Agenda for Organizational Actions.pdf"
  notes: null

---

id: "raghunathan-2024-cultivating-community-health-and-well-being"
title: "Cultivating Community Health and Well-being in Open Source: Mitigating Burnout and Prioritizing Mental Health"
authors:
  - "Raghunathan, Savitha"
year: 2024
doi: "10.47941/jts.1791"
venue: {type: "journal", name: "Journal of Technology and Systems", volume: 6, issue: 2, pages: "1-8"}
citation: "Raghunathan (2024). Cultivating Community Health and Well-being in Open Source: Mitigating Burnout and Prioritizing Mental Health. Journal of Technology and Systems, 6(2), 1-8. https://doi.org/10.47941/jts.1791"
article_type: "commentary"
method: {design: "mixed-methods", approach: "secondary-data", evidence_level: "weak", preregistered: false}
gist: >
  This whitepaper synthesizes secondary evidence -- an industry survey (Intel's open-source
  developer survey) plus contributor narratives drawn from blogs, forums, and press coverage
  -- to argue that open-source maintainer burnout stems from heavy volunteer workload,
  blurred work-life boundaries, social isolation, and the absence of formal support
  structures. It proposes a set of community-level interventions (awareness campaigns,
  flexible contribution norms, mentorship, psychological safety, diversity-aware support,
  and data-analytics-based early detection) aimed at sustaining maintainer and contributor
  mental health and, by extension, project sustainability.
claims:
  - text: "In Intel's open-source community survey, 'maintainer burnout' was the top-cited challenge (reported by 45% of respondents), followed by documentation/onboarding gaps (41%), sustainability (37%), and building community engagement (32%)."
    evidence: "cross-sectional"
    support_strength: "weak"
    outcomes: ["burnout"]
    predictors: ["workload", "open-source-maintenance"]
  - text: "The paper attributes open-source contributor burnout to high/unrealistic workload expectations combined with lack of boundaries, the always-available nature of volunteer contribution eroding work-life balance, and social isolation compounded by communication and language barriers that increase disengagement and conflict-induced stress."
    evidence: "review-scoping"
    support_strength: "weak"
    outcomes: ["burnout", "isolation", "work-life-balance"]
    predictors: ["workload", "boundary-management", "isolation"]
  - text: "Burnout among key maintainers and contributors is described as directly threatening project sustainability, illustrated by the case of the Rust project, where maintainer burnout was reported to jeopardize ongoing innovation and maintenance."
    evidence: "case-study"
    support_strength: "weak"
    outcomes: ["retention", "productivity"]
    predictors: ["open-source-maintenance", "workload"]
population:
  who: "Not a primary study of a sampled population; whitepaper synthesizes secondary evidence -- Intel's open-source developer survey results (respondent count not reported in this paper) and contributor narratives from blogs, forums, and news articles about open-source projects (e.g., Rust)."
  where: []
  when: null
  n: null
  sector: ["open-source"]
  sample_notes: >
    No original data collection; the author cites percentages from an external industry
    survey without reporting its sample size or methodology, and supplements with anecdotal
    contributor accounts pulled from external blog posts and news coverage, so
    representativeness cannot be assessed.
limitation:
  primary: "The paper conducts no original empirical research -- it is a secondary synthesis of an unverified industry survey and self-selected blog/forum narratives, so its 'findings' inherit whatever biases and unknown methodology those sources carry."
  others:
    - "Single-author whitepaper published in a low-visibility, rapid-turnaround open-access journal with an 8-page format and no apparent rigorous peer review evident in the text."
    - "No statistical analysis, effect sizes, or original quantitative/qualitative data beyond re-reporting cited percentages."
    - "Recommendations (awareness campaigns, flexible policies, mentorship, analytics-based early detection) are proposed but not empirically tested or evaluated within this paper."
risk_of_bias: "high"
relevance_to_project: >
  Provides a compact, citation-linked map of proposed maintainer-burnout mechanisms
  (workload/boundary blur, isolation, lack of formal support, diversity/inclusion gaps) and
  candidate interventions (peer support, mentorship, psychological safety, analytics-based
  early detection of disengagement) that the SNH project can treat as hypothesis-generating
  for open-source community health design, while noting the evidence itself is secondary and
  weak.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "isolation", "community-health", "psychological-safety"]
  method: ["review-scoping", "secondary-data"]
  population: ["open-source-maintainers", "open-source-contributors"]
source:
  markdown: "Papers_Data/Academic/MD/Cultivating Community Health and Well-being in Open Source Mitigating Burnout and Prioritizing Mental Health/Cultivating Community Health and Well-being in Open Source Mitigating Burnout and Prioritizing Mental Health.md"
  pdf: "papers/Academic/Cultivating Community Health and Well-being in Open Source Mitigating Burnout and Prioritizing Mental Health.pdf"
  notes: null

---

id: "kelliher-2010-doing-more-with-less-flexible-working"
title: "Doing more with less? Flexible working practices and the intensification of                work"
authors:
  - "Kelliher, Clare"
  - "Anderson, Deirdre"
year: 2010
doi: "10.1177/0018726709349199"
venue: {type: "journal", name: "Human Relations", volume: 63, issue: 1, pages: "83-106"}
citation: "Kelliher et al. (2010). Doing more with less? Flexible working practices and the intensification of                work. Human Relations, 63(1), 83-106. https://doi.org/10.1177/0018726709349199"
article_type: "empirical"
method: {design: "mixed-methods", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This study of UK professional flexible workers (37 interviewees plus a 2,066-respondent
  survey across three multinationals) finds that while flexible workers report significantly
  higher job satisfaction and organizational commitment than non-flexible peers, nearly all
  interviewees also describe work intensification -- doing more in the same or less time.
  The authors identify three mechanisms (imposed, enabled, and reciprocal/exchange-based
  intensification) and use social exchange theory to explain how workers trade added effort
  for the flexibility they are granted.
claims:
  - text: "Both remote and reduced-hours workers scored significantly higher than non-flexible workers on overall job satisfaction and organizational commitment (t-tests, p<.05 in all comparisons), and reduced-hours workers also reported significantly lower stress, based on a 2,066-respondent survey (729 remote, 228 reduced-hours) across three UK multinationals."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "retention", "stress"]
    predictors: ["remote-work-intensity", "autonomy"]
  - text: "36 of 37 interviewed flexible workers reported experiencing work intensification -- greater extensive effort (working outside scheduled hours) and/or intensive effort (working harder while working) -- even though the questionnaire did not directly ask about intensification."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "work-life-balance", "stress"]
    predictors: ["remote-work-intensity", "workload"]
  - text: "Intensification occurred through three distinct mechanisms: imposed (reduced-hours workers whose workload was not cut proportionally), enabled (remote workers concentrating effort away from office distractions), and reciprocal exchange (about 60% of interviewees expected to 'give something back' in effort for the flexibility granted, consistent with social exchange theory)."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "work-life-balance"]
    predictors: ["organizational-culture", "workload", "autonomy"]
population:
  who: "Professional/knowledge workers with voluntary flexible working arrangements (reduced hours and/or remote work) at three large UK multinational employers (IT, pharmaceutical, and consulting sectors); 37 semi-structured interviewees plus 2,066 survey respondents (including a non-flexible comparison group)."
  where: ["UK"]
  when: null
  n: 2066
  sector: ["technology", "pharmaceutical", "consulting"]
  sample_notes: >
    Interview sample: 37 flexible workers (15 IT, 9 pharma, 13 consulting), all in
    professional roles who had voluntarily requested their flexible arrangement (involuntary
    flexible workers excluded). Survey: 24% response rate to an emailed questionnaire link,
    yielding 2,066 responses (729 remote workers, 228 reduced-hours workers, remainder non-
    flexible); the questionnaire itself had no items specific to work intensification, so
    quantitative and qualitative findings come from separate instruments within the same
    organizations.
limitation:
  primary: "Sample is confined to professional/knowledge workers who voluntarily chose reduced-hours or partial remote arrangements at three large UK multinationals, limiting generalizability to other occupations, involuntary flexible workers, and non-UK settings."
  others:
    - "Cross-sectional, self-report design with no work-intensification-specific survey measure precludes causal inference or tracking of longer-term/cumulative effects."
    - "Only about a third of remote workers had a formal arrangement and most worked remotely just one day a week, so findings may not generalize to fully remote or informally arranged workers."
risk_of_bias: "medium"
relevance_to_project: >
  Directly warns SNH design against treating high job satisfaction/commitment scores as
  sufficient evidence that flexible or remote work is healthy: this study shows those same
  workers simultaneously self-report pervasive work intensification via imposed workload,
  self-enabled overwork, and reciprocal 'gratitude' effort, which is directly relevant to
  designing boundary-management supports and honest wellbeing measures for remote workers.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing", "burnout"]
  method: ["mixed-methods", "qualitative", "survey"]
  population: ["remote-workers", "professional-workers", "uk-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Doing More with Less Flexible Working Practices and the Intensification of Work/Doing More with Less Flexible Working Practices and the Intensification of Work.md"
  pdf: "papers/Academic/01 Academic - Extended/Doing More with Less Flexible Working Practices and the Intensification of Work.pdf"
  notes: null

---

id: "contreras-2020-e-leadership-and-teleworking-in-times"
title: "E-Leadership and Teleworking in Times of COVID-19 and Beyond: What We Know and Where Do We Go"
authors:
  - "Contreras, Francoise"
  - "Baykal, Elif"
  - "Abid, Ghulam"
year: 2020
doi: "10.3389/fpsyg.2020.590271"
venue: {type: "journal", name: "Frontiers in Psychology", volume: 11, issue: null, pages: null}
citation: "Contreras et al. (2020). E-Leadership and Teleworking in Times of COVID-19 and Beyond: What We Know and Where Do We Go. Frontiers in Psychology, 11. https://doi.org/10.3389/fpsyg.2020.590271"
article_type: "review"
method: {design: "review-scoping", approach: "analytical", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This narrative literature review (searching Web of Science, PsycINFO, Scopus, and SciELO
  for publications from 2000-2020, synthesizing roughly 80 peer-reviewed articles) argues
  that teleworking's benefits for performance, satisfaction, and turnover depend heavily on
  whether organizations pair it with effective 'e-leadership.' The authors define
  e-leadership as a distinct bundle of competencies (communication, social/trust-building,
  team-building, change management, and technological skill) needed to counter teleworking's
  central risk: employees' social and professional isolation from coworkers and supervisors.
  It closes by noting the field lacks a unified theory of e-leadership and that most
  underlying empirical studies are methodologically weak (small, non-representative samples,
  mostly descriptive/correlational).
claims:
  - text: "Across the reviewed literature, teleworking is associated with favorable outcomes including higher job performance and satisfaction, reduced work-family imbalance, and lower turnover intentions; a meta-analysis of 46 studies (Gajendran and Harrison, 2007, cited in this review) found telecommuting lowers turnover intentions and stress."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["turnover", "job-satisfaction", "stress", "work-life-balance"]
    predictors: ["remote-work-intensity"]
  - text: "Teleworking's most consistently reported risk across the reviewed studies is social/professional isolation from coworkers and supervisors, which is linked to lower job performance, gradual demotivation, and increased turnover intention and work-family conflict."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "performance", "turnover"]
    predictors: ["isolation", "remote-work-intensity"]
  - text: "The review concludes that effective e-leadership -- built on trust, clear and frequent communication, and cultivating an 'e-social' sense of connectedness -- can prevent team-member isolation and boost work engagement, but the evidence base is still nascent: only 32 of 102 Web of Science articles published 2001-2020 used 'e-leadership' in their title, and findings on its effectiveness remain inconclusive."
    evidence: "review-scoping"
    support_strength: "weak"
    outcomes: ["isolation", "job-engagement"]
    predictors: ["leadership-style", "social-support"]
population:
  who: "Approximately 80 peer-reviewed academic publications on telework/telecommuting and e-leadership (plus supporting theoretical and practitioner sources) synthesized via a non-systematic narrative literature review; the underlying studies collectively sample teleworking employees, managers, and virtual-team members across multiple countries and sectors."
  where: []
  when: "Search conducted March-July 2020; included literature published 2000-2020"
  n: null
  sector: []
  sample_notes: >
    Literature search used four databases (Web of Science, PsycINFO, Scopus, SciELO) and
    keyword combinations (telework, e-leadership, telecommuting, virtual teams, COVID-19);
    no PRISMA protocol, dual screening, or formal quality appraisal reported -- authors note
    the underlying primary studies mostly use small, non-representative samples.
limitation:
  primary: "The review is a non-systematic narrative synthesis (no PRISMA protocol, documented screening process, or risk-of-bias appraisal of included studies), so its conclusions rest on an author-curated selection of literature rather than a reproducible systematic search."
  others:
    - "Authors themselves flag that most underlying empirical studies on teleworking and e-leadership rely on small, non-representative samples and descriptive/correlational designs rather than experimental or longitudinal methods."
    - "No unified, empirically validated theory of e-leadership exists yet; the competency framework the review advances is presented as propositions for future testing, not as tested findings."
risk_of_bias: "medium"
relevance_to_project: >
  Directly supports the SNH project's thesis that remote/hybrid work's isolation risk is
  leadership-mediated: it links teleworking-driven isolation to concrete downstream harms
  (lower performance, higher turnover, work-family conflict) and proposes specific manager-
  facing levers (trust-building, communication norms, 'e-social' presence) that map onto
  candidate SNH interventions, while its honest admission of a thin, non-systematic evidence
  base is a caution against overclaiming those levers' effectiveness.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "job-satisfaction", "social-support"]
  method: ["review-scoping"]
  population: ["remote-workers", "managers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/E-Leadership and Teleworking in Times of COVID-19 and Beyond What We Know and Where Do We Go/E-Leadership and Teleworking in Times of COVID-19 and Beyond What We Know and Where Do We Go.md"
  pdf: "papers/Academic/01 Academic - Extended/E-Leadership and Teleworking in Times of COVID-19 and Beyond What We Know and Where Do We Go.pdf"
  notes: null

---

id: "graham-2024-employees-working-from-home-during-covid"
title: "Employees Working From Home During Covid-19 and Potential Mental Health Challenges"
authors:
  - "Graham, Jena"
year: 2024
doi: null
venue: {type: "thesis", name: "Walden University (ScholarWorks, Walden Dissertations and Doctoral Studies)", volume: null, issue: null, pages: null}
citation: "Graham (2024). Employees Working From Home During Covid-19 and Potential Mental Health Challenges. Walden University (ScholarWorks, Walden Dissertations and Doctoral Studies)."
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low", preregistered: false}
gist: >
  This Walden University dissertation uses descriptive phenomenology and semistructured
  interviews with nine U.S. remote workers to explore how the COVID-19-driven shift to
  working from home (WFH) affected their psychological well-being. Thematic analysis (via
  NVivo) identified six themes spanning job-security disruption, productivity effects,
  personal-life/work-boundary strain, distanced colleague relationships, and the buffering
  role of employer support, with most participants reporting loneliness, anxiety, or burnout
  tied to reduced face-to-face contact. The study frames its findings through Cognitive
  Evaluation Theory, arguing that WFH autonomy is undermined when relatedness (social
  contact) is stripped away.
claims:
  - text: "Most of the nine participants reported severe mental health effects of WFH, especially anxiety, burnout, and loneliness, which they attributed to reduced face-to-face contact with coworkers; several described feeling 'caged' or isolated, and single/extroverted participants reported disproportionate distress."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["loneliness", "burnout", "mental-health", "isolation"]
    predictors: ["remote-work-intensity", "isolation"]
  - text: "Participants who received tangible employer support (equipment/hardware, financial assistance, regular check-ins, weekly mental-health check-ins) described a smoother transition to WFH and better well-being, while those with 'mixed' or minimal employer support reported greater stress, frustration, and feeling left to cope alone."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["stress", "wellbeing"]
    predictors: ["social-support", "organizational-culture"]
  - text: "Remote work was described as distancing colleague relationships and reducing opportunities for informal bonding and collaboration; participants said video/chat tools sustained formal task communication but could not replicate the casual, unplanned interactions that had maintained working relationships in the office."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration", "isolation", "communication"]
    predictors: ["remote-work-intensity", "team-cohesion"]
population:
  who: "9 remote/knowledge workers (4 male, 5 female; average age 33; Hispanic, White, African American, and Native American participants) who had worked from home for at least 1 year since the COVID-19 pandemic was declared"
  where: []
  when: "interviews conducted circa 2023-2024 (data collected post-pandemic, recalling WFH experiences dating to 2020 onward); dissertation published December 2024"
  n: 9
  sector: ["mixed"]
  sample_notes: >
    Purposive, nonprobability sample recruited via professional networks, employer
    referrals, and social media (Twitter); no formal response rate reported. The
    dissertation gives two conflicting age-eligibility criteria in different sections (30+
    vs 22+). Country of participants is not explicitly stated but the literature review and
    framing are U.S.-centric (Walden University, U.S. dissertation); findings are not
    intended to generalize beyond this small, self-selected sample.
limitation:
  primary: "Very small purposive sample (n=9) of self-selected volunteers using a nonprobability sampling strategy limits generalizability of the six identified themes to the broader WFH workforce."
  others:
    - "All interviews were conducted virtually (no in-person contact), which the author notes may have reduced rapport and yielded less descriptive or candid participant accounts."
    - "Cross-sectional retrospective design relying on participants' recall of pre-pandemic vs. pandemic work experiences, with no longitudinal follow-up despite the study's stated interest in long-term mental health effects."
    - "Researcher held a dual observer-participant role (also a WFH remote worker), creating potential for reflexivity/bias that was only partially mitigated through bracketing and reflexive journaling."
risk_of_bias: "medium"
relevance_to_project: >
  Provides qualitative, first-person evidence for the SNH project's core mechanism linking
  reduced face-to-face colleague contact during WFH to loneliness, isolation, and burnout,
  and offers a concrete, theory-grounded (Cognitive Evaluation Theory) argument that
  employer-provided social/relational support -- not just equipment -- buffers these
  effects, which is directly relevant to designing organizational interventions for remote-
  worker social network health.
tags:
  topic: ["remote-work", "isolation", "loneliness", "burnout", "mental-health", "work-life-balance"]
  method: ["qualitative", "interview"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/MD/Employees Working from Home During Covid-19 and Potential Mental Health Challenges/Employees Working from Home During Covid-19 and Potential Mental Health Challenges.md"
  pdf: "papers/Academic/Employees Working from Home During Covid-19 and Potential Mental Health Challenges.pdf"
  notes: "no-doi: confirmed none (manual review)"

---

id: "singh-2022-enforced-remote-working-the-impact-of"
title: "Enforced remote working: The impact of digital platform-induced stress and remote working experience on technology exhaustion and subjective wellbeing"
authors:
  - "Singh, Pallavi"
  - "Bala, Hillol"
  - "Dey, Bidit Lal"
  - "Filieri, Raffaele"
year: 2022
doi: "10.1016/j.jbusres.2022.07.002"
venue: {type: "journal", name: "Journal of Business Research", volume: 151, issue: null, pages: "269-286"}
citation: "Singh et al. (2022). Enforced remote working: The impact of digital platform-induced stress and remote working experience on technology exhaustion and subjective wellbeing. Journal of Business Research, 151, 269-286. https://doi.org/10.1016/j.jbusres.2022.07.002"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This PLS-SEM survey of 306 UK employees during enforced COVID-19 work-from-home finds that
  both work-technology platform stress (WTPS) and personal-technology platform stress (PTPS)
  independently drive techno-exhaustion, which in turn reduces subjective wellbeing, with
  PTPS showing a stronger effect on exhaustion than WTPS. It also shows that low remote-work
  intensity amplifies WTPS and PTPS effects, and that high personal resilience paradoxically
  strengthens (rather than buffers) the negative link between techno-exhaustion and
  wellbeing, contradicting prior resilience-as-buffer findings.
claims:
  - text: "Both work-technology platform stress and personal-technology platform stress significantly increase techno-exhaustion, with PTPS having a stronger path coefficient than WTPS (WTPS -> exhaustion beta=0.327, t=5.109, p<.001; PTPS -> exhaustion beta=0.410, t=6.809, p<.001), and techno-exhaustion significantly reduces subjective wellbeing (beta=-0.263, t=4.265, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "wellbeing", "stress"]
    predictors: ["technostress", "remote-work-intensity"]
  - text: "Remote-work intensity moderates technostress: the effect of increased work-technology use on WTPS is stronger for those with less-intense remote working during COVID-19 (interaction beta=-0.359, t=3.586, p<.001), and the effect of increased personal-technology use on PTPS is stronger for those with less-intense remote working before COVID-19 (interaction beta=-0.193, t=2.678, p=.007)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress"]
    predictors: ["remote-work-intensity", "technostress"]
  - text: "Contrary to prior literature framing resilience as a protective buffer, resilience negatively moderates the exhaustion-wellbeing link such that techno-exhaustion has a stronger negative effect on subjective wellbeing for individuals with HIGH resilience (interaction beta=-0.187, t=3.281, p<.001), and resilience also strengthens the positive effect of low prior remote-work experience on wellbeing (interaction beta=-0.143, t=2.775, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "burnout"]
    predictors: ["technostress", "remote-work-intensity"]
population:
  who: "306 British employed adults (full-time, part-time, self-employed) working and living in the UK during COVID-19, recruited via Prolific"
  where: ["United Kingdom"]
  when: "July 2020"
  n: 306
  sector: ["mixed/cross-sector"]
  sample_notes: >
    Prolific-panel convenience sample; 47% had no prior remote-work experience and 84% did
    less than half their work remotely pre-COVID; 3 of 309 initial responses excluded for
    being out of work due to COVID; gender skewed female (63.7%); no representativeness
    claims beyond UK-employed Prolific users.
limitation:
  primary: "Cross-sectional single-timepoint design cannot capture how technostress and its outcomes evolved across different phases of the dynamic COVID-19 period, limiting causal inference."
  others:
    - "Focuses on individual-level work settings and does not examine how shared purpose, camaraderie, or team-level coping among colleagues might affect resilience and stress outcomes."
    - "Does not account for variation by household/family size, organisational role, or perceived job security, which the authors flag as likely moderators left unexplored."
    - "Self-selected online panel (Prolific) sample restricted to UK employed nationals limits generalizability to other countries or non-panel populations."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs SNH design questions about how remote/hybrid work technology load
  interacts with personal digital-platform use to drive burnout and reduced wellbeing, and
  complicates simple 'resilience is protective' assumptions used in intervention design by
  showing resilience can amplify harm from techno-exhaustion in enforced remote-work crises.
  Also supports designing for remote-work intensity/experience as a moderating factor when
  scoping interventions aimed at reducing technostress-driven burnout.
tags:
  topic: ["remote-work", "technostress", "burnout", "wellbeing", "work-life-balance"]
  method: ["cross-sectional", "survey", "pls-sem"]
  population: ["knowledge-workers", "uk-employees"]
source:
  markdown: "Papers_Data/Academic/MD/Enforced remote working- The impact of digital platform-induced stress and remote working experience on technology exhaustion and subjective wellbeing/Enforced remote working- The impact of digital platform-induced stress and remote working experience on technology exhaustion and subjective wellbeing.md"
  pdf: "papers/Academic/Enforced remote working- The impact of digital platform-induced stress and remote working experience on technology exhaustion and subjective wellbeing.pdf"
  notes: null

---

id: "mcleod-2011-factors-that-affect-software-systems-development"
title: "Factors that affect software systems development project outcomes"
authors:
  - "McLeod, Laurie"
  - "MacDonell, Stephen G."
year: 2011
doi: "10.1145/1978802.1978803"
venue: {type: "journal", name: "ACM Computing Surveys", volume: 43, issue: 4, pages: "1-56"}
citation: "McLeod et al. (2011). Factors that affect software systems development project outcomes. ACM Computing Surveys, 43(4), 1-56. https://doi.org/10.1145/1978802.1978803"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This is a large narrative literature review synthesizing 177 empirical studies (1996-2006)
  of factors influencing software systems development and deployment project outcomes, from
  which the authors build a four-dimension classificatory framework: project content,
  development processes, institutional context, and people and action. A key contribution is
  the 'people and action' dimension, which treats social interaction among developers,
  users, and management -- goals/expectations alignment, mutual understanding,
  communication, conflict/politics, trust, and team cohesion -- as a primary determinant of
  project success or failure, often more influential than technical factors. The review
  argues that prescriptive lists of isolated success factors are inadequate because factors
  interact dynamically over a project's lifecycle and are embedded in organizational and
  wider institutional context.
claims:
  - text: "Project team cohesiveness and effectiveness are positively associated with project performance, while larger project teams show reduced performance: Wang et al. (2005) found team cohesiveness significantly positively related to project performance, Jiang et al. (2002b) found strong project team effectiveness improved outcomes, and Aladwani (2002) found team size significantly negatively correlated with team performance and problem-solving."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["collaboration", "performance", "productivity"]
    predictors: ["team-cohesion"]
  - text: "The reviewed literature consistently finds that organizational and human-related issues -- including the quality of social interaction, communication, mutual understanding, conflict, and political dynamics between developers, users, and management -- have a greater effect on project outcomes than technical factors alone, echoing the Standish Group's finding that 'people and process have a greater effect on project outcome than technology.'"
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["collaboration", "communication", "performance"]
    predictors: ["team-cohesion", "organizational-culture", "leadership-style"]
  - text: "Top management support/commitment is one of the most consistently reported determinants of project success across the reviewed studies and national contexts, ranking first or second of ten success factors in the Standish Group's 1998 and 2000 CHAOS surveys, with its absence linked to project abandonment and failure."
    evidence: "review-scoping"
    support_strength: "moderate"
    outcomes: ["performance"]
    predictors: ["leadership-style", "organizational-culture"]
population:
  who: "Not human subjects directly: the review's 'sample' is 177 empirical studies of software systems development/deployment projects published in academic journals (with 30 large factor-based studies tabulated in an appendix), covering developers, users, project teams, and top management as study populations within those primary studies."
  where: []
  when: "Primary studies published 1996-2006; review article published 2011"
  n: 177
  sector: ["technology", "cross-sector"]
  sample_notes: >
    Studies identified via EBSCO Computer Source and Business Source Premier database
    searches (terms: 'project failure'/'project success' + 'computer software'/'information
    technology'), yielding 289 initial hits, supplemented by reference-list snowballing and
    targeted journal searches; restricted to peer-reviewed journal articles (conference
    proceedings largely excluded), so likely under-represents non-English, non-journal, and
    post-2006 or non-archival research.
limitation:
  primary: "As a narrative/classificatory review rather than a systematic review or meta-analysis, it synthesizes methodologically heterogeneous studies (surveys, interviews, Delphi studies, case studies) using inconsistent definitions and measures of 'project outcome,' with no formal risk-of-bias assessment or effect-size pooling across included studies."
  others:
    - "Definitions of project success/failure are frequently left unspecified or applied post hoc in the primary studies, limiting comparability of the 'findings' being synthesized."
    - "Scope explicitly excludes operating systems, real-time embedded systems, and infrastructural systems, and the underlying literature (1996-2006) predates modern distributed/remote and open-source development contexts the SNH project is most concerned with."
    - "The classificatory framework is an interpretive synthesis by two authors rather than an independently validated coding scheme."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a domain-adjacent evidence base showing that team cohesion, communication
  quality, trust, conflict/politics, and leadership support among software developers and
  stakeholders are documented predictors of project performance and collaboration outcomes
  -- supporting the SNH project's premise that social/organizational dynamics (not just
  tooling) drive collaboration, productivity, and team functioning in software-producing
  teams, including open-source and remote-work analogues.
tags:
  topic: ["collaboration", "community-health", "productivity", "measurement"]
  method: ["review-scoping", "secondary-data"]
  population: ["software-developers", "project-teams"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Factors that Affect Software Systems Development Project Outcomes A Survey of Research/Factors that Affect Software Systems Development Project Outcomes A Survey of Research.md"
  pdf: "papers/Academic/01 Academic - Extended/Factors that Affect Software Systems Development Project Outcomes A Survey of Research.pdf"
  notes: null

---

id: "russell-2009-the-impact-of-flexible-working-arrangements"
title: "The Impact of Flexible Working Arrangements on Work–life Conflict and Work Pressure in Ireland"
authors:
  - "Russell, Helen"
  - "O'Connell, Philip J."
  - "McGinnity, Frances"
year: 2009
doi: "10.1111/j.1468-0432.2008.00431.x"
venue: {type: "journal", name: "Gender, Work &amp; Organization", volume: 16, issue: 1, pages: "73-97"}
citation: "Russell et al. (2009). The Impact of Flexible Working Arrangements on Work–life Conflict and Work Pressure in Ireland. Gender, Work &amp; Organization, 16(1), 73-97. https://doi.org/10.1111/j.1468-0432.2008.00431.x"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a nationally representative 2003 telephone survey of over 5,000 Irish employees,
  this study tests whether four flexible working arrangements (flexitime, part-time work,
  job sharing, and home working) reduce work pressure and work-life conflict. It finds the
  effects are not uniform: part-time work and flexitime reduce both work pressure and work-
  life conflict as expected, but working from home is associated with significantly higher
  levels of both, even after controlling for hours worked. The authors conclude that home
  working should not be treated as a straightforward work-life balance measure and that
  flexible arrangements must be evaluated individually rather than as a package.
claims:
  - text: "Personal involvement in home working is associated with significantly greater work pressure (B=.272, p<.005) and greater work-life conflict (B=.206, p<.005) relative to non-involved employees with similar job/organizational characteristics; the negative association persists even after controlling for weekly hours worked, indicating a mechanism beyond longer hours (e.g., work intruding into family time/space)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Involvement in part-time work reduces both work pressure (B=-.097, p<.005) and work-life conflict (B=-.156, p<.005); the work-pressure-reducing effect is significant only for women, not men, in interaction models."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["boundary-management", "workload"]
  - text: "Flexitime is associated with modestly lower work pressure (B=-.055, significant only at p<.10) but this effect is confined to the public sector in sector-interaction models; flexitime shows no significant overall effect on work-life conflict once other factors are controlled. Job sharing has no significant effect on work pressure and is associated with significantly greater work-life conflict specifically among the small group of men who job-share."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["organizational-culture", "boundary-management"]
population:
  who: "Employees (not the self-employed or non-working) in the Republic of Ireland, drawn from the 2003 'Changing Workplace' national survey"
  where: ["Ireland"]
  when: "June-early September 2003"
  n: 5198
  sector: ["mixed-public-private", "general-workforce"]
  sample_notes: >
    Nationally representative telephone survey (300 randomly selected sampling points,
    random-digit dialing within area codes); 5,198 completed interviews, 46.5% response
    rate; data reweighted to national population parameters. Regression models use slightly
    smaller analytic samples (n=4,320 for work-pressure models, n=4,445 for work-life-
    conflict models) due to missing data on controls.
limitation:
  primary: "Cross-sectional design cannot establish causal direction — e.g., it is equally plausible that high-pressure organizations are less likely to adopt flexible arrangements, or that flexible arrangements reduce management's felt need to reduce pressure, as that the arrangements themselves change pressure levels."
  others:
    - "Relies on employee self-report of both the availability of workplace policies and their own pressure/conflict levels, introducing potential measurement error, especially for employees' awareness of organization-wide policies."
    - "Cannot capture informal workplace culture around flexible work (e.g., how supportively policies are implemented by managers), which the authors note may matter as much as formal policy availability."
    - "Excludes non-employees (e.g., stay-at-home caregivers) and other flexible arrangements like career breaks, and does not examine work-to-home spillover in the reverse direction."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a rare, large-sample, multivariate counter-finding to the common assumption that
  working from home reduces work pressure and improves work-life balance: it instead finds
  home working significantly increases both pressure and work-life conflict, net of hours
  worked, which is directly relevant to SNH's remote-work boundary-management and always-
  on/technostress design considerations. It also demonstrates that flexible-work categories
  (part-time, flexitime, job sharing, home working) have divergent, sometimes opposite,
  effects and should not be evaluated or designed for as a single bundled intervention.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing"]
  method: ["cross-sectional", "survey"]
  population: ["general-workforce", "ireland"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Gender Work   Organization - 2009 - Russell - The Impact of Flexible Working Arrangements on Work life Conflict and Work/Gender Work   Organization - 2009 - Russell - The Impact of Flexible Working Arrangements on Work life Conflict and Work.md"
  pdf: "papers/Academic/01 Academic - Extended/Gender Work   Organization - 2009 - Russell - The Impact of Flexible Working Arrangements on Work life Conflict and Work.pdf"
  notes: null

---

id: "sommovigo-2023-how-and-when-may-technostress-impact"
title: "How and When May Technostress Impact Workers’ Psycho-Physical Health and Work-Family Interface? A Study during the COVID-19 Pandemic in Italy"
authors:
  - "Sommovigo, Valentina"
  - "Bernuzzi, Chiara"
  - "Finstad, Georgia Libera"
  - "Setti, Ilaria"
  - "Gabanelli, Paola"
  - "Giorgi, Gabriele"
  - "Fiabane, Elena"
year: 2023
doi: "10.3390/ijerph20021266"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 20, issue: 2, pages: "1266"}
citation: "Sommovigo et al. (2023). How and When May Technostress Impact Workers’ Psycho-Physical Health and Work-Family Interface? A Study during the COVID-19 Pandemic in Italy. International Journal of Environmental Research and Public Health, 20(2), 1266. https://doi.org/10.3390/ijerph20021266"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This study tests a moderated-mediation model in 266 Italian workers surveyed during the
  COVID-19 pandemic, finding that technostress was linked to psycho-physical distress partly
  through fear of COVID-19 (exacerbated among workers who had lost a loved one to the
  virus), and to work-family conflict partly through the tendency to work excessively
  (buffered by resilience). It identifies two distinct pathways -- an emotional/health
  pathway and a workaholism/boundary pathway -- by which ICT-driven stress translates into
  worker harm, and points to fear, grief exposure, and low resilience as amplifiers.
claims:
  - text: "Technostress was positively associated with psycho-physical distress both directly (beta=0.26, p<0.01) and indirectly via fear of COVID-19 (beta=0.09, p<0.05), and this indirect (mediated) effect was significant only among workers who had lost a loved one to COVID-19 (beta=0.08, p<0.01), not among those who had not (beta=-0.04, ns)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "stress"]
    predictors: ["technostress", "sense-of-belonging"]
  - text: "Technostress was positively related to work-family conflict directly (beta=0.36, p<0.001) and indirectly through tendencies to work excessively (beta=0.17, p<0.05); working excessively in turn predicted work-family conflict (beta=0.45, p<0.001), but this link was buffered by resilience such that highly resilient workers showed no significant increase in conflict (beta=0.15, ns) versus low-resilience workers (beta=0.46, p<0.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "burnout"]
    predictors: ["technostress", "boundary-management"]
  - text: "Remote workers reported significantly higher technostress (M=2.57) and fear of COVID-19 (M=2.41) than traditional on-site workers (M=2.11 and M=2.04 respectively), and women reported higher fear, work-family conflict, and psycho-physical distress alongside lower resilience than men."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "mental-health"]
    predictors: ["remote-work-intensity", "technostress"]
population:
  who: "266 Italian workers (62.6% women, mean age 39.4) recruited via an online convenience sample distributed on social media, mixing remote and on-site employees during the COVID-19 pandemic"
  where: ["Italy"]
  when: "January-March 2021"
  n: 266
  sector: ["mixed-general-workforce"]
  sample_notes: >
    Convenience sample recruited via LinkedIn/Instagram/Facebook/Twitter/WhatsApp; 287
    responses collected, 21 excluded for incompleteness (final n=266); self-report cross-
    sectional online survey with likely selection/healthy-worker-effect bias per the
    authors' own limitations discussion; not nationally representative.
limitation:
  primary: "Cross-sectional single-source self-report design precludes causal inference about the mediation and moderation pathways and is subject to common-method bias (though Harman's test and a method-factor model suggested this was not severe)."
  others:
    - "Nonprobability convenience sample recruited via social media, raising selection bias concerns (e.g., possible healthy-worker effect excluding the most distressed non-respondents)."
    - "Findings limited to Italian workers during a specific pandemic period, limiting generalizability to non-pandemic or non-Italian contexts."
    - "Only one behavior-based source of work-family conflict (working excessively) was examined, leaving other time- and strain-based mechanisms unexamined."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a tested mechanism (fear/anxiety and compulsive overwork as mediators) linking
  ICT-driven technostress in remote/hybrid work to both mental-health distress and work-
  family conflict, and shows resilience as a measurable buffer -- directly informs which
  mediating variables and protective factors (e.g., resilience training, disconnection
  norms) an SNH intervention targeting remote-worker technostress or boundary management
  should measure or design for.
tags:
  topic: ["remote-work", "technostress", "wellbeing", "work-life-balance", "mental-health"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/How and When May Technostress Impact Workers Psycho-Physical Health and Work-Family Interface A Study during the COVID-19 Pandemic in Italy/How and When May Technostress Impact Workers Psycho-Physical Health and Work-Family Interface A Study during the COVID-19 Pandemic in Italy.md"
  pdf: "papers/Academic/01 Academic - Extended/How and When May Technostress Impact Workers Psycho-Physical Health and Work-Family Interface A Study during the COVID-19 Pandemic in Italy.pdf"
  notes: null

---

id: "ralph-2020-pandemic-programming"
title: "Pandemic programming"
authors:
  - "Ralph, Paul"
  - "Baltes, Sebastian"
  - "Adisaputri, Gianisa"
  - "Torkar, Richard"
  - "Kovalenko, Vladimir"
  - "Kalinowski, Marcos"
  - "Novielli, Nicole"
  - "Yoo, Shin"
  - "Devroey, Xavier"
  - "Tan, Xin"
  - "Zhou, Minghui"
  - "Turhan, Burak"
  - "Hoda, Rashina"
  - "Hata, Hideaki"
  - "Robles, Gregorio"
  - "Milani Fard, Amin"
  - "Alkadhi, Rana"
year: 2020
doi: "10.1007/s10664-020-09875-y"
venue: {type: "journal", name: "Empirical Software Engineering", volume: 25, issue: 6, pages: "4927-4961"}
citation: "Ralph et al. (2020). Pandemic programming. Empirical Software Engineering, 25(6), 4927-4961. https://doi.org/10.1007/s10664-020-09875-y"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A 12-language survey of 2225 software developers and other software professionals across
  53 countries found that emotional wellbeing and perceived productivity both declined
  significantly after switching to working from home during the COVID-19 pandemic, and that
  the two declines were closely intertwined. A structural equation model shows that pandemic
  fear, poor disaster preparedness, and poor home-office ergonomics drive these declines,
  that isolation is the strongest predictor of fear, and that women, parents, and people
  with disabilities appear disproportionately affected. The authors also find little
  consensus among developers about which organizational support actions actually help,
  arguing against one-size-fits-all interventions.
claims:
  - text: "Both wellbeing and perceived productivity declined significantly after developers switched to working from home due to COVID-19 (Wilcoxon signed-rank test, p<.001; wellbeing Cliff's delta=0.12±0.03, productivity delta=0.13±0.03), and change in wellbeing and change in productivity were strongly, directly related in the structural model (path coefficient=0.822, z=18.361, p<.001)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "productivity", "stress"]
    predictors: ["remote-work-intensity", "technostress"]
  - text: "In the SEM, home office ergonomics and pandemic-related fear predicted change in wellbeing (ergonomics beta=0.125, p<.001; fear beta=-0.031, p=.011), while ergonomics and disaster preparedness predicted change in productivity (ergonomics beta=0.242, p<.001; disaster preparedness beta=0.097, p=.005); isolation (not leaving home except for necessities) was the strongest predictor of fear (beta=0.502, p<.001), and disaster preparedness reduced fear (beta=-0.336, p=.002)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "productivity", "stress"]
    predictors: ["isolation", "home-office-ergonomics", "disaster-preparedness"]
  - text: "Exploratory subgroup analyses suggest disproportionate effects on protected groups: women reported significantly more fear (beta=0.273, p=.025); people with disabilities had less-prepared, less-ergonomic setups and more fear; and people living with young children had significantly less ergonomic home offices (beta=-0.163, p<.001), with effects sometimes conflicting (e.g., disability had both a direct positive and an indirect negative effect on productivity)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["stress", "productivity", "wellbeing"]
    predictors: ["caregiving-responsibilities", "disability-status", "gender"]
population:
  who: "Software developers and other software professionals worldwide who switched from working in an office to working from home because of COVID-19 (most respondents self-identified as developers)"
  where: ["Germany", "Russia", "Brazil", "Italy", "United States", "South Korea", "Belgium", "China", "Turkey", "India", "and 43 other countries (53 total)"]
  when: "March 27 - April 16, 2020"
  n: 2225
  sector: ["software-development", "technology"]
  sample_notes: >
    Convenience/snowball sampling via an anonymous 12-language questionnaire with country-
    specific advertising by a 17-author international team; 2668 total responses, 2225
    usable after excluding non-inclusion-criteria and blank responses. Sample skewed male
    (81% vs 18% female, 1% non-binary), 94% full-time employed, median age 30-34; response-
    bias check (completers vs non-completers of open-ended items) found only small, near-
    negligible differences (eta-squared <=0.009).
limitation:
  primary: "Wellbeing and productivity 'before' working from home were measured retrospectively via self-report at the same time as the 'after' measure, so causal precedence and recall accuracy cannot be fully verified despite the sophisticated SEM analysis."
  others:
    - "Non-random convenience/snowball sampling; despite 12-language localization the sample is unevenly distributed across countries (e.g., far more German than Southeast Asian respondents) and any random sample of developers is inherently hard to achieve."
    - "Perceived productivity (HPQ scale) is not the same as actual/objective productivity, and its validity in software development or during pandemics specifically is unconfirmed."
    - "Google Forms platform limited the ability to detect response bias (no partial-response or bounce-rate data, no protection against multiple submissions)."
risk_of_bias: "medium"
relevance_to_project: >
  Provides one of the largest quantitative models linking crisis-driven remote work to
  wellbeing and productivity, empirically showing isolation as a strong predictor of
  pandemic-related fear and home-office ergonomics/disaster-preparedness as levers
  organizations can act on; its finding of no organizational-support action universally
  rated helpful (Table 7) directly informs SNH's case for individualized rather than one-
  size-fits-all interventions.
tags:
  topic: ["remote-work", "wellbeing", "isolation", "productivity", "mental-health", "technostress"]
  method: ["survey", "cross-sectional"]
  population: ["software-developers", "international-sample", "remote-work"]
source:
  markdown: "Papers_Data/Academic/MD/How COVID-19 affects software developers and how their organizations can help/How COVID-19 affects software developers and how their organizations can help.md"
  pdf: "papers/Academic/How COVID-19 affects software developers and how their organizations can help.pdf"
  notes: null

---

id: "jibunoh-2025-impact-of-remote-work-dynamics-on"
title: "Impact of Remote Work Dynamics on Mental Health and Productivity"
authors:
  - "Jibunoh, Joy"
  - "Ezichi, Ogbonnaya"
  - "Okpanachi, Victor"
  - "Amaechi, Chibuzor"
  - "Awosan, Wuraola"
  - "Tchoumo, Prosper"
  - "Sanusi, Jubril"
year: 2025
doi: "10.4236/ojd.2025.141002"
venue: {type: "journal", name: "Open Journal of Depression", volume: 14, issue: 01, pages: "13-27"}
citation: "Jibunoh et al. (2025). Impact of Remote Work Dynamics on Mental Health and Productivity. Open Journal of Depression, 14(01), 13-27. https://doi.org/10.4236/ojd.2025.141002"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "low", preregistered: false}
gist: >
  Using a secondary Kaggle dataset of 5000 employees across six global regions and seven
  industries, this cross-sectional study finds that only 33.5% of respondents are satisfied
  with remote work and that workplace location (remote or hybrid vs. onsite) is the only
  statistically significant predictor of that satisfaction in a logistic regression, while
  gender, industry, region, and years of experience are not. Roughly three-quarters of
  employees report a mental health condition (anxiety, burnout, or depression) regardless of
  gender, and hybrid/remote workers report modestly better work-life balance than onsite
  workers (40% vs 37.2% high balance).
claims:
  - text: "Only 33.5% of employees (1675/5000) reported being satisfied with remote work, significantly less than the 50% baseline proportion tested (exact binomial test, p ≈ 0), with 66.5% unsatisfied or neutral."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "Approximately 75% of employees across all genders reported a mental health condition (anxiety, burnout, or depression) — 75.27% of women, 76.61% of men, 74.63% of non-binary employees — with no significant gender difference in susceptibility."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["mental-health", "anxiety", "burnout", "depression"]
    predictors: ["remote-work-intensity"]
  - text: "In binary logistic regression, workplace location was the only statistically significant predictor of remote-work satisfaction (Wald = 13.24, df = 2, p = 0.001): both remote (Exp(β) = 0.841, 95% CI 0.728–0.973) and hybrid (Exp(β) = 0.767, 95% CI 0.664–0.887) locations were associated with lower odds of satisfaction than onsite work, while age, gender, region, industry, years of experience, and meeting frequency were not significant predictors."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["job-satisfaction"]
    predictors: ["remote-work-intensity"]
population:
  who: "5000 employees drawn from a public Kaggle dataset spanning multiple industries (IT, consulting, retail, finance, healthcare, manufacturing, education) and work locations (remote, hybrid, onsite)"
  where: ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
  when: null
  n: 5000
  sector: ["technology", "finance", "healthcare", "manufacturing", "retail", "education", "consulting"]
  sample_notes: >
    Data were obtained secondhand from a public Kaggle dataset ('Remote Work & Mental
    Health'); the original survey's recruitment method, response rate, data-collection
    period, and representativeness are not described by the study authors.
limitation:
  primary: "The dataset is a secondary, publicly-posted Kaggle dataset whose original sampling frame, recruitment method, response rate, and data-collection dates are not described, making representativeness and even provenance of the 5000-respondent sample impossible to verify."
  others:
    - "Cross-sectional self-report design cannot establish causal direction between remote work location and mental health or satisfaction outcomes."
    - "Mental health condition was measured as a single self-reported categorical variable (anxiety/burnout/depression/none) without validated clinical instruments."
    - "Published in an SCIRP open-access journal (Open Journal of Depression), whose peer-review rigor is widely questioned in the literature."
risk_of_bias: "high"
relevance_to_project: >
  Offers rough population-level base rates (about 75% self-reported mental health condition,
  roughly one-third satisfaction with remote work) and evidence that self-reported workplace
  location, not demographic or industry factors, predicts remote-work satisfaction in this
  sample — useful as a coarse prevalence anchor and a caution against assuming demographic-
  targeted SNH interventions will move satisfaction more than format/location choices
  themselves, though the unverifiable data provenance limits how much weight to give it.
tags:
  topic: ["remote-work", "hybrid-work", "mental-health", "job-satisfaction", "wellbeing"]
  method: ["cross-sectional", "secondary-data"]
  population: ["remote-workers", "hybrid-workers", "global-sample", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/MD/Impact of Remote Work Dynamics on Mental Health and Productivity/Impact of Remote Work Dynamics on Mental Health and Productivity.md"
  pdf: "papers/Academic/Impact of Remote Work Dynamics on Mental Health and Productivity.pdf"
  notes: null

---

id: "xiao-2021-impacts-of-working-from-home-during"
title: "Impacts of Working From Home During COVID-19 Pandemic on Physical and Mental Well-Being of Office Workstation Users"
authors:
  - "Xiao, Yijing"
  - "Becerik-Gerber, Burcin"
  - "Lucas, Gale"
  - "Roll, Shawn C."
year: 2021
doi: "10.1097/jom.0000000000002097"
venue: {type: "journal", name: "Journal of Occupational &amp; Environmental Medicine", volume: 63, issue: 3, pages: "181-190"}
citation: "Xiao et al. (2021). Impacts of Working From Home During COVID-19 Pandemic on Physical and Mental Well-Being of Office Workstation Users. Journal of Occupational &amp; Environmental Medicine, 63(3), 181-190. https://doi.org/10.1097/jom.0000000000002097"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A 988-respondent survey of U.S. office workers fielded April-June 2020 found overall
  physical and mental well-being both declined after the abrupt shift to full-time work from
  home, with about two-thirds reporting new physical health issues and three-fourths
  reporting new mental health issues. Regression models showed decreased communication with
  coworkers, increased work distractions, less physical exercise, and higher junk food
  intake were significant predictors of worse well-being, while a dedicated workstation,
  good ergonomic set-up, and satisfaction with indoor environmental quality reduced the odds
  of new health issues. The study offers an early empirical map of which social, behavioral,
  and physical-space factors most strongly track WFH well-being decline.
claims:
  - text: "Decreased communication with coworkers was a significant predictor of both worse mental well-being (b=0.1, P<0.01) and worse physical well-being (b=0.06, P<0.05) in multivariate regression, after controlling for demographics, lifestyle, and home-office factors."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "mental-health"]
    predictors: ["social-support", "isolation"]
  - text: "Increased distractions while working was the strongest occupational predictor of decreased mental well-being (b=-0.15, P<0.001) and was associated with higher odds of reporting two or more new mental health issues (B=0.326, P<0.001); respondents who had to adjust work hours or schedule work around others also had higher odds of new mental and physical health issues."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "stress", "wellbeing"]
    predictors: ["workload", "boundary-management"]
  - text: "Approximately 65% of respondents reported new physical health issues and 74% reported new mental health issues since transitioning to WFH; having a dedicated work room, a good workstation set-up, and higher satisfaction with indoor environmental quality (lighting, thermal, air quality, noise) were each associated with significantly lower odds of reporting new health issues."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health", "wellbeing", "stress"]
    predictors: ["workload", "autonomy"]
population:
  who: "U.S. office/workstation-based workers who transitioned to full-time work from home due to COVID-19; 988 valid survey responses (of 1409 collected) from an online Qualtrics questionnaire"
  where: ["United States"]
  when: "April 24 to June 11, 2020"
  n: 988
  sector: ["business-office", "engineering-architecture", "education-arts", "healthcare-social-services", "computer-science-mathematics", "science", "service-physical-occupations"]
  sample_notes: >
    Convenience/snowball sample recruited via email, social media, and newsletters; screened
    for pre-pandemic office-desk work. Sample skewed heavily toward California (47.3%),
    Caucasian (60.9%), and highly educated/higher-income respondents relative to the general
    U.S. workforce, limiting generalizability; response completion required answering at
    least 75% of items.
limitation:
  primary: "Cross-sectional, self-report data collected in the earliest weeks of the pandemic capture an abrupt-transition snapshot, not durable/routine WFH conditions, and cannot establish causal direction between predictors and well-being."
  others:
    - "Convenience sample over-represents California, Caucasian, and higher-income/higher-education respondents, limiting generalizability to the broader U.S. or global workforce."
    - "Occupational categories, while varied, are not representative of all job types or of within-category job diversity."
    - "Well-being was measured via single-item retrospective self-comparison to pre-WFH status rather than a validated clinical instrument."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantitative, regression-based evidence that reduced coworker communication and
  increased work distractions are significant predictors of worse mental and physical well-
  being during full-time remote work, directly supporting the SNH project's interest in
  social-support and communication-frequency measures as levers for remote-worker health;
  also documents workstation/IEQ factors as a distinct, non-social predictor pathway worth
  separating from social-connection interventions in any design.
tags:
  topic: ["remote-work", "wellbeing", "mental-health", "isolation", "work-life-balance"]
  method: ["survey", "cross-sectional"]
  population: ["office-workers", "remote-workers", "united-states"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Impacts of Working From Home During COVID-19 Pandemic on Physical and Mental Well-Being of Office Workstation Users/Impacts of Working From Home During COVID-19 Pandemic on Physical and Mental Well-Being of Office Workstation Users.md"
  pdf: "papers/Academic/01 Academic - Extended/Impacts of Working From Home During COVID-19 Pandemic on Physical and Mental Well-Being of Office Workstation Users.pdf"
  notes: null

---

id: "althubaiti-2016-information-bias-in-health-research-definition"
title: "Information bias in health research: definition, pitfalls, and adjustment methods"
authors:
  - "Althubaiti, Alaa"
year: 2016
doi: "10.2147/jmdh.s104807"
venue: {type: "journal", name: "Journal of Multidisciplinary Healthcare", volume: null, issue: null, pages: "211"}
citation: "Althubaiti (2016). Information bias in health research: definition, pitfalls, and adjustment methods. Journal of Multidisciplinary Healthcare, 211. https://doi.org/10.2147/jmdh.s104807"
article_type: "review"
method: {design: "review-narrative", approach: "analytical", evidence_level: "reference", preregistered: false}
gist: >
  Althubaiti's narrative review catalogs three under-examined forms of information
  (measurement) bias in health research: self-reporting bias (social desirability and recall
  bias), measurement error bias (systematic vs. random), and confirmation bias, explaining
  the mechanism and consequence of each with worked examples (e.g., case-control recall
  asymmetry inflating odds ratios; naive analysis biasing regression estimators). It
  proposes concrete mitigation strategies -- internal/external validation studies,
  standardized scales (Marlowe-Crowne, Martin-Larsen), memory aids and shortened recall
  windows, calibration and statistical adjustment (simulation-extrapolation, regression
  calibration, instrumental-variable methods), and blinding/independent-check protocols for
  confirmation bias -- summarized in a study-design-by-bias-type reference table.
claims:
  - text: "In case-control studies, cases are more likely than healthy controls to recall past exposure to risk factors, so true exposure tends to be underreported in controls and overreported in cases; this widens the observed exposure-rate gap and inflates the observed odds ratio."
    evidence: "review-narrative"
    support_strength: "low"
    outcomes: ["measurement-bias"]
    predictors: ["sampling-method", "recall-bias"]
  - text: "Analyses that ignore measurement error ('naive analysis') can yield inconsistent or biased and inefficient estimators of regression parameters, producing poor confidence intervals and hypothesis tests; systematic errors are correctable via calibration studies, while random errors require statistical adjustment methods such as simulation-extrapolation, regression calibration, or instrumental-variable approaches."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["measurement-bias"]
    predictors: ["measurement-error", "intervention"]
  - text: "Even gold-standard validation methods carry error: in a cited validation study using 24-hour urinary excretion to estimate sodium intake, the estimated sodium intake tended to be lower than the true amount, illustrating that biological/laboratory measurement is not immune to bias."
    evidence: "review-narrative"
    support_strength: "weak"
    outcomes: ["measurement-bias"]
    predictors: ["measurement-error"]
population:
  who: "Not a study of a human sample; a methodological guidance paper aimed at epidemiologists and medical/health researchers who design and analyze observational or experimental studies using self-report, laboratory, or clinical-judgment data."
  where: []
  when: null
  n: null
  sector: []
  sample_notes: >
    No primary data collection; the paper synthesizes prior literature and cites
    illustrative examples (e.g., drug-use self-report validation, sodium-intake validation,
    blood-alcohol measurement error) drawn from other published studies rather than
    conducting new research.
limitation:
  primary: "This is a narrative, non-systematic review with no stated search strategy, inclusion criteria, or quality appraisal of the literature it draws on, so its claims cannot be treated as a comprehensive or quantitative synthesis of the evidence on information bias."
  others:
    - "The paper addresses general epidemiological and clinical research methodology, not any SNH-specific population, exposure, or outcome, so it functions only as background methods guidance rather than direct SNH evidence."
    - "Worked examples (e.g., sodium-intake validation, blood-alcohol measurement error) are illustrative single citations rather than a systematically assembled evidence base."
risk_of_bias: "medium"
relevance_to_project: >
  The paper itself contains no SNH findings, but it is directly usable as project methods
  guidance: it flags recall bias and social-desirability bias as threats whenever SNH corpus
  studies rely on self-reported loneliness, burnout, or social-support measures, and it
  supplies concrete mitigation tools (validation studies, standardized desirability scales,
  shortened recall windows, statistical adjustment for measurement error) that can inform
  how the project weighs self-report-based evidence when rating support_strength across
  other cards.
tags:
  topic: ["methodology", "measurement"]
  method: ["review-narrative", "analytical"]
  population: ["researchers", "not-applicable"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Information Bias in Health Research Definition Pitfalls and Adjustment Methods/Information Bias in Health Research Definition Pitfalls and Adjustment Methods.md"
  pdf: "papers/Academic/01 Academic - Extended/Information Bias in Health Research Definition Pitfalls and Adjustment Methods.pdf"
  notes: null

---

id: "penney-2005-job-stress-incivility-and-counterproductive-work"
title: "Job stress, incivility, and counterproductive work behavior (CWB): the moderating role of negative affectivity"
authors:
  - "Penney, Lisa M."
  - "Spector, Paul E."
year: 2005
doi: "10.1002/job.336"
venue: {type: "journal", name: "Journal of Organizational Behavior", volume: 26, issue: 7, pages: "777-796"}
citation: "Penney et al. (2005). Job stress, incivility, and counterproductive work behavior (CWB): the moderating role of negative affectivity. Journal of Organizational Behavior, 26(7), 777-796. https://doi.org/10.1002/job.336"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A field study of 299 employed college students (155 with matched peer-report data) tests
  whether workplace incivility, organizational constraints, and interpersonal conflict
  predict lower job satisfaction and more counterproductive work behavior (CWB), and whether
  trait negative affectivity moderates these stressor-CWB links. Incivility, constraints,
  and conflict were all negatively tied to satisfaction and positively tied to CWB, and
  negative affectivity strengthened the incivility/conflict/constraints-to-CWB relationship,
  though effects held more consistently for self-reported than peer-reported CWB. The study
  contributes an early empirical case for workplace incivility as a distinct social stressor
  with its own behavioral consequences, using multi-source (self- and peer-) data to reduce
  single-rater bias.
claims:
  - text: "Self- and peer-rated workplace incivility, interpersonal conflict, and organizational constraints were all significantly negatively correlated with job satisfaction (e.g., incivility r=-0.46 self / -0.38 peer; conflict r=-0.27 self / -0.36 peer; constraints r=-0.36), and incivility and conflict were positively correlated with counterproductive work behavior in most self/peer combinations (e.g., peer-rated incivility with self-CWB r=0.17 and peer-CWB r=0.51)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "counterproductive-work-behavior"]
    predictors: ["workplace-incivility", "interpersonal-conflict", "organizational-constraints"]
  - text: "Negative affectivity moderated the stressor-CWB relationship: the incivility x NA interaction was significant for self-reported CWB (beta=0.81, p<.01), the conflict x NA interaction was significant for both self-reported (beta=0.76) and peer-reported (beta=0.61) CWB, and the constraints x NA interaction was significant for self-reported CWB (beta=0.53); in each case the stressor-CWB slope was steeper for individuals high in negative affectivity, though none of the interactions replicated across both self- and peer-report CWB simultaneously."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["counterproductive-work-behavior"]
    predictors: ["workplace-incivility", "interpersonal-conflict", "organizational-constraints", "negative-affectivity"]
  - text: "Interpersonal conflict was more strongly correlated with person-directed CWB (CWB-P) than organization-directed CWB (CWB-O), a difference confirmed with Hotelling-Williams tests for both self-report [t(295)=2.98, p<.01] and peer-report [t(152)=3.52, p<.01] data, but the equivalent incivility-to-CWB-P vs CWB-O difference was not statistically significant."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["counterproductive-work-behavior"]
    predictors: ["interpersonal-conflict", "workplace-incivility"]
population:
  who: "Employed undergraduate/night-course students at a large public university in the Southeastern U.S., each recruiting one co-worker (not a supervisor) to provide peer-report data"
  where: ["United States"]
  when: "2002"
  n: 299
  sector: ["mixed/unspecified employment sectors"]
  sample_notes: >
    299 self-report participants (mean age 23.3, 77% female, average 2 years job tenure);
    peer questionnaires mailed back by co-workers with a 52% response rate yielding 155
    complete self-peer pairs; no significant differences found between participants with and
    without peer data on measured variables.
limitation:
  primary: "Convenience sample of predominantly female (77%) employed undergraduate students at a single university, which may limit generalizability to broader working populations despite the authors' argument that student-employee CWB patterns resemble non-student samples in prior research."
  others:
    - "Cross-sectional design precludes causal inference about the direction of stressor-CWB and stressor-satisfaction relationships (e.g., dissatisfaction could provoke incivility rather than the reverse)."
    - "Participants self-selected which co-worker received the peer survey, and only 52% of peer surveys were returned, raising selection-bias concerns about who served as the peer rater."
    - "Peer-report and self-report results diverged (e.g., self-rated incivility/constraints did not predict peer-rated CWB), and moderator effects were not consistently replicated across both data sources, weakening confidence in the negative-affectivity moderation findings."
risk_of_bias: "medium"
relevance_to_project: >
  Provides evidence that mild, ambiguous-intent social mistreatment (workplace incivility)
  functions as a distinct job stressor with its own path to reduced satisfaction and
  increased counterproductive behavior, and that individual differences (negative
  affectivity) shape how strongly interpersonal stressors translate into harmful workplace
  conduct -- relevant to designing conflict-escalation safeguards, moderation norms, and
  individual-differences-aware interventions for remote/distributed team and open-source
  community health.
tags:
  topic: ["job-satisfaction", "psychological-safety", "wellbeing", "measurement"]
  method: ["survey", "cross-sectional"]
  population: ["student-employees", "us-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/J Organ Behavior - 2005 - Penney - Job stress  incivility  and counterproductive work behavior  CWB   the moderating role/J Organ Behavior - 2005 - Penney - Job stress  incivility  and counterproductive work behavior  CWB   the moderating role.md"
  pdf: "papers/Academic/01 Academic - Extended/J Organ Behavior - 2005 - Penney - Job stress  incivility  and counterproductive work behavior  CWB   the moderating role.pdf"
  notes: null

---

id: "maslach-2001-job-burnout"
title: "Job Burnout"
authors:
  - "Maslach, Christina"
  - "Schaufeli, Wilmar B."
  - "Leiter, Michael P."
year: 2001
doi: "10.1146/annurev.psych.52.1.397"
venue: {type: "journal", name: "Annual Review of Psychology", volume: 52, issue: 1, pages: "397-422"}
citation: "Maslach et al. (2001). Job Burnout. Annual Review of Psychology, 52(1), 397-422. https://doi.org/10.1146/annurev.psych.52.1.397"
article_type: "review"
method: {design: "review-narrative", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This Annual Review of Psychology chapter by burnout's original researchers synthesizes 25
  years of empirical work establishing burnout as a three-dimensional syndrome (exhaustion,
  cynicism, reduced efficacy) that is a chronic response to job stressors rather than a form
  of depression. It documents that organizational and situational factors -- workload,
  control, reward, community/social support, fairness, and values -- are far stronger and
  more consistent predictors of burnout than individual demographic or personality traits,
  and introduces job engagement (energy, involvement, efficacy) as burnout's positive
  antithesis. It concludes that effective interventions must combine organizational-level
  change with individual coping training, since individual-only programs typically reduce
  exhaustion but leave cynicism and inefficacy largely unchanged.
claims:
  - text: "Burnout arises from chronic mismatches between people and their job across six areas of worklife -- workload, control, reward, community, fairness, and values -- and situational/organizational factors show stronger, more consistent associations with burnout than demographic or personality variables, indicating burnout is primarily a social/organizational phenomenon rather than an individual one."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["workload", "social-support", "organizational-culture", "autonomy"]
  - text: "A lack of social support -- especially from supervisors, more so than from coworkers -- is consistently and strongly linked to burnout, and perceived unfairness/inequity in the workplace independently fuels both emotional exhaustion and cynicism; an intervention targeting perceived inequity produced a significant decrease in exhaustion at 6 and 12 months versus controls (van Dierendonck et al 1998)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["social-support", "leadership-style", "organizational-culture"]
  - text: "Using phase-model burnout classification, roughly 20% of ~25,000 North American employees (62 samples) fell into the most advanced burnout phase, versus ~28% of ~7,000 employees across 21 samples in 12 mostly Asian/Eastern European countries, with national incidence ranging from 1% to 69% and the highest rates in Japan and Taiwan -- indicating burnout is a global phenomenon whose prevalence varies substantially by national/cultural context."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["burnout"]
    predictors: ["organizational-culture"]
population:
  who: "Narrative synthesis of empirical burnout research (predominantly quantitative survey studies) conducted from the mid-1970s through 2001, spanning human-service, healthcare, and education workers initially, later expanded to general occupational samples; includes large phase-model comparison datasets (62 North American samples, n≈25,000 employees; 21 samples across 12 Asian/Eastern European countries, n≈7,000 employees)."
  where: ["United States", "Canada", "Netherlands", "Germany", "France", "Poland", "United Kingdom", "Ireland", "Japan", "Taiwan", "Israel"]
  when: "1974-2001"
  n: null
  sector: ["healthcare", "education", "human-services", "general-workforce"]
  sample_notes: >
    Aggregates non-random, convenience-sampled studies from the wider literature rather than
    a single dataset; the authors (Maslach, Schaufeli, Leiter) are also the creators of the
    primary measurement instrument (the Maslach Burnout Inventory), a potential source of
    interpretive bias; the authors themselves flag that cross-national comparisons rest on
    non-random, non-representative samples.
limitation:
  primary: "As a narrative (non-systematic) review, it does not quantitatively pool effect sizes and its conclusions depend on the state and selection of literature available through 2001, much of which is cross-sectional/correlational and cannot establish causal direction between burnout and its correlates."
  others:
    - "Very few longitudinal studies existed at the time of writing, so sequential developmental models of burnout (exhaustion to cynicism to inefficacy) remain only partially tested."
    - "Nearly all cited findings rely on self-report questionnaires (chiefly the MBI), raising common-method-variance concerns."
    - "Cross-national burnout comparisons used non-random, non-representative samples, limiting confidence in true country-level differences."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs how SNH should operationalize burnout and its 'community' antecedent
  (loss of positive workplace connection and social support) as a core mechanism linking
  isolation to burnout in remote and open-source work, and supports designing interventions
  that pair organizational changes (workload, fairness, values alignment) with individual
  support rather than relying on coping-skills training alone.
tags:
  topic: ["burnout", "wellbeing", "social-support", "mental-health", "job-engagement", "measurement"]
  method: ["review-narrative"]
  population: ["healthcare", "education", "human-services", "cross-national"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Job Burnout/Job Burnout.md"
  pdf: "papers/Academic/01 Academic - Extended/Job Burnout.pdf"
  notes: null

---

id: "posel-2021-job-loss-and-mental-health-during"
title: "Job loss and mental health during the COVID-19 lockdown: Evidence from South Africa"
authors:
  - "Posel, Dorrit"
  - "Oyenubi, Adeola"
  - "Kollamparambil, Umakrishnan"
year: 2021
doi: "10.1371/journal.pone.0249352"
venue: {type: "journal", name: "PLOS ONE", volume: 16, issue: 3, pages: "e0249352"}
citation: "Posel et al. (2021). Job loss and mental health during the COVID-19 lockdown: Evidence from South Africa. PLOS ONE, 16(3), e0249352. https://doi.org/10.1371/journal.pone.0249352"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using two waves of South Africa's NIDS-CRAM telephonic panel survey during the COVID-19
  lockdown, this study exploits the pandemic's exogenous job losses as a natural experiment
  to estimate the effect of job loss and furlough on depressive symptoms (PHQ-2). Adults who
  retained employment reported significantly lower depression scores than those who lost
  jobs, with the protective effect of employment growing the longer it was retained, while
  furlough (having a job to return to but no current work or pay) conferred no mental-health
  benefit at all. Paid leave, by contrast, was strongly protective, suggesting that
  continued income rather than job attachment per se buffers mental health during economic
  shocks.
claims:
  - text: "Adults who retained employment in Wave 1 were 5.1 percentage points more likely to report no depressive symptoms than those who lost their jobs, rising to a further 6 percentage points more likely if they also retained employment in Wave 2, indicating the mental-health benefit of employment compounds over time."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["intervention"]
  - text: "Being furloughed (not working, not earning, but with a job to return to) showed no significant relationship with PHQ-2 depression scores compared to job loss, meaning the mere expectation of future work provided no measurable psychological protection."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["workload"]
  - text: "Adults on paid leave in Wave 2 were about 10 percentage points less likely than those who had lost their job to report no depressive symptoms, and paid leave produced significantly lower depression scores even relative to actively working adults (chi-square = 8.02, p < 0.02), indicating continued income protects mental health more than job status alone."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["social-support"]
population:
  who: "Adults aged 18+ in South Africa who were employed immediately before the COVID-19 hard lockdown, re-interviewed in both waves of the NIDS-CRAM rapid mobile survey with complete data on key variables"
  where: ["South Africa"]
  when: "May-August 2020 (NIDS-CRAM Waves 1-2), with baseline mental health data from NIDS 2017"
  n: 2213
  sector: ["general-population", "mixed-employment"]
  sample_notes: >
    Sample drawn from the 2017 National Income Dynamics Study (NIDS) panel via stratified
    batch sampling; Wave 1 surveyed 7073 adults, Wave 2 re-interviewed 5676 (80.2% response
    rate); analytic sample restricted to the 2213 pre-lockdown employed adults with non-
    missing data across both waves. No survey weights used (authors treat estimates as
    sample-based, not population-representative); telephonic interviews may still under-
    represent those without phone access.
limitation:
  primary: "Mental health measures are not directly comparable across time points: NIDS 2017 used the CES-D 10 while NIDS-CRAM Wave 2 used the abbreviated PHQ-2, precluding individual fixed-effects models or before/after comparisons of the same depression instrument."
  others:
    - "The 2-item PHQ-2 is a coarse screener that is less sensitive to variation in depression severity than the full PHQ-9 or CES-D 10, likely underestimating true symptom severity."
    - "No survey weights were applied, so estimates are sample-based rather than nationally representative, despite the underlying panel's stratified design."
    - "Observation window covers only the first few months of lockdown (through August 2020), limiting inference about longer-term mental health trajectories."
risk_of_bias: "low"
relevance_to_project: >
  Provides a rare quasi-experimental (exogenous shock) estimate of how job loss versus
  continued income affects depression, directly informing SNH's evidence base on
  economic/employment precarity as a predictor of mental-health decline; the finding that
  furlough (job security without income or activity) offers no protection is relevant to
  designing remote-work and community interventions that address income/activity continuity,
  not just formal job status.
tags:
  topic: ["mental-health", "wellbeing"]
  method: ["longitudinal", "survey"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa.md"
  pdf: "papers/Academic/01 Academic - Extended/Job Loss and Mental Health during the COVID-19 Lockdown Evidence from South Africa.pdf"
  notes: null

---

id: "star-2016-layers-of-silence-arenas-of-voice"
title: "Layers of Silence, Arenas of Voice: The Ecology of Visible and Invisible Work"
authors:
  - "Star, Susan Leigh"
  - "Strauss, Anselm"
year: 2016
doi: "10.7551/mitpress/10113.003.0024"
venue: {type: "book", name: "Boundary Objects and Beyond", volume: null, issue: null, pages: "351-374"}
citation: "Star et al. (2016). Layers of Silence, Arenas of Voice: The Ecology of Visible and Invisible Work. Boundary Objects and Beyond, 351-374. https://doi.org/10.7551/mitpress/10113.003.0024"
article_type: "theory"
method: {design: "theory", approach: "analytical", evidence_level: "weak", preregistered: false}
gist: >
  Star and Strauss develop a theoretical framework for CSCW design showing that no work is
  intrinsically visible or invisible; visibility is a negotiated, contextual status shaped
  by power, gender, and organizational values. Drawing on ethnographies of domestic workers,
  nurses, secretaries, and scientists, they identify three mechanisms that produce invisible
  work -- 'creating a nonperson,' 'disembedding background work,' and 'going backstage' --
  and argue that making work visible for one group (e.g., through metrics or classification
  systems) frequently displaces the burden onto less powerful workers rather than
  eliminating it. The paper closes with four design criteria for equitably balancing
  visibility and invisibility in coordination systems.
claims:
  - text: "Ethnographic accounts of domestic workers (Rollins, 1985) show that intense employer micromanagement coexists with the worker's total social invisibility ('nonperson' status) -- e.g., employers audio- and video-recorded workers' rooms and conversations while treating them as unable to hear or be addressed -- illustrating that visibility of the act of working and visibility of the person as a social actor are independently controlled by the more powerful party."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["isolation", "stress"]
    predictors: ["organizational-culture", "inclusiveness"]
  - text: "The Iowa Nursing Intervention Classification effort (Bowker, Timmermans & Star, 1995), which codified over 300 nursing interventions to make previously invisible, unrecorded nursing work visible in the medical record for professionalization and research purposes, is described as producing a visibility tradeoff: increased legitimacy and traceability of nursing work came bundled with increased surveillance and paperwork burden for nurses."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["burnout", "job-satisfaction"]
    predictors: ["workload", "organizational-culture"]
  - text: "The authors argue that CSCW systems which increase visibility of one type of work (e.g., a shared publishing system letting scientists share findings faster) can inequitably displace articulation-work burden onto lower-status workers (e.g., lab technicians, secretaries) whose reporting and data-entry load rises without corresponding recognition, and they propose four design criteria -- shared reduction of complexity, temporal/local flexibility, preserved arm's-length relationships, and tradeoff-aware requirements analysis -- for equitable visibility design."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["collaboration", "burnout"]
    predictors: ["workload", "organizational-culture"]
population:
  who: "Not an empirical sample; the paper synthesizes prior ethnographic and sociological case studies of specific occupational groups (domestic workers, nurses, secretaries, cleaners, scientists, athletes, fieldworkers) drawn from earlier published research."
  where: ["United States"]
  when: null
  n: null
  sector: ["healthcare", "domestic-work", "academia", "other"]
  sample_notes: >
    No original data collection; the analysis is built almost entirely on secondary sources,
    most extensively Judith Rollins' 1985 ethnography of domestic workers ('Between Women')
    and a 1995 study of nursing classification work by Bowker, Timmermans & Star,
    supplemented by numerous other cited studies and literary/anecdotal examples.
limitation:
  primary: "It is a conceptual essay synthesizing others' prior qualitative studies rather than presenting new primary data or systematic evidence, so its central claims about the 'ecology' of visible and invisible work are illustrative and theory-building rather than empirically tested."
  others:
    - "Heavy reliance on a small number of secondary ethnographic accounts (especially Rollins 1985) without independent verification or triangulation."
    - "Examples are predominantly US-centric (domestic service, American health care, US census categories), limiting generalizability across cultures and labor systems."
    - "The proposed CSCW design criteria are stated as normative principles but are not evaluated against any implemented system or outcome data."
risk_of_bias: "not-applicable"
relevance_to_project: >
  This paper's articulation-work/invisible-work framework directly informs how SNH should
  think about remote workers' and open-source maintainers' uncredited coordination, care,
  and community-tending labor (e.g., maintainer burnout, informal peer support) that escapes
  formal metrics and therefore goes unsupported by tools and management practice; its four
  design criteria offer concrete principles for building SNH measurement and support systems
  that surface such labor without inequitably shifting surveillance or reporting burden onto
  the least powerful contributors.
tags:
  topic: ["remote-work", "collaboration", "burnout", "measurement", "methodology"]
  method: ["theory", "qualitative"]
  population: ["knowledge-workers", "healthcare-workers", "domestic-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Layers of Silence Arenas of Voice The Ecology of Visible and Invisible Work/Layers of Silence Arenas of Voice The Ecology of Visible and Invisible Work.md"
  pdf: "papers/Academic/01 Academic - Extended/Layers of Silence Arenas of Voice The Ecology of Visible and Invisible Work.pdf"
  notes: null

---

id: "mitchell-2011-measuring-health-related-productivity-loss"
title: "Measuring Health-Related Productivity Loss"
authors:
  - "Mitchell, Rebecca J."
  - "Bates, Paul"
year: 2011
doi: "10.1089/pop.2010.0014"
venue: {type: "journal", name: "Population Health Management", volume: 14, issue: 2, pages: "93-98"}
citation: "Mitchell et al. (2011). Measuring Health-Related Productivity Loss. Population Health Management, 14(2), 93-98. https://doi.org/10.1089/pop.2010.0014"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using Health Risk Appraisal survey data from over 1 million employed OptumHealth
  participants (2007-2009), this study used propensity-score matching to isolate the
  productivity impact of 13 chronic health conditions and 4 lifestyle health risks (e.g.,
  obesity, smoking, high blood pressure/cholesterol), measuring both absenteeism and
  presenteeism (via the Work Limitations Questionnaire). It found that employees with health
  conditions or high risk levels lost significantly more workdays to absence and reduced on-
  the-job performance than matched healthy controls, and monetized these losses to show they
  can rival or exceed direct medical costs, with depression ranking among the three
  costliest conditions for productivity.
claims:
  - text: "After propensity-score matching and regression adjustment, employees with a given health condition or health risk had productivity costs ranging from $15 to $1,601 more per year than matched employees without it; for a 10,000-employee company this implies nearly $3.8 million in additional annual productivity loss."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity"]
    predictors: ["health-status"]
  - text: "Cancer, bronchitis, and depression were among the top three health conditions ranked by annual productivity cost per person, and combined productivity costs across conditions equaled about $0.40 for every $1 of medical costs for an average-size employer."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "mental-health"]
    predictors: ["health-status"]
  - text: "Productivity loss showed a dose-response relationship with health burden: participants with 2+ health conditions averaged 3.0 absent days and 20.1 unproductive days per year versus 1.4 and 3.7 days for those with none, and participants at high risk (5+ risk factors) averaged 3.6 absent days and 28.9 unproductive days versus 1.6 and 5.1 for low-risk participants."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["productivity", "wellbeing"]
    predictors: ["health-status"]
population:
  who: "Employed U.S. adults (ages 18-70) who completed employer-sponsored OptumHealth Health Risk Appraisal (HRA) surveys; a subgroup completed a second survey ~1 year later forming a matched-cohort sample used for cost analyses."
  where: ["United States"]
  when: "January 2007 to December 2009"
  n: 1000000
  sector: ["corporate", "occupational-health"]
  sample_notes: >
    Baseline sample of ~1.3 million HRA respondents narrowed to 1 million after
    age/completeness exclusions; ~260,000 also completed a follow-up survey and formed the
    cohort used for propensity-matched cost estimates. Sample drawn only from employers
    purchasing OptumHealth HRA services (77% white, 58% female, average age 42), which
    limits representativeness; all health measures (conditions, blood pressure, cholesterol,
    height/weight) were self-reported.
limitation:
  primary: "Monetization relies on an assumed wage multiplier (1.61) and extrapolation of 2-week presenteeism recall to annual estimates, and propensity-score matching cannot control for all confounders, so causal attribution of costs to specific conditions is uncertain."
  others:
    - "All health condition, risk factor, and biometric data (blood pressure, cholesterol, height, weight) were self-reported and not independently verified"
    - "Sample limited to employers who purchased OptumHealth HRA services, restricting generalizability across industries and job types"
    - "No direct linkage to actual medical claims data; medical cost comparisons used separate benchmark (ETG) data rather than the same participants' claims"
risk_of_bias: "medium"
relevance_to_project: >
  Offers a concrete, monetized method for quantifying how health conditions -- including
  depression, which ranked among the top three costliest for productivity -- translate into
  absenteeism and presenteeism losses, giving the SNH project a template and benchmark for
  building a cost/ROI case that mental-health and burnout-related interventions in
  remote/hybrid workplaces are not just wellbeing goods but financially material to
  employers.
tags:
  topic: ["mental-health", "wellbeing", "burnout", "measurement"]
  method: ["survey", "quasi-experimental"]
  population: ["employed-adults", "us-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Measuring Health-Related Productivity Loss/Measuring Health-Related Productivity Loss.md"
  pdf: "papers/Academic/01 Academic - Extended/Measuring Health-Related Productivity Loss.pdf"
  notes: null

---

id: "collins-2016-social-support-in-the-workplace-between"
title: "Social support in the workplace between teleworkers, office‐based colleagues and supervisors"
authors:
  - "Collins, Alison M."
  - "Hislop, Donald"
  - "Cartwright, Susan"
year: 2016
doi: "10.1111/ntwe.12065"
venue: {type: "journal", name: "New Technology, Work and Employment", volume: 31, issue: 2, pages: "161-175"}
citation: "Collins et al. (2016). Social support in the workplace between teleworkers, office‐based colleagues and supervisors. New Technology, Work and Employment, 31(2), 161-175. https://doi.org/10.1111/ntwe.12065"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This qualitative case study of a UK local authority's permanent full-time teleworking
  initiative finds that social support diverges sharply between office-based and teleworking
  staff: teleworkers relied on social support networks built before they began working from
  home, developed close bonds mainly with other teleworkers, and used this arrangement to
  distance themselves from disliked office relationships, while office-based staff continued
  to value and rely on co-located peer support. Over time, staff turnover, office
  restructuring, and infrequent office visits eroded teleworkers' ties to office-based
  colleagues, producing a broader 'us versus them' social disconnection between the two
  groups. Supervisors' relationships with teleworkers required more emotional investment and
  home-boundary-crossing than with office-based staff, with quality varying by individual
  relationship.
claims:
  - text: "Teleworkers' social support relationships with office-based colleagues diminished over time due to staff turnover and office restructuring, while teleworkers instead relied on and deepened social support ties with other teleworkers they had known prior to working from home."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "sense-of-belonging"]
    predictors: ["remote-work-intensity", "social-support"]
  - text: "Despite the organisation directing teleworkers to route queries through supervisors, the majority of teleworkers instead contacted fellow teleworkers (via personal phones and email) for informational, instrumental, and emotional support, indicating strong reliance on peer 'buddy' relationships rather than official channels."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["help-seeking", "communication"]
    predictors: ["peer-mentoring", "social-support"]
  - text: "Office-based staff continued to draw strong social, informational, and emotional support from co-located peers and reported team leaders actively fostering socializing (e.g., reorganizing seating, encouraging lunches), whereas only about half of teleworkers described a personal, emotionally supportive relationship with their supervisor, with the rest experiencing more transactional, compliance-based ties."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["social-support", "job-satisfaction"]
    predictors: ["leadership-style", "team-cohesion"]
population:
  who: "33 clerical/administrative employees of a UK local authority (council tax, benefits, and community services departments): 13 permanent teleworkers (11 full-time, 2 part-time), 12 office-based clerical staff, 6 supervisors, and 2 managers."
  where: ["United Kingdom"]
  when: null
  n: 33
  sector: ["public-sector", "government", "clerical-administrative"]
  sample_notes: >
    Single-organisation qualitative case study; participants individually interviewed (semi-
    structured, ~1 hour, transcribed verbatim) at office or home; teleworkers were permanent
    full-time home-based clerical staff, a neglected sub-group relative to the
    professional/knowledge-worker teleworkers usually studied. Findings are not
    generalisable beyond this case.
limitation:
  primary: "Single case-study organisation with a small, occupationally narrow sample (clerical/administrative local-authority staff), so findings cannot be generalised to teleworkers or workplaces more broadly."
  others:
    - "Qualitative, retrospective, self-report interview data susceptible to recall and self-presentation bias."
    - "No longitudinal or comparative design to causally establish that time-teleworking, rather than other factors, drives the social disconnection observed."
    - "Sample restricted to routine clerical telework with low autonomy; results may not extend to high-autonomy professional/knowledge teleworkers who dominate prior literature."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's model of remote-work isolation mechanisms: it shows
  social support networks for permanent remote workers depend on pre-existing relationships
  and decay over time without structured touchpoints (office visits, onboarding of new
  starters, deliberate manager check-ins), and that peer-to-peer (not just manager-to-
  worker) support channels are what remote workers actually use, which has design
  implications for community/tooling interventions aimed at sustaining belonging among long-
  tenured remote workers.
tags:
  topic: ["remote-work", "isolation", "social-support", "community-health"]
  method: ["qualitative", "case-study"]
  population: ["remote-workers", "public-sector", "clerical-workers"]
source:
  markdown: "Papers_Data/Academic/MD/New Technol Work Employ - 2016 - Collins - Social support in the workplace between teleworkers  office‐based colleagues and/New Technol Work Employ - 2016 - Collins - Social support in the workplace between teleworkers  office‐based colleagues and.md"
  pdf: null
  notes: null

---

id: "lyzwinski-2024-organizational-and-occupational-health-issues-with"
title: "Organizational and occupational health issues with working remotely during the pandemic: a scoping review of remote work and health"
authors:
  - "Lyzwinski, Lynnette-Natalia"
year: 2024
doi: "10.1093/joccuh/uiae005"
venue: {type: "journal", name: "Journal of Occupational Health", volume: 66, issue: 1, pages: null}
citation: "Lyzwinski (2024). Organizational and occupational health issues with working remotely during the pandemic: a scoping review of remote work and health. Journal of Occupational Health, 66(1). https://doi.org/10.1093/joccuh/uiae005"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  A PubMed/Google Scholar scoping review of 62 studies (spanning Europe, North America,
  South America, Asia, and the Asia-Pacific) on white-collar remote work during the first
  two years of the COVID-19 pandemic finds that social isolation and loneliness were the
  most consistently reported barriers to remote-worker wellbeing, and that co-worker and
  managerial social support, along with non-toxic leadership styles, buffered against these
  harms. Effects on productivity, job satisfaction, and work-life balance were mixed across
  studies and depended heavily on gender, childcare responsibilities, home-office adequacy,
  and leadership behavior, with women and parents (especially mothers) disproportionately
  disadvantaged.
claims:
  - text: "Level of social support was strongly linked to remote-worker isolation and loneliness: one included study found remote workers with low co-worker support were roughly 4 times more likely to report feelings of isolation than those with high co-worker support, and workers with low managerial support were 2.5 times more likely to report loneliness than those with high managerial support (Miyake et al., cited in the review)."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["isolation", "loneliness", "wellbeing"]
    predictors: ["social-support", "leadership-style"]
  - text: "Women reported higher stress and lower wellbeing than men across multiple included studies, and this gap widened with childcare load; one Australian study found a 63% productivity reduction among women with children versus a 32% reduction among men without children, and several studies linked unequal division of household/childcare labor to women's lower remote-work wellbeing and productivity."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["wellbeing", "stress", "productivity"]
    predictors: ["workload", "boundary-management"]
  - text: "Leadership style moderated remote-worker mental health: intrusive/toxic leadership was associated with increased depression, anxiety, reduced happiness, and workaholism in included studies, whereas participative and identity leadership were positively associated with job satisfaction and negatively associated with workplace loneliness."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health", "job-satisfaction", "loneliness"]
    predictors: ["leadership-style"]
population:
  who: "62 empirical studies of white-collar/office-type remote workers (e.g., managers, admin staff, researchers, academics, teachers, healthcare and public-sector employees) working from home during COVID-19 lockdowns; most included studies used cross-sectional self-report surveys."
  where: ["Europe", "North America", "South America", "Asia", "Asia-Pacific"]
  when: "Data collected March 2020 to 2021; search conducted October 2021"
  n: null
  sector: ["office-white-collar", "public-sector", "education", "healthcare", "academia"]
  sample_notes: >
    Aggregates 62 heterogeneous studies (mostly cross-sectional, some longitudinal/diary
    designs) identified via a PubMed/Medline and Google Scholar scoping search plus manual
    reference searches; restricted to English-language studies (or
    French/German/Polish/Italian) on white-collar workers 18+, excluding intervention
    studies and studies not assessing wellbeing/stress/satisfaction; no formal quality/risk-
    of-bias appraisal of included studies as is typical for scoping reviews.
limitation:
  primary: "As a scoping review, it did not formally appraise the methodological quality or risk of bias of the 62 included studies, most of which relied on cross-sectional self-report measures that limit causal inference and are open to self-report/recall bias."
  others:
    - "Search restricted largely to PubMed/Medline and English-language (plus a few European-language) literature, likely missing non-Western and non-English evidence."
    - "Included studies used highly heterogeneous, non-standardized measures of wellbeing, productivity, and isolation, limiting direct comparability or pooled synthesis."
    - "Review authors note gaps in evidence on age, ethnicity, socioeconomic status, disability, and domestic-violence risk among remote workers, which were rarely examined in the underlying studies."
risk_of_bias: "medium"
relevance_to_project: >
  This review is a strong evidence map for SNH design priorities: it identifies co-worker
  and managerial social support as the primary quantified buffer against remote-work
  isolation and loneliness (with concrete odds/likelihood ratios), and flags leadership
  style, gender, and childcare access as key moderators of remote-worker wellbeing and
  turnover-relevant outcomes — directly informing which interventions (peer support
  structures, leadership training, family-friendly policy) an SNH toolkit should prioritize
  and evaluate.
tags:
  topic: ["remote-work", "isolation", "loneliness", "social-support", "wellbeing", "burnout"]
  method: ["review-scoping"]
  population: ["remote-workers", "white-collar", "parents-caregivers", "women"]
source:
  markdown: "Papers_Data/Academic/MD/Organizational and occupational health issues with working remotely during the pandemic- a scoping review of remote work and health/Organizational and occupational health issues with working remotely during the pandemic- a scoping review of remote work and health.md"
  pdf: "papers/Academic/Organizational and occupational health issues with working remotely during the pandemic- a scoping review of remote work and health.pdf"
  notes: null

---

id: "wyman-2019-peeradult-network-structure-and-suicide-attempts"
title: "Peer‐adult network structure and suicide attempts in 38 high schools: implications for network‐informed suicide prevention"
authors:
  - "Wyman, Peter A."
  - "Pickering, Trevor A."
  - "Pisani, Anthony R."
  - "Rulison, Kelly"
  - "Schmeelk‐Cone, Karen"
  - "Hartley, Chelsey"
  - "Gould, Madelyn"
  - "Caine, Eric D."
  - "LoMurray, Mark"
  - "Brown, Charles Hendricks"
  - "Valente, Thomas W."
year: 2019
doi: "10.1111/jcpp.13102"
venue: {type: "journal", name: "Journal of Child Psychology and Psychiatry", volume: 60, issue: 10, pages: "1065-1075"}
citation: "Wyman et al. (2019). Peer‐adult network structure and suicide attempts in 38 high schools: implications for network‐informed suicide prevention. Journal of Child Psychology and Psychiatry, 60(10), 1065-1075. https://doi.org/10.1111/jcpp.13102"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using friend- and trusted-adult-nomination surveys from 10,291 students across 38 US high
  schools, this study builds whole-school social networks and tests whether structural
  features (integration, cohesion, centralization, and the relative popularity/clustering of
  suicidal students) predict school-level and individual rates of suicidal ideation (SI) and
  attempts (SA). Lower peer integration/cohesion and greater student isolation from trusted
  adults were linked to higher SI/SA, and schools where adult connections were concentrated
  in few students, or where suicidal students were unusually popular, had higher attempt
  rates. The paper argues that schoolwide network patterns, not just individual
  connectedness, are a distinct and actionable target for suicide-prevention design
  ("network-informed suicide prevention").
claims:
  - text: "In a multivariable school-level model, suicide attempt (SA) rates were higher in schools where youth-adult relationships were concentrated in fewer students (centralized outgoing-to-adult ties; B = 4.95, 95% CI [1.46, 8.44]) and where suicidal students had higher relative popularity versus nonsuicidal peers (B = 0.93, 95% CI [0.10, 1.77])."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["suicide-attempt"]
    predictors: ["network-structure", "peer-influence"]
  - text: "Individually, isolation from trusted adults was strongly associated with attempts: 42.7% of students with SA were adult-isolates versus 31.5% of non-suicidal students (OR = 1.70, 95% CI [1.44, 2.01] for SA vs. no-STB), and a 10-percentage-point (1 SD) reduction in school adult-isolation was associated with 1.41 fewer attempts per 100 students (a 20.1% relative reduction)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["suicide-attempt"]
    predictors: ["social-support", "isolation"]
  - text: "Schools with greater peer network integration and cohesion (more friendship ties, larger interconnected friend groups, higher transitivity) had lower rates of both SI and SA at the school level, and students who shared a trusted adult with a friend had markedly lower odds of attempts (OR = 0.50, 95% CI [0.43, 0.60] for SA vs. no-STB) than students who did not."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["suicide-attempt", "suicidal-ideation"]
    predictors: ["isolation", "social-support", "network-cohesion"]
population:
  who: "High-school students (grades 9-12) in 38 US high schools, plus the friends and trusted school adults they nominated, drawn from the baseline (pre-intervention) sample of the Sources of Strength suicide-prevention trial"
  where: ["United States (New York State)", "United States (North Dakota)"]
  when: "2010-2013 (baseline assessments, four enrollment cohorts, prior to program implementation)"
  n: 10291
  sector: ["education", "adolescent-health"]
  sample_notes: >
    Schools recruited from counties with above-average youth suicide rates in primarily
    rural/micropolitan communities (4 of 38 schools served American Indian reservations);
    school-level participation ranged 66%-95.6% (M=83%); sample was 48.9% female, 79% white,
    4.6% Native American; analysis unit for school-level models is only 38 schools, limiting
    statistical power despite the large individual N.
limitation:
  primary: "Network and outcome data were collected contemporaneously (cross-sectional), so the study cannot establish whether weak networks/adult isolation cause STB or are a consequence of it (e.g., students who attempt may subsequently withdraw from adults)."
  others:
    - "STB is measured entirely by self-report (YRBS items) with no corroborating records, as in nearly all general-population STB studies."
    - "Friend and adult nominations were restricted to the same school, and findings come from small-town/micropolitan, high-suicide-rate communities, so generalizability to urban or lower-risk schools is uncertain."
    - "School-level multivariable models are based on only 38 schools, so many univariable associations did not survive multivariable adjustment or sensitivity analyses controlling for depression, bullying, and violence victimization."
risk_of_bias: "medium"
relevance_to_project: >
  Offers a concrete, validated method (whole-network nomination +
  integration/cohesion/centralization metrics) for treating a community's social-support
  structure, not just individual connectedness, as the unit of design and measurement --
  directly transferable to assessing whether a remote-work or open-source community over-
  concentrates trusted-contact/mentor relationships in too few people, and to flagging risk
  when distressed members gain outsized social influence or clustering.
tags:
  topic: ["suicide-prevention", "isolation", "social-support", "community-health", "mental-health"]
  method: ["cross-sectional", "survey", "network-analysis"]
  population: ["adolescents", "students", "school-community"]
source:
  markdown: "Papers_Data/Academic/MD/Peer-adult network structure and suicide attempts/Peer-adult network structure and suicide attempts.md"
  pdf: "papers/Remote Worker SNH/Peer-adult network structure and suicide attempts.pdf"
  notes: null

---

id: "guest-2002-perspectives-on-the-study-of-work"
title: "Perspectives on the Study of Work-life Balance"
authors:
  - "Guest, David E."
year: 2002
doi: "10.1177/0539018402041002005"
venue: {type: "journal", name: "Social Science Information", volume: 41, issue: 2, pages: "255-279"}
citation: "Guest (2002). Perspectives on the Study of Work-life Balance. Social Science Information, 41(2), 255-279. https://doi.org/10.1177/0539018402041002005"
article_type: "review"
method: {design: "review-scoping", approach: "analytical", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  David Guest's 2002 Social Science Information article is a selective, conceptual review of
  work-life balance (WLB) research from a work-and-organizational-psychology perspective,
  arguing that 'balance' functions as a contested metaphor with both objective (hours,
  roles) and subjective (perceived equilibrium) meanings. It proposes a determinants-nature-
  consequences model (Table 1) linking work and home demands, organizational and home
  culture, and individual differences to subjective and objective indicators of balance and
  downstream well-being, performance, and relational outcomes, then illustrates the model
  with UK CIPD survey data and selected studies (Kossek et al. 2001; Mauno and Kinnunen
  1999; Clark 2000). It concludes that most evidence points to negative consequences of
  imbalance but that the field is methodologically dominated by cross-sectional surveys and
  North American/North European samples, and calls for richer designs (diaries, interviews,
  cross-national comparison).
claims:
  - text: "In annual UK CIPD Psychological Contract surveys of a random sample of roughly 1000 working adults, 73% (1998) and 74% (2000) reported having the right balance between work and life outside work; among those reporting the wrong balance, 9 in 10 said work dominated, and there was a strong correlation between working longer hours and reported imbalance."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "job-satisfaction"]
    predictors: ["workload"]
  - text: "A regression analysis of the same CIPD survey data showed imbalance was more likely among those working longer hours, in managerial or higher-income positions, women, those with dependent children, and multiple job-holders, and less likely among those reporting a friendly organizational climate with more HR practices and greater autonomy/participation; notably, the mere presence of family-friendly practices was NOT associated with reported balance."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["workload", "organizational-culture", "autonomy"]
  - text: "Citing Kossek et al. (2001), the review reports that a climate of 'sharing' (versus 'sacrifice') at home and work had a positive association with performance and well-being, while caring for an elderly relative at home in an unsupportive, non-sharing climate was particularly negatively associated with performance and well-being at both work and home."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["performance", "wellbeing", "work-life-balance"]
    predictors: ["social-support", "organizational-culture"]
population:
  who: "Composite population drawn together for illustrative review: UK working adults from CIPD Psychological Contract surveys (~1000/year, random sample, excluding unemployed and self-employed), plus samples from cited empirical studies (e.g., 215 Finnish dual-earner couples in Mauno and Kinnunen 1999, US Air Force women in Vinokur et al. 1999, UK graduates in Sturges et al. 2000, MBA students in Peiperl and Jones 2000)."
  where: ["UK", "Finland", "USA"]
  when: "Survey and cited-study data mostly 1998-2001"
  n: null
  sector: []
  sample_notes: >
    Not a single primary sample; the article synthesizes the author's own national survey
    work with selectively cited studies. The author explicitly states the review is
    'selective and illustrative' rather than comprehensive, and notes the underlying
    evidence base is dominated by North American and North European, largely white-
    collar/managerial samples.
limitation:
  primary: "The review is explicitly selective and illustrative rather than a systematic review, and the proposed determinants-nature-consequences model is a preliminary conceptual framework that is not itself empirically tested as a whole."
  others:
    - "Heavy reliance on the author's own UK CIPD cross-sectional survey data (self-report, correlational, excludes unemployed/self-employed) for the central empirical illustrations."
    - "Evidence base is dominated by North American and North European research and by large-scale cross-sectional surveys using structural equation modelling, with little coverage of qualitative or diary-based methods or of East European/non-Western contexts."
risk_of_bias: "medium"
relevance_to_project: >
  The article's determinants-nature-consequences model separates objective indicators
  (hours, roles) from subjective perceived balance and identifies organizational culture,
  autonomy, and direct participation -- rather than the mere presence of family-friendly
  policies -- as the levers actually associated with better reported work-life balance; this
  is directly useful for SNH intervention design for remote/hybrid workers, since it
  suggests policy adoption alone will not move the needle without genuine autonomy and a
  supportive climate, and it offers a ready-made framework (work/home demands, culture,
  individual differences -> subjective/objective balance -> well-being, performance,
  relational outcomes) for structuring SNH measures.
tags:
  topic: ["work-life-balance", "wellbeing", "burnout", "measurement"]
  method: ["review-scoping", "survey"]
  population: ["knowledge-workers", "dual-earner-couples", "managers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Perspectives on the Study of Work-Life Balance/Perspectives on the Study of Work-Life Balance.md"
  pdf: "papers/Academic/01 Academic - Extended/Perspectives on the Study of Work-Life Balance.pdf"
  notes: null

---

id: "nitschke-2020-resilience-during-uncertainty-greater-social-connectedness"
title: "Resilience During Uncertainty? Greater Social Connectedness During COVID-19 Lockdown is Associated with Reduced Distress and Fatigue"
authors:
  - "Nitschke, Jonas P."
  - "Forbes, Paul"
  - "Ali, Nida"
  - "Cutler, Jo"
  - "Apps, Matthew A J"
  - "Lockwood, Patricia"
  - "Lamm, Claus"
year: 2020
doi: "10.31234/osf.io/9ehm7"
venue: {type: "preprint", name: null, volume: null, issue: null, pages: null}
citation: "Nitschke et al. (2020). Resilience During Uncertainty? Greater Social Connectedness During COVID-19 Lockdown is Associated with Reduced Distress and Fatigue.. https://doi.org/10.31234/osf.io/9ehm7"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  In a representative sample of 902 Austrian adults surveyed during the last week of a six-
  week COVID-19 lockdown, larger active social network size (Social Network Index) was
  consistently associated with lower perceived stress, general worry, COVID-19-specific
  worry, and fatigue. Mediation analyses showed that distress (stress, worry, COVID-19
  worry) statistically mediated the negative association between social network size and
  fatigue, suggesting social connectedness buffers against somatic strain during collective
  adversity partly by reducing distress. The study frames social connectedness (number of
  unique people contacted) as a resilience factor even when in-person contact is restricted
  and much of the interaction shifts online.
claims:
  - text: "Social network size (number of unique contacts in the prior two weeks) was negatively associated with perceived stress (b = -0.020, 95% CI [-0.029, -0.011], p < .001), general worry (b = -0.015, 95% CI [-0.024, -0.006], p < .001), and COVID-19-specific worry (b = -0.019, 95% CI [-0.028, -0.010], p < .001), controlling for age, gender, financial worries, and COVID-19 experience; models explained 9.5-13.3% of variance."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["social-support", "network-structure"]
  - text: "Fatigue (Chalder Fatigue Questionnaire) was negatively associated with social network size (b = -0.014, 95% CI [-0.024, -0.005], p = .002, R2 = .053), and this association was significantly mediated by all three distress measures (indirect effects: PSS b = -0.008, PSWQ b = -0.004, COVID-19 worry b = -0.007, all p <= .006), indicating distress partially explains why smaller networks were linked to greater fatigue."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["social-support", "network-structure"]
  - text: "During lockdown, participants had significantly more frequent online than in-person interactions (mean 3.18 vs 2.51 on a 7-point frequency scale, t(901) = -13.401, p < .001), and social network size was not significantly associated with perceived risk of contracting COVID-19 (p > .1), suggesting connectedness buffered distress specifically rather than shifting risk perception."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "communication"]
    predictors: ["social-support", "network-structure"]
population:
  who: "Representative community sample of Austrian adults aged 18-90 recruited via an election-forecasting online panel during nationwide COVID-19 lockdown"
  where: ["Austria"]
  when: "23-30 April 2020"
  n: 902
  sector: ["general-population"]
  sample_notes: >
    Started with 981 respondents; 902 retained after excluding those who failed an attention
    check or dropped out before it. Sample representative on age and gender; 61% held a
    higher-education degree (vocational or above); 55.6% women. Self-report survey
    administered in German via commercial panel, so representativeness depends on panel
    recruitment methodology.
limitation:
  primary: "Cross-sectional design collected only during lockdown with no pre-lockdown baseline, so directionality between social connectedness and distress/fatigue cannot be established (authors note the relationship is likely bidirectional)."
  others:
    - "COVID-19-specific worry items were ad hoc and not previously validated/piloted, though internal reliability was acceptable (alpha = .74)."
    - "No measure of perceived quality/support of social interactions was collected, only quantity of contacts, so mechanisms (support, belonging, diversity) cannot be disentangled."
    - "No clinical measures of anxiety or depression were obtained, limiting inference to short-term distress/fatigue rather than diagnosable mental health outcomes."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a large, representative, quantitative test of a specific SNH mechanism relevant
  to remote/distributed work under disruption: quantity of social contact (not just quality)
  predicts lower stress, worry, and fatigue, and distress mediates the network-size-to-
  fatigue pathway, informing why maintaining even non-collocated (largely online) contact
  volume could be a protective design lever during isolating conditions like lockdowns or
  fully remote arrangements.
tags:
  topic: ["isolation", "wellbeing", "mental-health", "social-support"]
  method: ["survey", "cross-sectional"]
  population: ["general-population"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Resilience During Uncertainty Greater Social Connectedness During COVID-19/Resilience During Uncertainty Greater Social Connectedness During COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Resilience During Uncertainty Greater Social Connectedness During COVID-19.pdf"
  notes: null

---

id: "baltes-2022-sampling-in-software-engineering-research-a"
title: "Sampling in software engineering research: a critical review and guidelines"
authors:
  - "Baltes, Sebastian"
  - "Ralph, Paul"
year: 2022
doi: "10.1007/s10664-021-10072-8"
venue: {type: "journal", name: "Empirical Software Engineering", volume: 27, issue: 4, pages: null}
citation: "Baltes et al. (2022). Sampling in software engineering research: a critical review and guidelines. Empirical Software Engineering, 27(4). https://doi.org/10.1007/s10664-021-10072-8"
article_type: "methods"
method: {design: "review-critical", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  A critical review of 120 top-venue software engineering papers (2014-2019) finds that
  purposive (73.0%) and convenience (11.3%) sampling dominate, while probability sampling
  appears in only 8.3% of the 210 coded sampling stages, and nearly a quarter of stages
  never explain how the sample was obtained. Baltes and Ralph diagnose this as a
  'generalizability crisis' rooted in the near-total absence of usable sampling frames for
  software engineering phenomena, and synthesize an extensive primer plus concrete
  guidelines for researchers and reviewers on describing, defending, and evaluating sampling
  honestly instead of overselling representativeness.
claims:
  - text: "Across 210 sampling stages coded from 120 full papers in ICSE, FSE, TSE and TOSEM (2014-2019), purposive sampling was used in 149 stages (73.0%) and convenience sampling in 23 (11.3%), while probability sampling (simple random or stratified random) accounted for only 17 stages (8.3%); 49 stages (24.0%) did not explain the sampling strategy at all."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
  - text: "Predominantly quantitative studies outnumbered predominantly qualitative studies 126 to 16 among the 144 studies analyzed, and code artifacts were the most common unit of observation (132 of 204 sampling stages, 64.7%) versus people (37, 18.1%) or non-code artifacts (33, 16.2%)."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
  - text: "86 of 120 articles offered some justification for sample quality, most commonly asserting the sample was 'real-world' (29 articles), 'large' (16), 'representative' (13), or 'diverse' (8), frequently without explaining the actual sampling procedure used to obtain it."
    evidence: "review-critical"
    support_strength: "moderate"
    outcomes: ["research-rigor"]
    predictors: ["sampling-method"]
population:
  who: "120 full research papers (144 reported studies, 210 sampling stages) drawn via stratified random sampling (5 papers per venue-year) from four A* software engineering venues; also the general population of software engineering researchers addressed by the guidelines."
  where: []
  when: "2014-2019"
  n: 120
  sector: ["academia"]
  sample_notes: >
    Sampling frame restricted to full technical-track papers in ICSE, FSE, TSE and TOSEM
    (1,830 papers); coding was manual, done primarily by the first author with second-author
    audit of ambiguous cases; results are explicitly stated to generalize only to high-
    quality, English-language SE research at these four venues, not to SE research
    generally.
limitation:
  primary: "The review's evidentiary base is limited to four top-tier venues (ICSE, FSE, TSE, TOSEM) over six years, so findings may not generalize to other outlets, workshops, older research, or future methodological trends."
  others:
    - "Coding of sampling technique, methodology, and units of observation required subjective interpretation, mitigated only by second-author audit of ambiguous cases rather than full independent double-coding."
    - "The authors explicitly frame this as a purposive 'critical review' rather than a systematic review, so it deliberately analyzes a sample of primary studies rather than the full population of SE research."
risk_of_bias: "medium"
relevance_to_project: >
  Because SNH draws heavily on software-engineering research about open-source maintainers
  and remote developer communities, this paper's finding that 92% of top-venue SE sampling
  stages are non-probability (purposive/convenience) and often unexplained gives the project
  a concrete basis for weighing the generalizability of OSS/maintainer-burnout studies cited
  elsewhere in the corpus, and its guidelines (state the sampling algorithm, avoid
  overselling representativeness, match sampling strategy to epistemology) are directly
  applicable if SNH conducts its own developer or maintainer sampling.
tags:
  topic: ["methodology", "measurement", "open-source"]
  method: ["review-critical", "secondary-data"]
  population: ["academia"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Sampling in Software Engineering Research A Critical Review and Guidelines/Sampling in Software Engineering Research A Critical Review and Guidelines.md"
  pdf: "papers/Academic/01 Academic - Extended/Sampling in Software Engineering Research A Critical Review and Guidelines.pdf"
  notes: null

---

id: "stajkovic-1998-self-efficacy-and-work-related-performance"
title: "Self-efficacy and work-related performance: A meta-analysis."
authors:
  - "Stajkovic, Alexander D."
  - "Luthans, Fred"
year: 1998
doi: "10.1037/0033-2909.124.2.240"
venue: {type: "journal", name: "Psychological Bulletin", volume: 124, issue: 2, pages: "240-261"}
citation: "Stajkovic et al. (1998). Self-efficacy and work-related performance: A meta-analysis.. Psychological Bulletin, 124(2), 240-261. https://doi.org/10.1037/0033-2909.124.2.240"
article_type: "review"
method: {design: "review-systematic", approach: "secondary-data", evidence_level: "strong", preregistered: false}
gist: >
  A meta-analysis of 114 studies (k = 157 correlations, N = 21,616) finds a significant
  weighted-average correlation of .38 between self-efficacy and work-related performance, a
  larger effect than commonly-cited organizational interventions such as goal-setting,
  feedback interventions, or behavior modification programs. The relationship is not
  uniform: it weakens substantially as task complexity rises and weakens further in actual
  field settings compared to simulated laboratory settings, falling to its lowest magnitude
  (G(r+) = .20) for complex tasks performed in real organizational environments.
claims:
  - text: "The primary meta-analysis found a significant weighted average correlation between self-efficacy and work-related performance of G(r+) = .38 (p < .01) after removing sample-size outliers, equivalent to an effect size of d = .82 and a 28% gain in performance -- larger than comparable meta-analytic effects for goal-setting (10.39%), feedback interventions (13.6%), or organizational behavior modification (17%)."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["performance", "productivity"]
    predictors: ["self-efficacy"]
  - text: "Task complexity significantly moderated the self-efficacy-performance relationship (Qb1 = 375.63, p < .01): correlations were strongest for low-complexity tasks (G(r+) = .53), weaker for medium-complexity tasks (.38), and weakest for high-complexity tasks (.24)."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["performance"]
    predictors: ["self-efficacy", "task-complexity"]
  - text: "Type of study setting further moderated the relationship at each level of task complexity (Qbii = 344.94, p < .01): the self-efficacy-performance correlation was strongest for low-complexity/laboratory settings (G(r+) = .50) and weakest for high-complexity/field settings (G(r+) = .20), with actual field settings consistently showing weaker correlations than simulated laboratory settings at every complexity level."
    evidence: "review-systematic"
    support_strength: "strong"
    outcomes: ["performance"]
    predictors: ["self-efficacy", "task-complexity", "study-setting"]
population:
  who: "114 primary studies (157 individual self-efficacy/performance correlations) drawn from organizational, laboratory, and educational research on adult and student task performers, pooled across the meta-analysis"
  where: []
  when: "1977-1996"
  n: 21616
  sector: ["general-workforce", "mixed-sector"]
  sample_notes: >
    Studies identified via computerized database searches (Business Periodicals Index,
    PsycLIT, Sociofile, Social Science Index, Expanded Academic Index, ERIC, Dissertation
    Abstracts) plus manual journal and reference-list searches, English-language only,
    1977-1996; of 2,099 candidate studies, 114 (5%) met all inclusion/exclusion criteria.
    Geographic origin of primary studies is not systematically reported by the authors,
    though journals cited are predominantly US/Western. Five extreme and four outlier
    sample-size studies were excluded from the adjusted analyses reported here.
limitation:
  primary: "The meta-analysis is entirely correlational, aggregating cross-sectional and lab correlations across heterogeneous primary studies; it cannot support causal claims, and the authors explicitly caution the .38 correlation should not be read as evidence of a causal effect of self-efficacy on performance."
  others:
    - "Task complexity was coded by only two raters using Wood's (1986) 'objective' taxonomy, a framework the authors acknowledge is not a field-wide consensus definition."
    - "Substantial residual heterogeneity remained within several moderator classes (laboratory-setting classes especially) even after removing sample-size and correlation-magnitude outliers, indicating unmeasured moderators."
    - "Literature search was limited to English-language, largely US/Western databases and journals from 1977-1996, limiting generalizability to non-English or more recent (e.g., remote/hybrid work era) contexts."
risk_of_bias: "low"
relevance_to_project: >
  Self-efficacy is a well-established predictor of work performance and is mechanistically
  linked to coping, burnout, and engagement under workload; this meta-analysis quantifies
  that link's strength and shows it degrades in naturalistic field settings and on complex,
  ambiguous tasks. That pattern is directly relevant to designing self-efficacy-supporting
  interventions (task clarity, timely feedback, achievable framing) for remote workers doing
  complex, unsupervised, low-feedback work, where the paper's own findings predict self-
  efficacy's protective effect on performance will be weakest.
tags:
  topic: ["productivity", "methodology", "measurement"]
  method: ["meta-analysis", "secondary-data"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Self-Efficacy and Work-Related Performance A Meta-Analysis/Self-Efficacy and Work-Related Performance A Meta-Analysis.md"
  pdf: "papers/Academic/01 Academic - Extended/Self-Efficacy and Work-Related Performance A Meta-Analysis.pdf"
  notes: null

---

id: "ahmad-2014-single-item-measures-of-self-rated"
title: "Single item measures of self-rated mental health: a scoping review"
authors:
  - "Ahmad, Farah"
  - "Jhajj, Anuroop K"
  - "Stewart, Donna E"
  - "Burghardt, Madeline"
  - "Bierman, Arlene S"
year: 2014
doi: "10.1186/1472-6963-14-398"
venue: {type: "journal", name: "BMC Health Services Research", volume: 14, issue: 1, pages: null}
citation: "Ahmad et al. (2014). Single item measures of self-rated mental health: a scoping review. BMC Health Services Research, 14(1). https://doi.org/10.1186/1472-6963-14-398"
article_type: "review"
method: {design: "review-scoping", approach: "analytical", evidence_level: "moderate", preregistered: false}
gist: >
  This scoping review of 57 studies is the first synthesis of the single-item self-rated
  mental health (SRMH) measure ('would you say your mental health is excellent...poor?'). It
  finds SRMH correlates only moderately with multi-item clinical mental health scales
  (r=0.33-0.49), varies by racial/ethnic group, and is consistently associated with poorer
  physical health, higher health-service utilization, and adverse social determinants such
  as low socioeconomic status and weak social support. The authors argue SRMH is a low-
  burden population health indicator but not a substitute for validated multi-item scales.
claims:
  - text: "In a prospective cohort, individuals with poor self-rated mental health were 4.57 times more likely to develop a major depressive episode within a year than those with fair SRMH, and 9.97 times more likely than those with excellent SRMH, controlling for age, gender, and depression history (Hoff et al. 1997)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["depression", "mental-health"]
    predictors: ["self-rated-mental-health"]
  - text: "Using nationally representative MEPS data, SRMH correlated moderately with multi-item mental health measures (r=0.33-0.49 with SF-12 mental subscales, K6 distress scale, and PHQ-2), notably weaker than the correlations among the multi-item scales themselves (r>.69), indicating SRMH is related to but not interchangeable with standardized scales."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health"]
    predictors: ["self-rated-mental-health"]
  - text: "Across 19 studies examining social determinants, poor or fair SRMH was consistently associated with low socioeconomic status, weaker family and social support, neighbourhood/environmental stressors, and weaker sense of community belonging; family cohesion had an independent direct effect on SRMH beyond other social-connection measures (Zhang & Ta 2009)."
    evidence: "review-scoping"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health"]
    predictors: ["social-support", "sense-of-belonging"]
population:
  who: "57 published studies (primary data collection and secondary analyses of population health surveys) using a single-item SRMH question, drawn from general-population, ethnic-minority, and clinical/service-user samples."
  where: ["United States", "Canada", "China", "Singapore", "England", "Nigeria", "Puerto Rico", "Sri Lanka", "Turkey", "Ukraine"]
  when: "Literature published 1980-2012; databases searched from inception to July 2012"
  n: 57
  sector: ["healthcare", "public-health-surveillance"]
  sample_notes: >
    Included-study sample sizes ranged from 121 to 120,559 participants; 26 US, 20 Canada,
    11 other countries. 51 of 57 included studies were cross-sectional and only 6
    prospective; most were secondary analyses of surveys such as CCHS, MEPS, and NLAAS
    rather than primary data collection, limiting causal/temporal inference.
limitation:
  primary: "SRMH terminology is not standardized in the literature, so the search strategy (even supplemented by known-survey and reference-list searches) may have missed relevant studies, and heterogeneity across included studies precluded formal meta-analysis or quality synthesis."
  others:
    - "Only 6 of 57 included studies were prospective, so most evidence on SRMH's relationships is correlational and cannot establish whether SRMH predicts future mental health problems."
    - "Search was restricted to English-language, published (non-grey) literature, likely undercounting non-Western and non-English uses of the item."
    - "Few studies (4 of 57) formally validated SRMH against clinical diagnostic measures, so its psychometric performance remains only partially characterized."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs whether the SNH project could use a single self-rated mental health item
  as a low-burden screening/outcome measure in remote-worker or community surveys: the
  evidence supports SRMH as a defensible brief proxy correlated with clinical scales and
  social determinants (support, belonging, socioeconomic stress), but the moderate (not
  strong) correlation and documented ethnic/racial response differences argue against using
  it as a stand-alone diagnostic substitute for validated multi-item mental health scales.
tags:
  topic: ["mental-health", "measurement", "methodology"]
  method: ["review-scoping"]
  population: ["general-population", "clinical-population"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Single Item Measures of Self-Rated Mental Health A Scoping Review/Single Item Measures of Self-Rated Mental Health A Scoping Review.md"
  pdf: "papers/Academic/01 Academic - Extended/Single Item Measures of Self-Rated Mental Health A Scoping Review.pdf"
  notes: null

---

id: "ipsen-2021-six-key-advantages-and-disadvantages-of"
title: "Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19"
authors:
  - "Ipsen, Christine"
  - "van Veldhoven, Marc"
  - "Kirchner, Kathrin"
  - "Hansen, John Paulin"
year: 2021
doi: "10.3390/ijerph18041826"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 18, issue: 4, pages: "1826"}
citation: "Ipsen et al. (2021). Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19. International Journal of Environmental Research and Public Health, 18(4), 1826. https://doi.org/10.3390/ijerph18041826"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A 29-country European survey of 5,748 knowledge workers taken during the first COVID-19
  lockdown (March-May 2020) used exploratory factor analysis to reduce 27
  advantage/disadvantage items into six underlying factors: three advantages (work-life
  balance, work efficiency, work control) and three disadvantages (home office constraints,
  work uncertainties, inadequate tools). Most respondents (55%) rated the WFH experience as
  net positive, but individual variance was large, and the factors differed significantly by
  gender, presence of children, age, and manager-vs-employee status. The paper proposes
  these six factors as a practical, validated-in-progress instrument organizations can use
  (e.g. via spider diagrams) to diagnose which levers to pull for wellbeing and performance
  when managing remote/hybrid work.
claims:
  - text: "Factor analysis of 27 WFH experience items yielded three advantage factors (work-life balance, work efficiency, work control; explaining 49% of variance) and three disadvantage factors (home office constraints, work uncertainties, inadequate tools; explaining 47% of variance), replicated on a held-out half-sample with the same factor structure."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "wellbeing", "work-life-balance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "The majority of respondents (55%) rated their WFH experience during early lockdown as predominantly positive rather than negative, though scores showed considerable individual variance around the midpoint, indicating the experience was more individual than uniform across knowledge workers."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["wellbeing", "job-satisfaction"]
    predictors: ["remote-work-intensity"]
  - text: "The six factors varied significantly by demographic and role group with medium-to-large effect sizes: women reported more home-office constraints and less work efficiency than men (Cohen's d ~0.76-0.91, p<.01); workers with children at home reported lower work efficiency and more home-office constraints than those without (Cohen's d ~0.76-0.90, p<.01); and employees rated work-life balance and efficiency more positively than managers, who reported fewer work uncertainties (p<.01, medium-to-high effect sizes)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["remote-work-intensity", "workload"]
population:
  who: "5,748 professional and managerial ('knowledge') workers across 29 European countries, recruited via non-probability snowball sampling during the first COVID-19 lockdown"
  where: ["Denmark", "Germany", "Italy", "Sweden", "Austria", "Netherlands", "Spain", "United Kingdom", "other European countries"]
  when: "11 March to 11 May 2020"
  n: 5748
  sector: ["knowledge-work", "mixed-professional"]
  sample_notes: >
    Non-probabilistic snowball sample recruited via social media and professional/academic
    networks; skewed toward knowledge workers with high education (75.2% held a university
    degree), 59.2% women, 23% managers; authors explicitly flag sample bias toward people
    connected to the research team's academic/industry networks, limiting generalizability
    beyond knowledge work.
limitation:
  primary: "Non-probability snowball sampling collected during an acute crisis period introduces selection bias and limits generalizability to knowledge workers with characteristics similar to the sample, not the broader workforce."
  others:
    - "The six-factor scales were validated only with exploratory factor analysis and internal consistency (not confirmatory factor analysis); several advantage subscales had marginal reliability (Cronbach's alpha 0.53-0.61)."
    - "Cross-sectional design captured only the earliest weeks of forced lockdown WFH, so findings may not generalize to sustained or voluntary hybrid/remote arrangements post-pandemic."
    - "The study did not examine how the six factors relate to downstream wellbeing or performance outcomes over time, leaving causal and longitudinal questions unaddressed."
risk_of_bias: "medium"
relevance_to_project: >
  Offers the SNH project a compact, empirically-derived six-factor taxonomy (work-life
  balance, efficiency, control vs. home-office constraints, work uncertainties, inadequate
  tools) for diagnosing and measuring remote-worker experience, plus evidence that
  demographic subgroups (gender, parenthood, manager status) require differentiated
  organizational support rather than one-size-fits-all remote-work policy.
tags:
  topic: ["remote-work", "wellbeing", "work-life-balance", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "european-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19/Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Six Key Advantages and Disadvantages of Working from Home in Europe during COVID-19.pdf"
  notes: null

---

id: "steinfield-2008-social-capital-self-esteem-and-use"
title: "Social capital, self-esteem, and use of online social network sites: A longitudinal analysis"
authors:
  - "Steinfield, Charles"
  - "Ellison, Nicole B."
  - "Lampe, Cliff"
year: 2008
doi: "10.1016/j.appdev.2008.07.002"
venue: {type: "journal", name: "Journal of Applied Developmental Psychology", volume: 29, issue: 6, pages: "434-445"}
citation: "Steinfield et al. (2008). Social capital, self-esteem, and use of online social network sites: A longitudinal analysis. Journal of Applied Developmental Psychology, 29(6), 434-445. https://doi.org/10.1016/j.appdev.2008.07.002"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  A one-year panel study of Facebook users at a large U.S. university finds that Facebook
  Intensity in year one strongly predicts bridging social capital in year two, even after
  controlling for general Internet use, self-esteem, and satisfaction with life. Cross-
  lagged correlation and lagged regression analyses support a causal direction running from
  platform use to social capital rather than the reverse, and self-esteem moderates the
  relationship: students with lower self-esteem gain more bridging social capital from
  Facebook use than those with higher self-esteem. The authors argue Facebook's affordances
  (lightweight messaging, visible latent-tie information, low-friction contact) lower the
  barriers that especially affect lower-self-esteem users trying to build large,
  heterogeneous weak-tie networks.
claims:
  - text: "Facebook Intensity measured in year one was a highly significant predictor of bridging social capital in year two (scaled beta = .42, p < .0001), even after controlling for general Internet use, self-esteem, and satisfaction with university life; general Internet use itself showed no relationship to later bridging social capital (scaled beta = .06, ns)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["social-capital", "sense-of-belonging"]
    predictors: ["social-network-site-use", "loneliness"]
  - text: "Self-esteem moderated the Facebook-use to bridging-social-capital link: the self-esteem by Facebook-Intensity interaction significantly predicted bridging social capital (scaled beta = -.46, p < .05), and in cross-lagged correlation sub-sample analyses the lagged Facebook-use/bridging-social-capital correlation was stronger for lower self-esteem students (r = .57) than higher self-esteem students (r = .43)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["social-capital"]
    predictors: ["social-network-site-use", "self-esteem"]
  - text: "A cross-lagged correlation analysis with a modified Pearson-Filon (ZPF) significance test found Facebook use at time 1 more strongly associated with bridging social capital at time 2 than the reverse lagged path (z = 3.52, p < .001), supporting directionality from platform use to social capital gains rather than pre-existing social capital driving platform use."
    evidence: "longitudinal"
    support_strength: "low-to-moderate"
    outcomes: ["social-capital"]
    predictors: ["social-network-site-use"]
population:
  who: "Undergraduate students at a large Midwestern U.S. university (Michigan State) who completed Facebook/social-capital surveys in both April 2006 and April 2007, forming a 92-person longitudinal panel; supplemented by 18 in-depth interviews with students from the 2006 sample."
  where: ["United States"]
  when: "2006-2007"
  n: 92
  sector: ["higher-education"]
  sample_notes: >
    2006: random sample of 800 undergraduates invited by email, 286 completed (35.8%
    response). 2007: a new random sample of 1987 invited (477 completed, 24% response) plus
    the 277 prior 2006 respondents re-invited, of whom 92 (33%) responded and formed the
    panel used for the lagged/causal analyses. Panel demographics did not differ
    substantially from the broader samples, but the overall sample over-represented female,
    younger, in-state, and on-campus students relative to the full undergraduate population;
    non-responder demographics were unavailable, so response bias cannot be ruled out.
limitation:
  primary: "Causal claims rest on a non-experimental panel design (no random assignment or experimental control of Facebook use), so despite supportive cross-lagged and lagged-regression results the authors themselves note true causality cannot be established."
  others:
    - "The panel used for longitudinal/causal analyses is small (n = 92) and self-selected from those willing to be re-surveyed and located a year later, limiting precision and generalizability."
    - "Only one platform (Facebook) at a single university was studied, and measurement of Facebook minutes/friends changed from ordinal categories in 2006 to direct estimates in 2007, requiring approximate conversions across waves."
    - "Self-esteem variance in the sample was compressed (median 4.29 on a 5-point scale), weakening the power of the self-esteem moderation test."
risk_of_bias: "medium"
relevance_to_project: >
  This is a foundational panel study linking social-platform-use intensity to bridging
  social capital and showing self-esteem as a moderator (bigger gains for lower-self-esteem
  users), which directly informs SNH hypotheses about whether lightweight, low-friction
  connection tools disproportionately help socially anxious or isolated remote workers, and
  it models a cross-lagged/panel design SNH could reuse to test directionality between tool
  engagement and social outcomes rather than relying on cross-sectional correlations.
tags:
  topic: ["social-support", "wellbeing", "community-health", "measurement", "methodology"]
  method: ["longitudinal", "survey", "mixed-methods"]
  population: ["college-students", "young-adults"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Social Capital Self-Esteem and Use of Online Social Network Sites A Longitudinal Analysis/Social Capital Self-Esteem and Use of Online Social Network Sites A Longitudinal Analysis.md"
  pdf: "papers/Academic/01 Academic - Extended/Social Capital Self-Esteem and Use of Online Social Network Sites A Longitudinal Analysis.pdf"
  notes: null

---

id: "toscano-2020-social-isolation-and-stress-as-predictors"
title: "Social Isolation and Stress as Predictors of Productivity Perception and Remote Work Satisfaction during the COVID-19 Pandemic: The Role of Concern about the Virus in a Moderated Double Mediation"
authors:
  - "Toscano, Ferdinando"
  - "Zappalà, Salvatore"
year: 2020
doi: "10.3390/su12239804"
venue: {type: "journal", name: "Sustainability", volume: 12, issue: 23, pages: "9804"}
citation: "Toscano et al. (2020). Social Isolation and Stress as Predictors of Productivity Perception and Remote Work Satisfaction during the COVID-19 Pandemic: The Role of Concern about the Virus in a Moderated Double Mediation. Sustainability, 12(23), 9804. https://doi.org/10.3390/su12239804"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  In a survey of 265 Italian employees forced into full-time remote work during the March-
  May 2020 lockdown, social isolation was positively associated with stress (B=0.59), which
  in turn reduced perceived remote work productivity and, sequentially, remote work
  satisfaction. Concern about COVID-19 moderated two of the paths: the isolation-
  satisfaction link was stronger among more worried employees, while the productivity-
  satisfaction link was weaker among them, suggesting worry consumes cognitive resources
  that otherwise translate performance perceptions into satisfaction. The study extends the
  JD-R model's health-impairment path to remote work, framing isolation as a job demand with
  both direct and mediated costs.
claims:
  - text: "Social isolation was significantly and positively related to stress (B=0.59, p<0.01), and both social isolation (B=-0.38, p<0.01) and stress (B=-0.17, p<0.01) were negatively related to perceived remote work productivity."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "productivity"]
    predictors: ["isolation"]
  - text: "Social isolation had a significant direct negative effect on remote work satisfaction (B=-0.18, p<0.01), and this effect was also transmitted indirectly through stress alone, through perceived productivity alone, and through a sequential path via both stress and productivity (all indirect effects significant, e.g. isolation->stress->satisfaction B=-0.15)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction", "isolation"]
    predictors: ["isolation", "technostress"]
  - text: "Concern about COVID-19 moderated two relationships: it strengthened the negative link between social isolation and remote work satisfaction (B=-0.19, p<0.01), while it weakened the positive link between perceived productivity and remote work satisfaction (B=-0.14, p<0.01) — employees low in isolation but high in virus concern, and employees high in isolation but low in concern, both reported relatively higher satisfaction."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["job-satisfaction"]
    predictors: ["isolation", "technostress"]
population:
  who: "Italian employees suddenly shifted to full-time remote work during the COVID-19 lockdown (March-May 2020), recruited via social networks and an instant messaging app"
  where: ["Italy"]
  when: "April-May 2020"
  n: 265
  sector: ["mixed", "public-and-private"]
  sample_notes: >
    Convenience sample; 354 responses collected, 265 retained after excluding non-remote-
    workers and incomplete surveys (high dropout). Skewed young (42.3% aged 26-35) and
    highly educated (59.2% Master's degree, 12.1% PhD), 37% male, 80.4% third-sector
    employees; not representative of the general remote-work population. Perceived
    productivity and COVID-19 concern each measured with only 1-2 items.
limitation:
  primary: "Cross-sectional design precludes causal inference; the mediation model's directionality (e.g., isolation causing stress, productivity causing satisfaction) cannot be verified and alternative causal orderings remain plausible."
  others:
    - "Convenience sample recruited via social media/messaging apps is skewed young, well-educated, and not representative of the broader remote-workforce population."
    - "Perceived remote work productivity was measured with a single item and COVID-19 concern with only two items, both non-standard, single-study-developed measures."
    - "High attrition (265 of 354 initial respondents) may introduce non-response bias."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a quantified JD-R-model pathway (isolation -> stress -> perceived productivity ->
  satisfaction) with effect sizes directly usable for prioritizing SNH interventions that
  target perceived social isolation in remote workers, and shows that ambient anxiety/worry
  (here, pandemic concern) can amplify isolation's harm to satisfaction — relevant to
  designing supportive social touchpoints (video calls, social coffee breaks, peer support
  channels) during high-stress periods.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "job-satisfaction", "technostress"]
  method: ["survey", "cross-sectional"]
  population: ["knowledge-workers", "italy", "covid-19-lockdown"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Social Isolation and Stress as Predictors of Productivity Perception and Remote Work Satisfaction during COVID-19/Social Isolation and Stress as Predictors of Productivity Perception and Remote Work Satisfaction during COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Social Isolation and Stress as Predictors of Productivity Perception and Remote Work Satisfaction during COVID-19.pdf"
  notes: null

---

id: "perry-2018-stress-in-remote-work-two-studies"
title: "Stress in remote work: two studies testing the Demand-Control-Person model"
authors:
  - "Perry, Sara Jansen"
  - "Rubino, Cristina"
  - "Hunter, Emily M."
year: 2018
doi: "10.1080/1359432x.2018.1487402"
venue: {type: "journal", name: "European Journal of Work and Organizational Psychology", volume: 27, issue: 5, pages: "577-593"}
citation: "Perry et al. (2018). Stress in remote work: two studies testing the Demand-Control-Person model. European Journal of Work and Organizational Psychology, 27(5), 577-593. https://doi.org/10.1080/1359432x.2018.1487402"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Across two field surveys, autonomy alone was an inconsistent buffer against remote-work
  strain, but the combination of high job autonomy and high emotional stability was the
  strongest protective condition: these employees reported the lowest exhaustion,
  disengagement, and dissatisfaction, and this advantage held or strengthened as the extent
  of remote work increased. Mediation tests showed that autonomy and relatedness need
  satisfaction (from self-determination theory) explain much of this pattern, fully
  mediating effects on exhaustion and disengagement. Employees low in both autonomy and
  emotional stability were consistently the most strained, regardless of how much they
  worked remotely.
claims:
  - text: "Study 1 (N=258, two-wave field survey): the remote work × autonomy × emotional stability three-way interaction significantly predicted disengagement and dissatisfaction (but not exhaustion); the high-autonomy/high-emotional-stability group had the lowest strain of all four conditions across all three strain outcomes, with a significant negative disengagement slope (b=-0.54, p<.05) as remote work increased."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction", "stress"]
    predictors: ["autonomy", "emotional-stability", "remote-work-intensity"]
  - text: "Study 2 (N=145, three organizations): the three-way interaction again significantly predicted disengagement (pseudo R2=.27) and dissatisfaction (pseudo R2=.20), and the two-way remote work × autonomy interaction significantly predicted exhaustion (b=-0.22, p<.05), with a positive remote work-exhaustion slope (0.82, p<.05) among employees reporting low autonomy."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction", "stress"]
    predictors: ["autonomy", "emotional-stability", "remote-work-intensity"]
  - text: "Autonomy and relatedness need-satisfaction (SDT) significantly mediated the three-way interaction's effect on exhaustion and disengagement (full mediation, indirect effects p<.01), whereas the effect on dissatisfaction was only partially mediated by autonomy need satisfaction, with a remaining significant direct effect (A×B×C on dissatisfaction: b=-2.24, p<.01)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "job-satisfaction", "sense-of-belonging"]
    predictors: ["autonomy", "sense-of-belonging", "emotional-stability"]
population:
  who: "Full-time working adults in two U.S. field samples: Study 1 = 258 employees recruited via an online panel (MarketTools Zoomerang), mixed industries; Study 2 = 145 employees from three southern U.S. organizations (an engineering firm, a technology firm, and a local government agency), including HR staff, engineers/technology architects, admin support, and line managers."
  where: ["United States"]
  when: null
  n: 403
  sector: ["general-workforce", "engineering", "technology", "government"]
  sample_notes: >
    Study 1: two-wave design (predictors at Time 1, strain at Time 2, 3 months apart),
    online panel, no ethnicity data collected. Study 2: single-timepoint online survey, 23%
    response rate, employees clustered in 51 workgroups (multilevel/random-intercept models
    used). Authors explicitly state neither study is truly longitudinal, precluding causal
    claims.
limitation:
  primary: "Both studies rely entirely on self-report measures and neither is a true longitudinal or experimental design (Study 2 is single-timepoint; Study 1 has only a 3-month time lag between predictors and outcomes), so causal direction between autonomy/emotional stability and strain cannot be established."
  others:
    - "Extent of remote work was relatively low/skewed toward traditional office-based work in both samples, limiting statistical power at high remote-work intensities."
    - "Study 2 used a convenience sample from three organizations with a 23% response rate, limiting generalizability."
    - "Only emotional stability was examined in depth as the personality moderator; other traits (extraversion, conscientiousness, openness) were explored only in post hoc supplementary analyses."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH design question of which remote workers most need social-
  connection or support interventions: it identifies emotional stability as a moderator of
  whether job autonomy actually protects against strain, and shows that relatedness need
  satisfaction (not just autonomy) is a key mediating mechanism linking remote-work
  intensity to exhaustion, disengagement, and dissatisfaction — suggesting relatedness-
  building supports may matter most for lower-emotional-stability remote employees.
tags:
  topic: ["remote-work", "burnout", "wellbeing", "job-satisfaction", "job-engagement"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "full-time-employees", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Stress in remote work  two studies testing the Demand-Control-Person model/Stress in remote work  two studies testing the Demand-Control-Person model.md"
  pdf: "papers/Academic/01 Academic - Extended/Stress in remote work  two studies testing the Demand-Control-Person model.pdf"
  notes: null

---

id: "chong-2020-supporting-interdependent-telework-employees-a-moderated"
title: "Supporting interdependent telework employees: A moderated-mediation model linking daily COVID-19 task setbacks to next-day work withdrawal."
authors:
  - "Chong, SinHui"
  - "Huang, Yi"
  - "Chang, Chu-Hsiang (Daisy)"
year: 2020
doi: "10.1037/apl0000843"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 105, issue: 12, pages: "1408-1422"}
citation: "Chong et al. (2020). Supporting interdependent telework employees: A moderated-mediation model linking daily COVID-19 task setbacks to next-day work withdrawal.. Journal of Applied Psychology, 105(12), 1408-1422. https://doi.org/10.1037/apl0000843"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using 10-day experience-sampling data from 120 full-time telework employees during
  Singapore's COVID-19 lockdown (1,022 daily observations), this study tests a two-stage
  moderated-mediation model grounded in conservation of resources theory: daily COVID-19
  task setbacks predicted end-of-day emotional exhaustion, which in turn was hypothesized to
  predict next-day work withdrawal. Exhaustion effects on withdrawal were only significant
  for employees with higher task interdependence and low organizational telework task
  support, showing that organizational support for teleworkers can buffer the exhaustion-to-
  withdrawal pathway even though the direct exhaustion-withdrawal link was not significant
  overall.
claims:
  - text: "Daily COVID-19 task setbacks were positively related to end-of-day emotional exhaustion (gamma = .18, SE = .06, p = .00), and this relationship was significantly stronger for employees with higher (vs. lower) task interdependence with coworkers (gamma = .17, SE = .07, p = .02)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["team-cohesion", "workload"]
  - text: "The direct relationship between end-of-day exhaustion and next-day work withdrawal behavior was not significant overall (gamma = .02, SE = .02, p = .33), but was significantly moderated by organizational telework task support (gamma = -.05, SE = .02, p = .03): the exhaustion-withdrawal link was positive and significant for employees who perceived lower organizational support, and non-significant for those with higher perceived support."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["turnover", "job-engagement"]
    predictors: ["social-support", "organizational-culture"]
  - text: "The full conditional indirect effect (task setbacks to withdrawal via exhaustion) was strongest and only significant for employees with both higher task interdependence and lower organizational telework support (95% CI [.001, .042]); the difference between this subgroup and the opposite subgroup (lower interdependence, higher support) was also significant (95% CI [.002, .043]), supporting the full moderated-mediation model."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["turnover", "burnout"]
    predictors: ["social-support", "team-cohesion"]
population:
  who: "Full-time telework employees in Singapore during the country's mandatory 8-week COVID-19 lockdown, recruited via snowball sampling across diverse industries (civil service, law/research, finance, education)"
  where: ["Singapore"]
  when: "surveys administered during weeks 5-7 of Singapore's April-June 2020 lockdown"
  n: 120
  sector: ["public-sector", "professional-services", "finance", "education"]
  sample_notes: >
    Recruited via snowball sampling starting from the first author's social media and 20
    personal/professional contacts; 228 responded to eligibility screening, 128 completed
    baseline, and after exclusions for missing lagged daily data the final analytic sample
    was 120 participants providing 1,022 of 1,197 possible daily responses (93.5% response
    rate on completed surveys). Sample skewed 65.8% female and 97.5% ethnic Chinese,
    limiting generalizability.
limitation:
  primary: "Task interdependence and organizational telework task support were both measured only once at baseline (between-person), so the study cannot rule out unmeasured company/industry-level telework readiness as a confound, and it does not identify which specific support strategies (IT support, decision authority, information) drive the buffering effect."
  others:
    - "The direct end-of-day-exhaustion to next-day-withdrawal path (H3) was not statistically supported, weakening the core mediation logic of the model even though moderated paths were significant."
    - "Sample is demographically narrow (65.8% female, 97.5% ethnic Chinese, all Singapore-based) and does not control for home resources (internet connectivity, workspace quality) that plausibly affect telework strain."
    - "Authors themselves caution that the eight-variable, two-stage moderated-mediation model is complex, which past methodological critiques (Saylors & Trafimow, 2020) suggest lowers the likelihood that the full causal chain is correct without further experimental unpacking."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH question of what organizational-level supports buffer
  remote/telework strain: it provides quantitative evidence that perceived organizational
  telework task support (not team-level social contact per se) moderates whether daily
  exhaustion converts into work withdrawal, and that task-interdependent teleworkers are the
  highest-risk subgroup needing that support during disruptive periods.
tags:
  topic: ["remote-work", "burnout", "wellbeing", "job-engagement"]
  method: ["experience-sampling", "multilevel-modeling"]
  population: ["telework-employees", "covid-19-lockdown"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Supporting Interdependent Telework Employees A Moderated-Mediation Model Linking Daily COVID-19 Task Setbacks to Next-Day Work Withdrawal/Supporting Interdependent Telework Employees A Moderated-Mediation Model Linking Daily COVID-19 Task Setbacks to Next-Day Work Withdrawal.md"
  pdf: "papers/Academic/01 Academic - Extended/Supporting Interdependent Telework Employees A Moderated-Mediation Model Linking Daily COVID-19 Task Setbacks to Next-Day Work Withdrawal.pdf"
  notes: null

---

id: "cunnison-1998-talking-about-machines-an-ethnography-of"
title: "Talking About Machines: An Ethnography of a Modern Job."
authors:
  - "Cunnison, Sheila"
  - "Orr, Julian E."
year: 1998
doi: "10.2307/3034516"
venue: {type: "journal", name: "The Journal of the Royal Anthropological Institute", volume: 4, issue: 2, pages: "360"}
citation: "Cunnison et al. (1998). Talking About Machines: An Ethnography of a Modern Job.. The Journal of the Royal Anthropological Institute, 4(2), 360. https://doi.org/10.2307/3034516"
article_type: "commentary"
method: {design: "qualitative", approach: "ethnography", evidence_level: "low", preregistered: false}
gist: >
  This is a brief scholarly book review (Journal of the Royal Anthropological Institute,
  1998) of Julian Orr's ethnography 'Talking About Machines,' which studied photocopier
  repair technicians and found they built a strong occupational community with fellow
  technicians rather than with their employer, despite having no formal career ladder.
  Storytelling about diagnostic encounters served both as the primary means of sharing
  practical knowledge and as a social bonding and status ritual among technicians. The
  review notes that expertise emerged mainly through experiential learning and peer exchange
  rather than formal service manuals, under conditions of daily uncertainty and
  unpredictable machine faults. For SNH, it is a useful historical case of an informal, non-
  hierarchical community of practice sustaining both technical competence and social
  identity among dispersed, individually-working employees.
claims:
  - text: "Photocopier technicians identified not with their employer but with an 'occupational community' of fellow technicians, a close-knit trade-based culture that persisted despite the absence of a formal career ladder."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["sense-of-belonging", "communication"]
    predictors: ["community-engagement", "peer-mentoring"]
  - text: "Storytelling among technicians was not merely social talk but an integral part of the work process itself, functioning as the main channel for sharing diagnostic knowledge about unpredictable machine faults while also celebrating success, enabling competition, and conferring 'heroic' status within the group."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["collaboration", "communication"]
    predictors: ["peer-mentoring", "community-engagement"]
  - text: "Diagnostic expertise was built primarily through experiential learning and informal peer knowledge exchange rather than through formal service manuals, reflecting a triangular technician-customer-machine relationship under conditions of daily uncertainty."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["performance", "collaboration"]
    predictors: ["peer-mentoring", "autonomy"]
population:
  who: "Field technicians who repaired leased photocopiers for customer companies, studied via participant-observation ethnography for Julian Orr's doctoral dissertation research."
  where: []
  when: "study conducted prior to 1990 (dissertation completed 1990)"
  n: null
  sector: ["technical-services"]
  sample_notes: >
    This document is itself a ~1-page book review, not the primary ethnography, so sample
    size, exact field site, and study duration are not reported; population details are
    limited to what the reviewer summarizes about Orr's fieldwork.
limitation:
  primary: "This is a secondhand account (a short book review) of Orr's ethnography rather than the original text, so methodological detail such as sample size, site, duration, and analytic method is compressed or omitted entirely."
  others:
    - "Underlying findings rest on a single-site, single-occupation case study, limiting generalizability to other occupational communities."
    - "The review offers evaluative commentary rather than independent verification of Orr's claims."
risk_of_bias: "unclear"
relevance_to_project: >
  Illustrates how a distributed, non-managerial occupational community (photocopier repair
  technicians) sustained cohesion and diagnostic knowledge-sharing through storytelling
  rather than formal hierarchical structures or manuals — a useful historical analogue for
  how open-source maintainers and remote workers might build informal peer support and
  troubleshooting knowledge outside official channels.
tags:
  topic: ["community-health", "collaboration", "social-support"]
  method: ["qualitative", "case-study"]
  population: ["field-technicians", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Talking About Machines A Review by Sheila Cunnison/Talking About Machines A Review by Sheila Cunnison.md"
  pdf: "papers/Academic/01 Academic - Extended/Talking About Machines A Review by Sheila Cunnison.pdf"
  notes: null

---

id: "consiglio-2023-techno-stress-creators-burnout-and-psychological"
title: "Techno-Stress Creators, Burnout and Psychological Health among Remote Workers during the Pandemic: The Moderating Role of E-Work Self-Efficacy"
authors:
  - "Consiglio, Chiara"
  - "Massa, Nicoletta"
  - "Sommovigo, Valentina"
  - "Fusco, Luigi"
year: 2023
doi: "10.3390/ijerph20227051"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 20, issue: 22, pages: "7051"}
citation: "Consiglio et al. (2023). Techno-Stress Creators, Burnout and Psychological Health among Remote Workers during the Pandemic: The Moderating Role of E-Work Self-Efficacy. International Journal of Environmental Research and Public Health, 20(22), 7051. https://doi.org/10.3390/ijerph20227051"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  In a survey of 225 Italian remote workers during the COVID-19 pandemic, structural
  equation modeling showed that burnout (measured with the Burnout Assessment Tool) fully
  mediated the link between techno-stressors and depressive mood and partially mediated the
  link between techno-stressors and anxiety symptoms. E-work self-efficacy buffered these
  effects: workers with high e-work self-efficacy showed no significant indirect burnout-
  mediated increase in depressive mood or anxiety when facing techno-stressors, while a
  competing model showed general resilience did not have this protective moderating effect.
  The study frames techno-stressors (overload, invasion, complexity) as job demands that
  deplete psychological resources under Conservation of Resources theory.
claims:
  - text: "Techno-stressors were positively related to burnout (r = 0.43, p < 0.01); burnout in turn totally mediated the relationship between techno-stressors and depressive mood (indirect effect beta = 0.21, p < 0.01, 95% CI [0.12, 0.33]) and partially mediated the relationship between techno-stressors and anxiety symptoms (indirect effect beta = 0.11, p < 0.05, 95% CI [0.05, 0.18])."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "depression", "anxiety"]
    predictors: ["technostress", "workload"]
  - text: "E-work self-efficacy significantly moderated the techno-stressor-to-burnout path (interaction beta = -0.15, p < 0.01, 95% CI [-0.24, -0.06]): remote workers with high e-work self-efficacy showed a non-significant indirect effect of techno-stressors on depressive mood (beta = 0.05, ns) and anxiety (beta = 0.02, ns) via burnout, whereas those with low or moderate e-work self-efficacy showed significant indirect effects."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "depression", "anxiety"]
    predictors: ["technostress", "self-efficacy"]
  - text: "A competing moderated-mediation model using general resilience instead of e-work self-efficacy fit worse (AIC = 13,651.74, BIC = 14,065.09 vs. 13,485.92/13,899.27) and the resilience-by-techno-stressor interaction on burnout was not statistically significant (beta = -0.07, ns, 95% CI [-0.15, 0.01]), indicating domain-specific self-efficacy is a stronger protective resource than general resilience for remote workers facing techno-stressors."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout"]
    predictors: ["self-efficacy", "technostress"]
population:
  who: "Remote workers in Italy recruited via an anonymous online Qualtrics survey distributed on LinkedIn and personal contacts; final analytic sample of 225 (from 349 respondents, 124 excluded for incomplete responses)"
  where: ["Italy"]
  when: "June-October 2020 (COVID-19 pandemic)"
  n: 225
  sector: ["mixed/unspecified"]
  sample_notes: >
    Non-probability convenience sample skewed toward women (60%) and ages 26-35 (35.6%);
    32.9% office workers, 28.4% highly specialized professionals; 56.4% had permanent
    contracts; authors note possible healthy-worker effect (burned-out or unable-to-work
    individuals underrepresented) and limited representativeness of the broader Italian
    remote-working population.
limitation:
  primary: "Cross-sectional, self-report design precludes causal inference about the techno-stressor -> burnout -> mental health pathway, despite a reverse-mediation model fitting worse and a common-method-bias check being reassuring."
  others:
    - "Small, non-probability convenience sample (n=225) recruited via social media, limiting generalizability to the broader Italian or international remote-working population."
    - "E-work self-efficacy was measured with an adapted 5-item scale rather than a validated multidimensional instrument developed later."
    - "Prior mental health status was not controlled for, so baseline vulnerability could confound the observed associations between techno-stressors and psychological symptoms."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a quantified mechanism (burnout as mediator) and a specific, trainable protective
  factor (e-work self-efficacy, distinct from general resilience) for reducing
  depression/anxiety risk among remote workers exposed to technology-driven job demands --
  directly informing SNH intervention design around digital-competence training versus
  generic resilience-building programs.
tags:
  topic: ["remote-work", "technostress", "burnout", "mental-health", "wellbeing"]
  method: ["cross-sectional", "survey", "sem"]
  population: ["remote-workers", "italy", "pandemic-era"]
source:
  markdown: "Papers_Data/Academic/MD/Techno-Stress Creators, Burnout and Psychological Health among Remote Workers during the Pandemic- The Moderating Role of E-Work Self-Efficacy/Techno-Stress Creators, Burnout and Psychological Health among Remote Workers during the Pandemic- The Moderating Role of E-Work Self-Efficacy.md"
  pdf: "papers/Academic/Techno-Stress Creators, Burnout and Psychological Health among Remote Workers during the Pandemic- The Moderating Role of E-Work Self-Efficacy.pdf"
  notes: null

---

id: "ayyagari-2011-technostress-technological-antecedents-and-implications1"
title: "Technostress: Technological Antecedents and Implications1"
authors:
  - "Ayyagari, Ramakrishna"
  - "Grover, Varun"
  - "Purvis, Russell"
year: 2011
doi: "10.2307/41409963"
venue: {type: "journal", name: "MIS Quarterly", volume: 35, issue: 4, pages: "831-A10"}
citation: "Ayyagari et al. (2011). Technostress: Technological Antecedents and Implications1. MIS Quarterly, 35(4), 831-A10. https://doi.org/10.2307/41409963"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This study builds and tests a person-technology (P-T) fit model of technostress using
  structural equation modeling on field survey data from 661 full-time working
  professionals, showing that ICT characteristics -- especially presenteeism (constant
  reachability) and pace of technological change -- drive discrete workplace stressors (work
  overload, role ambiguity, work-home conflict, job insecurity, invasion of privacy), which
  in turn predict psychological strain. It reframes technostress from a monolithic 'black
  box' phenomenon into specific, actionable technology characteristics that organizations
  can diagnose and target with interventions.
claims:
  - text: "Technology presenteeism (the degree to which ICTs make individuals constantly reachable) was the strongest and most consistent antecedent of ICT-related stressors, significantly increasing role ambiguity (beta=0.61), work overload (beta=0.61), work-home conflict (beta=0.52), and invasion of privacy (beta=0.32), all p<0.01."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "work-life-balance"]
    predictors: ["technostress", "boundary-management"]
  - text: "Role ambiguity (beta=0.27) and work overload (beta=0.26) due to ICTs were the strongest predictors of psychological strain, together with work-home conflict (beta=0.17) and job insecurity (beta=0.10) explaining about 35% of variance in strain, while invasion of privacy was not significantly related to strain (beta=0.027, p>0.05)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["workload", "technostress"]
  - text: "Technology pace of change significantly predicted three stressors -- work overload (beta=0.14), role ambiguity (beta=0.23), and job insecurity (beta=0.14, explaining only 2% of its variance) -- whereas perceived technology complexity did not significantly predict work overload (beta=0.07, p>0.05), contrary to the hypothesized effect."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress"]
    predictors: ["technostress", "workload"]
population:
  who: "661 full-time working U.S. business users of ICTs across many industries (692 passed screening, 31 removed as invalid/outliers), recruited from a Zoomerang commercial online panel"
  where: ["United States"]
  when: null
  n: 661
  sector: ["general-workforce"]
  sample_notes: >
    Not occupation-specific: top industries were education (16.9%), healthcare (10.6%),
    government (9.3%), finance (7.1%), retail (6%), and manufacturing (5.7%). Average age
    49, 27.3 years work experience, 14.5 years ICT experience, 48% female. Recruited via an
    online panel screened for full-time employment and ICT use, so likely skews toward more
    experienced, digitally engaged workers rather than a random population sample.
limitation:
  primary: "Cross-sectional, single-source self-report survey design measuring perceived (direct) person-technology misfit rather than objective technology use or longitudinal change, so causal direction among technology characteristics, stressors, and strain cannot be firmly established."
  others:
    - "Measures used generic ICTs rather than any single technology, which the authors note likely produces conservative effect estimates compared to studies focused on one specific technology or role."
    - "Strain was operationalized as a single exhaustion-based construct; other consequences such as turnover, productivity, or physiological symptoms were not directly measured."
    - "Common method bias was addressed only statistically (a latent method factor), not through separation of data sources or time-lagged design."
risk_of_bias: "medium"
relevance_to_project: >
  Gives the SNH project an empirically validated causal chain from a specific, malleable
  technology characteristic -- presenteeism/constant reachability -- through concrete
  stressors (role ambiguity, work overload, work-home conflict) to psychological strain,
  supporting design and policy interventions (e.g., explicit non-availability windows,
  managed response-time expectations) as more promising levers for remote-work technostress
  than simplifying tool usability or complexity, which showed weaker or null effects.
tags:
  topic: ["technostress", "remote-work", "work-life-balance", "burnout", "measurement"]
  method: ["cross-sectional", "survey"]
  population: ["knowledge-workers", "general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Technostress Technological Antecedents and Implications/Technostress Technological Antecedents and Implications.md"
  pdf: "papers/Academic/01 Academic - Extended/Technostress Technological Antecedents and Implications.pdf"
  notes: null

---

id: "tarafdar-2007-the-impact-of-technostress-on-role"
title: "The Impact of Technostress on Role Stress and Productivity"
authors:
  - "Tarafdar, Monideepa"
  - "Tu, Qiang"
  - "Ragu-Nathan, Bhanu S."
  - "Ragu-Nathan, T. S."
year: 2007
doi: "10.2753/mis0742-1222240109"
venue: {type: "journal", name: "Journal of Management Information Systems", volume: 24, issue: 1, pages: "301-328"}
citation: "Tarafdar et al. (2007). The Impact of Technostress on Role Stress and Productivity. Journal of Management Information Systems, 24(1), 301-328. https://doi.org/10.2753/mis0742-1222240109"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using structural equation modeling on survey data from 233 ICT users across two U.S.
  public-sector organizations, this paper defines technostress as a five-dimension construct
  (techno-overload, techno-invasion, techno-complexity, techno-insecurity, techno-
  uncertainty) and shows it directly reduces individual productivity and also increases role
  stress (role conflict and role overload), which independently reduces productivity. It
  offers both a validated diagnostic instrument for technostress and a theoretical bridge
  between technology-induced stress and role theory, arguing organizations can partly offset
  technostress's productivity costs by managing role conflict and overload.
claims:
  - text: "Technostress is inversely related to individual productivity (standardized estimate -0.280, p<0.01 in the direct model; -0.158, p<0.10 in the full combined model), supporting Hypothesis 1."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "stress"]
    predictors: ["technostress", "workload"]
  - text: "Technostress is positively related to role stress (standardized estimate 0.610-0.613, p<0.01), and role stress in turn is inversely related to productivity (-0.306 to -0.210, p<0.05), indicating technostress also harms productivity indirectly by increasing role conflict and role overload."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "stress"]
    predictors: ["technostress", "workload", "boundary-management"]
  - text: "Exploratory factor analysis and reliability testing identified five distinct, internally consistent (Cronbach's alpha 0.81-0.89) technostress creators: techno-overload, techno-invasion (blurred work/personal boundaries), techno-complexity, techno-insecurity (fear of job displacement by technology or more tech-savvy coworkers), and techno-uncertainty (constant upgrade cycles)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress", "burnout"]
    predictors: ["technostress", "boundary-management"]
population:
  who: "ICT end users (non-IT-professional employees) in two U.S. public-sector organizations with similar client-server networked systems"
  where: ["United States"]
  when: null
  n: 233
  sector: ["public-sector"]
  sample_notes: >
    Self-selected volunteer sample (not random): 320 invitation emails sent, 264
    questionnaires distributed, 233 returned (88.2% of distributed, 73% of invited). Sample
    skewed heavily female (78%) and experienced (95% had 5+ years work experience);
    demographics suggest a specific administrative/clerical public-sector workforce,
    limiting generalizability to other occupations or private-sector/tech-industry settings.
limitation:
  primary: "Self-selected (non-random) sample means participants who felt more technostress may have been more motivated to respond, potentially inflating the observed relationships."
  others:
    - "Productivity was measured via a self-reported perceived-productivity scale, not objective performance data, so findings reflect perceived rather than actual productivity effects."
    - "Cross-sectional design cannot establish causal direction or rule out reverse causation between technostress, role stress, and productivity."
    - "Sample drawn from only two similar public-sector organizations with comparable IT support infrastructure, limiting generalizability to remote/distributed or knowledge-work settings."
risk_of_bias: "medium"
relevance_to_project: >
  Provides a validated, five-factor technostress measurement instrument (techno-overload,
  -invasion, -complexity, -insecurity, -uncertainty) directly usable for assessing SNH
  constructs like boundary-management and technostress in remote/distributed workers, and
  empirically links technostress to role stress and productivity loss, supporting the
  project's interest in ICT-driven mechanisms of burnout and reduced wellbeing.
tags:
  topic: ["technostress", "burnout", "productivity", "work-life-balance"]
  method: ["survey", "cross-sectional"]
  population: ["public-sector", "ict-users"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The Impact of Technostress on Role Stress and Productivity/The Impact of Technostress on Role Stress and Productivity.md"
  pdf: "papers/Academic/01 Academic - Extended/The Impact of Technostress on Role Stress and Productivity.pdf"
  notes: null

---

id: "vyas-2020-the-impact-of-working-from-home"
title: "The impact of working from home during COVID-19 on work and life domains: an exploratory study on Hong Kong"
authors:
  - "Vyas, Lina"
  - "Butakhieo, Nantapong"
year: 2020
doi: "10.1080/25741292.2020.1863560"
venue: {type: "journal", name: "Policy Design and Practice", volume: null, issue: null, pages: "1-18"}
citation: "Vyas et al. (2020). The impact of working from home during COVID-19 on work and life domains: an exploratory study on Hong Kong. Policy Design and Practice, 1-18. https://doi.org/10.1080/25741292.2020.1863560"
article_type: "review"
method: {design: "review-scoping", approach: "secondary-data", evidence_level: "low", preregistered: false}
gist: >
  Vyas and Butakhieo synthesize Hong Kong government WFH timelines, third-party workplace
  surveys, and the international teleworking literature into an exploratory framework
  (organizational and individual/family factors linked to work and life domain outcomes)
  plus a SWOT analysis of forced work-from-home adoption across the four 2020 COVID-19
  waves. Drawing on secondary polls (Lingnan University, JLL, Sun Life, FastLane, Mental
  Health Association of Hong Kong), they trace early enthusiasm for WFH cooling into
  consistent complaints about cramped multigenerational housing, blurred work/family
  boundaries, missed face-to-face collaboration, and elevated stress, anxiety, loneliness
  and burnout. The paper concludes WFH will likely persist as a flexible option rather than
  fully replace office work and recommends the Hong Kong government issue formal WFH
  guidelines, technology-training minimums, and updated labor/insurance policy to support
  hybrid arrangements.
claims:
  - text: "A secondary survey (Wong and Cheung 2020, Lingnan University) found over 80% of Hong Kong workers preferred at least partial WFH, citing more time to rest (72.2% strongly agree), decreased work-related stress (63.8%), and improved work-life balance (60.7%), though only 45% agreed employers provided adequate support for effective WFH."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["work-life-balance", "job-satisfaction", "stress"]
    predictors: ["remote-work-intensity", "organizational-culture"]
  - text: "A JLL (2020) survey found 68% of Hong Kong workers missed going to the office and missed human interaction, the professional environment, and face-to-face collaboration; workers 35 and older reported particular difficulty juggling home and work commitments simultaneously, attributed to multigenerational households with less dedicated space."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["isolation", "collaboration", "communication"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "A Mental Health Association of Hong Kong survey (May-July 2020) found 87% of respondents had symptoms of stress; the paper reports Hong Kong WFH employees, similar to Singapore and India, experienced elevated stress, job-security fears, anxiety, loneliness, and burnout, with a Singapore study finding WFH workers more stressed than COVID-19 front-line workers."
    evidence: "case-study"
    support_strength: "low"
    outcomes: ["stress", "loneliness", "burnout", "anxiety"]
    predictors: ["remote-work-intensity", "technostress", "isolation"]
population:
  who: "Working adults in Hong Kong during the COVID-19 pandemic, characterized indirectly through synthesis of multiple third-party polls and surveys (e.g., Lingnan University WFH survey, JLL property-sector survey, Sun Life corporate wellness survey, FastLane infographic survey, Mental Health Association of Hong Kong survey) rather than an original sample collected by the authors."
  where: ["Hong Kong"]
  when: "2020 (first through fourth COVID-19 waves, January-November 2020)"
  n: null
  sector: ["office-workers", "civil-service", "mixed-private-sector"]
  sample_notes: >
    The authors did not conduct their own survey or interviews; all quantitative figures are
    drawn from secondary, largely grey-literature sources (corporate surveys, NGO polls,
    news-reported infographics) whose sampling frames, response rates, and
    representativeness are not reported or independently verifiable, so figures should be
    treated as illustrative rather than generalizable.
limitation:
  primary: "This is a narrative/exploratory literature review and SWOT-style conceptual analysis, not a study with original primary data collection; every empirical figure cited rests on third-party polls, corporate surveys, or press-reported infographics of unverifiable methodology."
  others:
    - "No systematic review protocol is described; sources appear selectively cited to build the framework rather than exhaustively or reproducibly searched."
    - "Key statistics (e.g., 87% stress, 68% missed the office) come from grey literature/press releases with no reported sample size, response rate, or sampling method, so effect sizes cannot be assessed for bias."
    - "The SWOT analysis reflects the authors' qualitative synthesis rather than a coded or validated instrument."
risk_of_bias: "high"
relevance_to_project: >
  Provides a compact, Hong-Kong-specific catalogue of WFH strengths/weaknesses (missed human
  interaction and collaboration, loneliness, blurred work/family boundaries, lack of
  dedicated space) set against office strengths (belonging, onboarding, networking) that the
  SNH project can mine for candidate isolation and connection mechanisms and for framing
  dense-housing/hybrid-work policy recommendations, though its evidence base is secondary
  survey synthesis rather than original measurement.
tags:
  topic: ["remote-work", "work-life-balance", "isolation", "loneliness", "burnout", "mental-health"]
  method: ["review-scoping", "secondary-data", "case-study"]
  population: ["office-workers", "hong-kong"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The impact of working from home during COVID-19 on work and life domains  an exploratory study on Hong Kong/The impact of working from home during COVID-19 on work and life domains  an exploratory study on Hong Kong.md"
  pdf: "papers/Academic/01 Academic - Extended/The impact of working from home during COVID-19 on work and life domains  an exploratory study on Hong Kong.pdf"
  notes: null

---

id: "bodner-2022-the-impact-of-working-from-home"
title: "The Impact of Working from Home on Mental Health: A Cross-Sectional Study of Canadian Worker’s Mental Health during the Third Wave of the COVID-19 Pandemic"
authors:
  - "Bodner, Aidan"
  - "Ruhl, Leo"
  - "Barr, Emily"
  - "Shridhar, Arti"
  - "Skakoon-Sparling, Shayna"
  - "Card, Kiffer George"
year: 2022
doi: "10.3390/ijerph191811588"
venue: {type: "journal", name: "International Journal of Environmental Research and Public Health", volume: 19, issue: 18, pages: "11588"}
citation: "Bodner et al. (2022). The Impact of Working from Home on Mental Health: A Cross-Sectional Study of Canadian Worker’s Mental Health during the Third Wave of the COVID-19 Pandemic. International Journal of Environmental Research and Public Health, 19(18), 11588. https://doi.org/10.3390/ijerph191811588"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using a survey of 1576 Canadian workers collected during the third wave of COVID-19
  (April-June 2021), this study finds that both working exclusively from home and working
  exclusively in-person are associated with significantly poorer self-rated mental health
  than hybrid work arrangements, after adjusting for demographic and socioeconomic
  confounders. Vaccination status was a statistically significant but small mediator (about
  7%) of the relationship between work setting and mental health, while mask-wearing and
  physical distancing were not significant mediators. The authors argue hybrid work may
  protect mental health better than either extreme of fully remote or fully in-person work,
  and that pandemic-specific health behaviors are not the primary driver of the association.
claims:
  - text: "Compared to hybrid workers, those working exclusively from home had significantly higher odds of negative self-rated mental health (adjusted OR = 2.79, 95% CI: 1.90-4.07) and those working exclusively in-person also had higher odds (adjusted OR = 2.79, 95% CI: 1.83-4.26), controlling for income, age, gender, ethnicity, education, hours worked, and occupation."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health"]
    predictors: ["remote-work-intensity"]
  - text: "COVID-19 vaccination status significantly mediated approximately 7% of the association between work setting and self-rated mental health (p = 0.02), while mask-wearing (p = 0.76) and physical distancing (p = 0.20) were not significant mediators, suggesting fear of viral exposure was not the primary driver of the work-setting/mental-health relationship."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["mental-health"]
    predictors: ["remote-work-intensity"]
  - text: "Negative self-rated mental health was also significantly associated with increasing hours worked per week, being 40 years or older (vs. 18-29), identifying as non-binary (vs. man), and Middle Eastern or 'Other' ethnicity (vs. White); positive self-rated mental health was associated with employment in business, health, management, natural/applied sciences, or trades occupations (vs. sales and service) and having received two COVID-19 vaccine doses."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["mental-health"]
    predictors: ["workload"]
population:
  who: "Canadian workers aged 16+ who were employed during the COVID-19 pandemic, recruited online via paid social media advertising for the Canadian Social Connection Survey (CSCS)"
  where: ["Canada"]
  when: "21 April 2021 to 1 June 2021 (third wave of COVID-19 pandemic)"
  n: 1576
  sector: ["general-workforce"]
  sample_notes: >
    Analytic sample drawn from 2286 eligible CSCS respondents; 370 excluded as not currently
    employed and 340 more excluded for missing data on primary outcome/exposure, leaving
    1576. Convenience sample recruited via paid Facebook/Twitter/Instagram/Google ads, not
    representative; hybrid workers were over-represented (77.2%) relative to national work-
    from-home rates at the time, limiting generalizability.
limitation:
  primary: "Secondary cross-sectional survey data cannot establish causality and collapses work setting into only three categories and mental health into two, losing nuance in the association between telework intensity and mental health."
  others:
    - "Convenience sample recruited via paid social media ads over-represented hybrid workers (77.2%) relative to national estimates (26.5-40.5% working mostly from home in this period), limiting representativeness."
    - "The survey lacked measures of workers' worry about COVID-19 exposure at work or workplace protocol implementation, so mediation models involving vaccination/masking/distancing are described by the authors as preliminary."
    - "Self-rated mental health is a global, single-item measure not equivalent to validated clinical scales like PHQ-2/GAD-2, limiting diagnostic specificity."
risk_of_bias: "medium"
relevance_to_project: >
  Provides adjusted effect-size evidence (aOR ~2.8) that both fully-remote and fully-in-
  person arrangements are associated with worse self-rated mental health than hybrid work,
  directly informing SNH's design question of whether hybrid work schedules should be
  favored as a structural mitigation for remote-worker mental health risk, and shows that
  pandemic-safety-behavior mediators (vaccination, masking, distancing) explain very little
  of that relationship.
tags:
  topic: ["remote-work", "hybrid-work", "mental-health", "wellbeing"]
  method: ["cross-sectional", "survey"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Academic/MD/The Impact of Working from Home on Mental Health- A Cross-Sectional Study of Canadian Worker’s Mental Health during the Third Wave of the COVID-19 Pandemic/The Impact of Working from Home on Mental Health- A Cross-Sectional Study of Canadian Worker’s Mental Health during the Third Wave of the COVID-19 Pandemic.md"
  pdf: null
  notes: null

---

id: "geiger-2021-the-labor-of-maintaining-and-scaling"
title: "The Labor of Maintaining and Scaling Free and Open-Source Software Projects"
authors:
  - "Geiger, R. Stuart"
  - "Howard, Dorothy"
  - "Irani, Lilly"
year: 2021
doi: "10.1145/3449249"
venue: {type: "journal", name: "Proceedings of the ACM on Human-Computer Interaction", volume: 5, issue: "CSCW1", pages: "1-28"}
citation: "Geiger et al. (2021). The Labor of Maintaining and Scaling Free and Open-Source Software Projects. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1), 1-28. https://doi.org/10.1145/3449249"
article_type: "empirical"
method: {design: "qualitative", approach: "interview", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  Based on 37 semi-structured interviews with F/OSS maintainers, this study finds that the
  labor of maintaining open-source projects does not simply grow with scale but transforms
  in kind -- from solo, ad-hoc upkeep into distributed, rule-bound organizational,
  financial, and emotional labor. It introduces two influential constructs, 'scalar labor'
  (the work of building capacity to meet a project's growing needs) and 'scalar debt' (the
  burnout-inducing deficit that accrues when growth outpaces that capacity), and documents
  how popular maintainers can become hypervisible 'microcelebrities' rather than invisible
  infrastructure workers.
claims:
  - text: "As F/OSS projects scale across many dimensions (users, contributors, codebase complexity, ecosystem interdependence), the work of maintaining them does not merely increase in volume but fundamentally changes in kind (e.g., ad-hoc solo governance shifts to formal multi-maintainer structures; user support moves from a growth opportunity to an 'overwhelming flood' requiring triage teams and rules), and interviewees repeatedly linked this intensification to demotivation, exhaustion, and burnout."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "job-engagement"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "The paper introduces the concept of 'scalar debt' -- an accumulated deficit when a project's growth in users/contributors outpaces growth in its organizational capacity to maintain itself -- which interviewees described as living in a 'constant state of incipient crisis, overwork, or burnout' while trying to keep projects from falling further behind."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "stress"]
    predictors: ["open-source-maintenance", "workload"]
  - text: "Contrary to the dominant framing of infrastructural maintenance as invisible work, maintainers of large, popular F/OSS projects can become hypervisible 'microcelebrities' with large social-media followings who are routinely invited to speak at conferences and companies, yet this status generates its own invisible burdens (torrents of unsolicited messages, behind-the-scenes dispute adjudication) rather than relieving maintenance labor."
    evidence: "qualitative"
    support_strength: "low"
    outcomes: ["burnout", "social-presence"]
    predictors: ["open-source-maintenance"]
population:
  who: "37 current or former maintainers/core contributors of free and open-source software (F/OSS) projects, purposively sampled for diversity in geography, gender, employment status/sector, and project type/size, focused on projects that began as volunteer efforts and became widely relied-upon infrastructure"
  where: ["United States", "multiple countries (14 countries of origin, 12 of residence, across 5 continents)"]
  when: "2019-2020"
  n: 37
  sector: ["open-source", "technology"]
  sample_notes: >
    Non-random, purposive plus snowball sampling via personal networks, F/OSS conferences, a
    Twitter call for participation, and cold e-mail; not intended to be representative.
    Post-interview demographic survey completed by 85%: 19% women/female, 81% men/male, 0%
    non-binary; 72% white/Caucasian; ages 25-64 (53% aged 30-39); US most common country of
    birth (47%) and residence (56%).
limitation:
  primary: "Non-random, self-selected sample of 37 maintainers recruited through personal networks, conferences, and snowball sampling limits generalizability, and the sample specifically excludes the overwhelming majority of F/OSS projects that are single-maintainer or entirely corporate-developed."
  others:
    - "Retrospective interview accounts may be inaccurate; the authors note the study could be complemented by participant-observation, diary studies, or trace-data analysis for more contemporaneous data."
    - "All three authors have direct personal experience as F/OSS contributors/maintainers and the research was funded by non-profit foundations that also directly fund F/OSS projects, which the authors acknowledge may have shaped interviewee responses and analytic distance."
risk_of_bias: "medium"
relevance_to_project: >
  Directly informs the SNH project's model of open-source maintainer burnout: the 'scalar
  labor'/'scalar debt' framework gives a design-relevant mechanism (organizational capacity
  failing to keep pace with growth) for predicting when community-health interventions are
  needed, and the paper's concrete drivers of burnout -- user-support overload, emotional
  labor from entitled users, funding-driven governance strain, and
  hypervisibility/microcelebrity dynamics -- are candidate measurable predictors for an SNH
  maintainer-burnout instrument.
tags:
  topic: ["open-source", "maintainer-burnout", "burnout", "community-health"]
  method: ["qualitative", "interview"]
  population: ["open-source-maintainers"]
source:
  markdown: "Papers_Data/Academic/MD/The Labor of Maintaining and Scaling Free and Open-Source Software Projects/The Labor of Maintaining and Scaling Free and Open-Source Software Projects.md"
  pdf: "papers/Academic/The Labor of Maintaining and Scaling Free and Open-Source Software Projects.pdf"
  notes: null

---

id: "brown-1985-the-managed-heart-commercialization-of-human"
title: "The Managed Heart: Commercialization of Human Feeling."
authors:
  - "Brown, Julie V."
  - "Hochschild, Arlie Russell"
year: 1985
doi: "10.2307/2578990"
venue: {type: "journal", name: "Social Forces", volume: 64, issue: 1, pages: "223"}
citation: "Brown et al. (1985). The Managed Heart: Commercialization of Human Feeling.. Social Forces, 64(1), 223. https://doi.org/10.2307/2578990"
article_type: "commentary"
method: {design: "qualitative", approach: "ethnography", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This is a 1985 Social Forces book review by Julie V. Brown of Arlie Hochschild's The
  Managed Heart, summarizing Hochschild's argument that private 'feeling rules' governing
  emotional expression (via 'surface acting' and 'deep acting') are commercially
  appropriated by employers as 'emotional labor.' The review highlights Hochschild's
  ethnographic case studies of flight attendants and bill collectors, finding that
  sustained, employer-monitored emotional performance produced alienation, burnout ('loss of
  the capacity to feel'), or a sense of being a 'phony,' and that women disproportionately
  bear this labor even in identical jobs to men.
claims:
  - text: "Flight attendants subjected to sustained, employer-monitored emotional labor became alienated from their own feelings; Hochschild found some 'burned out' (lost the capacity to feel) while others came to see themselves as 'phonies.'"
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["burnout", "mental-health"]
    predictors: ["emotional-labor", "organizational-culture"]
  - text: "Emotion management varies by gender and social class: women perform substantially more emotional labor than men, such that identical jobs are experienced as 'one sort of job for a woman and another sort of job for a man.'"
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction", "wellbeing"]
    predictors: ["emotional-labor", "gender-differences"]
  - text: "In ordinary private life people regulate emotional expression according to socially shared 'feeling rules,' using effortful 'surface acting' (managing outward display) or 'deep acting' (inducing the actual feeling); when this private capacity is sold as labor (e.g., by flight attendants and bill collectors), the emotional exertion is redirected toward corporate ends."
    evidence: "qualitative"
    support_strength: "low-to-moderate"
    outcomes: ["communication", "social-presence"]
    predictors: ["emotional-labor"]
population:
  who: "Not this document's own sample: it is a book review describing Hochschild's original research subjects, primarily flight attendants at a major U.S. airline (training-program observation and interviews) plus bill collectors, with an earlier chapter drawing on data from Berkeley students."
  where: ["United States"]
  when: null
  n: null
  sector: ["service-work", "airline-industry"]
  sample_notes: >
    This is a secondary account (a journal book review), not the primary study; no sample
    size, response rate, or precise data-collection dates are reported here beyond mentions
    of flight-attendant training observations/interviews and a Berkeley student sample used
    in the book's first part.
limitation:
  primary: "This document is a brief, opinion-inflected book review, not the primary empirical source, so methodological details (sampling, interview counts, coding, dates) needed to assess rigor are absent."
  others:
    - "The reviewer's summary is necessarily selective and evaluative (e.g., calling one section 'least satisfying'), so it reflects interpretive framing as much as the book's findings."
    - "Underlying study (as described) is qualitative/ethnographic on a small number of occupations (flight attendants, bill collectors) plus a student sample, limiting generalizability even in the original work."
risk_of_bias: "high"
relevance_to_project: >
  Hochschild's emotional-labor concept, as relayed in this review, is directly relevant to
  SNH's interest in burnout among people whose work requires sustained interpersonal
  performance (e.g., community managers, moderators, support/help-desk roles): it suggests
  that requiring workers to continuously manage and display feelings toward others, without
  room for authentic experience, is itself a burnout pathway distinct from workload alone,
  and that this burden may fall unevenly by gender or role.
tags:
  topic: ["burnout", "mental-health", "wellbeing", "job-satisfaction"]
  method: ["qualitative", "ethnography"]
  population: ["service-workers", "flight-attendants", "gender"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The Managed Heart Commercialization of Human Feeling/The Managed Heart Commercialization of Human Feeling.md"
  pdf: "papers/Academic/01 Academic - Extended/The Managed Heart Commercialization of Human Feeling.pdf"
  notes: null

---

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

---

id: "loon-2019-the-paradox-of-employee-psychological-well"
title: "The paradox of employee psychological well-being practices: an integrative literature review and new directions for research"
authors:
  - "Loon, Mark"
  - "Otaye-Ebede, Lilian"
  - "Stewart, Jim"
year: 2019
doi: "10.1080/09585192.2018.1479877"
venue: {type: "journal", name: "The International Journal of Human Resource Management", volume: 30, issue: 1, pages: "156-187"}
citation: "Loon et al. (2019). The paradox of employee psychological well-being practices: an integrative literature review and new directions for research. The International Journal of Human Resource Management, 30(1), 156-187. https://doi.org/10.1080/09585192.2018.1479877"
article_type: "review"
method: {design: "review-integrative", approach: "analytical", evidence_level: "low-to-moderate", preregistered: false}
gist: >
  This integrative literature review synthesizes 68 peer-reviewed journal articles using a
  paradox metatheory lens to examine how HR practices intended to boost employee
  psychological wellbeing (PWB) often conflict with practices aimed at organisational
  performance. It catalogs specific 'paradoxical' practices (e.g., high-performance work
  systems, flexible work arrangements, performance-based compensation) that simultaneously
  help and harm PWB, identifies 'mutual-gains' practices (e.g., learning and development,
  ergonomic investment, employee voice) that support both wellbeing and performance, and
  proposes a new five-stage sensemaking framework (mess, problem, dilemma, paradox,
  achieving) for managers to navigate these tensions rather than resolve them through simple
  trade-offs.
claims:
  - text: "High-performance work systems (HPWS) and high-involvement management (HIM) can raise employee job satisfaction and intrinsic reward while simultaneously increasing anxiety, work intensity, and workload, so the same practice bundle produces both PWB gains and PWB harms rather than one clean effect (drawing on Decramer et al., 2015; Van De Voorde & Beijer, 2015; Wood, Van Veldhoven, Croon, & de Menezes, 2012)."
    evidence: "review-integrative"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction", "stress", "burnout"]
    predictors: ["workload", "organizational-culture"]
  - text: "Flexible working arrangements (FWA) increase job autonomy and work-life balance and thereby support PWB in some studies (Rudolph & Baltes, 2017; Boreham, Povey, & Tomaszewski, 2016), but other research finds FWA can instead create job insecurity, with effectiveness contingent on being coupled with effective team design (Lange, 2013; Liu & Wang, 2011)."
    evidence: "review-integrative"
    support_strength: "low-to-moderate"
    outcomes: ["work-life-balance", "wellbeing"]
    predictors: ["autonomy", "boundary-management"]
  - text: "Employees who perceive their relationship with the employer as an economic exchange interpret high-performance HR practices as exploitative, whereas those who perceive it as a social exchange view the same practices as a mutual-gains, win-win arrangement for wellbeing and performance (Zhang, Zhu, Dowling, & Bartram, 2013); organisational and procedural justice perceptions similarly shape whether PWB-performance tensions emerge."
    evidence: "review-integrative"
    support_strength: "low-to-moderate"
    outcomes: ["job-satisfaction", "wellbeing"]
    predictors: ["organizational-culture", "perceived-organizational-support"]
population:
  who: "68 English-language peer-reviewed journal articles (67.6% quantitative empirical, 2.9% qualitative, 4.4% multi-method, 17% conceptual/review) on employee HR practices, psychological wellbeing, and organisational performance, retrieved from Scopus and Web of Science"
  where: []
  when: null
  n: 68
  sector: ["general-workforce"]
  sample_notes: >
    Boolean keyword search ('health'/'well-being' + 'employee'/'workplace' + 'organi*ational
    performance' + 'human resource *') across Scopus (106 hits) and Web of Science (54
    hits); merged and deduplicated to 140, then screened by abstract to 93, with 68 retained
    after excluding healthcare-specific studies, articles with only cursory PWB or HR
    relevance, and studies emphasising unrelated constructs or personal/demographic
    detriments to PWB. Not a systematic/PRISMA review; single coding framework applied
    reflexively rather than by independent dual reviewers.
limitation:
  primary: "The search strategy, though transparently reported, is limited to two databases with keyword-based Boolean terms and a single-team reflexive coding process rather than independent dual-reviewer screening, leaving the paradox categorisations vulnerable to search-term and interpretive bias."
  others:
    - "Narrative/integrative synthesis rather than meta-analysis, so no pooled effect sizes are reported across the 68 studies"
    - "Only 68 of many candidate articles were retained after exclusion criteria, potentially omitting sector-specific (e.g., healthcare) or non-English findings relevant to PWB-performance tensions"
    - "The proposed sensemaking framework (mess-problem-dilemma-paradox-achieving) is conceptual and illustrative, built by analogy to prior sensemaking literature, and has not itself been empirically tested"
risk_of_bias: "medium"
relevance_to_project: >
  Provides a conceptual warning and evidence base for SNH intervention design: practices
  meant to raise remote/hybrid workers' wellbeing (flexible arrangements,
  communication/participation practices, performance incentives) can simultaneously
  undermine it, so interventions should be evaluated for paradoxical performance-wellbeing
  trade-offs rather than assumed to be win-win; the sensemaking framework also offers a
  possible process model for how managers can work through such tensions when designing SNH
  programs.
tags:
  topic: ["wellbeing", "job-satisfaction", "burnout", "work-life-balance", "methodology"]
  method: ["review-integrative", "literature-synthesis"]
  population: ["general-workforce", "hr-practices"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The paradox of employee psychological well-being practices  an integrative literature review and new directions for research/The paradox of employee psychological well-being practices  an integrative literature review and new directions for research.md"
  pdf: "papers/Academic/01 Academic - Extended/The paradox of employee psychological well-being practices  an integrative literature review and new directions for research.pdf"
  notes: null

---

id: "pavot-2008-the-satisfaction-with-life-scale-and"
title: "The Satisfaction With Life Scale and the emerging construct of life satisfaction"
authors:
  - "Pavot, William"
  - "Diener, Ed"
year: 2008
doi: "10.1080/17439760701756946"
venue: {type: "journal", name: "The Journal of Positive Psychology", volume: 3, issue: 2, pages: "137-152"}
citation: "Pavot et al. (2008). The Satisfaction With Life Scale and the emerging construct of life satisfaction. The Journal of Positive Psychology, 3(2), 137-152. https://doi.org/10.1080/17439760701756946"
article_type: "review"
method: {design: "review-narrative", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  This narrative review updates the 1993 Pavot & Diener review of the Satisfaction With Life
  Scale (SWLS), synthesizing 15+ years of subsequent research on the scale's psychometrics
  (alpha 0.79-0.89, test-retest 0.54-0.84) and on the cognitive processes underlying life
  satisfaction judgments. It concludes that life satisfaction judgments combine stable top-
  down influences (personality traits like extraversion/neuroticism) with bottom-up domain
  satisfactions, are only modestly disturbed by transient mood/context effects, and predict
  outcomes including reduced suicide risk, better health, and stronger social relationships
  across clinical, health, and cross-cultural samples.
claims:
  - text: "Life satisfaction judgments are predominantly based on chronically accessible information (personality dispositions and domain satisfactions such as work, relationships, health) rather than transient contextual factors; item-order and mood effects, while real, are generally small compared to stable variance (Schimmack & Oishi, 2005; Eid & Diener, 2004)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["wellbeing"]
    predictors: ["sense-of-belonging"]
  - text: "Life satisfaction is a significant negative predictor of suicidal ideation and suicide risk across multiple studies; a longitudinal Finnish Twin cohort study found life satisfaction predicted lower suicide risk 20 years later even after controlling for substance use, age, and gender (Koivumaa-Honkanen et al., 2001)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["suicidal-ideation", "mental-health"]
    predictors: ["social-support"]
  - text: "SWLS scores discriminate strongly by life circumstance and clinical status: psychiatric patients and severely disadvantaged groups (e.g., street-level sex workers M=10.3, male prison inmates M=12.3) score far below the neutral point (20) versus general population samples (M=23-27), and SWLS scores are sensitive to therapeutic improvement over time (e.g., significant increases after 1-2 months of therapy)."
    evidence: "review-narrative"
    support_strength: "moderate"
    outcomes: ["wellbeing", "mental-health"]
    predictors: ["social-support"]
population:
  who: "Narrative review synthesizing dozens of independent studies using the Satisfaction With Life Scale across college students, clinical/psychiatric patients, health/disability populations, and cross-cultural adult samples worldwide"
  where: ["USA", "Netherlands", "UK", "Australia", "Taiwan", "Japan", "Korea", "Germany", "Belarus", "Kenya", "Greenland", "Canada"]
  when: "Studies reviewed span 1985-2008"
  n: null
  sector: ["clinical", "general-population"]
  sample_notes: >
    No single sample; this is a selective narrative review of published SWLS studies chosen
    by the authors to represent a range of populations and findings rather than a systematic
    or meta-analytic sample; individual cited studies range from N=25 to N=5668.
limitation:
  primary: "As a narrative (non-systematic) review, study selection is author-curated rather than exhaustive or meta-analytic, so the synthesis may not represent the full literature or correct for publication bias."
  others:
    - "Most underlying studies are cross-sectional/correlational, limiting causal claims about what drives life satisfaction versus what it predicts."
    - "Heavy reliance on convenience samples (especially college students) in the underlying literature, noted explicitly by the authors as a limitation of the field."
    - "Cross-cultural comparability of raw SWLS scores is questioned within the review itself (e.g., item-response modeling revealing measurement non-invariance between Norwegian and Greenlandic samples)."
risk_of_bias: "medium"
relevance_to_project: >
  The SWLS is a widely-used, brief, well-validated 5-item measure of global life
  satisfaction (a cognitive/evaluative component of subjective wellbeing distinct from
  momentary affect) that the SNH project could adopt as an outcome measure for remote-worker
  or community wellbeing surveys; the review's evidence that life satisfaction predicts
  suicide risk, mental health, and social relationship quality supports its use as a distal
  wellbeing indicator alongside more proximal SNH constructs like isolation and belonging.
tags:
  topic: ["wellbeing", "mental-health", "measurement", "suicide-prevention"]
  method: ["review-narrative", "secondary-data"]
  population: ["general-population", "clinical-patients", "cross-cultural"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The Satisfaction With Life Scale and the emerging construct of life satisfaction/The Satisfaction With Life Scale and the emerging construct of life satisfaction.md"
  pdf: "papers/Academic/01 Academic - Extended/The Satisfaction With Life Scale and the emerging construct of life satisfaction.pdf"
  notes: null

---

id: "given-2007-the-wealth-of-networks-how-social"
title: "The wealth of networks: How social production transforms markets and freedom"
authors:
  - "Given, Jock"
year: 2007
doi: "10.1016/j.infoecopol.2007.03.001"
venue: {type: "journal", name: "Information Economics and Policy", volume: 19, issue: 2, pages: "278-282"}
citation: "Given (2007). The wealth of networks: How social production transforms markets and freedom. Information Economics and Policy, 19(2), 278-282. https://doi.org/10.1016/j.infoecopol.2007.03.001"
article_type: "commentary"
method: {design: "book-review", approach: "analytical", evidence_level: "speculative", preregistered: false}
gist: >
  This is a critical book review of Yochai Benkler's 'The Wealth of Networks' (2006), which
  argues that networked information technology has radically decentralized the capacity for
  'social production' - individuals and loose non-market affiliations producing goods and
  services (open-source software, Wikipedia, SETI@home) outside markets and the state. The
  reviewer, Jock Given, praises Benkler's account of open-source software and commons-based
  production as compelling but challenges the book's sharp moral dichotomy between monetary
  (bad) and non-monetary (good) motivations, and questions whether commons-based production
  will remain decentralized rather than being absorbed into commercial platforms. For the
  SNH project, the review is a secondary lens on the theoretical roots of open-
  source/commons-based collaboration rather than an empirical study of participant
  wellbeing.
claims:
  - text: "The reviewer argues Benkler's opposition between monetary/property-based production (framed as bad) and non-monetary/commons-based production (framed as good) is overdrawn, noting many contributors already mix market income, subsidies, and unremunerated sharing rather than fitting either pole."
    evidence: "book-review"
    support_strength: "speculative"
    outcomes: ["collaboration"]
    predictors: ["community-engagement", "organizational-culture"]
  - text: "The review points out that within two years of the book's publication, two prominent examples of 'social production' (MySpace and YouTube) were acquired by large commercial firms (News Corporation and Google), undercutting the thesis that networked technology durably decentralizes production away from market control."
    evidence: "book-review"
    support_strength: "speculative"
    outcomes: ["collaboration"]
    predictors: ["network-structure", "organizational-culture"]
  - text: "The reviewer credits Benkler's treatment of open-source software, Wikipedia, and academic publishing as the book's strongest evidence for social production, but argues the analysis is shaped too heavily by the narrow experience of academics, lawyers, and computer scientists as producers, limiting generalizability to other media and labor contexts."
    evidence: "book-review"
    support_strength: "speculative"
    outcomes: ["collaboration"]
    predictors: ["community-engagement", "sampling-method"]
population:
  who: "Not a study of a human sample; the review's subject is Benkler's 2006 book and the real-world social-production examples it discusses (open-source software projects, Wikipedia, SETI@home, academic publishing, MySpace/YouTube)."
  where: []
  when: "Review published 2007; discusses examples current through 2006-2007"
  n: null
  sector: ["open-source", "media", "academia"]
  sample_notes: >
    Not applicable - this is a single reviewer's critical essay about a book, not an
    empirical study with a sample.
limitation:
  primary: "This is one scholar's opinionated critique of a secondary source (a book), not original empirical research, so it offers no direct data on social-network-health outcomes."
  others:
    - "Focuses on economic and political theory (property rights, media policy, decentralization) rather than individual or community wellbeing, isolation, or burnout."
    - "Examples and critique are dated to the mid-2000s internet landscape (pre-social-media-platform consolidation in its modern form)."
risk_of_bias: "high"
relevance_to_project: >
  Provides theoretical background on why individuals contribute to open-source and other
  commons-based collaborative production without direct pay - relevant to understanding
  maintainer motivation and community engagement - but the reviewer's critique that non-
  monetary 'social production' can still be co-opted or is not intrinsically prosocial is a
  useful caution against assuming open-source community structures are automatically healthy
  for participants.
tags:
  topic: ["open-source", "community-health", "collaboration"]
  method: ["commentary", "analytical"]
  population: ["open-source-communities"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/The Wealth of Networks How Social Production Transforms Markets and Freedom/The Wealth of Networks How Social Production Transforms Markets and Freedom.md"
  pdf: "papers/Academic/01 Academic - Extended/The Wealth of Networks How Social Production Transforms Markets and Freedom.pdf"
  notes: null

---

id: "bennett-2021-videoconference-fatigue-exploring-changes-in-fatigue"
title: "Videoconference fatigue? Exploring changes in fatigue after videoconference meetings during COVID-19."
authors:
  - "Bennett, Andrew A."
  - "Campion, Emily D."
  - "Keeler, Kathleen R."
  - "Keener, Sheila K."
year: 2021
doi: "10.1037/apl0000906"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 106, issue: 3, pages: "330-344"}
citation: "Bennett et al. (2021). Videoconference fatigue? Exploring changes in fatigue after videoconference meetings during COVID-19.. Journal of Applied Psychology, 106(3), 330-344. https://doi.org/10.1037/apl0000906"
article_type: "empirical"
method: {design: "mixed-methods", approach: "experiment", evidence_level: "moderate", preregistered: false}
gist: >
  Using experience-sampling surveys sent hourly across a workweek plus open-ended
  qualitative questions, this study of 55 remote workers finds that videoconference fatigue
  is a distinct, real phenomenon (confirmed by 92.9% of qualitative respondents) that occurs
  close in time to specific meetings rather than only at end-of-day, and that it varies by
  time of day and by in-meeting behavior. Multilevel models of 279 meetings show that higher
  perceived group belongingness and, to a lesser extent, muting one's microphone predict
  lower post-meeting fatigue, while webcam use and meeting duration show no significant
  effect. The authors frame these findings with Attention Restoration Theory and argue
  belongingness is the most consistent protective factor against videoconference fatigue.
claims:
  - text: "In multilevel regression of 279 videoconference meetings (55 employees), higher perceived group belongingness was associated with significantly lower post-meeting fatigue (gamma = -.21, p = .003), the strongest and most consistent predictor in the model."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress"]
    predictors: ["sense-of-belonging"]
  - text: "Muting one's microphone during a meeting was associated with lower post-meeting fatigue (gamma = -.09, p = .09) and this effect was moderated by belongingness: at low group belongingness, more muting was linked to higher fatigue, whereas at high belongingness mute had no relationship with fatigue; webcam use, watching oneself, attention, and meeting duration showed no significant effects."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["stress"]
    predictors: ["sense-of-belonging", "communication"]
  - text: "Latent growth modeling of hourly fatigue across the workday found a quadratic (nonlinear) daily fatigue trajectory, and videoconferences held at specific times (around 10:30-11:30am, 1:30-2:30pm, and 3:30-4:30pm) were associated with fatigue deviating above the expected trajectory, while a midday (1:30pm) videoconference was associated with lower-than-expected fatigue; qualitative data showed 92.9% of 39 respondents described a distinct exhaustion/tiredness experience attributed to videoconferences."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["stress"]
    predictors: ["remote-work-intensity"]
population:
  who: "55 remote-working U.S. adults (from an initial 69) recruited via professional networking groups and the Prolific panel, working from home due to COVID-19, across legal, banking/finance, engineering, healthcare, education, and IT sectors"
  where: ["United States"]
  when: "April 30-May 22, 2020 (quantitative); September 2020 (qualitative)"
  n: 55
  sector: ["mixed-sector", "remote-work"]
  sample_notes: >
    58.2% male, 72.7% White, mean age 33.6; recruited via young-professional networking
    groups plus Prolific panel; 10 removed for low survey response and 4 for insufficient
    change in remote-work status; qualitative response rate 70.9% (39 of 55); quantitative
    analysis of videoconference characteristics used 279 meeting-level observations.
limitation:
  primary: "Small, non-probability convenience sample (n=55, one U.S. time zone, five consecutive workdays) limits generalizability to other populations, work schedules, and longer time horizons."
  others:
    - "Only postmeeting (near-term) fatigue was measured, not cumulative/long-term buildup across weeks despite qualitative hints that fatigue accumulates over time."
    - "Single-item measures were used for most videoconference characteristics (webcam, mute, watching self) to minimize survey burden, reducing measurement precision."
    - "Study focused only on fatigue (low energy), not vigor, and did not examine meeting content/topic as a moderator."
risk_of_bias: "medium"
relevance_to_project: >
  Directly identifies group belongingness as the most consistent protective factor against
  videoconference/remote-meeting fatigue, and offers evidence-based (if modest-effect)
  meeting-behavior levers (mute norms, belonging-building) that SNH interventions for remote
  workers could target to reduce burnout risk from meeting-heavy remote work.
tags:
  topic: ["remote-work", "wellbeing", "burnout", "social-presence"]
  method: ["mixed-methods", "experience-sampling"]
  population: ["remote-workers", "knowledge-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Videoconference Fatigue Exploring Changes in Fatigue After Videoconference Meetings During COVID-19/Videoconference Fatigue Exploring Changes in Fatigue After Videoconference Meetings During COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Videoconference Fatigue Exploring Changes in Fatigue After Videoconference Meetings During COVID-19.pdf"
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
  cultural 'domains' separated by physical, temporal, and psychological borders that people
  actively cross, negotiate, and shape rather than passively absorb spillover from. Building
  the theory from a personal journal, interviews with 15 individuals balancing demanding
  work and family roles, and prior literature, the paper defines border qualities
  (permeability, flexibility, blending, strength) and the role of 'border-keepers' (e.g.,
  supervisors, spouses), then derives eight testable propositions linking border/domain
  characteristics, central participation, and communication to work/family balance. It
  contributes a boundary-management vocabulary (segmentation-integration, border
  permeability/flexibility, other-domain awareness) that is directly reusable for modeling
  how remote workers manage the work/home border.
claims:
  - text: "In a cited study of 150 employed individuals with family responsibilities, participants reported that workplace cultures were, on average, more formal, less self-determined, less collective, less intimate, more hierarchical, more doing-oriented, and more likely to be money-based than their home/family cultures (Clark & Farmer, 1998, reported within this paper)."
    evidence: "cross-sectional"
    support_strength: "low"
    outcomes: ["work-life-balance"]
    predictors: ["organizational-culture"]
  - text: "Interviews with 15 individuals holding full-time jobs and significant family responsibilities indicated that border-crossers are largely proactive/enactive—shaping and negotiating work and family domains and the borders between them—rather than merely reactive recipients of spillover, as assumed by prior spillover/compensation theories."
    evidence: "qualitative"
    support_strength: "weak"
    outcomes: ["work-life-balance"]
    predictors: ["boundary-management"]
  - text: "A cited study of 2,000 women returning to work after childbirth found that supportive supervisors and supportive spouses were equally crucial to lowering stress during the transition, and other cited research found low supervisory support for employees' personal lives to be common despite employees preferring supervisors be accommodating of family needs (Galinsky & Stein, 1990; Galinsky & Hughes, 1987, reported within this paper)."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["stress", "wellbeing"]
    predictors: ["social-support", "leadership-style"]
population:
  who: "15 individuals with full-time employment and 'significant family responsibilities' (e.g., a single parent of three, a father with a hospitalized child), recruited as personal contacts of the author and two research assistants; theory also draws on published narrative sources and a broad multidisciplinary literature review"
  where: ["United States"]
  when: null
  n: 15
  sector: ["general-workforce"]
  sample_notes: >
    Convenience sample of the author's and research assistants' personal contacts,
    deliberately chosen for challenging work/family situations and diversity in age, family
    structure, work situation, ethnicity, gender and income; not randomly sampled and not
    intended to be representative. Additional 'findings' cited from other researchers'
    studies (e.g., n=150, n=2000) are secondary and reported without full methodological
    detail.
limitation:
  primary: "The theory's propositions are derived from a small, non-randomly selected qualitative interview sample and literature synthesis, then presented as testable but are not themselves empirically tested in this paper."
  others:
    - "Supporting empirical claims are drawn secondhand from other researchers' studies cited without effect sizes or full methodological detail."
    - "Published in 2000, predates the remote/hybrid work era, so its border concepts (physical/temporal/psychological permeability) were developed for traditional office-versus-home separation rather than home-based knowledge work."
    - "No demographic or occupational breakdown of the 15 interviewees is provided beyond illustrative anecdotes, limiting assessment of generalizability."
risk_of_bias: "not-applicable"
relevance_to_project: >
  Provides the SNH project's core vocabulary for boundary management (domain segmentation
  vs. integration, border permeability/flexibility/blending, border-keeper support, other-
  domain awareness) that is foundational for designing how remote and hybrid workers manage
  the work/home border to protect wellbeing and belonging; its propositions (e.g.,
  supervisor support and communication moderating imbalance) directly inform which boundary-
  management and social-support interventions the project should measure or design for.
tags:
  topic: ["work-life-balance", "remote-work", "wellbeing"]
  method: ["qualitative", "theory"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Work Family Border Theory A New Theory of Work Family Balance/Work Family Border Theory A New Theory of Work Family Balance.md"
  pdf: "papers/Academic/01 Academic - Extended/Work Family Border Theory A New Theory of Work Family Balance.pdf"
  notes: null

---

id: "galanti-2021-work-from-home-during-the-covid"
title: "Work From Home During the COVID-19 Outbreak"
authors:
  - "Galanti, Teresa"
  - "Guidetti, Gloria"
  - "Mazzei, Elisabetta"
  - "Zappalà, Salvatore"
  - "Toscano, Ferdinando"
year: 2021
doi: "10.1097/jom.0000000000002236"
venue: {type: "journal", name: "Journal of Occupational &amp; Environmental Medicine", volume: 63, issue: 7, pages: "e426-e432"}
citation: "Galanti et al. (2021). Work From Home During the COVID-19 Outbreak. Journal of Occupational &amp; Environmental Medicine, 63(7), e426-e432. https://doi.org/10.1097/jom.0000000000002236"
article_type: "empirical"
method: {design: "cross-sectional", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  Using the Job Demands-Resources model, this cross-sectional survey of 209 Italian
  employees forced into full-time WFH during the first year of COVID-19 found that family-
  work conflict and perceived social isolation were the strongest negative predictors of WFH
  productivity and work engagement and the strongest positive predictors of WFH stress,
  while job autonomy and self-leadership boosted productivity and engagement but did not
  significantly buffer stress. Distracting home environments hurt engagement specifically
  but not productivity or stress. The study frames social isolation as a core 'job demand'
  of enforced remote work that organizations should actively counter through structured
  communication.
claims:
  - text: "In the final regression model, perceived social isolation was significantly and negatively associated with WFH productivity (beta=-0.29, P<0.01) and work engagement (beta=-0.36, P<0.01), and positively associated with WFH stress (beta=0.48, P<0.01); family-work conflict showed a similar pattern (productivity beta=-0.29, engagement beta=-0.19, stress beta=0.31, all P<0.01)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "job-engagement", "stress"]
    predictors: ["isolation", "workload"]
  - text: "Job autonomy (beta=0.14, P<0.05) and self-leadership (beta=0.17, P<0.01) were positively related to WFH productivity, and both were also positively related to work engagement (autonomy beta=0.14/0.19, self-leadership beta=0.17/0.23 across steps, P<0.01), but neither resource had a significant relationship with WFH stress."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["productivity", "job-engagement", "stress"]
    predictors: ["autonomy", "sense-of-belonging"]
  - text: "A distracting home work environment was negatively associated with work engagement (beta=-0.14, P<0.05) but, unlike isolation and family-work conflict, was not a significant predictor of productivity or stress once other variables were controlled."
    evidence: "cross-sectional"
    support_strength: "low-to-moderate"
    outcomes: ["job-engagement", "productivity", "stress"]
    predictors: ["workload"]
population:
  who: "209 employees of Italian public and private organizations working from home full-time during the COVID-19 pandemic, most with no prior remote-work experience"
  where: ["Italy"]
  when: "May-July 2020"
  n: 209
  sector: ["mixed", "public-sector", "private-sector"]
  sample_notes: >
    Convenience sample recruited via an online Qualtrics questionnaire; 71.3% women, mean
    age 49.81 (SD 9.4); voluntary, anonymous, unpaid participation; only 9.1% had prior WFH
    experience, raising representativeness concerns for a broader remote-work population.
limitation:
  primary: "Cross-sectional design allows only associations, not causal claims, between job demands/resources and productivity, engagement, and stress."
  others:
    - "Convenience sample recruited entirely online, biasing toward digitally comfortable respondents and limiting generalizability."
    - "WFH productivity was measured with a single self-report item rather than a validated multi-item scale."
risk_of_bias: "medium"
relevance_to_project: >
  Provides quantified effect sizes tying perceived social isolation directly to reduced
  productivity/engagement and increased stress during enforced remote work, and shows
  autonomy/self-leadership as resources that improve engagement and productivity but do not
  offset isolation-driven stress -- useful evidence for designing interventions that target
  communication/connection specifically, not just general job-crafting resources.
tags:
  topic: ["remote-work", "isolation", "wellbeing", "job-engagement", "burnout"]
  method: ["survey", "cross-sectional"]
  population: ["remote-workers", "white-collar"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Work From Home During the COVID-19 Outbreak The Impact on Employees Remote Work Productivity Engagement and Stress/Work From Home During the COVID-19 Outbreak The Impact on Employees Remote Work Productivity Engagement and Stress.md"
  pdf: "papers/Academic/01 Academic - Extended/Work From Home During the COVID-19 Outbreak The Impact on Employees Remote Work Productivity Engagement and Stress.pdf"
  notes: null

---

id: "shockley-2021-work-family-strategies-during-covid-19"
title: "Work-family strategies during COVID-19: Examining gender dynamics among dual-earner couples with young children."
authors:
  - "Shockley, Kristen M."
  - "Clark, Malissa A."
  - "Dodd, Hope"
  - "King, Eden B."
year: 2021
doi: "10.1037/apl0000857"
venue: {type: "journal", name: "Journal of Applied Psychology", volume: 106, issue: 1, pages: "15-28"}
citation: "Shockley et al. (2021). Work-family strategies during COVID-19: Examining gender dynamics among dual-earner couples with young children.. Journal of Applied Psychology, 106(1), 15-28. https://doi.org/10.1037/apl0000857"
article_type: "empirical"
method: {design: "longitudinal", approach: "survey", evidence_level: "moderate", preregistered: false}
gist: >
  This two-wave study of 274 U.S. dual-earner couples with young children during the early
  COVID-19 shutdowns content-coded open-ended descriptions of childcare/work plans and used
  latent class analysis to identify seven distinct work-family management strategies.
  Gendered strategies (wife doing most/all childcare) persisted for 36.6% of couples and
  were linked to the worst family cohesion, relationship tension, and job performance for
  both spouses, while three novel egalitarian strategies (44.5% of the sample) emerged, with
  the 'Alternating Days' strategy (non-remote couples trading work days and reducing hours)
  best preserving wellbeing and performance for both partners.
claims:
  - text: "Latent class analysis identified 7 work-family strategy classes; 36.6% of couples used gendered strategies where the wife did most/all childcare, 44.5% used novel egalitarian strategies (e.g., alternating days, mini-shifts, need-based alternation), and 18.9% used strategies not clearly gendered or egalitarian."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["work-life-balance"]
    predictors: ["remote-work-intensity", "boundary-management"]
  - text: "Wives in the 'Wife Remote and Does It All' class had the lowest family cohesion, highest relationship tension, and lowest job performance of all classes at Time 2 (7 weeks later); husbands in this class also had the lowest family cohesion and highest relationship tension despite minimally altered work situations."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["performance", "wellbeing", "job-satisfaction"]
    predictors: ["boundary-management", "workload"]
  - text: "Among egalitarian strategies, couples using 'Alternating Days' (neither remote, alternating which spouse works each day, both reducing hours) had the most favorable outcomes overall, including highest sleep and lowest or second-lowest psychological distress for both spouses, outperforming the two remote-work-based egalitarian strategies (planned mini-shifts and need-based alternation)."
    evidence: "longitudinal"
    support_strength: "moderate"
    outcomes: ["wellbeing", "performance", "mental-health"]
    predictors: ["boundary-management", "remote-work-intensity"]
population:
  who: "Married, dual-earner (both full-time) heterosexual couples in the U.S. with at least one child under age 6 whose regular childcare was disrupted by COVID-19 closures"
  where: ["United States"]
  when: "Time 1: March 18-23, 2020; Time 2: May 7-18, 2020"
  n: 274
  sector: ["general-workforce"]
  sample_notes: >
    274 couples (668 individuals) at Time 1, recruited via snowball sampling through
    researchers' networks (n=51) and paid Facebook ads (n=232); 179 couples retained at Time
    2 after attention-check screening, with final outcome analyses on 133-172 couples.
    Sample skewed high-income (mean household income ~$140,700) and was screened to exclude
    same-sex couples and couples suspected of single-respondent or ineligible responses.
limitation:
  primary: "High-income, opposite-sex-couple sample limits generalizability to lower-income workers and to same-sex or non-married couples, who were explicitly excluded."
  others:
    - "Job performance was self-reported, which is prone to inflation and not independently verified."
    - "Findings are specific to the acute, unprecedented context of early COVID-19 shutdowns; generalizability to other crisis or non-crisis contexts is speculative."
    - "Substantial attrition between Time 1 (274 couples) and the final outcome analytic sample (133 couples) could introduce nonresponse bias despite reported non-significant differences on demographics."
risk_of_bias: "medium"
relevance_to_project: >
  Directly evidences how forced full-time remote work reshapes household boundary-management
  strategies and links specific work-family arrangements (not just 'remote work' as a
  monolith) to burnout-adjacent outcomes like psychological distress, relationship tension,
  and performance, informing SNH design questions about which boundary/scheduling patterns
  for remote workers with caregiving duties best protect wellbeing.
tags:
  topic: ["remote-work", "work-life-balance", "wellbeing", "burnout"]
  method: ["survey", "longitudinal"]
  population: ["parents", "dual-earner-couples", "remote-workers"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Work-Family Strategies During COVID-19 Examining Gender Dynamics Among Dual-Earner Couples With Young Children/Work-Family Strategies During COVID-19 Examining Gender Dynamics Among Dual-Earner Couples With Young Children.md"
  pdf: "papers/Academic/01 Academic - Extended/Work-Family Strategies During COVID-19 Examining Gender Dynamics Among Dual-Earner Couples With Young Children.pdf"
  notes: null

---

id: "bonacini-2021-working-from-home-and-income-inequality"
title: "Working from home and income inequality: risks of a ‘new normal’ with COVID-19"
authors:
  - "Bonacini, Luca"
  - "Gallo, Giovanni"
  - "Scicchitano, Sergio"
year: 2021
doi: "10.1007/s00148-020-00800-7"
venue: {type: "journal", name: "Journal of Population Economics", volume: 34, issue: 1, pages: "303-360"}
citation: "Bonacini et al. (2021). Working from home and income inequality: risks of a ‘new normal’ with COVID-19. Journal of Population Economics, 34(1), 303-360. https://doi.org/10.1007/s00148-020-00800-7"
article_type: "empirical"
method: {design: "cross-sectional", approach: "secondary-data", evidence_level: "moderate", preregistered: false}
gist: >
  Using unconditional quantile (RIF) regression on a merged Italian dataset (INAPP-PLUS 2018
  labour survey and the 2013 Italian Survey of Professions), this study estimates how a
  persistent, COVID-19-driven increase in work-from-home (WFH) feasibility would reshape the
  distribution of labour income. Swapping 10 percentage points of employees from low to high
  WFH feasibility raises mean annual income by about EUR 259 (1%) and widens the Gini index
  by about 0.004, with the wage premium concentrated among male, older, and highly-educated
  employees and largest in provinces hardest hit by COVID-19 infection. The paper argues
  that expanding remote work without regulation and compensating policy (income support,
  childcare, human-capital investment) risks deepening existing labour-market inequalities
  rather than being a socially neutral 'new normal.'
claims:
  - text: "A 10-percentage-point shift of employees from low to high WFH feasibility is associated with a mean labour income increase of about EUR 259 (about 1%) and a Gini index increase of about 0.004 (unconditional effect, p<0.05); effects shrink but remain significant on inequality once demographic/job covariates are controlled (unconditional partial effect)."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity"]
  - text: "The wage premium from higher WFH feasibility is highly unequal: it is much larger for male employees (+EUR 473 UE, +EUR 234 UPE) than female (+EUR 111 UE, near-zero/negative UPE), and larger for older (51-64, +EUR 496 UE) and graduated employees (+EUR 411 UE) than for younger/non-graduated employees, with the highest premium (~EUR 500, +1.7%) at the 8th income decile."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity"]
  - text: "Employees in Italian provinces with above-median COVID-19 infection incidence would benefit more from increased WFH feasibility than those in less-infected provinces (mean income effect +EUR 330 vs +EUR 193 unconditional; +EUR 137 vs +EUR 47 with covariates), and an inverse-probability-weighting robustness check confirms high WFH feasibility raises mean income by 3.5% overall, rising to 16.3% at the top decile."
    evidence: "cross-sectional"
    support_strength: "moderate"
    outcomes: ["turnover"]
    predictors: ["remote-work-intensity", "network-structure"]
population:
  who: "Italian employees aged 25-64 (self-employed excluded) drawn from the 2018 INAPP-PLUS labour survey merged with occupation-level WFH feasibility scores from the 2013 Italian Survey of Professions (ICP)"
  where: ["Italy"]
  when: "2018 (INAPP-PLUS survey wave); WFH feasibility index from 2013 ICP survey; COVID-19 infection data 24 Feb-5 May 2020"
  n: 14307
  sector: ["other"]
  sample_notes: >
    INAPP-PLUS is a stratified random CATI survey of ~45,000 working-age Italians per wave;
    analysis sample restricted to employed, non-self-employed individuals aged 25-64 with no
    missing values (14,307 of 45,000). Findings are specific to pre-pandemic Italian labour-
    market structure and a hypothetical 'employee-shares swap' counterfactual, not observed
    post-pandemic outcomes; robustness checks (self-employed included, different thresholds,
    unweighted, IPW) confirm main results.
limitation:
  primary: "The core analysis is a counterfactual simulation (hypothetical swap of shares of employees between WFH feasibility levels using pre-pandemic 2018/2013 data), not a measurement of actual post-pandemic WFH adoption or its realized income effects."
  others:
    - "WFH feasibility is an occupation-level task index (whether a job COULD be done remotely), not actual remote-work status or intensity of individual employees, so it is a proxy rather than a direct measure of remote work."
    - "Findings are specific to the Italian labour market and regulatory context (very low pre-pandemic telework prevalence, ~1%) and may not generalize to countries with different WFH norms or labour institutions."
    - "Analysis excludes self-employed workers and is limited to formally employed workers aged 25-64, omitting groups (students, informal workers, gig workers) that may face different WFH-inequality dynamics."
risk_of_bias: "low"
relevance_to_project: >
  Provides quantitative evidence that expanding remote-work feasibility is not
  distributionally neutral: it systematically advantages male, older, more educated, and
  already higher-paid workers, which is directly relevant to SNH's interest in how
  remote/hybrid work policy can inadvertently widen inequality alongside its social-
  connection effects, and supports the case for pairing remote-work expansion with
  compensating supports (childcare, training) rather than treating WFH access as an
  unambiguous wellbeing win.
tags:
  topic: ["remote-work", "wellbeing"]
  method: ["cross-sectional", "secondary-data"]
  population: ["general-workforce"]
source:
  markdown: "Papers_Data/Academic/01 Academic - Extended/MD/Working from Home and Income Inequality Risks of a New Normal with COVID-19/Working from Home and Income Inequality Risks of a New Normal with COVID-19.md"
  pdf: "papers/Academic/01 Academic - Extended/Working from Home and Income Inequality Risks of a New Normal with COVID-19.pdf"
  notes: null
