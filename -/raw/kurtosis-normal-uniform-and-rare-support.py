"""Population densities/masses and fourth moments; no simulation. Python 3.14."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 3, figsize=(10.2, 6.3), layout="constrained", facecolor="white")
    z = np.linspace(-4.5, 4.5, 1801)
    normal = np.exp(-z**2 / 2) / np.sqrt(2 * np.pi)
    a = np.sqrt(3)
    u = np.linspace(-a, a, 801)
    uniform = np.full_like(u, 1 / (2 * a))
    for col, points, density, name, kurtosis, excess in (
        (0, z, normal, "Standard normal", "3", "0"),
        (1, u, uniform, r"Uniform on $[-\sqrt{3},\sqrt{3}]$", "9/5", "−6/5"),
    ):
        top, bottom = axes[:, col]
        top.plot(points, density, color="#2b6f9c", linewidth=2)
        top.fill_between(points, density, color="#2b6f9c", alpha=0.14)
        if col == 1:
            top.vlines([-a, a], 0, density[0], color="#2b6f9c", linewidth=2)
            top.plot([-4.5, -a], [0, 0], color="#2b6f9c")
            top.plot([a, 4.5], [0, 0], color="#2b6f9c")
        weighted = points**4 * density
        bottom.plot(points, weighted, color="#bc4d2f", linewidth=2)
        bottom.fill_between(points, weighted, color="#bc4d2f", alpha=0.18)
        top.set(title=name, ylabel="Density f(z)", ylim=(0, 0.45))
        bottom.set(title=f"Area = κ = {kurtosis}; excess = {excess}", ylabel=r"Fourth-moment density $z^4 f(z)$")
        for ax in (top, bottom):
            ax.set(xlim=(-4.5, 4.5), xlabel="Standard score z", xticks=[-4, -2, 0, 2, 4])
    points = np.array([-10.0, 0.0, 10.0])
    mass = np.array([0.005, 0.99, 0.005])
    for ax, heights, ylabel in (
        (axes[0, 2], mass, "Probability mass p(z)"),
        (axes[1, 2], mass * points**4, r"Fourth-moment mass $p(z)z^4$"),
    ):
        ax.vlines(points, 0, heights, color="#bc4d2f", linewidth=3)
        ax.scatter(points, heights, color="#bc4d2f", zorder=3)
        ax.set(xlim=(-12, 12), ylim=(0, heights.max() * 1.25), xlabel="Standard score z", ylabel=ylabel, xticks=points)
        for point, value in zip(points, heights):
            ax.text(point, value + heights.max() * 0.06, f"{value:g}", ha="center")
    axes[0, 2].set_title("Rare support: q = 0.01")
    axes[1, 2].set_title("Sum = κ = 100; excess = 97")
    fig.text(0.5, 0.965, "Mean 0, variance 1: kurtosis weights distance to the fourth power", ha="center", fontsize=14)
    fig.get_layout_engine().set(rect=(0, 0.055, 1, 0.87))
    fig.text(0.5, 0.015, "Continuous panels show densities; discrete panels show masses. Axis scales differ. Normal tails continue beyond the window.", ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
