# 📖 Playbook 01: The Surgical Repo Refactor
**Objective:** Update a specific configuration value (Legacy Mode) across the codebase without redundant searching.
**Target Substrate:** `/sample_app` (The Verified Substrate).
**Logic:** Prioritize **savwiki** over **savref** to achieve maximum ROI.

## 📥 The Intent
**User:** *"I need to disable the legacy mode in our configuration to ensure we are using modern SHA-256 validation. Update the value and let me know the impact."*

## 🧠 Agentic Monologue (The "Thought" Process)

### Phase 1: Munch-Init (Wiki-First Discovery)
**Director:** "Establishing savwiki by checking the project memory. I am looking for the location of the legacy configuration toggle."
**Action:** read_wiki_page(path="wiki/index.md")
**Result:** Found link to [[architecture/session-logic]].
**Action:** read_wiki_page(path="wiki/architecture/session-logic.md")
**Result:** Wiki Verified. "Legacy Mode is controlled in sample_app/src/utils/config.ts via the legacyMode property."

### Phase 2: Munch-Grab (Tactical Isolation)
**Director:** "Executing a surgical strike. I am providing the Tactical Worker with the exact Stable ID found in the Wiki. No repository-wide search required."
**Action:** `jcodemunch::get_symbol(id="sample_app/src/utils/config.ts::globalConfig#const")`
**Worker nok~ (Near-context):**
```TypeScript
export const globalConfig = {
version: "1.0.0",
legacyMode: true, // <--- Targeted for refactor
environment: "development"
};
```

### Phase 3: The Relay & Munch-Sync
**Tactical Worker:** "Refactor complete. Value changed to `false`. I am emitting a **Munch-Sync Signal** because I've identified that this change will now enforce hash validation in `auth.ts`."
* **Signal:** 
    ```
    [MUNCH-SYNC-SIGNAL]
    Target: wiki/architecture/session-logic.md
    Context: legacyMode is now FALSE. SHA-256 validation is strictly enforced.
    [/MUNCH-SYNC-SIGNAL]
    ```

## 📤 The Result
**Munch-Director:** "Legacy mode has been disabled in `sample_app/src/utils/config.ts`. The system will now default to SHA-256 validation for all sessions."

## 📊 Munch-Audit (ROI Report)
**Method:** Wiki-First Relay Protocol.
**Tokens Used:** 1,450.
**Naive Baseline:** ~50,000 tokens (Scanning entire `/src` and `/utils` folders).
**Savings:** 48,550 tokens (97.1% ROI).
**Status:** rek~mi achieved via Synthesis.
