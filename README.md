# 🦖 Munch-Engine: The Precision-Retrieval Swarm

**Stop feeding your budget to brute-force AI.** Most agents explore repositories the expensive way: opening entire files, skimming thousands of irrelevant lines, and flooding context windows with noise. This "Naive RAG" approach is slow, costly, and hallucination-prone.

**Munch-Engine** is a recursive, multi-agent framework built on the **jMRI (jMunch Retrieval Interface)** specification. It enables agents to navigate codebases, documentation, and datasets with surgical precision—retrieving only the exact symbols, sections, or rows needed to solve a task.

---

## 💡 The "First Principles" Advantage
This engine is built on three core values to ensure maximum efficiency:
1. **Precision > Volume:** Fetching 20 lines of a specific function is better than reading a 2,000-line file.
2. **Objective ROI:** Every tool call returns a `_meta` block showing exactly how many tokens were saved. 
3. **Autopoietic Growth:** The system automatically builds its own "Skills" (.md files) when it encounters a new API or SDK.

---

## 🏗️ The Architecture (Tiered Agency)
Munch-Engine utilizes a three-tier swarm to separate high-level strategy from tactical execution:

- **The Project Director (Strategic):** The "Brain." Analyzes requests, scans the `/skills` library, and deconstructs goals into symbol-level tasks.
- **The Skill Creator Director (Architectural):** The "Engineer." If a skill is missing, it triggers a **Munch-Build** to ingest documentation and generate a new precision skill on the fly.
- **The Tactical Worker (Execution):** The "Hands." Specialized agents that operate under "Context Hygiene," seeing only the specific code or data blocks they are tasked to modify.

---

## 📈 Performance Benchmarks (Measured Savings)
Precision context consistently beats brute-force context. The following benchmarks represent real-world savings using jMRI retrieval:

| Task | Traditional Approach | Munch-Engine (jMRI) | Savings |
| :--- | :--- | :--- | :--- |
| **Find a specific function** | ~40,000 tokens | ~200 tokens | **99.5%** |
| **Understand Module API** | ~15,000 tokens | ~800 tokens | **94.6%** |
| **Explore Repo Structure** | ~200,000 tokens | ~2,000 tokens | **99.0%** |
| **Doc Reference Search** | ~12,000 tokens | ~400 tokens | **96.6%** |

---

## 🚀 Quickstart: 5 Minutes to ROI
1. **Setup:** Install core jMunch tools: `pip install jcodemunch-mcp jdocmunch-mcp jdatamunch-mcp`.
2. **Initialize:** Point your primary agent to `agent.md` and ensure `GLOSSARY.md` is in the root.
3. **Task:** Give the Director a high-level goal (e.g., *"Refactor the auth logic in this repo using jMRI precision"*).
4. **Audit:** Review the efficiency report at the end of the session to see your total `tokens_saved`.

---

## 🛠️ Substrate & Standards

The Munch-Engine is powered by the **jMRI (jMunch Retrieval Interface)** specification and utilizes the following core MCP servers:

* **Standard:** [jMRI Specification](https://github.com/jgravelle/mcp-retrieval-spec) — The protocol for precision agentic retrieval.
* **Code:** [jCodeMunch-MCP](https://github.com/jgravelle/jcodemunch-mcp) — AST-based symbol indexing.
* **Data:** [jDataMunch-MCP](https://github.com/jgravelle/jdatamunch-mcp) — Tabular data to SQLite transformation.
* **Docs:** [jDocMunch-MCP](https://github.com/jgravelle/jdocmunch-mcp) — Hierarchical documentation mapping.

---

## 📜 Credits & Standards
- **Standard:** [jMRI Specification](https://github.com/jgravelle/mcp-retrieval-spec)
- **Author:** Developed by **AlexJ**, inspired by the precision-retrieval work of **J. Gravelle**.
- **Philosophy:** *"Good communication is efficient AND effective mutual understanding."*