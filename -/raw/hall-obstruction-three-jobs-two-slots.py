"""Draw an original three-vertices/two-neighbours Hall obstruction.

Output the same basename in CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch


def main():
    left = {"a": (0, 3), "b": (0, 2), "c": (0, 1), "d": (0, -0.4)}
    right = {"1": (3, 2.7), "2": (3, 1.3), "3": (3, 0), "4": (3, -0.8)}
    allowed = [(a, b) for a in "abc" for b in "12"] + [("d", "3"), ("d", "4")]
    matching = {("a", "1"), ("b", "2"), ("d", "3")}
    fig, ax = plt.subplots(figsize=(6.4, 5.4), dpi=150, facecolor="white")
    ax.set_facecolor("white")
    for x, y, width, height in [(-0.28, 0.7, 0.56, 2.6), (2.72, 1, 0.56, 2)]:
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.08", facecolor="#fff3f0",
                                   edgecolor="#b73727", linewidth=2, zorder=0))
    for a, b in allowed:
        chosen = (a, b) in matching
        ax.plot([left[a][0], right[b][0]], [left[a][1], right[b][1]],
                color="#145a9b" if chosen else "#b7bec7",
                linewidth=4 if chosen else 1.5, zorder=2 if chosen else 1)
    for points, dx, align in [(left, -0.45, "right"), (right, 0.45, "left")]:
        for label, (x, y) in points.items():
            unmatched = label in {"c", "4"}
            ax.scatter(x, y, s=230, facecolor="white" if unmatched else "#145a9b",
                       edgecolor="#145a9b", linewidth=2, zorder=3)
            ax.text(x + dx, y, label, ha=align, va="center", fontsize=16)
    ax.text(0, 3.6, "Jobs L", ha="center", fontsize=14, weight="bold")
    ax.text(3, 3.6, "Slots R", ha="center", fontsize=14, weight="bold")
    ax.text(0, 0.43, "S: 3 jobs", ha="center", fontsize=12, color="#b73727")
    ax.text(3, 0.73, "N(S): 2 slots", ha="center", fontsize=12, color="#b73727")
    ax.text(1.5, 2.04, "2 < 3", ha="center", fontsize=17, color="#b73727",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 4}, zorder=4)
    ax.set_title("Enough slots in total; too few for these jobs", fontsize=15, pad=15)
    ax.legend(handles=[Line2D([0], [0], color="#145a9b", lw=4, label="Matching of size 3"),
                       Line2D([0], [0], color="#b7bec7", lw=1.5, label="Other allowed pairs")],
              loc="lower center", bbox_to_anchor=(0.5, -0.11), ncol=2,
              frameon=False, fontsize=11)
    ax.text(1.5, -1.4, "c cannot use the spare slot 4", ha="center", fontsize=13)
    ax.set_xlim(-0.85, 3.85)
    ax.set_ylim(-1.6, 3.9)
    ax.axis("off")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.87, bottom=0.15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
