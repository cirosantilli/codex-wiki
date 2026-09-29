"""Show all exponent choices for the divisors of 12; write basename PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce from the repository root: make _media/divisor-count-prime-exponents.png
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    exponents_two = np.arange(3)
    exponents_three = np.arange(2)
    divisors = 2 ** exponents_two[None, :] * 3 ** exponents_three[:, None]
    assert sorted(divisors.ravel().tolist()) == [1, 2, 3, 4, 6, 12]
    assert divisors.size == (2 + 1) * (1 + 1) == 6

    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=140, facecolor="white")
    blue, ink = "#176997", "#243746"
    for j in exponents_three:
        for i in exponents_two:
            ax.add_patch(Rectangle((i - 0.5, j - 0.5), 1, 1,
                                   facecolor="#edf5fa" if j == 0 else "#fff1e4",
                                   edgecolor="white", linewidth=3))
            ax.text(i, j + 0.11, rf"$2^{i}\,3^{j}={divisors[j, i]}$",
                    fontsize=18, ha="center", va="center", color=ink)
            ax.text(i, j - 0.21, f"divisor {divisors[j, i]}",
                    fontsize=11, ha="center", va="center", color=blue)
    ax.set(xlim=(-0.5, 2.5), ylim=(-0.5, 1.5))
    ax.set_xticks(exponents_two, [f"i = {i}" for i in exponents_two])
    ax.set_yticks(exponents_three, [f"j = {j}" for j in exponents_three])
    ax.tick_params(axis="both", length=0, labelsize=12, pad=9)
    ax.set_xlabel("Choose the exponent of 2: three possibilities", fontsize=12, labelpad=11)
    ax.set_ylabel("Exponent of 3: two possibilities", fontsize=12, labelpad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title(r"Each cell is one positive divisor: $d=2^i3^j$", fontsize=14, pad=17)
    fig.suptitle(r"$12=2^2\cdot3^1$: independent exponent choices", fontsize=17, y=0.96)
    fig.text(0.52, 0.04, r"$\tau(12)=(2+1)(1+1)=3\cdot2=6$",
             ha="center", fontsize=17, color=blue)
    fig.subplots_adjust(left=0.16, right=0.96, bottom=0.27, top=0.74)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
