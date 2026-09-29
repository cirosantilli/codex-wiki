"""Exact coin type-class masses and a divergence bound, not measured data."""

from math import comb, exp, log
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def divergence(q, p):
    return ((q * log(q / p)) if q else 0.0) + (
        ((1 - q) * log((1 - q) / (1 - p))) if q != 1 else 0.0)


def main():
    n, p = 40, 0.25
    q = [k / n for k in range(n + 1)]
    masses = [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]
    upper = [exp(-n * divergence(x, p)) for x in q]
    assert abs(sum(masses) - 1) < 1e-12
    assert all(a <= b * (1 + 1e-12) for a, b in zip(masses, upper))
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=120, facecolor="white")
    ax.semilogy(q, upper, "--", color="#ce7b19", linewidth=2,
        label=r"Upper bound $e^{-40D_e(q\Vert p)}$")
    ax.semilogy(q, masses, "o-", color="#245b90", markersize=3.8,
        label=r"Exact class mass $\binom{40}{k}p^k(1-p)^{40-k}$")
    ax.axvline(p, color="#47755d", alpha=0.5, linewidth=1)
    ax.annotate("Source law p = 1/4\nClass mass ≈ 0.144; bound = 1", xy=(p, masses[10]),
        xytext=(0.05, 0.003), fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "#47755d"})
    ax.annotate("20 ones: q = 1/2\nExact mass ≈ 0.000398", xy=(0.5, masses[20]),
        xytext=(0.48, 0.015), fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "#245b90"})
    ax.set(xlabel="Observed fraction of ones q = k/40", ylabel="Probability (logarithmic scale)",
        xlim=(-0.015, 1.015), ylim=(1e-25, 2),
        title="An unusual empirical distribution costs relative entropy")
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", fontsize=10)
    fig.text(0.5, 0.02, "Synthetic independent-coin model; each point is one class, not a tail probability.",
        ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
