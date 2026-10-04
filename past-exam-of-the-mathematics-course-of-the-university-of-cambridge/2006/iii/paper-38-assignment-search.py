#!/usr/bin/env python3
"""Draw the completed best-bound assignment search; output PNG to caller CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


def main():
    nodes = {
        "root": (8.0, 7, 58), "a1": (3.8, 5, 60), "a2": (10.2, 5, 58),
        "a3": (14.5, 5, 65), "a4": (17.5, 5, 78),
        "a1b2": (1, 3, 68), "a1b3": (4, 3, 61), "a1b4": (7, 3, 66),
        "a2b1": (8.5, 3, 68), "a2b3": (11, 3, 59), "a2b4": (13.5, 3, 64),
        "a1b3c2": (3, 1, 69), "a1b3c4": (5, 1, 61),
        "a2b3c1": (10, 1, 64), "a2b3c4": (12, 1, 65),
    }
    edges = [
        ("root", "a1", "a = 1"), ("root", "a2", "a = 2"),
        ("root", "a3", "a = 3"), ("root", "a4", "a = 4"),
        ("a1", "a1b2", "b = 2"), ("a1", "a1b3", "b = 3"),
        ("a1", "a1b4", "b = 4"),
        ("a2", "a2b1", "b = 1"), ("a2", "a2b3", "b = 3"),
        ("a2", "a2b4", "b = 4"),
        ("a1b3", "a1b3c2", "c = 2"), ("a1b3", "a1b3c4", "c = 4"),
        ("a2b3", "a2b3c1", "c = 1"), ("a2b3", "a2b3c4", "c = 4"),
    ]
    optimal = {"root", "a1", "a1b3", "a1b3c4"}
    pruned = {"a3", "a4", "a1b2", "a1b4", "a2b1", "a2b4",
              "a1b3c2", "a2b3c4"}
    green, gray, blue = "#17774b", "#8b9199", "#2d4e76"
    fig, ax = plt.subplots(figsize=(11.6, 5.8), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    for source, target, label in edges:
        x0, y0, _ = nodes[source]
        x1, y1, _ = nodes[target]
        color = green if source in optimal and target in optimal else gray if target in pruned else blue
        ax.plot([x0, x1], [y0, y1], color=color,
                linewidth=2.5 if color == green else 1.4,
                linestyle="--" if target in pruned else "-", zorder=1)
        ax.text((x0+x1)/2, (y0+y1)/2+0.13, label, fontsize=10,
                ha="center", va="center", color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.1})
    for name, (x, y, bound) in nodes.items():
        color = green if name in optimal else gray if name in pruned else blue
        face = "#e2f2e8" if name in optimal else "white"
        ax.add_patch(Circle((x, y), 0.34, facecolor=face, edgecolor=color,
                            linewidth=2 if name in optimal else 1.4, zorder=2))
        ax.text(x, y, str(bound), ha="center", va="center", fontsize=11,
                color=color, zorder=3)
    ax.text(5, 0.32, "Optimal: (a,b,c,d) = (1,3,4,2)", color=green,
            ha="center", fontsize=11, fontweight="bold")
    ax.text(10, 0.32, "First incumbent: 64", color=blue, ha="center", fontsize=10)
    ax.set_title("Completed best-bound search for the assignment problem\n"
                 "Circle values are lower bounds; leaves show completed costs",
                 fontsize=13, pad=10)
    ax.legend(handles=[
        Line2D([0], [0], color=green, linewidth=2.5, label="Optimal branch"),
        Line2D([0], [0], color=blue, label="Earlier exploration"),
        Line2D([0], [0], color=gray, linestyle="--", label="Pruned or more expensive"),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.035), ncol=3, frameon=False, fontsize=10)
    ax.set(xlim=(0.4, 18.2), ylim=(-0.05, 7.5), aspect="equal")
    ax.axis("off")
    fig.savefig(Path.cwd() / "paper-38-assignment-search.png", dpi=130,
                facecolor="white", transparent=False, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


if __name__ == "__main__":
    main()
