"""Original positive-tail/work comparison, without subtracting rounded sums.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; output to CWD.
The tails are accumulated relative to their first term in logarithmic form.
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def log10_bound(b, n, scale):
    """Log of scale * B_n(b), evaluated without underflow."""
    return (math.log(2 * scale) - math.pi * b * (n + 1) ** 2
            - math.log(-math.expm1(-math.pi * b * (2 * n + 3)))) / math.log(10)


def log10_tail(b, n, scale):
    """Log of positive tail; the discarded normalized tail is < exp(-745)."""
    start = n + 1
    normalized = []
    index = start
    while True:
        exponent = -math.pi * b * (index ** 2 - start ** 2)
        if exponent < -745:
            break
        normalized.append(math.exp(exponent))
        index += 1
    return (math.log(2 * scale) - math.pi * b * start ** 2
            + math.log(math.fsum(normalized))) / math.log(10)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.1), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, a in zip(axes, (0.04, 25.0)):
        # The broad side is shown across work budgets; the narrow side already
        # meets the requested tolerance at n=0, so only that point is relevant.
        broad_label = "Physical" if a < 1 else "Dual"
        narrow_label = "Dual" if a < 1 else "Physical"
        broad_scale = 1.0 if a < 1 else a ** -0.5
        narrow_scale = a ** -0.5 if a < 1 else 1.0
        broad_color = "#1864ab" if a < 1 else "#b45b08"
        narrow_color = "#b45b08" if a < 1 else "#1864ab"
        n = np.arange(16)
        work = 2 * n + 1
        bounds = [log10_bound(0.04, int(j), broad_scale) for j in n]
        tails = [log10_tail(0.04, int(j), broad_scale) for j in n]
        ax.plot(work, bounds, "--", color=broad_color,
                label=f"{broad_label}: rigorous bound")
        ax.plot(work, tails, "o-", markersize=3.5, color=broad_color,
                label=f"{broad_label}: positive tail")
        narrow = log10_bound(25.0, 0, narrow_scale)
        ax.scatter([1], [narrow], color=narrow_color, marker="D", s=65,
                   label=f"{narrow_label}: bound, zero term only", zorder=4)
        ax.annotate(f"{narrow_label}: one term", xy=(1, narrow),
                    xytext=(5, narrow + 3.2), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": narrow_color})
        first = next(i for i, value in enumerate(bounds) if value < -12)
        ax.annotate(f"{work[first]} terms", xy=(work[first], bounds[first]),
                    xytext=(work[first] - 9, -19), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": broad_color})
        ax.axhline(-12, color="#555555", linestyle=":", label=r"Tolerance $10^{-12}$")
        ax.set(xlim=(0, 33), ylim=(-36, 1), xticks=(1, 5, 9, 13, 17, 21, 25, 29, 31),
               xlabel=r"Retained lattice points ($2N+1$)",
               ylabel=r"$\log_{10}$(absolute truncation error or bound)",
               title=f"Approximating S({a:g})")
        ax.grid(alpha=0.16)
        ax.legend(loc="upper right", fontsize=8.5)
    fig.suptitle("Choose the narrow Gaussian sum to save work", fontsize=15)
    fig.supxlabel("Positive tails are summed directly in logarithmic form; "
                  "rounding error is excluded.\nEven symmetry needs only N+1 distinct exponential evaluations.",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
