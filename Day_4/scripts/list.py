import requests
import json
import argparse
from pathlib import Path

OPENALEX_URL = "https://api.openalex.org/works"

def load_queries(path: Path):
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]

def fetch_openalex(query: str, limit: int = 20):
    params = {
        "search": query,
        "per-page": limit,
        "mailto": "example@mail.com"  # required by OpenAlex politely
    }

    response = requests.get(OPENALEX_URL, params=params)
    data = response.json()

    papers = []
    for item in data.get("results", []):
        papers.append({
            "title": item.get("title"),
            "authors": [auth["author"]["display_name"] for auth in item.get("authorships", [])],
            "year": item.get("publication_year"),
            "venue": item.get("host_venue", {}).get("display_name"),
            "url": item.get("primary_location", {}).get("landing_page_url"),
            "doi": item.get("doi"),
            "abstract": item.get("abstract_inverted_index"),
            "cited_by_count": item.get("cited_by_count"),
            "openalex_id": item.get("id"),
            "query": query
        })
    return papers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", default="research/queries.txt")
    parser.add_argument("--out", default="research/papers.json")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    query_file = Path(args.queries)
    queries = load_queries(query_file)

    all_papers = []
    for q in queries:
        print(f"Searching: {q}")
        papers = fetch_openalex(q, args.limit)
        print(f" → found {len(papers)} papers")
        all_papers.extend(papers)

    out_path = Path(args.out)
    out_path.write_text(json.dumps(all_papers, indent=2))

    print(f"\nSaved: {args.out} ({len(all_papers)} papers total)")

if __name__ == "__main__":
    main()
