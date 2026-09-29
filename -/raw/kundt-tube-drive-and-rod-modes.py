"""Original functional Kundt-tube and free-end rod-mode diagrams.

Run from the desired output directory; writes this script's basename as PNG.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def rod_mode(x, mode):
    """Axial displacement of a uniform free-end rod, x in units of its length."""
    return np.cos(mode * np.pi * np.asarray(x))


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig = plt.figure(figsize=(11, 6.6), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=(1.3, 1), hspace=0.47)
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    ax.set_title("A. Electronic drive and a movable pressure probe", loc="left")
    ax.add_patch(Rectangle((2, 1.1), 6.7, 1.2, fill=False, lw=2))
    ax.add_patch(Rectangle((1.65, 1.1), 0.35, 1.2, color="#555555"))
    ax.text(1.45, 0.72, "driver", ha="center")
    xx = np.linspace(2.1, 8.5, 400)
    ax.plot(xx, 1.7 + 0.28 * np.cos(2 * np.pi * (xx - 2) / 2.2),
            color="#0072B2", alpha=0.65, lw=1.5)
    ax.text(3.5, 2.5, "air column", ha="center")
    ax.add_patch(Rectangle((0.15, 2.75), 1.85, 0.65,
                           facecolor="#E8F1F7", edgecolor="#0072B2"))
    ax.text(1.075, 3.075, "frequency source", ha="center", va="center")
    ax.add_patch(FancyArrowPatch((1.075, 2.75), (1.78, 2.3),
                                arrowstyle="->", mutation_scale=13))
    ax.plot([5.6, 9.2], [1.7, 1.7], color="#D55E00", lw=2)
    ax.scatter([5.6], [1.7], s=65, color="#D55E00", zorder=4)
    ax.annotate("small pressure probe", xy=(5.6, 1.7), xytext=(5.65, 3.12),
                ha="center", arrowprops={"arrowstyle": "->"})
    ax.annotate("", xy=(6.4, 2.7), xytext=(5.0, 2.7),
                arrowprops={"arrowstyle": "<->", "color": "#D55E00"})
    ax.plot([9.2, 9.2, 8.25], [1.7, 0.3, 0.3], color="#D55E00")
    ax.add_patch(Rectangle((6.35, 0.02), 1.9, 0.55,
                           facecolor="#FFF0E8", edgecolor="#D55E00"))
    ax.text(7.3, 0.295, "oscilloscope", ha="center", va="center")
    ax.plot([2, 8.7], [0.75, 0.75], color="#333333")
    for x in np.linspace(2, 8.7, 14):
        ax.plot([x, x], [0.68, 0.82], color="#333333", lw=0.8)
    ax.text(4.25, 0.32, "independent position scale", ha="center")

    x = np.linspace(0, 1, 501)
    choices = [(1, [0.5], r"$n=1$: one centre support", r"$\lambda_r=2\ell$"),
               (2, [0.25, 0.75], r"$n=2$: two quarter supports", r"$\lambda_r=\ell$")]
    for col, (mode, supports, title, wavelength) in enumerate(choices):
        panel = fig.add_subplot(grid[1, col])
        panel.axhline(0, color="#777777", lw=1)
        panel.plot(x, rod_mode(x, mode), color="#0072B2", lw=2.2)
        for support in supports:
            panel.scatter([support], [0], marker="^", s=110,
                          color="#444444", zorder=4)
            panel.axvline(support, color="#777777", lw=0.8, ls=":")
        panel.set(xlim=(0, 1), ylim=(-1.2, 1.35),
                  xlabel=r"position along rod, $x/\ell$",
                  ylabel="axial displacement / amplitude")
        panel.set_title(("B. " if col == 0 else "C. ") + title, loc="left")
        panel.text(0.5, 1.12, wavelength, ha="center")
        panel.set_xticks([0, 0.25, 0.5, 0.75, 1])
        panel.grid(alpha=0.18)
    fig.suptitle("Kundt tube: identify the detector and the selected rod mode",
                 fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.09, top=0.89)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
