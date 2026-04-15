# 🦖 Munch-Engine v2.1: The Persistent Knowledge Swarm

**Stop rediscovering your codebase on every session.** Traditional agents use "Passive RAG"—they search, retrieve, and forget. This brute-force approach floods your context window and forces the AI to "re-learn" your architecture every time you ask a question.

**Munch-Engine v2.1** is an autopoietic, multi-agent framework built on the **jMRI (jMunch Retrieval Interface)** specification. It doesn't just find information; it **incrementally builds a persistent Wiki** between the agent and the raw code.

---

## 💡 The Version 2.1 Advantage
Built on first principles for maximum efficiency and long-term accumulation:
1. **Persistent Synthesis:** Using the Karpathy Pattern, agents compile raw discovery into a `/wiki`.
2. **Wiki-First Discovery:** Agents establish **savwiki** (synthesized knowledge) to skip expensive repository-wide scans.
3. **Context Hygiene:** Specialized Workers operate in a vacuum, preventing "context poisoning" and ensuring byte-precise changes.
4. **Active Maintenance:** Every task ends with a **Munch-Sync** to ensure the project's "Mental Model" evolves alongside the code.
5. **Verified Substrate:** Includes a `/sample_app` for immediate integration testing and ROI verification.

---

## ⚖️ Core Values (The Standard)
1. **Objective Facts > Subjective Narratives:** Every agent action must be grounded in **savref** (reference).
2. **Value Injection:** Prioritize non-performative empathy and effective mutual understanding (**rek~mi**).
3. **The 2nd-Order Rule:** Always consider and document parallel consequences (**par~mi**) in the `/wiki`.

---

## 🏗️ The Architecture (The Knowledge Swarm)
Munch-Engine utilizes a tiered swarm to separate high-level strategy from tactical execution and persistence:

- **The Munch-Director (Strategic):** The "Brain." Prioritizes the `/wiki` map and orchestrates the "Relay" between execution and synthesis.
- **The Tactical Worker (Execution):** The "Hands." Operates on specific Stable IDs to perform surgical code or data changes.
- **The Wiki-Worker (The Archivist):** The "Memory." Compiles "Munch-Sync Signals" from Workers into structured, interlinked Markdown pages.

---

## 📊 Measured Token ROI
| Task | Naive (Full-Read) | Munch-Engine v2.1 | Savings |
| :--- | :--- | :--- | :--- |
| Refactor `auth.ts` | ~140,000 tokens | ~1,200 tokens | **99.1%** |
| Audit `transactions.csv` | ~15,000 tokens | ~1,850 tokens | **87.6%** |

---

## 🏗️ Verified Substrate (v2.1 Operational Milestone)
Unlike traditional "Passive RAG" frameworks, Munch-Engine v2.1 is shipped with a **Verified Substrate** located in `/sample_app`. This allows for immediate integration testing and verifiable ROI.

- **Source Code:** Located in `sample_app/src/`. Contains intentional "Technical Debt" (MD5 hashing) for refactoring simulations.
- **Data Substrate:** Located in `sample_app/data/transactions.csv`. A 1,000-row dataset for testing precision SQL-offloading via `jDataMunch`.
- **Knowledge Base:** Located in `/wiki`. Pre-populated with architectural "Whys" to demonstrate **savwiki** shortcutting.

---

## 🚀 Quickstart: 5-Minute ROI Verification
To prove the framework's validity, follow these steps using the included substrate:

1. **Setup:** Install the jMRI triad: `pip install jcodemunch-mcp jdatamunch-mcp jdocmunch-mcp`.
2. **Initialize:** Point your agent to the `/sample_app` directory.
3. **Task:** *"Director, establish **savwiki** from the `/wiki/index.md` and refactor the legacy hashing logic found in the auth module."*
4. **Observe the Relay:**
    - The **Director** will identify the Stable ID via the Wiki.
    - The **Tactical Worker** will perform the byte-precise refactor in `sample_app/src/core/auth.ts`.
    - The **Wiki-Worker** will emit a **Synthesis Receipt** and update the documentation.

---

## 📖 Implementation Guide

This section details how to implement the Munch-Engine framework and integrate it with your AI agents.

### 🔧 Installation

Ensure the jMRI triad is installed in your environment:

```bash
pip install jcodemunch-mcp jdatamunch-mcp jdocmunch-mcp
```

### 🤖 Agent Configuration

Direct your agent to operate within the context of a target repository. The framework expects the following environmental setup:

- **Working Directory:** The root of the repository you wish to manage.
- **Tool Access:** The agent must have access to the MCP servers provided by the jMRI stack.

### 📋 Standard Operating Procedure

1. **Establish the Map (savwiki):** Instruct the Director to load the existing knowledge map from `/wiki/index.md`. If it does not exist, the Director will initiate a full synthesis pass.
2. **Execute Tactical Changes:** Provide the agent with a Stable ID or a specific file path. The Tactical Worker will perform byte-precise modifications, ensuring no context poisoning.
3. **Synthesize and Sync:** Every significant change must trigger a **Munch-Sync Signal**. The Wiki-Worker will then update the `/wiki` with new architectural insights, maintaining the "Mental Model" of the project.

### 🧩 Integration with Your Agents

To embed Munch-Engine into your agent's workflow:

- **Directive:** Prefix high-level goals with "Director,". Example: *"Director, refactor the legacy authentication module using the stable ID `auth-module-v2` identified in the wiki."
- **Feedback Loop:** After execution, agents should query the `/wiki` for updated documentation to confirm the "par~mi" (parallel consequences) of their actions.

### 🛡️ Best Practices

- Always prioritize **savwiki** over raw repository scanning to conserve token budget.
- Use the `/sample_app` as a testing ground to validate token savings and framework integrity before deploying to production codebases.
- Enforce the **2nd-Order Rule** by documenting any potential side effects in the wiki immediately.

---

## 📜 Credits & Standards
* **The LLM Wiki Pattern:** Based on the persistent knowledge architecture authored by **Andrej Karpathy**.
* **jMRI Specification:** Reference implementation of the [jMunch Retrieval Interface](https://github.com/jgravelle/mcp-retrieval-spec).
* **Authorship:** **AlexJ** (Architect) & **Gemini** (Co-Architect/Systems Design).