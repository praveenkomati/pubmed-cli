import requests
import argparse

def fetch_papers(query: str, debug: bool = False) -> None:
    if debug:
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
        if debug:
            print(f"✅ Found PubMed IDs: {ids if ids else 'No results'}")
        else:
            print(f"✅ PubMed IDs: {ids}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query.")
    parser.add_argument("--query", "-q", required=True, help="Search query for PubMed")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    fetch_papers(args.query, args.debug)
