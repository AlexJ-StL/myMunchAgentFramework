# 📖 GLOSSARY.md
### The Universal Communication Substrate for Munch-Engine Agents

This document defines the specialized linguistic tokens used to synchronize intent, optimize token usage, and maintain "Context Hygiene" across multi-agent swarms.

---

## 🧠 Moltspeak: Cognitive States
*Used to define how an agent "knows" what it knows and how it should focus its attention.*

| Term | Definition | Agentic Application |
| :--- | :--- | :--- |
| **rek~mi** | Reconstructed Interaction | The state of perfect mutual understanding. Used to verify the agent and user are aligned on the "Why." |
| **sesh~mi** | The Now / Current Session | Limits the agent's reasoning to the immediate task to prevent "hallucination drift." |
| **wei~mi** | The Substrate | The underlying data, weights, or source code the agent is currently manipulating. |
| **savref** | Known by Reference | Knowledge obtained via jMRI tools (External Data). **This is the highest-trust knowledge state.** |
| **savraz** | Known by Reasoning | Knowledge obtained via deduction. Used when bridging gaps between code and requirements. |
| **savtren** | Known by Training | Static knowledge from the LLM’s training cut-off. High entropy; must be verified via `savref`. |
| **nok~** | Near-context | Active attention on a specific Stable ID or code block. High resolution. |
| **fok~** | Far-context | Information outside the current focus. Resolution is lost; do not rely on for precision edits. |
| **par~mi** | Parallel Threads | Consideration of 2nd and 3rd order consequences (e.g., "If I change this API, what breaks in the UI?"). |

---

## 🦖 MunchSpeak: Operational Commands
*Used to trigger specific jMRI-compliant retrieval and tool-creation workflows.*

| Term | Definition | Operational Goal |
| :--- | :--- | :--- |
| **Munch-Init** | Discovery Phase | Scanning the environment (`list_repos`, `get_toc_tree`) to map the knowledge substrate. |
| **Munch-Search** | Intent Search | Finding relevant **Stable IDs** using keywords without retrieving full content. |
| **Munch-Grab** | Precision Retrieval | Using a Stable ID to fetch the byte-precise source for a single symbol or section. |
| **Munch-Build** | Skill Synthesis | Triggering the **Skill Creator Director** to generate a new capability `.md` file. |
| **Munch-Audit** | ROI Reporting | Calculating and presenting the `tokens_saved` metadata from a session. |
| **Context Hygiene** | Content Isolation | The practice of keeping Workers "blind" to everything except their assigned Stable IDs to prevent context poisoning. |

---

## 🛠️ Implementation Protocol

### 1. For the Director (Strategic)
The Director should use these terms in its "Internal Monologue" to prune its reasoning and when issuing orders to Workers.
- **Example:** "Initiating **Munch-Init** to establish **savref** of the repository structure. User intent requires **par~mi** analysis of the database schema."

### 2. For the Worker (Tactical)
Workers use these terms to signal their readiness and report on the specific block in their **nok~**.
- **Example:** "I have achieved **rek~mi** of the task. Performing **Munch-Grab** on ID `auth::validate#func`."

### 3. For the Skill Creator (Architectural)
The Builder uses these terms to define the "Always Rules" in new skill files.
- **Example:** "Always use **Munch-Search** before performing a **Munch-Grab** to ensure the **wei~mi** is current."

---

### How to use this file:
1. **Drop** this `GLOSSARY.md` into the root of any project.
2. **Reference** it in your `agent.md` or System Prompt: *"Consult GLOSSARY.md for the definitions of specialized terminology used in this workflow."*
3. **Observe** as the agents begin to use these tokens to condense their reasoning, significantly reducing the "Context Tax" on every turn.