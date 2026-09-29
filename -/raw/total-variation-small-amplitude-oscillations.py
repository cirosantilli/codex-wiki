"""Plot an original smooth sequence whose uniform norm vanishes but variation does not."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(10, 5.6), dpi=120, facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 3, height_ratios=[1, 1.1])
    t = np.linspace(0, 1, 4097)
    for j, n in enumerate([1, 4, 16]):
        ax = fig.add_subplot(grid[0, j])
        ax.plot(t, np.sin(2 * np.pi * n * t) / n, color="#1565a8", lw=1.5)
        ax.axhline(0, color="#777777", lw=0.6)
        ax.set(xlabel="t", ylabel="fₙ(t)", title=f"n = {n}: amplitude 1/{n}", ylim=(-1.12, 1.12), xlim=(0, 1))
        ax.grid(alpha=0.18)
    ax = fig.add_subplot(grid[1, :])
    ns = np.array([1, 2, 4, 8, 16, 32, 64])
    ax.plot(ns, 4 * np.ones_like(ns), "o-", color="#a54a18", label="Total variation = 4")
    ax.plot(ns, 1 / ns, "o-", color="#1565a8", label="Uniform norm = 1/n")
    ax.set(xscale="log", yscale="log", xlabel="Positive integer n (selected powers of 2)", ylabel="Exact value", title="Smaller height is offset by more oscillations")
    ax.set_xticks(ns, labels=[str(x) for x in ns])
    ax.legend(loc="center right")
    ax.grid(alpha=0.22, which="both")
    fig.suptitle(r"$f_n(t)=\sin(2\pi nt)/n$ on $[0,1]$: uniform convergence does not erase variation", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
