"""Draw the classical extract-transfer experiment, with qualitative controls.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7; uses the root pyproject environment.
Output: second-messenger-transfer.png in the current directory.
Source: Rall, Sutherland and Berthet (1957), JBC 224, Figure 4, pp. 470-471,
https://doi.org/10.1016/S0021-9258(18)65045-8.
An original schematic, not digitized data or a reproduction of the paper's figure.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT = Path("second-messenger-transfer.png")
INK = "#24364a"
BLUE = "#1d6696"
GREEN = "#237b63"


def box(ax, x, y, width, height, text, color):
    ax.add_patch(FancyBboxPatch(
        (x, y), width, height, boxstyle="round,pad=0.10",
        facecolor="white", edgecolor=color, linewidth=1.5,
    ))
    ax.text(x + width / 2, y + height / 2, text,
            ha="center", va="center", color=INK, fontsize=10.5, linespacing=1.5)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.04, top=0.94)
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.text(5, 5.8, "A hormone response in two separable stages",
            ha="center", weight="bold", color=INK, fontsize=16)
    ax.text(5, 5.38, "Rall, Sutherland & Berthet (1957): original schematic, not measured data",
            ha="center", color=INK, fontsize=10)
    box(ax, 0.15, 3.65, 2.8, 1.22,
        "Washed cat-liver particles\n+ epinephrine and glucagon\n+ ATP and magnesium ions\n5 min at 30°C", BLUE)
    box(ax, 3.65, 3.65, 2.35, 1.22,
        "Boil for 3 min\nChill and remove\ninsoluble material", BLUE)
    box(ax, 6.7, 3.65, 3.05, 1.22,
        "Extract + soluble dog-liver\npreparation + ATP + Mg²⁺\nMeasure phosphorylase activity\nbefore / after 5 min at 30°C", GREEN)
    for left, right in ((3.05, 3.52), (6.12, 6.57)):
        ax.add_patch(FancyArrowPatch((left, 4.25), (right, 4.25),
                     arrowstyle="-|>", mutation_scale=17, color=INK, linewidth=1.5))
    ax.text(5, 3.22, "Compare additions to the same soluble assay preparation",
            ha="center", weight="bold", color=INK, fontsize=12)
    rows = [
        ("Water", "Baseline comparator"),
        ("Extract made without hormones", "Smaller effect"),
        ("Hormones added directly", "Smaller effect"),
        ("Extract made with hormones", "Larger increase in enzyme activity"),
    ]
    ax.text(0.28, 2.79, "Addition", weight="bold", color=INK)
    ax.text(5.25, 2.79, "Qualitative observation", weight="bold", color=INK)
    for index, (addition, observation) in enumerate(rows):
        y = 2.35 - 0.46 * index
        if index == 3:
            ax.add_patch(FancyBboxPatch((0.14, y - 0.19), 9.57, 0.37,
                         boxstyle="round,pad=0.02", linewidth=0,
                         facecolor="#eaf5ef"))
        ax.text(0.28, y, addition, color=INK, va="center", fontsize=11)
        ax.text(5.25, y, observation, color=GREEN if index == 3 else INK,
                va="center", fontsize=11)
    ax.text(5, 0.42, "Inference: a transferable, heat-stable intermediary; its identity needs further evidence.",
            ha="center", color=INK, fontsize=10.5)
    fig.savefig(OUTPUT, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
