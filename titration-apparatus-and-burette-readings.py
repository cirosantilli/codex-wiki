"""Original apparatus and volume-reading schematic. Run from _media with
Python 3.14 and Matplotlib 3.10.7; emit basename.png in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np


INK = "#253749"
BLUE = "#126594"
WATER = "#d9edf8"


def arrow(ax, label, target, text, **kwargs):
    ax.annotate(label, xy=target, xytext=text, fontsize=10, color=INK,
                arrowprops={"arrowstyle": "->", "color": INK, "lw": 1},
                **kwargs)


def reading(ax, x0, start, name):
    # Scale represents start+0.00 to start+0.60 mL; reading is start+0.35.
    top, step = 7.2, 0.7
    surface = top - 3.5 * step
    ax.add_patch(Rectangle((x0, 2.5), 1.0, 5.1, facecolor="white",
                           edgecolor=INK, linewidth=1.5))
    x = np.linspace(x0 + 0.05, x0 + 0.95, 101)
    y = surface + 0.30 * ((x - x0 - 0.5) / 0.45) ** 2
    ax.fill_between(x, 2.52, y, color=WATER)
    ax.plot(x, y, color=BLUE, lw=2)
    for j in range(7):
        yj = top - j * step
        ax.plot([x0 + 0.68, x0 + 1.0], [yj, yj], color=INK, lw=1)
        ax.text(x0 + 1.15, yj, f"{start + j / 10:.1f}", fontsize=10,
                va="center", color=INK)
    ax.plot([x0 - 0.25, x0 + 1.05], [surface, surface], ls="--",
            color="#a3452c", lw=1)
    ax.text(x0 + 0.5, 8.0, name, ha="center", fontsize=12, color=INK)
    ax.text(x0 + 0.55, 1.85, f"{start + 0.35:.2f} mL", ha="center",
            fontsize=13, fontweight="bold", color=BLUE)
    arrow(ax, "Bottom", (x0 + 0.5, surface), (x0 - 0.7, surface - 1.0))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=120,
                             gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Titration: a sample aliquot and a difference in readings",
                 fontsize=16, y=0.97)
    fig.text(0.5, 0.905, "Original schematic and illustrative readings; "
             "not experimental data", ha="center", fontsize=11)
    ax = axes[0]
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.add_patch(Rectangle((0.6, 0.4), 4.3, 0.3, color="#aeb8c0"))
    ax.plot([1.2, 1.2], [0.7, 9.4], color=INK, lw=4)
    ax.plot([1.2, 4.35], [7.5, 7.5], color=INK, lw=3)
    ax.add_patch(Rectangle((4.0, 4.6), 0.55, 4.6, edgecolor=INK,
                           facecolor="white", lw=1.5))
    ax.add_patch(Rectangle((4.02, 4.65), 0.51, 3.5, facecolor=WATER,
                           edgecolor="none"))
    for y in np.linspace(4.9, 8.95, 21):
        ax.plot([4.31, 4.53], [y, y], color=INK, lw=0.75)
    ax.plot([3.7, 4.8], [4.6, 4.6], lw=2.5, color=INK)
    ax.plot([4.27, 4.27], [4.6, 3.9], lw=1.8, color=INK)
    ax.add_patch(Ellipse((4.27, 3.65), 0.1, 0.2, facecolor=BLUE))
    # Beaker allows electrode immersion; scale and geometry are schematic.
    ax.plot([3.0, 3.0, 6.0, 6.0], [3.4, 1.15, 1.15, 3.4], lw=1.5, color=INK)
    ax.add_patch(Rectangle((3.03, 1.18), 2.94, 1.4, facecolor=WATER,
                           edgecolor="none"))
    ax.add_patch(Ellipse((4.5, 1.4), 0.8, 0.15, facecolor=INK))
    ax.add_patch(Rectangle((2.8, 0.72), 3.5, 0.35, facecolor="#c8d0d6"))
    ax.plot([5.3, 5.3], [2.0, 4.2], color="#d98937", lw=5)
    ax.plot([5.3, 5.3, 7.5], [4.2, 5.0, 5.0], color=INK, lw=1.2)
    ax.add_patch(Rectangle((7.5, 4.6), 1.5, 0.8, facecolor="white",
                           edgecolor=INK, lw=1.2))
    ax.text(8.25, 5.0, "pH meter", ha="center", va="center", fontsize=9)
    arrow(ax, "Burette: titrant", (4.55, 8.6), (5.5, 8.5))
    arrow(ax, "Stopcock", (4.6, 4.6), (1.8, 4.9))
    arrow(ax, "Optional glass\nelectrode", (5.3, 3.2), (6.4, 3.3))
    arrow(ax, "Pipetted sample\naliquot", (3.4, 2.2), (0.25, 2.4))
    arrow(ax, "Mixing bar", (4.5, 1.4), (6.8, 1.6))
    ax.text(4.5, 0.2, "Tip filled; delivered drops enter the sample", ha="center",
            fontsize=9, color=INK)
    ax = axes[1]
    ax.set(xlim=(0, 8.3), ylim=(0, 10))
    reading(ax, 1.0, 2.0, "Initial reading")
    reading(ax, 5.0, 12.0, "Final reading")
    ax.text(4.1, 9.0, "Read at eye level; scale increases downward", fontsize=10,
            ha="center", color=INK)
    ax.text(4.1, 0.65, "12.35 − 2.35 = 10.00 mL delivered", fontsize=12,
            ha="center", fontweight="bold", color=BLUE)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axis("off")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.05, top=0.83, wspace=0.05)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
