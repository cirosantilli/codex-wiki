"""Draw the first 18 elements at their actual 18-column table positions.

Writes first-three-periods.png in the current working directory.
Run from _media to produce the repository image. Colours distinguish columns,
not measured trends. Counts are neutral ground-state shell occupancies only.
Positions and symbols: https://iupac.org/what-we-do/periodic-table-of-elements/
Configurations: OpenStax Chemistry 2e, section 6.4.
Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


# atomic number, symbol, period, group, neutral ground-state shell occupancies
ELEMENTS = (
    (1, "H", 1, 1, (1,)), (2, "He", 1, 18, (2,)),
    (3, "Li", 2, 1, (2, 1)), (4, "Be", 2, 2, (2, 2)),
    (5, "B", 2, 13, (2, 3)), (6, "C", 2, 14, (2, 4)),
    (7, "N", 2, 15, (2, 5)), (8, "O", 2, 16, (2, 6)),
    (9, "F", 2, 17, (2, 7)), (10, "Ne", 2, 18, (2, 8)),
    (11, "Na", 3, 1, (2, 8, 1)), (12, "Mg", 3, 2, (2, 8, 2)),
    (13, "Al", 3, 13, (2, 8, 3)), (14, "Si", 3, 14, (2, 8, 4)),
    (15, "P", 3, 15, (2, 8, 5)), (16, "S", 3, 16, (2, 8, 6)),
    (17, "Cl", 3, 17, (2, 8, 7)), (18, "Ar", 3, 18, (2, 8, 8)),
)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(12.8, 5.8), dpi=110)
    fig.subplots_adjust(left=0.055, right=0.985, bottom=0.27, top=0.76)
    fig.suptitle("First three periods: atomic number and shell counts", fontsize=18, y=0.96)
    fig.text(0.5, 0.885, "Neutral ground states only; colours distinguish group columns, not property trends",
             ha="center", fontsize=12)
    colors = {1: "#d9edf6", 2: "#f8e4ce", 13: "#ebe0f3", 14: "#e3e7eb",
              15: "#dceaf8", 16: "#edeecf", 17: "#f7dfe4", 18: "#dceee1"}
    ax.set(xlim=(-0.85, 18.05), ylim=(-0.05, 3.08))
    ax.axis("off")
    for group in np.arange(1, 19):
        ax.text(group - 0.5, 3.20, str(group), ha="center", va="bottom", fontsize=11,
                clip_on=False)
    ax.text(8.5, 3.57, "Group (column)", ha="center", fontsize=12, clip_on=False)
    for period in (1, 2, 3):
        ax.text(-0.36, 3 - period + 0.5, str(period), ha="center", va="center", fontsize=13)
    ax.text(-0.73, 1.5, "Period (row)", rotation=90, va="center", ha="center", fontsize=12)
    for z, symbol, period, group, shell_counts in ELEMENTS:
        x, y = group - 1, 3 - period
        ax.add_patch(Rectangle((x + 0.025, y + 0.025), 0.95, 0.95,
                               facecolor=colors[group], edgecolor="#82909a", lw=1))
        ax.text(x + 0.14, y + 0.81, str(z), fontsize=10, va="center")
        ax.text(x + 0.5, y + 0.52, symbol, fontsize=17, weight="bold", ha="center", va="center")
        ax.text(x + 0.5, y + 0.17, ",".join(map(str, shell_counts)),
                fontsize=10, ha="center", va="center")
    ax.text(7, 1.51, "Columns 3–12 have no entries\nin the first three periods",
            ha="center", va="center", color="#67727a", fontsize=13)
    fig.text(0.075, 0.185, "Cell key: upper-left = atomic number Z; centre = symbol; bottom = shell counts",
             fontsize=12)
    fig.text(0.075, 0.124, "Compare Li (2,1) with Na (2,8,1): one outer electron in each.", fontsize=12)
    fig.text(0.075, 0.063, "The 2,8,8 summary stops at Ar. It is not a general shell-filling rule or an orbit model.",
             fontsize=12)
    fig.savefig(Path("first-three-periods.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
