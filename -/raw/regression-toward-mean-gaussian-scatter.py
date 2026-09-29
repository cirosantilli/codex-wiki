"""Original synthetic Gaussian pair; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes this script's basename with a .png suffix to the CWD.
The shaded band is one conditional standard deviation, not a confidence interval.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(314159)
    x, z = rng.standard_normal((2, 1800))
    y = 0.6 * x + 0.8 * z
    selected = x > 1
    grid = np.linspace(-3.5, 3.5, 400)
    fig, ax = plt.subplots(figsize=(8.2, 5.7), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axvspan(1, 3.5, color="#f6d3a6", alpha=0.30)
    ax.fill_between(grid, 0.6 * grid - 0.8, 0.6 * grid + 0.8,
                    color="#d9eaf7", label="One conditional SD: 0.8")
    ax.scatter(x[~selected], y[~selected], s=9, color="#617586", alpha=0.30,
               edgecolors="none", label="Generated pairs with X ≤ 1")
    ax.scatter(x[selected], y[selected], s=13, color="#c87920", alpha=0.60,
               edgecolors="none", label="Generated pairs selected by X > 1")
    ax.plot(grid, grid, "--", color="#454545", linewidth=1.6, label="No change: Y = X")
    ax.plot(grid, 0.6 * grid, color="#135a99", linewidth=2.5,
            label="Conditional mean: E[Y | X = x] = 0.6x")
    ax.axvline(1, color="#c87920", linewidth=1.1)
    ax.axhline(0, color="#bbbbbb", linewidth=0.6)
    ax.axvline(0, color="#bbbbbb", linewidth=0.6)
    ax.errorbar(2, 1.2, yerr=0.8, fmt="o", color="#103e65", capsize=5,
                linewidth=2, zorder=5)
    ax.annotate("At X = 2: mean 1.2, SD 0.8", xy=(2, 1.2), xytext=(-3.2, -2.75),
                arrowprops={"arrowstyle": "->", "color": "#103e65"}, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.94})
    ax.set(xlim=(-3.5, 3.5), ylim=(-3.5, 3.5),
           xlabel="First measurement X (standardized units)",
           ylabel="Second measurement Y (standardized units)",
           title="Synthetic Gaussian model: correlation 0.6\n"
                 "1,800 generated pairs; no actual measurements")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.96)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
