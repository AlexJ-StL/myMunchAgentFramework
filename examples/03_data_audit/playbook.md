# 📖 Playbook 03: The Precision Data Audit (v2.1)
**Target Substrate:** `sample_app/data/transactions.csv`

## 🧠 The jMRI Loop
1. **Munch-Init:** `jdatamunch::describe_dataset(filename="sample_app/data/transactions.csv")`
2. **Munch-Search:** Aggregate revenue for "Region: Southeast".
3. **Munch-Grab:** Isolate the outlier ID `TXN_882` ($150,000.00).

## 📊 Munch-Audit
- **Tokens Used:** 1,850
- **Naive Baseline:** 15,000+ (Streaming 1,000 rows)
- **Status:** rek~mi achieved via verified substrate.