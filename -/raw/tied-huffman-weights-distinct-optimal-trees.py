"""Two optimal binary prefix trees. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the current directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


WEIGHTS = {"A": Fraction(2, 5), "B": Fraction(1, 5),
           "C": Fraction(1, 5), "D": Fraction(1, 5)}


def draw_tree(ax, tree, title, lengths, merge_caption):
    leaves = []

    def walk(node, code=""):
        if isinstance(node, str):
            leaves.append((node, code))
        else:
            walk(node[0], code + "0")
            walk(node[1], code + "1")

    walk(tree)
    codes = dict(leaves)
    assert tuple(len(codes[s]) for s in "ABCD") == lengths
    assert sum(WEIGHTS[s] * len(codes[s]) for s in codes) == 2
    assert all(not b.startswith(a) for a in codes.values()
               for b in codes.values() if a != b)
    x_positions = dict(zip(codes, np.linspace(0, 3, 4)))

    def position(node, depth=0):
        if isinstance(node, str):
            return x_positions[node], -depth, WEIGHTS[node]
        children = [position(child, depth + 1) for child in node]
        x = sum(p[0] for p in children) / 2
        y = -depth
        weight = sum(p[2] for p in children)
        for i, (cx, cy, _) in enumerate(children):
            ax.plot([x, cx], [y, cy], color="#536373", lw=1.7, zorder=1)
            ax.text((x + cx) / 2 + (-0.065 if i == 0 else 0.065),
                    (y + cy) / 2, str(i), ha="center", va="center",
                    fontsize=12, color="#354452", backgroundcolor="white")
        is_tie = weight == Fraction(2, 5)
        ax.text(x, y, f"{float(weight):.1f}", ha="center", va="center", fontsize=13,
                bbox=dict(boxstyle="circle,pad=0.28", fc="white",
                          ec="#be5832" if is_tie else "#536373", lw=1.7), zorder=3)
        return x, y, weight

    position(tree)
    for s, code in leaves:
        ax.text(x_positions[s], -len(code),
                f"{s} ({float(WEIGHTS[s]):.1f})\n{code}\nd = {len(code)}",
                ha="center", va="center", fontsize=12,
                bbox=dict(boxstyle="round,pad=0.35", fc="white",
                          ec="#be5832" if s == "A" else "#287c69", lw=1.7), zorder=4)
    ax.set(xlim=(-0.7, 3.7), ylim=(-3.8, 0.6))
    ax.set_title(title, fontsize=14, pad=13)
    ax.text(1.5, -3.65, "Lengths: " + ", ".join(map(str, lengths)),
            ha="center", fontsize=13, weight="bold")
    ax.text(0.5, -0.13, merge_caption, transform=ax.transAxes,
            ha="center", fontsize=12)
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.2), dpi=100)
    draw_tree(axes[0], (("A", "B"), ("C", "D")), "Merge B with A (weight 0.4)",
              (2, 2, 2, 2), "Cost = (0.4 + 0.2 + 0.2 + 0.2) × 2 = 2 bits")
    draw_tree(axes[1], ("A", ("B", ("C", "D"))), "Merge B with CD (weight 0.4)",
              (1, 2, 3, 3), "Cost = 0.4 × 1 + 0.2 × 2 + 0.2 × 3 + 0.2 × 3 = 2 bits")
    fig.suptitle("A tie changes the tree shape without changing the optimal mean",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.89, "First merge C and D: their combined weight 0.4 ties with A.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Both sequences have merge weights 0.4, 0.6, 1.0, summing to 2 bits per symbol.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.77, bottom=0.22, wspace=0.15)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
