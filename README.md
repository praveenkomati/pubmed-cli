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

## 📁 Output Format (CSV)

Each row in the CSV file will contain:

- **PubmedID**: Unique paper ID
- **Title**: Title of the paper
- **Publication Date**: Year of publication
- **Non-academic Author(s)**: Authors from companies/industry
- **Company Affiliation(s)**: Detected company/institution
- **Corresponding Author Email**: If available

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/praveenkomati/pubmed-cli.git
cd pubmed-cli
```

### 2. Install Dependencies Using Poetry

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

```bash
poetry install
```

---

## 🚀 Usage

### Run the CLI Tool

```bash
poetry run python main.py -q "cancer AND AI" -f cancer_ai.csv --debug
```

### CLI Options

| Flag        | Description                          |
|-------------|--------------------------------------|
| `-q` / `--query` | PubMed search query (required)      |
| `-f` / `--file`  | Output CSV filename                |
| `-d` / `--debug` | Show debug output while running    |

If `--file` is not specified, the results will be printed to the console.

---

## 🛠 Project Structure

```
pubmed-cli/
├── main.py                 # Entry point
├── pubmed/
│   ├── __init__.py
│   ├── fetch.py            # PubMed API logic
│   └── utils.py            # CSV writing
├── pyproject.toml
├── poetry.lock
├── cancer_ai.csv           # Sample output file
└── README.md
```

---

## 🧪 Technologies Used

- Python 3.9+
- [Poetry](https://python-poetry.org/)
- [requests](https://pypi.org/project/requests/)
- [lxml](https://pypi.org/project/lxml/)
- [PubMed E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)

---
##🧠 Version Control:

This project uses Git for version control and is hosted on GitHub.

---

## 🧠 Heuristics for Non-Academic Affiliation

Authors are flagged as **non-academic** if their affiliation **does not contain** keywords like:

```
university, college, institute, school, hospital, center, department, lab
```

---

## 📌 Notes

- This project uses **type annotations**, is modular, and includes **error handling**.
- It can be extended to support pagination, more CSV columns, or custom filters.
- Designed to work with automated evaluators for submission.

---

## 👨‍💻 Author

**Praveen Komati**  
🔗 [GitHub: praveenkomati](https://github.com/praveenkomati)

---

## 📄 License

This tool is built for learning, demonstration, and take-home project submission only. No commercial license attached.
