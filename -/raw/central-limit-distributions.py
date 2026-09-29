"""Generate central-limit-distributions.png in the caller's working directory.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Uses exact binomial probabilities (successive convolutions), not simulations.
Run from _media with MPLCONFIGDIR set to a writable temporary directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def binomial_probabilities(n, p):
    probabilities = np.array([1.0])
    for _ in range(n):
        probabilities = np.convolve(probabilities, [1 - p, p])
    return probabilities


def main():
    p = 0.2
    grid = np.linspace(-4, 5, 700)
    normal_density = np.exp(-grid**2 / 2) / np.sqrt(2 * np.pi)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.7), dpi=120,
                             facecolor="white", sharex=True, sharey=True)
    for ax, n in zip(axes.flat, [1, 5, 25, 100]):
        probabilities = binomial_probabilities(n, p)
        counts = np.arange(n + 1)
        scale = np.sqrt(n * p * (1 - p))
        positions = (counts - n * p) / scale
        spacing = 1 / scale
        assert np.isclose(probabilities.sum(), 1)
        assert np.isclose(np.dot(positions, probabilities), 0, atol=1e-12)
        assert np.isclose(np.dot(positions**2, probabilities), 1)
        ax.bar(positions, probabilities / spacing, width=spacing,
               color="#2b7bba", alpha=0.7, edgecolor="white", linewidth=0.5,
               label="Exact mass / lattice spacing")
        ax.plot(grid, normal_density, color="#b24a23", lw=2.3,
                label="Standard normal density")
        ax.set(title=f"n = {n} trials", xlim=(-4, 5), ylim=(0, 0.48))
        ax.grid(axis="y", alpha=0.18)
    for ax in axes[-1]:
        ax.set_xlabel(r"Standardized count $z = (k - np)/\sqrt{np(1-p)}$")
    for ax in axes[:, 0]:
        ax.set_ylabel("Probability per unit z")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, 0.025))
    fig.suptitle("Central limit theorem: skewed Bernoulli trials, p = 0.2",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.005,
             "Each blue rectangle has area P(K = k); every panel has mean 0 and variance 1.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.085, 1, 0.95))
    fig.savefig(Path.cwd() / "central-limit-distributions.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
