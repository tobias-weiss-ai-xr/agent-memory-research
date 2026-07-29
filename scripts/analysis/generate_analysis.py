#!/usr/bin/env python3
"""Generate enhanced graph_analysis.html with D3 force-directed graph + comprehensive analysis."""
import json
import re
import os
import yaml
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 1. Parse papers.yaml ──────────────────────────────────────────────
with open(os.path.join(BASE, 'papers.yaml'), encoding='utf-8') as f:
    _data = yaml.safe_load(f)
entries = _data.get('papers', [])
print(f'Parsed {len(entries)} papers')

# ── 2. Statistics ─────────────────────────────────────────────────────
cat_counter = Counter()
subcat_counter = Counter()
cat_subcat = defaultdict(lambda: defaultdict(int))
pub_dates = []
venue_counter = Counter()

for e in entries:
    cat = e.get('category','unknown')
    sub = e.get('subcategory','unknown')
    cat_counter[cat] += 1
    subcat_counter[sub] += 1
    cat_subcat[cat][sub] += 1
    d = e.get('date','')
    if d and len(d) >= 7:
        pub_dates.append((d[:7], cat, sub))
    v = e.get('venue','')
    if v:
        venue_counter[v] += 1
    else:
        venue_counter['Unknown/None'] += 1

total = len(entries)
cat_order = ['factual','experiential','working']
subcat_order = ['token-level','parametric','latent']
cat_colors = {'factual':'#58a6ff','experiential':'#3fb950','working':'#d29922'}
subcat_colors = {'token-level':'#58a6ff','parametric':'#3fb950','latent':'#d29922'}
cat_vals = [cat_counter.get(c,0) for c in cat_order]
subcat_vals = [subcat_counter.get(s,0) for s in subcat_order]
heat = [[cat_subcat[c][s] for s in subcat_order] for c in cat_order]

# Timeline by category
ym_set = sorted(set(ym for ym,_,_ in pub_dates))
if not ym_set: ym_set = ['2024-01']
ym_cat_counter = defaultdict(lambda: Counter())
ym_sub_counter = defaultdict(lambda: Counter())
ym_total_counter = Counter()
for ym,cat,sub in pub_dates:
    ym_cat_counter[ym][cat] += 1
    ym_sub_counter[ym][sub] += 1
    ym_total_counter[ym] += 1

tl_factual = [ym_cat_counter[ym].get('factual',0) for ym in ym_set]
tl_exp = [ym_cat_counter[ym].get('experiential',0) for ym in ym_set]
tl_work = [ym_cat_counter[ym].get('working',0) for ym in ym_set]
tl_sub_token = [ym_sub_counter[ym].get('token-level',0) for ym in ym_set]
tl_sub_param = [ym_sub_counter[ym].get('parametric',0) for ym in ym_set]
tl_sub_latent = [ym_sub_counter[ym].get('latent',0) for ym in ym_set]
tl_total = [ym_total_counter[ym] for ym in ym_set]

# Cumulative
cum_f, cum_e, cum_w = [], [], []
f=e=w=0
for i,ym in enumerate(ym_set):
    f+=tl_factual[i]; e+=tl_exp[i]; w+=tl_work[i]
    cum_f.append(f); cum_e.append(e); cum_w.append(w)

cum_total = []
t=0
for i in range(len(ym_set)):
    t += tl_total[i]
    cum_total.append(t)

# 3-month rolling average
def rolling_avg(data, window=3):
    result = []
    for i in range(len(data)):
        start = max(0, i-window+1)
        result.append(sum(data[start:i+1])/(i-start+1))
    return result

roll_factual = rolling_avg(tl_factual)
roll_exp = rolling_avg(tl_exp)
roll_work = rolling_avg(tl_work)
roll_total = rolling_avg(tl_total)

# Year-over-year
year_total = defaultdict(int)
year_cat = defaultdict(lambda: defaultdict(int))
for ym,cat,_ in pub_dates:
    y = ym[:4]
    year_total[y] += 1
    year_cat[y][cat] += 1
years_sorted = sorted(year_total.keys())
year_labels = years_sorted
year_values = [year_total[y] for y in years_sorted]

# Category mix by year (for donut charts)
year_donut_labels = []
year_donut_data = []
for y in years_sorted:
    year_donut_labels.append(y)
    year_donut_data.append([year_cat[y].get(c,0) for c in cat_order])

