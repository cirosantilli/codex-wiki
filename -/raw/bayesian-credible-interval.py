"""Plot two exact-CDF beta credible intervals; tested with Python 3.14.4.

Only NumPy, Matplotlib, and the standard library are required. The CDF is
the analytically integrated polynomial density, evaluated in a positive
Bernstein basis to avoid cancellation near one. Quantiles use bisection,
not SciPy or integration of a sampled plot. Output is written to cwd.
"""

from math import comb, fsum
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def posterior_density(theta):
    return 2860 * theta**9 * (1 - theta)**3


def posterior_cdf(theta):
    """CDF of Beta(10,4), equal to 286t^10-780t^11+715t^12-220t^13.

    The binomial-tail polynomial has derivative 2860t^9(1-t)^3
    and is zero at t=0, so it is the same antiderivative.
    """
    if not 0 <= theta <= 1:
        raise ValueError("theta must lie in [0, 1]")
    return fsum(comb(13, j) * theta**j * (1 - theta)**(13 - j)
                for j in range(10, 14))


def posterior_quantile(probability):
    """Invert the exact polynomial CDF by 60 bisection steps."""
    if not 0 <= probability <= 1:
        raise ValueError("probability must lie in [0, 1]")
    if probability in (0, 1):
        return float(probability)
    low, high = 0.0, 1.0
    for _ in range(60):
        middle = (low + high) / 2
        if posterior_cdf(middle) < probability:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 13})
    lower = posterior_quantile(0.025)
    upper = posterior_quantile(0.975)
    one_sided = posterior_quantile(0.95)
    theta = np.linspace(0, 1, 2001)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.1), dpi=120,
                             facecolor="white", sharey=True)
    intervals = [(lower, upper, "Equal-tailed 95% interval",
                  "2.5% in each excluded tail"),
                 (0, one_sided, "One-sided 95% upper bound",
                  "5% in the excluded right tail")]
    for ax, (left, right, title, tail_note) in zip(axes, intervals):
        ax.plot(theta, posterior_density(theta), color="#007c68", lw=2.6)
        inside = np.linspace(left, right, 1001)
        ax.fill_between(inside, posterior_density(inside),
                        color="#56b4a4", alpha=0.5)
        for endpoint in (left, right):
            ax.vlines(endpoint, 0, posterior_density(endpoint),
                      color="#005848", linestyle="--", lw=1.5)
        ax.text(0.04, 0.94, f"[{left:.6f}, {right:.6f}]\n{tail_note}",
                transform=ax.transAxes, fontsize=11, va="top")
        ax.text(0.61, 1.15, "Shaded area\n= 0.95", fontsize=12, ha="center")
        ax.set(xlim=(0, 1), ylim=(0, 4.1), title=title,
               xlabel="Unknown heads probability θ")
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Posterior probability density")
    fig.suptitle("Same Beta(10, 4) posterior; two different 95% ranges", fontsize=16)
    fig.text(0.5, 0.035,
             "Endpoints solve the exact polynomial CDF. "
             "Both shaded regions contain 95% posterior probability.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.07, right=0.975, bottom=0.17,
                        top=0.79, wspace=0.14)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Equal-tailed: [{lower:.12f}, {upper:.12f}], "
          f"mass={posterior_cdf(upper) - posterior_cdf(lower):.15f}")
    print(f"One-sided: [0, {one_sided:.12f}], "
          f"mass={posterior_cdf(one_sided):.15f}")


if __name__ == "__main__":
    main()
