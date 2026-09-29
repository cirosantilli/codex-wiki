"""Original pleating cartoon; write an opaque white basename PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Only consecutive C-alpha positions and generic R groups are marked.
The connecting trace summarizes the backbone, not individual atomic bonds.
No hydrogen bonds are drawn to the marked carbon positions.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(1, 7, dtype=float)
    signs = np.where(np.arange(6) % 2 == 0, 1, -1)
    y = 0.28 * signs
    fig, ax = plt.subplots(figsize=(9.2, 4.7), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x, y, color="#34495e", lw=3, zorder=1)
    ax.scatter(x, y, s=210, facecolors="white", edgecolors="#34495e", lw=2, zorder=3)
    for index, (xi, yi, sign) in enumerate(zip(x, y, signs), start=1):
        color = "#217a9e" if sign == 1 else "#b35d23"
        end = yi + 0.80 * sign
        ax.plot((xi, xi), (yi, end), color=color, lw=2.3, zorder=2)
        ax.text(xi, end + 0.19 * sign, f"$R_{index}$", color=color,
                fontsize=15, ha="center", va="center")
        ax.text(xi, yi - 0.29 * sign, rf"$\mathrm{{C}}_{{\alpha,{index}}}$",
                ha="center", va="center", fontsize=12, color="#34495e")
    ax.annotate("", xy=(6.15, -1.84), xytext=(0.85, -1.84),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#34495e"})
    ax.text(3.5, -2.13, "N → C sequence order: consecutive residue positions 1–6",
            ha="center", fontsize=11)
    ax.set_xlim(0.35, 6.65)
    ax.set_ylim(-2.35, 1.65)
    ax.axis("off")
    fig.subplots_adjust(left=0.06, right=0.94, bottom=0.22, top=0.80)
    fig.suptitle("Beta-strand pleating and alternating side chains", fontsize=17, y=0.97)
    fig.text(0.5, 0.88, "Schematic side view • R groups alternate on opposite faces",
             ha="center", fontsize=11)
    fig.text(0.5, 0.11, "Circles mark Cα positions; the trace omits intervening backbone atoms.",
             ha="center", fontsize=11, color="#555555")
    fig.text(0.5, 0.055, "Cartoon geometry, not literal bond coordinates. Hydrogen bonds are not drawn.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
