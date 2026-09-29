"""Schematic of field preparation and magnetic readout; not a scale reconstruction.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes this script's basename with a .png suffix to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle


def arrow(ax, start, end, color="#bb472a", **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                lw=2, color=color, **kwargs))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), facecolor="white")
    blue, red, green = "#185b97", "#bb472a", "#23806c"
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 8), aspect="equal")
        ax.axis("off")
    ax = axes[0]
    ax.set_title("Prepare a closed path, then remove the field", fontsize=13, pad=16)
    ax.add_patch(Rectangle((1, 1.2), 6.7, 5.5, fc="#edf7fc", ec=blue, lw=1.5))
    ax.text(4.35, 6.15, "Liquid-helium bath / cryostat", ha="center", color=blue)
    for r in (1.45, 1.58, 1.71):
        ax.add_patch(Circle((4.2, 3.7), r, fill=False, ec=blue, lw=2))
    ax.plot([4.95, 5.23], [2.55, 2.3], lw=7, solid_capstyle="round", color=green)
    ax.annotate("Fused lead closure", xy=(5.1, 2.4), xytext=(5.7, 1.65),
                ha="center", arrowprops={"arrowstyle": "-", "color": green}, color=green)
    for x, y in ((3.55, 3.4), (4.65, 3.4), (4.1, 4.45)):
        ax.add_patch(Circle((x, y), .15, fill=False, ec=red, lw=1.5))
        ax.add_patch(Circle((x, y), .035, color=red))
    ax.text(4.2, 5.65, "Applied field through the turns", ha="center", color=red)
    ax.text(4.2, .65, "Cool in field; keep the loop closed.\nWithdraw the inducing magnet while cold.",
            ha="center", va="top")
    ax.text(.3, 7.2, "A  Face view", weight="bold")
    ax = axes[1]
    ax.set_title("Sense the field without a contact in the loop", fontsize=13, pad=16)
    ax.add_patch(Rectangle((.35, 1.8), 3.1, 4.4, fc="#edf7fc", ec=blue, lw=1.5))
    for x in (1.45, 1.7, 1.95):
        ax.add_patch(Ellipse((x, 4), .55, 2.6, fill=False, ec=blue, lw=2))
    ax.text(1.9, 6.45, "Cold lead loop", ha="center", color=blue)
    arrow(ax, (2.6, 4), (4.5, 4), color=blue)
    ax.text(3.9, 4.45, "Loop field", ha="center", color=blue)
    ax.add_patch(Circle((5.4, 4), .65, fc="white", ec="#555555"))
    arrow(ax, (5.4, 3.5), (5.4, 4.5), color="#343b40")
    ax.text(5.4, 2.8, "Compass needle\n(null at balance)", ha="center")
    for x in (8, 8.25, 8.5):
        ax.add_patch(Ellipse((x, 4), .35, 2.5, fill=False, ec=red, lw=2))
    arrow(ax, (7.55, 4), (6.3, 4), color=red)
    ax.text(7.45, 4.55, "Opposing field", ha="center", color=red)
    ax.text(8.15, 6.1, "Separate copper\ncompensation coil", ha="center", color=red)
    ax.text(7.8, 2.2, "Adjust measured\nreference current", ha="center", color=red)
    ax.text(.3, 7.2, "B  Plan view (schematic)", weight="bold")
    ax.text(5, .65, "The reference coil has its own circuit.\nNo galvanometer or supply interrupts the lead loop.",
            ha="center", va="top")
    fig.text(.5, .025, "Original schematic; winding counts, shapes and spacing are illustrative.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=.03, right=.98, top=.88, bottom=.12, wspace=.12)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
