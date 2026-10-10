"""Generate binomial-count-distribution.png in the caller's working directory.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../binomial-count-distribution.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All probabilities are calculated directly; no simulations are used.
"""

from math import comb, isclose, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n, p = 10, 0.3
    counts = np.arange(n + 1)
    masses = np.array([comb(n, k) * p**k * (1 - p)**(n - k)
                       for k in range(n + 1)])
    mean = float(np.dot(counts, masses))
    variance = float(np.dot((counts - mean)**2, masses))
    assert isclose(float(masses.sum()), 1, abs_tol=1e-14)
    assert isclose(mean, 3, abs_tol=1e-13)
    assert isclose(variance, 2.1, abs_tol=1e-13)
    assert isclose(float(masses[3]), 0.266827932, abs_tol=1e-14)
    assert isclose(float(masses[0]), 0.0282475249, abs_tol=1e-14)
    assert int(np.argmax(masses)) == 3

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=120, facecolor="white")
    colors = ["#c65c24" if k == 3 else "#287ba5" for k in counts]
    ax.bar(counts, masses, color=colors, width=0.72, zorder=3)
    ax.annotate(f"Exactly 3 successes\nP(K = 3) = {masses[3]:.7f}",
                xy=(3, masses[3]), xytext=(5.0, 0.26),
                arrowprops={"arrowstyle": "->", "color": "#333333"},
                fontsize=11, ha="left", va="center")
    ax.text(0.97, 0.61, "Mean = 3\nVariance = 2.1\nStandard deviation = 1.4491",
            transform=ax.transAxes, ha="right", va="top",
            bbox={"facecolor": "white", "edgecolor": "#cccccc", "pad": 8})
    ax.set(title="Ten independent trials, success probability 0.3",
           xlabel="Success count k", ylabel="Probability P(K = k)",
           xticks=counts, xlim=(-0.6, 10.6), ylim=(0, 0.32))
    ax.grid(axis="y", alpha=0.2, zorder=0)
    fig.text(0.5, 0.025, "Exact binomial masses; all eleven bars sum to 1.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    destination = Path.cwd() / "binomial-count-distribution.png"
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"PMF sum = {masses.sum():.15f}; mean = {mean:.12f}; variance = {variance:.12f}")
    print(f"P(K=3) = {masses[3]:.12f}; P(K>=1) = {1-masses[0]:.12f}; sd = {sqrt(variance):.12f}")
    print(f"Saved {destination}")


if __name__ == "__main__":
    main()
