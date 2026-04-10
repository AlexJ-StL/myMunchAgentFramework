# 📖 Playbook 03: The Precision Data Audit

* **Objective:** Extract specific insights from a massive dataset (e.g., a 500MB CSV of transaction logs) without reading the file.
* **Target Substrate:** global_sales_2025.csv (2.5 million rows).
* **Mechanism:** jDataMunch SQL-offloading.
* **Total Tokens Saved:** ~5,000,000+ (Calculation: 500MB is roughly 125M tokens; Munch-Engine used < 5k).

---

## 📥 The Intent
* **User:** "I need to know the total revenue for 'Region: Southeast' during 'Q3' from the sales CSV. Also, find the specific Row ID for the largest single transaction in that group."

---

## 🧠 Agentic Monologue (The "Thought" Process)

### Phase 1: Munch-Init (Schema Mapping)

* **Director:** "Establishing savref of the dataset. I cannot reason about the data (savraz) until I understand the column types and cardinality."
* **Action:** jdatamunch::describe_dataset(filename="global_sales_2025.csv")
* **Result:** Identifies columns: transaction_id, region, date, amount. Established that region is a categorical string.

### Phase 2: Munch-Search (The Aggregation)

* **Director:** "Performing a targeted aggregation. I am moving from fok~ to nok~ by requesting only the sum of the 'amount' column for the specified filters."
* **Action:** jdatamunch::aggregate(dataset="global_sales_2025", dimensions=["region"], measures=["sum(amount)"], filters={"region": "Southeast", "date": {"between": ["2025-07-01", "2025-09-30"]}})
* **Result:** Revenue: $4,200,550.

### Phase 3: Munch-Grab (Row-Level Strike)

* **Director:** "Identifying the outlier. I am requesting the single record with the highest value to maintain Context Hygiene."
* **Action:** jdatamunch::get_rows(dataset="global_sales_2025", sort="-amount", limit=1, filters={"region": "Southeast"})
* **Worker nok~ (Near-context):**
	```JSON
	{ "id": "global_sales_2025::row_882194#row", "amount": 150000, "customer": "CorpX" }
	```

---

## 📤 The Result
* **Tactical Worker:** "The total revenue for the Southeast in Q3 was $4,200,550. The largest single transaction was for $150,000 (ID: row_882194)."

---

## 📊 Munch-Audit (ROI Report)

* **Method:** jDataMunch SQL-to-SQLite.
* **Tokens Used:** 2,100.
* **Naive Baseline:** ERROR (Context Window Exceeded) or ~125 Million tokens if streamed.
* **Savings:** Theoretical Maximum.
* **Status:** rek~mi achieved via surgical query.

---

## 🛠️ Key Takeaways for the User

* **Size Independence:** The engine's performance remains the same whether the file is 1MB or 10GB.
* **Computational Offloading:** The heavy lifting (summing millions of rows) happened in the MCP server, not the LLM.
* **Traceability:**** The agent provided a Stable Row ID, allowing the human to verify the specific entry in the original file.