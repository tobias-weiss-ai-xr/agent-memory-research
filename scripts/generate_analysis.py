#!/usr/bin/env python3
"""Parse papers.yaml (no PyYAML dependency) and generate papers.json + graph_analysis.html."""
import json
import re
import os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 1. Parse papers.yaml ──────────────────────────────────────────────
entries = []
current = None
with open(os.path.join(BASE, 'papers.yaml')) as f:
    for line in f:
        stripped = line.rstrip('\n')
        # New record
        m = re.match(r'^-\s+title:\s+(.*)', stripped)
        if m:
            if current:
                entries.append(current)
            raw = m.group(1).strip()
            # Remove surrounding quotes
            if len(raw) >= 2 and raw[0] == "'" and raw[-1] == "'":
                raw = raw[1:-1]
            current = {'title': raw}
            continue
        if current is None:
            continue
        # Fields
        for key in ('date', 'category', 'subcategory', 'venue', 'url', 'code_url', 'project_url', 'abstract'):
            m2 = re.match(r'\s+' + key + r':\s+(.*)', stripped)
            if m2:
                val = m2.group(1).strip()
                if len(val) >= 2 and val[0] == "'" and val[-1] == "'":
                    val = val[1:-1]
                current[key] = val
if current:
    entries.append(current)

print(f'Parsed {len(entries)} papers')

# ── 2. Compute statistics ────────────────────────────────────────────
cat_counter = Counter()
subcat_counter = Counter()
cat_subcat = defaultdict(lambda: defaultdict(int))
year_cat = defaultdict(lambda: Counter())
pub_dates = []

for e in entries:
    cat = e.get('category', 'unknown')
    sub = e.get('subcategory', 'unknown')
    cat_counter[cat] += 1
    subcat_counter[sub] += 1
    cat_subcat[cat][sub] += 1

    d = e.get('date', '')
    if d and len(d) >= 7:
        ym = d[:7]
        pub_dates.append((ym, cat))
        y = d[:4]
        year_cat[y][cat] += 1
    elif d and len(d) >= 4:
        y = d[:4]
        year_cat[y][cat] += 1

pub_dates.sort()

# ── 3. Write papers.json ─────────────────────────────────────────────
with open(os.path.join(BASE, 'docs', 'papers.json'), 'w') as f:
    json.dump(entries, f, indent=2)
print('Wrote docs/papers.json')

# ── 4. Generate graph_analysis.html ───────────────────────────────────
total = len(entries)
cat_order = ['factual', 'experiential', 'working']
subcat_order = ['token-level', 'parametric', 'latent']
cat_colors = {'factual': '#58a6ff', 'experiential': '#3fb950', 'working': '#d29922'}
subcat_colors = {'token-level': '#58a6ff', 'parametric': '#3fb950', 'latent': '#d29922'}

cat_vals = [cat_counter.get(c, 0) for c in cat_order]
subcat_vals = [subcat_counter.get(s, 0) for s in subcat_order]

# Heatmap data
heat = [[cat_subcat[c][s] for s in subcat_order] for c in cat_order]

# Timeline: all unique year-month sorted
ym_set = sorted(set(ym for ym, _ in pub_dates))
if not ym_set:
    ym_set = ['2024-01']
tl_factual = []
tl_experiential = []
tl_working = []
ym_counter = defaultdict(lambda: Counter())
for ym, cat in pub_dates:
    ym_counter[ym][cat] += 1
for ym in ym_set:
    tl_factual.append(ym_counter[ym].get('factual', 0))
    tl_experiential.append(ym_counter[ym].get('experiential', 0))
    tl_working.append(ym_counter[ym].get('working', 0))

# Cumulative
cum_factual = []
cum_exp = []
cum_work = []
f, e, w = 0, 0, 0
for i, ym in enumerate(ym_set):
    f += tl_factual[i]
    e += tl_experiential[i]
    w += tl_working[i]
    cum_factual.append(f)
    cum_exp.append(e)
    cum_work.append(w)

# Venue distribution
venue_counter = Counter()
for e in entries:
    v = e.get('venue', '')
    if v:
        venue_counter[v] += 1
    else:
        venue_counter['Unknown/None'] += 1

