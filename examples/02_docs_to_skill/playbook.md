# 📖 Playbook 02: The Autopoietic Skill Factory

* **Objective:** Automatically generate a jMRI-compliant skill for a new SDK and use it to perform a task.
* **Target Substrate:** The official documentation for a new service (e.g., Stripe Node.js SDK).
* **Mechanism:** Skill-Director + Builder-Worker collaboration.

---

## 📥 The Intent
* **User:** "I want to create a new customer in Stripe using their Node.js SDK, but I don't have a Stripe skill yet. Here is the doc URL: https://docs.stripe.com/api"

---

## 🧠 Agentic Monologue (The "Build-Time" Process)

### Phase 1: Gap Analysis
* **Project Director:** "User requires a Stripe implementation. I have performed a Munch-Init on the /skills directory and confirmed no skill-stripe.md exists. Initiating Munch-Build via the Skill-Director."

### Phase 2: Architectural Spec (Skill-Director)
* **Skill-Director:** "I am establishing savref of the Stripe SDK patterns. Scanning the documentation tree to identify core symbols."
* **Action:** jdocmunch::get_toc_tree(url="https://docs.stripe.com/api")
* **Architectural Spec:** "IDs must follow stripe::customers#{type}. Mandate Munch-Search for error handling patterns before any create call."

### Phase 3: Synthesis (Builder-Worker)
* **Builder-Worker:** "Authoring skill-stripe.md following the Munch-Formula. Defining Stable IDs and ROI protocols."
* **Action:** Writes the .md file to /skills/generated/skill-stripe.md.
* **Validation:** "Ensuring the _meta block for token auditing is included in the tool table."

---

## ⚙️ The Execution (The "Run-Time" Result)
* **Project Director:** "Skill synthesized. I am now tasking a Tactical Worker to use the new skill-stripe to create the customer."

---

## 📊 Munch-Audit (ROI Report)
* **Task:** Stripe Skill Synthesis & Customer Creation.
* **Skill Generation Cost:** ~3,000 tokens (One-time investment).
* **Execution Cost:** 900 tokens (vs. ~15k for reading raw Stripe docs).
* **Future ROI:** Every subsequent Stripe task will now benefit from Context Hygiene and precision retrieval.

---

## 🛠️ Key Takeaways for the User
1. **Zero Configuration:** The user provided a URL, and the engine built the interface.
2. **Persistence:** The generated skill is saved. The engine is now permanently "smarter" regarding Stripe.
3. **Standardization:** Even though the skill was auto-generated, it follows the same MunchSpeak protocols as the core skills, ensuring it plays well with the rest of the swarm.
