"""Plot finite-support approximations and write the PNG basename to cwd.

Uses numpy/matplotlib from pyproject.toml; tested with Python 3.14.4.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../banach-completion-tail.py
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def check_tails():
    """Verify finite errors and the infinite tail using exact rational arithmetic."""
    for n in (1, 4, 10, 20):
        partial_sum = sum((Fraction(1, 2**k) for k in range(1, n + 1)), Fraction(0))
        assert 1 - partial_sum == Fraction(1, 2**n)
        for m in (n + 1, n + 7):
            difference = sum((Fraction(1, 2**k) for k in range(n + 1, m + 1)), Fraction(0))
            assert difference == Fraction(1, 2**n) - Fraction(1, 2**m)
        print(f"N={n}: norm={float(partial_sum):.12f}, exact tail={1 - partial_sum}")


def main():
    check_tails()
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.6),
                                    layout="constrained", facecolor="white")
    retained = 4
    k = np.arange(1, 11)
    values = 2.0**(-k)
    for mask, color, label in (
        (k <= retained, "#2873a7", r"Retained in $x^{(4)}$"),
        (k > retained, "#d07628", r"Omitted from $x^{(4)}$"),
    ):
        left.vlines(k[mask], 0, values[mask], color=color, linewidth=2.8)
        left.scatter(k[mask], values[mask], color=color, s=45, zorder=3, label=label)
    left.scatter(k[k > retained], np.zeros_like(k[k > retained]),
                 facecolors="white", edgecolors="#2873a7", s=35, zorder=4)
    left.axvline(4.5, color="#777777", linestyle=":", linewidth=1.3)
    left.text(5.1, 0.27, "An infinite nonzero tail\nwith finite total size:\n" +
              r"$\sum_{k=5}^{\infty}2^{-k}=1/16$", color="#a6571c")
    left.annotate("Tail continues", (10, values[-1]), xytext=(7.1, 0.09),
                  arrowprops={"arrowstyle": "->", "color": "#555555"})
    left.set(xlabel=r"Coordinate $k$", ylabel=r"Coordinate value $2^{-k}$",
             title="Four coordinates stored; the limit needs infinitely many",
             xlim=(0.5, 10.6), ylim=(-0.015, 0.55))
    left.set_xticks([1, 2, 4, 6, 8, 10])
    left.legend(loc="upper right", fontsize=10)
    left.grid(axis="y", alpha=0.2)

    n = np.arange(1, 13)
    tail = 2.0**(-n)
    right.semilogy(n, tail, "o-", color="#2873a7", linewidth=2.3, markersize=5,
                    label=r"$\|x-x^{(N)}\|_1=2^{-N}$")
    for count, offset in ((4, (18, 7)), (10, (-85, -30))):
        right.annotate(f"N={count}: 1/{2**count}", (count, 2.0**(-count)),
                       xytext=offset, textcoords="offset points", fontsize=10,
                       arrowprops={"arrowstyle": "->", "color": "#555555"})
    right.set(xlabel=r"Number of retained coordinates $N$",
              ylabel="Absolute-sum error (log scale)",
              title="Every extra coordinate halves the total error",
              xlim=(0.5, 12.5), ylim=(1.2e-4, 0.9))
    right.set_xticks([1, 4, 6, 8, 10, 12])
    right.legend(loc="upper right", fontsize=10)
    right.grid(which="major", alpha=0.2)
    fig.suptitle(r"Completion: from $c_{00}$ to $\ell^1$", fontsize=16)
    destination = Path.cwd() / "banach-completion-tail.png"
    fig.savefig(destination, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {destination.name}")


if __name__ == "__main__":
    main()
