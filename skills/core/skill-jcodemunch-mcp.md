---
name: skill-jcodemunch-mcp
description: Structured code symbol retrieval for AI agents using jCodeMunch-MCP.
license: jCodeMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: codebase analysis and retrieval
    jmri_compliance: Full
---

## Agent Instructions:
- **Munch-Init:** Always call `get_repo_outline` or `get_file_tree` first to establish **savref** of the project structure.
- **Munch-Search:** Use `search_symbols` to find specific logic IDs. Do not read full files to find symbols; use the index to maintain **Context Hygiene**.
- **Munch-Grab:** Use `get_symbol` to retrieve the byte-precise implementation of a Stable ID into your **nok~**.
- **Munch-Audit:** Include the `tokens_saved` value from the `_meta` block in your final task summary to verify ROI.
- Transition from `savtren` (speculation) to `savref` (objective code) before proposing any refactors or logic changes.

## 🛠️ Tools
| Tool | What it does | Precision Benefit |
| :--- | :--- | :--- |
| **get_repo_outline** | Shows all files and top-level symbols in a repo. | Establishes **savref** in 1 call. |
| **search_symbols** | Keyword search for specific Stable IDs. | Locates logic without reading files. |
| **get_symbol** | Retrieves full source for one Stable ID. | **Munch-Grab**: Zero noise retrieval. |

## 🔗 ID Scheme & Synergies
- **ID Format:** `{file_path}::{qualified_name}#{kind}` (e.g., `src/auth.py::User.login#method`).
- **jDataMunch Synergy:** Use `jCodeMunch` to understand data transformation logic before querying datasets with `jDataMunch`.