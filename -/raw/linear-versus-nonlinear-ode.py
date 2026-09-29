"""Show why the sum of two solutions to y'=y^2 is not a solution.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; writes linear-versus-nonlinear-ode.png.
Exact curves are restricted to 0 <= t <= 0.4, before blowup at 1 and 1/2.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0.0, 0.4, 401)
    y1, y2 = 1 / (1 - t), 2 / (1 - 2 * t)
    defect = -2 * y1 * y2
    blue, orange, red = "#2166ac", "#c36b13", "#b2182b"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9), dpi=120,
                             constrained_layout=True, facecolor="white")
    ax = axes[0]
    ax.plot(t, y1, color=blue, lw=2.6, label=r"$y_1=1/(1-t)$: solution")
    ax.plot(t, y2, color=orange, lw=2.6, label=r"$y_2=2/(1-2t)$: solution")
    ax.plot(t, y1 + y2, color=red, lw=2.6, ls="--",
            label=r"$s=y_1+y_2$: fails the equation")
    ax.scatter([0.25] * 3, [4 / 3, 4, 16 / 3],
               color=[blue, orange, red], s=30, zorder=4)
    ax.axvline(0.25, color="#777777", lw=1, ls=":", zorder=0)
    ax.set(title=r"Nonlinear: $y'=y^2$", ylabel="y (dimensionless)",
           ylim=(0, 12.2))
    ax.legend(loc="upper left", fontsize=9.8, framealpha=1)
    ax.text(0.018, 6.6, "At t = 0: s = 3\nactual slope = 5\nrequired slope = 9",
            fontsize=10, va="center", bbox={"facecolor": "white",
                                           "edgecolor": "none", "alpha": 0.95})
    ax = axes[1]
    ax.axhline(0, color="#258568", lw=2, ls=":",
               label="zero defect required for a solution")
    ax.plot(t, defect, color=red, lw=2.7,
            label=r"$s'-s^2=-2y_1y_2$")
    ax.fill_between(t, defect, 0, color=red, alpha=0.08)
    ax.scatter([0, 0.25], [-4, -32 / 3], color=red, s=35, zorder=4)
    ax.annotate(r"$t=1/4$: defect $=-32/3$", xy=(0.25, -32 / 3),
                xytext=(0.055, -22.5), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(title="A sum introduces a cross term",
           ylabel=r"equation defect $s'-s^2$", ylim=(-35.5, 5))
    ax.legend(loc="lower left", fontsize=9.8, framealpha=1)
    ax.text(0.02, 2.0, "homogeneous linear sums have zero defect",
            fontsize=9, color="#196649")
    for ax in axes:
        ax.set(xlabel="t (dimensionless)", xlim=(-0.006, 0.4))
        ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4])
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / "linear-versus-nonlinear-ode.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
