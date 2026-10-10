"""Draw a primary-assay workflow, with no simulated biological measurements.

Run from _media with Python 3.14 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def check_accounting():
    # Invented molecular counts for the independent bookkeeping example.
    populations = ({"unbound": 40, "inhibited": 50, "active": 10},
                   {"unbound": 40, "inhibited": 20, "active": 40})
    assert [sum(p.values()) for p in populations] == [100, 100]
    assert [p["inhibited"] + p["active"] for p in populations] == [60, 60]
    assert populations[1]["active"] / populations[0]["active"] == 4
    alpha, interval, blank = 3, 5, 7
    signals = [blank + alpha*p["active"]*interval for p in populations]
    assert (signals[1]-blank)/(signals[0]-blank) == 4
    # Dividing raw signals fails to recover the active-population ratio.
    assert signals[1]/signals[0] != 4


def main():
    check_accounting()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11.4, 7.2), dpi=100, facecolor="white")
    ax.set(xlim=(0, 11.4), ylim=(0, 7.2))
    ax.axis("off")
    ink = "#24374a"

    def box(x, y, w, h, text, face="#e9f1fa", fontsize=11):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle="round,pad=0.07", lw=1.5,
                                   facecolor=face, edgecolor=ink))
        ax.text(x, y, text, ha="center", va="center", color=ink,
                fontsize=fontsize, linespacing=1.45)

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=15, lw=1.7, color=ink))

    ax.text(5.7, 6.89, "Histone H1 labeling measures catalytic action during an assay",
            ha="center", fontsize=15, weight="bold", color=ink)
    ax.text(5.7, 6.48, "Workflow of Deibler & Kirschner (2010); no measured intensities drawn",
            ha="center", fontsize=11, color=ink)
    box(1.43, 5.40, 2.15, 1.35, "HeLa S3 extract\n+ cyclin B1\n20 min incubation")
    box(4.30, 5.40, 2.45, 1.35, "Aliquot + H1\n+ γ-³²P ATP\n15 min assay reaction")
    box(7.30, 5.40, 2.20, 1.35, "Stop reaction\nSDS-PAGE\nDry gel")
    box(10.02, 5.40, 2.02, 1.35, "Phosphorimager\nQuantify label\nin H1 band")
    for start, end in ((2.61, 2.98), (5.62, 6.11), (8.50, 8.94)):
        arrow((start, 5.40), (end, 5.40))

    ax.text(0.45, 4.27, "Reported controls answer different questions", fontsize=13,
            color=ink, weight="bold")
    box(2.02, 3.62, 3.02, 0.67, "No added cyclin B", face="#f3f3f3")
    ax.text(3.90, 3.62, "Baseline used for fold normalization; can include kinase activity",
            va="center", fontsize=11, color=ink)
    box(2.02, 2.74, 3.02, 0.67, "+ RO-3306 inhibitor", face="#faeceb")
    ax.text(3.90, 2.74, "Reduced H1 labeling supports a major CDK1 contribution",
            va="center", fontsize=11, color=ink)

    ax.text(0.45, 1.98, "Three measurements to keep distinct", fontsize=13,
            color=ink, weight="bold")
    box(2.03, 1.12, 3.03, 0.95, "Total-CDK1 immunoblot\nProtein amount", face="#f3f3f3")
    box(5.70, 1.12, 3.03, 0.95, "Site-specific immunoblot\nA phosphorylation state", face="#f3f3f3")
    box(9.37, 1.12, 3.03, 0.95, "H1 labeling readout\nSubstrate modification", face="#e6f4eb")
    ax.text(5.7, 0.23, "Extracts mix compartments; H1 is a supplied substrate, not a universal readout of mitosis.",
            ha="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
