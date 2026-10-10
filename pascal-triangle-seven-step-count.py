"""Draw Pascal's triangle with an original seven-step counting example.

Tested with Python 3.14, matplotlib 3.10.7; run from _media.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(9, 6.4), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.12, top=0.86)
    ax.set_facecolor("white")
    colors = {(6, 2): "#c76316", (6, 3): "#2477a2", (7, 3): "#603fa0"}
    for k in (2, 3):
        ax.annotate("", xy=(-0.5, -7 + 0.28), xytext=(k - 3, -6 - 0.28),
                    arrowprops={"arrowstyle": "->", "color": colors[(6, k)],
                                "lw": 2.5, "mutation_scale": 14})
    for n in range(8):
        ax.text(-5.1, -n, f"n = {n}", va="center", ha="left", color="#414651")
        for k in range(n + 1):
            color = colors.get((n, k), "#dfe7ee")
            highlighted = (n, k) in colors
            ax.add_patch(Circle((k - n / 2, -n), 0.28,
                                facecolor=color if highlighted else "#f4f7fa",
                                edgecolor=color, lw=1.6, zorder=3))
            ax.text(k - n / 2, -n, str(comb(n, k)), va="center", ha="center",
                    color="white" if highlighted else "#222936",
                    weight="bold" if highlighted else "normal", zorder=4)
    for k in range(8):
        ax.text(k - 3.5, -7.65, f"k={k}", ha="center", va="top", fontsize=10)
    ax.set(xlim=(-5.35, 4.1), ylim=(-8.2, 0.55), aspect="equal")
    ax.axis("off")
    fig.suptitle("Pascal's triangle: three north steps among seven steps", y=0.97,
                 fontsize=17, weight="bold")
    fig.text(0.5, 0.895, r"$T_{n,k}=\binom{n}{k}$     Row $n$: total steps; column $k$: north steps",
             ha="center", fontsize=13)
    fig.text(0.5, 0.045, r"$T_{7,3}=T_{6,2}+T_{6,3}=15+20=35$",
             ha="center", fontsize=17, color="#603fa0")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
