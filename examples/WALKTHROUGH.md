# 🚀 Munch-Engine v2.2: Full Loop Walkthrough

**Objective:** Secure the `sample_app` by disabling the legacy bypass and updating the project memory.

### 🏁 Step 1: User Intent
**User:** *"The auditor is worried about the MD5 bypass. Disable `legacyMode` in the config and make sure the Wiki reflects that SHA-256 is now mandatory."*

### 🧠 Step 2: Director Orchestration (savwiki)
The **Director** establishes the mental model by checking the `/wiki`.
- **Call:** `read_wiki_page(path="wiki/architecture/session-logic.md")`
- **Insight:** Identifies the target: `sample_app/src/config.ts::globalConfig#const`.

### 🛠️ Step 3: Tactical Execution (savref)
The **Tactical Worker** is dispatched to the specific Stable ID.
- **Call:** `jcodemunch::get_symbol(id="sample_app/src/config.ts::globalConfig#const")`
- **Action:** Updates `legacyMode: true` to `false`.
- **Signal Emission:**
	```json
	[MUNCH-SYNC-SIGNAL]
	{
		"target": "wiki/architecture/session-logic.md",
		"stable_id": "sample_app/src/config.ts::globalConfig#const",
		"insight": "legacyMode disabled in config.ts.",
		"par_mi": "MD5 bypass is now impossible; all auth paths default to SHA-256."
	}
	[/MUNCH-SYNC-SIGNAL]
	```

### 📚 Step 4: Knowledge Synthesis (Munch-Sync)
The **Director** detects the JSON block and tasks the `Wiki-Worker`.
- **Action:** Wiki-Worker parses the JSON and updates wiki/architecture/session-logic.md.
- **Result:** Synthesis Receipt Issued. "Page updated. Logic Drift resolved."

📊 Step 5: Final Audit
- **Tokens Used:** 2,150 (Total swarm overhead).
- **Manual Scan Baseline:** ~65,000 tokens.
- **Outcome:** Substrate secured. Memory updated. rek~mi achieved.