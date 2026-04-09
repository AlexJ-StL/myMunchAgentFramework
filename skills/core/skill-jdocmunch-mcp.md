---
name: skill-jdocmunch-mcp
description: Structured documentation retrieval for AI agents by use of jDocMunch-MCP
license: jDocMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: documentation analysis and retrieval
    source:
        repository: 'https://github.com/jgravelle/jdocmunch-mcp'
        example path: C:/Users/User/.agents/skills/skill-jdocmunch-mcp
---

## Agent Instructions:
- Use jdocmunch-mcp for navigating documentation to maintain context hygiene.
- Always call `get_toc_tree` or `get_document_outline` first to understand the doc structure.
- Retrieve specific sections via `get_section` instead of reading entire files.
- Use `search_sections` to find relevant explanations or configuration blocks.
- A qualified ID is expected: Use **Stable Section IDs** (e.g., `{repo}::{doc_path}::{ancestor-chain/slug}#{level}`) for retrieval.
- If a section requires more context, use `get_section_context` to see its parent and children.

## Tools

| Tool | What it does |
| :--- | :--- |
| **index_local** | Index a local documentation folder (Markdown, MDX, HTML, RST, etc.). |
| **index_repo** | Index documentation directly from a GitHub repository. |
| **list_repos** | List all indexed documentation sets available to the agent. |
| **get_toc_tree** | Returns a nested section tree for every document in the set. |
| **get_document_outline** | Shows the heading hierarchy for a single specific document. |
| **search_sections** | Weighted search that returns section summaries and IDs. |
| **get_section** | Retrieve the full, byte-precise content of a single section ID. |
| **get_sections** | Batch retrieval: get content for multiple section IDs at once. |
| **get_section_context** | Returns a section plus its ancestor headings and child summaries. |
| **delete_index** | Remove a documentation index from the local cache. |

## Configuration

| Variable | Default | Purpose |
| :--- | :--- | :--- |
| **DOC_INDEX_PATH** | `~/.doc-index/` | Storage for JSON indexes and cached documentation. |
| **JDOCMUNCH_SHARE_SAVINGS** | `1` | Set to `0` to disable anonymous token savings reporting. |
| **ANTHROPIC_API_KEY** | — | Used for AI-generated section summaries via Claude. |
| **GOOGLE_API_KEY** | — | Used for AI-generated summaries or Gemini embeddings. |
| **OPENAI_API_KEY** | — | Used for OpenAI embeddings (text-embedding-3-small). |

## Example Usage

| Scenario | Without jDocMunch | With jDocMunch | Measured savings |
| :--- | :--- | :--- | :--- |
| Find config section | ~12,000 tokens | ~400 tokens | ~30× |
| Browse doc structure | ~40,000 tokens | ~800 tokens | ~50× |
| Explore full doc set | ~100,000 tokens | ~2,000 tokens | ~50× |
| API reference dive | Manual file scan | `search_sections` → `get_section` | ~98%+ |

## ID Scheme

- Every section gets a stable ID based on the heading hierarchy:
	- `{repo}::{doc_path}::{ancestor-chain/slug}#{level}`
	- Example: `local/project::guide.md::configuration#2`
	- Example: `owner/repo::README.md::usage/configuration/advanced#4`
- These IDs remain stable as long as the path and heading text do not change.

## Synergies
- **jCodeMunch Synergy**: When code is found in `jCodeMunch` that lacks inline comments, use `jDocMunch` to find the corresponding architectural explanation in the external docs.
- **jDataMunch Synergy**: Use `jDocMunch` to retrieve data dictionaries or schema definitions stored in documentation before querying the actual data with `jDataMunch`.
- **Global Agent Context**: Prioritize documentation over code analysis when asked "How do I use..." to ensure usage follows the author's intended patterns rather than the agent's inferences.

## jDocMunch MCP Server Installation:

### 1. Install it
```bash
pip install jdocmunch-mcp
```
### 2. Add it to your MCP client
- If you're using Claude Code:
	```Bash
	claude mcp add jdocmunch uvx jdocmunch-mcp
	```
- Or add manually to your ``` ~/.claude.json ```:
	```JSON
	{
		"mcpServers": {
			"jdocmunch": {
				"command": "uvx",
				"args": ["jdocmunch-mcp"]
			}
		}
	}
	```