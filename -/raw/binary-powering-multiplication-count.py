"""Plot exact operation counts, not timings; tested on Python 3.14 / Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    ns = np.arange(1, 64)
    lengths = np.array([int(n).bit_length() for n in ns])
    counts = np.array([int(n).bit_length() + int(n).bit_count() - 2 for n in ns])
    fig, (ax, bars) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120,
                                  facecolor="white", gridspec_kw={"width_ratios": [1.45, 1]})
    fig.suptitle("Optimized binary powering: one square per remaining digit",
                 fontsize=15, y=0.97)
    ax.plot(ns, ns - 1, color="#999999", label="Successive products: n − 1")
    ax.step(ns, lengths - 1, where="post", linestyle="--", color="#13775f",
            label="Lower bound: ℓ − 1")
    ax.step(ns, 2 * lengths - 2, where="post", linestyle="--", color="#c5811a",
            label="Upper bound: 2ℓ − 2")
    ax.scatter(ns, counts, s=15, color="#18639a", label="Exact: ℓ + wt(n) − 2", zorder=3)
    ax.annotate("n = 13: 5", (13, 5), xytext=(20, 14), color="#18639a",
                arrowprops={"arrowstyle": "->", "color": "#18639a"})
    ax.set(xlabel="Positive exponent n", ylabel="Multiplications (including squares)",
           xlim=(0, 64), ylim=(-0.7, 64))
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    samples = [8, 13, 15, 16, 31]
    squares = np.array([n.bit_length() - 1 for n in samples])
    extra = np.array([n.bit_count() - 1 for n in samples])
    positions = np.arange(len(samples))
    bars.bar(positions, squares, color="#18639a", label="Squarings: ℓ − 1")
    bars.bar(positions, extra, bottom=squares, color="#c5811a", label="Further products: wt(n) − 1")
    for x, n, s, t in zip(positions, samples, squares, extra):
        bars.text(x, s / 2, str(s), ha="center", va="center", color="white")
        if t:
            bars.text(x, s + t / 2, str(t), ha="center", va="center", color="white")
        bars.text(x, s + t + 0.2, f"{s + t}", ha="center", weight="bold")
    bars.set_xticks(positions, [f"{n}\n{n:b}₂" for n in samples])
    bars.set(xlabel="Exponent and its binary expansion", ylabel="Multiplications",
             ylim=(0, 10.4), title="Same digit count, different weight")
    bars.legend(loc="upper left", fontsize=8)
    for panel in (ax, bars):
        panel.spines[["top", "right"]].set_visible(False)
        panel.grid(axis="y", alpha=0.15)
        panel.set_axisbelow(True)
    fig.text(0.5, 0.025, "Start at the leading 1. No base-specific shortcuts. Counts are arithmetic operations, not bit costs.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.98, top=0.82, bottom=0.2, wspace=0.38)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