# Get top venues (excluding Unknown/None for top chart, include it in the count)
top_venues = [(v, n) for v, n in venue_counter.most_common(12) if v != 'Unknown/None']
if venue_counter.get('Unknown/None', 0) > 0:
    top_venues.append(('Unknown/None', venue_counter['Unknown/None']))

venue_labels = json.dumps([v for v, _ in top_venues])
venue_values = json.dumps([n for _, n in top_venues])

# Top authors
authors_counter = Counter()
for e in entries:
    # Skip authors field if empty
    pass

# ── Recent 20 papers ─────────────────────────────────────────────────
sorted_entries = sorted(entries, key=lambda x: x.get('date', ''), reverse=True)
recent = sorted_entries[:20]

recent_rows = ''
for e in recent:
    title = e.get('title', '')
    date = e.get('date', '')
    cat = e.get('category', '')
    sub = e.get('subcategory', '')
    url = e.get('url', '')
    if url:
        row = f'<tr><td>{date}</td><td><a href="{url}" target="_blank">{title}</a></td><td>{cat}</td><td>{sub}</td></tr>\n'
    else:
        row = f'<tr><td>{date}</td><td>{title}</td><td>{cat}</td><td>{sub}</td></tr>\n'
    recent_rows += row

# Date ranges
def get_dates(cat):
    dates = [e.get('date', '') for e in entries if e.get('category') == cat and e.get('date')]
    dates.sort()
    if dates:
        return f'{dates[0]} – {dates[-1]}'
    return 'N/A'

