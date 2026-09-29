"""Original P4 example: greedy middle edge versus maximum matching.

Tested with Python 3.14.4 and matplotlib 3.10.7 (project dependencies).
Run from _media; saves its own basename PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


EDGES = ((1, 2), (2, 3), (3, 4))
GREEDY = {(2, 3)}
MAXIMUM = {(1, 2), (3, 4)}
BLUE = "#1765a8"
GRAY = "#a4abb2"


def draw_path(ax, selected, title, note):
    used = {v for edge in selected for v in edge}
    for u, v in EDGES:
        ax.plot([u, v], [0, 0], color=BLUE if (u, v) in selected else GRAY,
                linewidth=6 if (u, v) in selected else 2.3, zorder=1,
                linestyle="-" if (u, v) in selected else "--")
    for v in range(1, 5):
        ax.add_patch(Circle((v, 0), 0.13, facecolor="white",
                            edgecolor=BLUE if v in used else "#333333",
                            linewidth=2.5, zorder=3))
        ax.text(v, 0, str(v), ha="center", va="center", fontsize=14, zorder=4)
        if v not in used:
            ax.text(v, -0.33, "free", ha="center", fontsize=12)
    ax.set_title(title, fontsize=15, weight="bold", pad=12)
    ax.text(2.5, -0.65, note, ha="center", fontsize=12)
    ax.set(xlim=(0.55, 4.45), ylim=(-0.92, 0.53), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, top=0.72, bottom=0.23, wspace=0.24)
    fig.suptitle("Greedy pairing can stop too early on P₄", fontsize=18,
                 weight="bold", y=0.96)
    draw_path(axes[0], GREEDY, "Middle first: maximal, size 1",
              "Neither outer edge can be added.")
    draw_path(axes[1], MAXIMUM, "Outer edges: maximum, size 2",
              "Four vertices allow at most two pairs.")
    fig.text(0.5, 0.16, "Blue solid: selected edge     Gray dashed: unselected edge",
             ha="center", fontsize=12)
    fig.text(0.5, 0.075, "Replacing the middle edge allows both outer edges to be selected.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
