"""Draw a computed Gaussian KDE example; write the PNG to the current directory.

Run from _media with: python3 ../kernel-density-components.py
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    sample = np.array([-1.0, 0.0, 1.0])
    bandwidth = 0.5
    x = np.linspace(-3, 3, 2401)
    components = np.exp(-0.5 * ((x[:, None] - sample) / bandwidth) ** 2)
    components /= len(sample) * bandwidth * np.sqrt(2 * np.pi)
    estimate = components.sum(axis=1)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=120,
                             layout="constrained", facecolor="white")
    colors = ["#2878ad", "#cb632b", "#25846c"]
    for i, (center, color) in enumerate(zip(sample, colors)):
        axes[0].plot(x, components[:, i], color=color, lw=2,
                     label=f"Observation {center:g}: area 1/3")
    axes[0].plot(x, estimate, color="#202734", lw=2.5, label="Sum: total area 1")
    axes[0].scatter([0], [2 * (1 + 2 * np.exp(-2)) / (3 * np.sqrt(2 * np.pi))],
                    color="#202734", s=35, zorder=5)
    axes[0].annotate("Height at 0 = 0.337949", xy=(0, estimate[len(x) // 2]),
                     xytext=(-2.7, 0.43), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#202734"})
    axes[0].set_title("Add three weighted Gaussian bumps")
    axes[0].legend(loc="upper right", fontsize=9, framealpha=1)

    axes[1].plot(x, estimate, color="#202734", lw=2.5)
    interval = np.linspace(-0.5, 0.5, 601)
    interval_density = np.exp(-0.5 * ((interval[:, None] - sample) / bandwidth) ** 2)
    interval_density = interval_density.sum(axis=1) / (
        len(sample) * bandwidth * np.sqrt(2 * np.pi))
    axes[1].fill_between(interval, interval_density, color="#2878ad", alpha=0.3)
    axes[1].vlines([-0.5, 0.5], 0, [interval_density[0], interval_density[-1]],
                   color="#2878ad", lw=1.5, ls="--")
    axes[1].text(0, 0.17, "Interval area\n0.332433", ha="center", color="#1d4e74")
    axes[1].text(0, 0.435, "Density height and probability area differ", ha="center", fontsize=10)
    axes[1].set_title("Fitted probability of [-0.5, 0.5]")
    for ax in axes:
        ax.scatter(sample, np.full(3, -0.012), marker="|", s=120, lw=2,
                   color="#202734", clip_on=False, label="Observed sample")
        ax.set(xlabel="Outcome x", ylabel="Probability density", xlim=(-3, 3),
               ylim=(-0.025, 0.48), facecolor="white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e8e8e8", lw=0.7)
    fig.savefig(Path.cwd() / "kernel-density-components.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
