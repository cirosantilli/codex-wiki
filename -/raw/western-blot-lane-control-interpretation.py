"""Draw qualitative control lanes, not measured Western blot data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


BLUE = "#1764a0"
INK = "#203040"
GRAY = "#818b93"


def lane(ax, x, y, w, h):
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white",
                           edgecolor="#b8c5ce", lw=1.3))


def band(ax, x, y, w, color=BLUE, lw=6):
    ax.plot([x + .12, x + w - .12], [y, y], color=color, lw=lw,
            solid_capstyle="butt")


def main():
    fig, ax = plt.subplots(figsize=(12, 7.6), dpi=110, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 7.6))
    ax.axis("off")
    ax.text(6, 7.28, "Western blot controls ask different questions",
            ha="center", fontsize=19, weight="bold", color=INK)
    ax.text(6, 6.88, "Invented qualitative lane symbols • no measured positions, intensities or confirmed identity",
            ha="center", fontsize=11.5, color=INK)

    ax.text(.45, 6.34, "A  Is binding consistent with the proposed target?",
            fontsize=14, weight="bold", color=INK)
    xs = [1.8, 3.65, 5.5, 7.35]
    labels = ["Known positive", "Sample", "Target deleted", "No primary\n(matched sample)"]
    for x, label in zip(xs, labels):
        lane(ax, x, 3.7, 1.04, 1.75)
        ax.text(x + .52, 5.72, label, ha="center", va="center", fontsize=11, color=INK)
    for x in xs[:2]:
        band(ax, x, 4.96, 1.04)
    for x in xs[:3]:
        band(ax, x, 4.09, 1.04, GRAY, 5)
    ax.plot([.75, 8.6], [4.96, 4.96], color=BLUE, lw=.7, ls=":", zorder=0)
    ax.text(.52, 4.96, "candidate\nposition", ha="center", va="center",
            fontsize=9.5, color=BLUE)
    ax.text(9, 4.93, "Candidate disappears\nafter target deletion:\nsupports assignment", va="center",
            fontsize=11, color=BLUE)
    ax.text(9, 4.02, "Lower band persists:\nnot explained by target", va="center",
            fontsize=11, color=INK)
    ax.text(4.65, 3.36, "No-primary control tests secondary/reagent background; it cannot validate primary specificity.",
            ha="center", fontsize=10.3, color=INK)

    ax.text(.45, 2.85, "B  Did loading or transfer change with the target readout?",
            fontsize=14, weight="bold", color=INK)
    for x, label in [(2, "Sample A"), (4.1, "Sample B"), (6.2, "Patchy transfer")]:
        ax.text(x + .5, 2.47, label, ha="center", fontsize=11, color=INK)
        lane(ax, x, 1.97, 1, .24)
        lane(ax, x, .58, 1, 1.02)
    band(ax, 2, 2.09, 1, BLUE, 3)
    band(ax, 4.1, 2.09, 1, BLUE, 6)
    for y in [.74, .96, 1.18, 1.43]:
        band(ax, 2, y, 1, GRAY, 2)
        band(ax, 4.1, y, 1, GRAY, 4)
        if y < 1.1:
            band(ax, 6.2, y, 1, GRAY, 3)
    ax.text(1.63, 2.09, "Target", ha="right", va="center", fontsize=11, color=BLUE)
    ax.text(1.63, 1.09, "Total-protein\nstain", ha="right", va="center", fontsize=11, color=INK)
    ax.text(8.06, 2.03, "A target difference can accompany\na difference in total transferred protein.",
            va="center", fontsize=11, color=INK)
    ax.text(8.06, 1.12, "Blank patches suggest transfer trouble.\nA target signal alone cannot diagnose why.",
            va="center", fontsize=11, color=INK)
    ax.text(6, .18, "Check proportional response before normalization. Symbol thickness is explanatory only.",
            ha="center", fontsize=11, color=INK)
    fig.subplots_adjust(left=.015, right=.985, bottom=.01, top=.99)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
