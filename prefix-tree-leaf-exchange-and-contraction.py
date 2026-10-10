"""Worked binary prefix-tree exchange. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the current directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


WEIGHTS = {"A": Fraction(4, 10), "B": Fraction(3, 10),
           "C": Fraction(2, 10), "D": Fraction(1, 10)}


def draw_tree(ax, tree, weights, title, expected):
    """Draw every vertex at its actual codeword depth, with exact leaf costs."""
    leaves = []

    def walk(node, code=""):
        if isinstance(node, str):
            leaves.append((node, code))
        else:
            walk(node[0], code + "0")
            walk(node[1], code + "1")

    walk(tree)
    codes = dict(leaves)
    cost = sum(weights[s] * len(code) for s, code in leaves)
    assert cost == expected
    assert all(not b.startswith(a) for a in codes.values()
               for b in codes.values() if a != b)
    x_positions = dict(zip(codes, np.linspace(0, 3, len(codes))))

    def position(node, depth=0, code=""):
        if isinstance(node, str):
            return x_positions[node], -depth, weights[node]
        children = [position(child, depth + 1, code + str(i))
                    for i, child in enumerate(node)]
        x = sum(p[0] for p in children) / 2
        y = -depth
        weight = sum(p[2] for p in children)
        for i, (cx, cy, _) in enumerate(children):
            ax.plot([x, cx], [y, cy], color="#536373", lw=1.7, zorder=1)
            ax.text((x + cx) / 2 + (-0.07 if i == 0 else 0.07),
                    (y + cy) / 2, str(i), ha="center", va="center",
                    fontsize=11, color="#354452", backgroundcolor="white")
        ax.text(x, y, f"{float(weight):.1f}", ha="center", va="center",
                fontsize=12, bbox=dict(boxstyle="circle,pad=0.26",
                                      fc="white", ec="#536373"), zorder=3)
        return x, y, weight

    position(tree)
    for s, code in leaves:
        accent = "#be5832" if s in ("A", "D") else "#287c69"
        ax.text(x_positions[s], -len(code),
                f"{s} ({float(weights[s]):.1f})\n{code}\nd = {len(code)}",
                ha="center", va="center", fontsize=11,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=accent,
                          lw=1.7), zorder=4)
    ax.set(xlim=(-0.9, 3.9), ylim=(-3.8, 0.55))
    ax.set_title(title, fontsize=13, pad=12)
    ax.text(1.5, -3.65, f"Expected length = {float(cost):.1f} bits",
            ha="center", fontsize=12, weight="bold")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(14.4, 5.6), dpi=100)
    draw_tree(axes[0], ("D", ("B", ("C", "A"))), WEIGHTS,
              "Before: frequent A is too deep", Fraction(25, 10))
    draw_tree(axes[1], ("A", ("B", ("C", "D"))), WEIGHTS,
              "Exchange A and D", Fraction(19, 10))
    reduced = {"A": WEIGHTS["A"], "B": WEIGHTS["B"], "M": WEIGHTS["C"] + WEIGHTS["D"]}
    draw_tree(axes[2], ("A", ("B", "M")), reduced,
              "Contract siblings: M = C + D", Fraction(16, 10))
    fig.suptitle("Leaf labels determine weighted cost; siblings allow a smaller problem",
                 fontsize=16, y=0.98)
    fig.text(0.5, 0.045,
             "Exchange saves (0.4 − 0.1) × (3 − 1) = 0.6 bits.   Expansion adds p(C) + p(D) = 0.3 bits.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.84, bottom=0.15, wspace=0.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
