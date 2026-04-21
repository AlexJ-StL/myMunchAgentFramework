myMunchAgentFramework/

├── agents.md                   				<-- The Universal Template (Identity \& Process)

├── GLOSSARY.md                 				<-- The Rosetta Stone (v2.0: savwiki, Munch-Sync)

├── README.md                   				<-- The Front Door

│

├── /wiki                       					<-- THE KNOWLEDGE ENGINE (Karpathy Pattern)

│   ├── index.md                				<-- The high-level map of the project

│   ├── architecture/           				<-- Compiled module dependencies \& "Whys"

│   ├── entities/               				<-- Insights on specific data/objects

│   └── roadmap.md              			<-- Persistent tracking of system evolution

│

├── /prompts                    				<-- Instructional Anchors

│   ├── director-prompt.md      			<-- v2.0: Prioritizes savwiki over savref

│   ├── worker-prompt.md        			<-- v2.0: Triggers Munch-Sync upon task completion

│   ├── builder-prompt.md       			<-- Skill Factory logic

│   ├── wiki-worker-prompt.md   		<-- NEW: Specialized agent for wiki synthesis

│   └── skill-director-prompt.md			<-- Architectural: The Gatekeeper logic for new skills

│

├── /skills                     					<-- The Capability Substrate

│   ├── core/							<-- Native jMRI-Wiki Skills

│   │   ├── skill-munch-wiki.md 			<-- NEW: Tooling for reading/writing the Wiki

│   │   ├── skill-jcodemunch-mcp.md

│   │   ├── skill-jdatamunch-mcp.md

│   │   └── skill-jdocmunch-mcp.md

│

├── /examples                   				<-- Playbooks for the swarm

└── /docs                       					<-- Technical deep-dives

