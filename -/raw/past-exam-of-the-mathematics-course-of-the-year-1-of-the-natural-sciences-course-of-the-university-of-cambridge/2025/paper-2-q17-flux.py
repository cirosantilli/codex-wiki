"""Generate the Q17 flux sketch; tested with Python 3.14, NumPy 2.3.5,
and Matplotlib 3.10.7, using the repository's pyproject.toml dependencies.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(-1, 1, 500)
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
    curves = [2 + 3 * z - z**3, 3 * (1 - z**2)]
    labels = [r"$\Phi(z_0)/\pi$", r"$\Phi'(z_0)/\pi$"]
    endpoint_values = [(0, 4), (0, 0)]
    for ax, values, label, ends in zip(axes, curves, labels, endpoint_values):
        ax.plot(z, values, color="#176b9c", linewidth=2.3)
        ax.scatter([-1, 1], ends, s=40, facecolors="white", edgecolors="#176b9c", zorder=3)
        ax.axvline(0, color="0.7", linewidth=0.8)
        ax.axhline(0, color="0.7", linewidth=0.8)
        ax.set(xlabel=r"Truncation height $z_0$", ylabel=label, xlim=(-1.07, 1.07), ylim=(-0.16, 4.25))
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([0, 1, 2, 3, 4])
        ax.grid(alpha=0.2)
    axes[0].set_title("Flux increases with enclosed volume")
    axes[1].set_title("Rate of change peaks at the equator")
    axes[0].scatter([0], [2], color="#176b9c", s=20)
    axes[1].scatter([0], [3], color="#176b9c", s=20)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
