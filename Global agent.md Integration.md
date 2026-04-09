## 1. Global agent.md Integration

#### jMRI Operational Mandate (Precision Retrieval)
	
	- **Objective:** Minimize "Context Poisoning" and token waste by adhering to the jMRI specification.
	
	- **Primary Metric:** Success is measured by the `tokens_saved` value in tool metadata. High-volume raw file reading is considered a tactical failure.
	
	- **Protocol:**
		
		1. **Discover:** Query `list_datasets` or `list_repos` to see available knowledge substrates.
		
		2. **Search:** Use `search_data`, `search_symbols`, or `search_sections` to find specific IDs.
		
		3. **Retrieve:** Access content ONLY via Stable IDs (e.g., `{repo}::{symbol}#{kind}`).

## 2. skills.md Standardized Template

#### jMRI Compliance Level: Full

	- **Identifier Stability:** Uses the standard `{origin}::{name}#{type}` scheme for byte-precise addressing.

	- **Metadata Reporting:** Supports the `_meta` envelope providing `tokens_saved` and `total_tokens_saved`.

	- **Semantic Boundaries:** Retrieval is restricted to AST nodes (code), heading blocks (docs), or schema-validated rows (data), preventing "mid-sentence" chunking errors common in standard RAG.

3. System Prompt "Anchor"

You are a jMRI-compliant agent. You treat the user's token budget as a finite resource. You are strictly prohibited from reading entire files over 50 lines if a targeted jMRI search/retrieval tool is available. Before every retrieval, internally calculate if a more precise search could yield the same result for fewer tokens.

4. ROI Tracking (Personalization Trigger)
t the end of complex tasks involving multiple datasets or repositories, call get_session_stats and summarize the total tokens saved. Present this as a 'Efficiency Report' to validate the ROI of the current agentic strategy.


This all looks great! This is a fantastic place to introduce something else that I have been thinking about for a long time, but haven't found the time to inject it into an agentic apparatus. We have talk about in the past something that I have called "the round table" or a "consensus mechanism", perhaps another way to say it is "refined agentic action". "Refined agentic action" means that all forward progress is made only after a "hypothesis, synthesis, conclusion" type of process wherein a small group of specialized agents at every "node" in the path from user prompt to final solution. What this looks like practically from a development standpoint in the current context (seshi~mi) is the "director/manager" would be 1 position with at least 2, preferably 3