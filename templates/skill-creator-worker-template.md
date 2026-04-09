---
name: skill-[name]
description: [One sentence on what it does]
metadata:
    category: [category]
    jmri_compliance: [Core/Full]
    source: [URL/Path]
---

## 🎯 Protocol (The "Always" Rules)
- Always call [Orientation Tool] before performing [Action].
- Use jMRI Precision: Retrieve by ID `{origin}::{name}#{type}`.

## 🛠️ Tools (jMRI Table)
| Tool | What it does | Precision Benefit |
| :--- | :--- | :--- |
| **[tool_name]** | [functional description] | [e.g., "Saves 90% vs full file read"] |

## 🧪 Acceptance Criteria
- [ ] Agent can retrieve symbol X without reading file Y.
- [ ] Token savings are reported in `_meta`.