# Generate HTML
HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Memory Research - Graph Analysis</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: #0f1117; color: #e1e4e8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 24px; }}
h1 {{ font-size: 1.8rem; margin-bottom: 8px; color: #f0f6fc; }}
h2 {{ font-size: 1.2rem; margin: 24px 0 12px; color: #79c0ff; }}
.stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 24px; }}
.stat-card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }}
.stat-card .num {{ font-size: 1.8rem; font-weight: 700; color: #58a6ff; }}
.stat-card .label {{ font-size: 0.85rem; color: #8b949e; margin-top: 4px; }}
.chart-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }}
.chart-box {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }}
.chart-box.full {{ grid-column: 1 / -1; }}
canvas {{ max-height: 400px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; }}
th {{ text-align: left; padding: 8px 10px; border-bottom: 2px solid #30363d; color: #79c0ff; font-weight: 600; }}
td {{ padding: 7px 10px; border-bottom: 1px solid #21262d; }}
tr:hover td {{ background: #1c2128; }}
a {{ color: #58a6ff; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.heatmap-container {{ position: relative; width: 100%; max-width: 500px; margin: 0 auto; }}
.heatmap-canvas {{ width: 100%; height: auto; }}
.heatmap-cell {{ font-weight: 700; font-size: 0.9rem; }}
@media (max-width: 768px) {{ .chart-row {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>

<h1>Agent Memory Research Papers</h1>
<p style="color: #8b949e; margin-bottom: 16px;">Analysis of {total} papers on memory for LLM agents</p>

<div class="stats-grid">
  <div class="stat-card"><div class="num">{total}</div><div class="label">Total Papers</div></div>
  <div class="stat-card"><div class="num">{cat_counter.get('factual',0)}</div><div class="label">Factual Memory</div></div>
  <div class="stat-card"><div class="num">{cat_counter.get('experiential',0)}</div><div class="label">Experiential Memory</div></div>
  <div class="stat-card"><div class="num">{cat_counter.get('working',0)}</div><div class="label">Working Memory</div></div>
</div>

<div class="stats-grid">
  <div class="stat-card"><div class="num">{subcat_counter.get('token-level',0)}</div><div class="label">Token-level</div></div>
  <div class="stat-card"><div class="num">{subcat_counter.get('parametric',0)}</div><div class="label">Parametric</div></div>
  <div class="stat-card"><div class="num">{subcat_counter.get('latent',0)}</div><div class="label">Latent</div></div>
</div>

<h2>Category × Subcategory Heatmap</h2>
<div class="chart-box full" style="max-width: 520px;">
<canvas id="heatmapChart"></canvas>
</div>

<h2>Category Distribution</h2>
<div class="chart-row">
  <div class="chart-box"><canvas id="catChart"></canvas></div>
  <div class="chart-box"><canvas id="subcatChart"></canvas></div>
</div>

<h2>Publication Timeline (Monthly)</h2>
<div class="chart-box full">
<canvas id="timelineChart"></canvas>
</div>

<h2>Cumulative Growth</h2>
<div class="chart-box full">
<canvas id="cumulativeChart"></canvas>
</div>

<h2>Category Trends Over Time</h2>
<div class="chart-box full">
<canvas id="stackedTimelineChart"></canvas>
</div>

<h2>Venue Distribution</h2>
<div class="chart-box full">
<canvas id="venueChart"></canvas>
</div>

<h2>Date Ranges by Category</h2>
<div class="stats-grid">
  <div class="stat-card"><div class="num">{get_dates('factual')}</div><div class="label">Factual ({cat_counter.get('factual',0)} papers)</div></div>
  <div class="stat-card"><div class="num">{get_dates('experiential')}</div><div class="label">Experiential ({cat_counter.get('experiential',0)} papers)</div></div>
  <div class="stat-card"><div class="num">{get_dates('working')}</div><div class="label">Working ({cat_counter.get('working',0)} papers)</div></div>
</div>

<h2>20 Most Recent Papers</h2>
<table>
<thead><tr><th>Date</th><th>Title</th><th>Category</th><th>Subcategory</th></tr></thead>
<tbody>
{recent_rows}</tbody>
</table>

<script>
const catLabels = {json.dumps(cat_order)};
const catValues = {json.dumps(cat_vals)};
const catColors = {json.dumps([cat_colors[c] for c in cat_order])};

const subcatLabels = {json.dumps(subcat_order)};
const subcatValues = {json.dumps(subcat_vals)};
const subcatColors = {json.dumps([subcat_colors[s] for s in subcat_order])};

const tlLabels = {json.dumps(ym_set)};
const tlFactual = {json.dumps(tl_factual)};
const tlExperiential = {json.dumps(tl_experiential)};
const tlWorking = {json.dumps(tl_working)};

const cumFactual = {json.dumps(cum_factual)};
const cumExperiential = {json.dumps(cum_exp)};
const cumWorking = {json.dumps(cum_work)};

const heatData = {json.dumps(heat)};

const venueLabels = {venue_labels};
const venueValues = {venue_values};
const venueColors = ['#58a6ff','#3fb950','#d29922','#f0883e','#db6d8a','#7ee787','#a5d6ff','#79c0ff','#8b949e','#6e7681','#484f58','#30363d'];

new Chart(document.getElementById('catChart'), {{
  type: 'bar',
  data: {{
    labels: catLabels,
    datasets: [{{
      label: 'Papers',
      data: catValues,
      backgroundColor: catColors,
      borderRadius: 4
    }}]
  }},
  options: {{
    responsive: true,
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8b949e' }}, grid: {{ color: '#21262d' }} }},
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

new Chart(document.getElementById('subcatChart'), {{
  type: 'bar',
  data: {{
    labels: subcatLabels,
    datasets: [{{
      label: 'Papers',
      data: subcatValues,
      backgroundColor: subcatColors,
      borderRadius: 4
    }}]
  }},
  options: {{
    responsive: true,
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8b949e' }}, grid: {{ color: '#21262d' }} }},
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

new Chart(document.getElementById('timelineChart'), {{
  type: 'line',
  data: {{
    labels: tlLabels,
    datasets: [
      {{ label: 'Factual', data: tlFactual, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.1)', fill: true, tension: 0.3, pointRadius: 2 }},
      {{ label: 'Experiential', data: tlExperiential, borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.1)', fill: true, tension: 0.3, pointRadius: 2 }},
      {{ label: 'Working', data: tlWorking, borderColor: '#d29922', backgroundColor: 'rgba(210,153,34,0.1)', fill: true, tension: 0.3, pointRadius: 2 }}
    ]
  }},
  options: {{
    responsive: true,
    interaction: {{ mode: 'index', intersect: false }},
    plugins: {{ legend: {{ labels: {{ color: '#8b949e' }} }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8b949e', maxTicksLimit: 25 }}, grid: {{ color: '#21262d' }} }},
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

new Chart(document.getElementById('cumulativeChart'), {{
  type: 'line',
  data: {{
    labels: tlLabels,
    datasets: [
      {{ label: 'Factual', data: cumFactual, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.05)', fill: true, tension: 0.3, pointRadius: 1 }},
      {{ label: 'Experiential', data: cumExperiential, borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.05)', fill: true, tension: 0.3, pointRadius: 1 }},
      {{ label: 'Working', data: cumWorking, borderColor: '#d29922', backgroundColor: 'rgba(210,153,34,0.05)', fill: true, tension: 0.3, pointRadius: 1 }}
    ]
  }},
  options: {{
    responsive: true,
    interaction: {{ mode: 'index', intersect: false }},
    plugins: {{ legend: {{ labels: {{ color: '#8b949e' }} }} }},
    scales: {{
      x: {{ ticks: {{ color: '#8b949e', maxTicksLimit: 25 }}, grid: {{ color: '#21262d' }} }},
      y: {{ beginAtZero: true, ticks: {{ stepSize: 10, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

new Chart(document.getElementById('stackedTimelineChart'), {{
  type: 'bar',
  data: {{
    labels: tlLabels,
    datasets: [
      {{ label: 'Factual', data: tlFactual, backgroundColor: '#58a6ff', borderRadius: 2 }},
      {{ label: 'Experiential', data: tlExperiential, backgroundColor: '#3fb950', borderRadius: 2 }},
      {{ label: 'Working', data: tlWorking, backgroundColor: '#d29922', borderRadius: 2 }}
    ]
  }},
  options: {{
    responsive: true,
    scales: {{
      x: {{ stacked: true, ticks: {{ color: '#8b949e', maxTicksLimit: 25 }}, grid: {{ color: '#21262d' }} }},
      y: {{ stacked: true, beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }},
    plugins: {{ legend: {{ labels: {{ color: '#8b949e' }} }} }}
  }}
}});

new Chart(document.getElementById('venueChart'), {{
  type: 'bar',
  data: {{
    labels: venueLabels,
    datasets: [{{
      label: 'Papers',
      data: venueValues,
      backgroundColor: venueColors.slice(0, venueLabels.length),
      borderRadius: 4
    }}]
  }},
  options: {{
    indexAxis: 'y',
    responsive: true,
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }},
      y: {{ ticks: {{ color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}
    }}
  }}
}});

// Heatmap using matrix plugin approach
const heatCtx = document.getElementById('heatmapChart').getContext('2d');
const cellW = 90, cellH = 50, pad = 2;
const catNames = ['Factual', 'Experiential', 'Working'];
const subNames = ['Token-level', 'Parametric', 'Latent'];
const w = cellW * 3 + 120, h = cellH * 3 + 60;

heatCtx.canvas.width = w;
heatCtx.canvas.height = h;

function drawHeatmap() {{
  heatCtx.clearRect(0, 0, w, h);
  const maxVal = Math.max(...heatData.flat());
  // headers
  heatCtx.fillStyle = '#8b949e';
  heatCtx.font = '13px sans-serif';
  heatCtx.textAlign = 'center';
  heatCtx.textBaseline = 'middle';
  for (let j = 0; j < 3; j++) {{
    heatCtx.fillText(subNames[j], 120 + j * cellW + cellW/2, 20);
  }}
  heatCtx.textAlign = 'right';
  for (let i = 0; i < 3; i++) {{
    heatCtx.fillText(catNames[i], 110, 60 + i * cellH + cellH/2);
  }}
  for (let i = 0; i < 3; i++) {{
    for (let j = 0; j < 3; j++) {{
      const v = heatData[i][j];
      const frac = maxVal > 0 ? v / maxVal : 0;
      const r = Math.round(15 + frac * 50);
      const g = Math.round(70 + frac * 120);
      const b = Math.round(140 + frac * 115);
      heatCtx.fillStyle = `rgb(${{r}},${{g}},${{b}})`;
      heatCtx.fillRect(120 + j * cellW + pad, 55 + i * cellH + pad, cellW - pad*2, cellH - pad*2);
      heatCtx.fillStyle = '#e1e4e8';
      heatCtx.font = 'bold 16px sans-serif';
      heatCtx.textAlign = 'center';
      heatCtx.textBaseline = 'middle';
      heatCtx.fillText(v, 120 + j * cellW + cellW/2, 55 + i * cellH + cellH/2);
    }}
  }}
}}

drawHeatmap();
</script>
</body>
</html>'''

with open(os.path.join(BASE, 'docs', 'graph_analysis.html'), 'w') as f:
    f.write(HTML)
print(f'Wrote docs/graph_analysis.html ({len(HTML)} bytes)')
