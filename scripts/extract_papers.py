#!/usr/bin/env python3
"""One-time extraction script: parse README.md paper list into papers.yaml."""

import re
import yaml
from pathlib import Path


CATEGORY_MAP = {
    "Factual Memory": "factual",
    "Experiential Memory": "experiential",
    "Working Memory": "working",
}

SUBCATEGORY_MAP = {
    "Token-level": "token-level",
    "Parametric": "parametric",
    "Latent": "latent",
}


def fix_latex(title):
    patterns = [
        ("R{\\({^3}\\)}Mem", "R³Mem"),
        ("S${}^3$", "S³"),
        ("Memory${}^3$", "Memory³"),
        ("H${}^2$R", "H²R"),
    ]
    for pattern, replacement in patterns:
        title = re.sub(re.escape(pattern), replacement, title)
    return title.strip()


def normalize_url(url):
    url = url.strip()
    m = re.match(r"https?://(?:www\.)?(?:dx\.)?doi\.org/10\.48550/[Aa][Rr][Xx][Ii][Vv]\.(\S+)", url)
    if m:
        return f"https://arxiv.org/abs/{m.group(1)}"
    m = re.match(r"https?://(?:www\.)?arxiv\.org/abs/(\S+)", url)
    if m:
        return f"https://arxiv.org/abs/{m.group(1)}"
    if url.startswith("http://"):
        url = "https://" + url[len("http://"):]
    return url


def parse_entry(line):
    # Match: - [YYYY/MM] Title text [[paper](url)] or [[paper]](url) (broken markdown)
    # Also handles entries without period before link
    m = re.match(
        r'^- \[(\d{4}/\d{2})\]\s+(.+?)\s*\[\[paper\]\]?\((https?://[^\)]+)\)',
        line
    )
    if m:
        date_raw = m.group(1)
        title = m.group(2).strip()
        url = m.group(3)
        if title.endswith("."):
            title = title[:-1].strip()
        return {
            "title": fix_latex(title),
            "date": date_raw.replace("/", "-"),
            "url": normalize_url(url),
        }
    return None


def main():
    readme_path = Path(__file__).parent.parent / "README.md"
    output_path = Path(__file__).parent.parent / "papers.yaml"

    lines = readme_path.read_text(encoding="utf-8").splitlines()

    papers = []
    current_category = None
    current_subcategory = None
    in_paper_list = False
    entry_count = 0
    seen = set()

    for line in lines:
        stripped = line.strip()

        if stripped == "## 📚 Paper list":
            in_paper_list = True
            continue
        if in_paper_list and stripped.startswith("## "):
            break

        if not in_paper_list:
            continue

        cat_m = re.match(r"^### (.+)", line)
        if cat_m:
            current_category = CATEGORY_MAP.get(cat_m.group(1).strip())
            continue

        subcat_m = re.match(r"^#### (.+)", line)
        if subcat_m:
            current_subcategory = SUBCATEGORY_MAP.get(subcat_m.group(1).strip())
            continue

        if not current_category or not current_subcategory:
            continue

        if not stripped.startswith("- ["):
            continue

        entry = parse_entry(stripped)
        if not entry:
            continue

        key = (entry["url"], current_category, current_subcategory)
        if key in seen:
            continue
        seen.add(key)

        entry["category"] = current_category
        entry["subcategory"] = current_subcategory
        entry["authors"] = []
        entry["venue"] = ""
        entry["code_url"] = ""
        entry["project_url"] = ""
        entry["abstract"] = ""
        entry["tags"] = []
        papers.append(entry)
        entry_count += 1

    category_order = ["factual", "experiential", "working"]
    subcategory_order = ["token-level", "parametric", "latent"]

    grouped = {}
    for p in papers:
        grouped.setdefault((p["category"], p["subcategory"]), []).append(p)

    sorted_papers = []
    for cat in category_order:
        for sub in subcategory_order:
            group = grouped.get((cat, sub), [])
            group.sort(key=lambda x: x["date"], reverse=True)
            sorted_papers.extend(group)

    data = {"papers": sorted_papers}
    output_path.write_text(
        yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )

    print(f"Extracted {entry_count} papers into {output_path}")
    for cat in category_order:
        for sub in subcategory_order:
            count = len(grouped.get((cat, sub), []))
            if count:
                print(f"  {cat}/{sub}: {count}")


if __name__ == "__main__":
    main()
