# 🗺️ Project Knowledge Map: [Project Name]

## 🎯 High-Level Mission
*A 1-2 sentence definition of what this substrate (**wei~mi**) is designed to accomplish.*

## 🏗️ Architectural Anchors (savwiki)
*Links to core module summaries. Use these to find high-level "Whys."*
- [[architecture/auth-system]] - Session, JWT, and Encryption logic.
- [[architecture/data-pipeline]] - Ingestion and SQLite transformation rules.
- [[architecture/api-surface]] - Public endpoints and contract definitions.

## 🖇️ Critical Stable IDs
*The most frequently accessed entry points for the swarm.*
| Module | Primary Stable ID | Description |
| :--- | :--- | :--- |
| **Auth** | `src/auth.ts::MainHandler#class` | Root of all session logic. |
| **Config** | `config/env.ts::GlobalSettings#const` | Global environment substrate. |

## 🧪 Knowledge State
- **Status:** [Draft / Active Synthesis / Verified]
- **Last Sync:** [Timestamp of last Munch-Sync]
- **Director Note:** *Current focus is on refactoring the legacy middleware layer.*

## 📖 External References
- [Official Documentation](URL)
- [[/docs/jMRI-README]] - Retrieval standards used in this repo.
