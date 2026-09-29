"""Draw ordered coin outcomes and event operations (Python 3.14, matplotlib 3.10)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(8.8, 5.2), dpi=120, facecolor="white")
    ax.set(xlim=(-0.95, 4.6), ylim=(-0.7, 3.2))
    ax.axis("off")
    blue, pale, ink = "#16617d", "#e1f1f5", "#243442"
    ax.text(1.5, 2.93, "Two fair independent tosses", ha="center",
            fontsize=19, weight="bold", color=ink)
    ax.text(1, 2.52, "Second toss", ha="center", fontsize=12, color=ink)
    for x, label in [(0.5, "H"), (1.5, "T")]:
        ax.text(x, 2.2, label, ha="center", fontsize=15, weight="bold")
    ax.text(-0.72, 1, "First toss", rotation=90, va="center", fontsize=12)
    for y, label in [(1.5, "H"), (0.5, "T")]:
        ax.text(-0.22, y, label, ha="center", va="center", fontsize=15, weight="bold")
    for x, y, outcome in [(0, 1, "HH"), (1, 1, "HT"), (0, 0, "TH"), (1, 0, "TT")]:
        chosen = outcome != "TT"
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor=pale if chosen else "#f5f5f5",
                               edgecolor="white", linewidth=4))
        ax.text(x + 0.5, y + 0.60, outcome, ha="center", va="center",
                fontsize=24, weight="bold", color=blue if chosen else ink)
        ax.text(x + 0.5, y + 0.23, "P = 1/4", ha="center", fontsize=12, color=ink)
    ax.add_patch(Rectangle((0, 1), 2, 1, fill=False, edgecolor="#bd6632",
                           linewidth=2.5, zorder=5))
    ax.add_patch(Rectangle((0, 0), 1, 2, fill=False, edgecolor="#3565af",
                           linewidth=2.5, linestyle="--", zorder=6))
    ax.text(2.4, 1.82, "A: first toss is heads", color="#9f5024", fontsize=12)
    ax.text(2.4, 1.46, "B: second toss is heads", color="#3565af", fontsize=12)
    ax.text(2.4, 0.94, "Both heads", fontsize=13, weight="bold", color=ink)
    ax.text(2.4, 0.61, r"$A\cap B=\{HH\}$", fontsize=14, color=ink)
    ax.text(2.4, 0.27, "Probability 1/4", fontsize=12, color=ink)
    ax.text(1, -0.31, "Shaded: at least one head", ha="center",
            fontsize=13, weight="bold", color=blue)
    ax.text(1, -0.59, r"$A\cup B=\{HH,HT,TH\}$     Probability $3/4$",
            ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.04, top=0.98)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
