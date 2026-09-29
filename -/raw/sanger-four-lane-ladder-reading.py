"""Original toy endpoints, not gel measurements. Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


TEMPLATE = "TGCAATCG"  # displayed 3′ to 5′, after the primer-binding region
EXTENSION = "ACGTTAGC"  # synthesized 5′ to 3′
LANES = "ACGT"


def main():
    assert TEMPLATE.translate(str.maketrans("ACGT", "TGCA")) == EXTENSION
    endpoints = {base: [i for i, b in enumerate(EXTENSION, 1) if b == base]
                 for base in LANES}
    assert endpoints == {"A": [1, 6], "C": [2, 8], "G": [3, 7], "T": [4, 5]}
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10.8, 8), dpi=100, facecolor="white")
    ax = fig.add_axes((.05, .24, .9, .59))
    ax.set(xlim=(-1.5, 9.8), ylim=(-.3, 10))
    ax.axis("off")
    fig.suptitle("Four reactions → eight endpoints → one ordered extension", fontsize=17, y=.97)
    fig.text(.5, .91, "Displayed template region: 3′-TGCAATCG-5′   •   primer binds upstream (omitted)",
             ha="center", fontsize=12)
    ax.add_patch(Rectangle((-.45, .55), 4.0, 8.65, facecolor="#eef2f4",
                           edgecolor="#697d8b", lw=1.5))
    for lane, base in enumerate(LANES):
        ax.text(lane, 9.65, base, ha="center", weight="bold", fontsize=16)
        ax.add_patch(Rectangle((lane-.23, 8.78), .46, .18,
                               facecolor="white", edgecolor="#697d8b"))
        for n in endpoints[base]:
            # Increasing extension length is drawn higher: shortest travels farthest.
            ax.plot([lane-.27, lane+.27], [n, n], color="#243c50", lw=4.5,
                    solid_capstyle="butt")
    ax.text(4.1, 9.65, "Added\nposition", ha="center", va="center", fontsize=11)
    ax.text(5.2, 9.65, "Total\nlength", ha="center", va="center", fontsize=11)
    ax.text(7.7, 9.65, "Added prefix: 5′ → 3′", ha="center", fontsize=12)
    for n in range(1, len(EXTENSION)+1):
        ax.text(4.1, n, str(n), ha="center", va="center", fontsize=12)
        ax.text(5.2, n, f"p + {n}", ha="center", va="center", fontsize=12)
        ax.text(6.35, n, EXTENSION[:n-1], va="center", fontfamily="DejaVu Sans Mono",
                fontsize=14, color="#526577")
        # Separate terminal base by the same monospaced character spacing.
        ax.annotate(EXTENSION[n-1], (6.35, n), xytext=((n-1)*8.43, 0),
                    textcoords="offset points", va="center", fontfamily="DejaVu Sans Mono",
                    fontsize=14, weight="bold", color="#ad5620")
    ax.add_patch(FancyArrowPatch((-1.1, 1), (-1.1, 8), arrowstyle="-|>",
                                color="#167052", mutation_scale=18, lw=2))
    ax.text(-1.38, 4.5, "READ bottom → top", rotation=90, ha="center",
            va="center", color="#167052", fontsize=11, weight="bold")
    ax.text(1.5, .05, "Shortest shown: p + 1 nt", ha="center", fontsize=11)
    ax.add_patch(FancyArrowPatch((3.76, 8.45), (3.76, 1.1), arrowstyle="-|>",
                                color="#697d8b", mutation_scale=13, lw=1.5))
    ax.text(3.75, .38, "Migration", ha="center", fontsize=9, color="#526577")
    fig.text(.5, .205, "p = common known primer length; position 1 is ONE ADDED base, not a 1-nt whole molecule.",
             ha="center", fontsize=11, weight="bold")
    fig.text(.5, .158, "New extension: 5′-ACGTTAGC-3′     ⇄     aligned template: 3′-TGCAATCG-5′",
             ha="center", fontsize=13)
    fig.text(.5, .115, "Template written 5′ → 3′: 5′-GCTAACGT-3′  (reverse complement of the readout)",
             ha="center", fontsize=12, color="#167052")
    fig.text(.5, .067, "Denaturing polyacrylamide gel schematic: one-nucleotide differences, not an agarose size ladder.",
             ha="center", fontsize=10, color="#526577")
    fig.text(.5, .035, "Original invented bands. Spacing and darkness are illustrative, not measured migration or quantity.",
             ha="center", fontsize=10, color="#526577")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
