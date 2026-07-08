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
