"""Draw exact error/storage curves; output PNG basename in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The spectrum is stipulated, not fitted to measured data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    singular_values = np.array([8, 3, 1, 0.5])
    ranks = np.arange(5)
    frobenius = np.array([np.linalg.norm(singular_values[r:]) for r in ranks])
    operator = np.r_[singular_values, 0]
    np.testing.assert_allclose(frobenius ** 2, [74.25, 10.25, 1.25, 0.25, 0])
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, (error_ax, storage_ax) = plt.subplots(1, 2, figsize=(9.8, 4.8), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.965, bottom=0.23, top=0.78, wspace=0.27)
    fig.suptitle("Choosing rank: error saved versus storage spent", fontsize=16, y=0.96)
    fig.text(0.5, 0.86, "8 × 8 constructed matrix  •  singular values 8, 3, 1, ½  •  not measured data", ha="center")
    error_ax.plot(ranks, frobenius, "o-", color="#246aab", label="Frobenius: all-entry error", linewidth=2, markersize=6)
    error_ax.plot(ranks, operator, "s--", color="#b34b28", label="Operator: worst input", linewidth=2, markersize=5)
    error_ax.set(title="Optimal approximation error", xlabel="Retained rank r", ylabel="Absolute error norm", ylim=(-0.3, 9.8))
    error_ax.legend(loc="upper right", fontsize=9, frameon=False)
    for rank, label, offset in [(1, "√10.25", (8, 13)), (2, "√1.25", (8, 13)), (3, "½ (both)", (-12, 15)), (4, "0", (-8, 12))]:
        error_ax.annotate(label, (rank, frobenius[rank]), xytext=offset, textcoords="offset points", fontsize=10)
    error_ax.scatter([2], [frobenius[2]], s=150, facecolors="none", edgecolors="#246aab", linewidths=1.5, zorder=5)
    storage_ax.plot(ranks, 16 * ranks, "o-", color="#246aab", label="Two thin factors: 16r", linewidth=2, markersize=6)
    storage_ax.plot(ranks, 17 * ranks, "s--", color="#b34b28", label="SVD vectors + values: 17r", linewidth=2, markersize=5)
    storage_ax.axhline(64, color="#555555", linestyle=":", linewidth=1.8, label="Dense matrix: 64")
    storage_ax.set(title="Stored scalars at equal precision", xlabel="Retained rank r", ylabel="Number of scalars", ylim=(-2, 86))
    storage_ax.legend(loc="upper left", fontsize=9, frameon=False)
    storage_ax.annotate("32 / 34", (2, 34), xytext=(8, -18), textcoords="offset points", fontsize=10)
    storage_ax.annotate("64 / 68", (4, 68), xytext=(-41, 12), textcoords="offset points", fontsize=10)
    for ax in [error_ax, storage_ax]:
        ax.set_xticks(ranks)
        ax.set_xlim(-0.12, 4.22)
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.09, "Rank 2: 12.97% relative Frobenius error; 32 scalars in two factors versus 64 dense entries", ha="center", fontsize=11)
    fig.text(0.5, 0.04, "Lines connect integer choices only. Rank 4 is exact, but its generic factors save no storage.", ha="center", fontsize=10, color="#454545")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
