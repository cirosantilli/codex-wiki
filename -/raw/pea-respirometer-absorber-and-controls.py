"""Draw a qualitative, original pea respirometer; emit its white PNG in CWD.

Apparatus context: University of Oklahoma K20 Center, Cell Respiration,
pp. 3–4. No measurements, calibrated positions or particle counts are asserted.
Tested with Python 3.14, matplotlib 3.10.7 (see pyproject.toml).
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 7.2), dpi=130)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 7.2))
    ax.axis("off")
    blue, green, gray = "#17648a", "#398053", "#69717a"

    def arrow(a, b, color=blue):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                                    linewidth=1.8, color=color))

    ax.text(5, 6.9, "Pea respirometer: absorber and matched controls", ha="center",
            fontsize=17, weight="bold")
    ax.add_patch(Rectangle((.35, 2.55), 9.25, 3.3, facecolor="#eef8fc",
                           edgecolor=blue, linewidth=1.6))
    ax.text(5, 5.58, "Shared water bath: hold temperature and position steady", ha="center",
            fontsize=12, color=blue)
    # Horizontal vial in longitudinal section; its stopper connects to a pipette.
    ax.add_patch(Rectangle((1, 3.15), 3.9, 1.85, facecolor="white",
                           edgecolor="#303030", linewidth=2))
    ax.add_patch(Rectangle((1.05, 3.2), .55, 1.75, facecolor="#ead9be", edgecolor="none"))
    ax.add_patch(Rectangle((1.6, 3.2), .3, 1.75, facecolor="#f3f0e8", edgecolor=gray))
    ax.add_patch(Rectangle((4.65, 3.15), .35, 1.85, facecolor="#b49374", edgecolor="#303030"))
    ax.add_patch(Rectangle((4.7, 3.96), 3.7, .22, facecolor="white", edgecolor="#303030"))
    # Water enters from the open bath-facing tip on the right.
    ax.add_patch(Rectangle((7.05, 3.98), 1.35, .18, facecolor="#7bc2e2", edgecolor="none"))
    ax.plot([7.05, 7.05], [3.98, 4.16], color=blue, linewidth=2.5)
    for x in [5.3, 5.6, 5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8]:
        ax.plot([x, x], [4.2, 4.3], color=gray, linewidth=1)
    for x, y in [(2.3, 3.65), (2.8, 3.65), (3.3, 3.65), (3.8, 3.65),
                 (2.55, 4.12), (3.05, 4.12), (3.55, 4.12)]:
        ax.add_patch(Circle((x, y), .18, facecolor="#9cc77e", edgecolor=green))
    ax.text(3.2, 4.65, "Peas + gas space", ha="center", fontsize=12)
    ax.text(6.6, 4.9, "Calibrated pipette", ha="center", fontsize=12)
    ax.text(8.6, 4.45, "Open tip\nin bath", ha="center", fontsize=10)
    arrow((7.85, 3.65), (6.55, 3.65))
    ax.text(7.2, 3.25, "Water boundary moves inward\nas O₂ is consumed", ha="center", fontsize=11)
    arrow((1.32, 2.1), (1.32, 3.15), "#a95108")
    ax.text(1.25, 1.85, "KOH on cotton\nremoves CO₂ from gas", ha="center", fontsize=11)
    arrow((3.6, 2.15), (1.75, 3.15), gray)
    ax.text(3.9, 1.85, "Dry separator\nkeeps peas off KOH", ha="center", fontsize=11)
    arrow((5.2, 5.3), (4.85, 4.55), gray)
    ax.text(5.4, 5.25, "Sealed stopper", fontsize=10)
    # Three comparison groups; circles are icons, not specimen counts.
    for x, title, color in [(.5, "A: germinating peas", green),
                             (3.5, "B: dry peas + beads", gray),
                             (6.5, "C: beads only", gray)]:
        ax.add_patch(Rectangle((x, .85), 2.7, .6, facecolor="white", edgecolor=color, linewidth=1.5))
        ax.text(x + 1.35, 1.15, title, ha="center", va="center", fontsize=11)
    ax.text(5, .5, "Match occupied volumes; C corrects common drift; B is a biological comparison.",
            ha="center", fontsize=11)
    ax.text(5, .15, "Original schematic, not to scale. Boundary position and tick spacing are not measured data.",
            ha="center", fontsize=10, color="#424242")
    fig.subplots_adjust(left=.015, right=.985, top=.985, bottom=.015)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
