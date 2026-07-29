#!/usr/bin/env python3
"""Export papers.yaml to BibTeX format."""

import argparse
import sys
import re
from pathlib import Path

import yaml


def clean_title(title: str) -> str:
    """Clean LaTeX special chars in title."""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    for old, new in replacements.items():
        title = title.replace(old, new)
    return title


def arxiv_id_from_url(url: str) -> str:
    """Extract arXiv ID from URL."""
    m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)(?:v\d+)?', url)
    return m.group(1) if m else None


def url_to_doi(url: str) -> str:
    """Convert URL to DOI string for BibTeX."""
    aid = arxiv_id_from_url(url)
    if aid:
        return f"10.48550/arXiv.{aid}"

    m = re.search(r'doi\.org/(10\.\S+)', url)
    if m:
        return m.group(1)

    # aclanthology
    m = re.search(r'aclanthology\.org/(\S+)', url)
    if m:
        return f"10.18653/v1/{m.group(1)}"

    return None


def paper_to_bibtex(paper: dict) -> str:
    """Convert a paper dict to a BibTeX entry."""
    aid = arxiv_id_from_url(paper['url'])
    doi = url_to_doi(paper['url'])

    # Generate citation key: FirstAuthorYear
    authors = paper.get("authors", [])
    first_author = authors[0].split()[-1] if authors else "Unknown"
    year = paper['date'][:4]
    title_short = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].split(':')[0].split('—')[0].strip()[:30])
    cite_key = f"{first_author}{year}{title_short[:20]}"

    # Clean authors
    author_str = " and ".join(authors) if authors else "Unknown"

    entry_lines = [f"@article{{{cite_key},"]
    entry_lines.append(f"  title     = {{{clean_title(paper['title'])}}},")
    entry_lines.append(f"  author    = {{{author_str}}},")

    if paper.get("venue"):
        entry_lines.append(f"  journal   = {{{paper['venue']}}},")

    if doi:
        entry_lines.append(f"  doi       = {{{doi}}},")

    entry_lines.append(f"  year      = {{{year}}},")
    entry_lines.append(f"  url       = {{{paper['url']}}},")
    entry_lines.append(f"  archivePrefix = {{arXiv}},")

    if aid:
        entry_lines.append(f"  eprint    = {{{aid}}},")
        entry_lines.append(f"  primaryClass = {{cs.AI}},")

    entry_lines.append("}")

    return "\n".join(entry_lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Export papers.yaml to BibTeX")
    parser.add_argument("--output", "-o", default="paper/references.bib",
                        help="Output BibTeX file path")
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    yaml_path = base / "papers.yaml"
    output_path = base / args.output

    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    papers = data.get("papers", [])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    for paper in papers:
        entries.append(paper_to_bibtex(paper))

    output_path.write_text("".join(entries), encoding="utf-8")
    print(f"Generated {output_path} with {len(entries)} BibTeX entries")


if __name__ == "__main__":
    main()
