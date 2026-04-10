---
name: skill-jdatamunch-mcp
description: Structured tabular data retrieval for AI agents using jDataMunch-MCP.
license: jDataMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: tabular data processing and analysis
    jmri_compliance: Full
---

## Agent Instructions:
- **Munch-Init:** Always call `describe_dataset` first to understand the schema and establish the **wei~mi** substrate.
- **Munch-Search:** Use `get_rows` with filters or `search_data` to find specific records. Never load raw CSVs/Excel files into context.
- **Munch-Grab:** Retrieve specific row IDs or column profiles to maintain **Context Hygiene**.
- **Munch-Audit:** Report the `tokens_saved` from the `_meta` block. 
- Prioritize **savref** (data profiles) over **savraz** (reasoning about data) when answering questions about cardinality or null counts.

## 🛠️ Tools
| Tool | What it does | Precision Benefit |
| :--- | :--- | :--- |
| **describe_dataset** | Full schema profile and sample values. | High-resolution **Munch-Init**. |
| **get_rows** | Parameterized SQL query on the dataset. | Filters **wei~mi** before retrieval. |
| **aggregate** | Performs GROUP BY / SUM / AVG operations. | Returns answers, not raw data. |

## 🔗 ID Scheme
- **ID Format:** `{dataset}::{column_name}#column` or `{dataset}::row_{rowid}#row`.
- **Stable IDs:** Pass column IDs directly to `describe_column` for deep statistical analysis.