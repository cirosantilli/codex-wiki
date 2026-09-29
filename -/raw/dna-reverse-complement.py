"""Draw complement then reverse; write dna-reverse-complement.png in CWD.

Run from _media: python ../dna-reverse-complement.py
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
This is a sequence-operation diagram, not a drawing of molecular motion.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    sequence = "ACGTAC"
    mapping = str.maketrans("ACGT", "TGCA")
    partner = sequence.translate(mapping)
    reverse_complement = partner[::-1]
    assert partner == "TGCATG" and reverse_complement == "GTACGT"
    assert reverse_complement.translate(mapping)[::-1] == sequence
    colors = {"A": "#f4cb72", "T": "#a9dce8", "G": "#c8b9e7", "C": "#add8b0"}
    ink = "#31485c"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.8, 5.4))
    fig.subplots_adjust(left=0.03, right=0.98, top=0.87, bottom=0.05)
    ax.set(xlim=(-2.8, 6.0), ylim=(-0.65, 4.3))
    ax.axis("off")
    fig.suptitle("Reverse complement: complement letters, then reverse order", fontsize=15)
    for y, text, label, left, right in [
        (3.8, sequence, "Original strand", "5′", "3′"),
        (2.0, partner, "Aligned partner", "3′", "5′"),
        (0.2, reverse_complement, "Partner read 5′ → 3′", "5′", "3′"),
    ]:
        ax.text(-2.6, y, label, ha="left", va="center", fontsize=11)
        ax.text(-0.55, y, left, ha="center", va="center", fontsize=17)
        ax.text(5.65, y, right, ha="center", va="center", fontsize=17)
        for i, base in enumerate(text):
            ax.add_patch(FancyBboxPatch((i - 0.3, y - 0.28), 0.6, 0.56,
                                      boxstyle="round,pad=0.02", facecolor=colors[base],
                                      edgecolor=ink, zorder=3))
            ax.text(i, y, base, ha="center", va="center", fontsize=18, zorder=4)
    for i in range(6):
        ax.annotate("", (i, 2.36), (i, 3.44),
                    arrowprops={"arrowstyle": "->", "color": "#176b92", "lw": 1.3})
    ax.text(2.5, 2.89, "1. Complement: A ↔ T, C ↔ G", ha="center", va="center",
            fontsize=12, bbox={"fc": "white", "ec": "none", "pad": 3}, zorder=5)
    ax.text(2.5, 1.12, "2. Reverse aligned lettering:  T G C A T G  →  G T A C G T",
            ha="center", va="center", fontsize=11)
    ax.text(2.5, -0.48, "Same partner strand; only the direction used to write it changes",
            ha="center", fontsize=11, color=ink)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{sequence} → aligned {partner} → reverse complement {reverse_complement}")


if __name__ == "__main__":
    main()
