# Contributing to Agent Memory Paper List

Thank you for your interest in contributing! This guide explains how to add papers to the list.

## Overview

This repository maintains a curated list of papers related to **memory in AI agents**, supporting the survey [Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564).

The source of truth is `papers.yaml`. The `README.md` is **auto-generated** from `papers.yaml` — never edit it directly.

## Quick Start: Adding a Paper

1. **Check for duplicates** — search `papers.yaml` by title and URL. If the paper already exists, skip.
2. **Edit `papers.yaml`** — add your entry following the schema below.
3. **Validate** — run `python3 scripts/validate_papers.py`
4. **Regenerate README** — run `python3 scripts/generate_readme.py`
5. **Commit and open a PR** — see the PR checklist below.

## papers.yaml Schema

```yaml
papers:
  - title: "Paper Title"            # Required
    date: "2026-01"                  # Required, YYYY-MM format
    url: "https://arxiv.org/abs/XXXX"  # Required, normalized arXiv URL
    category: "factual"             # Required: factual | experiential | working
    subcategory: "token-level"       # Required: token-level | parametric | latent
    # Optional fields:
    authors: ["Author1", "Author2"]
    venue: "NeurIPS 2025"
    code_url: "https://github.com/..."
    project_url: "https://..."
    abstract: "..."
    tags: ["tag1", "tag2"]
```

## URL Normalization Rules

- **arXiv papers**: always use `https://arxiv.org/abs/XXXX` format
  - Do NOT use `https://doi.org/10.48550/arXiv.XXXX`
  - Do NOT use `https://www.arxiv.org/abs/XXXX`
  - Do NOT use `https://arxiv.org/pdf/XXXX`
- **Non-arXiv papers**: keep URLs as-is (e.g., `aclanthology.org`, `openreview.net`, `papers.nips.cc`)

## Taxonomy Guide

### Category (function — why agents need memory)

| Category | Description | Examples |
|----------|-------------|----------|
| **factual** | Knowledge facts, world knowledge, personal profiles | Entity knowledge bases, user profiles, factual QA |
| **experiential** | Skills, procedures, experience-driven learning | Tool usage skills, task trajectories, in-context learning |
| **working** | Active context management, context compression, KV cache | Long-context management, KV cache compression, context window strategies |

### Subcategory (form — what carries memory)

| Subcategory | Description | Examples |
|-------------|-------------|----------|
| **token-level** | Explicit text/graph storage in context | Memory strings, knowledge graphs, structured context |
| **parametric** | Model weights, LoRA, knowledge editing | LoRA adapters, knowledge injection, model editing |
| **latent** | Hidden states, KV cache, soft prompts | KV cache retention, soft prompts, attention sink management |

A paper may belong to one category/subcategory combination. If a paper spans multiple, choose the **primary** contribution.

## Deduplication Checklist

Before adding a paper, check that it is not already in the list:

1. Search `papers.yaml` by **title** (case-insensitive)
2. Search `papers.yaml` by **URL**
3. If the same paper appears under a different category, that is acceptable — each unique (title, category, subcategory) triple is valid

## Local Development Setup

```bash
pip install -r requirements.txt
```

### Useful Commands

| Command | Description |
|---------|-------------|
| `python3 scripts/validate_papers.py` | Validate `papers.yaml` for errors |
| `python3 scripts/validate_papers.py --fix` | Validate and auto-fix URL normalization |
| `python3 scripts/generate_readme.py` | Regenerate `README.md` from `papers.yaml` |
| `python3 scripts/generate_readme.py --check` | Check if README is up-to-date (CI use) |
| `python3 scripts/fetch_metadata.py` | Fetch authors/venue/abstract from arXiv and Semantic Scholar |
| `python3 scripts/fetch_metadata.py --dry-run` | Preview metadata fetches without modifying files |
| `python3 scripts/fetch_new_papers.py` | Discover new agent memory papers from arXiv |
| `python3 scripts/fetch_new_papers.py --dry-run` | Preview new papers without creating anything |

## PR Process

1. Fork this repository
2. Create a branch: `git checkout -b add-paper-name`
3. Edit `papers.yaml` to add your paper entry
4. Run the validator: `python3 scripts/validate_papers.py`
5. Run the README generator: `python3 scripts/generate_readme.py`
6. Commit your changes
7. Open a pull request

## PR Checklist

- [ ] Added entry to `papers.yaml` (not `README.md`)
- [ ] Used normalized URL format (`https://arxiv.org/abs/XXXX`)
- [ ] Checked for duplicates (searched by title and URL)
- [ ] Ran `python3 scripts/validate_papers.py` — no errors
- [ ] Ran `python3 scripts/generate_readme.py` — README updated
- [ ] Used correct date format (YYYY-MM)
