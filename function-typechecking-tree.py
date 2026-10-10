"""Draw a typing derivation for (lambda x. x + 1) 3.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the matching opaque white PNG is written to the CWD.
This is a diagram of stated typing rules, not a compiler implementation.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10.5, 7.0), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis("off")
    ink, blue, green = "#203040", "#155d8a", "#187355"

    def box(x, y, width, label, color=blue):
        ax.add_patch(FancyBboxPatch(
            (x - width / 2, y - 0.34), width, 0.68,
            boxstyle="round,pad=0.08", facecolor="#f3f7fb",
            edgecolor=color, linewidth=1.6,
        ))
        ax.text(x, y, label, ha="center", va="center", color=color)

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=17,
            linewidth=1.6, color=blue,
        ))

    ax.text(6, 7.62, "Checking a function call from its parts",
            ha="center", va="center", fontsize=20, weight="bold", color=ink)
    ax.text(6, 7.10, "Read downward: check operands, sum, function, argument and call result.",
            ha="center", va="center", fontsize=12, color=ink)
    box(2.2, 6.18, 3.4, "x : int ⊢ x : int")
    box(6.2, 6.18, 3.4, "x : int ⊢ 1 : int")
    arrow((2.2, 5.75), (3.5, 4.99))
    arrow((6.2, 5.75), (4.9, 4.99))
    ax.text(4.2, 5.40, "addition rule", ha="center", fontsize=11, color=ink)
    box(4.2, 4.55, 5.6, "x : int ⊢ x + 1 : int")
    arrow((4.2, 4.12), (4.2, 3.16))
    ax.text(4.48, 3.65, "abstraction: bind x", ha="left", fontsize=11, color=ink)
    box(4.2, 2.72, 6.4, "∅ ⊢ λx. x + 1 : int → int")
    box(9.5, 2.72, 2.8, "∅ ⊢ 3 : int", green)
    arrow((4.2, 2.29), (5.3, 1.50))
    arrow((9.5, 2.29), (6.7, 1.50))
    ax.text(6.5, 1.99, "application: argument type matches int",
            ha="center", fontsize=11, color=ink,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    box(6, 1.08, 9.6, "∅ ⊢ (λx. x + 1) 3 : int", green)
    ax.text(6, 0.35, "∅ = no free-name assumptions.  Arrows connect premises to conclusions.",
            ha="center", va="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
