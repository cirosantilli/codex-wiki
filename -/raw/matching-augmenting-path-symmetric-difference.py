"""Original P6 alternating-path toggle from a size-two to size-three matching.

Tested with Python 3.14.4 and matplotlib 3.10.7 (project dependencies).
Run from _media; saves its own basename PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


EDGES = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6))
BEFORE = {(2, 3), (4, 5)}
AFTER = BEFORE.symmetric_difference(EDGES)
BLUE = "#1765a8"
ORANGE = "#b15d08"


def path_row(ax, y, selected, label, toggle=False):
    used = {v for edge in selected for v in edge}
    ax.text(0.55, y + 0.42, label, ha="left", fontsize=14, weight="bold")
    for u, v in EDGES:
        chosen = (u, v) in selected
        color = BLUE if chosen else ORANGE if toggle else "#a4abb2"
        ax.plot([u, v], [y, y], color=color,
                linewidth=5.5 if chosen else 3 if toggle else 2.2,
                linestyle="-" if chosen else "--", zorder=1)
        if toggle:
            ax.text((u + v) / 2, y - 0.3, "remove" if chosen else "add",
                    color=color, ha="center", fontsize=12)
    for v in range(1, 7):
        free = v not in used
        ax.add_patch(Circle((v, y), 0.15, facecolor="#fff2d6" if free else "white",
                            edgecolor=ORANGE if free else BLUE,
                            linewidth=2.3, zorder=3))
        ax.text(v, y, str(v), ha="center", va="center", fontsize=14, zorder=4)
        if free:
            ax.text(v, y + 0.24, "free", color=ORANGE, ha="center", fontsize=12)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(9, 5.8), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.97, top=0.85, bottom=0.18)
    fig.suptitle("An augmenting path reassigns partners on P₆", y=0.965,
                 fontsize=18, weight="bold")
    path_row(ax, 1.95, BEFORE, "Before: M = {(2,3), (4,5)}     |M| = 2", toggle=True)
    ax.text(3.5, 1.03, "Toggle all five path edges together: M′ = M △ E(P)",
            ha="center", fontsize=14)
    path_row(ax, 0, AFTER, "After: M′ = {(1,2), (3,4), (5,6)}     |M′| = 3")
    ax.set(xlim=(0.5, 6.5), ylim=(-0.45, 2.55), aspect="equal")
    ax.axis("off")
    fig.text(0.5, 0.115, "The endpoints 1 and 6 are free before the toggle; afterwards all vertices are paired.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.055, "Three added edges − two removed edges = one extra pair.",
             ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
