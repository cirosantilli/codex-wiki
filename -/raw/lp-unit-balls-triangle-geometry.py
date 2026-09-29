"""Draw closed planar Lp unit balls; run from _media with Python 3.14.

Uses matplotlib 3.10.7 and numpy 2.3.5. Writes its basename to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.1), layout="constrained")
    fig.patch.set_facecolor("white")
    theta = np.linspace(0, 2 * np.pi, 1001)
    direction = np.column_stack((np.cos(theta), np.sin(theta)))
    specifications = [
        (1, r"$p=1$: diamond", r"$|x|+|y|\leq 1$", "#007f8b"),
        (2, r"$p=2$: disk", r"$x^2+y^2\leq 1$", "#3758a8"),
        (np.inf, r"$p=\infty$: square", r"$\max(|x|,|y|)\leq 1$", "#a26121"),
    ]
    for ax, (p, title, formula, color) in zip(axes, specifications):
        radius = (
            np.max(np.abs(direction), axis=1)
            if np.isinf(p)
            else np.sum(np.abs(direction) ** p, axis=1) ** (1 / p)
        )
        boundary = direction / radius[:, None]
        ax.set_facecolor("white")
        ax.fill(*boundary.T, color=color, alpha=0.12)
        ax.plot(*boundary.T, color=color, linewidth=2)
        points = np.array([[1.0, 0.0], [0.0, 1.0]])
        if np.isinf(p):
            points = np.array([[1.0, -0.7], [1.0, 0.7]])
        midpoint = points.mean(axis=0)
        ax.plot(*points.T, "o--", color="#3f3f3f", linewidth=1.3, markersize=5)
        ax.plot(*midpoint, "o", color="#c13248", markersize=7)
        label = "midpoint inside" if p == 2 else "midpoint on boundary"
        ax.text(0, -1.48, label, ha="center", color="#a42035", fontsize=11)
        ax.axhline(0, color="#777777", linewidth=0.7)
        ax.axvline(0, color="#777777", linewidth=0.7)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.6, 1.25), aspect="equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_xlabel("x")
        ax.set_ylabel("y", labelpad=0)
        ax.set_title(title + "\n" + formula)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Convex unit balls; flat edges allow distinct unit vectors to share a midpoint", fontsize=13)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
