"""Compare strict Minkowski, equality, and failure below exponent one.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the CWD with this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, step, color, label, offset):
    end = start + step
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
    ax.text(*(start + 0.53 * step + offset), label, color=color, fontsize=12)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.8))
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.22, top=0.76, wspace=0.39)
    fig.patch.set_facecolor("white")
    specifications = [
        (2, np.array([1.0, 0.0]), np.array([0.0, 1.0]), "Strict inequality", r"$\sqrt{2}<1+1$", 1.3),
        (2, np.array([1.0, 1.0]), np.array([2.0, 2.0]), "Positive multiples: equality", r"$3\sqrt{2}=\sqrt{2}+2\sqrt{2}$", 3.5),
        (0.5, np.array([1.0, 0.0]), np.array([0.0, 1.0]), "Triangle inequality fails", r"$4>1+1$", 1.3),
    ]
    theta = np.linspace(0, 2 * np.pi, 1501)
    direction = np.column_stack((np.cos(theta), np.sin(theta)))
    for ax, (p, u, v, title, formula, upper) in zip(axes, specifications):
        ax.set_facecolor("white")
        radius = np.sum(np.abs(direction) ** p, axis=1) ** (1 / p)
        boundary = direction / radius[:, None]
        ax.fill(*boundary.T, color="#3758a8", alpha=0.09)
        ax.plot(*boundary.T, color="#3758a8", linewidth=1.2)
        origin = np.zeros(2)
        if title.startswith("Positive"):
            # Offset labels keep them clear of the collinear arrows.
            arrow(ax, origin, u, "#007f8b", r"$u$", np.array([-0.35, 0.0]))
            arrow(ax, u, v, "#a26121", r"$v$", np.array([-0.35, 0.0]))
            ax.plot([0, 3], [0, 3], color="#c13248", linewidth=1.2, linestyle="--")
            ax.text(2.55, 2.15, r"$u+v$", color="#c13248")
        else:
            arrow(ax, origin, u, "#007f8b", r"$u$", np.array([0.0, -0.16]))
            arrow(ax, u, v, "#a26121", r"$v$", np.array([0.06, 0.0]))
            arrow(ax, origin, u + v, "#c13248", r"$u+v$", np.array([-0.28, 0.07]))
        ax.plot(*(u + v), "o", color="#c13248", markersize=4)
        ax.axhline(0, color="#777777", linewidth=0.7)
        ax.axvline(0, color="#777777", linewidth=0.7)
        ax.set(xlim=(-1.15, upper), ylim=(-1.15, upper), aspect="equal")
        ticks = [0, 1, 2, 3] if upper > 2 else [0, 0.5, 1]
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_xlabel("x")
        ax.set_ylabel("y", labelpad=0)
        panel_title = "Positive multiples" if title.startswith("Positive") else title
        subtitle = r"$p=1/2$: quasi-norm" if p == 0.5 else r"$p=2$"
        ax.set_title(panel_title + "\n" + subtitle, fontsize=13)
        bbox = ax.get_position()
        fig.text((bbox.x0 + bbox.x1) / 2, 0.04, formula, ha="center", fontsize=14)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Vector addition compared with the sizes of its two steps", fontsize=14, y=0.98)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
