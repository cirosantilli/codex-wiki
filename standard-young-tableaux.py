"""Enumerate and draw all SYT of (3,2); write basename PNG in CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""

from itertools import permutations
from math import factorial
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


SHAPE = (3, 2)
DARK = "#243746"


def enumerate_tableaux(shape):
    cells = [(i, j) for i, part in enumerate(shape) for j in range(part)]
    output = []
    for entries in permutations(range(1, sum(shape) + 1)):
        filling = dict(zip(cells, entries))
        if all(filling[i, j] < filling[i, j + 1]
               for i, j in cells if (i, j + 1) in filling) and all(
                filling[i, j] < filling[i + 1, j]
                for i, j in cells if (i + 1, j) in filling):
            output.append(tuple(tuple(filling[i, j] for j in range(part))
                                for i, part in enumerate(shape)))
    return output


def main():
    tableaux = enumerate_tableaux(SHAPE)
    expected = [((1, 2, 3), (4, 5)), ((1, 2, 4), (3, 5)),
                ((1, 2, 5), (3, 4)), ((1, 3, 4), (2, 5)),
                ((1, 3, 5), (2, 4))]
    assert tableaux == expected
    assert len(tableaux) == factorial(5) // 24 == 5
    fig, axes = plt.subplots(1, 5, figsize=(11.5, 3.7), dpi=120,
                             facecolor="white")
    for index, (ax, tableau) in enumerate(zip(axes, tableaux), 1):
        for i, row in enumerate(tableau):
            for j, entry in enumerate(row):
                face = "#f8cf91" if entry == 5 else "#e0eef7"
                ax.add_patch(Rectangle((j, i), 1, 1, facecolor=face,
                                       edgecolor=DARK, linewidth=1.8))
                ax.text(j + 0.5, i + 0.5, str(entry), ha="center", va="center",
                        fontsize=22, color=DARK)
        ax.set(xlim=(-0.12, 3.12), ylim=(2.15, -0.12), aspect="equal")
        ax.axis("off")
        ax.set_title(f"$T_{index}$", fontsize=15, color=DARK, pad=12)
    fig.suptitle("All five standard Young tableaux of shape (3, 2)",
                 fontsize=16, color=DARK, y=0.96)
    fig.text(0.5, 0.13, "Entries increase → along rows and ↓ down columns; each uses 1–5 once.",
             ha="center", fontsize=12, color=DARK)
    fig.text(0.5, 0.035, "The largest entry (orange) always occupies a removable corner.",
             ha="center", fontsize=11, color=DARK)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.79, bottom=0.26,
                        wspace=0.18)
    fig.savefig(Path.cwd() / "standard-young-tableaux.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print(f"Enumerated {len(tableaux)} tableaux by checking all {factorial(5)} fillings.")


if __name__ == "__main__":
    main()
