"""Toy replicator coordination figure; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../replicator-coordination.py
The matching PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def trajectory(x0, times):
    """Fourth-order Runge–Kutta integration of the stated scalar model."""
    values = np.empty_like(times)
    values[0] = x0
    def rhs(x):
        return x * (1 - x) * (5 * x - 2)
    for k, dt in enumerate(np.diff(times)):
        x = values[k]
        a = rhs(x)
        b = rhs(x + dt * a / 2)
        c = rhs(x + dt * b / 2)
        d = rhs(x + dt * c)
        values[k + 1] = x + dt * (a + 2 * b + 2 * c + d) / 6
    return values


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (payoff, paths) = plt.subplots(1, 2, figsize=(9.4, 4.4))
    fig.suptitle("Coordination: a threshold separates two outcomes", fontsize=16, y=0.97)
    x = np.linspace(0, 1, 501)
    payoff.plot(x, 3 * x, color="#2364a0", lw=2.5, label=r"$f_1=3x$")
    payoff.plot(x, 2 * (1 - x), color="#be571c", lw=2.5, label=r"$f_2=2(1-x)$")
    payoff.axvline(0.4, color="#777777", ls="--", lw=1)
    payoff.scatter([0.4], [1.2], color="#333333", zorder=5)
    payoff.text(0.43, 1.35, r"$x_*=2/5$", fontsize=12)
    payoff.set(xlim=(-0.04, 1.04), ylim=(-0.68, 3.2), xlabel="Frequency x of convention 1",
               ylabel="Expected payoff", title=r"Toy payoff table: $A=[(3,0),(0,2)]$")
    payoff.axhline(-0.35, color="#444444", lw=1)
    payoff.annotate("", xy=(0.07, -0.35), xytext=(0.31, -0.35),
                    arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 2})
    payoff.annotate("", xy=(0.91, -0.35), xytext=(0.54, -0.35),
                    arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 2})
    payoff.scatter([0, 1], [-0.35, -0.35], color="#333333", zorder=5)
    payoff.scatter([0.4], [-0.35], facecolors="white", edgecolors="#333333", zorder=5)
    payoff.legend(loc="upper center", frameon=False)
    times = np.linspace(0, 5, 2001)
    for x0 in [0.08, 0.25, 0.38, 0.42, 0.65, 0.92]:
        color = "#be571c" if x0 < 0.4 else "#2364a0"
        paths.plot(times, trajectory(x0, times), color=color, lw=1.8)
    paths.axhline(0.4, color="#777777", ls="--", lw=1.4)
    paths.text(1.85, 0.43, "Exactly at 2/5: stationary", color="#555555", fontsize=10)
    paths.text(2.35, 0.91, "Above 2/5: to x = 1", color="#2364a0", fontsize=10)
    paths.text(2.35, 0.09, "Below 2/5: to x = 0", color="#be571c", fontsize=10)
    paths.set(xlim=(0, 5), ylim=(-0.04, 1.04), xlabel="Time (model units)",
              ylabel="Frequency x", title=r"$\dot{x}=x(1-x)(5x-2)$")
    paths.grid(alpha=0.16)
    fig.text(0.5, 0.02, "Toy model, not measured data. Phase line: filled = attracting; open = repelling.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.18, top=0.79, wspace=0.3)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
