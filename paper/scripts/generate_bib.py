#!/usr/bin/env python3
"""Generate proper BibTeX citations from papers.yaml with arXiv IDs."""
import yaml
import re
from collections import defaultdict

# Load papers
with open('../papers.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    papers = data['papers']

# Create title -> arxiv_id mapping
title_to_arxiv = {}
for p in papers:
    title = p.get('title', '')
    url = p.get('url', '')
    if 'arxiv.org/abs/' in url:
        arxiv_id = url.split('arxiv.org/abs/')[1].split('.')[0]
        # Clean title for matching
        clean_title = re.sub(r'[^\w\s-]', '', title.lower())
        clean_title = re.sub(r'\s+', ' ', clean_title).strip()
        title_to_arxiv[clean_title] = {
            'arxiv_id': arxiv_id,
            'title': title,
            'authors': p.get('authors', []),
            'date': p.get('date', ''),
            'url': url
        }

# Print mapping for key papers
key_papers = [
    'MemGPT',
    'Generative Agents',
    'Mem0',
    'Zep',
    'Reflexion',
    'ExpeL',
    'HippoRAG',
    'Memorizing Transformer',
    'AgentPoison',
    'SCM',
    'Engram',
    'FadeMem',
    'MRAgent',
    'MAGMA',
    'MemVerse',
    'WorldMM',
    'TeleMem',
    'VisMem',
    'MemoryVLA',
    'CraniMem',
    'All-Mem',
    'MemRL',
    'LongMemEval',
    'MemBench',
    'MemoryAgentBench',
]

print("Key paper mappings:")
for keyword in key_papers:
    for clean_title, info in title_to_arxiv.items():
        if keyword.lower() in clean_title:
            print(f"  {keyword}: {info['arxiv_id']} - {info['title'][:60]}")
            break

# Generate BibTeX entries
print("\n\n=== BibTeX Entries ===\n")

def make_citekey(info):
    """Create a proper citekey from paper info."""
    authors = info['authors']
    if not authors:
        return f"Unknown{info['arxiv_id']}"
    
    first_author = authors[0].split()[-1]  # Last name
    year = info['date'][:4] if info['date'] else 'Unknown'
    
    # Clean title for key
    title = info['title']
    title_words = re.findall(r'\w+', title.lower())
    # Take first 2-3 meaningful words
    key_words = [w for w in title_words if len(w) > 4][:2]
    title_part = ''.join(word.capitalize() for word in key_words)
    
    return f"{first_author}{year}{title_part}"

# Generate entries for key papers
bibtex_entries = []
for clean_title, info in title_to_arxiv.items():
    citekey = make_citekey(info)
    authors_bib = ' and '.join(info['authors'])
    year = info['date'][:4] if info['date'] else '2026'
    
    entry = f"""@article{{{citekey},
  title = {{{info['title']}}},
  author = {{{authors_bib}}},
  year = {{{year}}},
  url = {{{info['url']}}},
  archivePrefix = {{{{arXiv}}}},
  eprint = {{{info['arxiv_id']}}}
}}"""
    bibtex_entries.append((citekey, entry))

# Print first 20 entries
for citekey, entry in bibtex_entries[:20]:
    print(entry)
    print()

# Save all entries
with open('references_new.bib', 'w', encoding='utf-8') as f:
    f.write('% Auto-generated BibTeX from papers.yaml\n')
    f.write('% Generated: 2026-07-26\n\n')
    for citekey, entry in bibtex_entries:
        f.write(entry)
        f.write('\n\n')

print(f"\n\nSaved {len(bibtex_entries)} entries to references_new.bib")
