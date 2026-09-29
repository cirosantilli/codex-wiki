"""Exact finite Ising boundaries; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the matching opaque PNG is written to the current directory.
The open chain has N-1 bonds and the periodic ring has N bonds, with N >= 3.
"""

from itertools import product
from math import exp, fsum, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def log_partition(n, coupling, periodic):
    bulk = n * np.log(2 * np.cosh(coupling))
    if periodic:
        return bulk + np.log1p(np.tanh(coupling)**n)
    return bulk - np.log(np.cosh(coupling))


def check():
    worst = 0.0
    cases = 0
    for n in (3, 4, 7, 11):
        for coupling in (0.0, 0.3, 0.8, 1.6):
            transfer = np.array([[exp(coupling), exp(-coupling)], [exp(-coupling), exp(coupling)]])
            for periodic in (False, True):
                # Direct microstate enumeration, independently of transfer eigenvalues.
                weights = []
                for spins in product((-1, 1), repeat=n):
                    bonds = sum(spins[i] * spins[i + 1] for i in range(n - 1))
                    if periodic:
                        bonds += spins[-1] * spins[0]
                    weights.append(exp(coupling * bonds))
                z = fsum(weights)
                matrix_z = np.trace(np.linalg.matrix_power(transfer, n)) if periodic else np.ones(2) @ np.linalg.matrix_power(transfer, n - 1) @ np.ones(2)
                errors = (abs(log(z) - log_partition(n, coupling, periodic)), abs(matrix_z / z - 1), abs(fsum(w / z for w in weights) - 1))
                worst = max(worst, *errors)
                assert max(errors) < 3e-12
                cases += 1
    return {"enumerated_cases": cases, "max_absolute_error": float(worst), "checks": "direct sum, transfer-matrix power, probability normalization"}


def main():
    print(check())
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    coupling = 0.8
    n = np.arange(3, 81)
    bulk_g = -np.log(2 * np.cosh(coupling))
    open_g = -log_partition(n, coupling, False) / n
    ring_g = -log_partition(n, coupling, True) / n
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained", facecolor="white")
    axes[0].plot(1 / n, open_g, "o-", ms=3, color="#0072B2", label="Open chain (N − 1 bonds)")
    axes[0].plot(1 / n, ring_g, "s-", ms=3, color="#D55E00", label="Periodic ring (N bonds)")
    axes[0].axhline(bulk_g, color="0.4", ls="--", label=r"Limit $g_\infty$ (reference)")
    axes[0].set(title="The same bulk limit", xlabel="Inverse number of spins 1/N", ylabel=r"$g_N=F_N/(Nk_BT)$", xlim=(0, 0.34))
    axes[0].legend(fontsize=9, loc="upper left")
    axes[1].plot(n, n * (open_g - bulk_g), "o-", ms=3, color="#0072B2", label="Open chain")
    axes[1].plot(n, n * (ring_g - bulk_g), "s-", ms=3, color="#D55E00", label="Periodic ring")
    axes[1].axhline(0, color="0.6", lw=0.8)
    axes[1].text(22, 0.315, r"$\log\cosh K$: constant boundary term", fontsize=10, color="#0072B2")
    axes[1].text(17, -0.07, r"$-\log[1+(\tanh K)^N]\to0$", fontsize=10, color="#D55E00")
    axes[1].set(title="Expose the total correction", xlabel="Number of spins N", ylabel=r"$N(g_N-g_\infty)$", ylim=(-0.27, 0.4), xlim=(2, 81))
    fig.suptitle("Finite Ising chain and ring: exact sums at J/(kBT) = 0.8", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
