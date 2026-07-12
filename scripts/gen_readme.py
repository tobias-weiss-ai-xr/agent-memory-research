#!/usr/bin/env python3
"""Generate README paper list from papers.yaml without PyYAML."""
import re
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent

# Parse papers.yaml
entries = []
current = None
with open(BASE / 'papers.yaml') as f:
    for line in f:
        m = re.match(r'^-\s+title:\s+(.*)', line)
        if m:
            if current:
                entries.append(current)
            raw = m.group(1).strip()
            if raw.startswith("'") and raw.endswith("'"):
                raw = raw[1:-1]
            current = {'title': raw}
            continue
        if current is None:
            continue
        for key in ('date', 'category', 'subcategory', 'url', 'code_url'):
            m2 = re.match(r'\s+' + key + r':\s+(.*)', line)
            if m2:
                val = m2.group(1).strip()
                if val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]
                current[key] = val
if current:
    entries.append(current)

# Group by category then subcategory
cat_order = ['factual', 'experiential', 'working']
subcat_order = ['token-level', 'parametric', 'latent']
cat_display = {'factual': 'Factual Memory', 'experiential': 'Experiential Memory', 'working': 'Working Memory'}

groups = defaultdict(lambda: defaultdict(list))
for e in entries:
    cat = e.get('category', 'unknown')
    sub = e.get('subcategory', 'unknown')
    groups[cat][sub].append(e)

# Sort each group by date descending
for cat in groups:
    for sub in groups[cat]:
        groups[cat][sub].sort(key=lambda x: x.get('date', ''), reverse=True)

# Generate list
lines = ['## 📚 Paper list', '']
for cat in cat_order:
    if cat not in groups:
        continue
    lines.append(f'### {cat_display[cat]}')
    lines.append('')
    for sub in subcat_order:
        if sub not in groups[cat]:
            continue
        lines.append(f'#### {sub.capitalize()}')
        lines.append('')
        for e in groups[cat][sub]:
            date_display = e.get('date', '').replace('-', '/')
            title = e.get('title', '')
            url = e.get('url', '')
            code = e.get('code_url', '')
            entry = f'- [{date_display}] {title}. [[paper]({url})]'
            if code:
                entry += f' [[code]({code})]'
            lines.append(entry)
        lines.append('')

paper_list = '\n'.join(lines)

# Read current README
readme_path = BASE / 'README.md'
content = readme_path.read_text(encoding='utf-8')

start_marker = '## 📚 Paper list'
end_marker = '## 📖 Citation'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('ERROR: Could not find markers')
    exit(1)

before = content[:start_idx]
after = content[end_idx:]

new_content = before + paper_list + '\n' + after
readme_path.write_text(new_content, encoding='utf-8')
print(f'Updated README.md ({len(entries)} papers)')
