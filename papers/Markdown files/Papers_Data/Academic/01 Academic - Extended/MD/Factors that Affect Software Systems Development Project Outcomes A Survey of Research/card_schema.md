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
