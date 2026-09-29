"""Draw an original schematic DNA ladder; write basename.png in cwd.

Build: make _media/dna-antiparallel-complement.png
Uses the repository's Python 3.14 and Matplotlib dependencies.
Blocks and rails are sequence symbols, not chemical atom structures.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


COLORS = {"A": "#f3c86a", "T": "#9dd9e8", "G": "#bdb0e2", "C": "#a7d2a2"}


def main():
    sequence = "ATGCC"
    complement = sequence.translate(str.maketrans("ATGC", "TACG"))
    reverse_complement = complement[::-1]
    assert complement == "TACGG" and reverse_complement == "GGCAT"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    fig.subplots_adjust(left=0.035, right=0.985, bottom=0.04, top=0.88)
    ax.set(xlim=(-1.35, 5.7), ylim=(-1.0, 4.5))
    ax.axis("off")
    fig.suptitle("DNA: matched bases, opposite strand directions", fontsize=16)
    for y, left, right in [(3.5, "5′", "3′"), (0.8, "3′", "5′")]:
        ax.plot([-0.45, 4.45], [y, y], color="#526779", lw=3, zorder=1)
        ax.text(-0.75, y, left, ha="center", va="center", fontsize=16)
        ax.text(4.8, y, right, ha="center", va="center", fontsize=16)
        for i in range(5):
            ax.text(i, y, "S", ha="center", va="center", fontsize=11,
                    bbox={"boxstyle": "square,pad=0.25", "fc": "white", "ec": "#526779"})
            if i < 4:
                ax.text(i + 0.5, y, "P", ha="center", va="center", fontsize=10,
                        bbox={"boxstyle": "circle,pad=0.2", "fc": "white", "ec": "#526779"})
    for i, (top, bottom) in enumerate(zip(sequence, complement)):
        ax.plot([i, i], [0.8, 1.19], color="#526779", lw=1.8, zorder=1)
        ax.plot([i, i], [3.11, 3.5], color="#526779", lw=1.8, zorder=1)
        for y, base in [(2.8, top), (1.5, bottom)]:
            ax.add_patch(FancyBboxPatch((i - 0.27, y - 0.29), 0.54, 0.58,
                                       boxstyle="round,pad=0.02", facecolor=COLORS[base],
                                       edgecolor="#526779", lw=1.1, zorder=2))
            ax.text(i, y, base, ha="center", va="center", fontsize=17, zorder=3)
        # One dashed link denotes a base pair, not a hydrogen-bond count.
        ax.plot([i, i], [1.86, 2.43], color="#526779", lw=2, ls=":", zorder=4)
    for start, end, y in [(-0.25, 4.25, 4.02), (4.25, -0.25, 0.27)]:
        ax.annotate("", (end, y), (start, y),
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#176b92"})
    ax.text(2, 4.19, "5′ → 3′ reading direction", ha="center", fontsize=11, color="#176b92")
    ax.text(2, -0.05, "Read the lower strand right to left:  5′–GGCAT–3′",
            ha="center", fontsize=12)
    ax.text(5.45, 2.15, "A ↔ T\nG ↔ C", ha="center", va="center", fontsize=12,
            linespacing=1.8)
    ax.text(2.05, -0.65, "S: deoxyribose sugar     P: phosphate     Blocks: bases\n"
            "Unrolled schematic; not an atom structure or a molecular-scale shape",
            ha="center", va="center", fontsize=10, color="#526779", linespacing=1.6)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"5′–{sequence}–3′ / 3′–{complement}–5′; reverse complement: {reverse_complement}")


if __name__ == "__main__":
    main()
