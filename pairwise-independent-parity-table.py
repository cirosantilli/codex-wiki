"""Original parity tables. Tested: Python 3.14.4, Matplotlib 3.10.7.

Run from _media; writes the matching PNG basename to the current directory.
"""
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    triples = [(u, v, u ^ v) for u, v in product((0, 1), repeat=2)]
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(9, 5.6), dpi=120, facecolor="white")
    fig.suptitle("Three fair bits from two: Z = X XOR Y", fontsize=18, y=.965)
    top = fig.add_axes((.15, .47, .70, .37))
    top.axis("off")
    table = top.table(
        cellText=[[x, y, z, "1/4", x+y+z] for x, y, z in triples],
        colLabels=["X = U", "Y = V", "Z = U XOR V", "Probability", "X + Y + Z"],
        cellLoc="center", loc="center", bbox=(0, 0, 1, 1),
        colWidths=[.16, .16, .28, .20, .20],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#a5b3bd")
        cell.set_facecolor("#dceaf3" if row == 0 else "#f5f8fa")
        if row == 0:
            cell.set_text_props(weight="bold")
    for k, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        ax = fig.add_axes((.055 + k*.32, .14, .25, .23))
        ax.axis("off")
        names = "XYZ"
        ax.set_title(f"Pair ({names[i]}, {names[j]})", fontsize=13, pad=9)
        counts = [[sum(t[i] == a and t[j] == b for t in triples)
                   for b in (0, 1)] for a in (0, 1)]
        assert counts == [[1, 1], [1, 1]]
        cells = [[f"{a}", *[f"{n}/4" for n in counts[a]]] for a in (0, 1)]
        small = ax.table(cellText=cells,
                         colLabels=[f"{names[i]} / {names[j]}", "0", "1"],
                         cellLoc="center", bbox=(0, 0, 1, 1),
                         colWidths=[.42, .29, .29])
        small.auto_set_font_size(False)
        small.set_fontsize(12)
        for (row, col), cell in small.get_celld().items():
            cell.set_edgecolor("#a5b3bd")
            cell.set_facecolor("#dceaf3" if row == 0 or col == 0 else "white")
    fig.text(.5, .425, "Every pair has four equally likely values; each marginal is (1/2, 1/2).",
             ha="center", fontsize=12)
    fig.text(.5, .055, "Only even-sum triples occur: any two bits determine the third.",
             ha="center", fontsize=12, color="#234c69")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
