"""Exact binomial tails versus Hoeffding; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Rational integer weights avoid subtraction of nearly equal CDFs.
"""

from fractions import Fraction
from math import comb, exp, fsum, isclose, lgamma, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def exact_tail(n, numerator, denominator, k):
    """P(K >= k) for p=numerator/denominator, including the boundary mass."""
    if k <= 0:
        return Fraction(1)
    if k > n:
        return Fraction(0)
    return Fraction(
        sum(comb(n, j) * numerator**j * (denominator - numerator)**(n - j)
            for j in range(k, n + 1)),
        denominator**n,
    )


def logarithmic_tail(n, p, k):
    """Independent floating evaluation by log-gamma and log-sum-exp."""
    terms = [lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1)
             + j * log(p) + (n - j) * log(1 - p)
             for j in range(k, n + 1)]
    largest = max(terms)
    return exp(largest) * fsum(exp(t - largest) for t in terms)


def check_model():
    for numerator, denominator in ((1, 2), (1, 10)):
        p = Fraction(numerator, denominator)
        # Independent convolution of individual Bernoulli laws, including endpoints.
        pmf = [Fraction(1)]
        for n in range(1, 13):
            next_pmf = [Fraction(0)] * (n + 1)
            for j, mass in enumerate(pmf):
                next_pmf[j] += mass * (1 - p)
                next_pmf[j + 1] += mass * p
            pmf = next_pmf
            for k in range(n + 2):
                assert sum(pmf[k:]) == exact_tail(n, numerator, denominator, k)
        for k in range(100 * numerator // denominator + 1, 101):
            tail = float(exact_tail(100, numerator, denominator, k))
            independent = logarithmic_tail(100, float(p), k)
            assert isclose(tail, independent, rel_tol=2e-12)
            epsilon = float(Fraction(k, 100) - p)
            assert tail <= exp(-200 * epsilon**2) * (1 + 1e-12)
    assert isclose(float(exact_tail(100, 1, 2, 60)), 0.0284439668204904, rel_tol=1e-13)
    assert isclose(float(exact_tail(100, 1, 10, 20)), 0.00197856086577123, rel_tol=1e-13)


def main():
    check_model()
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), sharey=True, layout="constrained")
    for ax, denominator in zip(axes, (2, 10)):
        p = Fraction(1, denominator)
        mean = 100 // denominator
        ks = np.arange(mean + 1, mean + 31)
        epsilons = np.array([float(Fraction(int(k), 100) - p) for k in ks])
        tails = np.array([float(exact_tail(100, 1, denominator, int(k))) for k in ks])
        ax.semilogy(epsilons, np.exp(-200 * epsilons**2), color="#bb5528",
                    lw=2.2, label=r"Hoeffding: $e^{-2n\varepsilon^2}$")
        ax.semilogy(epsilons, tails, "o-", color="#246d99", ms=3.6,
                    lw=1.6, label=r"Exact: $P(K\geq k)$")
        ax.axvline(0.1, color="0.65", ls=":", lw=1)
        ax.set(title=rf"$n=100$, $p=1/{denominator}$",
               xlabel=r"Excess frequency $\varepsilon=k/n-p$", xlim=(0, 0.31),
               ylim=(1e-16, 1))
        ax.grid(axis="y", alpha=0.22)
        ax.legend(loc="lower left", fontsize=9.4)
    axes[0].set_ylabel("Upper-tail probability (log scale)")
    fig.suptitle("Exact binomial tails and Hoeffding bounds", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
