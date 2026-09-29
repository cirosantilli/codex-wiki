"""Exact unit-step endpoint PMFs, using math.comb rather than SciPy.

Tested with Python 3.14 and the root pyproject NumPy/Matplotlib environment.
Run through make _media/random-walk-endpoint-distributions.png; output to CWD.
"""

from math import comb, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def endpoint_pmf(n, p):
    endpoints = 2 * np.arange(n + 1) - n
    masses = np.array([comb(n, b) * p**b * (1 - p)**(n - b)
                       for b in range(n + 1)])
    mean = n * (2 * p - 1)
    variance = 4 * n * p * (1 - p)
    assert np.isclose(masses.sum(), 1, atol=1e-14, rtol=0)
    assert np.isclose(endpoints @ masses, mean, atol=1e-12, rtol=0)
    assert np.isclose((endpoints - mean)**2 @ masses, variance,
                      atol=1e-12, rtol=0)
    assert np.all((endpoints - n) % 2 == 0)
    return endpoints, masses


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    cases = [(20, 0.5, "#2274a5"), (80, 0.5, "#43876d"),
             (80, 0.65, "#d27727")]
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.4), dpi=120,
                             facecolor="white", sharey=True)
    for ax, (n, p, color) in zip(axes, cases):
        endpoints, masses = endpoint_pmf(n, p)
        mean = n * (2 * p - 1)
        variance = 4 * n * p * (1 - p)
        sigma = sqrt(variance)
        ax.vlines(endpoints, 0, masses, color=color, lw=1.3)
        ax.scatter(endpoints, masses, color=color, s=11, zorder=3)
        ax.axvline(mean, color="#182b40", ls="--", lw=1.5)
        ax.plot([mean - sigma, mean + sigma], [0.196, 0.196],
                color="#182b40", lw=2, marker="|", markersize=10)
        ax.text(mean, 0.203, r"Mean $\pm$ one SD", ha="center", fontsize=9)
        ax.text(0.04, 0.74,
                f"Mean = {mean:g}\nVariance = {variance:g}\nSD = {sigma:.3f}",
                transform=ax.transAxes, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
        ax.set(title=f"n = {n}, p = {p:.2f}", xlabel=r"Endpoint $s$ (even integers)",
               xlim=(-n - 2, n + 2), ylim=(0, 0.228))
        ax.set_xticks(np.linspace(-n, n, 5, dtype=int))
        ax.grid(axis="y", color="#edf0f3")
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
        print(f"n={n}, p={p}: mass={masses.sum():.16g}, "
              f"mean={endpoints @ masses:.12g}, variance={variance:.12g}, "
              f"SD={sigma:.9f}, SD/n={sigma/n:.9f}, spacing/SD={2/sigma:.9f}")
    axes[0].set_ylabel(r"Probability $P(S_n=s)$")
    fig.suptitle("Exact endpoint probabilities: spread, drift, and parity", fontsize=16)
    fig.text(0.5, 0.06,
             "Full support shown: -n, -n+2, ..., n. Odd endpoints have probability zero.\n"
             "Stems show binomial masses, not a continuous density or simulation histogram.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.22, top=0.83, wspace=0.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
