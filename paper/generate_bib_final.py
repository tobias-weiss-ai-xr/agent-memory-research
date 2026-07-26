#!/usr/bin/env python3
"""Generate BibTeX from papers.yaml matching LaTeX citekeys."""
import yaml
import re
from collections import defaultdict

# Load papers
with open('../papers.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    papers = data['papers']

# Extract all citekeys from LaTeX files
citekeys_used = set()
for section_file in ['sections/00_abstract.tex', 'sections/01_introduction.tex', 
                     'sections/02_background.tex', 'sections/03_methodology.tex',
                     'sections/04_taxonomy.tex', 'sections/05_landscape.tex',
                     'sections/06_gap_analysis.tex', 'sections/07_benchmarks.tex',
                     'sections/08_conclusion.tex', 'sections/A1_paper_list.tex']:
    try:
        with open(section_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract all \cite{...} and \citet{...} keys
            matches = re.findall(r'\\cite[tp]?\{([^}]+)\}', content)
            for match in matches:
                # Split by comma if multiple citations
                for key in match.split(','):
                    citekeys_used.add(key.strip())
    except FileNotFoundError:
        pass

print(f"Found {len(citekeys_used)} unique citekeys in LaTeX files")

# Create title -> paper mapping
title_to_paper = {}
for p in papers:
    title = p.get('title', '')
    url = p.get('url', '')
    if 'arxiv.org/abs/' in url:
        arxiv_id = url.split('arxiv.org/abs/')[1].split('.')[0]
        title_to_paper[title] = {
            'arxiv_id': arxiv_id,
            'url': url,
            'authors': p.get('authors', []),
            'date': p.get('date', ''),
            'title': title
        }

# Generate BibTeX entries for all citekeys used
def make_bibtex_entry(citekey, paper):
    """Generate a BibTeX entry for a paper."""
    if not paper:
        return None
    
    authors = paper['authors']
    if not authors:
        authors = ['Unknown']
    
    authors_bib = ' and '.join(authors)
    year = paper['date'][:4] if paper['date'] else '2026'
    
    # Clean title for various uses
    title = paper['title']
    
    entry = f"""@article{{{citekey},
  title = {{{title}}},
  author = {{{authors_bib}}},
  year = {{{year}}},
  url = {{{paper['url']}}},
  archivePrefix = {{{{arXiv}}}},
  eprint = {{{paper['arxiv_id']}}}
}}"""
    return entry

# Generate entries
entries = []
missing = []

for citekey in sorted(citekeys_used):
    # Try to find the paper
    paper = None
    
    # Try exact title match first
    for title, p in title_to_paper.items():
        if citekey.lower().replace('unknown', '').replace(' ', '') in title.lower().replace(' ', ''):
            paper = p
            break
    
    # Try arxiv ID match
    if not paper:
        # Extract year and keywords from citekey
        match = re.match(r'Unknown(\d{4})(\w+)', citekey)
        if match:
            year, keyword = match.groups()
            keyword = keyword.lower()
            for title, p in title_to_paper.items():
                if year in p['date'] and keyword.lower() in title.lower():
                    paper = p
                    break
    
    if paper:
        entry = make_bibtex_entry(citekey, paper)
        if entry:
            entries.append((citekey, entry))
    else:
        missing.append(citekey)

print(f"Generated {len(entries)} entries")
print(f"Missing {len(missing)} entries: {missing[:20]}")

# Write to file
with open('references_final.bib', 'w', encoding='utf-8') as f:
    f.write('% Auto-generated BibTeX from papers.yaml\n')
    f.write(f'% Generated: 2026-07-26\n')
    f.write(f'% Citekeys used: {len(citekeys_used)}\n')
    f.write(f'% Entries generated: {len(entries)}\n\n')
    for citekey, entry in entries:
        f.write(entry)
        f.write('\n\n')

print(f"\nSaved to references_final.bib")
