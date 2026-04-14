# 🛠️ Core Capabilities: The Munch-Engine Substrate

Welcome to the **Munch-Engine** Core Library. These skills are the "Sensors" and "Actuators" of your swarm, enabling agents to interact with code, data, and documentation with surgical precision. 

In Version 2.0, these skills are no longer just retrieval tools; they are the primary feed for the **Active Synthesis** loop.

## 📦 The Core Triad

| Skill | Primary Goal | v2.0 Synthesis Role |
| :--- | :--- | :--- |
| **jCodeMunch** | Codebase Analysis | Maps raw symbols to **Stable IDs** for the Wiki. |
| **jDocMunch** | Documentation Sync | Reconciles "Official Intent" with "Actual Logic." |
| **jDataMunch** | Tabular Precision | Audits massive datasets and stores insights in the Wiki. |

---

## 🧠 The v2.0 Operational Protocol
Every core skill in this folder follows the **Munch-Engine Relay**:

1. **Munch-Init:** Agents establish **savref** (reference) to the physical files.
2. **Munch-Search/Grab:** Agents isolate the specific logic or data in the **nok~**.
3. **Munch-Sync Signal:** Upon completion, the agent emits an architectural brain-dump.
4. **Wiki-Synthesis:** The **Wiki-Worker** compiles that signal into the `/wiki` substrate.

---

## 🔧 Technical Substrate

### How it Works
- **AST Parsing (jCodeMunch):** Uses Tree-Sitter to build a relational map of code symbols, ensuring IDs remain stable even if lines shift.
- **Hierarchy Awareness (jDocMunch):** Maps Table of Contents to prevent "context poisoning" from unrelated document sections.
- **SQLite Offloading (jDataMunch):** Converts flat files into queryable databases, allowing for high-resolution analysis without flooding the context window.

### Performance Benchmarks (Per Query)
- **Traditional Search:** ~200,000 tokens
- **Munch-Engine v2.0:** ~1,500 tokens
- **Efficiency Gain:** **99.2%**

---

## 🚀 Original Sources & Credits
The underlying MCP servers are open-source and based on the **jMRI (jMunch Retrieval Interface)** specification.

- **jCodeMunch:** [GitHub](https://github.com/jgravelle/jcodemunch-mcp)
- **jDataMunch:** [GitHub](https://github.com/jgravelle/jdatamunch-mcp)
- **jDocMunch:** [GitHub](https://github.com/jgravelle/jdocmunch-mcp)
- **Protocol:** [jMRI Spec](https://github.com/jgravelle/mcp-retrieval-spec)
- **Concept:** Persistence layer inspired by Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## 📜 Agent Compliance
The `.md` files in this folder are **Behavioral Steering Documents**. 
- **DO NOT** add prose or "fluff" to the individual skill files. 
- Use this README for human-facing documentation.
- Maintain **Context Hygiene** by only calling the specific tools required for the task.