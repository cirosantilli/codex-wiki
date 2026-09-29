"""Original beta-plane vorticity-tendency schematic; Python 3.14, matplotlib 3.10."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 0), 0.55, color="#d4e8fa", ec="#28639a", lw=2))
    ax.text(0, 0, "Initial cyclone\npositive vorticity", ha="center", va="center", fontsize=12)
    ax.add_patch(Arc((0, 0), 1.65, 1.65, theta1=25, theta2=315, color="#28639a", lw=2))
    ax.add_patch(FancyArrowPatch((0.67, -0.50), (0.80, -0.17), arrowstyle="-|>", mutation_scale=17, color="#28639a", lw=2))
    for x, label, color in [(-1.5, "+", "#28639a"), (1.5, "−", "#b24632")]:
        ax.add_patch(Circle((x, 0), 0.30, facecolor="white", edgecolor=color, lw=2))
        ax.text(x, 0, label, ha="center", va="center", fontsize=29, color=color)
    ax.annotate("Southward flow\n$\\Delta f<0$; $\\Delta\\xi>0$", xy=(-0.8, 0), xytext=(-2.15, -1), ha="center", fontsize=12, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("Northward flow\n$\\Delta f>0$; $\\Delta\\xi<0$", xy=(0.8, 0), xytext=(2.15, -1), ha="center", fontsize=12, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("Pattern shifts west", xy=(-1.6, 1.2), xytext=(0.5, 1.2), va="center", fontsize=13, arrowprops={"arrowstyle": "-|>", "lw": 2})
    ax.annotate("North\n$f$ increases", xy=(2.7, 1.4), xytext=(2.7, 0.4), ha="center", fontsize=11, arrowprops={"arrowstyle": "->"})
    ax.text(0, -1.6, "$D(\\xi+f)/Dt=0$  implies  $D\\xi/Dt=-\\beta v$", ha="center", fontsize=14)
    ax.set(xlim=(-3.2, 3.2), ylim=(-1.85, 1.7), aspect="equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
