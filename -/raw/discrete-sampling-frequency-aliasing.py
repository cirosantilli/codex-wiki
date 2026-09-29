"""Plot m=1 and m=9 aliases; write discrete-sampling-frequency-aliasing.png to cwd.

Uses only the root pyproject.toml dependencies. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    time = np.linspace(0, 1, 2401)
    sample_time = np.arange(8) / 8
    blue, orange = "#2266aa", "#ce6a16"
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.6), layout="constrained")
    fig.suptitle("One cycle and nine cycles: identical eight samples", fontsize=16)
    for ax, trig, name in zip(axes, (np.cos, np.sin), ("Cosine", "Sine")):
        slow = trig(2 * np.pi * sample_time)
        fast = trig(18 * np.pi * sample_time)
        np.testing.assert_allclose(slow, fast, atol=1e-14)
        ax.plot(time, trig(2 * np.pi * time), color=blue, lw=2.4,
                label="m = 1: one cycle per unit time")
        ax.plot(time, trig(18 * np.pi * time), color=orange, lw=1.5, alpha=0.85,
                label="m = 9: nine cycles per unit time")
        ax.scatter(sample_time, slow, facecolors="white", edgecolors=blue,
                   s=105, linewidths=1.9, zorder=4, label="m = 1 samples")
        ax.scatter(sample_time, fast, color=orange, marker="x", s=55,
                   linewidths=1.9, zorder=5, label="m = 9 samples")
        ax.axhline(0, color="#999999", lw=0.8, zorder=0)
        ax.set(title=f"{name}: every orange cross lands on a blue circle",
               xlim=(-0.025, 1.025), ylim=(-1.45, 1.85),
               xlabel="Time t (samples at n/8, n = 0,…,7)", ylabel="Value",
               xticks=np.arange(9) / 8)
        ax.grid(alpha=0.17)
        ax.legend(loc="upper right", ncol=2, fontsize=9)
    fig.savefig(Path("discrete-sampling-frequency-aliasing.png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
