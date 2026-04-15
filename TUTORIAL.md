#🚀 Munch-Engine v2.0: 5-Minute Setup & Test

## 1. The Environment
Ensure you have the core triad installed:
```Python
pip install jcodemunch-mcp jdatamunch-mcp jdocmunch-mcp
```

## 2. The First Audit (Munch-Init)
Point your agent to the root folder. Ask:
' "Director, analyze the /sample_app. Establish savwiki from the index and tell me the primary tech debt in the auth module." '

## 3. Observe the Relay
1.  The Director will read `wiki/index.md`.
2.  The Tactical Worker will grab `sample_app/src/core/auth.ts::validateSession#func`.
3.  The Wiki-Worker will flag the `legacyMode` dependency.

## 4. Verify the ROI
Check the Munch-Audit in the final response. You should see a token savings of >90% compared to a full-file read.

---

## 🛠️ Automated Verification
To ensure your environment is audit-ready, run the included utility scripts:
1.  **python `tools/validate_refs.py`:** Ensures all Wiki Stable IDs are physically present in the code.
2.  **python `tools/munch_sync.py` [json_file]:** Simulates the Wiki-Worker's archival process by injecting worker signals into the knowledge base.