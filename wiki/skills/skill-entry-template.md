\# 🛠️ Skill: \[Skill Name]



\## 🎯 High-Level Purpose

\*Explain what this skill allows the swarm to do that it couldn't do before (e.g., "Enables precision interaction with the Twilio SMS API").\*



\## 🖇️ Primary Stable IDs

\*List the most important entry points for this skill. This allows the Director to find them via \*\*savwiki\*\*.\*

| Tool | Primary ID Pattern | Use Case |

| :--- | :--- | :--- |

| \*\*Send SMS\*\* | `twilio::messages#create` | Outbound notifications. |

| \*\*Lookup\*\* | `twilio::numbers#get` | Verifying carrier data. |



\## 🧠 Strategic Patterns (savwiki)

\- \*\*Error Handling:\*\* \*Describe how this skill handles failures (e.g., "Always check `status\_code` 400 before retrying").\*

\- \*\*Context Limits:\*\* \*Note any specific constraints (e.g., "Do not fetch more than 50 message logs at once").\*



\## 🏗️ Evolution \& Sync

\- \*\*Origin:\*\* Generated via `Munch-Build` on \[Date].

\- \*\*Source of Truth:\*\* \[Link to Documentation URL or /docs/ file].

\- \*\*Munch-Sync Notes:\*\* \*Keep a log of architectural discoveries made while using this skill.\*



\---

\[\[/wiki/index]] | \[\[/skills/core/README]]

