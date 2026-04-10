---
name: skill-jdocmunch-mcp
description: Structured documentation retrieval for AI agents using jDocMunch-MCP.
license: jDocMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: documentation analysis and retrieval
    jmri_compliance: Full
---

## Agent Instructions:
- **Munch-Init:** Always call `get_toc_tree` or `get_document_outline` first to establish the documentation hierarchy.
- **Munch-Search:** Use `search_sections` to find relevant explanation blocks without reading the entire document.
- **Munch-Grab:** Retrieve specific sections via `get_section` to ensure your focus remains in the **nok~**.
- **Context Hygiene:** If a section is ambiguous, use `get_section_context` to see immediate parents/children rather than the whole file.
- **Synergy:** Prioritize documentation (**savref**) over code analysis when asked "How do I use X" to ensure implementation follows the author's intent (**rek~mi**).

## 🛠️ Tools
| Tool | What it does | Precision Benefit |
| :--- | :--- | :--- |
| **get_toc_tree** | Shows the full heading hierarchy of a repo. | Maps the **fok~** instantly. |
| **search_sections** | Semantic search for specific documentation IDs. | Locates "How-To" blocks with 0 fluff. |
| **get_section** | Fetches the content of a single Stable ID. | **Munch-Grab**: Isolated context. |

## 🔗 ID Scheme
- **ID Format:** `{repo}::{doc_path}::{ancestor-chain/slug}#{level}`.
- **jCodeMunch Synergy:** Use `jDocMunch` to find architectural "Whys" when `jCodeMunch` shows confusing implementation "Hows."