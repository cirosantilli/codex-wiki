"""Toy replicator coexistence figure; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../replicator-coexistence.py
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
        return x * (1 - x) * (3 - 4 * x)
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
    fig.suptitle("Coexistence: both rare types have an advantage", fontsize=16, y=0.97)
    x = np.linspace(0, 1, 501)
    payoff.plot(x, 3 - 2 * x, color="#2364a0", lw=2.5, label=r"$f_1=3-2x$")
    payoff.plot(x, 2 * x, color="#be571c", lw=2.5, label=r"$f_2=2x$")
    payoff.axvline(0.75, color="#777777", ls="--", lw=1)
    payoff.scatter([0.75], [1.5], color="#333333", zorder=5)
    payoff.text(0.46, 1.32, r"$x_*=3/4$", fontsize=12)
    payoff.set(xlim=(-0.04, 1.04), ylim=(-0.68, 3.2), xlabel="Frequency x of type 1",
               ylabel="Expected payoff", title=r"Toy payoff table: $A=[(1,3),(2,0)]$")
    payoff.axhline(-0.35, color="#444444", lw=1)
    payoff.annotate("", xy=(0.67, -0.35), xytext=(0.14, -0.35),
                    arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 2})
    payoff.annotate("", xy=(0.80, -0.35), xytext=(0.97, -0.35),
                    arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 2})
    payoff.scatter([0.75], [-0.35], color="#333333", zorder=5)
    payoff.scatter([0, 1], [-0.35, -0.35], facecolors="white", edgecolors="#333333", zorder=5)
    payoff.legend(loc="upper center", frameon=False)
    times = np.linspace(0, 10, 4001)
    for x0 in [0.04, 0.2, 0.5, 0.7, 0.85, 0.97]:
        color = "#2364a0" if x0 < 0.75 else "#be571c"
        paths.plot(times, trajectory(x0, times), color=color, lw=1.8)
    paths.axhline(0.75, color="#333333", ls="--", lw=1.4)
    paths.plot(times, np.zeros_like(times), color="#999999", lw=1, ls=":")
    paths.plot(times, np.ones_like(times), color="#999999", lw=1, ls=":")
    paths.text(5, 0.60, "Interior states approach\nx = 3/4", ha="center", fontsize=10)
    paths.text(5, 0.045, "Absent types stay absent\nat x = 0 or 1", ha="center", color="#666666", fontsize=10)
    paths.set(xlim=(0, 10), ylim=(-0.04, 1.04), xlabel="Time (model units)",
              ylabel="Frequency x", title=r"$\dot{x}=x(1-x)(3-4x)$")
    paths.grid(alpha=0.16)
    fig.text(0.5, 0.02, "Toy model, not measured data. Phase line: filled = attracting; open = repelling.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.18, top=0.79, wspace=0.3)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
