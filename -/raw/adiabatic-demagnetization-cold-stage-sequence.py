"""Draw a functional magnetic refrigerator; Python 3.14, matplotlib 3.10.7.

Run from _media; writes only this script's basename.png to the current directory.
The geometry is original and functional, not a historical apparatus drawing.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def box(ax, xy, size, text, color):
    ax.add_patch(FancyBboxPatch(xy, *size, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="#30465a", linewidth=1.5))
    ax.text(xy[0] + size[0] / 2, xy[1] + size[1] / 2, text,
            ha="center", va="center", fontsize=11, linespacing=1.5)


def arrow(ax, a, b, color="#30465a", lw=2):
    ax.annotate("", b, a, arrowprops=dict(arrowstyle="->", lw=lw, color=color))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(11, 6.8), facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.5, 1], hspace=0.22, wspace=0.12)
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 11), ylim=(0, 4.2))
    ax.axis("off")
    ax.text(5.5, 4.03, "A cold stage with a controllable thermal link", ha="center",
            fontsize=16, weight="bold")
    box(ax, (0.25, 1.25), (2.0, 1.1), "Cold heat bath\nmaintains $T_b$", "#deedf8")
    ax.add_patch(Rectangle((4.4, 0.6), 6.35, 2.9, facecolor="#f5f7f9",
                           edgecolor="#93a4b3", linestyle="--", linewidth=1.4))
    ax.text(5.93, 3.2, "Cold-stage boundary", ha="center", color="#4e6171")
    box(ax, (4.95, 1.25), (1.95, 1.1), "Magnetic\nrefrigerant", "#e5f2df")
    ax.plot([2.25, 2.95], [1.8, 1.8], color="#bc7424", lw=4)
    ax.plot([3.65, 4.95], [1.8, 1.8], color="#bc7424", lw=4)
    ax.plot([2.95, 3.62], [1.8, 2.16], color="#bc7424", lw=3)
    ax.scatter([2.95, 3.65], [1.8, 1.8], s=30, c="#bc7424", zorder=3)
    ax.text(3.35, 2.65, "Heat switch", ha="center", weight="bold")
    ax.text(3.25, 0.94, "Closed: exports heat\nOpen: suppresses heat flow", ha="center", fontsize=10)
    box(ax, (8.5, 1.25), (2.0, 1.1), "Load +\nthermometer", "#fcebd5")
    ax.plot([6.9, 8.5], [1.8, 1.8], color="#bc7424", lw=4)
    ax.text(7.73, 1.02, "Thermal\ncontact", ha="center", fontsize=10)
    arrow(ax, (5.1, 0.32), (6.75, 0.32), color="#674c94")
    ax.text(5.93, -0.04, "Applied field $B$", ha="center", fontsize=10, color="#674c94")
    ax.text(9.35, 3.33, "Sensing coil / readout", ha="center", fontsize=10)
    ax.add_patch(Rectangle((4.7, 1.0), 2.45, 1.65, fill=False,
                           edgecolor="#386983", linestyle=":", linewidth=1.8))
    ax.plot([7.15, 8.1, 8.1], [2.65, 2.65, 3.25], color="#386983", linestyle=":", lw=1.8)
    ax.text(0.3, 3.3, "Functional layout\n(no geometric scale)", color="#4e6171", fontsize=10)
    states = [
        ("1  Prepare", "Switch CLOSED", "Raise field slowly", "$T=T_b$,  $S$ falls", "Heat goes to bath", "#deedf8"),
        ("2  Isolate", "Switch OPEN", "Hold high field", "Bath link suppressed", "Stage initially at $T_b$", "#f0eafa"),
        ("3  Cool", "Switch OPEN", "Lower field slowly", "$T$ falls,  $S$ fixed*", "Then absorb load heat", "#e5f2df"),
    ]
    for i, (title, switch, field, result, foot, color) in enumerate(states):
        a = fig.add_subplot(grid[1, i])
        a.set(xlim=(0, 1), ylim=(0, 1))
        a.axis("off")
        box(a, (0.03, 0.08), (0.93, 0.86), "", color)
        a.text(0.5, 0.8, title, fontsize=14, weight="bold", ha="center")
        a.text(0.5, 0.62, switch, ha="center", weight="bold", fontsize=11)
        a.text(0.5, 0.45, field, ha="center", fontsize=11)
        a.text(0.5, 0.29, result, ha="center", fontsize=11)
        a.text(0.5, 0.14, foot, ha="center", fontsize=10)
    fig.text(0.5, 0.035, "*Constant total entropy requires negligible heat leaks and entropy production, with internal equilibrium.",
             ha="center", fontsize=10, color="#384c5e")
    fig.subplots_adjust(left=0.035, right=0.98, top=0.97, bottom=0.1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
