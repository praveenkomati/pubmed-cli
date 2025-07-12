import requests
from typing import List, Dict
from lxml import etree

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
