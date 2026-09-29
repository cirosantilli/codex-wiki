"""Draw an original AB step-growth count; run from _media.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def draw_chain(ax, x, y, length, new_join=None):
    spacing = 0.53
    for j in range(length - 1):
        ax.plot([x + j * spacing, x + (j + 1) * spacing], [y, y],
                color="#178249" if j == new_join else "#425568",
                lw=4 if j == new_join else 2.5, zorder=1)
    for j in range(length):
        ax.add_patch(Circle((x + j * spacing, y), 0.16,
                            facecolor="#eaf0f7", edgecolor="#425568", lw=1.4, zorder=2))
    ax.text(x - 0.27, y, "A", color="#b34b15", ha="center", va="center", fontsize=12)
    ax.text(x + (length - 1) * spacing + 0.27, y, "B", color="#285da8",
            ha="center", va="center", fontsize=12)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.4, 6.3), facecolor="white")
    ax.set(xlim=(-0.4, 10.1), ylim=(-0.55, 5.8))
    ax.axis("off")
    fig.suptitle("Step growth: joining chains reduces the molecule count", fontsize=17, y=0.98)
    rows = [([1] * 8, 4.65, "Eight AB feed molecules", 0),
            ([2, 3, 1, 1, 1], 2.85, "Three joins already made", 3),
            ([5, 1, 1, 1], 1.05, "Join the two-unit and three-unit chains", 4)]
    for lengths, y, label, joins in rows:
        ax.text(-0.2, y + 0.57, label, fontsize=13, weight="bold")
        x = 0.15
        for i, length in enumerate(lengths):
            draw_chain(ax, x, y, length, new_join=1 if joins == 4 and i == 0 else None)
            x += (length - 1) * 0.53 + 0.92
        n = len(lengths)
        assert sum(lengths) == 8 and 8 - n == joins
        remaining = 8 - joins
        ax.text(7.5, y + 0.22, f"N = {n},   joins = {joins}", fontsize=12)
        ax.text(7.5, y - 0.13, f"A left = B left = {remaining}", fontsize=12)
        ax.text(7.5, y - 0.49, rf"$p={joins}/8,\quad X_n=8/{n}$", fontsize=13)
    for y in [3.75, 1.95]:
        ax.annotate("", xy=(6.75, y - 0.3), xytext=(6.75, y + 0.2),
                    arrowprops={"arrowstyle": "->", "color": "#425568", "lw": 1.8})
    ax.text(-0.15, -0.02, "Circle = one feed-derived unit; line = joining bond; letters = unreacted groups",
            fontsize=11.5)
    ax.text(-0.15, -0.43, "Green bond: 2 + 3 → 5 units. One join removes one molecule and one A/B pair.",
            fontsize=11.5, color="#17683c")
    fig.subplots_adjust(left=0.04, right=0.98, top=0.9, bottom=0.03)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
