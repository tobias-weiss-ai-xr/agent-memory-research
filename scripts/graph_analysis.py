#!/usr/bin/env python3
"""Generate a comprehensive graph analysis HTML page from papers.json."""

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR / "docs" / "papers.json"
HTML_PATH = BASE_DIR / "docs" / "graph_analysis.html"


def load_papers():
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
    return data.get("papers", [])


def compute_stats(papers):
    total = len(papers)
    category_counts = Counter(p["category"] for p in papers)
    subcategory_counts = Counter(p["subcategory"] for p in papers)

    dates = sorted(set(p["date"] for p in papers if p.get("date")))
    date_range = (dates[0], dates[-1]) if dates else ("", "")

    cat_sub = defaultdict(lambda: defaultdict(int))
    for p in papers:
        cat_sub[p["category"]][p["subcategory"]] += 1

    sorted_papers = sorted(papers, key=lambda p: p.get("date", ""), reverse=True)
    recent_20 = sorted_papers[:20]

    timeline = Counter()
    for p in papers:
        d = p.get("date", "")
        if d:
            timeline[d] += 1

    return {
        "total": total,
        "category_counts": dict(category_counts),
        "subcategory_counts": dict(subcategory_counts),
        "date_range": date_range,
        "cat_sub": {k: dict(v) for k, v in cat_sub.items()},
        "recent_20": recent_20,
        "timeline": dict(sorted(timeline.items())),
    }


def build_html(stats):
    cats_json = json.dumps(list(stats["category_counts"].keys()))
    cat_vals_json = json.dumps(list(stats["category_counts"].values()))
    subcats_json = json.dumps(list(stats["subcategory_counts"].keys()))
    subcat_vals_json = json.dumps(list(stats["subcategory_counts"].values()))
    timeline_labels = json.dumps(list(stats["timeline"].keys()))
    timeline_vals = json.dumps(list(stats["timeline"].values()))

    heatmap_cats = json.dumps(list(stats["cat_sub"].keys()))
    heatmap_subcats = json.dumps(
        sorted(
            set(
                sc for v in stats["cat_sub"].values() for sc in v.keys()
            )
        )
    )
    heatmap_data = json.dumps(
        [
            [stats["cat_sub"].get(c, {}).get(sc, 0) for sc in json.loads(heatmap_subcats)]
            for c in json.loads(heatmap_cats)
        ]
    )

    recent_rows = ""
    for p in stats["recent_20"]:
        title = p.get("title", "")
        date = p.get("date", "")
        url = p.get("url", "")
        cat = p.get("category", "")
        sub = p.get("subcategory", "")
        link = f'<a href="{url}" target="_blank">{title}</a>' if url else title
        recent_rows += f"<tr><td>{link}</td><td>{date}</td><td>{cat}</td><td>{sub}</td></tr>\n"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent Memory Research - Graph Analysis</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: #0f1117; color: #e1e4e8; font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; padding: 2rem; }}
h1 {{ font-size: 2rem; margin-bottom: 0.5rem; color: #f0f6fc; }}
h2 {{ font-size: 1.3rem; margin: 2rem 0 1rem; color: #f0f6fc; border-bottom: 1px solid #21262d; padding-bottom: 0.5rem; }}
.summary {{ display: flex; gap: 1.5rem; flex-wrap: wrap; margin: 1.5rem 0; }}
.stat-card {{ background: #161b22; border: 1px solid #21262d; border-radius: 8px; padding: 1.2rem 1.5rem; min-width: 140px; }}
.stat-card .num {{ font-size: 2rem; font-weight: 700; color: #58a6ff; }}
.stat-card .label {{ font-size: 0.85rem; color: #8b949e; margin-top: 0.25rem; }}
.chart-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0; }}
.chart-box {{ background: #161b22; border: 1px solid #21262d; border-radius: 8px; padding: 1rem; }}
.chart-box.full {{ grid-column: 1 / -1; }}
.chart-box canvas {{ max-height: 350px; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; background: #161b22; border: 1px solid #21262d; border-radius: 8px; overflow: hidden; }}
th, td {{ padding: 0.6rem 1rem; text-align: left; border-bottom: 1px solid #21262d; }}
th {{ background: #1c2128; color: #8b949e; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; }}
td {{ font-size: 0.85rem; }}
tr:last-child td {{ border-bottom: none; }}
a {{ color: #58a6ff; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.footer {{ margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #21262d; color: #484f58; font-size: 0.8rem; text-align: center; }}
@media (max-width: 800px) {{ .chart-grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<h1>Agent Memory Research — Graph Analysis</h1>
<p style="color:#8b949e;">Comprehensive quantitative analysis of the agent memory literature corpus.</p>

<div class="summary">
<div class="stat-card"><div class="num">{stats['total']}</div><div class="label">Total Papers</div></div>
<div class="stat-card"><div class="num">{stats['category_counts'].get('factual', 0)}</div><div class="label">Factual Memory</div></div>
<div class="stat-card"><div class="num">{stats['category_counts'].get('experiential', 0)}</div><div class="label">Experiential Memory</div></div>
<div class="stat-card"><div class="num">{stats['category_counts'].get('working', 0)}</div><div class="label">Working Memory</div></div>
<div class="stat-card"><div class="num">{stats['date_range'][0]} — {stats['date_range'][1]}</div><div class="label">Date Range</div></div>
</div>

<div class="chart-grid">
<div class="chart-box">
<h2>Distribution by Category</h2>
<canvas id="chartCategory"></canvas>
</div>
<div class="chart-box">
<h2>Distribution by Subcategory</h2>
<canvas id="chartSubcategory"></canvas>
</div>
<div class="chart-box full">
<h2>Publication Timeline</h2>
<canvas id="chartTimeline"></canvas>
</div>
<div class="chart-box full">
<h2>Category × Subcategory Heatmap</h2>
<canvas id="chartHeatmap"></canvas>
</div>
</div>

<h2>Most Recent 20 Papers</h2>
<table>
<thead><tr><th>Title</th><th>Date</th><th>Category</th><th>Subcategory</th></tr></thead>
<tbody>{recent_rows}</tbody>
</table>

<div class="footer">Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} &mdash; Agent Memory Research</div>

<script>
const COLORS = {{
factual: '#58a6ff', experiential: '#3fb950', working: '#d29922',
'token-level': '#58a6ff', parametric: '#3fb950', latent: '#d29922'
}};
const BG = {{
factual: 'rgba(88,166,255,0.7)', experiential: 'rgba(63,185,80,0.7)', working: 'rgba(210,153,34,0.7)',
'token-level': 'rgba(88,166,255,0.7)', parametric: 'rgba(63,185,80,0.7)', latent: 'rgba(210,153,34,0.7)'
}};

new Chart(document.getElementById('chartCategory'), {{
type: 'bar',
data: {{
labels: {cats_json},
datasets: [{{ label: 'Papers', data: {cat_vals_json}, backgroundColor: {cats_json}.map(c => BG[c]), borderColor: {cats_json}.map(c => COLORS[c]), borderWidth: 2, borderRadius: 4 }}]
}},
options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }} }}, scales: {{ y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }} }}, x: {{ ticks: {{ color: '#8b949e' }}, grid: {{ display: false }} }} }} }}
}});

new Chart(document.getElementById('chartSubcategory'), {{
type: 'bar',
data: {{
labels: {subcats_json},
datasets: [{{ label: 'Papers', data: {subcat_vals_json}, backgroundColor: {subcats_json}.map(c => BG[c]), borderColor: {subcats_json}.map(c => COLORS[c]), borderWidth: 2, borderRadius: 4 }}]
}},
options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }} }}, scales: {{ y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }}}}, x: {{ ticks: {{ color: '#8b949e' }}, grid: {{ display: false }} }} }} }}
}});

