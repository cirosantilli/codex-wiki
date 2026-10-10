"""Plot exact exponential maxima; write the basename PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def maximum_cdf(x, n, rate=1.0):
    """CDF with the nonnegative support handled explicitly."""
    x = np.asarray(x, dtype=float)
    return (-np.expm1(-rate * np.maximum(x, 0.0))) ** n


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=100)
    x = np.linspace(-0.35, 10, 2401)
    for n, color in zip((1, 10, 100), ("#bf5b20", "#2674af", "#34804a")):
        median = -np.log(-np.expm1(np.log(0.5) / n))
        ax.plot(x, maximum_cdf(x, n), color=color, linewidth=2.6,
                label=rf"$n={n}$: median {median:.3f} s")
        ax.vlines(median, 0, 0.5, color=color, linestyle=":", linewidth=1.3)
        ax.scatter([median], [0.5], color=color, s=48, zorder=5)
    ax.axhline(0.5, color="#555555", linestyle="--", linewidth=1.1)
    ax.set(xlim=(-0.35, 10), ylim=(0, 1.025),
           xlabel="Delay threshold x (seconds)",
           ylabel=r"Cumulative probability $P(M_n\leq x)$")
    ax.legend(loc="lower right", frameon=True, framealpha=0.96, fontsize=11)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("More independent delays move the maximum to the right",
                 fontsize=15, weight="bold", y=0.96)
    ax.set_title(r"Exact laws: $M_n=\max(X_1,\ldots,X_n)$, rate $\lambda=1\ \mathrm{s}^{-1}$",
                 fontsize=12, pad=13)
    fig.text(0.5, 0.025, "Dots mark exact medians; every curve is zero for negative delays.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.105, right=0.97, bottom=0.15, top=0.80)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
