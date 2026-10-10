"""Group all four-trial binary samples by their sufficient sum.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the working directory with this script's basename.
"""

from itertools import product
from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    groups = [[x for x in product((0, 1), repeat=4) if sum(x) == t] for t in range(5)]
    assert [len(group) for group in groups] == [comb(4, t) for t in range(5)]
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis("off")
    ax.text(0.2, 5.94, "Sixteen sequences, five sufficient-statistic groups", fontsize=17, weight="bold")
    ax.text(0.2, 5.58, "Independent Bernoulli(p) observations; fixed sample size n = 4", fontsize=12)
    ax.text(0.2, 5.02, "Sum T", fontsize=12, weight="bold")
    ax.text(1.3, 5.02, "Possible observed arrangements", fontsize=12, weight="bold")
    ax.text(8.3, 5.02, "P(X = x | T)", fontsize=12, weight="bold")
    colors = ["#edf2f8", "#e8f2ee", "#e7eefc", "#f8f0e3", "#f5eaf1"]
    for t, group in enumerate(groups):
        y = 4.45 - 0.85 * t
        ax.add_patch(FancyBboxPatch((0.15, y - 0.29), 9.65, 0.66, boxstyle="round,pad=0.02", facecolor=colors[t], edgecolor="#d4dae2"))
        ax.text(0.5, y, str(t), fontsize=16, weight="bold", va="center")
        for j, x in enumerate(group):
            ax.text(1.4 + j * 1.12, y, "".join(map(str, x)), fontsize=15, family="monospace", va="center", bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": "#72849a"})
        ax.text(8.65, y, "1" if len(group) == 1 else f"1/{len(group)}", fontsize=16, va="center", ha="center")
    ax.text(0.2, 0.42, r"Group mass: $P_p(T=t)=\binom{4}{t}p^t(1-p)^{4-t}$", fontsize=13)
    ax.text(0.2, 0.04, "For 0 < p < 1, every row is possible; p changes row masses, not within-row weights.", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.99, bottom=0.04, top=0.98)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