new Chart(document.getElementById('chartTimeline'), {{
type: 'line',
data: {{
labels: {timeline_labels},
datasets: [{{ label: 'Papers', data: {timeline_vals}, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.1)', fill: true, tension: 0.3, pointRadius: 3, pointBackgroundColor: '#58a6ff' }}]
}},
options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }} }}, scales: {{ y: {{ beginAtZero: true, ticks: {{ stepSize: 1, color: '#8b949e' }}, grid: {{ color: '#21262d' }}}}, x: {{ ticks: {{ color: '#8b949e', maxRotation: 45 }}, grid: {{ display: false }} }} }} }}
}});

(function() {{
const cats = {heatmap_cats};
const subcats = {heatmap_subcats};
const data = {heatmap_data};
const maxVal = Math.max(...data.flat(), 1);
const canvas = document.getElementById('chartHeatmap');
const ctx = canvas.getContext('2d');
const cellW = canvas.width / (subcats.length + 1) * 0.7;
const cellH = canvas.height / (cats.length + 1) * 0.7;
const offX = canvas.width * 0.18;
const offY = canvas.height * 0.12;
ctx.clearRect(0, 0, canvas.width, canvas.height);
ctx.fillStyle = '#8b949e';
ctx.font = '12px sans-serif';
ctx.textAlign = 'right';
ctx.textBaseline = 'middle';
cats.forEach((c, i) => {{ ctx.fillStyle = '#e1e4e8'; ctx.fillText(c, offX - 8, offY + i * cellH + cellH / 2); }});
ctx.textAlign = 'center';
ctx.textBaseline = 'bottom';
subcats.forEach((s, j) => {{ ctx.fillStyle = '#e1e4e8'; ctx.fillText(s, offX + j * cellW + cellW / 2, offY - 8); }});
for (let i = 0; i < cats.length; i++) {{
for (let j = 0; j < subcats.length; j++) {{
const v = data[i][j];
const alpha = v / maxVal;
const grad = ctx.createRadialGradient(offX + j * cellW + cellW / 2, offY + i * cellH + cellH / 2, 0, offX + j * cellW + cellW / 2, offY + i * cellH + cellH / 2, cellW * 0.6);
grad.addColorStop(0, `rgba(88, 166, 255, ${{0.3 + alpha * 0.7}})`);
grad.addColorStop(1, `rgba(88, 166, 255, ${{alpha * 0.5}})`);
ctx.fillStyle = grad;
ctx.fillRect(offX + j * cellW + 2, offY + i * cellH + 2, cellW - 4, cellH - 4);
ctx.fillStyle = alpha > 0.5 ? '#0f1117' : '#e1e4e8';
ctx.font = 'bold 14px sans-serif';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillText(v, offX + j * cellW + cellW / 2, offY + i * cellH + cellH / 2);
}}
}}
}})();
</script>
</body>
</html>"""
    return html


def main():
    papers = load_papers()
    stats = compute_stats(papers)
    html = build_html(stats)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"HTML generated: {HTML_PATH.resolve()}")
    print(f"Total papers: {stats['total']}")
    print(f"Categories: {stats['category_counts']}")
    print(f"Subcategories: {stats['subcategory_counts']}")
    print(f"Date range: {stats['date_range'][0]} to {stats['date_range'][1]}")


if __name__ == "__main__":
    main()
