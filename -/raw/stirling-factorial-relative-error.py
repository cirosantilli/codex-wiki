"""Relative errors for factorial estimates; opaque PNG written to CWD.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from math import exp, factorial, log, pi
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(1, 101)
    log_s = 0.5 * np.log(2 * pi * n) + n * (np.log(n) - 1)
    # The reference is the exact integer factorial, rather than a second
    # asymptotic approximation or a gamma-library approximation.
    log_exact = np.array([log(factorial(int(k))) for k in n])
    leading = np.abs(np.expm1(log_s - log_exact))
    corrected = np.abs(np.expm1(log_s + np.log1p(1 / (12 * n)) - log_exact))
    assert np.all(corrected < leading)
    assert np.isclose(leading[9], 0.008295960443936, atol=1e-12)
    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=130)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.loglog(n, leading, color="#2768a6", lw=2.3,
              label=r"Leading estimate $S_n$")
    ax.loglog(n, corrected, color="#238367", lw=2.3,
              label=r"Corrected estimate $S_n(1+1/(12n))$")
    ax.scatter([10], [leading[9]], color="#2768a6", zorder=4)
    ax.scatter([10], [corrected[9]], color="#238367", zorder=4)
    ax.annotate("n = 10: 0.830%", (10, leading[9]), (2, 0.02),
                arrowprops={"arrowstyle": "->", "color": "#2768a6"},
                color="#2768a6", fontsize=11)
    ax.annotate("n = 10: 0.003176%", (10, corrected[9]), (2, 2e-6),
                arrowprops={"arrowstyle": "->", "color": "#238367"},
                color="#238367", fontsize=11)
    ax.set(xlim=(1, 100), ylim=(1e-7, 0.15), xlabel="Positive integer n",
           ylabel=r"Relative error $|\mathrm{estimate}/n!-1|$",
           title="A first correction substantially improves Stirling's formula")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.grid(which="both", alpha=0.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
