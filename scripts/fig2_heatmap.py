#!/usr/bin/env python3
"""Figure 2: Paper distribution heatmap across 3x3 taxonomy cells."""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import yaml

base = Path(__file__).parent.parent
with open(base / "papers.yaml") as f:
    data = yaml.safe_load(f)
papers = data["papers"]

cats = ["factual", "experiential", "working"]
subs = ["token-level", "parametric", "latent"]
cat_labels = ["Factual", "Experiential", "Working"]
sub_labels = ["Token-level", "Parametric", "Latent"]

grid = np.zeros((3, 3), dtype=int)
for p in papers:
    i = cats.index(p["category"])
    j = subs.index(p["subcategory"])
    grid[i, j] += 1

fig, ax = plt.subplots(figsize=(5, 3.5))
im = ax.imshow(grid, cmap="Blues", aspect="auto", vmin=0, vmax=max(grid.flatten()))

ax.set_xticks(range(3))
ax.set_yticks(range(3))
ax.set_xticklabels(sub_labels, fontsize=10)
ax.set_yticklabels(cat_labels, fontsize=10)

for i in range(3):
    for j in range(3):
        ax.text(j, i, str(grid[i, j]), ha="center", va="center",
                fontsize=16, fontweight="bold",
                color="white" if grid[i, j] > grid.max() / 2 else "black")

cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("Number of Papers", fontsize=9)
ax.set_title("Paper Distribution Across Taxonomy Cells", fontsize=11, fontweight="bold")

plt.tight_layout()
out = base / "paper/figures/fig2_heatmap.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, bbox_inches="tight")
print(f"Saved {out}")
