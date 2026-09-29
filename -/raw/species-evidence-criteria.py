"""Contrast hypothetical species evidence; this figure contains no measured data.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching PNG is written to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ink = "#183245"
    ax.text(5, 5.65, "Three questions about a species boundary", ha="center",
            fontsize=18, weight="bold", color=ink)
    ax.text(5, 5.26, "Hypothetical evidence combinations · no named species or measurements",
            ha="center", fontsize=11.5, color=ink)
    xs = [.22, 1.16, 3.44, 5.72, 8]
    ws = [.94, 2.28, 2.28, 2.28, 1.78]
    heads = ["Pair", "Morphology\nDifferent form?", "Mating\nReduced crossing?",
             "Ancestry\nDistinct lineage?", "Interpretation"]
    for x, w, label in zip(xs, ws, heads):
        ax.add_patch(Rectangle((x, 4.1), w, .8, facecolor="#e8f0f5",
                               edgecolor="white", lw=2))
        ax.text(x+w/2, 4.5, label, ha="center", va="center", fontsize=11.5,
                weight="bold", color=ink, linespacing=1.5)
    rows = [
        ["A", "Different", "Not tested", "Not tested", "Missing\nevidence"],
        ["B", "Similar", "Reduced", "Distinct", "Form alone\ncan miss a split"],
        ["C", "Different", "Compatible", "Not separated", "Check variation\nwithin a species"],
    ]
    for k, row in enumerate(rows):
        y = 3.15 - .95*k
        for j, (x, w, label) in enumerate(zip(xs, ws, row)):
            fill = "#f5f8fa" if k % 2 == 0 else "white"
            ax.add_patch(Rectangle((x, y), w, .95, facecolor=fill,
                                   edgecolor="#d6e1e8", lw=.8))
            ax.text(x+w/2, y+.475, label, ha="center", va="center",
                    fontsize=11 if j == 4 else 12, color=ink,
                    weight="bold" if j == 0 else "normal", linespacing=1.5)
    ax.text(5, .87, "Different criteria can disagree; an unperformed test is not a negative result.",
            ha="center", fontsize=12, color=ink)
    ax.text(5, .4, "State the criterion, sampling and assay conditions before interpreting a boundary.",
            ha="center", fontsize=11.5, color=ink)
    fig.subplots_adjust(left=.025, right=.975, top=.99, bottom=.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
