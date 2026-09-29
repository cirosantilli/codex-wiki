"""Compare exact Bernstein corner errors with a sufficient probability bound.

Outputs an opaque PNG in the current directory. No experimental data are used.
Tested with the Python, NumPy and Matplotlib versions in pyproject.toml.
"""

from fractions import Fraction
from math import comb, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bernstein_corner(x, n):
    return sum(
        abs(k / n - 0.5) * comb(n, k) * x**k * (1 - x) ** (n - k)
        for k in range(n + 1)
    )


def exact_peak_error(n):
    assert n >= 2 and n % 2 == 0
    return Fraction(comb(n, n // 2), 2 ** (n + 1))


def verify():
    """Check the closed form against an independent exact binomial sum."""
    for n in range(2, 202, 2):
        direct = sum(Fraction(comb(n, k), 2**n) * abs(Fraction(k, n) - Fraction(1, 2))
                     for k in range(n + 1))
        assert direct == exact_peak_error(n)
        assert float(direct) <= 1 / (2 * sqrt(n))
    assert exact_peak_error(2) == Fraction(1, 4)
    assert exact_peak_error(4) == Fraction(3, 16)


def main():
    verify()
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120, layout="constrained")
    fig.set_facecolor("white")
    x = np.linspace(0, 1, 1601)
    for n, color in zip((2, 10, 50, 200), ("#cc6677", "#e69f00", "#0072b2", "#009e73")):
        axes[0].plot(x, bernstein_corner(x, n) - abs(x - 0.5), color=color,
                     linewidth=1.7, label=rf"$n={n}$")
    axes[0].set(xlim=(0, 1), ylim=(-0.006, 0.265), xlabel=r"$x$", ylabel="Approximation error",
                title="Largest error at the corner")
    axes[0].legend(fontsize=10)
    ns = np.arange(2, 202, 2)
    peaks = np.array([float(exact_peak_error(int(n))) for n in ns])
    axes[1].loglog(ns, peaks, color="#0072b2", linewidth=2, label="Exact maximum error (even n)")
    axes[1].loglog(ns, 1 / (2 * np.sqrt(ns)), "--", color="#cc6677", linewidth=2,
                   label=r"Sufficient bound $1/(2\sqrt{n})$")
    axes[1].set(xlabel=r"Polynomial degree $n$", ylabel="Maximum error",
                title="Probability supplies an error guarantee")
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.22, which="both")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
