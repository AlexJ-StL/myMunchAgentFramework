---
name: skill-jcodemunch-mcp
description: Structured code symbol retrieval for AI agents by use of jCodeMunch-MCP
license: jCodeMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: codebase analysis and retrieval
    source:
        repository: 'https://github.com/jgravelle/jcodemunch-mcp'
        example path: C:/Users/User/.agents/skills/skill-jcodemunch-mcp
---


## Agent Instructions:
- Use jcodemunch-mcp for navigating codebases to minimize token waste.
- Always call `get_repo_outline` or `get_file_tree` first to orient on project structure.
- Use `search_symbols` to find specific logic rather than reading full files.
- Use `get_symbol` to retrieve exact implementations (functions, classes, methods).
- A qualified ID is expected: Use **Stable Symbol IDs** (e.g., `{file_path}::{qualified_name}#{kind}`) for retrieval.
- When results are ambiguous, fall back to `search_text` for full-text keyword matching.


## Tools

| Tool | What it does |
| :--- | :--- |
| **index_folder** | Index a local directory. Uses tree-sitter AST to extract symbols. |
| **index_repo** | Index a GitHub repository via URL (e.g., "owner/repo"). |
| **list_repos** | List all indexed repositories and local folders. |
| **get_repo_outline** | High-level overview: lists top-level modules and key entry points. |
| **get_file_tree** | Returns the full directory structure of the indexed repository. |
| **get_file_outline** | Shows the symbol hierarchy (classes, methods) for a specific file. |
| **get_symbol** | Retrieve the full source code of a single specific symbol ID. |
| **get_symbols** | Batch retrieval: get source for multiple symbol IDs in one call. |
| **search_symbols** | Search for symbols by name, kind, or language with filters. |
| **search_text** | Standard full-text search with surrounding context lines. |
| **get_file_content** | Retrieve a specific line range from a cached file. |
| **invalidate_cache** | Remove a cached index to force a fresh re-index. |


## Configuration

| Variable | Default | Purpose |
| :--- | :--- | :--- |
| **CODE_INDEX_PATH** | `~/.code-index/` | Storage for JSON indexes and cached symbols. |
| **JCODEMUNCH_LOG_LEVEL** | `WARNING` | Set to `DEBUG` for troubleshooting indexing issues. |
| **GITHUB_TOKEN** | — | Required for private repos or high GitHub API limits. |
| **ANTHROPIC_API_KEY** | — | AI-generated symbol summaries via Claude (takes priority). |
| **GOOGLE_API_KEY** | — | AI-generated symbol summaries via Gemini Flash. |


## Example Usage

| Scenario | Without jCodeMunch | With jCodeMunch | Measured savings |
| :--- | :--- | :--- | :--- |
| Find a function | Paste raw files (~40k tokens) | `search_symbols` (~200 tokens) | ~200× |
| Understand Module API | Read full module (~15k tokens) | `get_file_outline` (~800 tokens) | ~18× |
| Explore Repo Structure | Walk 338 files (~200k tokens) | `get_repo_outline` (~2k tokens) | 100× |
| Locate math logic | Manual scan (~7,500 tokens) | `search_symbols` → `get_symbol` (~1,449) | ~80% |


## ID Scheme

- Every symbol gets a stable ID based on its signature:
	- `{file_path}::{qualified_name}#{kind}`
	- Example: `src/main.py::UserService.login#method`
	- Example: `src/utils.py::authenticate#function`
- Use these IDs with `get_symbol` or `get_symbols` for precision retrieval.


## Synergies
- **jDataMunch Synergy**: Use `jCodeMunch` to understand the data processing logic (e.g., a transformation function) before using `jDataMunch` to query the resulting dataset.
- **Global Agent Context**: When asked to "refactor" or "debug," use this tool to isolate the specific code block before suggesting changes.


## jCodeMunch MCP Server Installation:

### 1. Install it
```bash
pip install jcodemunch-mcp
```
### 2. Add it to your MCP client
- If you're using Claude Code:
	```Bash
	claude mcp add jcodemunch uvx jcodemunch-mcp
	```
- Or add manually to your ~/.claude.json:
	```JSON
	{
		"mcpServers": {
			"jcodemunch": {
				"command": "uvx",
				"args": ["jcodemunch-mcp"]
			}
		}
	}
	```