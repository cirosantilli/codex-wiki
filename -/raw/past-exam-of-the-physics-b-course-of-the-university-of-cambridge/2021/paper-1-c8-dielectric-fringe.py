#!/usr/bin/env python3
"""Draw an original local schematic of dielectric insertion and fringe lines.

This is a qualitative electrode-end sketch, not a numerical solution for
finite coaxial conductors or a reconstruction of the source diagram.
Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
matching the repository pyproject.toml. Writes the PNG basename into cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
from matplotlib.path import Path as MplPath


def main():
    fig, ax = plt.subplots(figsize=(7.2, 3.7), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Rectangle((-1.1, -.82), 2.65, 1.64, facecolor="#ded5f0",
                           edgecolor="#8c78b3", linewidth=1.1, alpha=.65))
    for x in [-2.6, -2.05, -1.5, -.95, -.4]:
        ax.plot([x, x], [1, -1], color="#0072b2", linewidth=1.2)
        ax.annotate("", xy=(x, -.15), xytext=(x, .2),
                    arrowprops={"arrowstyle": "->", "color": "#0072b2", "lw": 1.2})
    for bulge in [.45, 1.05, 1.8]:
        curve = MplPath([(0, 1), (bulge, .7), (bulge, -.7), (0, -1)],
                        [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4])
        ax.add_patch(PathPatch(curve, edgecolor="#0072b2", facecolor="none", linewidth=1.2))
        ax.annotate("", xy=(.745 * bulge, -.13), xytext=(.745 * bulge, .15),
                    arrowprops={"arrowstyle": "->", "color": "#0072b2", "lw": 1.2})
    ax.plot([-3, 0], [1, 1], color="0.15", linewidth=4)
    ax.plot([-3, 0], [-1, -1], color="0.15", linewidth=4)
    ax.text(-3.22, .96, "+", fontsize=15)
    ax.text(-3.22, -1.06, "−", fontsize=15)
    ax.text(-2.4, 1.37, "Stronger interior field", ha="center", fontsize=10)
    ax.text(.85, 1.37, "Spreading fringe field", ha="center", fontsize=10)
    ax.annotate("Dielectric", xy=(1.35, .6), xytext=(1.6, .93), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#6b558f"})
    ax.annotate("", xy=(-1, -1.4), xytext=(.9, -1.4),
                arrowprops={"arrowstyle": "->", "color": "#d55e00", "lw": 2})
    ax.text(-.05, -1.7, "Force toward larger overlap", ha="center", fontsize=10, color="#b24b00")
    ax.set(xlim=(-3.5, 2.3), ylim=(-1.95, 1.8), title="Local electrode-end sketch: field and insertion force")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
