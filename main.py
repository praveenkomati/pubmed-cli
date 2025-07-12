import argparse
from pubmed.fetch import fetch_papers, get_paper_details
from pubmed.utils import save_to_csv
from pubmed.fetch import fetch_papers, get_paper_details
from pubmed.utils import save_to_csv


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
            save_to_csv(paper_details, args.file)
        else:
            for paper in paper_details:
                print("🧾", paper)
    else:
        print("❌ No PubMed IDs found.")
