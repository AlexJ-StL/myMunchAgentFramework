# 📖 Playbook 01: The Surgical Repo Refactor (v2.1 Verified)

**Objective:** Disable Legacy Mode to enforce SHA-256 validation.
**Target Substrate:** `/sample_app/src/utils/config.ts`
**ROI Logic:** Prioritize **savwiki** to avoid repository-wide scanning.

## 🧠 The jMRI Loop

### Phase 1: Munch-Init (Wiki-First)
**Director:** "Checking `wiki/architecture/session-logic.md` for the configuration anchor."
- **Result:** Found Stable ID: `sample_app/src/utils/config.ts::globalConfig#const`.

### Phase 2: Munch-Grab (Tactical Isolation)
**Director:** "Handing off to Tactical Worker. Initiating Munch-Grab on the Stable ID."
- **Worker Action:** `jcodemunch::get_symbol(id="sample_app/src/utils/config.ts::globalConfig#const")`
- **Context (nok~):** `legacyMode: true` identified.

### Phase 3: Execution & Sync
**Worker:** "Updating `legacyMode` to `false`. Emitting mandatory signal."
- **Signal:** [MUNCH-SYNC-SIGNAL]
  Target: wiki/architecture/session-logic.md
  Insight: legacyMode is now FALSE. SHA-256 is enforced.
  [/MUNCH-SYNC-SIGNAL]

## 📊 Munch-Audit
- **Tokens Used:** 1,200
- **Tokens Saved:** 48,800 (vs. Naive Scan)
- **Status:** rek~mi achieved.
