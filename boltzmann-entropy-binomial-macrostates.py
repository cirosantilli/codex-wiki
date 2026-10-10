"""Count binary configurations of 20 labeled particles by left occupancy.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3
../boltzmann-entropy-binomial-macrostates.py
Writes its matching PNG basename to the current working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7 (Debian +dfsg1).
"""

from math import comb, log
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator


def main():
    n = 20
    ks = list(range(n + 1))
    counts = [comb(n, k) for k in ks]
    entropies = [log(count) for count in counts]
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), dpi=120)
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.23, top=0.76, wspace=0.32)
    fig.suptitle("Twenty labels, two equal boxes: count each occupancy", fontsize=16, y=0.96)
    fig.text(0.5, 0.87, "One string per left/right assignment; all 1,048,576 strings equally likely",
             ha="center", fontsize=12)
    blue, orange = "#216b9d", "#ac4b14"
    axes[0].bar(ks, counts, color=blue, width=0.72)
    axes[0].bar([10], [counts[10]], color=orange, width=0.72)
    axes[0].set_ylabel(r"Count $\Omega(k)=\binom{20}{k}$")
    axes[0].set_ylim(0, 245000)
    axes[0].yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    axes[0].annotate("184,756 at k = 10", xy=(10, counts[10]), xytext=(10, 222000),
                     ha="center", fontsize=11, color=orange,
                     arrowprops={"arrowstyle": "->", "color": orange})
    axes[1].plot(ks, entropies, "o-", color=blue, markersize=4, linewidth=1.8)
    axes[1].scatter([10], [entropies[10]], color=orange, zorder=3, s=45)
    axes[1].set_ylabel(r"Entropy $S(k)/k_B=\ln\Omega(k)$")
    axes[1].set_ylim(-0.6, 16.0)
    axes[1].annotate("12.126791 at k = 10", xy=(10, entropies[10]), xytext=(10, 14.4),
                     ha="center", fontsize=11, color=orange,
                     arrowprops={"arrowstyle": "->", "color": orange})
    for ax in axes:
        ax.set(xlim=(-0.7, 20.7), xlabel="Number k in the left box")
        ax.set_xticks([0, 5, 10, 15, 20])
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.grid(axis="y", alpha=0.22)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.12, r"All-left: $k=20$, $\Omega=1$, $S/k_B=0$; all-right is symmetric.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.055, r"One balanced macrostate: $\ln 184756$; all allowed strings together: $20\ln 2=13.862944$.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "boltzmann-entropy-binomial-macrostates.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
