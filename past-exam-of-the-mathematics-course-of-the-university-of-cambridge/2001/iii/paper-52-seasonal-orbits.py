"""Illustrate two annual population maps; write the PNG into the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def seasonal_step(x, y, r, survival, attack, birth):
    next_x = r * x * np.exp(-attack * y)
    return next_x, survival * y * (1 + birth * next_x)


def nicholson_bailey_step(x, y, r, attack, conversion):
    surviving_fraction = np.exp(-attack * y)
    return r * x * surviving_fraction, conversion * x * (1 - surviving_fraction)


def trajectory(step, initial, steps):
    points = [initial]
    for _ in range(steps):
        points.append(step(*points[-1]))
    return np.asarray(points)


def main():
    r, survival, attack, birth = np.exp(0.8), 0.5, 0.02, 0.01
    x_star = (1 - survival) / (survival * birth)
    y_star = np.log(r) / attack
    scale = np.array([x_star, y_star])
    conversion = y_star / (x_star * (1 - 1 / r))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.8), dpi=100, layout="constrained")
    seasonal = lambda x, y: seasonal_step(x, y, r, survival, attack, birth)
    for offset, color in zip((0.025, 0.055, 0.09, 0.14), ("#0072b2", "#009e73", "#d55e00", "#cc79a7")):
        orbit = trajectory(seasonal, (x_star * (1 + offset), y_star), 1200) / scale
        axes[0].scatter(orbit[:, 0], orbit[:, 1], s=5, color=color, alpha=0.7)
        axes[0].plot(*orbit[0], marker=">", color=color, markersize=7)
    axes[0].set(title="Pulse breeding: neutral annual samples", xlim=(0.76, 1.25), ylim=(0.76, 1.25))
    axes[0].text(0.04, 0.95, "No attracting oscillation amplitude", transform=axes[0].transAxes, va="top")
    nb = lambda x, y: nicholson_bailey_step(x, y, r, attack, conversion)
    orbit = trajectory(nb, (1.01 * x_star, y_star), 24) / scale
    axes[1].plot(orbit[:, 0], orbit[:, 1], "o-", color="#0072b2", markersize=3, linewidth=1.3)
    for n in (6, 13, 20):
        axes[1].annotate("", xy=orbit[n + 1], xytext=orbit[n], arrowprops={"arrowstyle": "->", "color": "#d55e00", "lw": 1.8})
    axes[1].plot(*orbit[0], marker=">", color="#d55e00", markersize=7, label="Initial population")
    axes[1].set(title="Nicholson-Bailey: outward spiral")
    axes[1].text(0.04, 0.95, "Both eigenvalues have modulus > 1", transform=axes[1].transAxes, va="top")
    for axis in axes:
        axis.plot(1, 1, "k+", markersize=11, markeredgewidth=2)
        axis.set(xlabel=r"Prey or host abundance $X/X_*$", ylabel=r"Predator or parasitoid abundance $Y/Y_*$")
        axis.grid(alpha=0.2)
        axis.set_aspect("equal", adjustable="box")
    fig.suptitle("Illustrative annual maps with matching positive equilibria", fontsize=16)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
