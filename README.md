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

```bash
git clone https://github.com/praveenkomati/pubmed-cli.git
cd pubmed-cli
2. Install Dependencies Using Poetry
Make sure you have Poetry installed.

bash
Copy
Edit
poetry install
🚀 How to Use
Basic Command:
bash
Copy
Edit
poetry run python main.py -q "cancer AND AI" -f cancer_ai.csv
Optional Flags:
-d or --debug: Print debug output

-f or --file: Save results to a CSV file

-q or --query: Search query for PubMed

🧪 Tools & Libraries Used
Python

Poetry

requests

lxml

PubMed E-utilities API

📂 Project Structure
pgsql
Copy
Edit
pubmed-cli/
├── main.py
├── pubmed/
│   ├── __init__.py
│   ├── fetch.py
│   └── utils.py
├── pyproject.toml
├── poetry.lock
├── results.csv (sample output)
└── README.md
✅ Author
Praveen Komati
GitHub: praveenkomati

📝 License
This project is for educational/demo purposes only.

yaml
Copy
Edit

---

Let me know if you also want to include the **top part** (title, description, features, output format) too.
