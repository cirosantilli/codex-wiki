"""Draw distinct 1909/1913 scattering geometries; Python 3.14, Matplotlib 3.10.7.

Run from _media; creates the matching opaque white PNG in the current directory.
Schematic paths only: no trajectory calculation or historical dimensions implied.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle


BLUE = "#176a9c"
RED = "#bc4937"
GREEN = "#237e53"
GRAY = "#596572"


def arrow(ax, start, end, color=BLUE, **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                 linewidth=1.8, color=color, **kwargs))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.2), facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.16, wspace=0.12)
    fig.suptitle("Counting flashes to probe the atom", fontsize=19, y=0.97)
    fig.text(0.5, 0.90, "Two different experimental arrangements • schematic, not to scale",
             ha="center", color=GRAY, fontsize=12)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_xlim(-5.2, 4.4)
        ax.set_ylim(-3.1, 4.0)
        ax.axis("off")

    ax = axes[0]
    ax.set_title("1909: fixed reflection screen", fontsize=14, pad=18)
    source = Polygon([(-4.8, 1.85), (-4.8, 0.65), (-3.0, 1.15), (-3.0, 1.35)],
                     closed=True, facecolor="#e8eef2", edgecolor=GRAY, linewidth=1.5)
    ax.add_patch(source)
    ax.plot([-3.0, -3.0], [1.13, 1.37], color=GREEN, linewidth=3)
    ax.text(-4.7, 2.25, "Source in conical tube", fontsize=11)
    ax.annotate("Mica window", xy=(-3.0, 1.25), xytext=(-3.3, 0.52),
                arrowprops={"arrowstyle": "-", "color": GRAY}, fontsize=10, ha="right")
    foil_x, hit_y = 2.05, 1.25
    ax.add_patch(Rectangle((foil_x, -1.1), 0.12, 3.5, facecolor="#d7ae49",
                           edgecolor="#9f7c23"))
    ax.text(2.33, 2.65, "Metal\nreflector", ha="center", fontsize=11)
    arrow(ax, (-2.8, hit_y), (foil_x, hit_y))
    ax.text(-1.6, 1.55, r"Incident $\alpha$", color=BLUE)
    screen = np.array([-0.65, -0.95])
    arrow(ax, (foil_x, hit_y), screen, color=RED)
    ax.text(1.2, -0.63, "Deflected\nparticle", color=RED, ha="center", fontsize=10)
    ax.add_patch(Rectangle((-5.0, -0.05), 4.9, 0.22, facecolor=GRAY))
    ax.text(-4.7, -0.5, "Lead shield blocks\ndirect source → screen paths", fontsize=10)
    ax.plot([-1.15, -0.15], [-0.98, -0.98], color=GREEN, linewidth=5)
    ax.text(-1.1, -1.48, "Fixed ZnS screen", color=GREEN, fontsize=10)
    ax.add_patch(Rectangle((-0.91, -2.65), 0.52, 0.83, facecolor="#e8eef2",
                           edgecolor=GRAY, linewidth=1.4))
    ax.plot([-0.65, -0.65], [-1.13, -1.79], color=GREEN, linestyle=":")
    ax.text(0.1, -2.35, "Microscope:\ncount light flashes", fontsize=10)
    ax.annotate("", xy=(-0.38, -2.18), xytext=(0.04, -2.18),
                arrowprops={"arrowstyle": "-", "color": GRAY})

    ax = axes[1]
    ax.set_title("1913: rotating angular detector", fontsize=14, pad=18)
    ax.add_patch(FancyBboxPatch((-5.05, -2.8), 9.25, 6.45,
                               boxstyle="round,pad=0,rounding_size=0.3",
                               facecolor="#f7fafb", edgecolor="#adb8c2", linewidth=1.2))
    ax.text(0.2, -2.65, "Evacuated chamber", ha="center", color=GRAY, fontsize=10)
    ax.add_patch(Rectangle((-4.7, -0.35), 0.75, 0.7, facecolor="#e8eef2",
                           edgecolor=GRAY))
    ax.text(-4.35, -0.83, "Source", ha="center")
    for y in [-0.95, 0.09]:
        ax.add_patch(Rectangle((-2.6, y), 0.16, 0.86, facecolor=GRAY))
    ax.annotate("Diaphragm\n(collimator)", xy=(-2.5, -0.35), xytext=(-3.9, -1.6),
                arrowprops={"arrowstyle": "-", "color": GRAY}, fontsize=10)
    arrow(ax, (-3.9, 0), (-0.02, 0))
    ax.plot([0, 0], [-0.65, 0.65], color="#b18b2a", linewidth=4)
    ax.annotate("Thin foil", xy=(0, -0.55), xytext=(0.55, -1.1),
                arrowprops={"arrowstyle": "-", "color": GRAY})
    ax.plot([0, 3.9], [0, 0], linestyle="--", color=GRAY, linewidth=1)
    ax.text(2.6, -0.44, "Forward", color=GRAY, fontsize=10)
    angle = np.deg2rad(64.0)
    direction = np.array([np.cos(angle), np.sin(angle)])
    tangent = np.array([-direction[1], direction[0]])
    detector = 2.53 * direction
    arrow(ax, (0, 0), detector, color=RED)
    edge1, edge2 = detector - 0.36 * tangent, detector + 0.36 * tangent
    ax.plot([edge1[0], edge2[0]], [edge1[1], edge2[1]], color=GREEN, linewidth=5)
    # The microscope stays radially outside the screen and rotates with it.
    p0 = 2.88 * direction
    corners = [p0 - 0.24 * tangent, p0 + 0.24 * tangent,
               p0 + 0.24 * tangent + 0.8 * direction,
               p0 - 0.24 * tangent + 0.8 * direction]
    ax.add_patch(Polygon(corners, closed=True, facecolor="#e8eef2", edgecolor=GRAY))
    ax.annotate("ZnS screen", xy=detector, xytext=(2.1, 1.75), fontsize=10,
                color=GREEN, arrowprops={"arrowstyle": "-", "color": GREEN})
    ax.annotate("Microscope", xy=3.4 * direction, xytext=(-1.1, 3.45), fontsize=10,
                arrowprops={"arrowstyle": "-", "color": GRAY})
    ax.add_patch(Arc((0, 0), 1.7, 1.7, theta1=0, theta2=64, color=RED, linewidth=1.2))
    ax.text(0.97, 0.45, r"$\theta$", fontsize=15, color=RED)
    ax.add_patch(Arc((0, 0), 5.06, 5.06, theta1=83, theta2=152,
                     color=GREEN, linestyle="--", linewidth=1.2))
    arrow(ax, (-2.18, 1.28), (-2.28, 1.08), color=GREEN)
    ax.text(-2.0, 2.45, "Rotate together", color=GREEN, ha="center", fontsize=10)
    fig.text(0.5, 0.07,
             "Controls: reflector / foil removed • compare materials or foil thickness • correct backgrounds",
             ha="center", fontsize=11, color=GRAY)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
