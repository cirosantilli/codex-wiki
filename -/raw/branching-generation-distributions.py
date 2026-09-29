"""Exact Galton-Watson generation PMFs for p=(1/4, 1/4, 1/2).

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Build: make _media/branching-generation-distributions.png
Writes an opaque white same-basename PNG to the working directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def generation_distributions(last=6):
    """Return exact rational coefficients of G_n=F composed n times.

    Independently check normalization, extinction iteration and mean.
    Coefficient k is P(Z_n=k); no Monte Carlo or truncated support.
    """
    quarter, half = Fraction(1, 4), Fraction(1, 2)
    pmf = [Fraction(0), Fraction(1)]
    extinction = Fraction(0)
    distributions = []
    for n in range(last + 1):
        assert len(pmf) == 2**n + 1
        assert all(p >= 0 for p in pmf)
        assert sum(pmf) == 1
        assert pmf[0] == extinction
        mean = sum(k * p for k, p in enumerate(pmf))
        assert mean == Fraction(5, 4)**n
        if n == 2:
            assert pmf == [Fraction(11, 32), Fraction(1, 8),
                           Fraction(9, 32), Fraction(1, 8), Fraction(1, 8)]
        distributions.append(pmf)
        if n == last:
            break
        # G_{n+1} = 1/4 + G_n/4 + G_n^2/2, computed over rationals.
        square = [Fraction(0)] * (2 * len(pmf) - 1)
        for i, a in enumerate(pmf):
            for j, b in enumerate(pmf):
                square[i + j] += a * b
        next_pmf = [half * coefficient for coefficient in square]
        for k, p in enumerate(pmf):
            next_pmf[k] += quarter * p
        next_pmf[0] += quarter
        pmf = next_pmf
        extinction = quarter + quarter * extinction + half * extinction**2
    return distributions


def main():
    distributions = generation_distributions()
    for n, pmf in enumerate(distributions):
        mean = sum(k * p for k, p in enumerate(pmf))
        print(f"n={n}: full support 0..{len(pmf)-1}, exact mass=1, "
              f"q_n={float(pmf[0]):.12f}, mean={float(mean):.12f}")
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.8), dpi=120,
                             sharey=True, facecolor="white")
    for ax, n in zip(axes.flat, (0, 2, 4, 6)):
        pmf = distributions[n]
        sizes = np.arange(len(pmf))
        masses = np.array([float(p) for p in pmf])
        colors = ["#c55c28"] + ["#237a9c"] * (len(pmf) - 1)
        ax.bar(sizes, masses, color=colors, width=0.8, zorder=3)
        mean = float(Fraction(5, 4)**n)
        ax.axvline(mean, color="#324254", ls="--", lw=1.4, zorder=4)
        # One ancestor is certain at n=0; every later PMF has all sizes 0..2^n.
        ax.set(title=f"Generation n = {n}", xlabel=r"Population size $k$",
               ylabel=r"Probability $P(Z_n=k)$", ylim=(0, 1.08),
               xlim=(-0.8, max(2.8, 2**n + 0.8)))
        if n == 0:
            ax.set_xticks([0, 1, 2])
        elif n == 2:
            ax.set_xticks(range(5))
        else:
            ax.set_xticks(np.arange(0, 2**n + 1, 2**n // 4))
        ax.text(0.97, 0.94,
                f"Empty: {masses[0]:.6f}\nMean: {mean:.6f}",
                transform=ax.transAxes, ha="right", va="top", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none"})
        ax.grid(axis="y", color="#e6ebf0", zorder=0)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Exact generation distributions: growth can coexist with extinction",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.91, r"Offspring: $p_0=1/4$, $p_1=1/4$, $p_2=1/2$; one initial ancestor",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025,
             "Orange: empty families. Blue: nonempty families. Dashed line: mean.\n"
             "Each panel shows its full support, on a different horizontal scale; eventual extinction = 1/2.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.83, bottom=0.14,
                        hspace=0.44, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
