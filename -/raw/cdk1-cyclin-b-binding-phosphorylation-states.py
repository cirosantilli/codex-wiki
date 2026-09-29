"""Draw qualitative Xenopus Cdc2 states; no measured rates or fitted data.

Run from _media with Python 3.14 and matplotlib 3.10.7.
"""
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def permissive(bound, activating_p, inhibitory_t14, inhibitory_y15):
    """Coarse state classification, not a biochemical rate law."""
    return bound and activating_p and not (inhibitory_t14 or inhibitory_y15)


def check_states():
    states = list(product((False, True), repeat=4))
    active = [s for s in states if permissive(*s)]
    assert active == [(True, True, False, False)]
    assert all(not permissive(False, *s) for s in product((False, True), repeat=3))
    # Clearing inhibitory sites cannot replace a missing binding partner or pT161.
    assert not permissive(True, False, False, False)
    assert not permissive(True, True, False, True)


def main():
    check_states()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11.4, 7), dpi=100, facecolor="white")
    ax.set(xlim=(0, 11.4), ylim=(0, 7))
    ax.axis("off")
    blue, ink, red, green = "#e9f1fa", "#24374a", "#a34543", "#2b7752"

    def box(x, y, w, h, lines, face=blue, edge=ink):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle="round,pad=0.08", lw=1.7,
                                   facecolor=face, edgecolor=edge))
        ax.text(x, y, lines, ha="center", va="center", color=ink, linespacing=1.5)

    def arrow(start, end, color=ink):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=15, lw=1.8, color=color))

    ax.text(5.7, 6.72, "Cyclin binding ≠ activating phosphorylation ≠ removal of inhibition",
            ha="center", va="center", fontsize=15, weight="bold", color=ink)
    ax.text(5.7, 6.30, "Qualitative states for the studied Xenopus Cdc2 (CDK1)",
            ha="center", color=ink)
    box(1.20, 3.35, 1.75, 1.10, "Free CDK1\n+ cyclin B", face="#f3f3f3")
    arrow((2.16, 3.28), (3.30, 2.32))
    ax.text(2.75, 3.35, "binding", ha="center", fontsize=11, color=ink)

    for x in (4.8, 9.45):
        ax.text(x, 5.91, "All boxes: CDK1 bound to cyclin B", ha="center", fontsize=11, color=ink)
    box(4.8, 5.02, 2.7, 1.16, "No pT161\nInhibitory P present\nNot activity-permissive")
    box(9.45, 5.02, 2.7, 1.16, "pT161 present\nInhibitory P present\nInhibited", face="#faeceb", edge=red)
    box(4.8, 2.32, 2.7, 1.16, "No pT161\nT14 and Y15 clear\nNot activity-permissive")
    box(9.45, 2.32, 2.7, 1.16, "pT161 present\nT14 and Y15 clear\nActivity-permissive", face="#e6f4eb", edge=green)

    for y in (5.02, 2.32):
        arrow((6.28, y), (7.96, y))
        ax.text(7.12, y+0.26, "CAK: add", ha="center", fontsize=11, color=ink)
        ax.text(7.12, y-0.38, "pT161", ha="center", fontsize=11, color=ink)
    for x in (4.8, 9.45):
        arrow((x-0.9, 4.36), (x-0.9, 2.99), green)
        arrow((x+0.9, 2.99), (x+0.9, 4.36), red)
        ax.text(x, 4.03, "Cdc25: remove", ha="center", fontsize=11, color=green)
        ax.text(x, 3.67, "inhibitory P", ha="center", fontsize=11, color=ink)
        ax.text(x, 3.30, "Myt1: add", ha="center", fontsize=11, color=red)

    ax.text(5.7, 1.23, "Inhibitory P = pT14 and/or pY15; pT161 is activating.",
            ha="center", color=ink)
    ax.text(5.7, 0.80, "Arrows are state changes, not a required reaction order or measured rates.",
            ha="center", color=ink, fontsize=11)
    ax.text(5.7, 0.36, "Activity-permissive describes this coarse classification; other regulators are omitted.",
            ha="center", color=ink, fontsize=11)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
