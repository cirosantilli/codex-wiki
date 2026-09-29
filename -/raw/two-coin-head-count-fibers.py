"""Draw head-count fibers and their exact masses (Python 3.14, matplotlib 3.10)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(9.2, 5.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ink, blue, pale = "#243442", "#16617d", "#e1f1f5"
    ax.text(5, 5.70, "Head count: four outcomes, three values", ha="center",
            fontsize=19, weight="bold", color=ink)
    ax.text(1.8, 5.12, r"Outcomes in $\Omega$", ha="center", fontsize=14, color=ink)
    ax.text(5.1, 5.12, r"$X$ counts heads", ha="center", fontsize=14, color=ink)
    ax.text(8.1, 5.12, "Values and probabilities", ha="center", fontsize=14, color=ink)
    source = {"HH": 4.3, "HT": 3.25, "TH": 2.2, "TT": 1.15}
    target = {2: 4.3, 1: 2.725, 0: 1.15}
    counts = {o: o.count("H") for o in source}
    for outcome, y in source.items():
        chosen = counts[outcome] >= 1
        ax.add_patch(FancyBboxPatch((0.7, y - 0.35), 2.2, 0.7,
                                   boxstyle="round,pad=0.04", linewidth=1.5,
                                   edgecolor=blue if chosen else "#78848c",
                                   facecolor=pale if chosen else "#f5f5f5"))
        ax.text(1.27, y, outcome, ha="center", va="center", fontsize=19,
                weight="bold", color=ink)
        ax.text(2.24, y, "1/4", ha="center", va="center", fontsize=14, color=ink)
        ax.add_patch(FancyArrowPatch((3.02, y), (6.68, target[counts[outcome]]),
                                    arrowstyle="-|>", mutation_scale=18, linewidth=2,
                                    color=blue if chosen else "#78848c"))
    masses = {0: "1/4", 1: "1/4 + 1/4 = 1/2", 2: "1/4"}
    for value, y in target.items():
        chosen = value >= 1
        ax.add_patch(FancyBboxPatch((6.8, y - 0.47), 2.7, 0.94,
                                   boxstyle="round,pad=0.04", linewidth=1.5,
                                   edgecolor=blue if chosen else "#78848c",
                                   facecolor=pale if chosen else "#f5f5f5"))
        ax.text(8.15, y + 0.18, str(value), ha="center", va="center",
                fontsize=23, weight="bold", color=ink)
        ax.text(8.15, y - 0.22, masses[value], ha="center", va="center",
                fontsize=13, color=ink)
    ax.text(5, 0.46, r"Shaded values: $\{1,2\}$  $\longleftarrow$  shaded outcomes: $\{HH,HT,TH\}$",
            ha="center", fontsize=13, color=blue)
    ax.text(5, 0.10, r"$X^{-1}(\{1,2\})=\{X\geq1\}$     Probability $1/2+1/4=3/4$",
            ha="center", fontsize=13, color=ink)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.98)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
