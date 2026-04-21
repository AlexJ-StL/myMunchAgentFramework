---
name: skill-munch-wiki
description: Autonomous maintenance and synthesis of the project's LLM Wiki (Knowledge Engine).
metadata:
    category: knowledge synthesis and persistence
    jmri_compliance: Full (Synthetic)
---

## Agent Instructions:
- **The Core Goal:** Maintain a persistent, interlinked Markdown Wiki in the `/wiki` directory that "compiles" raw data into high-level context.
- **Munch-Init:** Before searching raw code or docs, check `/wiki/index.md` or `/wiki/map.md` to establish **savwiki** (synthesized knowledge).
- **Munch-Sync:** At the conclusion of any task where new architectural or logic insights were gained via `jCodeMunch` or `jDocMunch`, you MUST update the relevant wiki pages.
- **Context Hygiene:** Do not duplicate raw source code in the wiki. Use the wiki to store **Stable IDs**, architectural "Whys," and cross-module dependencies.
- **Munch-Grab:** Retrieve specific wiki pages to skip expensive repository-wide discovery phases.

## 🛠️ Tools
| Tool | What it does | Precision Benefit |
| :--- | :--- | :--- |
| **read_wiki_page** | Fetches the content of a specific .md file in `/wiki`. | Instant **savwiki** without discovery. |
| **update_wiki_page** | Appends or revises knowledge based on new findings. | Persistent synthesis (Karpathy Pattern). |
| **create_wiki_link** | Generates interlinks between pages and Stable IDs. | Associative trails between docs/code. |

## 🧠 The Synthesis Protocol
1. **Extraction:** After a code refactor, extract the "Second Order Consequences" (**par~mi**).
2. **Reconciliation:** If new code contradicts a wiki page, update the wiki and note the "Logic Drift."
3. **ID Mapping:** Always include the relevant jMRI Stable IDs (e.g., `src/auth.ts::login#func`) in the wiki page so the next agent can perform a **Munch-Grab** instantly.

## 🔗 Synergies
- **jCodeMunch:** Use the Wiki to store the "Mental Model" of complex classes.
- **jDocMunch:** Use the Wiki to bridge the gap between "Official Docs" and "Actual Implementation."
- **jDataMunch:** Use the Wiki to store persistent row IDs and data-audit results.