"""Plot normalized exponential maxima and their Gumbel limit; PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def normalized_cdf(z, n):
    """Use the shifted support, avoiding powers of a negative CDF base."""
    z = np.asarray(z, dtype=float)
    shifted = np.maximum(z + np.log(n), 0.0)
    return (-np.expm1(-shifted)) ** n


def gumbel_cdf(z):
    return np.exp(-np.exp(-np.asarray(z, dtype=float)))


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=100)
    z = np.linspace(-4.5, 6, 2801)
    for n, color, style in zip((1, 5, 20, 100),
                               ("#bf5b20", "#2674af", "#8862ad", "#34804a"),
                               ("-", "--", "-.", "-")):
        ax.plot(z, normalized_cdf(z, n), color=color, linestyle=style,
                linewidth=2.2, label=rf"Exact, $n={n}$")
    ax.plot(z, gumbel_cdf(z), color="#222222", linestyle=(0, (4, 2)),
            linewidth=2.8, label=r"Gumbel limit $\exp(-e^{-z})$")
    median = -np.log(np.log(2))
    ax.scatter([median], [0.5], color="#222222", s=43, zorder=6)
    ax.annotate("Limit median\n0.366513", xy=(median, 0.5), xytext=(2.2, 0.43),
                fontsize=11, ha="left", va="center",
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.set(xlim=(-4.5, 6), ylim=(0, 1.025),
           xlabel=r"Normalized threshold $z$ (dimensionless)",
           ylabel=r"Cumulative probability $P(Z_n\leq z)$")
    ax.legend(loc="upper left", frameon=True, framealpha=0.96, fontsize=10.5)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Subtract the logarithmic growth: one limiting shape remains",
                 fontsize=15, weight="bold", y=0.96)
    ax.set_title(r"$Z_n=\lambda M_n-\log n$ for independent exponential observations",
                 fontsize=12, pad=13)
    fig.text(0.5, 0.025, r"Finite-sample CDFs are zero below $-\log n$; the limit has no finite lower boundary.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.105, right=0.97, bottom=0.15, top=0.80)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
