#!/usr/bin/env python3
"""Figure 4: Data-driven curation pipeline diagram."""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

base = Path(__file__).parent.parent

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.axis("off")

# Boxes: (x, y, width, height, label, sublabel, color)
boxes = [
    (0.02, 0.55, 0.14, 0.30, "papers.yaml", "Source of Truth", "#E8F5E9"),
    (
        0.22,
        0.55,
        0.14,
        0.30,
        "validate_papers.py",
        "Validation &\nNormalization",
        "#E3F2FD",
    ),
    (
        0.42,
        0.55,
        0.14,
        0.30,
        "generate_readme.py",
        "README + JSON\nGeneration",
        "#FFF3E0",
    ),
    (0.62, 0.55, 0.14, 0.30, "docs/", "Interactive\nWeb Interface", "#F3E5F5"),
    # Bottom row: external inputs
    (0.02, 0.10, 0.14, 0.25, "arXiv API", "Paper Discovery", "#FBE9E7"),
    (0.22, 0.10, 0.14, 0.25, "fetch_metadata.py", "Metadata\nEnrichment", "#FBE9E7"),
    (
        0.42,
        0.10,
        0.14,
        0.25,
        "fetch_new_papers.py",
        "arXiv New\nPaper Crawler",
        "#FBE9E7",
    ),
    (0.62, 0.10, 0.14, 0.25, "GitHub Actions", "CI/CD Validation", "#E8F5E9"),
]

font_kw = dict(fontsize=8, ha="center", va="center")
sub_kw = dict(fontsize=6, ha="center", va="center", color="dimgray")

for x, y, w, h, label, sublabel, color in boxes:
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.05", facecolor=color, edgecolor="gray", lw=1
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h * 0.55, label, fontweight="bold", **font_kw)
    ax.text(x + w / 2, y + h * 0.25, sublabel, **sub_kw)

# Arrows (main flow — top row)
arrows = [
    (0.16, 0.70, 0.22, 0.70),
    (0.36, 0.70, 0.42, 0.70),
    (0.56, 0.70, 0.62, 0.70),
]
for x1, y1, x2, y2 in arrows:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color="gray", lw=1.5),
    )

# Arrows (bottom → top)
bottom_arrows = [
    (0.09, 0.35, 0.09, 0.55),
    (0.29, 0.35, 0.29, 0.55),
    (0.49, 0.35, 0.49, 0.55),
]
for x1, y1, x2, y2 in bottom_arrows:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color="coral", lw=1.2),
    )

# Feedback arrow (docs → papers.yaml suggests updates)
ax.annotate(
    "",
    xy=(0.09, 0.55),
    xytext=(0.69, 0.40),
    arrowprops=dict(
        arrowstyle="->",
        color="green",
        lw=1,
        linestyle="dashed",
        connectionstyle="arc3,rad=-0.3",
    ),
)

ax.set_xlim(0, 0.8)
ax.set_ylim(0, 0.95)
ax.set_title("Figure 4: Data-Driven Curation Pipeline", fontsize=10, fontweight="bold")

plt.tight_layout()
out_pdf = base / "paper/figures/fig4_pipeline.pdf"
out_png = base / "paper/figures/fig4_pipeline.png"
out_png_web = (
    base.parent
    / "next-tobias-weiss-org/public/images/research/agent-memory-fig4-pipeline.png"
)
out_pdf.parent.mkdir(parents=True, exist_ok=True)
out_png_web.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out_pdf, bbox_inches="tight")
plt.savefig(out_png, bbox_inches="tight", dpi=150)
plt.savefig(out_png_web, bbox_inches="tight", dpi=150)
print(f"Saved {out_pdf}")
