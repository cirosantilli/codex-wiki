"""Logistic orbits, cobwebs and bifurcation diagram.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes logistic-map-dynamics.png to the caller's working directory.
Uses only the dependencies in the repository's pyproject.toml.
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def orbit(r, initial, steps):
    values = np.empty(steps + 1)
    values[0] = initial
    for n in range(steps):
        values[n + 1] = r * values[n] * (1 - values[n])
    return values


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(12, 10), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(3, 3, height_ratios=(0.85, 1.35, 1.3))
    colors = ("#2166ac", "#b35806", "#387a48")
    parameters = (2.8, 3.2, 3.5)
    periods = (1, 2, 4)
    curve = np.linspace(0, 1, 500)
    for col, (r, period, color) in enumerate(zip(parameters, periods, colors)):
        values = orbit(r, 0.2, 50)
        ax = fig.add_subplot(grid[0, col])
        ax.plot(np.arange(51), values, ".-", color=color, lw=1, ms=4)
        ax.set(xlim=(0, 50), ylim=(0, 1), xlabel="Iteration n", ylabel=r"State $x_n$")
        description = "fixed point" if period == 1 else f"period-{period} cycle"
        ax.set_title(f"r = {r}: attracting {description}")
        ax.grid(alpha=0.18)

        ax = fig.add_subplot(grid[1, col])
        ax.plot(curve, r * curve * (1 - curve), color="#333333", lw=1.8,
                label=r"$y=r x(1-x)$")
        ax.plot(curve, curve, color="#888888", ls="--", lw=1, label="y = x")
        web = orbit(r, 0.2, 22)
        px, py = [web[0]], [0.0]
        for n in range(len(web) - 1):
            px.extend((web[n], web[n + 1]))
            py.extend((web[n + 1], web[n + 1]))
        ax.plot(px, py, color=color, lw=1.2, alpha=0.85)
        ax.annotate("", xy=(web[0], web[1]), xytext=(web[0], 0.08),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.5})
        ax.annotate("", xy=(web[1], web[1]), xytext=(web[0] + 0.04, web[1]),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.5})
        fixed = 1 - 1 / r
        ax.scatter([fixed], [fixed], s=42, edgecolors="#9e2929",
                   facecolors="#9e2929" if period == 1 else "white", zorder=5)
        if period > 1:
            cycle = orbit(r, 0.2, 800)[-period:]
            ax.scatter(cycle, r * cycle * (1 - cycle), s=30, color=color, zorder=4)
        ax.set(xlim=(0, 1), ylim=(0, 1), xlabel=r"Current state $x_n$",
               ylabel=r"Next state $x_{n+1}$", title="Vertical to curve; horizontal to diagonal")
        ax.set_aspect("equal", adjustable="box")
        ax.grid(alpha=0.12)
        if col == 0:
            ax.legend(loc="upper left", fontsize=9, framealpha=0.95)

    ax = fig.add_subplot(grid[2, :])
    # One initial state per parameter, with a long discarded transient.
    # Avoid r=4 at the endpoint: finite precision there can have exceptional cycles.
    r_grid = np.linspace(2.5, 4, 2800, endpoint=False)
    state = np.full_like(r_grid, 0.2)
    for _ in range(2000):
        state = r_grid * state * (1 - state)
    retained = np.empty((240, len(r_grid)))
    for n in range(len(retained)):
        state = r_grid * state * (1 - state)
        retained[n] = state
    ax.scatter(np.tile(r_grid, len(retained)), retained.ravel(),
               s=0.09, color="#202e48", alpha=0.35, linewidths=0)
    for threshold, label in ((3, "first doubling"), (1 + np.sqrt(6), "second doubling")):
        ax.axvline(threshold, color="#9e2929", ls="--", lw=0.9)
        ax.text(threshold + 0.012, 1.015, label, fontsize=10, color="#9e2929")
    ax.axvspan(3.8285, 3.8414, color="#e3b342", alpha=0.3)
    ax.annotate("period-3 window", xy=(3.835, 0.15), xytext=(3.58, 0.04),
                arrowprops={"arrowstyle": "->", "color": "#8e650c"},
                color="#8e650c", fontsize=11)
    ax.set(xlim=(2.5, 4), ylim=(0, 1.08), yticks=(0, 0.25, 0.5, 0.75, 1),
           xlabel="Parameter r", ylabel=r"Retained states $x_n$",
           title="Bifurcation diagram: 240 iterates after discarding 2,000; periodic windows remain")
    fig.savefig(Path.cwd() / "logistic-map-dynamics.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
