"""Plot distinguishable and aliased samples; write sampling-aliasing.png to cwd.

Uses the root pyproject.toml dependencies. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    time = np.linspace(0, 1, 2001)
    slow = np.cos(2 * np.pi * 2 * time)
    fast = np.cos(2 * np.pi * 8 * time)
    blue, orange = "#2266aa", "#ce6a16"
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.4), layout="constrained")
    fig.suptitle("Sampling: different waves can leave the same numbers", fontsize=16)
    for ax, rate in zip(axes, (20, 10)):
        samples = np.arange(rate + 1) / rate
        slow_samples = np.cos(2 * np.pi * 2 * samples)
        fast_samples = np.cos(2 * np.pi * 8 * samples)
        ax.plot(time, slow, color=blue, lw=2, label="2 cycles/s")
        ax.plot(time, fast, color=orange, lw=1.7, alpha=0.8, label="8 cycles/s")
        ax.scatter(samples, slow_samples, s=72, facecolors="white", edgecolors=blue,
                   linewidths=1.7, zorder=4, label="2 cycles/s samples")
        ax.scatter(samples, fast_samples, s=38, marker="x", color=orange,
                   linewidths=1.6, zorder=5, label="8 cycles/s samples")
        ax.set(xlim=(-0.025, 1.025), ylim=(-1.25, 1.25),
               xlabel="Time (seconds)", ylabel="Value")
        ax.grid(alpha=0.18)
        if rate == 20:
            ax.set_title("20 samples/s: the two sets of samples differ", loc="left", fontsize=12)
            ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.30), ncol=4, fontsize=9)
        else:
            ax.set_title("10 samples/s: every orange cross lands on a blue circle", loc="left", fontsize=12)
    fig.savefig(Path("sampling-aliasing.png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
