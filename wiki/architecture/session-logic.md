# 🔐 Module: Session Logic

## 📜 Overview
Synthesized map of the authentication substrate. This module manages the transition from legacy MD5 hashing to modern SHA-256 standards.

## 🧠 Architectural "Whys" (savwiki)
- **SHA-256 Transition:** The system is in a transition state. MD5 is currently used in the core for backward compatibility.
- **Legacy Mode Guardrail:** The `validateSession` logic is gated by the `legacyMode` toggle in the global configuration. 
- **Drift Discovery:** (Verified 2026-04-15) A discovery via **Munch-Sync Signal** confirmed that `legacyMode` must be explicitly set to `false` in production.

## 📍 Verified Stable IDs
| Entity | Stable ID | Role |
| :--- | :--- | :--- |
| **Validation** | `sample_app/src/core/auth.ts::validateSession#func` | Primary entry point for session checks. |
| **Config** | `sample_app/src/config.ts::globalConfig#const` | Source of truth for `legacyMode` toggle. |

## ⚠️ Known Side Effects (par~mi)
- **Session Invalidation:** Toggling `legacyMode` in `config.ts` will immediately change the validation path in `auth.ts`, potentially invalidating active sessions.

---
[[wiki/index]] | [[GLOSSARY]]
