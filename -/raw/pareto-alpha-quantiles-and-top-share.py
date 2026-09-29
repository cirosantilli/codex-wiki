"""Compare exact Pareto quantiles and top shares as alpha varies.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter, ScalarFormatter


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.5), layout="constrained",
                             facecolor="white")
    alpha = np.linspace(0.75, 4, 700)
    ax = axes[0]
    for p, color in zip([0.5, 0.9, 0.99], ["#007487", "#a74900", "#6743ad"]):
        ax.semilogy(alpha, (1 - p) ** (-1 / alpha), color=color, linewidth=2.3,
                    label=rf"$p={p:g}$")
    ax.set(xlabel=r"Shape $\alpha$", ylabel=r"Quantile / minimum, $Q(p)/\beta$",
           title="Quantiles remain finite at every shown shape", ylim=(1, 600))
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.legend(title="Cumulative probability", fontsize=10, loc="upper right")
    ax = axes[1]
    finite = alpha[alpha > 1]
    share = 0.2 ** (1 - 1 / finite)
    ax.plot(finite, share, color="#007487", linewidth=2.6)
    ax.axvspan(0.75, 1, color="#eeeeee")
    ax.text(0.88, 0.66, "Infinite mean\nshare undefined", ha="center", va="center",
            rotation=90, fontsize=10)
    chosen = np.log(5) / np.log(4)
    ax.plot([chosen, chosen], [0, 0.8], color="#a74900", linestyle=":")
    ax.plot([0.75, chosen], [0.8, 0.8], color="#a74900", linestyle=":")
    ax.scatter([chosen, 2], [0.8, np.sqrt(0.2)], c=["#a74900", "#007487"],
               s=38, zorder=4)
    ax.annotate(r"80/20: $\alpha=\log 5/\log 4$" + "\n" + r"$\alpha\approx1.160964$",
                xy=(chosen, 0.8), xytext=(1.9, 0.91), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#a74900"})
    ax.annotate(r"$\alpha=2$: 44.72%", xy=(2, np.sqrt(0.2)),
                xytext=(2.25, 0.56), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#007487"})
    ax.set(xlabel=r"Shape $\alpha$", ylabel="Share of amount in largest 20%",
           title=r"$T(0.2)=0.2^{1-1/\alpha}$ requires $\alpha>1$", ylim=(0, 1))
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    for ax in axes:
        for boundary in [1, 2]:
            ax.axvline(boundary, color="#777777", linewidth=1, linestyle="--", zorder=0)
        ax.set_xlim(0.75, 4)
        ax.grid(True, which="major", alpha=0.2)
    fig.supxlabel("Dashed boundaries: finite mean for α > 1; finite variance for α > 2.\n"
                  "Exact theoretical curves with chosen parameters; no observed wealth data.",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
