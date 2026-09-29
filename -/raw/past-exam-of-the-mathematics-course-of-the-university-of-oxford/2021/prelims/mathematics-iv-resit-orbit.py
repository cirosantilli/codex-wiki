"""Oxford Prelims IV resit 2021, Q4: run in the desired output directory.

Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def point(theta):
    radius = 1 / (2 * np.log(np.sqrt(np.e) + theta / 2))
    return radius * np.cos(theta), radius * np.sin(theta)


def main():
    fig, ax = plt.subplots(figsize=(6.4, 5.4), facecolor="white")
    theta = np.linspace(0, 12 * np.pi, 6000)
    ax.plot(*point(theta), color="#17658a", lw=1.8)
    for angle in [0.4, 1.8, 4.2, 7.9, 13.2, 20.0, 29.2]:
        ax.annotate("", xy=point(angle + 0.16), xytext=point(angle),
                    arrowprops={"arrowstyle": "->", "color": "#b04430", "lw": 1.8})
    ax.scatter([1, 0], [0, 0], color=["#b04430", "#222222"], s=[28, 16], zorder=5)
    ax.annotate(r"Start: $r=1,\ \theta=0$", (1, 0), (0.53, -0.33),
                arrowprops={"arrowstyle": "-", "color": "#555555"}, fontsize=10)
    ax.annotate(r"$r\to0$ as $\theta\to\infty$", (0.02, 0.02), (-0.63, -0.68),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.axhline(0, color="#cccccc", lw=0.8, zorder=0)
    ax.axvline(0, color="#cccccc", lw=0.8, zorder=0)
    ax.set(xlim=(-0.78, 1.12), ylim=(-0.78, 0.78), xlabel="$x$", ylabel="$y$",
           title="Counterclockwise motion along an inward spiral")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
