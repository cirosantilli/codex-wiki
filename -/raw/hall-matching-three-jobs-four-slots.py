"""Draw an original Hall matching example; output the same basename in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def main():
    left = {"a": (0, 2.7), "b": (0, 1.5), "c": (0, 0.3)}
    right = {"1": (3, 3), "2": (3, 2), "3": (3, 1), "4": (3, 0)}
    allowed = [("a", "1"), ("a", "2"), ("b", "1"),
               ("c", "2"), ("c", "3"), ("c", "4")]
    matching = {("a", "2"), ("b", "1"), ("c", "3")}
    fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=150, facecolor="white")
    ax.set_facecolor("white")
    for a, b in allowed:
        if (a, b) not in matching:
            ax.plot([left[a][0], right[b][0]], [left[a][1], right[b][1]],
                    color="#b7bec7", linewidth=1.5, zorder=1)
    for a, b in sorted(matching):
        ax.plot([left[a][0], right[b][0]], [left[a][1], right[b][1]],
                color="#145a9b", linewidth=4, zorder=2)
    for points, dx, align in [(left, -0.22, "right"), (right, 0.22, "left")]:
        for label, (x, y) in points.items():
            unmatched = label == "4"
            ax.scatter(x, y, s=280, facecolor="white" if unmatched else "#145a9b",
                       edgecolor="#145a9b", linewidth=2, zorder=3)
            ax.text(x + dx, y, label, ha=align, va="center", fontsize=16)
    ax.text(0, 3.42, "Jobs L", ha="center", fontsize=14, weight="bold")
    ax.text(3, 3.42, "Slots R", ha="center", fontsize=14, weight="bold")
    ax.text(3.57, 0, "unused", va="center", fontsize=12, color="#475569")
    ax.set_title("Every job gets a distinct allowed slot", fontsize=16, pad=15)
    ax.legend(handles=[Line2D([0], [0], color="#145a9b", lw=4, label="Chosen matching"),
                       Line2D([0], [0], color="#b7bec7", lw=1.5, label="Other allowed pairs")],
              loc="lower center", bbox_to_anchor=(0.5, -0.12), ncol=2,
              frameon=False, fontsize=11)
    ax.set_xlim(-0.7, 4.15)
    ax.set_ylim(-0.3, 3.7)
    ax.axis("off")
    fig.subplots_adjust(left=0.07, right=0.97, top=0.87, bottom=0.15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
