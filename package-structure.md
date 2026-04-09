/munch-engine
├── README.md               <-- The "Front Door": ROI, Quickstart, and Workflow Diagrams
├── GLOSSARY.md             <-- The Rosetta Stone: Definitions for Moltspeak & MunchSpeak
├── agent.md                <-- The Universal Template (Identity & Cognitive Process)
│
├── /prompts                <-- The "Instructional Anchors" (System Prompts)
│   ├── director-prompt.md  <-- Strategic: Deconstruction & Delegation logic
│   ├── worker-prompt.md    <-- Tactical: Precision execution & Context Hygiene
│   ├── builder-prompt.md   <-- Skill Factory: Auto-generation of new .md skills
│   └── skill-director.md   <-- Architectural: The Gatekeeper logic for new skills
│
├── /skills                 <-- The "Capability Substrate"
│   ├── /core               <-- Native jMRI Skills
│   │   ├── skill-jcodemunch-mcp.md
│   │   ├── skill-jdocmunch-mcp.md
│   │   └── skill-jdatamunch-mcp.md
│   ├── /standard           <-- Non-jMRI but essential (Git, Docker, Ansible, etc.)
│   └── /generated          <-- Output folder for the Builder Worker
│
├── /templates              <-- Blueprints for the Skill Factory
│   └── skill-formula.md    <-- The empty jMRI-compliant rubric for new skills
│
└── /docs                   <-- Technical deep-dives
    └── jMRI-spec.md        <-- Local copy of the jMunch Retrieval Interface spec