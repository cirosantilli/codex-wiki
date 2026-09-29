"""Plot exact stipulated Bernoulli comparisons; tested with Python 3.14.4.

Run from _media; writes its matching PNG to the current directory.
No observations or random simulations are used.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    heads = np.arange(11)
    factors = np.array([
        float(Fraction(7, 4)**int(k) * Fraction(1, 2)**int(10-k))
        for k in heads
    ])
    bf = factors[8]
    prior = Fraction(1, 9)
    posterior = bf * float(prior)
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.4, 4.9), dpi=120, facecolor="white"
    )
    fig.suptitle("Ten Bernoulli trials: H₀ has p = 0.4, H₁ has p = 0.7",
                 fontsize=15, y=0.98)
    left.semilogy(heads, factors, "o-", color="#176eaa", lw=2, ms=5)
    left.axhline(1, color="#69757c", lw=1.2, linestyle="--")
    left.scatter([8], [bf], color="#ce5900", s=65, zorder=5)
    left.annotate(f"8 heads: BF₁₀ = {bf:.5f}", xy=(8, bf),
                  xytext=(2.1, 58), fontsize=11, color="#a54600",
                  arrowprops={"arrowstyle": "->", "color": "#a54600"})
    left.text(0.5, 1.6, "favors H₁", color="#53616b", fontsize=10)
    left.text(0.5, 0.36, "favors H₀", color="#53616b", fontsize=10)
    left.set(xlim=(-0.2, 10.2), ylim=(0.0006, 700), xticks=range(0, 11, 2),
             xlabel="Number of heads k (out of 10)",
             ylabel="BF₁₀ = (0.7/0.4)ᵏ (0.3/0.6)¹⁰⁻ᵏ  [log scale]",
             title="Evidence for every possible heads count")
    odds = np.geomspace(0.003, 3, 200)
    right.loglog(odds, bf * odds, color="#176eaa", lw=2.4,
                 label=f"Posterior odds = {bf:.5f} × prior odds")
    right.loglog(odds, odds, color="#89939a", lw=1.4, linestyle="--",
                 label="Unchanged odds (BF = 1)")
    right.axhline(1, color="#69757c", lw=1, linestyle=":")
    right.scatter([float(prior)], [posterior], color="#ce5900", s=65, zorder=5)
    right.annotate("Prior P(H₁) = 0.1\nOdds: 1/9 → 2.44344\nPosterior P(H₁ | D) = 0.70959",
                   xy=(float(prior), posterior), xytext=(0.007, 10.5),
                   fontsize=10.5, color="#a54600",
                   arrowprops={"arrowstyle": "->", "color": "#a54600"})
    right.set(xlim=(0.003, 3), ylim=(0.003, 90),
              xlabel="Prior odds H₁ : H₀  [log scale]",
              ylabel="Posterior odds H₁ : H₀  [log scale]",
              title="Hold the eight-head result fixed")
    right.legend(loc="lower right", fontsize=8.5, framealpha=1)
    for ax in (left, right):
        ax.grid(color="#e4e9ec", which="major")
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.035,
             "Calculated model quantities, not observed frequencies. Both point models are fixed before the data.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.17,
                        top=0.83, wspace=0.33)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
