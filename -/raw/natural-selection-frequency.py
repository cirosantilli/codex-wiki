"""Original selection/drift illustration; writes basename.png to the cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The finite model samples N haploid offspring independently with replacement.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def selected_frequency(p, w):
    return w * p / (w * p + 1 - p)


def main():
    p0, n, generations = 0.2, 50, 30
    times = np.arange(generations + 1)
    rng = np.random.default_rng(1859)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 4.3), sharey=True)
    fig.set_facecolor("white")
    colors = plt.get_cmap("tab10").colors
    for ax, w in zip(axes, (1.2, 1.0)):
        deterministic = w**times * p0 / (1 - p0 + w**times * p0)
        for j in range(8):
            path = np.empty(generations + 1)
            path[0] = p0
            for t in range(generations):
                q = selected_frequency(path[t], w)
                path[t + 1] = rng.binomial(n, q) / n
            ax.plot(times, path, color=colors[j], lw=1.15, alpha=0.7,
                    label="8 finite-population paths" if j == 0 else None)
        ax.plot(times, deterministic, color="#171717", lw=2.6,
                linestyle="--", label="Deterministic limit" if w > 1
                else "Neutral expected frequency")
        ax.plot(0, p0, "o", color="#171717", ms=4)
        ax.set(xlim=(0, generations), ylim=(-0.025, 1.025),
               xlabel="Generation", xticks=[0, 10, 20, 30])
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="lower right", fontsize=8, framealpha=0.95)
    axes[0].set_title("Selection + drift: w = 1.2", fontsize=12)
    axes[1].set_title("Neutral drift: w = 1", fontsize=12)
    axes[0].set_ylabel("Frequency of inherited type A")
    axes[0].annotate("First update: 0.23077", xy=(1, 3 / 13),
                     xytext=(4, 0.42), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#333333"})
    fig.suptitle("Expected advantage and random offspring sampling", fontsize=14)
    fig.text(0.5, 0.025, "Idealized haploid models; N = 50 for each simulated path; initial frequency = 0.2",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.065, 1, 0.94))
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
