"""Original procedural ice-pail schematic; no invented instrument data.

Run from _media; tested with Python 3.14 and Matplotlib 3.10.7.
Charge labels use the ideal deep-enclosure limit, not an exact open-pail solution.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def ground(ax, x, y):
    ax.plot([x, x], [y, y-.15], color="#555b63", lw=1.5)
    for offset, width in [(0, .24), (.07, .16), (.14, .08)]:
        ax.plot([x-width/2, x+width/2], [y-.15-offset]*2, color="#555b63", lw=1.5)


def panel(ax, stage):
    ax.set(xlim=(-.7, 4.6), ylim=(-1.45, 4.8), aspect="equal")
    ax.axis("off")
    blue, orange = "#1764a0", "#b65013"
    # Separate pail and grounded shield, both open at the top.
    ax.plot([-.3, -.3, 2.9, 2.9], [2.9, -.25, -.25, 2.9],
            color="#86919b", lw=3)
    ax.plot([0, 0, 2.6, 2.6], [2.65, 0, 0, 2.65], color="#273f55", lw=5)
    for x in [.35, 2.25]:
        ax.add_patch(Rectangle((x-.09, -.22), .18, .18, fc="#c8e9e9", ec="#518383"))
    ax.plot([-.3, -.5], [-.05, -.05], color="#555b63", lw=1.5)
    ground(ax, -.5, -.05)
    ax.add_patch(Rectangle((3.3, .8), 1.05, 1.0, fc="white", ec=blue, lw=1.5))
    ax.text(3.825, 1.48, "meter", ha="center", fontsize=10, color=blue)
    ax.text(3.825, 1.08, ["zero", "response", "residual"][stage], ha="center", fontsize=9)
    ax.plot([2.6, 3.1, 3.1, 3.3], [2.2, 2.2, 1.65, 1.65], color=blue, lw=1.5)
    ax.plot([3.3, 3.15, 3.15], [1, 1, .5], color="#555b63", lw=1.5)
    ground(ax, 3.15, .5)
    if stage == 0:
        ax.text(1.3, 3.6, "charged source kept distant", ha="center", fontsize=9)
    elif stage == 1:
        y = 1.35
        ax.add_patch(Circle((1.3, y), .25, fc="#fff2e7", ec=orange, lw=1.5))
        ax.text(1.3, y, "+q", ha="center", va="center", color=orange, fontsize=11)
        ax.plot([1.3, 1.3], [y+.25, 4.0], color="#7a5b90", lw=1.5)
        if stage == 1:
            for yy in [.5, 1.15, 1.8]:
                ax.text(.16, yy, "−", color=blue, fontsize=16)
                ax.text(2.25, yy, "−", color=blue, fontsize=16)
                ax.text(-.24, yy+.17, "+", color=orange, fontsize=14)
                ax.text(2.66, yy+.17, "+", color=orange, fontsize=14)
            ax.text(1.3, .5, "no contact", ha="center", fontsize=10)
            ax.text(1.3, 3.25, "insulating suspension", ha="center", fontsize=9)
    else:
        for yy in [.5, 1.15, 1.8]:
            ax.text(-.24, yy+.17, "+", color=orange, fontsize=14)
            ax.text(2.66, yy+.17, "+", color=orange, fontsize=14)
        ax.text(1.3, 1.5, "object removed\nafter contact", ha="center", fontsize=10)
    headings = ["1. Zero, then isolate", "2. Insert without contact", "3. Contact, then withdraw"]
    ax.text(1.9, 4.45, headings[stage], ha="center", fontsize=12, fontweight="bold")
    notes = ["Initial pail + signal charge: 0\nSource charged away from the pail",
             "Inner induced charge ≈ −q\nExterior signal charge ≈ +q\nTotal signal charge remains 0",
             "Transferred signal charge: +q\nNo-touch withdrawal instead\nreturns the meter to baseline"]
    ax.text(1.8, -1.04, notes[stage], ha="center", va="center", fontsize=10,
            linespacing=1.45)
    if stage == 0:
        ax.text(.55, 1.6, "pail", color="#273f55", fontsize=10)
        ax.text(.65, -.43, "grounded shield", color="#616c76", fontsize=9)


def main():
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.8))
    fig.patch.set_facecolor("white")
    for stage, ax in enumerate(axes):
        panel(ax, stage)
    fig.suptitle("Ice-pail demonstration: redistribution versus transfer", fontsize=15, y=.95)
    fig.text(.5, .07, "Original procedural schematic • meter labels are qualitative outcomes, not measured readings",
             ha="center", fontsize=10, color="#4b5158")
    fig.text(.5, .035, "Deep-enclosure approximation; exterior charge includes the connected signal lead and meter input",
             ha="center", fontsize=10, color="#4b5158")
    fig.subplots_adjust(left=.02, right=.98, top=.87, bottom=.12, wspace=.12)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
