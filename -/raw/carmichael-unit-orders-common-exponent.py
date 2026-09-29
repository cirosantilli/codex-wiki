"""Show exact powers, individual orders and the common unit exponent.

Output PNG in the CWD. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5.
"""

from math import gcd, lcm
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def order(a, n):
    return next(k for k in range(1, n) if pow(a, k, n) == 1)


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 6), dpi=120, facecolor="white")
    for ax, n in zip(axes, [8, 15]):
        units = [a for a in range(1, n) if gcd(a, n) == 1]
        orders = [order(a, n) for a in units]
        exponent = lcm(*orders)
        values = np.array([[pow(a, k, n) for k in range(exponent + 1)] for a in units])
        assert np.all(values[:, exponent] == 1)
        assert not any(all(pow(a, k, n) == 1 for a in units) for k in range(1, exponent))
        assert (exponent, len(units)) == ({8: (2, 4), 15: (4, 8)}[n])
        ax.imshow(values == 1, cmap=ListedColormap(["#f1f3f5", "#cfe8fa"]), vmin=0, vmax=1, aspect="auto")
        for i, row in enumerate(values):
            for k, value in enumerate(row):
                ax.text(k, i, str(value), ha="center", va="center", color="#1769aa" if value == 1 else "#333333", fontsize=13, fontweight="bold" if value == 1 else "normal")
            ax.text(exponent + 0.7, i, str(orders[i]), ha="center", va="center", color="#333333", fontsize=13)
        ax.set_xticks(range(exponent + 1))
        ax.set_yticks(range(len(units)), units)
        ax.set_xticks(np.arange(-0.5, exponent + 1, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(units), 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=2)
        ax.tick_params(which="minor", bottom=False, left=False)
        ax.set(xlabel=r"Exponent $k$", ylabel=r"Unit $a$", title=f"Powers modulo {n}")
        ax.axvline(exponent - 0.5, color="#1769aa", linewidth=2)
        ax.text(1.07, 1.06, "Order", transform=ax.transAxes, ha="center", fontsize=11)
        ax.text(0.5, -0.16, rf"$\lambda({n})={exponent}$: common return" + "\n" + rf"$\varphi({n})={len(units)}$: number of units", transform=ax.transAxes, ha="center", va="top", fontsize=13)
        ax.spines["right"].set_visible(False)
    fig.suptitle("One exponent returns every unit to 1", fontsize=18, y=0.97)
    fig.text(0.5, 0.885, r"Cells contain $a^k\;\mathrm{mod}\;n$; blue means 1. The final column is $k=\lambda(n)$.", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.075, right=0.91, top=0.79, bottom=0.23, wspace=0.65)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
