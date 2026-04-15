# 📖 Playbook 03: The Precision Data Audit (v2.1)
**Objective:** Extract specific insights from a dataset without loading the entire file into the context window.
**Target Substrate:** sample_app/data/transactions.csv.
**Mechanism:** jDataMunch SQL-offloading for savref establishment.
**Total Tokens Saved:** ~99% (Comparing full-file streaming vs. targeted SQL aggregation).

## 📥 The Intent
**User:** "I need to know the total revenue for 'Region: Southeast' from our transaction data. Also, find the specific Stable ID for the largest single transaction in that group."

## 🧠 Agentic Monologue (The "Thought" Process)

### Phase 1: Munch-Init (Schema Mapping)
**Director:** "Establishing savref of the verified substrate. I must verify the column headers before reasoning (savraz)."
**Action:** `jdatamunch::describe_dataset(filename="sample_app/data/transactions.csv")`
**Result:** Identifies columns: transaction_id, region, date, amount, status.

### Phase 2: Munch-Search (The Aggregation)
**Director:** "Performing targeted aggregation. Moving from fok~ to fok~ by requesting only the sum of the 'amount' column for 'Southeast'."
**Action:** jdatamunch::aggregate(dataset="sample_app/data/transactions", dimensions=["region"], measures=["sum(amount)"], filters={"region": "Southeast"})
**Result:** Revenue: $151,200.50 (based on sample outliers).

### Phase 3: Munch-Grab (Row-Level Strike)
**Director:** "Isolating the outlier to maintain Context Hygiene."
**Action:** `jdatamunch::get_rows(dataset="sample_app/data/transactions", sort="-amount", limit=1, filters={"region": "Southeast"})`
**Worker nok~ (Near-context):**
```
JSON
{ 
  "transaction_id": "TXN_882", 
  "region": "Southeast", 
  "amount": 150000.00, 
  "status": "completed" 
}
```

## 📤 The Result
**Tactical Worker:** "The total revenue for the Southeast region was $151,200.50. The largest single transaction was for $150,000.00 (ID: TXN_882)."

## 📊 Munch-Audit (ROI Report)
**Method:** `jDataMunch` SQL-to-SQLite relay.
**Tokens Used:** 1,850.
**Naive Baseline:** ~15,000 tokens (if reading the full 1,000-row CSV).
**Savings:** ~87% (Scaling to 99%+ as file size increases).
**Status:** `rek~mi` achieved via surgical query.