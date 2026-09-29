"""Computed B3/S23 blinker diagram; Python 3.14, matplotlib 3.10.7.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Only writes the matching PNG basename in the current directory.
"""

from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INITIAL = {(-1, 0), (0, 0), (1, 0)}
LIVE_COLOR = "#164f72"


def neighbor_counts(live):
    return Counter(
        (x + dx, y + dy)
        for x, y in live
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )


def evolve(live):
    return {
        cell
        for cell, n in neighbor_counts(live).items()
        if n == 3 or (cell in live and n == 2)
    }


def draw_board(ax, live, counts=None):
    for y in range(-2, 3):
        for x in range(-2, 3):
            alive = (x, y) in live
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1,
                                   facecolor=LIVE_COLOR if alive else "white",
                                   edgecolor="#a7b2bb", linewidth=0.7))
            if counts is not None:
                ax.text(x, y, str(counts[(x, y)]), ha="center", va="center",
                        color="white" if alive else "#303943", fontsize=12)
    if counts is not None:
        for x, y in [(0, -1), (0, 1)]:
            ax.add_patch(Rectangle((x - 0.46, y - 0.46), 0.92, 0.92,
                                   fill=False, edgecolor="#b85417", linewidth=2.4))
    ax.set(xlim=(-2.5, 2.5), ylim=(2.5, -2.5), aspect="equal",
           xticks=range(-2, 3), yticks=range(-2, 3))
    ax.tick_params(length=0, labelsize=9)
    for spine in ax.spines.values():
        spine.set_visible(False)


def main():
    frames = [set(INITIAL)]
    for _ in range(2):
        frames.append(evolve(frames[-1]))
    assert frames[1] == {(0, -1), (0, 0), (0, 1)}
    assert frames[2] == frames[0]
    fig, axes = plt.subplots(1, 4, figsize=(10.4, 3.8), facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.98, bottom=0.24, top=0.78, wspace=0.28)
    titles = ["t = 0: horizontal", "Counts from t = 0", "t = 1: vertical", "t = 2: returned"]
    for ax, title, live, counts in zip(
        axes, titles, [frames[0], frames[0], frames[1], frames[2]],
        [None, neighbor_counts(frames[0]), None, None], strict=True
    ):
        draw_board(ax, live, counts)
        ax.set_title(title, fontsize=11, pad=10)
    fig.suptitle("Blinker: count first, then change every cell together", fontsize=15, y=0.97)
    fig.text(0.5, 0.16, "Blue = live. Numbers exclude the center cell. Orange outlines = the two births.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.085, "Endpoints have 1 neighbor and die; center has 2 and survives; births have exactly 3.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Computed toy pattern on an infinite dead background; y increases downward.",
             ha="center", fontsize=9, color="#49545e")
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
