"""Gas electron diffraction apparatus and a rigid pair-distance inference.

Original schematic; no measured or simulated detector intensity is displayed.
Apparatus follows Reuter et al. (2016), DOI 10.1515/znb-2015-0186, and
the Wann group's authored experiment account, both cited in chemistry.bigb.
The lower triangle is a normalized construction using water's 104.4776-degree
equilibrium angle from NIST, not a geometry measurement made with this setup.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Write the opaque white same-basename PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyBboxPatch, Rectangle
import numpy as np

INK = "#243342"
BLUE = "#2868a5"
ORANGE = "#b45d16"
GREEN = "#287e61"


def arrow(ax, start, end, colour=BLUE, lw=2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": colour, "lw": lw})


def box(ax, x, y, w, h, text):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                               ec="#a4adb7", fc="white", lw=1.3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=11)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": INK})
    fig = plt.figure(figsize=(10, 6.6), facecolor="white")
    fig.suptitle("From electron scattering to a molecular bond angle", y=0.97,
                 fontsize=17, weight="bold")
    ax = fig.add_axes([0.035, 0.49, 0.93, 0.40])
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    ax.add_patch(Rectangle((2.5, 0.3), 7.1, 3.35, fc="white", ec="#a4adb7", lw=1.2))
    ax.text(2.7, 0.46, "vacuum chamber · pumps and cold trap", fontsize=10)
    box(ax, 0.2, 1.55, 1.75, 1, "hot cathode\nelectron gun")
    arrow(ax, (1.95, 2.05), (4.5, 2.05))
    ax.plot([2.8, 2.8], [1.65, 2.45], color=INK, lw=2)
    ax.plot([3.35, 3.35], [1.65, 2.45], color=INK, lw=2)
    ax.text(3.07, 2.63, "beam shaping", ha="center", fontsize=9)
    ax.add_patch(Rectangle((4.35, 3.15), 0.6, 0.35, fc="white", ec=ORANGE, lw=2))
    arrow(ax, (4.65, 3.1), (4.65, 2.1), ORANGE)
    ax.text(4.65, 3.75, "sample vapour nozzle", ha="center", color=ORANGE, fontsize=10)
    ax.add_patch(Circle((4.65, 2.05), 0.075, fc=ORANGE, ec=ORANGE))
    arrow(ax, (4.8, 2.05), (7.05, 2.05), BLUE)
    ax.add_patch(Rectangle((7.12, 1.83), 0.25, 0.44, fc=INK, ec=INK))
    ax.text(7.25, 1.48, "beam stop", ha="center", fontsize=10)
    for end_y in [0.95, 1.45, 2.65, 3.15]:
        arrow(ax, (4.7, 2.05), (8.6, end_y), GREEN, lw=1.4)
    ax.text(6.5, 3.32, "scattered electrons", color=GREEN, fontsize=10)
    ax.add_patch(Rectangle((8.65, 0.85), 0.23, 2.4, fc="white", ec=GREEN, lw=2))
    ax.text(9.17, 2.05, "imaging\nplate", ha="center", color=GREEN, fontsize=10)
    ax.text(5, 0.01, "Apparatus schematic only; detector data are not drawn", ha="center", fontsize=10)

    flow = fig.add_axes([0.045, 0.10, 0.49, 0.33])
    flow.set(xlim=(0, 5), ylim=(0, 3.1))
    flow.axis("off")
    box(flow, 0.2, 2.15, 4.5, 0.62, "Read calibrated detector signal vs position")
    arrow(flow, (2.45, 2.0), (2.45, 1.82), INK, lw=1.5)
    box(flow, 0.2, 1.03, 4.5, 0.62, "Extract molecular intensity; fit pair distances")
    arrow(flow, (2.45, 0.88), (2.45, 0.65), INK, lw=1.5)
    flow.text(2.45, 0.42, "Geometry converts consistent distances to angles", ha="center", fontsize=11)
    flow.text(2.45, 0.03, "The fitted model and nuclear-motion corrections matter", ha="center", fontsize=9)

    geo = fig.add_axes([0.59, 0.095, 0.37, 0.34])
    geo.set(xlim=(-1.45, 1.45), ylim=(-1.2, 1.32), aspect="equal")
    geo.axis("off")
    half = np.deg2rad(104.4776 / 2)
    x, y = np.sin(half), -np.cos(half)
    geo.plot([-x, 0, x], [y, 0, y], color=BLUE, lw=2.5)
    geo.plot([-x, x], [y, y], ":", color=GREEN, lw=2)
    for pos, label, colour in [((0, 0), "O", ORANGE), ((-x, y), "H", BLUE), ((x, y), "H", BLUE)]:
        geo.add_patch(Circle(pos, 0.11, fc="white", ec=colour, lw=2, zorder=4))
        geo.text(*pos, label, ha="center", va="center", color=colour, fontsize=10, zorder=5)
    geo.add_patch(Arc((0, 0), 0.66, 0.66, theta1=270 - 104.4776 / 2,
                      theta2=270 + 104.4776 / 2, ec=INK, lw=1.5))
    geo.text(0, -0.27, r"$\theta$", ha="center", fontsize=12)
    geo.text(-0.56, -0.17, r"$b=1$", ha="center", fontsize=11)
    geo.text(0.56, -0.17, r"$b=1$", ha="center", fontsize=11)
    geo.text(0, y - 0.22, r"$d=2b\sin(\theta/2)\approx1.5811$", ha="center", fontsize=11, color=GREEN)
    geo.text(0, 0.68, "Normalized rigid geometry", ha="center", weight="bold", fontsize=11)
    geo.text(0, 0.43, "104.4776° input · lengths arbitrary", ha="center", fontsize=9)
    fig.text(0.5, 0.032, "Constructed explanation, not observed diffraction or measured distances",
             ha="center", fontsize=10, color=ORANGE)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
