"""Draw quotient fibers; run from _media with Python 3.14.

Uses the repository's matplotlib dependency and writes a PNG to the cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    colors = ["#0072B2", "#B45400", "#007D64"]
    fig, ax = plt.subplots(figsize=(8, 4.7), dpi=130, facecolor="white")
    ax.set(xlim=(-0.4, 8.7), ylim=(-0.6, 9.5))
    ax.axis("off")
    ax.text(4.15, 9.02, r"The quotient map $q(x)=[x]$", ha="center",
            fontsize=18, weight="bold")
    ax.text(1.6, 8.15, "X: nine elements", ha="center", fontsize=14)
    ax.text(6.6, 8.15, r"$X/{\sim}$: three classes", ha="center", fontsize=14)
    for r, y in enumerate((6.55, 3.95, 1.35)):
        color = colors[r]
        ax.add_patch(FancyBboxPatch((0.35, y-0.95), 2.65, 1.9,
                     boxstyle="round,pad=0.10", edgecolor=color,
                     facecolor="white", linewidth=1.6, linestyle="--"))
        ax.add_patch(FancyBboxPatch((5.45, y-0.65), 2.6, 1.3,
                     boxstyle="round,pad=0.12", edgecolor=color,
                     facecolor="white", linewidth=2.4, zorder=3))
        for j, n in enumerate(range(r, 9, 3)):
            start_y = y + (1-j)*0.59
            ax.annotate("", xy=(5.3, y), xytext=(2.75, start_y),
                        arrowprops={"arrowstyle": "->", "color": color,
                                    "lw": 1.5, "mutation_scale": 14}, zorder=2)
            ax.scatter(2.5, start_y, s=430, color=color, zorder=4)
            ax.text(2.5, start_y, str(n), ha="center", va="center",
                    fontsize=13, color="white", weight="bold", zorder=5)
        ax.text(0.6, y, f"fiber\nof [{r}]", ha="left", va="center",
                fontsize=12, color=color)
        ax.text(6.75, y+0.26, f"[{r}]", ha="center", va="center",
                fontsize=16, color=color, weight="bold", zorder=4)
        ax.text(6.75, y-0.26, "{" + ", ".join(str(n) for n in range(r, 9, 3)) + "}",
                ha="center", va="center", fontsize=14, zorder=4)
    ax.text(4.2, -0.30, "Each box on the right is one quotient element: an entire set.",
            ha="center", fontsize=12, color="#333333")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.02)
    fig.savefig(Path("quotient-map-collapsing-classes.png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
