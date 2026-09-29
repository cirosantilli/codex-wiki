"""Original coding-segment ledger; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 5.3), dpi=120, facecolor="white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.02, 0.97, "Sequence change does not specify one consequence", fontsize=17, weight="bold")
    ax.text(0.02, 0.91, "Constructed coding strand, 5′ → 3′; fixed initiation and standard genetic code", fontsize=11)
    ax.text(0.02, 0.82, "Change from reference", fontsize=12, weight="bold")
    ax.text(0.31, 0.82, "DNA codons", fontsize=12, weight="bold")
    ax.text(0.69, 0.82, "Predicted product", fontsize=12, weight="bold")
    rows = [
        ("Reference", ["ATG", "TTT", "GAA", "TAA"], {}, "Met–Phe–Glu; stop"),
        ("One substitution: T → C", ["ATG", "TTC", "GAA", "TAA"], {(1, 2): True}, "Met–Phe–Glu; stop"),
        ("One substitution: T → C", ["ATG", "TCT", "GAA", "TAA"], {(1, 1): True}, "Met–Ser–Glu; stop"),
        ("One substitution: G → T", ["ATG", "TTT", "TAA", "TAA"], {(2, 0): True}, "Met–Phe; early stop"),
        ("Insert three bases: GGA", ["ATG", "GGA", "TTT", "GAA", "TAA"], {(1, i): True for i in range(3)}, "Met–Gly–Phe–Glu; stop"),
        ("Delete three bases: TTT", ["ATG", "---", "GAA", "TAA"], {}, "Met–Glu; stop"),
    ]
    for r, (label, codons, changed, product) in enumerate(rows):
        y = 0.72 - r * 0.105
        ax.add_patch(Rectangle((0.01, y - 0.033), 0.98, 0.075, facecolor="#f2f5f8" if r % 2 == 0 else "white", edgecolor="none"))
        ax.text(0.02, y, label, fontsize=11, va="center")
        for c, codon in enumerate(codons):
            for b, letter in enumerate(codon):
                ax.text(0.31 + c * 0.071 + b * 0.018, y, letter, family="monospace", fontsize=13, va="center", color="#b14e00" if (c, b) in changed else "#18354a", weight="bold" if (c, b) in changed else "normal")
        ax.text(0.69, y, product, fontsize=11, va="center")
    ax.text(0.02, 0.055, "Orange = changed / inserted base. Gap = removed codon. Stop contributes no amino acid.", fontsize=10)
    ax.text(0.02, 0.005, "Coding predictions alone do not establish gene expression, protein function or phenotype.", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.05, top=0.95)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
