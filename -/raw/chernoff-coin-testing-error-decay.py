"""Compute finite-binomial optimal errors and compare with their exponent."""

from math import comb, fsum
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def error_probability(n):
    terms = [comb(n, k) * 0.2**k * 0.8**(n-k) for k in range(n//2+1, n+1)]
    if n % 2 == 0:
        terms.append(0.5 * comb(n, n//2) * 0.2**(n//2) * 0.8**(n//2))
    return fsum(terms)


def main():
    n = np.arange(1, 161)
    errors = np.array([error_probability(int(k)) for k in n])
    c = -np.log(0.8)
    bound = 0.5 * np.exp(-c*n)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 4.6), layout="constrained")
    fig.set_facecolor("white")
    left.semilogy(n, errors, color="#186c99", linewidth=2, label="Exact optimal average error")
    left.semilogy(n, bound, color="#af5423", linestyle="--", linewidth=1.7,
                  label="Chernoff bound: ½ exp(−nC)")
    left.set(xlabel="Number n of independent observations", ylabel="Error probability",
             title="Equal-prior coin testing")
    left.legend(frameon=False, fontsize=9.5)
    right.plot(n, -np.log(errors)/n, color="#186c99", linewidth=2,
               label="−ln(exact error) / n")
    right.axhline(c, color="#af5423", linestyle="--", linewidth=1.7,
                  label="Limiting C ≈ 0.22314")
    right.set(xlabel="Number n of independent observations", ylabel="Nats per observation",
              title="Finite exponent approaches the limit", ylim=(0.18, 0.9))
    right.legend(frameon=False, fontsize=10)
    right.text(0.97, 0.96, "n = 1: 1.60944 (above plot)", transform=right.transAxes,
               ha="right", va="top", fontsize=9.5)
    for ax in (left, right):
        ax.set_xlim(1, 160)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    fig.suptitle("Stipulated Bernoulli laws: success probabilities 0.2 and 0.8", fontsize=14)
    assert np.all(errors <= bound * (1 + 1e-12))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
