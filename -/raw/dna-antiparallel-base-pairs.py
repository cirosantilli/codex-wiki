"""Draw canonical DNA pair counts; write dna-antiparallel-base-pairs.png in CWD.

Run from _media: python ../dna-antiparallel-base-pairs.py
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Original unrolled schematic: boxes are bases, not atomic structures.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    sequence = "ACGTAC"
    partner = sequence.translate(str.maketrans("ACGT", "TGCA"))
    counts = [2 if base in "AT" else 3 for base in sequence]
    assert partner == "TGCATG" and partner[::-1] == "GTACGT"
    assert counts == [2, 3, 3, 2, 2, 3] and sum(counts) == 15
    colors = {"A": "#f4cb72", "T": "#a9dce8", "G": "#c8b9e7", "C": "#add8b0"}
    ink = "#31485c"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.8, 5.0))
    fig.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.04)
    ax.set(xlim=(-1.1, 6.0), ylim=(-0.9, 4.1))
    ax.axis("off")
    fig.suptitle("DNA: antiparallel strands and canonical base pairs", fontsize=16)
    for y, left, right in [(3.0, "5′", "3′"), (0.5, "3′", "5′")]:
        ax.plot([-0.35, 5.35], [y, y], color=ink, lw=3)
        ax.text(-0.75, y, left, ha="center", va="center", fontsize=18)
        ax.text(5.75, y, right, ha="center", va="center", fontsize=18)
        for i in range(6):
            ax.text(i, y, "S", ha="center", va="center", fontsize=11,
                    bbox={"boxstyle": "square,pad=0.22", "fc": "white", "ec": ink})
            if i < 5:
                ax.text(i + 0.5, y, "P", ha="center", va="center", fontsize=10,
                        bbox={"boxstyle": "circle,pad=0.18", "fc": "white", "ec": ink})
    for i, (top, bottom, count) in enumerate(zip(sequence, partner, counts)):
        ax.plot([i, i], [2.63, 3.0], color=ink, lw=2)
        ax.plot([i, i], [0.5, 0.87], color=ink, lw=2)
        for y, base in [(2.35, top), (1.15, bottom)]:
            ax.add_patch(FancyBboxPatch((i - 0.28, y - 0.27), 0.56, 0.54,
                                      boxstyle="round,pad=0.02", facecolor=colors[base],
                                      edgecolor=ink, zorder=3))
            ax.text(i, y, base, ha="center", va="center", fontsize=18, zorder=4)
        for j in range(count):
            x = i + (j - (count - 1) / 2) * 0.13
            ax.plot([x, x], [1.46, 2.04], color=ink, lw=1.5, ls=":")
        ax.text(i, 1.75, str(count), ha="center", va="center", fontsize=10,
                bbox={"fc": "white", "ec": "none", "pad": 0.5}, zorder=5)
    for start, end, y in [(-0.25, 5.25, 3.55), (5.25, -0.25, 0.05)]:
        ax.annotate("", (end, y), (start, y),
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#176b92"})
    ax.text(2.5, 3.73, "Arrows show each strand’s 5′ → 3′ direction", ha="center", fontsize=11)
    ax.text(2.5, -0.34, "3 A–T pairs × 2 + 3 G–C pairs × 3 = 15 hydrogen bonds",
            ha="center", fontsize=12)
    ax.text(2.5, -0.72, "S: sugar   P: phosphate   Dotted lines: hydrogen bonds\n"
            "Unrolled schematic; connector positions do not show atomic geometry",
            ha="center", va="center", fontsize=10, color=ink)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"5′–{sequence}–3′ / 3′–{partner}–5′; counts: {counts}; total: {sum(counts)}")


if __name__ == "__main__":
    main()
