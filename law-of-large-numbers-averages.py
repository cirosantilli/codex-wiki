"""Generate law-of-large-numbers-averages.png in the caller's working directory.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Seeded Bernoulli paths; exact binomial tail sums, evaluated in floating point.
Run from _media with MPLCONFIGDIR set to a writable temporary directory.
"""

from math import lgamma, log
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def binomial_probabilities(n, p):
    counts = np.arange(n + 1)
    log_coefficients = np.fromiter(
        (lgamma(n + 1) - lgamma(int(k) + 1) - lgamma(n - int(k) + 1)
         for k in counts), dtype=float, count=n + 1)
    probabilities = np.exp(log_coefficients + counts * log(p)
                           + (n - counts) * log(1 - p))
    assert np.isclose(probabilities.sum(), 1)
    return counts, probabilities


def main():
    p = 0.2
    tolerance = 0.1
    rng = np.random.default_rng(20261009)
    sizes = np.arange(1, 10001)
    trials = rng.binomial(1, p, size=(4, sizes.size))
    averages = np.cumsum(trials, axis=1) / sizes
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=120,
                             facecolor="white")
    for path, color in zip(averages, ["#2b7bba", "#b24a23", "#23815c", "#805da6"]):
        axes[0].plot(sizes, path, color=color, lw=1.1)
    axes[0].axhline(p, color="#222222", ls="--", lw=1.5, label="True mean p = 0.2")
    axes[0].set(xscale="log", xlim=(1, 10000), ylim=(0, 1),
                xlabel="Number of trials n", ylabel="Running success proportion",
                title="Strong law: four sample paths")
    axes[0].legend(loc="upper right", frameon=False, fontsize=10)
    sample_sizes = np.unique(np.geomspace(10, 1000, 90).astype(int))
    tail_probabilities = []
    for n in sample_sizes:
        counts, probabilities = binomial_probabilities(int(n), p)
        # Exact integer boundary for |K/n - 1/5| >= 1/10.
        outside = np.abs(10 * counts - 2 * n) >= n
        tail_probabilities.append(probabilities[outside].sum())
    axes[1].loglog(sample_sizes, tail_probabilities, color="#2b7bba", lw=2,
                   label="Exact binomial probability")
    bound = np.minimum(1, p * (1 - p) / (sample_sizes * tolerance**2))
    axes[1].loglog(sample_sizes, bound, color="#b24a23", lw=1.7, ls="--",
                   label="Chebyshev upper bound")
    assert np.all(np.asarray(tail_probabilities) <= bound + 1e-12)
    axes[1].set(xlim=(10, 1000), ylim=(1e-14, 1.1),
                xlabel="Number of trials n", ylabel="Probability of error at least 0.1",
                title="Weak law: unlikely fixed-size errors")
    axes[1].legend(loc="lower left", frameon=False, fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle("Law of large numbers: Bernoulli trials, p = 0.2",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.025,
             "Paths illustrate the theorem; the right panel sums exact probabilities, without simulation.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    fig.savefig(Path.cwd() / "law-of-large-numbers-averages.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
