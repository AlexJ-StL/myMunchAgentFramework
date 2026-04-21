\# 📖 Playbook 2.0: The Persistent Knowledge Relay



* \*\*Objective:\*\* Investigate a legacy module, refactor a function, and "compile" the newly discovered architectural rules into the Wiki.
* \*\*Swarm:\*\* Munch-Director, Tactical Worker, Wiki-Worker.
* \*\*Substrate:\*\* `src/legacy-auth/` and `/wiki/architecture/`.



\---



\## 📥 The Intent



* \*\*User:\*\* "How does the session validation work in the legacy auth module? If it's still using the old MD5 hash, update it to SHA-256, and make sure we don't forget why we made this change."



\---



\## 🧠 Phase 1: Wiki-First Discovery (savwiki)



* \*\*Munch-Director:\*\* "Checking the knowledge substrate before touching the code. I am looking for existing insights on the legacy auth module."

  * \*\*Action:\*\* `read\_wiki\_page(path="wiki/architecture/auth-overview.md")`
  * \*\*Result:\*\* Wiki Found. "The wiki notes that legacy auth is a 'high-fragility zone' with a custom timeout logic at `src/legacy-auth/session.ts::validate#func`."
  * \*\*ROI:\*\* Discovery phase completed in 400 tokens (vs. 15k to scan the folder).



\---



\## 🛠️ Phase 2: Tactical Execution (savref)



* \*\*Munch-Director:\*\* "Providing the Tactical Worker with the Stable ID found in the Wiki. Mandating Context Hygiene."

  * \*\*Tactical Worker Action:\*\* `jcodemunch::get\_symbol(id="src/legacy-auth/session.ts::validate#func")`
  * \*\*Discovery:\*\* The worker notices that while the hash is MD5, there is a hidden dependency on an external `globalConfig` object not mentioned in the Wiki.
  * \*\*Execution:\*\* Updates MD5 to SHA-256.
  * \*\*Munch-Sync Signal:\*\* "CRITICAL: `validate` function has a side-effect dependency on `globalConfig.legacyMode`. If this is toggled, SHA-256 will fail. MD5 was used previously for compatibility with the 2018 database schema."



\---



\## ✍️ Phase 3: The Knowledge Sync (Munch-Sync)



* \*\*Munch-Director:\*\* "Signal received. Tactical task complete. Handing off to the Wiki-Worker to update our Long-Term Memory."

  * \*\*Wiki-Worker Action:\*\* `update\_wiki\_page(path="wiki/architecture/auth-overview.md")`
  * \*\*Update: \*\*- Adds the new SHA-256 requirement.

    * Documents the `globalConfig.legacyMode` dependency.
    * Links the 2018 Database Schema context to the page.



\---



\## 📤 The Result



* \*\*Munch-Director:\*\* "Task complete. The session validation has been upgraded. More importantly, the Munch-Wiki now contains the 'Why' behind the MD5 choice and the new SHA-256 logic."



\---



\## 📊 Munch-Audit (Version 2.0 ROI)



* \*\*Method:\*\* Wiki-Relay Protocol.
* \*\*Total Tokens:\*\* 3,200.
* \*\*Persistence:\*\* Knowledge is now 'Compiled'. The next time an agent enters this module, it will have savwiki of the `globalConfig` dependency immediately.
* \*\*Status:\*\* \*\*rek\~mi\*\* achieved across code and memory.



\---



\## 🛠️ Key Takeaways for Version 2.0



* \*\*The Shortcut:\*\* Because the Director checked the Wiki first, it knew exactly which function to hit without a single "Search" call.
* \*\*Institutional Memory:\*\* The "Hidden Dependency" found by the worker is no longer hidden. It is now part of the repository's permanent knowledge base.
* \*\*Pipelining:\*\* The Tactical Worker didn't get bogged down in documentation; it just "Signaled," and the Archivist handled the rest.

