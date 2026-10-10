"""Draw a path-position bijection and its exact recursive arrival counts.

Tested with Python 3.14, matplotlib 3.10.7; run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.35, top=0.84, wspace=0.33)
    blue, orange, purple = "#2477a2", "#c76316", "#603fa0"
    for ax in axes:
        ax.set_facecolor("white")
        for x in range(5):
            ax.plot([x, x], [0, 3], color="#dfe5eb", lw=1, zorder=0)
        for y in range(4):
            ax.plot([0, 4], [y, y], color="#dfe5eb", lw=1, zorder=0)
        ax.set(xlim=(-0.35, 4.35), ylim=(-0.35, 3.35), aspect="equal",
               xticks=range(5), yticks=range(4))
        ax.set_xlabel("x  (east →)")
        ax.set_ylabel("y  (north ↑)")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.tick_params(length=0)
    word = "ENENEEN"
    x, y = 0, 0
    axes[0].scatter([0], [0], s=70, color="#222936", zorder=4)
    for step in word:
        nx, ny = x + (step == "E"), y + (step == "N")
        color = orange if step == "N" else blue
        axes[0].annotate("", xy=(nx, ny), xytext=(x, y),
                         arrowprops={"arrowstyle": "->", "lw": 3,
                                     "color": color, "shrinkA": 1, "shrinkB": 1})
        x, y = nx, ny
    axes[0].scatter([4], [3], s=75, color=purple, zorder=4)
    axes[0].set_title("One path: ENENEEN", fontsize=14, pad=14)
    counts = {}
    for y in range(4):
        for x in range(5):
            counts[x, y] = 1 if x == 0 or y == 0 else counts[x - 1, y] + counts[x, y - 1]
    special = {(3, 3): blue, (4, 2): orange, (4, 3): purple}
    for (x, y), value in counts.items():
        color = special.get((x, y), "#222936")
        axes[1].text(x, y, str(value), ha="center", va="center", fontsize=14,
                     weight="bold" if (x, y) in special else "normal",
                     color="white" if (x, y) in special else color,
                     bbox={"boxstyle": "round,pad=0.24", "facecolor": color if (x, y) in special else "white",
                           "edgecolor": "none"}, zorder=4)
    for start, color in [((3, 3), blue), ((4, 2), orange)]:
        axes[1].annotate("", xy=(4, 3), xytext=start,
                         arrowprops={"arrowstyle": "->", "lw": 2.5, "color": color,
                                     "shrinkA": 18, "shrinkB": 18})
    axes[1].set_title("All paths: last-step addition", fontsize=14, pad=14)
    fig.suptitle("Four east steps + three north steps = 35 paths", fontsize=18,
                 weight="bold", y=0.965)
    for i, step in enumerate(word, 1):
        left = 0.12 + (i - 1) * 0.041
        fig.text(left + 0.017, 0.265, str(i), ha="center", fontsize=10)
        fig.add_artist(Rectangle((left, 0.196), 0.034, 0.046, transform=fig.transFigure,
                                 facecolor=orange if step == "N" else "#edf4f8",
                                 edgecolor=orange if step == "N" else blue))
        fig.text(left + 0.017, 0.206, step, ha="center", fontsize=12,
                 color="white" if step == "N" else blue, weight="bold")
    fig.text(0.265, 0.137, r"North positions $\{2,4,7\}$ ↔ path", ha="center", fontsize=13)
    fig.text(0.75, 0.232, r"$P(4,3)=P(3,3)+P(4,2)$", ha="center", fontsize=14)
    fig.text(0.75, 0.16, r"$35=20+15$", ha="center", fontsize=17, color=purple)
    fig.text(0.5, 0.055, r"Choose the three north positions: $\binom{7}{3}=35$",
             ha="center", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
