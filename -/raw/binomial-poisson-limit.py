"""Generate binomial-poisson-limit.png in the caller's working directory.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../binomial-poisson-limit.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uses exact binomial formula and Poisson recursion, never sampled counts.
"""

from math import comb, exp, isclose
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def binomial_masses(n, p):
    return np.array([comb(n, k) * p**k * (1-p)**(n-k)
                     for k in range(n+1)])


def poisson_masses(parameter, maximum):
    masses = np.empty(maximum + 1)
    masses[0] = exp(-parameter)
    for k in range(1, maximum + 1):
        masses[k] = masses[k-1] * parameter / k
    return masses


def main():
    parameter = 3.0
    reference = poisson_masses(parameter, 200)
    counts = np.arange(len(reference))
    assert isclose(float(reference.sum()), 1, abs_tol=1e-14)
    assert isclose(float(np.dot(counts, reference)), parameter, abs_tol=1e-13)
    assert isclose(float(np.dot((counts-parameter)**2, reference)), parameter, abs_tol=1e-13)
    assert isclose(float(reference[3]), 4.5*exp(-3), abs_tol=1e-14)
    visible_counts = np.arange(13)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(10, 4.3), dpi=120,
                             facecolor="white", sharex=True, sharey=True)
    for ax, n in zip(axes, [10, 50, 200]):
        p = parameter / n
        masses = binomial_masses(n, p)
        all_counts = np.arange(n+1)
        mean = float(np.dot(all_counts, masses))
        variance = float(np.dot((all_counts-mean)**2, masses))
        assert isclose(float(masses.sum()), 1, abs_tol=3e-14)
        assert isclose(mean, parameter, abs_tol=1e-12)
        assert isclose(variance, parameter*(1-p), abs_tol=1e-12)
        plotted_masses = np.zeros(len(visible_counts))
        plotted_masses[:min(n+1, len(visible_counts))] = masses[:len(visible_counts)]
        ax.bar(visible_counts, plotted_masses, width=0.7, color="#287ba5",
               alpha=0.75, label="Exact binomial mass", zorder=2)
        ax.plot(visible_counts, reference[:len(visible_counts)], "o",
                color="#c65c24", markersize=5.5, markerfacecolor="white",
                markeredgewidth=1.7, label="Poisson(3) mass", zorder=3)
        ax.set(title=f"n = {n},  p = {p:g}", xlabel="Success count k",
               xlim=(-0.7, 12.7), ylim=(0, 0.31), xticks=np.arange(0, 13, 2))
        ax.grid(axis="y", alpha=0.2, zorder=0)
        ax.text(0.95, 0.91, f"Mean = 3\nVariance = {variance:.3f}",
                transform=ax.transAxes, ha="right", va="top", fontsize=10)
        tail = float(masses[13:].sum())
        assert tail < 2e-5
        print(f"n={n}, p={p:g}: PMF sum={masses.sum():.15f}, mean={mean:.12f}, "
              f"variance={variance:.12f}, P(K=3)={masses[3]:.12f}, omitted k>12 mass={tail:.3g}")
    axes[0].set_ylabel("Probability mass at k")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=2, loc="lower center", frameon=False,
               bbox_to_anchor=(0.5, 0.052))
    fig.suptitle("Rare-event limit: more trials, smaller p, fixed mean np = 3",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.014, "All panels use the same axes. Counts above 12 have total mass below 0.00002 in every law.",
             ha="center", fontsize=9)
    assert float(reference[13:].sum()) < 2e-5
    fig.tight_layout(rect=(0, 0.13, 1, 0.91))
    destination = Path.cwd() / "binomial-poisson-limit.png"
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Poisson(3): P(N=0)={reference[0]:.12f}, P(N=3)={reference[3]:.12f}, "
          f"P(N>=1)={1-reference[0]:.12f}, omitted k>12 mass={reference[13:].sum():.3g}")
    print(f"Saved {destination}")


if __name__ == "__main__":
    main()
