"""Cross-sections illustrate signed cube flux and equal spherical flux."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def main():
    assert -1+1 == 0
    assert np.isclose(1**2 * 1, 2**2 * .25)
    blue, orange, green = "#176997", "#b55d20", "#43804d"
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=120)
    ax = axes[0]
    ax.add_patch(Rectangle((-1, -1), 2, 2, facecolor="#f1f5f7", edgecolor="#9baab6", lw=1.5))
    for y in [-.75, -.25, .25, .75]:
        for start in [-1.7, -.4, .9]:
            ax.annotate("", (start+.7, y), (start, y),
                        arrowprops={"arrowstyle": "->", "lw": 1.8, "color": blue})
    ax.plot([-1, -1], [-1, 1], color=orange, lw=3)
    ax.plot([1, 1], [-1, 1], color=green, lw=3)
    ax.annotate("", (-1.45, 0), (-1, 0),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
    ax.annotate("", (1.45, 0), (1, 0),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": green})
    ax.text(-1.35, -1.18, "Left face:\n−E₀ℓ²", ha="center", va="top", color=orange, fontsize=11)
    ax.text(1.3, -1.18, "Right face:\n+E₀ℓ²", ha="center", va="top", color=green, fontsize=11)
    ax.text(0, 1.32, "Same uniform field throughout", ha="center", color=blue, fontsize=11)
    ax.text(0, 0, "Q enclosed = 0", ha="center", va="center", fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    ax.text(0, -1.96, "Other four faces: zero flux\nTotal: 0, despite E ≠ 0", ha="center", fontsize=11)
    ax.set(xlim=(-2.2, 2.2), ylim=(-2.3, 2.05))
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Cross-section of an uncharged cube", fontsize=12)
    ax = axes[1]
    ax.add_patch(Circle((0, 0), 1, fill=False, color=blue, lw=1.8))
    ax.add_patch(Circle((0, 0), 2, fill=False, color=orange, lw=1.8, ls="--"))
    for radius, length, color in [(1, .65, blue), (2, .65/4, orange)]:
        for angle in np.arange(0, 2*np.pi, np.pi/4):
            direction = np.array([np.cos(angle), np.sin(angle)])
            ax.annotate("", (radius+length)*direction, radius*direction,
                        arrowprops={"arrowstyle": "->", "color": color,
                                    "lw": 1.6, "shrinkA": 0, "shrinkB": 0})
    ax.scatter([0], [0], color="#243746", s=75, zorder=4)
    ax.text(.12, .12, "+Q", fontsize=12)
    ax.text(-.67, -.45, "r = R", color=blue, fontsize=11)
    ax.text(.8, -2.04, "r = 2R", color=orange, fontsize=11)
    ax.set(xlim=(-2.6, 2.6), ylim=(-2.7, 2.4))
    ax.set_aspect("equal"); ax.axis("off")
    ax.text(0, -2.50, "Area × 4; field ÷ 4; flux unchanged", ha="center", fontsize=11)
    ax.set_title("Cross-sections of two Gaussian spheres", fontsize=12)
    fig.suptitle("Gauss' law constrains flux, not each local field value", fontsize=15)
    fig.text(.5, .025, "Outward normal determines flux sign. The arrows on the two spheres have a 4:1 magnitude ratio.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.98, bottom=.11, top=.82, wspace=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
