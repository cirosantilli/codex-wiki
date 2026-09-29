"""The same exact ECDF gap on exponential and uniform horizontal scales.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; output uses
the script basename in the current directory. No sampling or p-values.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    u = np.array([0.1, 0.4, 0.8, 0.9])
    x = -np.log1p(-u)
    np.testing.assert_allclose(-np.expm1(-x), u, atol=1e-15)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.8), sharey=True,
                             layout="constrained")
    for ax, values, xmax, name in zip(axes, [x, u], [3, 1], ["exponential", "uniform"]):
        t = np.linspace(0, xmax, 700)
        f = -np.expm1(-t) if name == "exponential" else t
        ax.plot(t, f, color="#d47716", lw=2, label="Specified CDF")
        edges = np.r_[0, values, xmax]
        for i in range(5):
            ax.plot(edges[i:i + 2], [i / 4] * 2, color="#1767a6", lw=2.5,
                    label="ECDF" if i == 0 else None)
        ax.scatter(values, np.arange(4) / 4, s=55, facecolors="white",
                   edgecolors="#1767a6", linewidths=1.5, zorder=5)
        ax.scatter(values, np.arange(1, 5) / 4, s=40, color="#1767a6", zorder=6)
        ax.annotate("", xy=(values[2], 0.8), xytext=(values[2], 0.5),
                    arrowprops={"arrowstyle": "<->", "color": "#a72f57", "lw": 2})
        ax.text(values[2] - 0.07 * xmax, 0.67, r"$3/10$", ha="right", color="#a72f57")
        ax.set(xlim=(-0.02 * xmax, xmax * 1.02), ylim=(-0.03, 1.05))
        ax.set_yticks(np.arange(5) / 4)
        ax.grid(alpha=0.15)
        ax.legend(loc="lower right", fontsize=10, framealpha=1)
    axes[0].set(title=r"$F_0(x)=1-e^{-x}$, $x\geq0$", xlabel=r"Threshold $x$")
    axes[0].set_ylabel("Cumulative probability")
    axes[1].set(title=r"$u=F_0(x)$: uniform scale", xlabel=r"Threshold $u$")
    axes[1].set_xticks([0, 0.1, 0.4, 0.8, 0.9, 1])
    fig.suptitle("Probability integral transform preserves the vertical gap", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
