"""Draw connected branch sets, their quotient triangle, and a path minor.

Python 3.14, matplotlib 3.10.7. Run from _media; output goes to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse


COLORS = {"A": "#2268a8", "B": "#b85b13", "C": "#258354"}
PALE = {"A": "#e5effa", "B": "#fff0da", "C": "#e6f5e9"}


def node(ax, label, position, group):
    ax.add_patch(Circle(position, 0.17, facecolor="white", edgecolor=COLORS[group],
                        linewidth=2, zorder=4))
    ax.text(*position, label, ha="center", va="center", fontsize=14,
            color=COLORS[group], weight="bold", zorder=5)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10, 4.75), dpi=120, facecolor="white")
    host = fig.add_axes((0.025, 0.22, 0.37, 0.58))
    quotient = fig.add_axes((0.46, 0.22, 0.22, 0.58))
    path = fig.add_axes((0.765, 0.22, 0.22, 0.58))
    pos = {"1": (-1.0, 0.8), "2": (-1.0, -0.5),
           "3": (0.0, -1.1), "4": (1.0, -0.5),
           "5": (1.0, 0.8), "6": (0.0, 1.4)}
    groups = {"1": "A", "2": "A", "3": "B", "4": "B", "5": "C", "6": "C"}
    for a, b in [("1", "2"), ("3", "4"), ("5", "6")]:
        group = groups[a]
        p, q = pos[a], pos[b]
        centre = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        angle = {"A": 90, "B": 31, "C": -31}[group]
        length = 1.8 if group == "A" else 1.65
        host.add_patch(Ellipse(centre, length, 0.65, angle=angle,
                               facecolor=PALE[group], edgecolor=COLORS[group],
                               linewidth=1.2, zorder=0))
        host.plot(*zip(p, q), color=COLORS[group], linewidth=3, zorder=1)
    for a, b, label, text_pos in [
        ("2", "3", "AB: 23", (-0.95, -1.17)),
        ("4", "5", "BC: 45", (1.14, 0.12)),
        ("6", "1", "CA: 61", (-0.8, 1.57)),
    ]:
        host.plot(*zip(pos[a], pos[b]), color="#34495e", linewidth=2, zorder=1)
        host.text(*text_pos, label, fontsize=11, color="#34495e",
                  ha="left" if label.startswith("BC") else "center")
    host.plot(*zip(pos["2"], pos["4"]), color="#68737e", linewidth=1.8,
              linestyle="--", zorder=2)
    host.text(0, -0.36, "extra AB: 24", ha="center", fontsize=11, color="#68737e")
    for label, position in pos.items():
        node(host, label, position, groups[label])
    target = {"A": (-0.9, 0.9), "B": (0.9, 0.9), "C": (0, -0.9)}
    for ax, edges in [(quotient, [("A", "B"), ("B", "C"), ("C", "A")]),
                      (path, [("A", "B"), ("B", "C")])]:
        for a, b in edges:
            ax.plot(*zip(target[a], target[b]), color="#34495e", linewidth=2.2)
        for label, position in target.items():
            node(ax, label, position, label)
    for ax in (host, quotient, path):
        ax.set(xlim=(-1.65, 1.75), ylim=(-1.5, 1.85), aspect="equal")
        ax.axis("off")
    fig.suptitle("Branch sets retain selected adjacencies", fontsize=16, weight="bold", y=0.97)
    fig.text(0.21, 0.84, "Host: 6 vertices, 7 edges", ha="center", weight="bold")
    fig.text(0.57, 0.84, "Triangle minor", ha="center", weight="bold")
    fig.text(0.875, 0.84, "Path minor", ha="center", weight="bold")
    overlay = fig.add_axes((0, 0, 1, 1), frameon=False)
    overlay.set(xlim=(0, 1), ylim=(0, 1))
    overlay.axis("off")
    for start, end in [(0.397, 0.455), (0.685, 0.758)]:
        overlay.annotate("", xy=(end, 0.53), xytext=(start, 0.53),
                         arrowprops={"arrowstyle": "->", "lw": 1.6})
    fig.text(0.427, 0.34, "contract\n12, 34, 56", ha="center", fontsize=10)
    fig.text(0.721, 0.34, "delete\nAC", ha="center", fontsize=10)
    for x, group, members in [(0.16, "A", "{1, 2}"), (0.5, "B", "{3, 4}"),
                              (0.83, "C", "{5, 6}")]:
        fig.text(x, 0.145, f"{group} = {members}", color=COLORS[group],
                 weight="bold", ha="center", fontsize=13)
    fig.text(0.5, 0.055, "Coloured internal edges establish connectedness; black edges witness target adjacency.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
