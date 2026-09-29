"""Generate brownian-quadratic-variation.png in the caller's working directory.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Nested partitions reuse finite Gaussian samples; Monte Carlo uses fresh grids.
Run from _media: MPLCONFIGDIR=/tmp/brownian-mpl python3 ../brownian-quadratic-variation.py
"""

from math import sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    seed, horizon, finest = 20261011, 1.0, 16384
    rng = np.random.default_rng(seed)
    increments = rng.normal(0.0, sqrt(horizon / finest), size=(3, finest))
    paths = np.column_stack((np.zeros(3), np.cumsum(increments, axis=1)))
    sizes = 2 ** np.arange(2, 15)
    qv = np.empty((3, len(sizes)))
    for j, n in enumerate(sizes):
        coarse_increments = np.diff(paths[:, ::finest // int(n)], axis=1)
        qv[:, j] = np.sum(coarse_increments ** 2, axis=1)
        assert np.allclose(coarse_increments,
                           increments.reshape(3, int(n), -1).sum(axis=2))
    smooth_qv = horizon ** 2 / sizes  # f(t)=t, computed on the same partitions

    trials = 4096
    mc_sizes = 2 ** np.arange(2, 12)
    empirical_rmse = []
    for n in mc_sizes:
        samples = rng.normal(0.0, sqrt(horizon / n), size=(trials, int(n)))
        sums = np.sum(samples ** 2, axis=1)
        empirical_rmse.append(sqrt(np.mean((sums - horizon) ** 2)))
        # Broad Monte Carlo checks; exact formulas are printed separately.
        assert abs(sums.mean() - horizon) < 6 * horizon * sqrt(2 / (n * trials))
        ratio = sums.var(ddof=1) / (2 * horizon ** 2 / n)
        assert 0.85 < ratio < 1.15
    empirical_rmse = np.asarray(empirical_rmse)
    theoretical_rmse = horizon * np.sqrt(2 / mc_sizes)
    assert np.all(np.abs(empirical_rmse / theoretical_rmse - 1) < 0.08)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120,
                             facecolor="white")
    for i, color in enumerate(["#2878ad", "#c05a2a", "#24805e"]):
        axes[0].plot(sizes, qv[i], "o-", color=color, markersize=3,
                     label=f"Sample {i+1}")
    axes[0].axhline(horizon, color="#333333", ls="--", label="Brownian limit T = 1")
    axes[0].plot(sizes, smooth_qv, ":", color="#8655a4", lw=2,
                 label=r"Smooth path $f(t)=t$: $Q_n=1/n$")
    axes[0].set(xscale="log", xlabel="Number of intervals n",
                ylabel=r"$Q_n=\sum_k (\Delta B_k)^2$",
                title="Three finite samples, nested uniform grids", ylim=(0, max(1.5, qv.max()*1.12)))
    axes[0].legend(fontsize=8.5, loc="upper right")
    axes[1].loglog(mc_sizes, theoretical_rmse, color="#333333", lw=2,
                   label=r"Exact RMS error $T\sqrt{2/n}$")
    axes[1].loglog(mc_sizes, empirical_rmse, "o", color="#2878ad", markersize=5,
                   label="Monte Carlo RMS error")
    axes[1].set(xlabel="Number of intervals n", ylabel=r"RMS error of $Q_n$ about T",
                title="Error shrinks as the grid is refined")
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.17, which="both")
    fig.suptitle("Brownian quadratic variation on [0, 1]")
    fig.text(0.5, 0.025,
             f"Seed {seed}; largest nested grid: 16,384 intervals. "
             f"Monte Carlo: {trials:,} independent samples per grid size.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.055, 1, 0.94))
    fig.savefig(Path.cwd() / "brownian-quadratic-variation.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Finite nested-grid Q_n values at n=16384:", qv[:, -1])
    print("Largest relative Monte Carlo RMS error:",
          float(np.max(np.abs(empirical_rmse / theoretical_rmse - 1))))
    for t, n in [(1.0, 100), (2.0, 100)]:
        variance = 2 * t ** 2 / n
        print(f"T={t:g}, n={n}: E Q_n={t:g}, Var Q_n={variance:g}, "
              f"RMS error={sqrt(variance):.10f}")
    assert 2 * 2.0 ** 2 / 100 == 0.08


if __name__ == "__main__":
    main()
