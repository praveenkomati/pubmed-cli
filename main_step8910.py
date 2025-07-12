import requests
import argparse
import csv
from typing import List, Optional
from lxml import etree
from typing import Dict

def fetch_papers(query: str, debug: bool = False) -> List[str]:
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
        return ids
    except Exception as e:
        print(f"❌ Error: {e}")
        return []


def save_to_csv(paper_ids: List[str], filename: str) -> None:
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["PubMedID"])
        for pid in paper_ids:
            writer.writerow([pid])
    print(f"💾 Saved {len(paper_ids)} PubMed IDs to {filename}")

def get_paper_details(pubmed_ids: List[str], debug: bool = False) -> List[Dict[str, str]]:
    if not pubmed_ids:
        return []

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        root = etree.fromstring(response.content)
        articles = root.xpath("//PubmedArticle")

        results = []

        for article in articles:
            title = article.xpath("string(.//ArticleTitle)")
            pub_date = article.xpath("string(.//PubDate/Year)")

            authors = article.xpath(".//AuthorList/Author")
            non_academic_authors = []
            company_affiliations = []

            for author in authors:
                aff = author.xpath("string(.//AffiliationInfo/Affiliation)")
                name = author.xpath("string(.//LastName)") + " " + author.xpath("string(.//ForeName)")

                # Detect company authors (not academic)
                if aff and not any(word in aff.lower() for word in [
                    "university", "college", "institute", "school", "hospital", "center", "department", "lab"
                ]):
                    non_academic_authors.append(name)
                    company_affiliations.append(aff)

            email = ""
            affiliations = article.xpath(".//AffiliationInfo/Affiliation")
            for aff in affiliations:
                text = aff.text or ""
                if "@" in text:
                    email = text
                    break
            results.append({
                "PubmedID": article.xpath("string(.//PMID)"),
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": email  
            })

        if debug:
            print(f"🔍 Parsed {len(results)} articles from efetch")

        return results
    except Exception as e:
        print(f"❌ Failed to fetch details: {e}")
        return []    
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query.")
    parser.add_argument("--query", "-q", required=True, help="Search query for PubMed")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")
    parser.add_argument("--file", "-f", type=str, help="CSV file to save results")

    args = parser.parse_args()

    paper_ids = fetch_papers(args.query, args.debug)

    if paper_ids:
        paper_details = get_paper_details(paper_ids, args.debug) 
        if args.file:
            keys = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
            with open(args.file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(paper_details)
            print(f"💾 Saved {len(paper_details)} detailed records to {args.file}")
        else:
            for paper in paper_details:
                print("🧾", paper)
    else:
        print("❌ No PubMed IDs found.")


    

