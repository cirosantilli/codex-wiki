"""Draw the subset cube of divisors of 30; write a basename PNG to cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7.
Reproduce: make _media/mobius-divisor-cancellation.png
"""

from itertools import product
from math import prod
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    primes = (2, 3, 5)
    vertices = list(product((0, 1), repeat=3))
    divisors = {v: prod(p for p, bit in zip(primes, v) if bit)
                for v in vertices}
    weights = {v: (-1) ** sum(v) for v in vertices}
    assert sorted(divisors.values()) == [1, 2, 3, 5, 6, 10, 15, 30]
    assert sum(weights.values()) == 0
    assert all(weights[v] == -weights[(1, v[1], v[2])]
               for v in vertices if v[0] == 0)

    ink, positive, negative = "#243746", "#176997", "#b45325"
    positions = {v: (2.4 * v[0] + 0.95 * v[1],
                     0.9 * v[1] + 2.25 * v[2]) for v in vertices}
    fig, (ax, key) = plt.subplots(
        1, 2, figsize=(9.8, 5.4), dpi=110, facecolor="white",
        gridspec_kw={"width_ratios": [1.6, 1]})
    for v in vertices:
        for i in range(3):
            if v[i]:
                continue
            w = tuple(1 if j == i else bit for j, bit in enumerate(v))
            x, y = positions[v]
            end_x, end_y = positions[w]
            ax.plot([x, end_x], [y, end_y],
                    color="#71899a" if i == 0 else "#c4ced5",
                    lw=2.2 if i == 0 else 1.5,
                    linestyle="--" if i == 1 else "-", zorder=1)
    for v in vertices:
        x, y = positions[v]
        sign = "+1" if weights[v] == 1 else "−1"
        ax.text(x, y, f"d = {divisors[v]}\nμ(d) = {sign}",
                ha="center", va="center", fontsize=12, zorder=3,
                color=positive if weights[v] == 1 else negative,
                bbox={"boxstyle": "round,pad=0.48", "linewidth": 1.3,
                      "edgecolor": positive if weights[v] == 1 else negative,
                      "facecolor": "#edf5fa" if weights[v] == 1 else "#fff2e9"})
    ax.text(1.2, -0.51, "insert 2 → sign flips", ha="center", color=ink,
            fontsize=11)
    ax.set(xlim=(-0.58, 3.93), ylim=(-0.78, 3.72))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Each node selects a subset of {2, 3, 5}", fontsize=13,
                 color=ink, pad=12)

    key.axis("off")
    key.text(0.5, 0.95, "Pair by inserting 2", fontsize=14, weight="bold",
             ha="center", color=ink)
    for row, pair in enumerate(((1, 2), (3, 6), (5, 10), (15, 30))):
        y = 0.79 - row * 0.145
        key.text(0.5, y, f"μ({pair[0]}) + μ({pair[1]}) = 0", fontsize=13,
                 ha="center", color=ink)
    key.text(0.5, 0.13, r"$1-3+3-1=0$", fontsize=18,
             ha="center", color=ink)
    key.text(0.5, 0.01, r"$(1-1)^3=0$", fontsize=18,
             ha="center", color=ink)
    fig.suptitle("Möbius weights cancel over the divisors of 30",
                 fontsize=17, color=ink, y=0.97)
    fig.text(0.5, 0.035, "Every edge inserts one prime. Blue: +1; orange: −1.",
             ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=0.03, right=0.985, bottom=0.14,
                        top=0.82, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
