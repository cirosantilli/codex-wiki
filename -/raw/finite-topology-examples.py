"""Original finite-topology diagram; run from _media to save the PNG to cwd.

Tested with Python 3.14 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    blue, orange = "#186aa6", "#bd4a18"
    fig, ax = plt.subplots(figsize=(9.6, 4.6), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.04, top=0.93)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    ax.text(5, 4.85, "Same set, different open sets", ha="center", fontsize=18)
    for xpos, title, color in [(2.1, "Discrete topology", blue),
                               (7.9, "Indiscrete topology", orange)]:
        box = FancyBboxPatch((xpos-1.85, 2.55), 3.7, 1.85,
                             boxstyle="round,pad=0.08", facecolor="#f7f9fb",
                             edgecolor=color, lw=1.6)
        ax.add_patch(box)
        ax.text(xpos, 4.03, title, ha="center", fontsize=15, color=color)
        ax.scatter([xpos-0.55, xpos+0.55], [3.55, 3.55], s=110, color=color)
        ax.text(xpos-0.55, 3.21, "a", ha="center", fontsize=13)
        ax.text(xpos+0.55, 3.21, "b", ha="center", fontsize=13)
    ax.text(2.1, 2.77, r"Open sets: $\varnothing,\{a\},\{b\},\{a,b\}$",
            ha="center", fontsize=12)
    ax.text(7.9, 2.77, r"Open sets: $\varnothing,\{a,b\}$",
            ha="center", fontsize=12)
    ax.annotate("", xy=(7.9, 2.06), xytext=(2.1, 2.06),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 2.2})
    ax.text(5, 2.23, "Identity map: continuous", ha="center", fontsize=14, color=blue)
    ax.text(5, 1.73, "Every target open set has an open inverse image.",
            ha="center", fontsize=12)
    ax.annotate("", xy=(2.1, 1.06), xytext=(7.9, 1.06),
                arrowprops={"arrowstyle": "->", "color": orange, "lw": 2.2})
    ax.text(5, 1.23, "Inverse identity map: not continuous", ha="center",
            fontsize=14, color=orange)
    ax.text(5, 0.73, r"$\{a\}$ is open in the target, but its inverse image $\{a\}$ is not open.",
            ha="center", fontsize=12)
    ax.text(5, 0.16, "A continuous bijection can fail to be a homeomorphism.",
            ha="center", fontsize=13, weight="bold")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
