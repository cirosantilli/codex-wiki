"""Draw exactly 40 distinct observed individuals in two overlapping sample sets.

Tested with Python 3.14.4 and Matplotlib 3.10.7 (Debian +dfsg1 build).
Run from _media; write an opaque white PNG with this script's basename to CWD.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    first = set(range(1, 21))
    second = set(range(16, 41))
    assert (len(first), len(second), len(first & second), len(first | second)) == (20, 25, 5, 40)
    groups = (
        (sorted(first - second), (0.65, 1.75, 2.85), "#24669b"),
        (sorted(first & second), (4.15,), "#754a9f"),
        (sorted(second - first), (5.45, 6.55, 7.65, 8.75), "#168173"),
    )
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 5.2), dpi=100)
    ax.add_patch(FancyBboxPatch((0.0, 0.35), 4.6, 6.0, boxstyle="round,pad=0.12",
                              facecolor="#edf5fc", edgecolor="#24669b", linewidth=2))
    ax.add_patch(FancyBboxPatch((3.7, 0.35), 5.65, 6.0, boxstyle="round,pad=0.12",
                              facecolor="#eaf7f3", edgecolor="#168173", linewidth=2))
    ax.add_patch(FancyBboxPatch((3.7, 0.35), 0.9, 6.0, boxstyle="round,pad=0.12",
                              facecolor="#f1eafb", edgecolor="none"))
    # Each identifier occupies one position, including the five shared identifiers.
    plotted_ids = []
    for ids, columns, color in groups:
        positions = [(x, y) for y in (5, 4, 3, 2, 1) for x in columns]
        assert len(ids) == len(positions)
        ax.scatter([x for x, y in positions], [y for x, y in positions],
                   s=150, color=color, edgecolor="white", linewidth=0.8, zorder=4)
        plotted_ids.extend(ids)
    assert len(plotted_ids) == len(set(plotted_ids)) == 40
    assert sum(len(collection.get_offsets()) for collection in ax.collections) == 40
    ax.text(2.3, 7.05, "First sample A: M = 20", ha="center", color="#24669b", weight="bold")
    ax.text(6.7, 7.05, "Second sample B: C = 25", ha="center", color="#168173", weight="bold")
    ax.text(1.75, 5.85, "First only: 15", ha="center", color="#24669b")
    ax.text(4.15, 5.82, "Shared\nR = 5", ha="center", color="#754a9f", fontsize=10)
    ax.text(7.1, 5.85, "Second only: 20", ha="center", color="#168173")
    ax.text(4.65, -0.25, "Distinct observed individuals: 15 + 5 + 20 = 40", ha="center", weight="bold")
    ax.set(xlim=(-0.3, 9.7), ylim=(-0.75, 7.5))
    ax.axis("off")
    fig.suptitle("Mark and recapture: overlap carries information", y=0.97, fontsize=16, weight="bold")
    fig.text(0.5, 0.035, "One dot = one individual.  Unobserved individuals are not drawn.  Constructed toy counts.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.045, right=0.98, top=0.87, bottom=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
