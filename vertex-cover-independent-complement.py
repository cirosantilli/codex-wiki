"""Draw complementary optimum sets on C5; write the PNG basename to CWD.

Tested with Python 3.14.4 and Matplotlib 3.10.7, as in pyproject.toml.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../vertex-cover-independent-complement.py
"""
from math import cos, pi, sin
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    vertices = range(5)
    edges = [(i, (i + 1) % 5) for i in vertices]
    positions = {i: (cos(pi / 2 - 2 * pi * i / 5),
                     sin(pi / 2 - 2 * pi * i / 5)) for i in vertices}
    cover, independent = {1, 3, 4}, {0, 2}
    assert cover.isdisjoint(independent) and cover | independent == set(vertices)
    assert all(u in cover or v in cover for u, v in edges)
    assert all(not (u in independent and v in independent) for u, v in edges)
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.6), dpi=100, facecolor="white")
    panels = [(cover, "#a95012", "Minimum vertex cover", r"$C=\{1,3,4\},\quad\tau(C_5)=3$"),
              (independent, "#087f80", "Maximum independent set", r"$I=\{0,2\},\quad\alpha(C_5)=2$")]
    for ax, (selected, color, title, formula) in zip(axes, panels):
        for u, v in edges:
            ax.plot([positions[u][0], positions[v][0]],
                    [positions[u][1], positions[v][1]], color="#687380", lw=2, zorder=1)
        for v in vertices:
            chosen = v in selected
            ax.add_patch(Circle(positions[v], 0.15, facecolor=color if chosen else "white",
                                edgecolor=color if chosen else "#687380", lw=2, zorder=2))
            ax.text(*positions[v], str(v), ha="center", va="center", fontsize=14,
                    weight="bold", color="white" if chosen else "#253342", zorder=3)
        ax.set_title(title, fontsize=14, weight="bold", pad=14)
        ax.text(0, -1.23, formula, ha="center", fontsize=14)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.4, 1.3), aspect="equal")
        ax.axis("off")
    fig.suptitle("The same five-cycle, two complementary selections", fontsize=15, y=0.97)
    fig.text(0.5, 0.07, "Every edge touches orange on the left; no edge joins two teal vertices on the right.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.02, r"$I=V\setminus C\qquad\tau(C_5)+\alpha(C_5)=3+2=5$", ha="center", fontsize=13)
    fig.subplots_adjust(top=0.80, bottom=0.19, left=0.03, right=0.97, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
