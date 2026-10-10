"""Draw finite modulo-three classes; run from _media with Python 3.14.

Uses the repository's matplotlib dependency and writes a PNG to the cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    colors = ["#0072B2", "#B45400", "#007D64"]
    fig, ax = plt.subplots(figsize=(8, 3.9), dpi=130, facecolor="white")
    ax.set(xlim=(-0.8, 8.8), ylim=(-2.35, 1.55))
    ax.axis("off")
    ax.text(4, 1.22, "Same remainder, same equivalence class", ha="center",
            fontsize=17, weight="bold")
    ax.text(4, 0.78, r"$X=\{0,1,\ldots,8\},\quad x\sim y\Longleftrightarrow 3\mid(x-y)$",
            ha="center", fontsize=14)
    ax.annotate("", xy=(8.65, 0), xytext=(-0.6, 0),
                arrowprops={"arrowstyle": "->", "color": "#666666", "lw": 1.6})
    for n in range(9):
        ax.scatter(n, 0, s=190, color=colors[n % 3], edgecolor="white",
                   linewidth=1.4, zorder=3)
        ax.text(n, -0.38, str(n), ha="center", fontsize=14)
    for r, x in enumerate((0.8, 4, 7.2)):
        ax.add_patch(FancyBboxPatch((x-1.35, -1.62), 2.7, 0.74,
                     boxstyle="round,pad=0.08", edgecolor=colors[r],
                     facecolor="white", linewidth=2))
        ax.text(x, -1.10, f"[{r}] = [{r+3}] = [{r+6}]", ha="center",
                fontsize=13, color=colors[r], weight="bold")
        ax.text(x, -1.44, "{" + ", ".join(str(n) for n in range(r, 9, 3)) + "}",
                ha="center", fontsize=14)
    ax.text(4, -2.05, "Three disjoint classes cover X; each number appears once.",
            ha="center", fontsize=12, color="#333333")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.02)
    fig.savefig(Path("equivalence-classes-modulo-three.png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
