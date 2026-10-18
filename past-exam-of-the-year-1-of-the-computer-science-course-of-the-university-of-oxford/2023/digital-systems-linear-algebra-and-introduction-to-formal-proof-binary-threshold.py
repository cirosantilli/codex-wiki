"""Draw disjoint binary-prefix cases for an exact formula model count.

Tested with Python 3.14.4 and Matplotlib 3.10.7. Dependencies are declared
in the repository pyproject.toml. Write the opaque PNG into the CWD.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(9.0, 2.7), dpi=100, facecolor="white")
    groups = [(0, 8, "#bad5e8", "0***: 8 assignments"),
              (8, 10, "#b9ddc6", "100*: 2"),
              (10, 11, "#f3cc9f", "1010: 1"),
              (11, 16, "#e7e7e7", "Rejected: 5")]
    for first, last, color, label in groups:
        for value in range(first, last):
            ax.add_patch(Rectangle((value, 0), 1, 1, facecolor=color,
                                   edgecolor="white", linewidth=1.5))
            ax.text(value + 0.5, 0.66, str(value), ha="center", va="center", fontsize=11)
            ax.text(value + 0.5, 0.29, f"{value:04b}", ha="center", va="center", fontsize=8)
        height = 1.28 if first != 10 else 1.76
        ax.annotate(label, xy=((first + last) / 2, 1.02),
                    xytext=((first + last) / 2, height), ha="center", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": "#666666"})
    ax.plot((11, 11), (-0.13, 1.11), color="#a13d24", linewidth=2)
    ax.text(11, -0.35, "k = 11", color="#a13d24", ha="center", fontsize=11)
    ax.set_xlim(-0.2, 16.2)
    ax.set_ylim(-0.65, 2.15)
    ax.axis("off")
    fig.suptitle("Three prefix cases select exactly 11 of 16 assignments", fontsize=14, y=0.96)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.06, top=0.84)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white",
                transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
