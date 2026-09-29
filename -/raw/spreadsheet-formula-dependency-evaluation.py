"""Original spreadsheet DAG and exact evaluation trace.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def values(a1):
    a2 = 4
    b1, b2 = a1 + a2, 2 * a1
    c1 = b1 + b2
    return [a1, a2, b1, b2, c1, Fraction(c1, 2), a2**2]


def number(x):
    return str(float(x)) if isinstance(x, Fraction) else str(x)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(10.8, 7.8), facecolor="white")
    fig.suptitle("Spreadsheet dependencies: compute prerequisites first", y=0.975, fontsize=17)
    fig.text(0.5, 0.925, "Arrow = prerequisite → consumer; cell positions do not prescribe order",
             ha="center", fontsize=11)
    ax = fig.add_axes((0.025, 0.48, 0.95, 0.41))
    ax.set(xlim=(-0.9, 10.4), ylim=(-0.6, 4.3))
    ax.axis("off")
    pos = {"A1": (0, 3.4), "A2": (0, 0.6), "B1": (3.2, 3.4),
           "B2": (3.2, 1.65), "C1": (6.4, 2.55), "D1": (9.5, 2.55),
           "E1": (3.2, -0.05)}
    formulas = {"A1": "input 3 → 5", "A2": "input 4", "B1": "=A1+A2",
                "B2": "=2*A1", "C1": "=B1+B2", "D1": "=C1/2", "E1": "=A2^2"}
    edges = [("A1", "B1"), ("A2", "B1"), ("A1", "B2"),
             ("B1", "C1"), ("B2", "C1"), ("C1", "D1"), ("A2", "E1")]
    boxes = {}
    for cell, (x, y) in pos.items():
        fill = "#fff0d6" if cell in {"A1", "B1", "B2", "C1", "D1"} else "#e8f2fb"
        boxes[cell] = FancyBboxPatch((x-0.83, y-0.40), 1.66, 0.8,
                                    boxstyle="round,pad=0.02", facecolor=fill,
                                    edgecolor="#3c5268", linewidth=1.3, zorder=2)
        ax.add_patch(boxes[cell])
    for u, v in edges:
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>",
                                    patchA=boxes[u], patchB=boxes[v],
                                    mutation_scale=16, shrinkA=4, shrinkB=4,
                                    linewidth=1.6, color="#506275", zorder=1))
    for cell, (x, y) in pos.items():
        ax.text(x, y+0.13, cell, ha="center", va="center", weight="bold", zorder=3)
        ax.text(x, y-0.18, formulas[cell], ha="center", va="center",
                fontsize=10, family="DejaVu Sans Mono", zorder=3)
    fig.text(0.5, 0.445, "One valid order: A1, A2, B1, B2, C1, D1, E1", ha="center", weight="bold")
    tax = fig.add_axes((0.10, 0.065, 0.8, 0.33))
    tax.axis("off")
    old, new = values(3), values(5)
    rows = [[c, formulas[c].replace("input 3 → 5", "3, then 5").replace("input 4", "4"),
             number(a), number(b)] for c, a, b in zip(formulas, old, new)]
    table = tax.table(cellText=rows, colLabels=["Cell", "Stored input / formula", "Initial", "After A1 = 5"],
                      loc="center", cellLoc="center", colWidths=[0.13, 0.41, 0.20, 0.26])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.60)
    for (r, c), item in table.get_celld().items():
        item.set_edgecolor("#b9c4cf")
        if r == 0:
            item.set_facecolor("#e2ebf4")
            item.set_text_props(weight="bold")
        elif r in (2, 7):
            item.set_facecolor("#f2f6fa")
        else:
            item.set_facecolor("#fff7e9")
    fig.text(0.5, 0.022, "Recompute B1, B2, C1, D1; keep A2 and E1 cached.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
