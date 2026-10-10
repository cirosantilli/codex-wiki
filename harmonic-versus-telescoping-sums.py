"""Compare vanishing terms and divergent/convergent partial sums; PNG to CWD."""

from pathlib import Path
from math import fsum

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    n = np.arange(1, 10001, dtype=float)
    harmonic_terms = 1 / n
    telescoping_terms = 1 / (n * (n + 1))
    harmonic_sums = np.cumsum(harmonic_terms)
    telescoping_sums = n / (n + 1)
    for count in [10, 100, 1000, 10000]:
        assert abs(harmonic_sums[count - 1] - fsum(1 / k for k in range(1, count + 1))) < 5e-13
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5.3), dpi=100)
    left.loglog(n, harmonic_terms, color="#246bce", linewidth=2.5,
                label=r"Harmonic: $1/n$")
    left.loglog(n, telescoping_terms, color="#bf5520", linewidth=2.5,
                label=r"Telescoping: $1/[n(n+1)]$")
    left.set(xlabel="Term index n", ylabel="Term magnitude", xlim=(1, 10000))
    left.set_title("Both individual terms tend to zero", fontsize=13, weight="bold")
    left.grid(which="both", alpha=0.16)
    left.legend(frameon=False, fontsize=11)
    right.semilogx(n, harmonic_sums, color="#246bce", linewidth=2.5,
                   label=r"Harmonic sum $H_N$")
    right.semilogx(n, np.log(n), color="#69747d", linestyle="--", linewidth=1.7,
                   label=r"Lower comparison $\log N$")
    right.semilogx(n, telescoping_sums, color="#bf5520", linewidth=2.5,
                   label=r"Telescoping sum $N/(N+1)$")
    right.axhline(1, color="#bf5520", linestyle=":", linewidth=1.5)
    for count in [10, 100, 1000, 10000]:
        value = harmonic_sums[count - 1]
        right.scatter([count], [value], color="#246bce", s=25, zorder=5)
        right.annotate(f"{value:.3f}", (count, value),
                       xytext=(-5, 12) if count == 10000 else (2, 12),
                       textcoords="offset points",
                       ha="right" if count == 10000 else "left", fontsize=10)
    right.set(xlabel="Number of terms N", ylabel="Partial sum",
              xlim=(1, 14000), ylim=(0, 11))
    right.set_title("Their accumulated totals behave differently",
                    fontsize=13, weight="bold")
    right.grid(alpha=0.2)
    right.legend(loc="upper left", frameon=False, fontsize=10)
    fig.suptitle("Small next terms do not decide whether an infinite sum is finite",
                 fontsize=16, weight="bold", y=0.975)
    fig.subplots_adjust(left=0.07, right=0.975, bottom=0.14, top=0.80, wspace=0.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
