"""Draw the Oxford 2015 Compilers Q2 activation stack into the current directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 (Debian 3.10.7+dfsg1),
and NumPy 2.3.5, using the dependencies declared in the root pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(9.2, 6.8), dpi=140)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-0.7, 6.4)
    ax.axis("off")
    levels = {"main": 0.35, "p": 1.45, "r": 2.55, "s": 3.65, "q": 4.75}
    details = {"main": "oldest activation", "p": "t = 3, x = 3", "r": "", "s": "", "q": "y = 3; executing now"}
    for name, y in levels.items():
        ax.add_patch(Rectangle((-1.25, y - 0.38), 2.5, 0.76,
                               facecolor="#f0f5fa", edgecolor="#263746", linewidth=1.4))
        ax.text(0, y + (0.13 if details[name] else 0), name,
                ha="center", va="center", fontsize=15, weight="bold")
        if details[name]:
            ax.text(0, y - 0.15, details[name], ha="center", va="center", fontsize=10)
    dynamic = [("q", "s"), ("s", "r"), ("r", "p"), ("p", "main")]
    static = [("q", "p"), ("s", "r"), ("r", "p"), ("p", "main")]
    for source, target in dynamic:
        y1, y2 = levels[source], levels[target]
        route = f"angle,angleA=180,angleB=180,rad=0"
        arrow = FancyArrowPatch((-1.25, y1), (-1.25, y2),
                                connectionstyle="arc3,rad=0.8", arrowstyle="-|>",
                                mutation_scale=14, color="#1763a4", linewidth=1.8)
        ax.add_patch(arrow)
    for source, target in static:
        y1, y2 = levels[source], levels[target]
        rad = -0.82 if source == "q" else -0.62
        ax.add_patch(FancyArrowPatch((1.25, y1), (1.25, y2),
                                    connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                    mutation_scale=14, color="#ae4c20", linewidth=1.8))
    ax.text(-2.8, 5.65, "Dynamic links", color="#1763a4", ha="center", fontsize=14, weight="bold")
    ax.text(-2.8, 5.31, "caller", color="#1763a4", ha="center", fontsize=11)
    ax.text(2.8, 5.65, "Static links", color="#ae4c20", ha="center", fontsize=14, weight="bold")
    ax.text(2.8, 5.31, "lexically enclosing activation", color="#ae4c20", ha="center", fontsize=10)
    ax.text(0, 6.1, "Activation stack while q executes", ha="center", fontsize=16, weight="bold")
    ax.text(-2.75, 2.55, "q → s → r → p → main", rotation=90,
            ha="center", va="center", fontsize=11, color="#1763a4")
    ax.text(3.4, 3.05, "q → p", rotation=90, ha="center", va="center", fontsize=11, color="#ae4c20")
    ax.text(0, -0.38, "main has null caller and enclosing-frame links", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.035, top=0.975)
    fig.savefig(Path.cwd() / "compilers-2015-stack-links.png", facecolor="white",
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
