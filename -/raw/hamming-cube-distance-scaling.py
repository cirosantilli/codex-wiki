"""Draw hamming-cube-distance-scaling.png in the current working directory.

Uses the repository's NumPy/Matplotlib environment; tested with Python 3.14.4.
Checks every unordered pair for n=1,3,8 and every distance class for n=32.
"""

from itertools import combinations, product
from math import comb

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def verify_distances():
    for n in (1, 3, 8):
        vertices = np.array(list(product((0, 1), repeat=n)), dtype=int)
        counts = np.zeros(n + 1, dtype=int)
        ratios = []
        for i, j in combinations(range(len(vertices)), 2):
            delta = vertices[i] - vertices[j]
            # Independently count the differing positions, then compare norms.
            k = sum(a != b for a, b in zip(vertices[i], vertices[j]))
            d1, d2 = np.linalg.norm(delta, 1), np.linalg.norm(delta, 2)
            assert d1 == k
            assert np.isclose(d2, np.sqrt(k))
            ratios.append(d2 / k)
            counts[k] += 1
        assert counts.sum() == comb(2**n, 2)
        assert all(counts[k] == 2**(n - 1) * comb(n, k) for k in range(1, n + 1))
        assert np.isclose(max(ratios) / min(ratios), np.sqrt(n))
    # Full enumeration at n=32 is infeasible. Each class is represented by
    # zero versus a vector with exactly k ones; the coordinate proof covers
    # every pair because each difference coordinate has square 0 or 1.
    for k in range(1, 33):
        delta = np.array([1] * k + [0] * (32 - k))
        assert np.linalg.norm(delta, 1) == k
        assert np.isclose(np.linalg.norm(delta, 2), np.sqrt(k))
    assert np.isclose(np.sqrt(32), 4 * np.sqrt(2))


def main():
    verify_distances()
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.5), facecolor="white")
    blue, orange = "#296b91", "#bd602d"
    for column, n in enumerate((3, 8, 32)):
        k = np.arange(1, n + 1)
        ax = axes[0, column]
        ax.plot(k, k, "o-", color=blue, ms=3.5, label=r"L1: $d_1=k$")
        ax.plot(k, np.sqrt(k), "o-", color=orange, ms=3.5, label=r"L2: $d_2=\sqrt{k}$")
        ax.set(title=f"Hamming cube: n = {n}", xlabel="Differing coordinates k",
               ylabel="Image distance", xlim=(0, n + 0.5), ylim=(0, n * 1.12))
        ax.set_xticks([1, 2, 3] if n == 3 else [1, n // 2, n])
        ax.legend(loc="upper left", frameon=False, fontsize=10)

    for column, n in enumerate((3, 8)):
        ax = axes[1, column]
        k = np.arange(1, n + 1)
        ax.plot(k, 1 / np.sqrt(k), "o-", color=orange, ms=4)
        ax.axhline(1, color="#777777", lw=0.8, ls=":")
        ax.axhline(1 / np.sqrt(n), color=orange, lw=0.8, ls=":")
        ax.set(title=rf"This L2 map: distortion $\sqrt{{{n}}}$",
               xlabel="Hamming distance k", ylabel=r"Ratio $d_2/d_H$",
               xlim=(0.8, n + 0.2), ylim=(0, 1.15))
        ax.set_xticks([1, 2, 3] if n == 3 else [1, n // 2, n])
        ax.annotate("b = 1", (1, 1), xytext=(12, 3), textcoords="offset points")
        ax.annotate(rf"$a=1/\sqrt{{{n}}}$", (n, 1 / np.sqrt(n)),
                    xytext=(-4, -23), textcoords="offset points", ha="right")

    ax = axes[1, 2]
    t = np.linspace(0, 32, 400)
    ax.plot(t, np.sqrt(t), color=orange, lw=2.5)
    ax.set(title="One coarse control for every n", xlabel="Source distance t",
           ylabel="Lower and upper control", xlim=(0, 32), ylim=(0, 6.8))
    ax.text(0.08, 0.83, r"$\rho_-(t)=\rho_+(t)=\sqrt{t}$", transform=ax.transAxes, fontsize=13)
    ax.text(0.08, 0.65, "Unbounded as t grows\nIndependent of dimension", transform=ax.transAxes,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for ax in axes.flat:
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Same binary coordinates, different distance growth", fontsize=18, y=0.985)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.09, top=0.88, hspace=0.57, wspace=0.34)
    fig.savefig("hamming-cube-distance-scaling.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
