# PubMed CLI Tool 🧬

A Python command-line tool to search PubMed for research papers with **non-academic (pharma/biotech) affiliated authors** and export results to a CSV file.

---

## 🔍 Features

- Search PubMed using any advanced query (e.g., `"cancer AND AI"`)
- Fetch paper details using PubMed API
- Detect authors with **non-academic affiliations** (e.g., companies)
- Extract corresponding author email (if available)
- Export results to a CSV file
- CLI options for query, output file, and debug mode

---

## 📁 Output Format

Each row in the CSV will have:

- `PubmedID`
- `Title`
- `Publication Date`
- `Non-academic Author(s)`
- `Company Affiliation(s)`
- `Corresponding Author Email`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

