"""Normalize the exact vector (3,4) and show opposite unit directions."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, end, color, width=2.7):
    ax.annotate("", xy=end, xytext=(0, 0),
                arrowprops={"arrowstyle": "-|>", "mutation_scale": 18,
                            "lw": width, "color": color, "shrinkA": 0, "shrinkB": 0})


def main():
    vector = np.array([3., 4.]); unit = vector / np.linalg.norm(vector)
    green, blue, purple = "#268153", "#2878a3", "#80558d"
    theta = np.linspace(0, 2 * np.pi, 400)
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 6.3), dpi=100, facecolor="white")
    for ax in axes:
        ax.set_facecolor("white"); ax.set_aspect("equal", adjustable="box")
        ax.axhline(0, color="#a9b1b7", lw=.8); ax.axvline(0, color="#a9b1b7", lw=.8)
        ax.plot(np.cos(theta), np.sin(theta), color="#c39437", lw=1.6)
        ax.grid(alpha=.18); ax.set(xlabel="x", ylabel="y")
    ax = axes[0]
    arrow(ax, vector, green); arrow(ax, unit, blue, 3.2)
    ax.scatter(*vector, c=green, s=40, zorder=5); ax.scatter(*unit, c=blue, s=40, zorder=5)
    ax.annotate(r"$\mathbf{v}=(3,4)$" + "\nMagnitude 5", vector, xytext=(-63, 12), textcoords="offset points", fontsize=12)
    ax.annotate(r"$\widehat{\mathbf{v}}=(3/5,4/5)$", unit, xytext=(33, -17), textcoords="offset points", fontsize=12,
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(xlim=(-1.2, 4.1), ylim=(-1.2, 5.1), title="Same direction, different magnitude")
    ax.set_xticks([-1, 0, 1, 2, 3, 4]); ax.set_yticks([-1, 0, 1, 2, 3, 4, 5])
    ax = axes[1]
    arrow(ax, unit, blue); arrow(ax, -unit, purple)
    ax.plot([unit[0], unit[0]], [0, unit[1]], ls="--", color=blue, lw=1.1)
    ax.plot([0, unit[0]], [unit[1], unit[1]], ls="--", color=blue, lw=1.1)
    ax.scatter(*unit, c=blue, s=40, zorder=5); ax.scatter(*-unit, c=purple, s=40, zorder=5)
    ax.annotate("(3/5, 4/5)", unit, xytext=(-58, 12), textcoords="offset points", fontsize=12, color=blue)
    ax.annotate("(−3/5, −4/5)", -unit, xytext=(-17, -23), textcoords="offset points", fontsize=12, color=purple)
    ax.text(0, 1.18, r"$(3/5)^2+(4/5)^2=1$", ha="center", fontsize=12)
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.4, 1.4), title="Unit directions on the unit circle")
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
    fig.suptitle("Vector normalization separates magnitude from direction", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, .93))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
