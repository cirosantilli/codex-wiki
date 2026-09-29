"""Constrained product maximum; Python 3.14 and repository plotting dependencies.

Run from the intended PNG output directory. This is an original illustration.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    p, q = 3.0, 1.5
    xmax = p ** (1 / p)
    x = np.linspace(0, xmax, 750)
    y = np.maximum(q * (1 - x ** p / p), 0) ** (1 / q)
    fig, ax = plt.subplots(figsize=(7.4, 5.7), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x, y, lw=2.4, color="#245fa0",
            label=r"Constraint $x^3/3+y^{3/2}/(3/2)=1$")
    hx = np.linspace(0.4, 1.65, 500)
    ax.plot(hx, 1 / hx, lw=2, color="#d17b1c", label=r"Product level $xy=1$")
    tx = np.linspace(0.3, 1.65, 200)
    ax.plot(tx, 2 - tx, lw=1.5, ls="--", color="#a43246",
            label=r"Common tangent $x+y=2$")
    ax.scatter([1], [1], s=53, color="black", zorder=4)
    ax.annotate(r"Unique maximum: $(1,1)$", (1, 1), xytext=(1.15, 1.43),
                arrowprops={"arrowstyle": "-", "color": "black"}, fontsize=10)
    ax.annotate("", xy=(1.23, 1.23), xytext=(1.015, 1.015),
                arrowprops={"arrowstyle": "->", "color": "#7046a2", "lw": 1.8})
    ax.text(1.04, 1.26, r"$\nabla f=\nabla g$", color="#7046a2", fontsize=11)
    ax.scatter([0, xmax], [q ** (1 / q), 0], s=27, color="#245fa0", zorder=4)
    ax.set(xlim=(0, 1.7), ylim=(0, 1.95), xlabel="$x$", ylabel="$y$")
    ax.set_title("Young's inequality: a sharp constrained maximum", fontsize=13)
    ax.legend(loc="lower left", fontsize=9, framealpha=0.96)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.13)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2015-young-inequality-constraint.png", dpi=140,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