# Linear regression trend line on monthly totals
n_months = len(ym_set)
trend_slope = 0
trend_intercept = 0
if n_months > 1:
    x_vals = list(range(n_months))
    y_vals = tl_total
    x_mean = sum(x_vals) / n_months
    y_mean = sum(y_vals) / n_months
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_vals, y_vals))
    den = sum((x - x_mean) ** 2 for x in x_vals)
    if den != 0:
        trend_slope = num / den
        trend_intercept = y_mean - trend_slope * x_mean
trend_line = [trend_intercept + trend_slope * i for i in range(n_months)]

# Title word frequency (filter stopwords)
STOPWORDS = {'the','a','an','of','for','in','to','and','on','with','via','by','from','as','at','is','that','this','its','their','our','are','based','using','toward','towards','across','over','through','into','between','after','under','during','without','after','before','all','each','both','more','than','most','some','any','new','large','long','short','high','low','multi','self','co'}
word_counter = Counter()
for e in entries:
    title = e.get('title','')
    words = re.findall(r"[A-Za-z][A-Za-z-]+", title)
    for w in words:
        wl = w.lower()
        if len(wl) > 2 and wl not in STOPWORDS and not wl.startswith('260') and not wl.startswith('250'):
            word_counter[wl] += 1
top_words = word_counter.most_common(30)
word_labels = [w for w,_ in top_words]
word_values = [n for _,n in top_words]

# Top venues
top_venues = [(v,n) for v,n in venue_counter.most_common(12) if v != 'Unknown/None']
if venue_counter.get('Unknown/None',0) > 0:
    top_venues.append(('Unknown/None', venue_counter['Unknown/None']))

# Compute degree centrality for nodes
node_degree = Counter()

# ── 3. Force-directed graph data ──────────────────────────────────────
nodes = []
edges = []
edge_set = set()
venue_groups = defaultdict(list)
subyear_groups = defaultdict(list)
catyear_groups = defaultdict(list)

for i, e in enumerate(entries):
    d = e.get('date','')
    year = d[:4] if d and len(d)>=4 else '2026'
    nodes.append({
        'id': i,
        'title': e.get('title',''),
        'cat': e.get('category','unknown'),
        'sub': e.get('subcategory','unknown'),
        'year': year,
        'url': e.get('url',''),
        'venue': e.get('venue','')
    })
    v = e.get('venue','')
    if v: venue_groups[v].append(i)
    sub = e.get('subcategory','unknown')
    subyear_groups[(sub, year)].append(i)
    cat = e.get('category','unknown')
    catyear_groups[(cat, year)].append(i)

for v, ids in venue_groups.items():
    if len(ids) < 2: continue
    ids_sorted = sorted(ids)
    for idx in range(len(ids_sorted)):
        for jdx in range(idx+1, min(idx+8, len(ids_sorted))):
            key = (ids_sorted[idx], ids_sorted[jdx])
            if key not in edge_set:
                edge_set.add(key)
                edges.append({'source': ids_sorted[idx], 'target': ids_sorted[jdx], 'strength': 0.6})

for (sub, yr), ids in subyear_groups.items():
    if len(ids) < 2 or len(ids) > 30: continue
    ids_sorted = sorted(ids)
    for idx in range(len(ids_sorted)):
        for jdx in range(idx+1, min(idx+5, len(ids_sorted))):
            key = (ids_sorted[idx], ids_sorted[jdx])
            if key not in edge_set:
                edge_set.add(key)
                edges.append({'source': ids_sorted[idx], 'target': ids_sorted[jdx], 'strength': 0.3})

for (cat, yr), ids in catyear_groups.items():
    if len(ids) < 2 or len(ids) > 25: continue
    ids_sorted = sorted(ids)
    for idx in range(len(ids_sorted)):
        for jdx in range(idx+1, min(idx+4, len(ids_sorted))):
            key = (ids_sorted[idx], ids_sorted[jdx])
            if key not in edge_set:
                edge_set.add(key)
                edges.append({'source': ids_sorted[idx], 'target': ids_sorted[jdx], 'strength': 0.15})

# Compute degree centrality
for edge in edges:
    s = edge['source']
    t = edge['target']
    if isinstance(s, dict): s = s['id']
    if isinstance(t, dict): t = t['id']
    node_degree[s] += 1
    node_degree[t] += 1

