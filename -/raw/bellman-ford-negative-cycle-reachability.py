"""Draw relevant and irrelevant negative cycles and reverse every arrow.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The output PNG is written to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.path import Path as MplPath


POSITIONS = {"S": (0, 1.5), "A": (2, 2.5), "B": (2, 0.5),
             "C": (4, 0.5), "T": (5.6, 2.5), "U": (5.2, -1.45)}
EDGES = (("S", "A", 4), ("S", "B", 5), ("A", "B", -2),
         ("B", "C", 3), ("C", "T", 2), ("A", "T", 8),
         ("C", "A", -4))
CYCLE = {("A", "B"), ("B", "C"), ("C", "A")}
LABEL_POSITIONS = {( "S", "A"): (0.85, 2.30),
                   ("S", "B"): (0.75, 0.67),
                   ("A", "B"): (1.62, 1.50),
                   ("B", "C"): (3, 0.21),
                   ("C", "T"): (5.10, 1.40),
                   ("A", "T"): (3.75, 2.77),
                   ("C", "A"): (3.30, 1.66)}


def panel(ax, reversed_arrows):
    ax.set(xlim=(-0.7, 6.3), ylim=(-2.45, 3.5), aspect="equal")
    ax.axis("off")
    for u, v, weight in EDGES:
        tail, head = (v, u) if reversed_arrows else (u, v)
        color = "#bb293a" if (u, v) in CYCLE else "#587a8c"
        ax.add_patch(FancyArrowPatch(POSITIONS[tail], POSITIONS[head],
                                    arrowstyle="-|>", mutation_scale=17,
                                    linewidth=2.1, color=color,
                                    shrinkA=21, shrinkB=21))
        ax.text(*LABEL_POSITIONS[u, v], str(weight).replace("-", "−"),
                ha="center", va="center", fontsize=12, color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for v, (x, y) in POSITIONS.items():
        affected = v in ("A", "B", "C", "T")
        edge = "#bb293a" if affected else "#263b48"
        face = "#fff0f1" if affected else "white"
        if v == "U":
            edge, face = "#687783", "#f1f3f5"
        ax.add_patch(Circle((x, y), 0.37, facecolor=face, edgecolor=edge,
                            linewidth=1.8, zorder=3))
        ax.text(x, y + 0.13, v, ha="center", va="center", fontsize=12,
                weight="bold", zorder=4)
        distance = r"$-\infty$" if affected else ("0" if v == "S" else r"$\infty$")
        ax.text(x, y - 0.16, distance, ha="center", va="center", fontsize=11,
                color=edge, zorder=4)
    ux, uy = POSITIONS["U"]
    loop_points = [(ux - 0.29, uy - 0.23), (ux - 1.0, uy - 1.12),
                   (ux + 1.0, uy - 1.12), (ux + 0.29, uy - 0.23)]
    if reversed_arrows:
        loop_points.reverse()
    loop = MplPath(loop_points, [MplPath.MOVETO] + [MplPath.CURVE4] * 3)
    ax.add_patch(FancyArrowPatch(path=loop,
                                arrowstyle="-|>", mutation_scale=14, linewidth=1.8,
                                color="#687783", zorder=2))
    ax.text(ux + 0.80, uy - 0.65, "−1", ha="center", fontsize=11, color="#687783")
    ax.text(3, -0.40, "cycle total = −3", ha="center", va="center",
            color="#a52131", fontsize=11)
    ax.text(1.55, -1.35, "S stays 0\nU stays ∞", ha="center", va="center",
            fontsize=12, color="#263b48")
    title = "Reversed arrows: distances TO sink S" if reversed_arrows else "Original arrows: distances FROM source S"
    ax.set_title(title, fontsize=12, weight="bold", pad=8)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.3), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.82, bottom=0.14, wspace=0.10)
    fig.suptitle("Negative cycles: which distances become −∞?", fontsize=18,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.89, "Add C→A of weight −4 and an isolated negative self-loop at U",
             ha="center", fontsize=12)
    panel(axes[0], False)
    panel(axes[1], True)
    fig.text(0.265, 0.115, "Affected: cycle vertices and their descendants", ha="center", fontsize=11)
    fig.text(0.755, 0.115, "Affected: cycle vertices and their ancestors", ha="center", fontsize=11)
    fig.text(0.5, 0.043, "A, B, C, T have distance −∞ in both panels.  The isolated cycle at U is irrelevant.",
             ha="center", fontsize=12, color="#263b48")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
