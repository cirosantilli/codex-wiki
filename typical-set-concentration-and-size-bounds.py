"""Exact binomial sums and typical-set cardinalities; output matching PNG to cwd."""

from fractions import Fraction
from math import comb, log2
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    sizes = [10, 20, 40, 80, 160, 320, 640]
    epsilon = 0.1
    entropy = 2 - 0.75 * log2(3)
    variance = 3 * log2(3) ** 2 / 16
    probabilities, rates, lower_rates = [], [], []
    for n in sizes:
        ks = [k for k in range(n + 1) if abs((2 * n - (n - k) * log2(3)) / n - entropy) <= epsilon]
        cardinality = sum(comb(n, k) for k in ks)
        probability = sum((Fraction(comb(n, k) * 3 ** (n - k), 4**n) for k in ks), Fraction())
        mass = float(probability)
        rate = log2(cardinality) / n
        lower = entropy - epsilon + log2(mass) / n
        assert lower <= rate <= entropy + epsilon
        assert mass >= max(0, 1 - variance / (n * epsilon**2))
        probabilities.append(mass)
        rates.append(rate)
        lower_rates.append(lower)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=120)
    fig.patch.set_facecolor("white")
    ns = np.asarray(sizes)
    axes[0].plot(ns, probabilities, "o-", color="#267e49", label="Exact binomial sum")
    axes[0].plot(ns, np.maximum(0, 1 - variance / (ns * epsilon**2)), "s--", color="#897447", label="Chebyshev lower bound")
    axes[0].axhline(1, color="#888888", linewidth=0.9)
    axes[0].set_ylim(-0.025, 1.08)
    axes[0].set_title("Typical-set probability tends to one")
    axes[0].set_ylabel("P(T₀.₁⁽ⁿ⁾)")
    axes[0].legend(loc="lower right", fontsize=10)
    axes[1].fill_between(ns, lower_rates, entropy + epsilon, color="#267e49", alpha=0.1)
    axes[1].plot(ns, rates, "o-", color="#246c9a", label="Exact log₂ size / n")
    axes[1].plot(ns, lower_rates, "--", color="#267e49", label="Finite lower bound")
    axes[1].axhline(entropy + epsilon, color="#267e49", linestyle="--", linewidth=1.2)
    axes[1].axhline(entropy, color="#888888", linestyle=":", linewidth=1.2)
    axes[1].text(12, entropy + epsilon + 0.005, "H + ε", color="#267e49", fontsize=10)
    axes[1].text(250, entropy - 0.013, "H ≈ 0.811278", color="#777777", fontsize=10)
    axes[1].set_ylim(0.6, 0.95)
    axes[1].set_title("Fixed tolerance leaves a size interval")
    axes[1].set_ylabel("log₂ |T₀.₁⁽ⁿ⁾| / n, bits/symbol")
    axes[1].legend(loc="lower right", fontsize=10)
    for ax in axes:
        ax.set_xscale("log", base=2)
        ax.set_xticks(ns, labels=[str(n) for n in sizes])
        ax.set_xlabel("Block length n")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Biased-coin typical sets: high probability and controlled cardinality", fontsize=16)
    fig.text(0.5, 0.025, "p = 1/4, ε = 0.1 bits/symbol; lower size rate = H − ε + log₂ P(T) / n.", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.8, bottom=0.18, wspace=0.3)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
