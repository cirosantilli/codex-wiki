"""Plot the optimal value, its supporting tangent and the inequality multiplier.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; saves this script's basename.png in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11})
    bound = np.linspace(-0.1, 3.8, 800)
    value = np.maximum(2 - bound, 0) ** 2
    multiplier = 2 * np.maximum(2 - bound, 0)
    tangent = 3 - 2 * bound
    assert np.all(value >= tangent - 1e-12)
    assert np.isclose((2 - 1.1) ** 2 - 1, -0.19)
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 6.5), sharex=True,
                             layout="constrained", facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axvspan(bound[0], 2, color="#e0f0e8")
        ax.axvspan(2, bound[-1], color="#edf0f4")
        ax.axvline(2, color="#6b7580", lw=1.3, ls=":")
        ax.grid(alpha=0.18)
        ax.set_xlim(bound[0], bound[-1])
    top, bottom = axes
    top.plot(bound, value, lw=2.7, color="#246f55", label=r"$V(b)=\max(2-b,0)^2$")
    top.plot(bound, tangent, ls="--", lw=1.7, color="#cb7029", label=r"Supporting tangent $3-2b$")
    top.scatter([1, 1.1, 2, 3], [1, 0.81, 0, 0], color="#246f55", s=42, zorder=5)
    top.annotate("At b = 1: slope = −2", (1, 1), xytext=(1.3, 2.35),
                 arrowprops={"arrowstyle": "->", "color": "#cb7029"}, fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    top.annotate("Flat value: extra room has no benefit", (3, 0), xytext=(2.05, 1.35),
                 arrowprops={"arrowstyle": "->", "color": "#246f55"}, fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    top.set(ylim=(-0.55, 4.6), ylabel="Optimal value V(b)")
    top.legend(loc="upper right", fontsize=10, framealpha=1)
    bottom.plot(bound, multiplier, color="#355e9b", lw=2.7,
                label=r"$\lambda_*(b)=2\max(2-b,0)=-V'(b)$")
    bottom.scatter([1, 2, 3], [2, 0, 0], color="#355e9b", s=42, zorder=5)
    bottom.annotate("b = 2: active constraint,\nzero multiplier", (2, 0), xytext=(2.2, 1.65),
                    arrowprops={"arrowstyle": "->", "color": "#355e9b"}, fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    bottom.text(0.2, 0.35, "Active; positive shadow price", fontsize=10, color="#246f55")
    bottom.text(2.36, 0.38, "Inactive", fontsize=10, color="#4b5663")
    bottom.set(ylim=(-0.25, 4.6), xlabel=r"Upper bound b (increasing b relaxes $x\leq b$)",
               ylabel=r"Multiplier $\lambda_*(b)$")
    bottom.set_xticks([0, 1, 2, 3])
    bottom.legend(loc="upper right", fontsize=10, framealpha=1)
    fig.suptitle("A multiplier measures the value of relaxing the bound", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
