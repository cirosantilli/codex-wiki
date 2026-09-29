"""Show feasibility, stationarity and slackness for a moving upper bound.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; saves this script's basename.png in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.5), layout="constrained", facecolor="white")
    grid = np.linspace(-0.2, 3.6, 800)
    objective = (grid - 2) ** 2
    cases = [(1.0, "Active: positive multiplier"),
             (2.0, "Active: zero multiplier"),
             (3.0, "Inactive: zero multiplier")]
    for ax, (bound, title) in zip(axes, cases):
        optimum = min(2.0, bound)
        value = (optimum - 2) ** 2
        multiplier = 2 * max(2 - bound, 0)
        assert optimum <= bound
        assert np.isclose(2 * (optimum - 2) + multiplier, 0)
        assert np.isclose(multiplier * (optimum - bound), 0)
        assert multiplier >= 0
        ax.set_facecolor("white")
        ax.axvspan(grid[0], bound, color="#e0f0e8", zorder=0)
        ax.plot(grid, objective, color="#abb4bd", lw=2, ls="--", label="Infeasible part")
        feasible = grid <= bound
        # Include the exact feasible endpoint rather than the closest sample.
        allowed_x = np.r_[grid[feasible], bound]
        ax.plot(allowed_x, (allowed_x - 2) ** 2, color="#246f55", lw=2.7, label="Feasible objective")
        ax.axvline(bound, color="#4b5663", lw=1.4, ls=":")
        ax.scatter([optimum], [value], color="#cb7029", s=65, zorder=5)
        ax.annotate(rf"$x_*={optimum:g},\ f(x_*)={value:g}$", (optimum, value),
                    xytext=(0.16, 2.4), fontsize=11,
                    arrowprops={"arrowstyle": "->", "color": "#a45d29"},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        ax.text(0.04, 0.96, rf"$b={bound:g}$" + "\n" + rf"$\lambda_*={multiplier:g}$",
                transform=ax.transAxes, va="top", color="#246f55", fontsize=12,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2}, zorder=6)
        ax.text(bound, 3.65, r"$x=b$", ha="center", fontsize=10)
        ax.set(xlim=(-0.2, 3.6), ylim=(-0.3, 4.8), xlabel="Decision x", title=title)
        ax.set_xticks([0, 1, 2, 3])
        ax.grid(alpha=0.18)
    axes[0].set_ylabel(r"Objective $f(x)=(x-2)^2$")
    axes[0].legend(loc="upper right", fontsize=9, framealpha=1)
    axes[1].text(0.5, 0.2, "Boundary passes through\nthe unconstrained minimum",
                 transform=axes[1].transAxes, ha="center", fontsize=10)
    axes[2].annotate("Slack = 1", (2.5, 0.2), xytext=(2.5, 0.7), ha="center", fontsize=10)
    axes[2].annotate("", (2, 0.2), (3, 0.2), arrowprops={"arrowstyle": "<->", "color": "#4b5663"})
    fig.suptitle(r"Minimize $(x-2)^2$ subject to $x\leq b$", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
