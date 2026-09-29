"""Original gene-expression and codon diagram; writes basename PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The nine-nucleotide example is a growing segment, not a complete protein.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch


CODONS = ("AUG", "GCU", "GAA")
# Standard-code assignments, also checked independently against NCBI table 1.
STANDARD_CODE_EXCERPT = {"AUG": "Met", "GCU": "Ala", "GAA": "Glu"}


def arrow(ax, start, end, color="#34495e"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 1.7, "color": color})


def box(ax, text, xy, width, height, color):
    ax.add_patch(FancyBboxPatch(xy, width, height,
                               boxstyle="round,pad=0.025,rounding_size=0.10",
                               edgecolor=color, facecolor="white", lw=1.7))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=12, color=color)


def main():
    residues = [STANDARD_CODE_EXCERPT[codon] for codon in CODONS]
    assert residues == ["Met", "Ala", "Glu"]
    fig, ax = plt.subplots(figsize=(9.0, 6.1))
    fig.patch.set_facecolor("white")
    # Upper panel: processing/export is a separate step across two membranes.
    ax.add_patch(FancyBboxPatch((0.2, 3.65), 4.75, 1.75,
                               boxstyle="round,pad=0.04,rounding_size=0.18",
                               facecolor="#faf1ff", edgecolor="#79519b", lw=2))
    ax.add_patch(FancyBboxPatch((0.30, 3.75), 4.55, 1.55,
                               boxstyle="round,pad=0.04,rounding_size=0.14",
                               facecolor="none", edgecolor="#79519b", lw=1))
    ax.text(2.5, 5.60, "NUCLEUS", fontsize=12, ha="center", color="#79519b")
    ax.text(7.35, 5.60, "CYTOPLASM", fontsize=12, ha="center", color="#267e9e")
    ax.text(1.0, 4.50, "DNA", ha="center", fontsize=14, color="#79519b")
    arrow(ax, (1.48, 4.50), (2.95, 4.50), "#79519b")
    ax.text(2.22, 4.85, "Transcription", ha="center", fontsize=10)
    ax.text(3.47, 4.50, "RNA", ha="center", fontsize=14, color="#267e9e")
    ax.text(3.1, 3.94, "Processing before export", ha="center", fontsize=10)
    # Gap in the schematic envelope marks the export route.
    ax.plot([4.75, 5.1], [4.5, 4.5], color="white", lw=16)
    ax.plot([4.76, 5.07], [4.66, 4.66], color="#34495e", lw=2)
    ax.plot([4.76, 5.07], [4.34, 4.34], color="#34495e", lw=2)
    arrow(ax, (3.94, 4.5), (6.34, 4.5), "#267e9e")
    ax.text(5.50, 4.97, "RNA export", ha="center", fontsize=10)
    ax.text(5.5, 3.76, "Via nuclear pore complex", ha="center", fontsize=9)
    ax.add_patch(Ellipse((7.0, 4.50), 1.2, 0.74, facecolor="#fbe4d6",
                         edgecolor="#b65620", lw=1.7))
    ax.text(7.0, 4.5, "Ribosome", ha="center", fontsize=11, color="#a14c18")
    arrow(ax, (7.69, 4.5), (8.65, 4.5), "#b65620")
    ax.text(8.12, 4.97, "Translation", ha="center", fontsize=10)
    ax.text(9.10, 4.50, "Protein", ha="center", fontsize=13, color="#a14c18")
    ax.text(7.48, 3.90, "RNA supplies the template", ha="center", fontsize=9)
    ax.axhline(3.32, xmin=0.04, xmax=0.96, color="#d8dfe5", lw=1)
    ax.text(5.0, 2.97, "Read three codons in the stated frame", ha="center", fontsize=13)
    ax.text(0.8, 2.14, "mRNA  5′", ha="center", fontsize=12, color="#267e9e")
    for i, codon in enumerate(CODONS):
        left = 2.0 + 2.15 * i
        box(ax, codon, (left, 1.86), 1.50, 0.57, "#267e9e")
        arrow(ax, (left + 0.75, 1.75), (left + 0.75, 1.13))
        box(ax, residues[i], (left, 0.45), 1.50, 0.57, "#b65620")
        if i < len(CODONS) - 1:
            ax.plot([left + 1.55, left + 2.1], [0.73, 0.73],
                    color="#b65620", lw=2)
    ax.text(8.63, 2.14, "3′", ha="center", fontsize=12, color="#267e9e")
    arrow(ax, (2.02, 2.68), (7.90, 2.68), "#267e9e")
    ax.text(1.05, 0.73, "N end", ha="center", fontsize=11, color="#b65620")
    ax.text(8.73, 0.73, "Growing C end", ha="center", fontsize=11, color="#b65620")
    ax.text(5.0, 0.04, "9 nucleotides → 3 codons → 3 residues joined by 2 peptide bonds",
            ha="center", fontsize=11)
    ax.set(xlim=(-0.3, 10), ylim=(-0.25, 5.85))
    ax.axis("off")
    fig.suptitle("Gene expression across compartments", fontsize=16, y=0.975)
    fig.text(0.5, 0.048, "AUG–GCU–GAA has no stop codon: this is a growing segment, not a complete released protein.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.015, "Original schematic • suitable initiation context assumed • additional machinery and termination omitted",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.12, top=0.92)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
