"""Draw a functional LIGO optical/readout diagram; emit PNG in the CWD.

Python 3.14, matplotlib 3.10.7. Original layout, no measured data.
Apparatus reference: Advanced LIGO, arXiv:1411.4547, sections 2, 4.4, 4.8.
The feedback reconstruction is the ideal linear model in gravitational-wave.bigb.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


BLUE = "#17649c"
RED = "#b33435"
INK = "#243342"


def arrow(ax, start, end, color=INK, dashed=False, both=False):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="<->" if both else "->",
                                mutation_scale=12, lw=1.6, color=color,
                                linestyle="--" if dashed else "-"))


def box(ax, xy, width, height, text, color=INK, size=10):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.05",
                              facecolor="white", edgecolor=color, lw=1.4))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=size, color=color)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(11.5, 8.2), facecolor="white")
    ax = fig.add_axes((0.035, 0.39, 0.93, 0.53))
    ax.set(xlim=(0, 12), ylim=(0, 8.5))
    ax.axis("off")
    fig.suptitle("Differential strain → light → calibrated strain", fontsize=18, y=0.97)
    ax.text(0.1, 8.15, "A. Functional optics (not to scale)", weight="bold", color=INK)

    box(ax, (0.2, 2.65), 1.65, 0.8, "Stabilized\nlaser", BLUE)
    arrow(ax, (1.9, 3.05), (4.8, 3.05), BLUE)
    ax.plot([3.0, 3.0], [2.65, 3.45], color=INK, lw=3)
    ax.text(2.9, 2.25, "Power recycling", ha="center", fontsize=10)
    ax.plot([4.7, 5.3], [2.75, 3.35], color=INK, lw=3)
    ax.text(4.95, 3.65, "Beam splitter", ha="right", fontsize=10)

    arrow(ax, (5.2, 3.05), (11.1, 3.05), BLUE, both=True)
    arrow(ax, (5.0, 3.25), (5.0, 7.65), BLUE, both=True)
    for x in (6.7, 11.1):
        ax.plot([x, x], [2.65, 3.45], color=INK, lw=4)
        ax.plot([x, x], [3.48, 4.0], color="#788a99", lw=1)
        ax.plot([x - 0.22, x + 0.22], [4.0, 4.0], color="#788a99", lw=2)
    for y in (4.9, 7.65):
        ax.plot([4.65, 5.35], [y, y], color=INK, lw=4)
        ax.plot([5.4, 5.8], [y, y + 0.32], color="#788a99", lw=1)
        ax.plot([5.65, 5.95], [y + 0.32, y + 0.32], color="#788a99", lw=2)
    ax.text(8.85, 4.2, "x arm: resonant cavity ≈ 4 km", ha="center", color=BLUE)
    ax.text(8.85, 2.45, r"$\delta L_x = +Lh_+/2$", ha="center", color=BLUE)
    ax.text(4.1, 6.25, "y arm\nresonant\ncavity\n≈ 4 km", ha="right", va="center", color=BLUE)
    ax.text(6.1, 6.35, r"$\delta L_y = -Lh_+/2$", color=BLUE)
    ax.text(7.0, 7.7, "Illustrated: normal incidence,\nplus polarization along the arms", fontsize=10, va="top")
    ax.text(6.9, 5.3, "Suspended mirrors\non isolated platforms; vacuum", fontsize=10)
    arrow(ax, (5.0, 2.85), (5.0, 0.85), RED)
    ax.plot([4.65, 5.35], [2.05, 2.05], color=INK, lw=3)
    ax.text(4.35, 1.85, "Signal\nrecycling", ha="right", va="center", fontsize=10)
    box(ax, (4.1, 0.05), 1.8, 0.75, "Output filter", RED)
    arrow(ax, (5.95, 0.425), (7.0, 0.425), RED)
    box(ax, (7.05, 0.05), 1.65, 0.75, "Photodetector", RED)
    ax.text(9.0, 0.42, r"$P = |E_{\rm ref}+E_{\rm sig}|^2$", va="center", color=RED)
    ax.text(0.2, 0.35, "Small offset supplies\nreference light", color=RED, fontsize=10)

    bx = fig.add_axes((0.045, 0.055, 0.91, 0.29))
    bx.set(xlim=(0, 12), ylim=(0, 4))
    bx.axis("off")
    bx.text(0, 3.72, "B. Locking the optics preserves a recoverable signal", weight="bold", color=INK)
    bx.text(0.08, 2.7, r"$x_{\rm ext}$", ha="left", va="center", color=BLUE)
    arrow(bx, (0.85, 2.7), (1.6, 2.7), BLUE)
    bx.add_patch(Circle((1.85, 2.7), 0.23, fill=False, color=INK, lw=1.5))
    bx.text(1.85, 2.7, "+", ha="center", va="center")
    arrow(bx, (2.1, 2.7), (3.1, 2.7))
    bx.text(2.58, 3.05, r"$x_{\rm res}$", ha="center", fontsize=10)
    box(bx, (3.15, 2.25), 1.8, 0.9, "Sensing C", RED)
    arrow(bx, (5.0, 2.7), (6.15, 2.7), RED)
    bx.text(5.57, 3.05, r"$d_{\rm err}$", ha="center", color=RED)
    box(bx, (6.2, 2.25), 1.8, 0.9, "Controller")
    arrow(bx, (8.05, 2.7), (9.3, 2.7))
    bx.text(8.65, 3.05, r"$d_{\rm ctrl}$", ha="center")
    box(bx, (9.35, 2.25), 1.8, 0.9, "Actuation A")
    bx.plot([11.2, 11.65, 11.65, 1.85], [2.7, 2.7, 1.55, 1.55], color=INK, lw=1.5)
    arrow(bx, (1.85, 1.55), (1.85, 2.45))
    bx.text(2.1, 1.95, "−", fontsize=13)
    bx.text(6.8, 1.15, "Recorded residual + recorded compensation", ha="center", color=INK)
    bx.text(6.0, 0.35, r"$\widetilde h_D=(C^{-1}\widetilde d_{\rm err}+A\widetilde d_{\rm ctrl})/L$",
            ha="center", va="center", fontsize=15, color=BLUE)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
