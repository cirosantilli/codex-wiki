"""Show original DNA-content/ploidy states, not fluorescence measurements.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from the desired output directory; save the matching basename PNG there.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, (ax, panel) = plt.subplots(1, 2, figsize=(12, 5.8), dpi=100,
                                   gridspec_kw={"width_ratios": [1.15, 1]})
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0.55, 2.55), ylim=(0.45, 4.9), xticks=[1, 2],
           xticklabels=["1 set (haploid)", "2 sets (diploid)"],
           yticks=[1, 2, 3, 4], yticklabels=["1C", "2C", "3C", "4C"])
    ax.set_xlabel("Ploidy: complete chromosome sets", labelpad=12)
    ax.set_ylabel("Nuclear DNA content", labelpad=8)
    ax.set_title("A. Allocation path per product", weight="bold", pad=18)
    ax.grid(axis="y", color="#e4e9ed")
    ax.spines[["top", "right"]].set_visible(False)
    for xy, label, offset in [((2, 2), "Diploid G1", (10, -26)),
                               ((2, 4), "Diploid G2", (10, 9)),
                               ((1, 2), "After meiosis I", (-8, 14)),
                               ((1, 1), "After meiosis II", (10, -14))]:
        ax.scatter(*xy, s=130, color="#167c91", edgecolors="white", zorder=4)
        ax.annotate(label, xy=xy, xytext=offset, textcoords="offset points",
                    ha="right" if offset[0] < 0 else "left", fontsize=11)
    for start, end in [((2, 2.12), (2, 3.88)), ((1.9, 3.9), (1.08, 2.13)),
                       ((1, 1.88), (1, 1.12))]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "lw": 2.2, "color": "#435267"})
    ax.text(2.12, 3.0, "DNA\nreplication", fontsize=11, va="center")
    ax.text(1.40, 3.43, "Meiosis I", fontsize=11, rotation=37,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.text(0.93, 1.5, "Meiosis II", fontsize=11, ha="right", va="center")
    panel.set(xlim=(0, 1), ylim=(0, 1))
    panel.axis("off")
    panel.set_title("B. Same amount, different set count", weight="bold", pad=18)
    panel.text(0.5, 0.85, "2C", ha="center", fontsize=30, weight="bold", color="#167c91")
    for y, title, text in [(0.56, "Diploid G1", "2 sets × 1 copy per chromosome\n6 chromosomes; 6 DNA copies"),
                            (0.22, "Haploid after meiosis I", "1 set × 2 sister copies\n3 chromosomes; 6 DNA copies")]:
        panel.add_patch(FancyBboxPatch((0.02, y - 0.11), 0.96, 0.24,
                                       boxstyle="round,pad=0.015", facecolor="#f6f8fa",
                                       edgecolor="#b7c4cf"))
        panel.text(0.5, y + 0.064, title, ha="center", weight="bold", fontsize=13)
        panel.text(0.5, y - 0.035, text, ha="center", va="center", fontsize=12, linespacing=1.5)
    panel.text(0.5, 0.01, "A DNA amount alone does not identify ploidy.", ha="center", fontsize=11)
    fig.suptitle("Illustrative nuclear DNA content versus ploidy: stipulated 2n = 6",
                 fontsize=17, weight="bold", y=0.96)
    fig.text(0.5, 0.025, "Original idealized states, not measurements. Arrows describe completed products; they do not represent elapsed time.",
             ha="center", fontsize=10, color="#435267")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.8, bottom=0.16, wspace=0.4)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
