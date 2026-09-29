"""Draw a qualitative yeast complementation design, without simulated growth data.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The output basename matches this generator and is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ink, blue, green = "#203448", "#eaf3fb", "#edf6ef"

    def box(x, y, w, h, text, fill=blue, size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008",
                                   facecolor=fill, edgecolor=ink, linewidth=1.3))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=size, color=ink, linespacing=1.45)

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=13, color=ink, linewidth=1.5))

    ax.text(.5, .955, "Can a gene from another yeast supply a missing function?",
            ha="center", va="center", fontsize=17, weight="bold", color=ink)
    ax.text(.5, .905, "Same S. cerevisiae recipient: methionine-gene deletion + uracil deficiency",
            ha="center", va="center", fontsize=12, color=ink)

    box(.025, .68, .235, .13, "Native S. cerevisiae gene\npositive control")
    box(.025, .52, .235, .13, "Candidate S. pombe gene\nfunction under test")
    box(.025, .36, .235, .13, "Unrelated gene\nnegative control")
    ax.text(.145, .835, "Three plasmid constructs", ha="center", weight="bold", color=ink)
    box(.345, .51, .245, .23,
        "Select transformed colonies\n−uracil, +methionine\n\nPlasmid presence can support\ngrowth before rescue is tested", green, 11)
    for y in np.array([.745, .585, .425]):
        arrow((.265, y), (.337, .625))
    arrow((.599, .625), (.66, .625))

    box(.67, .51, .3, .23,
        "Replica plating\n\nVelveteen-covered block\n+ orientation marks\nPreserve colony locations", blue, 12)
    for x in np.linspace(.735, .905, 4):
        ax.add_patch(Circle((x, .775), .009, facecolor=ink, edgecolor=ink))
    ax.text(.82, .81, "Corresponding samples", ha="center", color=ink, fontsize=10)

    conditions = [
        (.025, "Transfer / viability check\n+ methionine, glucose\n− uracil", "Can the transferred cells grow?"),
        (.355, "Function test with induction\n− methionine, galactose\n− uracil", "Does the candidate restore growth?"),
        (.685, "Noninducing comparison\n− methionine, glucose\n− uracil", "Does growth depend on induction?"),
    ]
    for x, label, question in conditions:
        arrow((.82, .498), (x + .145, .3))
        box(x, .13, .29, .165, label, green if x == .025 else blue, 11)
        ax.text(x + .145, .09, question, ha="center", va="center", fontsize=10, color=ink)
    ax.text(.5, .035, "Design schematic only: no colony counts or rescue outcomes are depicted.",
            ha="center", fontsize=10, color=ink)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
