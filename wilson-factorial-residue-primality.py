"""Plot exact factorial residues and inverse pairs; output PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from math import factorial, isqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def main():
    ns = np.arange(2, 31)
    residues = np.array([factorial(int(n) - 1) % int(n) for n in ns])
    prime = np.array([is_prime(int(n)) for n in ns])
    assert np.array_equal(residues == ns - 1, prime)
    assert all(r == 0 for n, r in zip(ns, residues) if not is_prime(int(n)) and n != 4)
    assert residues[2] == 2

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6.1), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 1, height_ratios=[3, 1.3], hspace=0.65)
    ax = fig.add_subplot(grid[0])
    ax.plot(ns, ns - 1, color="#8a97a5", linestyle="--", linewidth=1.5, label=r"Wilson target: $n-1$")
    ax.scatter(ns[~prime], residues[~prime], color="#667381", s=38, label="Composite", zorder=3)
    ax.scatter(ns[prime], residues[prime], color="#1769aa", s=55, label="Prime", zorder=4)
    ax.scatter([4], [2], color="#b45b12", s=65, zorder=5)
    ax.annotate(r"$3!\;\mathrm{mod}\;4=2$", xy=(4, 2), xytext=(7, 7), color="#93470b", arrowprops={"arrowstyle": "->", "color": "#93470b"})
    ax.set(xlim=(1, 31), ylim=(-1.5, 30), xlabel="Modulus n", ylabel=r"Least nonnegative residue of $(n-1)!$")
    ax.set_xticks([2, 4, 6, 10, 15, 20, 25, 30])
    ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("Factorial residues detect primes exactly", pad=12, fontsize=17)

    pairs = [(1,), (2, 4), (3, 5), (6,)]
    assert {a for pair in pairs for a in pair} == set(range(1, 7))
    assert all((pair[0] * pair[-1]) % 7 == 1 for pair in pairs)
    bx = fig.add_subplot(grid[1])
    bx.axis("off")
    bx.set_title("Why it works: inverse pairs modulo 7", fontsize=14, pad=8)
    for x, pair in zip([0.1, 0.36, 0.64, 0.9], pairs):
        label = str(pair[0]) if len(pair) == 1 else f"{pair[0]} × {pair[1]}"
        contribution = "1" if pair != (6,) else "6 ≡ −1"
        bx.text(x, 0.7, label, ha="center", va="center", fontsize=15, bbox={"boxstyle": "round,pad=0.4", "facecolor": "#e9f3fa", "edgecolor": "#1769aa"})
        bx.text(x, 0.12, contribution, ha="center", fontsize=13)
    fig.subplots_adjust(left=0.095, right=0.98, top=0.91, bottom=0.06)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
