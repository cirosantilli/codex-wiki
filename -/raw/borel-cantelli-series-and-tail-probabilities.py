"""Generate original Borel–Cantelli series and tail curves in the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(1, 10001, dtype=float)
    harmonic = np.cumsum(1 / (n + 1))
    squared = np.cumsum(1 / (n + 1) ** 2)
    m = np.unique(np.geomspace(1, 10000, 360).astype(int))
    # R_m = sum_{k=m+1}^infinity k^{-2}, evaluated from the Basel sum.
    inverse_square_prefix = np.cumsum(1 / np.arange(1, 10001, dtype=float) ** 2)
    tail = np.pi**2 / 6 - inverse_square_prefix[m - 1]
    assert np.all(tail > 0)
    assert np.all(tail <= 1 / m)
    assert np.all(np.diff(tail) < 0)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7), layout="constrained")
    blue, orange, green = "#2463a0", "#b55318", "#237f59"
    axes[0].plot(n, harmonic, color=orange, lw=2.3, label=r"$p_n=1/(n+1)$")
    axes[0].plot(n, squared, color=blue, lw=2.3, label=r"$p_n=1/(n+1)^2$")
    axes[0].axhline(np.pi**2 / 6 - 1, color=blue, lw=1, ls=":")
    axes[0].annotate(r"Limit: $\pi^2/6-1\approx0.645$", xy=(650, 0.645),
                     xytext=(22, 2.5), arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    axes[0].set(title="Finite partial sums", ylabel=r"$S_N=\sum_{n=1}^N p_n$", xlabel="Last index N")
    axes[0].legend(loc="upper left", frameon=False)
    axes[0].set_ylim(0, 9.1)

    axes[1].plot(m, np.ones_like(m), color=green, lw=2.3, label="Independent harmonic: exact")
    axes[1].plot(m, 1 / m, color="#777777", lw=1.4, ls="--", label=r"Squared: upper bound $1/m$")
    axes[1].plot(m, tail, color=blue, lw=2.3, label=r"Squared: union bound $R_m$")
    axes[1].plot(m, 1 / (m + 1), color=orange, lw=2.3, ls=":", label="Shared harmonic: exact")
    axes[1].set(title="An event somewhere at or after m", ylabel="Tail probability or upper bound", xlabel="Starting index m")
    axes[1].set_yscale("log")
    axes[1].set_ylim(0.000065, 2)
    axes[1].legend(loc="lower left", frameon=False, fontsize=9.5)
    for ax in axes:
        ax.set_xscale("log")
        ax.set_xlim(1, 10000)
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Individual probabilities shrink in both models; dependence changes the tail", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
