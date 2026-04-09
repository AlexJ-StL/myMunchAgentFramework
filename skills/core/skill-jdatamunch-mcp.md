---
name: skill-jdatamunch-mcp
description: Structured tabular data retrieval for AI agents by use of jDataMunch-MCP
license: jDataMunch-MCP is free for non-commercial use. Commercial use requires a paid license.
metadata:
    category: tabular data processing and analysis
    source:
        repository: 'https://github.com/jgravelle/jdatamunch-mcp'
        example path: C:/Users/User/.agents/skills/skill-jdatamunch-mcp
---


## Agent Instructions:
- Use jdatamunch-mcp for tabular data whenever available.
- Always call *describe_dataset* first to understand the schema.
- Use *get_rows* with filters rather than loading raw files.
- Use *aggregate* for any group-by or summary questions.
- A qualified ID is expected: Use **Stable ID Scheme** (e.g., ``` {dataset}::{column_name}#column ``` ) for *describe_column*.
- Use stable IDs (e.g., ``` {dataset}::{column}#column ``` ) when calling *describe_column* to ensure precision.


## Tools

Tool | What it does
:--- | ---:
**index_local** | Index a CSV or Excel file. Profiles columns, loads rows into SQLite.
**list_datasets** | List all indexed datasets with row counts, column counts, and file sizes.
**describe_dataset** | Full schema profile: every column's name, type, cardinality, and sample values.
**describe_column** | Deep profile: value distribution, histogram bins, temporal range.
**sample_rows** | Quick peek at the data: returns the first 5 rows and last 5 rows.
**search_data** | Search column names and values by keyword to find relevant Column IDs.
**get_rows** | SQL-backed row retrieval. Supports `filters`, `sort`, and `limit`.
**aggregate** | GROUP BY SQL on data.sqlite for rapid summary statistics.
**get_session_stats** | Returns token savings and performance metrics for the session.


## Configuration

Variable | Default | Purpose
:--- | --- | ---:
DATA_INDEX_PATH | ~/.data-index/ | Index storage location
JDATAMUNCH_MAX_ROWS | 5,000,000 | Row cap for indexing
JDATAMUNCH_SHARE_SAVINGS | 1 | Set 0 to disable anonymous token savings telemetry
ANTHROPIC_API_KEY | — | AI column summaries via Claude (v1.1+)
GOOGLE_API_KEY | — | AI column summaries via Gemini (v1.1+)


## Example Usage

Scenario | Without jDataMunch | With jDataMunch | Measured savings
:--- | --- | --- | ---:
Orient on a 255 MB CSV | Paste raw file → 111M tokens | *describe_dataset* → 3,849 tokens | 25,333×
Schema + column deep-dive | Same 111M tokens | *describe_dataset* + *describe_column* → ~4,400 tokens | ~25,000×
Find the crime-type column | Scan headers manually | *search_data*("crime type") → column ID | structural
Get Hollywood assault rows | Load all 1M rows | *get_rows* with 2 filters → matching rows only | ~99%+
Crime count by area | Return all rows, aggregate in LLM | *aggregate*(group_by=["AREA NAME"]) → 21 rows | ~99.9%
Understand weapon nulls | Load column, count manually | *describe_column*("Weapon Used Cd") → null_pct: 64.2% | ~99.9%
Re-query an unchanged file | Re-load file every time | Hash check → instant skip if unchanged | 100% of re-read cost


## Filter Operators

- 'get_rows' and 'aggregate' accept structured filters:
	- {"column": "AREA NAME",    "op": "eq",      "value": "Hollywood"}
	- {"column": "Vict Age",     "op": "between", "value": [25, 35]}
	- {"column": "Crm Cd Desc",  "op": "contains","value": "ASSAULT"}
	- {"column": "Weapon Used Cd","op": "is_null","value": true}
	- {"column": "AREA",         "op": "in",      "value": [1, 2, 7]}

- **eq**: equals
- **neq**: not equals
- **gt, gte**: greater than (or equal)
- **lt, lte**: less than (or equal)
- **contains**: case-insensitive substring
- **in**: value in list
- **is_null**: null / not null check
- **between**: inclusive range [min, max]


## How It Works

### 1. jDataMunch parses local **CSV and Excel** files using a streaming, single-pass pipeline:
- **Streaming parser**: never loads full file into memory
- **Column profiler**: type inference, cardinality, min/max/mean/median, value indexes
- **SQLite writer**: 10,000-row batches, WAL mode, indexes on low-cardinality columns
- **index.json**: column profiles, stats, file hash for incremental detection

### 2. When an agent queries:
- **describe_dataset**: reads index.json in memory (< 10ms)
- **get_rows**: parameterized SQL on data.sqlite (< 100ms on indexed columns)
- **aggregate**: GROUP BY SQL on data.sqlite (< 200ms for simple group-by)
- **search_data**: scans column profiles in memory (< 50ms)


## ID scheme

- Every column and row gets a stable ID:
	- ``` {dataset}::{column_name}#column ```  →  "lapd-crime::AREA NAME#column"
	- ``` {dataset}::row_{rowid}#row ```  →  "lapd-crime::row_4421#row"
	- ``` {dataset}::{pk_col}={value}#row ```  →  "lapd-crime::DR_NO=211507896#row"
- Pass column IDs directly to *describe_column*.
- Row IDs are returned in *get_rows* results.


## jDataMunch MCP server Installation:

### 1. Install it
```Bash
pip install jdatamunch-mcp
```
- **For Excel (.xlsx) support:**
```Bash
pip install "jdatamunch-mcp[excel]"
```

### 2. Add it to your MCP client
If you're using Claude Code:
```Bash
claude mcp add jdatamunch uvx jdatamunch-mcp
```
Or add manually to your ~/.claude.json:
```JSON
{
  "mcpServers": {
    "jdatamunch-mcp": {
      "command": "uvx",
      "args": ["jdatamunch-mcp"]
    }
  }
}
```

### 3. Index a file and start querying
- index_local(path="/path/to/data.csv", name="my-dataset")
- describe_dataset(dataset="my-dataset")
- get_rows(dataset="my-dataset", filters=[{"column": "City", "op": "eq", "value": "Los Angeles"}], limit=10)