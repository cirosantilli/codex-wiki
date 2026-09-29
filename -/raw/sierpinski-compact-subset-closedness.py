"""Generate sierpinski-compact-subset-closedness.png in the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
Point locations are schematic; open and closed sets are listed exactly.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.3), dpi=120, facecolor="white")
    ink, blue, orange = "#263746", "#2269a4", "#c25d12"
    rows = [
        ("Discrete two-point space", r"$\varnothing,\ \{0\},\ \{1\},\ S$",
         r"$\varnothing,\ \{0\},\ \{1\},\ S$", "Hausdorff", "K is compact and closed", blue),
        ("Sierpiński space", r"$\varnothing,\ \{1\},\ S$",
         r"$\varnothing,\ \{0\},\ S$", "Not Hausdorff", "K is compact but not closed", orange),
    ]
    for ax, (title, opens, closed, separation, result, color) in zip(axes, rows):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.set_title(title, fontsize=14, pad=12, color=ink)
        ax.text(.5, .91, separation, ha="center", color=color, fontsize=12)
        ax.add_patch(Ellipse((.5, .64), .87, .33, facecolor="white", edgecolor=ink, lw=1.5))
        ax.add_patch(Ellipse((.72, .64), .26, .23, facecolor="#fff2df", edgecolor=color, lw=2))
        ax.scatter([.28, .72], [.64, .64], s=60, color=ink, zorder=3)
        ax.text(.28, .69, "0", ha="center", fontsize=13)
        ax.text(.72, .69, "1", ha="center", fontsize=13)
        ax.text(.72, .54, r"$K=\{1\}$", ha="center", fontsize=12, color=color)
        ax.text(.10, .77, "S", fontsize=12, color=ink)
        ax.text(.5, .40, "Open sets: " + opens, ha="center", fontsize=12, color=ink)
        ax.text(.5, .30, "Closed sets: " + closed, ha="center", fontsize=12, color=ink)
        ax.text(.5, .16, result, ha="center", fontsize=12, color=color, weight="bold")
    fig.suptitle("Compactness depends on the subset; closedness depends on the ambient topology",
                 fontsize=12, y=.97)
    fig.text(.5, .045, "Every subset here is compact because it is finite. Ovals only mark sets, not open neighborhoods.",
             ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=.025, right=.975, top=.85, bottom=.10, wspace=.13)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
