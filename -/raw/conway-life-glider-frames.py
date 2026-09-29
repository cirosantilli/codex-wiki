"""Computed five-frame glider diagram; Python 3.14, matplotlib 3.10.7.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Only writes the matching PNG basename in the current directory.
"""

from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INITIAL = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
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


def draw_board(ax, live, ghost=False):
    for y in range(-1, 5):
        for x in range(-1, 5):
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1,
                                   facecolor=LIVE_COLOR if (x, y) in live else "white",
                                   edgecolor="#a7b2bb", linewidth=0.7))
    if ghost:
        for x, y in INITIAL:
            ax.add_patch(Rectangle((x - 0.43, y - 0.43), 0.86, 0.86, fill=False,
                                   edgecolor="#c65a16", linestyle="--", linewidth=1.6))
        ax.annotate("", xy=(3.15, 3.15), xytext=(2.15, 2.15),
                    arrowprops={"arrowstyle": "->", "color": "#c65a16", "lw": 2})
    ax.set(xlim=(-1.5, 4.5), ylim=(4.5, -1.5), aspect="equal",
           xticks=range(-1, 5), yticks=range(-1, 5))
    ax.tick_params(length=0, labelsize=8)
    for spine in ax.spines.values():
        spine.set_visible(False)


def main():
    frames = [set(INITIAL)]
    for _ in range(4):
        frames.append(evolve(frames[-1]))
    assert all(len(frame) == 5 for frame in frames)
    assert frames[4] == {(x + 1, y + 1) for x, y in frames[0]}
    fig, axes = plt.subplots(1, 5, figsize=(11.0, 3.65), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.985, bottom=0.28, top=0.76, wspace=0.30)
    for t, (ax, frame) in enumerate(zip(axes, frames, strict=True)):
        draw_board(ax, frame, ghost=t == 4)
        ax.set_title(f"t = {t}" + (": shifted" if t == 4 else ""), fontsize=11, pad=10)
    fig.suptitle("Glider: the same shape returns one cell right and one cell down", fontsize=15, y=0.97)
    fig.text(0.5, 0.18, "Every panel uses the same coordinates. Blue = live; orange dashes at t = 4 mark t = 0.",
             ha="center", fontsize=10.5)
    fig.text(0.5, 0.105, "Four synchronous B3/S23 steps give displacement (1, 1); no rule tells a cell to move.",
             ha="center", fontsize=10.5)
    fig.text(0.5, 0.035, "Computed toy pattern on an infinite dead background; x increases rightward, y downward.",
             ha="center", fontsize=9, color="#49545e")
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
