"""Exact biased-coin word costs and count masses; write the matching PNG to cwd."""

from math import comb
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n, p, epsilon = 40, 0.25, 0.1
    k = np.arange(n + 1)
    entropy = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    costs = -k * np.log2(p) - (n - k) * np.log2(1 - p)
    mass = np.array([comb(n, int(j)) * p**j * (1 - p) ** (n - j) for j in k])
    typical = np.abs(costs / n - entropy) <= epsilon
    assert np.array_equal(k[typical], np.arange(8, 13))
    assert np.isclose(mass.sum(), 1)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=120)
    fig.patch.set_facecolor("white")
    axes[0].plot(k, costs, color="#246c9a", linewidth=2.3)
    axes[0].scatter([0], [costs[0]], color="#a84725", s=48, zorder=3)
    axes[0].annotate("All-zero word:\nmost likely individual", xy=(0, costs[0]), xytext=(7, 20), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#a84725"})
    axes[0].axhline(n * entropy, color="#267e49", linestyle="--", linewidth=1.2)
    axes[0].text(18, n * entropy + 1.5, "nH ≈ 32.451", color="#267e49", fontsize=11)
    axes[0].set_title("One word's probability cost")
    axes[0].set_ylabel("−log₂ P(word), bits")
    axes[1].bar(k, mass, width=0.85, color=np.where(typical, "#267e49", "#82abc3"))
    axes[1].annotate("Many words near k = 10\ncarry most total probability", xy=(10, mass[10]), xytext=(18, 0.11),
                     fontsize=11, arrowprops={"arrowstyle": "->", "color": "#267e49"})
    axes[1].set_title("All words with that count")
    axes[1].set_ylabel("P(K = k)")
    axes[1].set_ylim(0, 0.17)
    for ax in axes:
        ax.axvspan(7.5, 12.5, color="#267e49", alpha=0.10, zorder=0)
        ax.set_xlim(-1, 41)
        ax.set_xlabel("Number k of ones in a 40-bit word")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A high-probability collection need not contain the most likely word", fontsize=16)
    fig.text(0.5, 0.025, "p = 1/4; P(K = k) = C(40,k) · (1/4)ᵏ · (3/4)⁴⁰⁻ᵏ. Green: tolerance 0.1 bits/symbol.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.8, bottom=0.18, wspace=0.3)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
