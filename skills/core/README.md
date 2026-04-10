# 🛠️ Core Capabilities (jMRI Swarm)

Welcome to the **Munch-Engine** Core Library. These skills enable your agents to interact with the physical world of code, data, and documentation with surgical precision.

## 📦 The Core Triad

| Skill | Primary Goal | Human ROI |
| :--- | :--- | :--- |
| **jCodeMunch** | Codebase Analysis | Stop paying for AI to read thousands of lines of irrelevant code. |
| **jDocMunch** | Documentation Sync | Ensure agents follow author-intended patterns, not generic guesses. |
| **jDataMunch** | Tabular Precision | Query massive CSVs or Excel files without crashing the context window. |

---

## 🔧 Technical "How It Works"

### The jMRI Loop
Every core skill in this folder is designed to follow the **Munch-Init -> Munch-Search -> Munch-Grab** loop.
- **AST Parsing:** jCodeMunch uses Tree-Sitter to build a relational map of your code symbols.
- **Hierarchy Awareness:** jDocMunch maps the table of contents to prevent "context poisoning."
- **SQLite Offloading:** jDataMunch converts raw files into a local SQLite database, allowing the agent to "query" data rather than "reading" it.

### Performance Benchmarks
*Tested on a repository with 300+ files:*
- **Traditional Search:** ~200k tokens per query.
- **Munch-Engine Search:** ~2k tokens per query.
- **Efficiency Gain:** **99.0%**

---

## 🚀 Installation & Setup

Before your agents can use these skills, you must install the underlying MCP servers on your local machine:

```bash
# Install the core triad
pip install jcodemunch-mcp jdocmunch-mcp jdatamunch-mcp

# Optional: Excel support for jDataMunch
pip install "jdatamunch-mcp[excel]"

---

## 🔗 Original Sources
For detailed technical documentation, issue tracking, and implementation details of the underlying servers, visit the official GitHub repositories:

- **jCodeMunch:** [jCodeMunch-MCP](https://github.com/jgravelle/jcodemunch-mcp)
- **jDataMunch:** [jDataMunch-MCP](https://github.com/jgravelle/jdatamunch-mcp)
- **jDocMunch:** [jDocMunch-MCP](https://github.com/jgravelle/jdocmunch-mcp)
- **Protocol:** [jMRI Spec](https://github.com/jgravelle/mcp-retrieval-spec)