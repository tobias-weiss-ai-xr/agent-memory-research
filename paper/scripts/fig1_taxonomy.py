#!/usr/bin/env python3
"""Figure 1: Extended taxonomy diagram — 3x3 original + 3 new dimensions."""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import yaml

base = Path(__file__).parent.parent
with open(base / "papers.yaml") as f:
    data = yaml.safe_load(f)
papers = data["papers"]

cats = ["factual", "experiential", "working"]
subs = ["token-level", "parametric", "latent"]
cat_labels = ["Factual", "Experiential", "Working"]
sub_labels = ["Token-level", "Parametric", "Latent"]

counts = {}
for p in papers:
    key = (p["category"], p["subcategory"])
    counts[key] = counts.get(key, 0) + 1

fig, axes = plt.subplots(
    1, 2, figsize=(10, 3.5), gridspec_kw={"width_ratios": [1.3, 1]}
)

# Left: 3x3 table
ax = axes[0]
ax.axis("off")
col_widths = [0.28, 0.24, 0.24, 0.24]
row_height = 0.22
start_x, start_y = 0.05, 0.92

# Header — subcategories
ax.text(start_x + col_widths[0] / 2, start_y, "", fontsize=9, ha="center", va="bottom")
for j, sl in enumerate(sub_labels):
    ax.text(
        start_x + sum(col_widths[: j + 1]) + col_widths[j + 1] / 2,
        start_y,
        sl,
        fontsize=8,
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Rows
for i, (cat, cl) in enumerate(zip(cats, cat_labels)):
    y = start_y - (i + 1) * row_height
    ax.text(
        start_x + col_widths[0] / 2,
        y + row_height / 2,
        cl,
        fontsize=9,
        ha="center",
        va="center",
        fontweight="bold",
    )
    for j, sub in enumerate(subs):
        cx = start_x + sum(col_widths[: j + 1]) + col_widths[j + 1] / 2
        cnt = counts.get((cat, sub), 0)
        ax.text(
            cx,
            y + row_height / 2,
            str(cnt),
            fontsize=11,
            ha="center",
            va="center",
            color="darkblue",
            fontweight="bold",
        )

# Total row
y_tot = start_y - 4 * row_height
ax.text(
    start_x + col_widths[0] / 2,
    y_tot + row_height / 2,
    "Total",
    fontsize=9,
    ha="center",
    va="center",
    fontweight="bold",
)
for j, sub in enumerate(subs):
    cx = start_x + sum(col_widths[: j + 1]) + col_widths[j + 1] / 2
    total = sum(counts.get((c, sub), 0) for c in cats)
    ax.text(
        cx,
        y_tot + row_height / 2,
        str(total),
        fontsize=11,
        ha="center",
        va="center",
        color="darkred",
        fontweight="bold",
    )

ax.set_xlim(0, 1.1)
ax.set_ylim(0, 1)
ax.set_title(
    "Original 3x3 Taxonomy (Paper Counts)", fontsize=10, fontweight="bold", pad=5
)

# Right: 3 new dimensions
ax2 = axes[1]
ax2.axis("off")

dims = [
    ("Temporal Dynamics", ["None", "Decay", "Consolidation", "Bi-temporal"]),
    ("Modality", ["Text", "M.-in", "M.-out", "Full"]),
    ("Biological Inspiration", ["None", "Cognitive", "Neuro", "Brain"]),
]

y_start = 0.88
for idx, (dim_name, levels) in enumerate(dims):
    y = y_start - idx * 0.30
    ax2.text(0.02, y, dim_name, fontsize=8.5, fontweight="bold", va="center")
    for j, lv in enumerate(levels):
        x = 0.28 + j * 0.17
        ax2.add_patch(
            mpatches.FancyBboxPatch(
                (x - 0.06, y - 0.08),
                0.14,
                0.16,
                boxstyle="round,pad=0.02",
                facecolor="lightsteelblue",
                edgecolor="steelblue",
                lw=0.8,
            )
        )
        ax2.text(x, y, lv, fontsize=6.5, ha="center", va="center")
    # Arrow between levels
    for j in range(len(levels) - 1):
        x1 = 0.28 + j * 0.17 + 0.07
        x2 = 0.28 + (j + 1) * 0.17 - 0.07
        ax2.annotate(
            "",
            xy=(x2, y),
            xytext=(x1, y),
            arrowprops=dict(arrowstyle="->", color="gray", lw=0.8),
        )

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_title("New Orthogonal Dimensions", fontsize=10, fontweight="bold", pad=5)

plt.tight_layout()
out_pdf = base / "paper/figures/fig1_taxonomy.pdf"
out_png = base / "paper/figures/fig1_taxonomy.png"
out_png_web = (
    base.parent
    / "next-tobias-weiss-org/public/images/research/agent-memory-fig1-taxonomy.png"
)
out_pdf.parent.mkdir(parents=True, exist_ok=True)
out_png_web.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out_pdf, bbox_inches="tight")
plt.savefig(out_png, bbox_inches="tight", dpi=150)
plt.savefig(out_png_web, bbox_inches="tight", dpi=150)
print(f"Saved {out_pdf}")
