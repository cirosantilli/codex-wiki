"""Original oriented sequence-flow diagram; Python 3.14, Matplotlib.

Build: make _media/gene-expression-transcription-translation.png
Writes an opaque white, same-basename PNG in the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def example():
    coding = "ATGGCTTAA"
    template = coding.translate(str.maketrans("ATGC", "TACG"))
    rna = template.translate(str.maketrans("TACG", "AUGC"))
    codons = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    # The three standard-code entries used here; not a complete genetic code.
    meanings = {"AUG": "Methionine", "GCU": "Alanine", "UAA": "STOP"}
    decoded = [meanings[c] for c in codons]
    assert template == "TACCGAATT" and rna == "AUGGCUUAA"
    assert coding.replace("T", "U") == rna
    assert decoded == ["Methionine", "Alanine", "STOP"]
    assert len(rna) == 9 and len(decoded[:-1]) == 2
    assert template[::-1] == "TTAAGCCAT"
    return coding, template, rna, codons, decoded


def main():
    coding, template, rna, codons, decoded = example()
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 6.1))
    fig.subplots_adjust(left=0.035, right=0.985, bottom=0.035, top=0.91)
    ax.set(xlim=(-0.2, 10.3), ylim=(-0.15, 7.5))
    ax.axis("off")
    fig.suptitle("Gene expression: a template directs synthesis of a different molecule", fontsize=15)
    centers = [3.5, 5.6, 7.7]
    palette = ["#1766ac", "#16805d", "#ae5226"]

    def row(y, label, sequence, left, right, boxes=False):
        ax.text(0.0, y, label, va="center", fontsize=11)
        ax.text(2.05, y, left, va="center", fontsize=14)
        ax.text(9.12, y, right, va="center", fontsize=14)
        for i, x in enumerate(centers):
            if boxes:
                ax.add_patch(FancyBboxPatch((x - 0.84, y - 0.32), 1.68, 0.64,
                                           boxstyle="round,pad=0.03", facecolor="#f3f7fa",
                                           edgecolor=palette[i], lw=1.7))
            ax.text(x, y, sequence[3 * i:3 * i + 3], family="monospace", fontsize=20,
                    ha="center", va="center", color=palette[i] if boxes else "#334155")

    ax.text(5.6, 7.1, "Chosen DNA coding segment (surrounding signals omitted)", ha="center", fontsize=12)
    row(6.5, "Coding DNA", coding, "5′", "3′")
    row(5.75, "Template DNA", template, "3′", "5′")
    for x in centers:
        ax.plot([x - 0.67, x + 0.67], [6.12, 6.12], color="#b4bdc5", ls=":", lw=2)
    ax.annotate("", (8.55, 5.15), (2.65, 5.15),
                arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#6b4b99"})
    ax.text(5.6, 5.38, "RNA polymerase reads template 3′ → 5′", ha="center", fontsize=11, color="#6b4b99")
    ax.annotate("", (1.65, 4.25), (1.65, 5.4),
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#6b4b99"})
    ax.text(0.0, 4.8, "Transcription", color="#6b4b99", fontsize=11)
    row(4.25, "mRNA", rna, "5′", "3′", boxes=True)
    ax.annotate("", (8.55, 3.6), (2.65, 3.6),
                arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#6b4b99"})
    ax.text(5.6, 3.71, "RNA synthesis and ribosome reading: 5′ → 3′", ha="center", fontsize=10)
    for x, meaning, color in zip(centers, decoded, palette):
        ax.annotate("", (x, 2.80), (x, 3.36),
                    arrowprops={"arrowstyle": "->", "lw": 1.5, "color": color})
        ax.text(x, 2.52, meaning, ha="center", va="center", color=color, fontsize=12, weight="bold")
    ax.text(0.0, 2.65, "Translation", color="#6b4b99", fontsize=11)
    ax.text(4.55, 1.93, "tRNA supplies these amino acids", ha="center", fontsize=10)
    ax.text(7.7, 1.93, "Release factor;\nno amino acid added", ha="center", fontsize=10, linespacing=1.4)
    ax.add_patch(FancyBboxPatch((2.4, 0.82), 6.6, 0.72, boxstyle="round,pad=0.04",
                               facecolor="#f3f7fa", edgecolor="#a2adb5"))
    ax.text(5.7, 1.2, "Product:  N — methionine — alanine — C", ha="center", va="center", fontsize=13)
    ax.text(5.7, 0.52, "Chain grows N → C; each new residue is added at the C end", ha="center", fontsize=10)
    ax.text(5.15, 0.05, "Standard code; chosen reading frame; suitable eukaryotic initiation context assumed.\n"
            "Nine displayed nucleotides are a coding example, not a complete independently translatable RNA.",
            ha="center", fontsize=9.5, color="#475569", linespacing=1.5)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Coding: {coding}; template (3′→5′): {template}; mRNA: {rna}; "
          f"codons: {codons}; meanings: {decoded}; 9 nucleotides, 2 residues, 1 stop.")


if __name__ == "__main__":
    main()
