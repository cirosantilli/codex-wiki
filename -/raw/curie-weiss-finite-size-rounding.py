"""Exact finite Curie–Weiss curves; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the matching opaque PNG is written to the current directory.
All curves use finite sums, including the constant diagonal interaction terms.
"""

from itertools import product
from math import comb, exp, fsum, lgamma, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def distribution(n, coupling, field):
    k = np.arange(n + 1)
    spin_sum = 2 * k - n
    log_multiplicity = np.array([
        lgamma(n + 1) - lgamma(int(j) + 1) - lgamma(n - int(j) + 1)
        for j in k
    ])
    log_weights = log_multiplicity + coupling * spin_sum**2 / (2 * n) + field * spin_sum
    shift = float(log_weights.max())
    weights = np.exp(log_weights - shift)
    denominator = float(weights.sum())
    return spin_sum / n, weights / denominator, shift + log(denominator)


def check():
    worst = 0.0
    cases = 0
    # Independent enumeration uses pair products, not grouped squared spin sums.
    for n in (2, 5, 9, 12):
        for coupling, field in ((0.0, 0.0), (0.7, 0.11), (1.5, -0.08)):
            m, p, log_z = distribution(n, coupling, field)
            raw = []
            sums = []
            for spins in product((-1, 1), repeat=n):
                pair_sum = sum(spins[i] * spins[j] for i in range(n) for j in range(i + 1, n))
                s = sum(spins)
                raw.append(exp(coupling * pair_sum / n + coupling / 2 + field * s))
                sums.append(s / n)
            z = fsum(raw)
            errors = (abs(log_z - log(z)), abs(float(m @ p) - fsum(w * s for w, s in zip(raw, sums)) / z), abs(float(p.sum()) - 1))
            worst = max(worst, *errors)
            assert max(errors) < 2e-12
            cases += 1
    # Independent integer multiplicities check normalization for larger sizes.
    for n in (16, 64, 256):
        assert sum(comb(n, k) for k in range(n + 1)) == 2**n
        m, p, _ = distribution(n, 1.5, 0.0)
        assert np.max(np.abs(p - p[::-1])) < 1e-12
        assert abs(float(m @ p)) < 1e-12
    for n in (16, 1024):
        _, p, log_z = distribution(n, 0, 0.13)
        assert abs(log_z - n * np.log(2 * np.cosh(0.13))) < 2e-10
        assert abs(float(p.sum()) - 1) < 1e-12
    m, p, _ = distribution(64, 1.5, 0.01)
    step = 1e-6
    plus = distribution(64, 1.5, 0.01 + step)
    minus = distribution(64, 1.5, 0.01 - step)
    slope = (plus[0] @ plus[1] - minus[0] @ minus[1]) / (2 * step)
    response = 64 * (m**2 @ p - (m @ p)**2)
    assert abs(slope - response) < 1e-6
    return {"enumerated_cases": cases, "max_absolute_error": worst, "response_identity_error": float(abs(slope - response))}


def main():
    print(check())
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained", facecolor="white")
    fields = np.linspace(-0.09, 0.09, 721)
    temperatures = np.linspace(0.65, 1.5, 221)
    for n, color in zip((16, 64, 256, 1024), ("#0072B2", "#D55E00", "#009E73", "#7A5195")):
        means = []
        magnitudes = []
        for u in fields:
            m, p, _ = distribution(n, 1.5, u)
            assert abs(float(p.sum()) - 1) < 1e-12
            means.append(float(m @ p))
        for theta in temperatures:
            m, p, _ = distribution(n, 1 / theta, 0.0)
            assert abs(float(m @ p)) < 1e-11
            magnitudes.append(float(np.abs(m) @ p))
        axes[0].plot(fields, means, color=color, label=f"N = {n}", lw=2)
        axes[1].plot(temperatures, magnitudes, color=color, label=f"N = {n}", lw=2)
    axes[0].axhline(0, color="0.7", lw=0.7)
    axes[0].axvline(0, color="0.7", lw=0.7)
    axes[0].set(title="Field rounding: J/(kBT) = 1.5", xlabel=r"Conjugate field $u=h/(k_BT)$", ylabel=r"Mean magnetization $\langle m\rangle$", ylim=(-1, 1))
    axes[0].set_xticks((-0.08, -0.04, 0, 0.04, 0.08))
    axes[0].legend(loc="upper left", fontsize=10)
    axes[1].axvline(1, color="0.4", ls="--", lw=1)
    axes[1].text(1.025, 0.87, "Limiting critical\ntemperature", color="0.3", fontsize=10)
    axes[1].set(title="Temperature rounding: h = 0", xlabel=r"Temperature $k_BT/J$", ylabel=r"Mean magnitude $\langle |m|\rangle$", ylim=(0, 1))
    axes[1].text(0.05, 0.025, r"$\langle m\rangle=0$ for every finite N", transform=axes[1].transAxes, fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    fig.suptitle("Curie–Weiss model: exact finite sums, not measured data", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
