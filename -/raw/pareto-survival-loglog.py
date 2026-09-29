"""Draw exact Pareto survival laws.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media:
MPLBACKEND=Agg python ../pareto-survival-loglog.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 5.6), layout="constrained",
                           facecolor="white")
    ratio = np.geomspace(1, 100, 600)
    colors = ["#a74900", "#007487", "#6743ad"]
    for alpha, color, regime in zip(
        [0.75, 1.5, 3], colors,
        ["infinite mean", "finite mean, infinite variance", "finite variance"],
    ):
        ax.loglog(ratio, ratio ** (-alpha), color=color, linewidth=2.6,
                  label=rf"$\alpha={alpha:g}$: {regime}")
        ax.scatter([10], [10 ** (-alpha)], color=color, s=32, zorder=3)
    ax.axvline(10, color="#666666", linewidth=1, linestyle=":")
    ax.text(11, 0.38, r"At $x=10\beta$: $\overline{F}=10^{-\alpha}$",
            fontsize=11, bbox={"facecolor": "white", "edgecolor": "none"})
    ax.set(xlim=(1, 100), ylim=(1e-6, 1.05),
           xlabel=r"Threshold / minimum, $x/\beta$ (log scale)",
           ylabel=r"Survival probability $P(X>x)$ (log scale)",
           title=r"Pareto survival: straight lines with slope $-\alpha$")
    ax.grid(True, which="major", alpha=0.25)
    ax.legend(loc="lower left", framealpha=1, fontsize=10)
    fig.supxlabel("Exact theoretical curves; chosen parameters, no observed data", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
