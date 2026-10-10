"""Draw inference boundaries for cross-species functional complementation.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The output is an original inference schematic, not measured pathway data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ink, blue, green, amber = "#203448", "#eaf3fb", "#edf6ef", "#fff3df"

    def box(x, y, w, h, label, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                                   facecolor=color, edgecolor=ink, linewidth=1.3))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                color=ink, linespacing=1.45)

    def arrow(start, end, dashed=False):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                    linewidth=1.5, color=ink,
                                    linestyle="--" if dashed else "-"))

    ax.text(.5, .95, "Transfer the tested function with its conditions attached",
            ha="center", weight="bold", fontsize=17, color=ink)
    box(.025, .66, .25, .18, "Sequence resemblance\n\nChoose a candidate gene\nfrom S. pombe", blue)
    box(.36, .66, .275, .18, "Intervention in S. cerevisiae\n\nIntroduce candidate gene\ninto deletion recipient", blue)
    box(.72, .66, .255, .18, "Growth rescue?\n\nCompare native gene,\nunrelated gene and media", blue)
    arrow((.289, .75), (.345, .75))
    arrow((.649, .75), (.705, .75))
    ax.text(.317, .87, "candidate", ha="center", fontsize=10, color=ink)
    ax.text(.676, .87, "assay", ha="center", fontsize=10, color=ink)

    box(.26, .395, .48, .15,
        "If rescue occurs and controls work:\nfunction sufficient for this growth requirement\nin this recipient, with this expression and medium", green)
    arrow((.848, .649), (.74, .49))
    ax.text(.145, .47, "Supported scope", ha="center", weight="bold", color=ink)

    lower = [
        (.025, "Same native role\nin donor species?\n\nTest donor genetics"),
        (.355, "Same regulation\nand expression level?\n\nTest native expression"),
        (.685, "Same behavior in\nanother context?\n\nTest new conditions"),
    ]
    for (x, label), anchor in zip(lower, np.linspace(.36, .64, 3)):
        box(x, .095, .29, .175, label, amber)
        arrow((anchor, .383), (x + .145, .284), dashed=True)
    ax.text(.5, .325, "Each broader claim needs additional evidence", ha="center",
            fontsize=11, color=ink, bbox={"facecolor": "white", "edgecolor": "none", "pad": 4})
    ax.text(.5, .035, "A failed rescue also permits expression, tag or cellular-context explanations.",
            ha="center", fontsize=11, color=ink)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
