"""Compare faithful and nonfaithful C4 actions; write matching PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def action(k, degree):
    return tuple((k + x) % degree for x in range(degree))


def main():
    regular = [action(k, 4) for k in range(4)]
    reduced = [action(k, 2) for k in range(4)]
    for degree in [4, 2]:
        for g in range(4):
            for h in range(4):
                assert tuple(action(g, degree)[x] for x in action(h, degree)) == action((g + h) % 4, degree)
    assert len(set(regular)) == 4
    assert len(set(reduced)) == 2
    assert [k for k in range(4) if action(k, 2) == (0, 1)] == [0, 2]

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig = plt.figure(figsize=(10, 6.8), facecolor="white")
    fig.suptitle("The same group, two actions: which elements remain distinguishable?", fontsize=17, y=.97)
    for j, (degree, title, color) in enumerate([
        (4, "Faithful: four labels", "#2369a0"),
        (2, "Nonfaithful: two labels", "#ad4b24"),
    ]):
        left = .05 + j * .5
        ax = fig.add_axes([left, .52, .4, .31])
        angles = np.pi / 2 - np.arange(degree) * 2 * np.pi / degree
        points = np.column_stack((.72 * np.cos(angles), .72 * np.sin(angles)))
        for i, p in enumerate(points):
            ax.add_patch(FancyArrowPatch(p, points[(i + 1) % degree], arrowstyle="-|>",
                                        connectionstyle="arc3,rad=.24", shrinkA=17, shrinkB=17,
                                        mutation_scale=16, color=color, lw=2))
            ax.scatter(*p, s=650, facecolor="white", edgecolor=color, lw=2, zorder=2)
            ax.text(*p, str(i), ha="center", va="center", fontsize=15, zorder=3)
        ax.set(xlim=(-1.2, 1.2), ylim=(-1, 1), aspect="equal")
        ax.set_title(title, fontsize=16, color=color, pad=8)
        ax.axis("off")
        fig.text(left + .2, .48, rf"Generator $1$: $x\mapsto 1+x$ (mod {degree})", ha="center", fontsize=13)
        tax = fig.add_axes([left, .17, .4, .26])
        tax.axis("off")
        notation = ["id", "(0 1 2 3)", "(0 2)(1 3)", "(0 3 2 1)"] if degree == 4 else ["id", "(0 1)", "id", "(0 1)"]
        rows = [[str(k), notation[k]] for k in range(4)]
        table = tax.table(cellText=rows, colLabels=[r"$k\in C_4$", "Permutation on the labels"],
                          cellLoc="center", bbox=[0, 0, 1, 1], colWidths=[.22, .78])
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        for (row, col), cell in table.get_celld().items():
            cell.set_edgecolor("#c5ccd2")
            if row == 0:
                cell.set_facecolor("#edf2f6")
            elif degree == 2:
                cell.set_facecolor("#fff0df" if row in [1, 3] else "#f0e9f5")
        summary = r"Kernel $=\{0\}$; image has 4 elements" if degree == 4 else r"Kernel $=\{0,2\}$; image has 2 elements"
        fig.text(left + .2, .115, summary, ha="center", color=color, fontsize=13)
    fig.text(.5, .04, "Both actions reach every point. Only the left action distinguishes every group element.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
