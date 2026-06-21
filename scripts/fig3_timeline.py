#!/usr/bin/env python3
"""Figure 3: Timeline of agent memory papers (2013–2026)."""

from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import yaml

base = Path(__file__).parent.parent
with open(base / "papers.yaml") as f:
    data = yaml.safe_load(f)
papers = data["papers"]

cats = ["factual", "experiential", "working"]
cat_labels = ["Factual", "Experiential", "Working"]
colors = ["#4C72B0", "#DD8452", "#55A868"]

yearly = {c: Counter() for c in cats}
for p in papers:
    year = int(p["date"][:4])
    yearly[p["category"]][year] += 1

years = list(range(2013, 2027))
width = 0.25
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(7, 3.5))

bottoms = np.zeros(len(years))
for idx, cat in enumerate(cats):
    vals = [yearly[cat].get(y, 0) for y in years]
    ax.bar(x + idx * width, vals, width, label=cat_labels[idx], color=colors[idx])

# Vertical line at Jan 2026 cutoff
cutoff_x = years.index(2026) + 0.5
ax.axvline(x=cutoff_x, color="red", linestyle="--", linewidth=1, alpha=0.7)
ax.text(cutoff_x + 0.1, ax.get_ylim()[1] * 0.9, "Original Survey\nCutoff (Jan 2026)",
        fontsize=7, color="red", va="top")

ax.set_xlabel("Year", fontsize=10)
ax.set_ylabel("Number of Papers", fontsize=10)
ax.set_title("Agent Memory Papers Timeline (2013–2026)", fontsize=11, fontweight="bold")
ax.set_xticks(x + width)
ax.set_xticklabels(years, fontsize=8, rotation=45)
ax.legend(fontsize=8, loc="upper left")
ax.set_xlim(-0.5, len(years) - 0.5)

plt.tight_layout()
out = base / "paper/figures/fig3_timeline.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, bbox_inches="tight")
print(f"Saved {out}")