max_degree = max(node_degree.values()) if node_degree else 1
for i, n in enumerate(nodes):
    n['degree'] = node_degree.get(i, 0)
    n['normDegree'] = round(node_degree.get(i, 0) / max_degree, 3)

# Graph-level metrics
num_nodes = len(nodes)
num_edges = len(edges)
max_possible = num_nodes * (num_nodes - 1) / 2
graph_density = round(num_edges / max_possible, 6) if max_possible > 0 else 0
# Average degree
avg_degree = round(sum(node_degree.values()) / num_nodes, 2) if num_nodes > 0 else 0

print(f'Force graph: {num_nodes} nodes, {num_edges} edges (density={graph_density}, avg_deg={avg_degree})')

# ── 4. Recent papers ──────────────────────────────────────────────────
sorted_entries = sorted(entries, key=lambda x: x.get('date',''), reverse=True)
recent = sorted_entries[:20]
recent_rows = ''
for e in recent:
    date = e.get('date','')
    title = e.get('title','')
    cat = e.get('category','')
    sub = e.get('subcategory','')
    url = e.get('url','')
    row = f'<tr><td>{date}</td><td><a href="{url}" target="_blank">{title}</a></td><td>{cat}</td><td>{sub}</td></tr>\n'
    recent_rows += row

def get_dates(cat):
    dates = sorted([e.get('date','') for e in entries if e.get('category')==cat and e.get('date')])
    return f'{dates[0]} – {dates[-1]}' if dates else 'N/A'

