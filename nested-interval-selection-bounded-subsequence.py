"""Exact nested-interval selection from a specified alternating sequence.

This uses knowledge of the model's limit, not a claim to decide an arbitrary
infinite input sequence by inspecting finitely many terms. Outputs to cwd.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def selection(steps=8):
    a, b = Fraction(-1), Fraction(2)
    last = 0
    rows = []
    for j in range(1, steps + 1):
        mid = (a + b) / 2
        # Every interval chosen here has upper endpoint > 1, so infinitely
        # many even-indexed terms 1+1/(n+1) belong to it.
        if mid < 1:
            a = mid
        else:
            b = mid
        n = last + 1
        while n % 2 or not a <= 1 + Fraction(1, n + 1) <= b:
            n += 1
        x = 1 + Fraction(1, n + 1)
        assert a <= 1 <= x <= b and n > last
        assert b - a == Fraction(3, 2**j)
        assert abs(x - 1) <= b - a
        rows.append((j, a, b, n, x))
        last = n
    return rows


def main():
    rows = selection()
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=120, layout="constrained")
    fig.set_facecolor("white")
    for j, a, b, n, x in rows:
        axes[0].plot((float(a), float(b)), (j, j), color="#0072b2", linewidth=5,
                     solid_capstyle="butt", alpha=0.62)
        axes[0].scatter([float(x)], [j], color="#d55e00", s=32, zorder=4)
        axes[0].text(2.05, j, rf"$n_{j}={n}$", va="center", fontsize=10)
    axes[0].axvline(1, color="#555555", linestyle="--", linewidth=1)
    axes[0].set(xlim=(0.45, 2.58), ylim=(8.7, 0.3), xlabel="Interval position / selected value",
                ylabel=r"Bisection step $j$", title="Nested halves and increasing indices")
    axes[0].set_yticks(range(1, 9))
    js = np.array([r[0] for r in rows])
    errors = np.array([float(r[4] - 1) for r in rows])
    widths = np.array([float(r[2] - r[1]) for r in rows])
    axes[1].semilogy(js, widths, "o--", color="#0072b2", label=r"Interval length $3/2^j$")
    axes[1].semilogy(js, errors, "o-", color="#d55e00", label=r"Selected error $|x_{n_j}-1|$")
    axes[1].set(xlabel=r"Bisection step $j$", ylabel="Length / absolute error",
                title="Shrinking enclosure certifies convergence")
    axes[1].set_xticks(range(1, 9))
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
