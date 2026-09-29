"""Hyperbolic function coordinates and sector area; PNG goes to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def main():
    blue, orange, purple = "#176b9c", "#bf5a15", "#74418b"
    t = np.linspace(-1.65, 1.65, 501)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.plot(t, np.cosh(t), color=blue, lw=2.5, label=r"$\cosh t$")
    ax.plot(t, np.sinh(t), color=orange, lw=2.5, label=r"$\sinh t$")
    for value in [-1, 0, 1]:
        ax.axvline(value, color="0.8", ls=":", lw=1)
        ax.scatter([value, value], [np.cosh(value), np.sinh(value)],
                   color=[blue, orange], s=38, zorder=4)
    ax.set(xlim=(-1.7, 1.7), ylim=(-2.8, 2.9), xlabel="Input t",
           ylabel="Function value", title="Two functions of the same input")
    ax.set_xticks([-1, 0, 1])
    ax.legend(loc="lower right", framealpha=1)

    ax = axes[1]
    ax.plot(np.cosh(t), np.sinh(t), color=purple, lw=2.5,
            label=r"$x^2-y^2=1,\ x\geq1$")
    u = np.linspace(0, 1, 250)
    boundary = np.vstack([[0, 0], np.column_stack((np.cosh(u), np.sinh(u))),
                          [0, 0]])
    ax.add_patch(Polygon(boundary, facecolor="#d8c8e4", alpha=.85,
                         edgecolor="none"))
    x1, y1 = np.cosh(1), np.sinh(1)
    ax.plot([0, x1], [0, y1], color=purple, lw=1.3)
    ax.plot([0, 1], [0, 0], color=purple, lw=1.3)
    ax.plot([x1, x1, 0], [0, y1, y1], color="0.4", ls=":", lw=1.2)
    ax.text(.69, .21, r"$A=\frac{1}{2}$", color=purple, fontsize=13)
    for value in [-1, 0, 1]:
        px, py = np.cosh(value), np.sinh(value)
        ax.scatter(px, py, color=purple, s=38, zorder=5)
        offset = (9, 0) if value else (9, -17)
        ax.annotate(f"t = {value}", (px, py), xytext=offset,
                    textcoords="offset points", fontsize=11)
    ax.annotate(r"$\cosh 1\approx1.543$", (x1, 0), xytext=(18, -24),
                textcoords="offset points", fontsize=10, color=blue)
    ax.annotate(r"$\sinh 1\approx1.175$", (0, y1), xytext=(7, 6),
                textcoords="offset points", fontsize=10, color=orange)
    ax.set(xlim=(-.15, 2.85), ylim=(-2.7, 2.7), xlabel="x = cosh t",
           ylabel="y = sinh t", title="Coordinates on the unit hyperbola")
    ax.set_aspect("equal", adjustable="box")
    ax.legend(loc="lower left", fontsize=10, framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.5", lw=.8, zorder=0)
        ax.axvline(0, color="0.5", lw=.8, zorder=0)
        ax.grid(alpha=.16)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Hyperbolic cosine and sine: graphs, coordinates and area",
                 fontsize=15)
    fig.text(.5, .035, "The shaded sector corresponds to t = 1.  "
             "The parameter t is twice its area, rather than the ordinary ray angle.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.07, right=.97, bottom=.17, top=.84, wspace=.3)
    fig.savefig(Path.cwd() / "hyperbolic-functions-and-unit-hyperbola.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
