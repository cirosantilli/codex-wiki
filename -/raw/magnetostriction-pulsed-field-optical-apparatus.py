"""Functional schematic; source: arXiv:1002.0275, Fig. 1 and methods.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; write to CWD.
Coil winding and physical optical placement are deliberately symbolic.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11, 7.2), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.02)
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis("off")
    blue, orange, ink = "#176b99", "#b85c18", "#263746"

    def box(x, y, w, h, label, color=ink):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.09",
                                   facecolor="white", edgecolor=color, lw=1.6))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=color)

    def arrow(a, b, color=blue, **kwargs):
        ax.annotate("", xy=b, xytext=a,
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.8, **kwargs))

    ax.text(6, 7.63, "Measuring magnetostrictive strain with reflected light",
            ha="center", va="center", fontsize=17, weight="bold", color=ink)
    ax.text(6, 7.17, "Functional schematic • optical routing and magnet coil are symbolic",
            ha="center", fontsize=11, color=ink)
    box(0.45, 5.6, 2.25, 0.9, "Broadband\nlight source", blue)
    box(4.25, 5.6, 2.0, 0.9, "Circulator", blue)
    box(8.1, 5.6, 3.3, 0.9, "Spectrometer\nand optical detector", blue)
    arrow((2.8, 6.05), (4.12, 6.05))
    arrow((6.38, 6.05), (7.98, 6.05))
    ax.text(7.18, 6.31, "return", ha="center", color=blue)
    ax.plot([5.1, 5.1, 3.7, 3.7, 5.2], [5.48, 4.87, 4.87, 3.18, 3.18],
            color=blue, lw=1.8)
    arrow((3.7, 4.5), (3.7, 3.65))
    arrow((3.91, 3.65), (3.91, 4.5))
    ax.text(1.55, 4.35, "Reflected wavelength\nencodes strain", ha="center", color=blue)
    ax.add_patch(FancyBboxPatch((4.3, 1.2), 4.8, 3.2, boxstyle="round,pad=0.08",
                               facecolor="white", edgecolor="#7e8d98", lw=1.5,
                               linestyle="--"))
    ax.text(8.84, 4.12, "5.4 K", ha="right", color=ink)
    for x in np.linspace(4.85, 8.2, 12):
        ax.add_patch(Ellipse((x, 2.99), 0.33, 1.32,
                             facecolor="none", edgecolor=orange, lw=1.15, zorder=1))
    ax.add_patch(Rectangle((5.0, 2.7), 3.1, 0.46, facecolor="#dae5ed",
                           edgecolor=ink, lw=1.6, zorder=3))
    ax.plot([5.2, 7.4], [3.18, 3.18], color=blue, lw=3, zorder=4)
    for x in np.linspace(5.3, 7.3, 24):
        ax.plot([x, x], [3.12, 3.24], color=blue, lw=0.7, zorder=5)
    ax.plot([8.14, 8.14], [2.54, 3.3], color=ink, lw=3, zorder=5)
    ax.text(6.3, 3.92, "Bonded 2 mm grating", color=blue, ha="center")
    ax.text(6.65, 2.02, r"GdSb: $3\times1.5\times1.5\ \mathrm{mm^3}$",
            ha="center", color=ink)
    arrow((5.45, 1.64), (7.83, 1.64), ink)
    ax.text(6.6, 1.27, r"$\Delta L\parallel B\parallel a$", ha="center", color=ink)
    ax.text(10.55, 3.52, "Pulsed coil\n(symbol)", ha="center", color=orange)
    arrow((9.8, 3.2), (8.35, 3.2), orange)
    ax.text(10.6, 2.08, "End mount\n(symbol)", ha="center", color=ink)
    arrow((9.8, 2.3), (8.21, 2.65), ink)
    ax.text(1.6, 2.6, "Readout", ha="center", weight="bold", color=blue)
    ax.text(1.6, 1.9, r"$\Delta\lambda_B/\lambda_B$" + "\n↓\n" + r"$\Delta L/L$",
            ha="center", va="center", fontsize=14, color=blue)
    ax.text(6, 0.55, "Inference requires temperature control and reliable strain transfer.",
            ha="center", color=ink, fontsize=12)
    ax.text(6, 0.12, "Original diagram • no experimental curve reproduced",
            ha="center", color="#586977", fontsize=10)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
