"""Draw a finite n=4 trace and an infinite stalled loop.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    n, i, s = 4, 0, 0
    states = [(i, s, n - i)]
    while i < n:
        i = i + 1
        s = s + i
        states.append((i, s, n - i))
    assert states == [(0, 0, 4), (1, 1, 3), (2, 3, 2), (3, 6, 1), (4, 10, 0)]
    assert all(2 * acc == pos * (pos + 1) for pos, acc, _ in states)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.86, bottom=0.055)
    ax.set(xlim=(0, 11), ylim=(0, 6.4))
    ax.axis("off")
    ink, blue, green, orange = "#23334a", "#266ca0", "#21795f", "#bc641d"
    fig.suptitle("An invariant remembers; a variant proves progress", y=0.97,
                 fontsize=19, weight="bold", color=ink)
    fig.text(0.5, 0.9, "n = 4 • states shown just before each condition check • exact integers",
             ha="center", color=ink, fontsize=12)
    ax.axvline(7.05, ymin=0.04, ymax=0.98, color="#cbd1d9", lw=1)
    ax.text(0.1, 6.12, "Increment i, then add i", fontsize=15, weight="bold", color=blue)
    ax.text(7.45, 6.12, "Stalled body:  i = i", fontsize=15, weight="bold", color=orange)
    ax.text(0.1, 5.58, "i", weight="bold", ha="center", color=ink)
    ax.text(0.9, 5.58, "s", weight="bold", ha="center", color=ink)
    ax.text(2.3, 5.58, "V = 4 − i", weight="bold", color=ink)
    ax.text(5.9, 5.58, "i < 4 ?", weight="bold", color=ink, ha="center")

    for row, (pos, acc, variant) in enumerate(states):
        y = 4.95 - row * 0.87
        ax.add_patch(FancyBboxPatch((-0.13, y - 0.3), 6.85, 0.6,
                                   boxstyle="round,pad=0.04", linewidth=0,
                                   facecolor="#eaf6ef" if variant == 0 else "#eef6fd"))
        ax.text(0.1, y, str(pos), ha="center", va="center", fontsize=16, color=ink)
        ax.text(0.9, y, str(acc), ha="center", va="center", fontsize=16, color=ink)
        for k in range(variant):
            ax.add_patch(Rectangle((2.3 + 0.47 * k, y - 0.17), 0.35, 0.34,
                                   facecolor=blue, edgecolor="white"))
        ax.text(4.55, y, str(variant), ha="center", va="center", fontsize=16, color=blue)
        ax.text(5.9, y, "false → exit" if variant == 0 else "true", va="center",
                ha="center", color=green if variant == 0 else ink, fontsize=12)
        if row < n:
            ax.add_patch(FancyArrowPatch((1.55, y - 0.32), (1.55, y - 0.54),
                                        arrowstyle="-|>", mutation_scale=12, color=blue))
            ax.text(1.73, y - 0.435, f"+{pos + 1}", va="center", fontsize=11, color=blue)

    for y in (4.85, 3.48, 2.11):
        ax.add_patch(FancyBboxPatch((7.55, y - 0.37), 2.95, 0.74,
                                   boxstyle="round,pad=0.07", facecolor="#fff4e6",
                                   edgecolor=orange, linewidth=1.2))
        ax.text(9.025, y, "i = 0,  s = 0,  V = 4", ha="center", va="center", color=ink)
    for y in (4.4, 3.03):
        ax.add_patch(FancyArrowPatch((9.025, y), (9.025, y - 0.45),
                                    arrowstyle="-|>", mutation_scale=13, color=orange))
    ax.text(9.025, 1.24, "⋮", ha="center", va="center", fontsize=26, color=orange)
    ax.text(3.3, 0.63, "Four additions; return s = 10\n" + r"$2\cdot10=4\cdot5$",
            color=green, ha="center", va="center", fontsize=13, linespacing=1.6)
    ax.text(9.025, 0.5, "Equation stays true.\nCondition stays true. No exit.",
            color=orange, ha="center", va="center", linespacing=1.6)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
