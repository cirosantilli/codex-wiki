"""Draw original finite-volume amount bookkeeping; Python 3.14, matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3 ../finite-volume-shared-face-bookkeeping.py
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    step = Fraction(1, 4)
    old = [Fraction(2), Fraction(1)]
    flux = [Fraction(1), Fraction(3), Fraction(2)]
    new = [old[j] + step * (flux[j] - flux[j + 1]) for j in range(2)]
    assert new == [Fraction(3, 2), Fraction(5, 4)]
    assert sum(new) - sum(old) == step * (flux[0] - flux[-1])

    fig, ax = plt.subplots(figsize=(9, 4.7), dpi=130, facecolor="white")
    ax.set(xlim=(-0.35, 4.35), ylim=(-1.8, 2.5))
    ax.axis("off")
    fig.suptitle("One face transfer, two opposite entries", fontsize=17, y=0.97)
    ax.text(2, 2.05, r"Unit cell widths; time step $k=1/4$; all fluxes oriented right",
            ha="center", fontsize=11)
    for x, color, label, value in [(0, "#e7f0fa", "Left cell", "2"),
                                    (2, "#edf5e6", "Right cell", "1")]:
        ax.add_patch(Rectangle((x, 0), 2, 1.4, facecolor=color,
                               edgecolor="#34495e", linewidth=1.5))
        ax.text(x + 1, 1.12, label, ha="center", fontsize=13, weight="bold")
        ax.text(x + 1, 0.77, rf"Old amount = ${value}$", ha="center", fontsize=12)
    for x, rate, amount, color in [(0, "1", "1/4", "#326ca0"),
                                  (2, "3", "3/4", "#b55712"),
                                  (4, "2", "1/2", "#326ca0")]:
        ax.add_patch(FancyArrowPatch((x - 0.32, 0.25), (x + 0.32, 0.25),
                                    arrowstyle="-|>", mutation_scale=20,
                                    linewidth=2.5, color=color))
        ax.text(x, 1.65, rf"$F={rate}$", ha="center", fontsize=13, color=color)
        ax.text(x, -0.28, rf"Transfer $kF={amount}$", ha="center", fontsize=11,
                color=color)
    ax.text(1, -0.77, r"$2+1/4-3/4=3/2$", ha="center", fontsize=15)
    ax.text(3, -0.77, r"$1+3/4-1/2=5/4$", ha="center", fontsize=15)
    ax.text(2, -1.23, r"Shared interior transfer: $-3/4+3/4=0$", ha="center",
            fontsize=13, color="#b55712")
    ax.text(2, -1.64, r"Total: $3\ \longrightarrow\ 11/4$; boundary change $1/4-1/2=-1/4$",
            ha="center", fontsize=12)
    fig.subplots_adjust(left=0.06, right=0.94, bottom=0.04, top=0.86)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
