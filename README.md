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
2. Install Dependencies Using Poetry
Make sure you have Poetry installed.
Copy
Edit
poetry install
##🚀 How to Use
Basic Command:
bash
Copy
Edit
poetry run python main.py -q "cancer AND AI" -f cancer_ai.csv
Optional Flags:
-q or --query: PubMed search query

-f or --file: Save output to CSV

-d or --debug: Enable debug output

If no --file is provided, results are printed in the terminal.

🧪 Tools & Libraries Used
Python 3.9+

Poetry

requests

lxml

PubMed E-utilities API

###📂 Project Structure
csharp
Copy
Edit
pubmed-cli/
├── main.py                 # Entry point (CLI)
├── pubmed/
│   ├── __init__.py
│   ├── fetch.py            # API handling functions
│   └── utils.py            # CSV writing utilities
├── pyproject.toml
├── poetry.lock
├── results.csv             # Sample output
└── README.md
###✅ Author
Praveen Komati
GitHub: praveenkomati

###📝 License
This project is for educational and demonstration purposes only. No license is associated with commercial use.

yaml
Copy
Edit

