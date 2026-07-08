id: "riehle-2012-the-single-vendor-commercial-open-course"
title: "The single-vendor commercial open course business model"
authors:
  - "Riehle, Dirk"
year: 2012
doi: "10.1007/s10257-010-0149-x"
venue: {type: "journal", name: "Information Systems and e-Business Management", volume: 10, issue: 1, pages: "5-17"}
citation: "Riehle (2012). The single-vendor commercial open course business model. Information Systems and e-Business Management, 10(1), 5-17. https://doi.org/10.1007/s10257-010-0149-x"
article_type: "theory"
method: {design: "theory", approach: "secondary-data", evidence_level: "weak", preregistered: false}
gist: >
  Riehle synthesizes public statements, interviews, and presentations by practitioners at
  single-vendor commercial open source firms (e.g., MySQL, SugarCRM, Jaspersoft, Alfresco)
  into a comprehensive account of how such firms build and monetize an open source project
  they alone control. The central argument is that an engaged, self-supporting user
  community is the core business asset: it lowers customer acquisition cost, produces
  credible peer marketing, feeds product and engineering innovation, and absorbs most
  support burden through community self-help, all while the firm withholds full utility or
  operational comfort for paying customers. For SNH, the paper is a firm-level account of
  how organizations deliberately cultivate community engagement and peer support as a
  commercial resource, illuminating the incentive structures maintainer communities operate
  under.
claims:
  - text: "Conversion rates from non-paying open source user to paying customer are commonly only 0.5-2% for single-vendor commercial open source firms, per practitioner-reported figures (Taylor 2009), meaning the vast majority of the engaged community never becomes a revenue source."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["customer-conversion"]
    predictors: ["community-engagement"]
  - text: "Reliance on a self-supporting community substantially lowers a firm's support costs: engaged non-paying users build and maintain documentation, wikis, and peer knowledge bases, and increasingly resolve problems via search before ever contacting paid support, shifting the support burden away from the commercial firm."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["help-seeking", "collaboration"]
    predictors: ["community-engagement", "peer-mentoring"]
  - text: "Estimated sales-and-marketing-to-R&D expense ratios are much lower for commercial open source firms than for traditional vendors -- roughly 0.6 for a hypothetical open source CRM vendor versus 2.3 typical for traditional software firms and 6 for proprietary competitor Salesforce -- attributed to community members providing free, credible word-of-mouth marketing."
    evidence: "theory"
    support_strength: "weak"
    outcomes: ["productivity"]
    predictors: ["community-engagement", "open-source-maintenance"]
population:
  who: "Single-vendor commercial open source software firms and their user/developer communities (e.g., MySQL, SugarCRM, Jaspersoft, Alfresco), characterized through public interviews, conference presentations, and industry reports by practitioners and analysts (2005-2009)."
  where: []
  when: "2005-2009 (source statements); published 2010"
  n: null
  sector: ["technology", "open-source"]
  sample_notes: >
    Not a systematic empirical study: the author compiled anecdotal public statements,
    interviews, and presentations by open source business practitioners and industry
    analysts (Gartner, IDC, FLOSSmetrics), then synthesized them into a descriptive
    framework. No sampling frame, response rate, or primary data collection is reported; a
    handful of named firms serve as illustrative examples throughout.
limitation:
  primary: "The paper is a narrative synthesis of anecdotal practitioner statements and presentations rather than systematic empirical research, so its claims (conversion rates, cost ratios, causal community benefits) lack controlled measurement, sampling rigor, or statistical validation."
  others:
    - "Focuses exclusively on single-vendor commercial firms, so findings about community dynamics may not generalize to volunteer-governed community open source projects."
    - "Now over a decade old (published 2010, sources from 2005-2009); the commercial open source landscape and business models have evolved substantially since."
    - "The author acknowledges no prior comprehensive reference existed, underscoring the exploratory, non-cumulative nature of the evidence base."
risk_of_bias: "high"
relevance_to_project: >
  Documents the incentive structure firms use to cultivate engaged, self-supporting open
  source communities -- treating community peer-support and word-of-mouth engagement as a
  deliberate cost-saving business strategy. This is directly relevant to SNH's interest in
  open-source maintainer and contributor dynamics: it frames community engagement and help-
  seeking behavior as something organizations actively design for and extract value from,
  which has implications for maintainer workload and burnout risk when 'self-supporting'
  communities under-deliver.
tags:
  topic: ["open-source", "community-health", "maintainer-burnout", "collaboration"]
  method: ["theory", "secondary-data"]
  population: ["open-source-firms", "software-industry"]
source:
  markdown: "Papers_Data/Articles/01 Articles - Extended/MD/The Single-Vendor Commercial Open Source Business Model/The Single-Vendor Commercial Open Source Business Model.md"
  pdf: "papers/Articles/01 Articles - Extended/The Single-Vendor Commercial Open Source Business Model.pdf"
  notes: null
