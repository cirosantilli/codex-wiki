"""Draw the left-multiplication convention; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7, 4.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    angles = np.linspace(0, 2 * np.pi, 400)
    ax.plot(5 * np.cos(angles), 5 * np.sin(angles), color="#b8c5d1", lw=1.4)
    ax.axhline(0, color="#687582", lw=0.9)
    ax.axvline(0, color="#687582", lw=0.9)
    for endpoint, color in [((3, 4), "#205ea8"), ((5, 0), "#b44822")]:
        ax.annotate("", xy=endpoint, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.6})
        ax.plot(*endpoint, "o", color=color, ms=5)
    ax.plot([3, 3, 0], [0, 4, 4], "--", color="#7799bb", lw=1)
    theta = np.arctan2(4, 3)
    arc = np.linspace(theta, 0, 100)
    ax.plot(2.4 * np.cos(arc), 2.4 * np.sin(arc), color="#744c97", lw=2)
    ax.add_patch(FancyArrowPatch(
        (2.4 * np.cos(0.12), 2.4 * np.sin(0.12)), (2.4, 0),
        arrowstyle="-|>", mutation_scale=14, color="#744c97", lw=2))
    ax.text(3.15, 4.05, r"$(3,4)^T$", color="#205ea8", fontsize=13)
    ax.text(4.3, -0.65, r"$(5,0)^T$", color="#b44822", fontsize=13)
    ax.text(2.5, 1.45, r"$-\theta$", color="#744c97", fontsize=14)
    ax.text(-4.8, 3.8, r"$c=3/5,\quad s=4/5$", fontsize=12)
    ax.text(-4.8, 2.85, r"$\theta=\arctan(4/3)$", fontsize=12)
    ax.text(-4.8, 1.9, "Clockwise rotation", fontsize=11, color="#744c97")
    ax.text(-4.8, -3.5, r"$\|Gx\|_2=\|x\|_2=5$", fontsize=14)
    ax.set(xlim=(-5.8, 6.2), ylim=(-5.5, 5.6), aspect="equal")
    ax.set_xticks([-5, 0, 3, 5])
    ax.set_yticks([-5, 0, 4, 5])
    ax.set_xlabel("First coordinate", fontsize=11)
    ax.set_ylabel("Second coordinate", fontsize=11)
    ax.set_title("Givens rotation: eliminate a component, preserve length", fontsize=13, pad=12)
    ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
