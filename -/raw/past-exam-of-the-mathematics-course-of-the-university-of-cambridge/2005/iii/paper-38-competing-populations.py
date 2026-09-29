"""Plot the symmetric competition model; write the PNG to the working directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, (time_ax, phase_ax) = plt.subplots(1, 2, figsize=(9, 4.2), layout="constrained")
    times = np.linspace(0, 6, 401)
    for rate, colour in [(0.5, "#2468ad"), (2.0, "#d06b23")]:
        z = rate / (1 + (rate - 1) * np.exp(-rate * times))
        time_ax.plot(times, z, color=colour, lw=2.2, label=rf"$\lambda={rate:g}$")
        time_ax.axhline(rate, color=colour, lw=1, ls=":")
    time_ax.set(xlabel="Time", ylabel=r"Equal populations $x=y=z$", title=r"Diagonal relaxation ($\mu=1$)", ylim=(0.35, 2.15))
    time_ax.legend(frameon=False, loc="center right")
    time_ax.grid(alpha=0.2)

    grid = np.linspace(0.1, 1.9, 13)
    x, y = np.meshgrid(grid, grid)
    u, v = x * (1 - y), y * (1 - x)
    norm = np.hypot(u, v)
    good = norm > 1e-12
    u = np.divide(u, norm, out=np.zeros_like(u), where=good)
    v = np.divide(v, norm, out=np.zeros_like(v), where=good)
    phase_ax.quiver(x, y, u, v, color="#91989f", angles="xy", scale_units="xy", scale=9, width=0.005)
    phase_ax.plot([0, 2], [0, 2], color="#2468ad", lw=2, label="Invariant diagonal")
    phase_ax.scatter([1], [1], s=45, c="#202830", zorder=4)
    phase_ax.annotate("Coexistence saddle", (1, 1), xytext=(0.12, 1.7), arrowprops={"arrowstyle": "->", "color": "#202830"})
    for start, end in [((1.05, 0.95), (1.48, 0.52)), ((0.95, 1.05), (0.52, 1.48))]:
        phase_ax.annotate("", end, xytext=start, arrowprops={"arrowstyle": "->", "color": "#d06b23", "lw": 2})
    phase_ax.set(xlabel=r"Population $x$", ylabel=r"Population $y$", title=r"Difference grows ($\lambda=\mu=1$)", xlim=(0, 2), ylim=(0, 2), aspect="equal")
    phase_ax.legend(frameon=False, loc="lower left")
    fig.savefig(Path.cwd() / "paper-38-competing-populations.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
