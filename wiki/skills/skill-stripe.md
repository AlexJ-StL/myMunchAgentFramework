\# 🛠️ Skill: skill-stripe



\## 🎯 High-Level Purpose

Provides a jMRI-compliant interface for the Stripe Node.js SDK, specifically optimized for Customer and Subscription management without context window flooding.



\## 🖇️ Primary Stable IDs

| Tool | Primary ID Pattern | Use Case |

| :--- | :--- | :--- |

| \*\*Create Customer\*\* | `stripe::customers#create` | Initializing new user billing. |

| \*\*List Invoices\*\* | `stripe::invoices#list` | Auditing payment history. |



\## 🧠 Strategic Patterns (savwiki)

\- \*\*Idempotency:\*\* Always pass an `idempotency\_key` when using the `create` IDs to prevent double-billing during agent retries.

\- \*\*Verification:\*\* Use the `stripe::customers#retrieve` ID to establish \*\*savref\*\* of a user's status before attempting a subscription update.



\## 🏗️ Evolution \& Sync

\- \*\*Origin:\*\* Generated via `Munch-Build` on 2026-04-11.

\- \*\*Source of Truth:\*\* https://docs.stripe.com/api

\- \*\*Munch-Sync Notes:\*\* \*2026-04-12: Discovered that Stripe IDs starting with `cus\_` must be treated as immutable Stable IDs in the `/wiki/entities` substrate.\*

