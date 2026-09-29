"""Illustrate an original binary Markov-source model; write the PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(7391)
    n, q = 80, 1 / 8
    flips = rng.random(n - 1) < q
    source = np.empty(n, dtype=int)
    source[0] = rng.integers(0, 2)
    for i in range(1, n):
        source[i] = source[i - 1] ^ int(flips[i - 1])
    independent = rng.integers(0, 2, size=n)
    assert np.array_equal(source[1:] ^ source[:-1], flips.astype(int))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(3, 1, figsize=(12, 7.2), dpi=100, sharex=True)
    fig.patch.set_facecolor("white")
    t = np.arange(1, n + 1)
    axes[0].step(t, source, where="post", color="#287557", linewidth=2)
    axes[0].scatter(t, source, color="#287557", s=10)
    axes[0].set_title("Persistent source: each marginal bit is fair, but transitions usually repeat")
    axes[0].set_ylabel(r"$X_n$")
    axes[1].vlines(t[1:][flips], 0, 1, color="#a44a27", linewidth=2)
    axes[1].scatter(t[1:], flips.astype(int), color="#a44a27", s=15)
    axes[1].set_title(r"Flip decisions: $Z_n=X_n\oplus X_{n-1}$, independent with probability $q=1/8$")
    axes[1].set_ylabel(r"$Z_n$")
    axes[1].text(1, 0.6, "Initial bit\nis sent separately", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 4})
    axes[2].step(t, independent, where="post", color="#476c9b", linewidth=1.6)
    axes[2].scatter(t, independent, color="#476c9b", s=9)
    axes[2].set_title("Comparison: independent fair bits, with one new bit of uncertainty per symbol")
    axes[2].set_ylabel("IID bit")
    for ax in axes:
        ax.set_ylim(-0.18, 1.22)
        ax.set_yticks([0, 1])
        ax.grid(axis="x", alpha=0.16)
    axes[2].set(xlim=(0.5, n + 0.5), xlabel="Symbol index n")
    fig.suptitle("A fair marginal distribution does not imply independent symbols", fontsize=18)
    fig.text(0.5, 0.018, "Original simulated paths, seed 7391; finite counts do not prove the theoretical entropy rate",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.865, bottom=0.10, hspace=0.67)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
