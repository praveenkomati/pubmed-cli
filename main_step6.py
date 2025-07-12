import requests

def fetch_papers(query: str) -> None:
    print(f"🔍 Searching PubMed for: {query}")
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        ids = data.get("esearchresult", {}).get("idlist", [])
        print(f"✅ Found PubMed IDs: {ids if ids else 'No results'}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("✅ Running main.py")
    fetch_papers("covid AND cancer")
