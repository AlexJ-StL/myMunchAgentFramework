# 📖 Playbook 01: The Surgical Repo Refactor

* **Objective:** Change a specific configuration value across a multi-module repository without reading every file.
* **Target Substrate:** A TypeScript/Node.js backend repository with 150+ files.
* **Total Tokens Saved:** ~148,000 (98.6% ROI).

---

## 📥 The Intent

**User:** "I need to update our JWT session timeout from 1 hour to 24 hours. I think it's defined as a constant somewhere, but I'm not sure where."

---

## 🧠 Agentic Monologue (The "Thought" Process)

### Phase 1: Munch-Init (Discovery)
	
* **Director:** I have received the intent to update the JWT timeout. I am establishing savref of the repository structure to locate the configuration constants. I am ignoring savtren (training data) regarding common file names to ensure I don't guess."
	* **Action:** jcodemunch::get_repo_outline()
	* **Result:** Identifies src/config/, src/auth/, and src/middleware/ as high-probability zones.

### Phase 2: Munch-Search (The Strike Zone)

* **Director:** "Searching the wei~mi for 'JWT' and 'TIMEOUT' symbols. I am looking for a Stable ID."
	* **Action:** jcodemunch::search_symbols(query="JWT_EXPIRY")
	* **Result:** Found src/config/auth-constants.ts::JWT_EXPIRY#variable.

### Phase 3: Munch-Grab (Tactical Isolation)

* **Director:** "Handing off to a Tactical Worker. Establishing Context Hygiene by providing only the Stable ID. Initiating Munch-Grab."
	* **Worker Action:** jcodemunch::get_symbol(id="src/config/auth-constants.ts::JWT_EXPIRY#variable")
	* **Worker nok~ (Near-context):**
		```typescript
		export const JWT_EXPIRY = 3600; // 1 hour in seconds
		```

---

## 📤 The Result

**Tactical Worker:** "I have updated the JWT_EXPIRY constant to 86400 (24 hours). I verified that no other symbols in the file were affected, maintaining the integrity of the 'wei~mi'."

---

## 📊 Munch-Audit (ROI Report)

* **Method:** jMRI Precision Retrieval.
* **Tokens Used:** 1,850.
* **Naive Baseline:** ~140,000 tokens (Reading all files in src/).
* **Savings:** 138,150 tokens.
* **Status:** rek~mi achieved.

---

## 🛠️ Key Takeaways for the User

1. **No Guessing:** The agent never opened README.md or package.json to find the constant; it went straight to the AST symbol.
2. **Context Hygiene:** The Worker never saw the database passwords or API routes in the same folder, preventing context poisoning.
3. **Speed:** The entire operation took seconds because the LLM didn't have to process 2MB of text.