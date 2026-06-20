#!/usr/bin/env python3
"""Fetch metadata (authors, venue, abstract) from arXiv and Semantic Scholar APIs."""

import argparse
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})")
ARXIV_API = "http://export.arxiv.org/api/query?id_list={}"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/arXiv:{}?fields=title,authors,venue,year,abstract,citationCount"
API_DELAY = 3


def extract_arxiv_id(url):
    match = ARXIV_ID_PATTERN.search(url)
    return match.group(1) if match else None


def fetch_arxiv_metadata(arxiv_id):
    try:
        resp = requests.get(ARXIV_API.format(arxiv_id), timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return None

        authors = []
        for author in entry.findall("atom:author", ns):
            name = author.find("atom:name", ns)
            if name is not None and name.text:
                authors.append(name.text.strip())

        published = entry.find("atom:published", ns)
        date = published.text[:7] if published is not None and published.text else None

        summary = entry.find("atom:summary", ns)
        abstract = summary.text.strip() if summary is not None and summary.text else None

        return {"authors": authors, "date": date, "abstract": abstract}
    except Exception as e:
        print(f"  WARNING: arXiv API error for {arxiv_id}: {e}", flush=True)
        return None


def fetch_semantic_scholar(arxiv_id):
    try:
        resp = requests.get(SEMANTIC_SCHOLAR_API.format(arxiv_id), timeout=30)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        data = resp.json()

        authors = [a.get("name", "") for a in data.get("authors", []) if a.get("name")]

        return {
            "authors": authors,
            "venue": data.get("venue") or "",
            "abstract": data.get("abstract") or "",
            "citation_count": data.get("citationCount", 0),
        }
    except Exception as e:
        print(f"  WARNING: Semantic Scholar API error for {arxiv_id}: {e}", flush=True)
        return None


def main():
    parser = argparse.ArgumentParser(description="Fetch metadata for papers from arXiv and Semantic Scholar")
    parser.add_argument("--dry-run", action="store_true", help="Preview without modifying papers.yaml")
    parser.add_argument("--paper-id", type=str, help="Fetch metadata for a single paper (1-based index)")
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent / "papers.yaml"
    if not yaml_path.exists():
        print(f"ERROR: {yaml_path} not found", flush=True)
        sys.exit(1)

    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f) or {}

    papers = data.get("papers", [])
    total = len(papers)

    if args.paper_id:
        try:
            idx = int(args.paper_id) - 1
            if idx < 0 or idx >= total:
                print(f"ERROR: paper index {args.paper_id} out of range (1-{total})", flush=True)
                sys.exit(1)
            papers = [papers[idx]]
            total = 1
            start_idx = idx
        except ValueError:
            print(f"ERROR: --paper-id must be a number", flush=True)
            sys.exit(1)
    else:
        start_idx = 0

    updated = 0
    for i, paper in enumerate(papers):
        real_idx = start_idx + i
        title = paper.get("title", "Untitled")
        url = paper.get("url", "")

        arxiv_id = extract_arxiv_id(url)
        if not arxiv_id:
            print(f"Skipping paper {real_idx + 1}/{total}: '{title}' (no arXiv ID)", flush=True)
            continue

        print(f"Fetching metadata for paper {real_idx + 1}/{total}: '{title}' [{arxiv_id}]", flush=True)

        arxiv_meta = fetch_arxiv_metadata(arxiv_id)
        if arxiv_meta and not args.dry_run:
            if arxiv_meta["authors"] and not paper.get("authors"):
                paper["authors"] = arxiv_meta["authors"]
                updated += 1
            if arxiv_meta["date"] and not paper.get("date"):
                paper["date"] = arxiv_meta["date"]
                updated += 1
            if arxiv_meta["abstract"] and not paper.get("abstract"):
                paper["abstract"] = arxiv_meta["abstract"]
                updated += 1

        time.sleep(API_DELAY)

        ss_meta = fetch_semantic_scholar(arxiv_id)
        if ss_meta and not args.dry_run:
            if ss_meta["authors"] and not paper.get("authors"):
                paper["authors"] = ss_meta["authors"]
                updated += 1
            if ss_meta["venue"] and not paper.get("venue"):
                paper["venue"] = ss_meta["venue"]
                updated += 1
            if ss_meta["abstract"] and not paper.get("abstract"):
                paper["abstract"] = ss_meta["abstract"]
                updated += 1

        time.sleep(API_DELAY)

    if not args.dry_run and updated > 0:
        with open(yaml_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print(f"\nUpdated {updated} field(s) in {yaml_path}", flush=True)
    elif args.dry_run:
        print("\nDry run complete — no files modified", flush=True)
    else:
        print("\nNo new metadata found", flush=True)


if __name__ == "__main__":
    main()
