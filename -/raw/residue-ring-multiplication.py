"""Compare computed residue-ring products; write the matching PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def multiplication_table(n):
    residues = np.arange(n, dtype=int)
    return np.outer(residues, residues) % n


def main():
    six, five = multiplication_table(6), multiplication_table(5)
    assert six[2].tolist() == [0, 2, 4, 0, 2, 4]
    assert np.flatnonzero(six[2] == 2).tolist() == [1, 4]
    assert np.flatnonzero(six[2] == 1).tolist() == []
    assert six[2, 3] == six[4, 3] == 0
    assert [a for a in range(6) if 1 in six[a]] == [1, 5]
    for row in five[1:]:
        assert sorted(row.tolist()) == list(range(5))
    assert [int(np.flatnonzero(five[a] == 1)[0]) for a in range(1, 5)] == [1, 3, 2, 4]

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 5.3), dpi=120)
    for ax, n, table, color in zip(axes, (6, 5), (six, five), ("#b95f22", "#176997")):
        for a in range(n):
            for b in range(n):
                nontrivial_zero = a != 0 and b != 0 and table[a, b] == 0
                fill = "#ffe0d8" if nontrivial_zero else (
                    "#fff0df" if n == 6 and a == 2 else (
                        "#e7f0f7" if n == 5 and a != 0 else "#f6f7f8"))
                ax.add_patch(Rectangle((b - 0.5, a - 0.5), 1, 1,
                                       facecolor=fill, edgecolor="white", linewidth=2))
                ax.text(b, a, str(table[a, b]), ha="center", va="center", fontsize=15,
                        color="#a62b25" if nontrivial_zero else "#243441",
                        fontweight="bold" if nontrivial_zero else "normal")
        if n == 6:
            ax.add_patch(Rectangle((-0.5, 1.5), n, 1, fill=False,
                                   edgecolor=color, linewidth=2))
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.tick_params(length=0, labelsize=12, pad=7)
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position("top")
        ax.set_xlabel("second factor", fontsize=11, labelpad=10)
        ax.set_ylabel("first factor", fontsize=11, labelpad=9)
        ax.set_xlim(-0.55, n - 0.45)
        ax.set_ylim(n - 0.45, -0.55)
        ax.set_aspect("equal")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_title(f"Multiplication modulo {n}", color=color, fontsize=14, pad=47)
    axes[0].text(0.5, -0.13, "Row 2 repeats: 0, 2, 4, 0, 2, 4\nRed: nonzero factors give zero",
                 transform=axes[0].transAxes, ha="center", va="top", fontsize=11)
    axes[1].text(0.5, -0.13, "Every nonzero row contains each output once\nEach has one entry equal to 1: an inverse",
                 transform=axes[1].transAxes, ha="center", va="top", fontsize=11)
    fig.suptitle("A nonzero multiplier can lose information", fontsize=16, y=0.985)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.20, top=0.75, wspace=0.35)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
