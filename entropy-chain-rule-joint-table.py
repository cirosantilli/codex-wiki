"""Draw the exact joint law and entropy accounting for a binary pair.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


def main():
    p = 0.1
    h = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    shared = 1 - h
    blue, orange, gray = "#2166ac", "#e69028", "#e4e7eb"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (table_ax, bars_ax) = plt.subplots(
        1, 2, figsize=(10.4, 4.8), gridspec_kw={"width_ratios": [1, 1.3]}
    )
    fig.suptitle(r"A fair bit plus an independent flip: $B=A\oplus N$, $p=0.1$", fontsize=16, y=0.96)
    table_ax.set_axis_off()
    table_ax.set_title("Joint probabilities", pad=18)
    table = table_ax.table(
        cellText=[["0.45", "0.05", "0.50"], ["0.05", "0.45", "0.50"], ["0.50", "0.50", "1.00"]],
        rowLabels=[r"$A=0$", r"$A=1$", "Total"],
        colLabels=[r"$B=0$", r"$B=1$", "Total"],
        cellLoc="center", rowLoc="center", bbox=[0.08, 0.31, 0.91, 0.54]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#a6adb5")
        if row == 0 or col == -1 or row == 3 or col == 2:
            cell.set_facecolor("#f1f3f5")
        else:
            cell.set_facecolor("#dbeaf7" if (row, col) in [(1, 0), (2, 1)] else "#fff0dc")
    table_ax.text(0.5, 0.20, r"$H(A)=H(B)=1$ bit", ha="center", transform=table_ax.transAxes)
    table_ax.text(0.5, 0.10, "Each row and column sums to 0.50", ha="center", fontsize=11, transform=table_ax.transAxes)
    bars_ax.set_title("Count shared uncertainty once", pad=18)
    for y in [0, 1]:
        bars_ax.barh(y, 1, height=0.43, color=blue)
        bars_ax.barh(y, h, left=1, height=0.43, color=orange)
        bars_ax.text(0.5, y, "1.000", ha="center", va="center", color="white", fontweight="bold")
        bars_ax.text(1 + h / 2, y, f"{h:.3f}", ha="center", va="center", color="#35230c", fontweight="bold")
    bars_ax.barh(1, shared, left=1 + h, height=0.43, facecolor=gray, edgecolor="#737b85", hatch="///")
    bars_ax.text(1 + h + shared / 2, 1, f"{shared:.3f}", ha="center", va="center", fontsize=11)
    bars_ax.set_yticks([0, 1], [r"$H(A,B)$", r"$H(A)+H(B)$"])
    bars_ax.set_ylim(-0.6, 1.65)
    bars_ax.set_xlim(0, 2.08)
    bars_ax.set_xticks([0, 0.5, 1, 1.5, 2])
    bars_ax.set_xlabel("Uncertainty (bits)")
    bars_ax.grid(axis="x", color="#dce0e5", linewidth=0.7)
    bars_ax.set_axisbelow(True)
    bars_ax.spines[["top", "right", "left"]].set_visible(False)
    bars_ax.legend(handles=[
        Patch(color=blue, label=r"First bit: $H(A)$"),
        Patch(color=orange, label=r"New uncertainty: $H(B\mid A)$"),
        Patch(facecolor=gray, edgecolor="#737b85", hatch="///", label=r"Overcount: $I(A;B)$"),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.24), frameon=False, fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.34, top=0.80, wspace=0.40)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