def js_str(s): return json.dumps(s)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Memory Research - Graph Analysis</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #0f1117; color: #e1e4e8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 24px; }
h1 { font-size: 1.8rem; margin-bottom: 8px; color: #f0f6fc; }
h2 { font-size: 1.2rem; margin: 24px 0 12px; color: #79c0ff; }
h3 { font-size: 1rem; margin: 16px 0 8px; color: #79c0ff; }
p { color: #8b949e; margin-bottom: 16px; }
.metrics-row { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
.metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 12px 16px; flex: 1; min-width: 140px; }
.metric-card .num { font-size: 1.4rem; font-weight: 700; color: #58a6ff; }
.metric-card .label { font-size: 0.78rem; color: #8b949e; margin-top: 2px; }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 24px; }
.stat-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }
.stat-card .num { font-size: 1.8rem; font-weight: 700; color: #58a6ff; }
.stat-card .label { font-size: 0.85rem; color: #8b949e; margin-top: 4px; }
.chart-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.chart-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.chart-row-4 { display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.chart-box { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; overflow: hidden; }
.chart-box.full { grid-column: 1 / -1; }
canvas { max-height: 400px; }
table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
th { text-align: left; padding: 8px 10px; border-bottom: 2px solid #30363d; color: #79c0ff; font-weight: 600; }
td { padding: 7px 10px; border-bottom: 1px solid #21262d; }
tr:hover td { background: #1c2128; }
a { color: #58a6ff; text-decoration: none; }
a:hover { text-decoration: underline; }
.heatmap-container { position: relative; width: 100%; max-width: 500px; margin: 0 auto; }
#forceGraph { width: 100%; height: 550px; background: #0d1117; border-radius: 6px; cursor: grab; }
#forceGraph:active { cursor: grabbing; }
.tooltip { position: absolute; background: #1c2128; border: 1px solid #30363d; border-radius: 6px; padding: 8px 12px; font-size: 0.8rem; pointer-events: none; color: #e1e4e8; max-width: 300px; z-index: 100; }
.legend { display: flex; gap: 16px; flex-wrap: wrap; margin: 8px 0; font-size: 0.8rem; }
.legend-item { display: flex; align-items: center; gap: 6px; }
.legend-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
.year-mix-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
@media (max-width: 768px) { .chart-row, .chart-row-3, .chart-row-4 { grid-template-columns: 1fr; } }
</style>
</head>
<body>

<h1>Agent Memory Research Papers</h1>
<p>Analysis of ''' + str(total) + ''' papers on memory for LLM agents</p>

<div class="stats-grid">
  <div class="stat-card"><div class="num">''' + str(total) + '''</div><div class="label">Total Papers</div></div>
  <div class="stat-card"><div class="num">''' + str(cat_counter.get('factual',0)) + '''</div><div class="label">Factual Memory</div></div>
  <div class="stat-card"><div class="num">''' + str(cat_counter.get('experiential',0)) + '''</div><div class="label">Experiential Memory</div></div>
  <div class="stat-card"><div class="num">''' + str(cat_counter.get('working',0)) + '''</div><div class="label">Working Memory</div></div>
</div>

<div class="stats-grid">
  <div class="stat-card"><div class="num">''' + str(subcat_counter.get('token-level',0)) + '''</div><div class="label">Token-level</div></div>
  <div class="stat-card"><div class="num">''' + str(subcat_counter.get('parametric',0)) + '''</div><div class="label">Parametric</div></div>
  <div class="stat-card"><div class="num">''' + str(subcat_counter.get('latent',0)) + '''</div><div class="label">Latent</div></div>
</div>

<h2>Graph Network Metrics</h2>
<div class="metrics-row">
  <div class="metric-card"><div class="num">''' + str(num_nodes) + '''</div><div class="label">Graph Nodes (Papers)</div></div>
  <div class="metric-card"><div class="num">''' + str(num_edges) + '''</div><div class="label">Graph Edges (Relationships)</div></div>
  <div class="metric-card"><div class="num">''' + str(graph_density) + '''</div><div class="label">Graph Density</div></div>
  <div class="metric-card"><div class="num">''' + str(avg_degree) + '''</div><div class="label">Average Degree</div></div>
  <div class="metric-card"><div class="num">''' + str(max_degree) + '''</div><div class="label">Max Degree (Hub)</div></div>
</div>

<h2>Paper Relationship Graph</h2>
<div class="chart-box full">
<div class="legend">
  <span class="legend-item"><span class="legend-dot" style="background:#58a6ff"></span> Factual</span>
  <span class="legend-item"><span class="legend-dot" style="background:#3fb950"></span> Experiential</span>
  <span class="legend-item"><span class="legend-dot" style="background:#d29922"></span> Working</span>
  <span style="color:#8b949e; margin-left: 12px;">Node size = degree centrality (more connections = larger) | Click node for paper</span>
</div>
<svg id="forceGraph"></svg>
<div id="tooltip" class="tooltip" style="display:none"></div>
</div>

<h2>Category × Subcategory Heatmap</h2>
<div class="chart-box full" style="max-width: 520px;">
<canvas id="heatmapChart"></canvas>
</div>

<div class="chart-row">
  <div class="chart-box"><canvas id="catChart"></canvas></div>
  <div class="chart-box"><canvas id="subcatChart"></canvas></div>
</div>

<h2>Publication Timeline (Monthly)</h2>
<div class="chart-box full">
<canvas id="timelineChart"></canvas>
</div>

<h2>Publication Velocity (Monthly Papers + Trend)</h2>
<div class="chart-box full">
<canvas id="velocityChart"></canvas>
</div>

<h2>Subcategory Trends Over Time</h2>
<div class="chart-box full">
<canvas id="subcatTrendChart"></canvas>
</div>

<div class="chart-row">
  <div class="chart-box"><canvas id="cumulativeChart"></canvas></div>
  <div class="chart-box"><canvas id="yearGrowthChart"></canvas></div>
</div>

<h2>Category Mix Over Time</h2>
<div class="chart-box full">
<div class="year-mix-grid" id="yearMixGrid"></div>
</div>

<div class="chart-row">
  <div class="chart-box"><canvas id="venueChart"></canvas></div>
  <div class="chart-box"><canvas id="radarChart"></canvas></div>
</div>

<h2>Most Common Title Keywords</h2>
<div class="chart-box full">
<canvas id="wordChart"></canvas>
</div>

<h2>Date Ranges by Category</h2>
<div class="stats-grid">
  <div class="stat-card"><div class="num">''' + get_dates('factual') + '''</div><div class="label">Factual (''' + str(cat_counter.get('factual',0)) + ''' papers)</div></div>
  <div class="stat-card"><div class="num">''' + get_dates('experiential') + '''</div><div class="label">Experiential (''' + str(cat_counter.get('experiential',0)) + ''' papers)</div></div>
  <div class="stat-card"><div class="num">''' + get_dates('working') + '''</div><div class="label">Working (''' + str(cat_counter.get('working',0)) + ''' papers)</div></div>
</div>

<h2>20 Most Recent Papers</h2>
<table>
<thead><tr><th>Date</th><th>Title</th><th>Category</th><th>Subcategory</th></tr></thead>
<tbody>''' + recent_rows + '''</tbody>
</table>

<script>
// ── Data ──────────────────────────────────────────────────────────
const catLabels = ''' + js_str(cat_order) + ''';
const catValues = ''' + js_str(cat_vals) + ''';
const catColors = ''' + js_str([cat_colors[c] for c in cat_order]) + ''';
const catColorsObj = ''' + js_str(cat_colors) + ''';

const subcatLabels = ''' + js_str(subcat_order) + ''';
const subcatValues = ''' + js_str(subcat_vals) + ''';
const subcatColors = ''' + js_str([subcat_colors[s] for s in subcat_order]) + ''';

const tlLabels = ''' + js_str(ym_set) + ''';
const tlFactual = ''' + js_str(tl_factual) + ''';
const tlExperiential = ''' + js_str(tl_exp) + ''';
const tlWorking = ''' + js_str(tl_work) + ''';
const tlTotal = ''' + js_str(tl_total) + ''';

const tlSubToken = ''' + js_str(tl_sub_token) + ''';
const tlSubParam = ''' + js_str(tl_sub_param) + ''';
const tlSubLatent = ''' + js_str(tl_sub_latent) + ''';

const rollFactual = ''' + js_str(roll_factual) + ''';
const rollExperiential = ''' + js_str(roll_exp) + ''';
const rollWorking = ''' + js_str(roll_work) + ''';
const rollTotal = ''' + js_str(roll_total) + ''';

const cumFactual = ''' + js_str(cum_f) + ''';
const cumExperiential = ''' + js_str(cum_e) + ''';
const cumWorking = ''' + js_str(cum_w) + ''';
const cumTotal = ''' + js_str(cum_total) + ''';

const yearLabels = ''' + js_str(year_labels) + ''';
const yearValues = ''' + js_str(year_values) + ''';

const heatData = ''' + js_str(heat) + ''';

const venueLabels = ''' + js_str([v for v,n in top_venues]) + ''';
const venueValues = ''' + js_str([n for _,n in top_venues]) + ''';
const venueColors = ['#58a6ff','#3fb950','#d29922','#f0883e','#db6d8a','#7ee787','#a5d6ff','#79c0ff','#8b949e','#6e7681','#484f58','#30363d'];

const graphNodes = ''' + js_str(nodes) + ''';
const graphEdges = ''' + js_str(edges) + ''';

const yearDonutLabels = ''' + js_str(year_donut_labels) + ''';
const yearDonutData = ''' + js_str(year_donut_data) + ''';

const trendLine = ''' + js_str(trend_line) + ''';

const wordLabels = ''' + js_str(word_labels) + ''';
const wordValues = ''' + js_str(word_values) + ''';

// ── Force-directed graph ──────────────────────────────────────────
const catColorMap = { 'factual': '#58a6ff', 'experiential': '#3fb950', 'working': '#d29922' };
const width = document.getElementById('forceGraph').clientWidth;
const height = 550;

const svg = d3.select('#forceGraph')
  .attr('viewBox', [0, 0, width, height]);

const g = svg.append('g');
svg.call(d3.zoom().scaleExtent([0.3, 4]).on('zoom', (event) => {
  g.attr('transform', event.transform);
}));

const tooltip = d3.select('#tooltip');

// Node radius: base 3 + degree centrality * 12
const degreeMax = d3.max(graphNodes, d => d.normDegree) || 1;
const sim = d3.forceSimulation(graphNodes)
  .force('link', d3.forceLink(graphEdges).id(d => d.id).distance(60).strength(d => d.strength || 0.3))
  .force('charge', d3.forceManyBody().strength(-25))
  .force('center', d3.forceCenter(width/2, height/2))
  .force('collision', d3.forceCollide().radius(d => 3 + d.normDegree * 10));

const link = g.append('g')
  .selectAll('line')
  .data(graphEdges)
  .join('line')
  .attr('stroke', '#30363d')
  .attr('stroke-width', d => 0.3 + (d.strength || 0.3) * 0.8)
  .attr('stroke-opacity', d => 0.15 + (d.strength || 0.3) * 0.5);

const node = g.append('g')
  .selectAll('circle')
  .data(graphNodes)
  .join('circle')
  .attr('r', d => 3 + d.normDegree * 10)
  .attr('fill', d => catColorMap[d.cat] || '#8b949e')
  .attr('stroke', '#0d1117')
  .attr('stroke-width', 1)
  .attr('opacity', 0.8)
  .call(d3.drag()
    .on('start', (event, d) => { if (!event.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
    .on('drag', (event, d) => { d.fx = event.x; d.fy = event.y; })
    .on('end', (event, d) => { if (!event.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }))
  .on('mouseover', (event, d) => {
    tooltip.style('display', 'block')
      .html('<strong>' + d.title + '</strong><br>Category: ' + d.cat + ' | Sub: ' + d.sub + ' | Year: ' + d.year + '<br>Degree: ' + d.degree + ' connections')
      .style('left', (event.pageX + 12) + 'px')
      .style('top', (event.pageY - 10) + 'px');
  })
  .on('mouseout', () => tooltip.style('display', 'none'))
  .on('click', (event, d) => { if (d.url) window.open(d.url, '_blank'); });

sim.on('tick', () => {
  link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
  node.attr('cx', d => d.x).attr('cy', d => d.y);
});

// ── Category Mix Donut Charts ──────────────────────────────────────
const yearMixGrid = document.getElementById('yearMixGrid');
yearDonutLabels.forEach((year, yi) => {
  const box = document.createElement('div');
  box.style.cssText = 'background:#161b22; border:1px solid #30363d; border-radius:8px; padding:8px; text-align:center;';
  const canvas = document.createElement('canvas');
  canvas.id = 'donut-' + year;
  canvas.style.cssText = 'max-height:160px;';
  box.appendChild(canvas);
  const label = document.createElement('div');
  label.style.cssText = 'color:#8b949e; font-size:0.8rem; margin-top:4px;';
  label.textContent = year + ' (' + yearDonutData[yi].reduce((a,b) => a+b, 0) + ')';
  box.appendChild(label);
  yearMixGrid.appendChild(box);
  
  new Chart(document.getElementById('donut-' + year), {
    type: 'doughnut',
    data: {
      labels: catLabels,
      datasets: [{ data: yearDonutData[yi], backgroundColor: catColors, borderWidth: 1, borderColor: '#0f1117' }]
    },
    options: {
      responsive: true, cutout: '55%',
      plugins: { legend: { display: false }, tooltip: { callbacks: { label: ctx => ctx.label + ': ' + ctx.raw } } }
    }
  });
});

// ── Charts ────────────────────────────────────────────────────────
new Chart(document.getElementById('catChart'), {
  type: 'bar',
  data: { labels: catLabels, datasets: [{ label: 'Papers', data: catValues, backgroundColor: catColors, borderRadius: 4 }] },
  options: { responsive: true, plugins: { legend: { display: false } }, scales: { x: { ticks: { color: '#8b949e' }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } } } }
});

new Chart(document.getElementById('subcatChart'), {
  type: 'bar',
  data: { labels: subcatLabels, datasets: [{ label: 'Papers', data: subcatValues, backgroundColor: subcatColors, borderRadius: 4 }] },
  options: { responsive: true, plugins: { legend: { display: false } }, scales: { x: { ticks: { color: '#8b949e' }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } } } }
});

new Chart(document.getElementById('timelineChart'), {
  type: 'line',
  data: {
    labels: tlLabels,
    datasets: [
      { label: 'Factual', data: tlFactual, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.1)', fill: true, tension: 0.3, pointRadius: 2 },
      { label: 'Experiential', data: tlExperiential, borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.1)', fill: true, tension: 0.3, pointRadius: 2 },
      { label: 'Working', data: tlWorking, borderColor: '#d29922', backgroundColor: 'rgba(210,153,34,0.1)', fill: true, tension: 0.3, pointRadius: 2 },
      { label: 'Factual (3mo avg)', data: rollFactual, borderColor: '#58a6ff', borderDash: [4,3], borderWidth: 1.5, pointRadius: 0, fill: false },
      { label: 'Experiential (3mo avg)', data: rollExperiential, borderColor: '#3fb950', borderDash: [4,3], borderWidth: 1.5, pointRadius: 0, fill: false },
      { label: 'Working (3mo avg)', data: rollWorking, borderColor: '#d29922', borderDash: [4,3], borderWidth: 1.5, pointRadius: 0, fill: false }
    ]
  },
  options: {
    responsive: true, interaction: { mode: 'index', intersect: false },
    plugins: { legend: { labels: { color: '#8b949e' } } },
    scales: { x: { ticks: { color: '#8b949e', maxTicksLimit: 25 }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('velocityChart'), {
  type: 'line',
  data: {
    labels: tlLabels,
    datasets: [
      { label: 'Papers per month', data: tlTotal, borderColor: '#7ee787', backgroundColor: 'rgba(126,231,135,0.12)', fill: true, tension: 0.3, pointRadius: 2, pointBackgroundColor: '#7ee787' },
      { label: '3-month avg', data: rollTotal, borderColor: '#f0883e', borderDash: [4,3], borderWidth: 2, pointRadius: 0, fill: false },
      { label: 'Linear trend', data: trendLine, borderColor: '#db6d8a', borderWidth: 1.5, pointRadius: 0, fill: false, borderDash: [6,3] }
    ]
  },
  options: {
    responsive: true, interaction: { mode: 'index', intersect: false },
    plugins: { legend: { labels: { color: '#8b949e' } } },
    scales: { x: { ticks: { color: '#8b949e', maxTicksLimit: 25 }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('subcatTrendChart'), {
  type: 'line',
  data: {
    labels: tlLabels,
    datasets: [
      { label: 'Token-level', data: tlSubToken, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.06)', fill: true, tension: 0.3, pointRadius: 1.5 },
      { label: 'Parametric', data: tlSubParam, borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.06)', fill: true, tension: 0.3, pointRadius: 1.5 },
      { label: 'Latent', data: tlSubLatent, borderColor: '#d29922', backgroundColor: 'rgba(210,153,34,0.06)', fill: true, tension: 0.3, pointRadius: 1.5 }
    ]
  },
  options: {
    responsive: true, interaction: { mode: 'index', intersect: false },
    plugins: { legend: { labels: { color: '#8b949e' } } },
    scales: { x: { ticks: { color: '#8b949e', maxTicksLimit: 25 }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('cumulativeChart'), {
  type: 'line',
  data: {
    labels: tlLabels,
    datasets: [
      { label: 'Total', data: cumTotal, borderColor: '#7ee787', backgroundColor: 'rgba(126,231,135,0.05)', fill: true, tension: 0.3, pointRadius: 1, borderWidth: 2 },
      { label: 'Factual', data: cumFactual, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.05)', fill: true, tension: 0.3, pointRadius: 1 },
      { label: 'Experiential', data: cumExperiential, borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.05)', fill: true, tension: 0.3, pointRadius: 1 },
      { label: 'Working', data: cumWorking, borderColor: '#d29922', backgroundColor: 'rgba(210,153,34,0.05)', fill: true, tension: 0.3, pointRadius: 1 }
    ]
  },
  options: {
    responsive: true, interaction: { mode: 'index', intersect: false },
    plugins: { legend: { labels: { color: '#8b949e' } } },
    scales: { x: { ticks: { color: '#8b949e', maxTicksLimit: 25 }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 20, color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('yearGrowthChart'), {
  type: 'bar',
  data: { labels: yearLabels, datasets: [{ label: 'Papers', data: yearValues, backgroundColor: '#58a6ff', borderRadius: 4 }] },
  options: {
    responsive: true, plugins: { legend: { display: false } },
    scales: { x: { ticks: { color: '#8b949e' }, grid: { color: '#21262d' } }, y: { beginAtZero: true, ticks: { stepSize: 20, color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('venueChart'), {
  type: 'bar',
  data: { labels: venueLabels, datasets: [{ label: 'Papers', data: venueValues, backgroundColor: venueColors.slice(0, venueLabels.length), borderRadius: 4 }] },
  options: {
    indexAxis: 'y', responsive: true, plugins: { legend: { display: false } },
    scales: { x: { beginAtZero: true, ticks: { stepSize: 1, color: '#8b949e' }, grid: { color: '#21262d' } }, y: { ticks: { color: '#8b949e' }, grid: { color: '#21262d' } } }
  }
});

new Chart(document.getElementById('radarChart'), {
  type: 'radar',
  data: {
    labels: catLabels,
    datasets: [{
      label: 'Token-level', data: [''' + str(cat_subcat['factual']['token-level']) + ''',''' + str(cat_subcat['experiential']['token-level']) + ''',''' + str(cat_subcat['working']['token-level']) + '''], backgroundColor: 'rgba(88,166,255,0.2)', borderColor: '#58a6ff', pointBackgroundColor: '#58a6ff'
    }, {
      label: 'Parametric', data: [''' + str(cat_subcat['factual']['parametric']) + ''',''' + str(cat_subcat['experiential']['parametric']) + ''',''' + str(cat_subcat['working']['parametric']) + '''], backgroundColor: 'rgba(63,185,80,0.2)', borderColor: '#3fb950', pointBackgroundColor: '#3fb950'
    }, {
      label: 'Latent', data: [''' + str(cat_subcat['factual']['latent']) + ''',''' + str(cat_subcat['experiential']['latent']) + ''',''' + str(cat_subcat['working']['latent']) + '''], backgroundColor: 'rgba(210,153,34,0.2)', borderColor: '#d29922', pointBackgroundColor: '#d29922'
    }]
  },
  options: {
    responsive: true,
    plugins: { legend: { labels: { color: '#8b949e' } } },
    scales: { r: { beginAtZero: true, ticks: { stepSize: 20, color: '#8b949e', backdropColor: 'transparent' }, grid: { color: '#30363d' }, angleLines: { color: '#30363d' }, pointLabels: { color: '#8b949e' } } }
  }
});

new Chart(document.getElementById('wordChart'), {
  type: 'bar',
  data: { labels: wordLabels, datasets: [{ label: 'Occurrences', data: wordValues, backgroundColor: '#58a6ff', borderRadius: 3 }] },
  options: {
    indexAxis: 'y', responsive: true, plugins: { legend: { display: false } },
    scales: { x: { beginAtZero: true, ticks: { stepSize: 2, color: '#8b949e' }, grid: { color: '#21262d' } }, y: { ticks: { color: '#8b949e', font: { size: 11 } }, grid: { color: '#21262d' } } }
  }
});

// ── Heatmap ───────────────────────────────────────────────────────
const heatCtx = document.getElementById('heatmapChart').getContext('2d');
const cellW = 90, cellH = 50, pad = 2;
const catNames = ['Factual', 'Experiential', 'Working'];
const subNames = ['Token-level', 'Parametric', 'Latent'];
const w = cellW * 3 + 120, h = cellH * 3 + 60;
heatCtx.canvas.width = w;
heatCtx.canvas.height = h;

function drawHeatmap() {
  heatCtx.clearRect(0, 0, w, h);
  const maxVal = Math.max(...heatData.flat());
  heatCtx.fillStyle = '#8b949e';
  heatCtx.font = '13px sans-serif';
  heatCtx.textAlign = 'center';
  heatCtx.textBaseline = 'middle';
  for (let j = 0; j < 3; j++) heatCtx.fillText(subNames[j], 120 + j * cellW + cellW/2, 20);
  heatCtx.textAlign = 'right';
  for (let i = 0; i < 3; i++) heatCtx.fillText(catNames[i], 110, 60 + i * cellH + cellH/2);
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const v = heatData[i][j];
      const frac = maxVal > 0 ? v / maxVal : 0;
      const r = Math.round(15 + frac * 50);
      const g = Math.round(70 + frac * 120);
      const b = Math.round(140 + frac * 115);
      heatCtx.fillStyle = 'rgb('+r+','+g+','+b+')';
      heatCtx.fillRect(120 + j * cellW + pad, 55 + i * cellH + pad, cellW - pad*2, cellH - pad*2);
      heatCtx.fillStyle = '#e1e4e8';
      heatCtx.font = 'bold 16px sans-serif';
      heatCtx.textAlign = 'center';
      heatCtx.textBaseline = 'middle';
      heatCtx.fillText(v, 120 + j * cellW + cellW/2, 55 + i * cellH + cellH/2);
    }
  }
}
drawHeatmap();
</script>
</body>
</html>'''

with open(os.path.join(BASE, 'docs', 'graph_analysis.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f'Wrote docs/graph_analysis.html ({len(HTML)} bytes)')
