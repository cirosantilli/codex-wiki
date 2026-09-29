"""Original toy sequence diagram; Python 3.14, matplotlib 3.10.7.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes protein-primary-sequence-composition.png into the current directory.
"""
from pathlib import Path
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SEQUENCES = ("MAGAMG", "MMAAGG")
COLORS = {"M": "#c7dbef", "A": "#f9d7ab", "G": "#d1e7d3"}


def main():
    assert Counter(SEQUENCES[0]) == Counter(SEQUENCES[1])
    fig, ax = plt.subplots(figsize=(9.2, 5.1), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.5))
    ax.axis("off")
    ax.text(5, 5.15, "Composition loses order", ha="center", fontsize=20, weight="bold")
    ax.text(5, 4.72, "Two invented six-residue chains • not measured protein data", ha="center", fontsize=12)
    for row, (seq, y) in enumerate(zip(SEQUENCES, (3.75, 2.35)), start=1):
        ax.text(.3, y, f"Chain {row}", va="center", fontsize=12, weight="bold")
        ax.text(1.7, y, "N-end", ha="right", va="center", fontsize=11)
        for i, aa in enumerate(seq):
            x = 2.15 + i * 1.12
            if i < len(seq) - 1:
                ax.plot((x+.35, x+.77), (y, y), color="#435366", lw=2, zorder=1)
            ax.add_patch(FancyBboxPatch((x-.35, y-.3), .7, .6, boxstyle="round,pad=0.04", facecolor=COLORS[aa], edgecolor="#435366", zorder=2))
            ax.text(x, y, aa, fontsize=18, ha="center", va="center", weight="bold")
            ax.text(x, y+.48, str(i+1), fontsize=10, ha="center", color="#56616b")
        ax.text(8.3, y, "C-end", va="center", fontsize=11)
        ax.annotate("", xy=(8.05, y-.65), xytext=(1.85, y-.65), arrowprops={"arrowstyle": "->", "color": "#435366", "lw": 1.5})
    ax.text(5, 1.22, "Both: 2 M + 2 A + 2 G • 5 peptide bonds • same end residues", ha="center", fontsize=12, weight="bold")
    ax.text(5, .77, "M = methionine     A = alanine     G = glycine", ha="center", fontsize=12)
    ax.text(5, .31, "Read left → right from N-terminus to C-terminus; boxes are residues, not atoms.", ha="center", fontsize=11)
    fig.subplots_adjust(left=.02, right=.98, bottom=.03, top=.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
