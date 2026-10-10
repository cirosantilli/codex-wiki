"""Original experimental logic and toy overlap diagram.

Historical logic: F. Sanger, The Chemistry of Insulin, Nobel lecture (1958).
No historical image or experimental measurements are reproduced.
Tested with Python 3.14 and matplotlib 3.10.7; run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Output basename matches this script.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(9.6, 7.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 10))
    ax.axis("off")
    ax.text(6, 9.65, "How destructive tests recover a sequence", ha="center", fontsize=19, weight="bold")
    ax.text(6, 9.2, "Insulin: complementary tests on separate portions of the sample", ha="center", fontsize=12)

    def box(x, y, w, h, text, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=.08", facecolor=color, edgecolor="#536575"))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=11, linespacing=1.45)

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops={"arrowstyle": "->", "color": "#435366", "lw": 1.5})

    for x, title in ((.25, "1  Chain ends"), (4.25, "2  Residue order"), (8.25, "3  S–S connections")):
        ax.text(x+1.75, 8.65, title, ha="center", fontsize=12, weight="bold")
    box(.25, 7.05, 3.5, 1.15, "Label free amino groups\nwith FDNB", "#f9e4b2")
    box(.25, 5.35, 3.5, 1.15, "Hydrolyze; separate products\nIdentify labeled end residues:\nglycine and phenylalanine", "#f9e4b2")
    arrow(2, 7, 2, 6.55)
    box(4.25, 7.05, 3.5, 1.15, "Oxidize S–S bonds\nSeparate A and B chains", "#d4e5f2")
    box(4.25, 5.35, 3.5, 1.15, "Different partial hydrolyses\nSeparate and characterize\noverlapping fragments", "#d4e5f2")
    arrow(6, 7, 6, 6.55)
    box(8.25, 7.05, 3.5, 1.15, "Obtain fragments retaining\nS–S links; prevent\nbond rearrangement", "#dcebdc")
    box(8.25, 5.35, 3.5, 1.15, "Identify linked fragments\nThen oxidize to identify\ntheir component pieces", "#dcebdc")
    arrow(10, 7, 10, 6.55)
    ax.text(6, 4.92, "Each path answers a different question; chain oxidation erases the original S–S pairings.", ha="center", fontsize=10.5)
    ax.plot((.3, 11.7), (4.55, 4.55), color="#b8c2ca", lw=1)
    ax.text(6, 4.13, "Toy overlap puzzle — invented fragments, not insulin", ha="center", fontsize=13, weight="bold")
    seq = "MAGAMG"
    colors = {"M": "#c7dbef", "A": "#f9d7ab", "G": "#d1e7d3"}
    # Exact fragments from two deliberately chosen, nonbiochemical cutting patterns.
    for y, label, pieces in ((3.12, "Cut pattern I", ((0, "MAG"), (3, "AMG"))),
                             (2.05, "Cut pattern II", ((0, "MA"), (2, "GA"), (4, "MG"))),
                             (.98, "Reconstructed", ((0, seq),))):
        ax.text(.4, y, label, va="center", fontsize=11, weight="bold")
        for start, fragment in pieces:
            width = len(fragment) * 1.0 - .18
            ax.add_patch(FancyBboxPatch((3.2+start, y-.35), width, .7, boxstyle="round,pad=.02", facecolor="#f6f8fa", edgecolor="#728494"))
            for i, aa in enumerate(fragment):
                assert aa == seq[start+i]
                x = 3.6 + start + i
                ax.text(x, y, aa, ha="center", va="center", fontsize=16, weight="bold", bbox={"boxstyle": "round,pad=.12", "facecolor": colors[aa], "edgecolor": "none"})
    ax.text(10.0, 2.6, "GA spans the\nMAG | AMG join", ha="center", va="center", fontsize=11, color="#344e69")
    ax.text(6, .25, "Rows show alignment after deduction; isolated fragments arrive without position labels.", ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.99)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
