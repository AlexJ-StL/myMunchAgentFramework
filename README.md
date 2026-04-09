# 🦖 Munch-Engine: The Precision-Retrieval Swarm

**Stop burning your budget on "Brute-Force" AI.** Most AI agents explore code and data the expensive way: they read entire files, skim thousands of irrelevant lines, and flood their context windows with noise. This "Naive RAG" approach is slow, hallucination-prone, and costs up to 100x more than it should.

**Munch-Engine** is a recursive, multi-agent framework built on the **jMRI (jMunch Retrieval Interface) Specification**. It enables agents to navigate codebases, documentation, and datasets with surgical precision—retrieving only the exact symbols, sections, or rows needed to solve a task.


## 💡 The "First Principles" Advantage

This engine operates on three core values:

	1. Precision > Volume: Fetching 20 lines of a specific function is better than reading a 2,000-line file.

	2. Objective ROI: Every tool call returns a _meta block showing exactly how many tokens were saved.

	3. Autopoietic Growth: The system automatically builds its own "Skills" (.md files) when it encounters a new API or SDK.


## 🏗️ The Architecture (Tiered Agency)

The engine utilizes a three-tier "Swarm" to separate strategy from execution:

	1. **The Project Director (Strategic):** The "Brain." Analyzes your request, scans the ``` /skills ``` library, and coordinates the mission.

	2. **The Skill Creator Director (Architectural):** The "Engineer." If a skill is missing, it reads the documentation and drafts a new jMRI-compliant skill file.

	3. **The Tactical Worker (Execution):** The "Hands." A specialized agent that uses a single skill to perform a precise task (e.g., refactoring one function) without seeing the rest of the project.


## 🚀 Quickstart: 5 Minutes to 99% Savings

#### 1. Prerequisites

Install the core jMunch MCP servers:
```Bash
pip install jcodemunch-mcp jdocmunch-mcp jdatamunch-mcp
```

#### 2. Installation

Clone this repository and point your AI agent (Claude Code, Cursor, etc.) to the ``` agent.md ``` file.
```Bash
git clone https://github.com/your-repo/munch-engine.git
```

#### 3. Run a Task

Ask the Director a high-level goal:

"Analyze the auth logic in this repo and update the login session timeout to 24 hours."


#### 4. The Loop

The engine will:

- **Discover:** Scan your repo using jCodeMunch.

- **Search:** Find the specific login function ID.

- **Retrieve:** Fetch only that function.

- **Execute:** A Worker performs the update.

- **Report:** You receive the fix and an Efficiency Report.


## 📈 Performance Benchmarks

Task | Naive Retrieval | Munch-Engine (jMRI) | Savings
:-- | --- | --- | --:
Repo Exploration | "200,000 tokens" | "2,000 tokens" | 99%
Doc Reference | "12,000 tokens" | 400 tokens | 96%
Data Aggregation | Full File Load | Row-Level Query | Variable (High)


## 🛠️ The Skill Factory

One of the most powerful features of Munch-Engine is its ability to self-expand. If you need to work with a new SDK (e.g., Supabase or Stripe), simply tell the Director. The Skill Creator will:

	1. Use jDocMunch to ingest the official API docs.

	2. Generate a new skill-supabase.md using the Munch Formula.

	3. Validate the skill and add it to your library for future use.


## 📜 License & Credits

**Framework:** Open Source (MIT)

**Specification:** jMRI (jMunch Retrieval Interface)

**Author:** Developed in collaboration with AlexJ, inspired by the work of **J. Gravelle**.

“Good communication is efficient AND effective mutual understanding.”
Join the swarm. Save the tokens.