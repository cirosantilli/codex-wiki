"""Draw a maxima-Gumbel return-level curve with chosen toy parameters.

CDF and inverse convention: NIST EDA handbook, section 1.3.6.6.16.
https://www.itl.nist.gov/div898/handbook/eda/section3/eda366g.htm
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib:
    python3 ../gumbel-return-level-curve.py
Writes the matching PNG basename to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7+dfsg1.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


def return_level(period, location=10.0, scale=2.0):
    """Invert the maxima-Gumbel CDF at 1 - 1 / period for period > 1."""
    period = np.asarray(period, dtype=float)
    return location - scale * np.log(-np.log1p(-1.0 / period))


def main():
    period = np.geomspace(2.0, 1000.0, 1001)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.8), dpi=100)
    ax.semilogx(period, return_level(period), color="#226d9b", lw=2.7,
                label="Exact maxima-Gumbel quantile")
    ax.semilogx(period, 10 + 2 * np.log(period), color="#9c651e", lw=2,
                linestyle=":", label=r"Large-$T$ approximation: $10+2\log T$")
    positions = {2: (3.0, 10.95), 10: (14, 14.0),
                 100: (36, 20.5), 1000: (200, 24.6)}
    for t, position in positions.items():
        z = float(return_level(t))
        ax.scatter(t, z, color="#226d9b", s=45, zorder=5)
        ax.annotate(f"T = {t}: {z:.3f}", xy=(t, z), xytext=position,
                    fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": "#226d9b"},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    z100 = float(return_level(100))
    ax.plot([2, 100, 100], [z100, z100, 10], color="#677480", lw=1.2,
            linestyle="--", zorder=1)
    ax.text(2.2, z100 + 0.22, "Read across, then down: 19.200 units ↔ 100 years",
            fontsize=10.5, color="#46515c")
    ticks = [2, 10, 100, 1000]
    ax.set(xlim=(2, 1000), ylim=(10, 25.5),
           xlabel=r"Return period $T$ (toy years; logarithmic axis)",
           ylabel=r"Return level $z_T$ (arbitrary units)")
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.set_yticks([10, 12, 14, 16, 18, 20, 22, 24])
    top = ax.secondary_xaxis("top")
    top.set_xticks(ticks, ["50%", "10%", "1%", "0.1%"])
    top.set_xlabel(r"Annual exceedance probability $1/T$", labelpad=9)
    top.minorticks_off()
    ax.grid(alpha=0.18)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="lower right", framealpha=1, fontsize=10.5)
    fig.suptitle(r"Return level: invert the annual distribution ($\mu=10$, $b=2$)",
                 weight="bold", fontsize=15, y=0.97)
    fig.text(0.5, 0.025, "Exact toy model. Markers are calculated quantiles; no data or confidence intervals.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.105, right=0.97, bottom=0.16, top=0.76)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
