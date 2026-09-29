"""Generate the exact fold-map diagram in the current working directory.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../critical-points-values-fold.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange, red, purple = "#2468a0", "#bf6a14", "#b52b39", "#704599"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), dpi=110)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.78, bottom=0.27, wspace=0.3)
    fig.suptitle(r"A fold loses one target direction: $F(x,y)=(x,y^2)$", y=0.98, fontsize=16)
    fig.text(0.5, 0.885, "Critical points live in the source; critical values live in the target.", ha="center")
    source, target = axes
    source.set_title(r"Source: $(x,y)$")
    source.axhspan(0, 1.7, color=blue, alpha=0.055)
    source.axhspan(-1.7, 0, color=orange, alpha=0.055)
    for x in np.linspace(-1.7, 1.7, 9):
        source.plot([x, x], [-1.7, 1.7], color="#dddddd", lw=0.7)
    for y in [-1.5, -1, -0.5, 0.5, 1, 1.5]:
        source.axhline(y, color=blue if y > 0 else orange, alpha=0.35, lw=0.8)
    source.axhline(0, color=red, lw=2.5)
    source.scatter([0.65, 0.65], [1, -1], c=[blue, orange], s=65, zorder=4)
    source.annotate(r"$(a,1)$", (0.65, 1), xytext=(0.9, 1.15), color=blue)
    source.annotate(r"$(a,-1)$", (0.65, -1), xytext=(0.9, -1.32), color=orange)
    source.text(-1.65, 0.1, "critical: rank 1", color=red, weight="bold")
    source.text(-1.65, 1.37, "regular: rank 2", color=blue)
    source.text(-1.65, -1.58, "regular: rank 2", color=orange)
    source.set(xlim=(-1.8, 1.8), ylim=(-1.7, 1.7), xlabel="x", ylabel="y")

    target.set_title(r"Target: $(a,b)$")
    target.axhspan(-0.9, 0, color="#eeeeee")
    target.axhspan(0, 2.7, color=purple, alpha=0.045)
    for y in [0.5, 1, 1.5]:
        target.axhline(y*y, color=purple, alpha=0.3, lw=0.8)
    target.axhline(0, color=red, lw=2.5)
    target.scatter([0.65], [1], c=purple, s=85, zorder=4)
    target.annotate("same output\nfrom two inputs", (0.65, 1), xytext=(-1.6, 1.25),
                    arrowprops={"arrowstyle": "->", "color": purple}, color=purple)
    target.text(-1.65, 2.4, "b > 0: regular values", color=purple)
    target.text(-1.65, 0.1, "b = 0: critical values", color=red, weight="bold")
    target.text(-1.65, -0.68, "b < 0: outside image\nregular values, empty fibers", color="#555555")
    target.set(xlim=(-1.8, 1.8), ylim=(-0.9, 2.7), xlabel="a", ylabel="b")
    for ax in axes:
        ax.set_facecolor("white")
        ax.tick_params(labelsize=10)
    for xpos, label, color in [(0.17, "b > 0\n2 regular inputs", purple),
                               (0.5, "b = 0\n1 critical input", red),
                               (0.83, "b < 0\n0 inputs", "#555555")]:
        fig.text(xpos, 0.125, label, ha="center", va="center", color=color,
                 bbox={"boxstyle": "round,pad=0.5", "fc": "white", "ec": color})
    fig.text(0.5, 0.02, "Exact polynomial example; colors distinguish branches, not measured data.",
             ha="center", fontsize=10, color="#555555")

    for y in [-1.0, 0.0, 1.0]:
        jac = np.diag([1.0, 2*y])
        assert np.linalg.matrix_rank(jac) == (1 if y == 0 else 2)
    for b in [0.0, 0.25, 1.0, 4.0]:
        fiber = [(0.65, 0.0)] if b == 0 else [(0.65, np.sqrt(b)), (0.65, -np.sqrt(b))]
        assert len(fiber) == (1 if b == 0 else 2)
        assert all(np.allclose([x, y*y], [0.65, b]) for x, y in fiber)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
