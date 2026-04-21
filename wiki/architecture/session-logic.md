\# 🔐 Module: Session Logic



\## 📜 Overview

Handles the lifecycle of user sessions. Recently refactored to remove legacy MD5 hashing in favor of SHA-256 for enhanced security.



\## 🧠 Architectural "Whys" (savwiki)

\- \*\*SHA-256 Transition:\*\* Updated on 2026-04-11. MD5 was previously maintained only for compatibility with the 2018 schema.

\- \*\*Legacy Mode dependency:\*\* The `validate` function relies on `globalConfig.legacyMode`. If enabled, the system bypasses SHA verification. \*\*(Discovered via Munch-Sync Signal)\*\*.



\## 📍 Associated Stable IDs

\- `src/auth/session.ts::validate#func` - Primary validation logic.

\- `src/auth/session.ts::generateHash#func` - Hash generation utility.



\## ⚠️ Known Side Effects (par\~mi)

\- Changing the hashing algorithm will invalidate all active sessions in the Redis store immediately.

\- Dependency on `globalConfig` makes this module sensitive to environment-level toggles.

