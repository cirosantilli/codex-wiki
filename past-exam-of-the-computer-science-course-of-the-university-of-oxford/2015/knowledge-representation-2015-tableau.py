"""Draw the two relevant tableau branches; write an opaque PNG in cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), dpi=120)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")

    def node(ax, x, y, name, color="#17624f"):
        ax.add_patch(Circle((x, y), 0.045, facecolor="white", edgecolor=color, lw=2))
        ax.text(x, y, name, ha="center", va="center", color=color, fontsize=15)

    left, right = axes
    left.set_title("Open branch: choose universal alternatives", fontsize=12, pad=15)
    node(left, 0.5, 0.82, "$x$")
    left.text(0.5, 0.66, "$D',\\ \\Gamma$", ha="center", fontsize=16)
    labels = [
        "$A_0,\\ \\neg B$",
        "$\\forall R.(L\\sqcap B)$",
        "$\\forall R.\\exists P.\\top$",
        "$\\forall R.\\overline{L},\\ \\forall R.L$",
    ]
    for y, label in zip((0.55, 0.46, 0.37, 0.28), labels):
        left.text(0.5, y, label, ha="center", fontsize=15)
    left.text(0.5, 0.12, "No successors required; no clash", ha="center", color="#17624f")
    left.text(0.5, 0.04, "Direct blocking: none", ha="center", fontsize=11)

    right.set_title("Closed alternative: choose an existential", fontsize=12, pad=15)
    node(right, 0.18, 0.82, "$x$")
    right.text(0.31, 0.82, "$D',\\ \\Gamma,\\ \\exists R.\\exists R.L$", va="center", fontsize=14)
    right.add_patch(FancyArrowPatch((0.18, 0.765), (0.18, 0.48), arrowstyle="-|>", mutation_scale=16, lw=1.8, color="#444444"))
    right.text(0.11, 0.62, "$R$", fontsize=14)
    node(right, 0.18, 0.43, "$y$", "#9c3030")
    right.text(0.31, 0.47, "$\\Gamma,\\ \\exists R.L,\\ \\exists P.\\top$", va="center", fontsize=14)
    right.text(0.31, 0.35, "$A_0,\\ B,\\ \\neg B$", va="center", color="#9c3030", fontsize=16,
               bbox={"boxstyle": "round,pad=0.35", "facecolor": "#fff4f2", "edgecolor": "#9c3030"})
    right.text(0.5, 0.12, "Clash at y: both B and its negation", ha="center", color="#9c3030")
    right.text(0.5, 0.04, "Direct blocking: none", ha="center", fontsize=11)

    fig.suptitle("Unfolded tableau for D: universal restrictions do not create edges", fontsize=14, y=0.98)
    fig.subplots_adjust(left=0.025, right=0.98, top=0.84, bottom=0.06, wspace=0.18)
    fig.savefig(Path.cwd() / "knowledge-representation-2015-tableau.png", facecolor="white", transparent=False,
                metadata={"Software": "codex-wiki matplotlib generator"})
    plt.close(fig)


if __name__ == "__main__":
    main()
