"""Draw open-chain sugar configurations; write basename.png in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Condensed end groups and Fischer crosses encode connectivity/configuration,
not bond lengths or the predominant species in aqueous solution.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def draw_sugar(ax, x, right_groups, color):
    ax.plot([x, x], [1.2, 4.9], color="#333333", lw=1.8)
    ax.text(x, 5.05, "CHO", ha="center", va="center", fontsize=19,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.text(x, 1.05, r"CH$_2$OH", ha="center", va="center", fontsize=19,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for number, (y, right) in enumerate(zip((4, 3, 2), right_groups), 2):
        ax.plot([x - 0.67, x + 0.67], [y, y], color="#333333", lw=1.8)
        ax.text(x - 0.9, y, "H", ha="center", va="center", fontsize=18)
        ax.text(x + 0.95, y, right, ha="center", va="center", fontsize=18,
                color=color if right == "OH" else "#333333")
        ax.text(x - 0.23, y + 0.19, f"C{number}", ha="right",
                fontsize=10, color="#666666")
    ax.text(x - 0.82, 5.05, "C1", ha="right", va="center", fontsize=10,
            color="#666666")
    ax.text(x - 0.82, 1.05, "C5", ha="right", va="center", fontsize=10,
            color="#666666")


def main():
    fig, ax = plt.subplots(figsize=(8.8, 6.6))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.23, top=0.89)
    ax.set(xlim=(0, 8.8), ylim=(0.4, 6.3))
    ax.axis("off")
    draw_sugar(ax, 2.0, ("OH", "OH", "OH"), "#216c96")
    draw_sugar(ax, 6.5, ("H", "OH", "OH"), "#216c96")
    ax.text(2.0, 6.0, "D-ribose", ha="center", fontsize=17, weight="bold")
    ax.text(6.5, 6.0, "2-deoxy-D-ribose", ha="center", fontsize=17, weight="bold")
    ax.text(2.0, 5.55, r"C$_5$H$_{10}$O$_5$", ha="center", fontsize=14)
    ax.text(6.5, 5.55, r"C$_5$H$_{10}$O$_4$", ha="center", fontsize=14)
    ax.add_patch(FancyBboxPatch((5.3, 3.65), 2.5, 0.7,
                              boxstyle="round,pad=0.03", facecolor="#fff0d9",
                              edgecolor="#bb6c16", lw=1.2, zorder=0))
    ax.annotate("OH → H\nat C2", xy=(5.2, 4), xytext=(4.35, 4),
                ha="center", va="center", fontsize=12, color="#985611",
                arrowprops={"arrowstyle": "->", "color": "#985611"})
    fig.suptitle("Open-chain Fischer projections", fontsize=18, y=0.97)
    fig.text(0.5, 0.18, "C2 in deoxyribose has two H groups: it is not a stereocenter.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.12, "Horizontal bonds: toward viewer.  Vertical bonds: away from viewer.",
             ha="center", fontsize=11, color="#444444")
    fig.text(0.5, 0.06, "Reference configurations; open-chain ribose is a minor form in water.",
             ha="center", fontsize=11, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}")


if __name__ == "__main__":
    main()
