"""Draw bandwidth detail and positive-support leakage; write the PNG to cwd.

Run from _media with: python3 ../kernel-density-bandwidth.py
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import erfc, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def gaussian_kde(x, sample, bandwidth):
    displacement = (np.asarray(x)[..., None] - sample) / bandwidth
    return np.exp(-0.5 * displacement**2).mean(axis=-1) / (
        bandwidth * np.sqrt(2 * np.pi))


def main():
    sample = np.array([-1.8, -1.4, -1.1, -0.7, 0.7, 1.1, 1.4, 1.8])
    x = np.linspace(-5.5, 5.5, 6001)
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.5), dpi=120,
                             layout="constrained", facecolor="white")
    for ax, bandwidth, title in zip(
        axes.flat, [0.08, 0.35, 1.2],
        ["Narrow spikes at observations", "Two broad observed groups", "Groups blur together"],
    ):
        ax.plot(x, gaussian_kde(x, sample, bandwidth), color="#2878ad", lw=2.3)
        ax.scatter(sample, np.full(len(sample), -0.018), marker="|", s=100, lw=2,
                   color="#202734", clip_on=False)
        ax.set(title=f"h = {bandwidth:g}: {title}", xlim=(-5.5, 5.5), ylim=(-0.04, 0.8))
        ax.text(0.97, 0.91, "Total area = 1", transform=ax.transAxes,
                ha="right", fontsize=10)

    positive_sample = np.array([0.1, 0.4, 0.9])
    bandwidth = 0.5
    boundary_x = np.linspace(-2.2, 3, 3001)
    ax = axes[1, 1]
    ax.plot(boundary_x, gaussian_kde(boundary_x, positive_sample, bandwidth),
            color="#202734", lw=2.3)
    below_zero = np.linspace(-2.2, 0, 1401)
    ax.fill_between(below_zero, gaussian_kde(below_zero, positive_sample, bandwidth),
                    color="#c34e39", alpha=0.3)
    ax.axvline(0, color="#8a8a8a", lw=1, ls="--")
    ax.scatter(positive_sample, np.full(3, -0.018), marker="|", s=100, lw=2,
               color="#202734", clip_on=False)
    leaked_mass = sum(erfc(v / (bandwidth * sqrt(2))) / 2 for v in positive_sample) / 3
    ax.annotate(f"Below zero: {100 * leaked_mass:.2f}%", xy=(-0.35, 0.18),
                xytext=(-2.08, 0.54), fontsize=10, color="#9f3829",
                arrowprops={"arrowstyle": "->", "color": "#9f3829"})
    ax.text(0.98, 0.9, "Sample: 0.1, 0.4, 0.9\nKnown support: x >= 0",
            transform=ax.transAxes, ha="right", fontsize=10)
    ax.set(title="h = 0.5: positive data leak below zero", xlim=(-2.2, 3), ylim=(-0.04, 0.8))
    for ax in axes.flat:
        ax.set(xlabel="Outcome x", ylabel="Probability density", facecolor="white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e8e8e8", lw=0.7)
    fig.savefig(Path.cwd() / "kernel-density-bandwidth.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
