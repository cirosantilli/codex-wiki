"""Draw independent instantiations of a let-polymorphic identity.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the matching opaque white PNG is written to the CWD.
The constraints illustrate pure Hindley-Milner rules without compiler deps.
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
    ink, blue, green, orange = "#203040", "#155d8a", "#187355", "#a84b12"

    def box(x, y, width, height, label, color=blue):
        ax.add_patch(FancyBboxPatch(
            (x - width / 2, y - height / 2), width, height,
            boxstyle="round,pad=0.08", facecolor="#f3f7fb",
            edgecolor=color, linewidth=1.6,
        ))
        ax.text(x, y, label, ha="center", va="center", color=color,
                linespacing=1.55)

    def arrow(start, end, color=blue):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=18,
            linewidth=1.8, color=color,
        ))

    ax.text(6, 7.62, "One let-bound identity, two independent uses",
            ha="center", va="center", fontsize=20, weight="bold", color=ink)
    ax.text(6, 7.10, "Pure Hindley–Milner: let identity = λx. x in ...",
            ha="center", va="center", fontsize=12, color=ink)
    box(6, 6.13, 8.4, 1.0, "Stored scheme: identity : ∀α. α → α\nThis scheme stays general.")
    arrow((4.6, 5.55), (3.0, 4.87))
    arrow((7.4, 5.55), (9.0, 4.87), green)
    box(3.0, 4.3, 4.7, 0.95, "First use: fresh α₁ → α₁\nargument 3 requires α₁ = int")
    box(9.0, 4.3, 4.7, 0.95, "Second use: fresh α₂ → α₂\nargument true requires α₂ = bool", green)
    arrow((3.0, 3.75), (3.0, 2.85))
    arrow((9.0, 3.75), (9.0, 2.85), green)
    ax.text(3.0, 3.28, "substitute int in this instance", ha="center", fontsize=11, color=ink,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.text(9.0, 3.28, "substitute bool in this instance", ha="center", fontsize=11, color=ink,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    box(3.0, 2.25, 4.7, 1.05, "int → int\nidentity 3 : int   (value 3)")
    box(9.0, 2.25, 4.7, 1.05, "bool → bool\nidentity true : bool   (value true)", green)
    ax.text(6, 1.36, "α₁ and α₂ are separate; each instance repeats its own type on both sides.",
            ha="center", va="center", fontsize=11, color=ink)
    box(6, 0.62, 10.9, 0.72,
        "A λ-bound f has one monomorphic type: using f 3 and f true conflicts.", orange)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
