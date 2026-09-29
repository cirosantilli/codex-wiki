"""Draw exact toy multi-year exceedance probabilities, without sampled data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib:
    python3 ../return-period-exceedance-horizons.py
Writes the matching PNG basename to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7+dfsg1.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


def main():
    p = 0.01
    years = np.arange(0, 201)
    chance = -np.expm1(years * np.log1p(-p))
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.7), dpi=100)
    ax.plot(years, chance, color="#226d9b", lw=2.7,
            label=r"Independent years: $1-0.99^n$")
    ax.hlines(p, 1, 200, color="#a85120", lw=2.3, linestyle="--",
              label=r"One shared indicator for every year: $0.01$")
    ax.axvline(100, color="#677480", linestyle=":", lw=1.4)
    positions = {10: (26, 0.14), 30: (48, 0.30),
                 50: (68, 0.43), 100: (122, 0.62)}
    for n, position in positions.items():
        value = -np.expm1(n * np.log1p(-p))
        ax.scatter(n, value, s=43, color="#226d9b", zorder=5)
        ax.annotate(f"{n} years: {100 * value:.1f}%", xy=(n, value),
                    xytext=position, fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": "#226d9b"},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.text(105, 0.19, "100 years: mean count = 1\nChance of no exceedance = 36.6%",
            fontsize=11, color="#303840", ha="left", va="center",
            bbox={"facecolor": "white", "edgecolor": "#d4dce2", "pad": 7})
    ax.set(xlim=(0, 200), ylim=(0, 1),
           xlabel=r"Horizon $n$ (complete toy years)",
           ylabel="Probability of at least one exceedance")
    ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    ax.set_xticks([0, 10, 30, 50, 100, 150, 200])
    ax.grid(axis="y", alpha=0.20)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", framealpha=1, fontsize=10.5)
    fig.suptitle("A 100-year return period is a frequency scale",
                 weight="bold", fontsize=16, y=0.97)
    ax.set_title("Both models have a 1% annual exceedance probability",
                 fontsize=12, pad=14)
    fig.text(0.5, 0.025, "Exact toy models, not measurements. Lines join integer-year probabilities.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.16, top=0.82)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
