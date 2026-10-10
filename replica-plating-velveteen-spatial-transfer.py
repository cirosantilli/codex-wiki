"""Original replica-plating schematic. Run from _media; Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle


BLUE = "#236c91"
ORANGE = "#bb6615"
GRAY = "#59636b"
SITES = [(-0.43, 0.35), (0.05, 0.52), (0.44, 0.22), (-0.50, -0.14),
         (0.02, -0.03), (0.37, -0.39), (-0.25, -0.49)]


def arrow(ax, start, end, color=GRAY, dashed=False, curve=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                color=color, lw=1.7, linestyle="--" if dashed else "-",
                                connectionstyle=f"arc3,rad={curve}"))


def plate(ax, center, label, surviving=None, fabric=False):
    x, y = center
    ax.add_patch(Circle(center, 0.80, fc="#f5f8fa", ec=GRAY, lw=1.5,
                        hatch="..." if fabric else None))
    ax.add_patch(Polygon([(x - .08, y + .88), (x + .08, y + .88),
                          (x, y + .73)], color=GRAY))
    for i, (dx, dy) in enumerate(SITES):
        if surviving is None or i in surviving:
            ax.add_patch(Circle((x + dx, y + dy), .067, fc=BLUE, ec="white", lw=.6))
    ax.text(x, y - 1.03, label, ha="center", va="top", fontsize=11, zorder=5,
            bbox={"fc": "white", "ec": "none", "pad": 1})


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(11, 6.6), dpi=110, facecolor="white")
    ax = fig.add_axes([.03, .05, .94, .85])
    ax.set(xlim=(0, 11), ylim=(-.7, 6), aspect="equal")
    ax.axis("off")
    fig.suptitle("Replica plating preserves a spatial address", y=.97, fontsize=18)
    ax.text(.10, 5.65, "Carrier: separated side view", fontsize=13, weight="bold")
    ax.text(4.05, 5.65, "Sample transfer: aligned plate views", fontsize=13, weight="bold")
    ax.plot([3.65, 3.65], [.1, 5.8], color="#dde2e5")

    # The master is inverted, with its culture surface facing the fabric.
    ax.add_patch(Rectangle((.65, 4.65), 2.3, .18, fc="#edf3f5", ec=GRAY))
    ax.add_patch(Rectangle((.67, 4.63), 2.26, .04, fc="#ded5b5", ec="none"))
    for x in [.9, 1.5, 2.4]:
        ax.add_patch(Ellipse((x, 4.61), .17, .055, fc=BLUE))
    ax.text(1.80, 5.08, "Inverted master plate", ha="center")
    arrow(ax, (1.80, 4.47), (1.80, 4.01))
    ax.text(2.05, 4.24, "light contact", fontsize=10)
    ax.add_patch(Rectangle((.70, 2.02), 2.2, 1.82, fc="#e4d6c1", ec=GRAY))
    ax.add_patch(Ellipse((1.80, 2.02), 2.2, .28, fc="#e4d6c1", ec=GRAY))
    ax.add_patch(Ellipse((1.80, 3.84), 2.2, .28, fc="#e8e0ec", ec=GRAY))
    for x in [0.86 + .095 * i for i in range(21)]:
        ax.plot([x, x], [3.83, 3.99], color="#8d729b", lw=1)
    ax.add_patch(Rectangle((.65, 3.59), 2.3, .14, fc="#a0aab0", ec=GRAY))
    ax.text(1.80, 3.27, "Wood or cork\nsupport", ha="center", va="center")
    ax.annotate("Sterile velveteen\npile faces upward", xy=(1.0, 3.96), xytext=(.05, 1.18),
                arrowprops={"arrowstyle": "-", "color": GRAY}, fontsize=10)
    ax.annotate("Retaining hoop", xy=(2.76, 3.67), xytext=(2.1, .60),
                arrowprops={"arrowstyle": "-", "color": GRAY}, fontsize=10, ha="center")

    plate(ax, (5.05, 4.2), "Master\nsource retained")
    plate(ax, (7.55, 4.2), "Fabric imprint\nsamples at matching sites", fabric=True)
    plate(ax, (6.00, 1.20), "Growth-supporting\ncontrol replica")
    plate(ax, (9.45, 1.20), "Challenged replica\ntwo growing sites", surviving={1, 5})
    arrow(ax, (5.95, 4.20), (6.65, 4.20))
    arrow(ax, (7.20, 3.30), (6.28, 2.18))
    arrow(ax, (8.00, 3.30), (9.10, 2.18))
    ax.text(9.35, 4.05, "▲ same orientation\n     on every plate", ha="center", fontsize=10)
    arrow(ax, (10.33, 1.40), (5.55, 5.03), color=ORANGE, dashed=True, curve=.35)
    ax.text(8.40, 5.18, "Read location → recover from master", color=ORANGE,
            ha="center", fontsize=10, bbox={"fc": "white", "ec": "none", "pad": 2})
    ax.text(7.65, -.58, "Original schematic • invented positions • no measured growth data",
            fontsize=9, color=GRAY, ha="center")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
