"""Plot exact original binary-source entropy and expected code costs; output to cwd."""
from fractions import Fraction
import heapq
from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def binary_entropy(p):
    p = np.asarray(p, dtype=float)
    out = np.zeros_like(p)
    interior = (p > 0) & (p < 1)
    out[interior] = -p[interior] * np.log2(p[interior]) - (1 - p[interior]) * np.log2(1 - p[interior])
    return out


def expected_huffman_length(n=16):
    # Each word with k flips has weight 7^(n-1-k) / (2 * 8^(n-1)).
    weights = [7 ** (n - 1 - k) for k in range(n)
               for _ in range(2 * comb(n - 1, k))]
    denominator = 2 * 8 ** (n - 1)
    assert sum(weights) == denominator
    heapq.heapify(weights)
    weighted_length = 0
    while len(weights) > 1:
        merged = heapq.heappop(weights) + heapq.heappop(weights)
        weighted_length += merged
        heapq.heappush(weights, merged)
    return Fraction(weighted_length, denominator)


def main():
    q = np.linspace(0, 1, 801)
    chosen = 1 / 8
    rate = float(binary_entropy(chosen))
    n = np.arange(1, 65)
    block_rate = rate + (1 - rate) / n
    code_rate = float(expected_huffman_length()) / 16
    assert block_rate[15] <= code_rate < block_rate[15] + 1 / 16
    plt.rcParams.update({"font.size": 13, "axes.titlesize": 14})
    fig, (ax, block_ax) = plt.subplots(1, 2, figsize=(12, 6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.axhline(1, color="#999999", linestyle="--", label="Marginal entropy: 1 bit")
    ax.plot(q, binary_entropy(q), color="#287557", linewidth=2.8, label=r"Entropy rate $h_2(q)$")
    ax.scatter([chosen], [rate], color="#a44a27", s=70, zorder=5)
    ax.annotate("q = 1/8\nRate ≈ 0.543564", (chosen, rate), xytext=(0.24, 0.37),
                fontsize=12, color="#8b3d21", arrowprops={"arrowstyle": "->", "color": "#a44a27"})
    ax.set(xlim=(0, 1), ylim=(-0.02, 1.12), xlabel="Flip probability q", ylabel="Bits per symbol",
           title="Unbiased symbols with predictable transitions")
    ax.legend(loc="lower center", fontsize=11)
    ax.grid(alpha=0.15)
    block_ax.axhline(1, color="#999999", linestyle="--", label="Ignoring dependence")
    block_ax.axhline(rate, color="#287557", linestyle=":", linewidth=2.5, label="Limiting entropy rate")
    block_ax.plot(n, block_rate, color="#476c9b", linewidth=2.7, label=r"Block entropy $H_n/n$")
    block_ax.scatter([16], [code_rate], color="#a44a27", s=70, zorder=5,
                     label="Expected Huffman length / 16")
    block_ax.annotate("16-symbol code\n≈ 0.574695 bits/symbol", (16, code_rate), xytext=(3.3, 0.74),
                      fontsize=12, color="#8b3d21", arrowprops={"arrowstyle": "->", "color": "#a44a27"})
    block_ax.set_xscale("log", base=2)
    block_ax.set_xticks([1, 2, 4, 8, 16, 32, 64], labels=["1", "2", "4", "8", "16", "32", "64"])
    block_ax.set(xlim=(1, 64), ylim=(0.49, 1.05), xlabel="Block length n", ylabel="Bits per symbol",
                 title="q = 1/8: the initial fair bit adds overhead")
    block_ax.legend(loc="upper right", fontsize=10, framealpha=0.96)
    block_ax.grid(alpha=0.15)
    fig.suptitle("Entropy rate measures new uncertainty, rather than marginal randomness", fontsize=17)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.13, top=0.83, wspace=0.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
