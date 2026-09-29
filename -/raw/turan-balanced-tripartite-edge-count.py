"""Draw the balanced tripartite T_3(8) and its exact edge and clique counts.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig, (ax, counts) = plt.subplots(1, 2, figsize=(9.2, 5.2), dpi=120,
                                    gridspec_kw={"width_ratios": [1.25, 1]})
    parts = [[(0, y) for y in (0.4, 1.4, 2.4)],
             [(2.7, y) for y in (0.4, 1.4, 2.4)],
             [(x, 4.0) for x in (0.85, 1.85)]]
    colors = ["#176c9d", "#af650d", "#25794f"]
    for i, j in combinations(range(3), 2):
        for a in parts[i]:
            for b in parts[j]:
                ax.plot([a[0], b[0]], [a[1], b[1]], lw=1.2,
                        color="#95a4af", alpha=0.75, zorder=1)
    for i, (part, color) in enumerate(zip(parts, colors)):
        xs, ys = zip(*part)
        ax.add_patch(FancyBboxPatch((min(xs) - 0.34, min(ys) - 0.33),
                     max(xs) - min(xs) + 0.68, max(ys) - min(ys) + 0.66,
                     boxstyle="round,pad=0.04", linewidth=1.3, edgecolor=color,
                     facecolor="white", zorder=0))
        for k, (x, y) in enumerate(part, 1):
            ax.scatter(x, y, s=270, facecolor=color, edgecolor="white", linewidth=1.5, zorder=3)
            ax.text(x, y, rf"${'abc'[i]}_{k}$", ha="center", va="center", fontsize=11,
                    color="white", zorder=4)
    ax.text(-0.52, 1.4, "A: 3", ha="right", va="center", fontsize=13, color=colors[0])
    ax.text(3.22, 1.4, "B: 3", ha="left", va="center", fontsize=13, color=colors[1])
    ax.text(1.35, 4.65, "C: 2", ha="center", fontsize=13, color=colors[2])
    ax.set(xlim=(-1.3, 4.0), ylim=(-0.45, 5.05), aspect="equal")
    ax.axis("off")
    counts.axis("off")
    counts.text(0.02, 0.92, "Count each pair of parts once", fontsize=13, fontweight="bold")
    for y, label in zip((0.80, 0.69, 0.58),
                        (r"A–B: $3\times3=9$ edges", r"A–C: $3\times2=6$ edges",
                         r"B–C: $3\times2=6$ edges")):
        counts.text(0.04, y, label, fontsize=14)
    counts.text(0.04, 0.43, r"Total: $9+6+6=21$ edges", fontsize=15, fontweight="bold")
    counts.text(0.04, 0.27, r"No $K_4$: four vertices, three parts", fontsize=12)
    counts.text(0.04, 0.18, "Two must share an independent part.", fontsize=11)
    counts.text(0.04, 0.04, r"Triangles: $3\times3\times2=18$", fontsize=13)
    fig.suptitle(r"Balanced tripartite construction: $T_3(8)=K_{3,3,2}$", fontsize=17, y=0.96)
    fig.text(0.5, 0.07, "Every cross edge is present; every edge inside a part is absent.",
             ha="center", fontsize=12, color="#495765")
    fig.text(0.5, 0.025, "Only labelled dots are vertices; line crossings are not vertices.",
             ha="center", fontsize=10, color="#495765")
    fig.subplots_adjust(left=0.025, right=0.98, top=0.86, bottom=0.14, wspace=0.02)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
