"""Generate original modular-power and exponent-period diagrams.

Run from _media with Python 3.14 and matplotlib 3.10.7. Writes its own
basename as an opaque white-background PNG in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(13.5, 7.2), dpi=80)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-2.0, 10.0), ylim=(-2.6, 5.5))
    ax.axis("off")
    ax.text(4, 5.22, "A guaranteed return can exceed the shortest period",
            ha="center", fontsize=18)
    ax.text(-1.85, 4.48, "Exponent k", fontsize=13)
    for k in range(9):
        ax.text(k + 0.4, 4.48, str(k), ha="center", fontsize=14)
    rows = [(5, 12, 2, 2, 4), (7, 15, 4, 4, 8), (4, 15, 2, 4, 8), (3, 15, None, 4, 8)]
    colors = ["#e8f2f7", "#ede6f4", "#eaf3e7", "#fcf0de"]
    for row, (a, n, order, carmichael, phi) in enumerate(rows):
        y = 3.63 - 1.32 * row
        ax.text(-1.85, y + 0.15, rf"${a}^k$ mod {n}", va="center", fontsize=16)
        for k in range(9):
            value = pow(a, k, n)
            first = order is not None and k == order
            ax.add_patch(FancyBboxPatch((k + 0.08, y - 0.16), 0.64, 0.64,
                                        boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor=colors[row], edgecolor="#323d48" if first else "#cbd0d5",
                                        lw=2.8 if first else 1))
            ax.text(k + 0.4, y + 0.16, str(value), ha="center", va="center", fontsize=16)
        if order:
            label = rf"first return: $d={order}$     |     common return: $\lambda({n})={carmichael}$     |     Euler return: $\varphi({n})={phi}$"
            assert pow(a, order, n) == 1
            assert all(pow(a, j, n) != 1 for j in range(1, order))
        else:
            label = "nonunit: no positive-exponent return to 1; exponent reduction by 8 fails"
        ax.text(0.05, y - 0.55, label, fontsize=12, color="#323d48")
    ax.text(4.0, -1.98, r"$2029=253\cdot8+5\quad\Rightarrow\quad 7^{2029}\equiv7^5\equiv7\; (\mathrm{mod}\;15)$",
            ha="center", fontsize=16)
    ax.text(4.0, -2.50, r"$2029=507\cdot4+1\quad\Rightarrow\quad 7^{2029}\equiv7^1\equiv7\; (\mathrm{mod}\;15)$",
            ha="center", fontsize=16, color="#744391")
    fig.subplots_adjust(left=0.02, right=0.99, bottom=0.055, top=0.99)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
