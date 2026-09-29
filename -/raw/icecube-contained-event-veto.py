"""Draw a functional veto schematic; Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.

Run from _media; writes the matching PNG to the current directory.
Positions are schematic, not IceCube geometry or measured event coordinates.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def arrow(ax, start, end, color, dashed=False, width=2.2):
    ax.annotate("", end, start,
                arrowprops=dict(arrowstyle="->", color=color, lw=width,
                                linestyle="--" if dashed else "-"))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.6), dpi=110)
    fig.patch.set_facecolor("white")
    titles = ["Entering muon", "Contained interaction", "Atmospheric companion"]
    blue, orange, purple = "#176aa1", "#c45516", "#7153a3"
    for ax, title in zip(axes, titles):
        ax.set(xlim=(0, 10), ylim=(0, 12))
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=13, weight="bold", pad=8)
        ax.add_patch(Rectangle((0.6, 1.7), 8.8, 7.8, facecolor="#e9f3f7",
                               edgecolor="#718a99", linewidth=1.4))
        ax.add_patch(Rectangle((2.1, 3), 5.8, 5.1, facecolor="white",
                               edgecolor="#718a99", linestyle="--"))
        for x in np.linspace(1.3, 8.7, 5):
            ax.plot([x, x], [2.2, 9], color="#c7d4dd", lw=0.7)
            for y in np.linspace(2.2, 9, 6):
                ax.add_patch(Circle((x, y), 0.095, color="#687f8c"))
        ax.text(5, 0.9, "Boundary veto / interior", ha="center", color="#425967")

    arrow(axes[0], (2.5, 11.5), (6.8, 2.1), orange)
    axes[0].plot(3.46, 9.4, "o", color=orange, ms=10)
    axes[0].text(0.8, 10.3, "Early boundary light", color=orange)
    axes[0].text(5, 4.4, "Later track light", ha="center", color=orange,
                 bbox=dict(facecolor="white", edgecolor="none", pad=2))
    axes[0].text(5, 0, "VETO", ha="center", color=orange, weight="bold", fontsize=13)

    vertex = (4.8, 5.5)
    arrow(axes[1], (0.5, 11.2), vertex, blue, dashed=True)
    axes[1].text(0.4, 10.6, r"$\nu$", color=blue, fontsize=16)
    axes[1].plot(*vertex, "*", ms=19, color=blue, zorder=5)
    for angle in np.linspace(0, 2 * np.pi, 10, endpoint=False):
        end = (vertex[0] + 1.4 * np.cos(angle), vertex[1] + 1.4 * np.sin(angle))
        arrow(axes[1], vertex, end, "#62a9cf", width=1)
    axes[1].text(5, 3.5, "Shower light", color=blue, ha="center")
    axes[1].text(5, 0, "CANDIDATE", ha="center", color=blue, weight="bold", fontsize=13)

    arrow(axes[2], (3, 11.5), (4.8, 5.5), blue, dashed=True)
    arrow(axes[2], (6.1, 11.5), (7.3, 2.2), orange)
    axes[2].text(4.7, 11.5, r"$\nu\quad\mu$", ha="center", fontsize=15)
    axes[2].plot(6.37, 9.4, "o", color=orange, ms=10)
    axes[2].plot(4.8, 5.5, "*", color=blue, ms=19)
    axes[2].text(5, 3.5, "Real neutrino; vetoed", ha="center", color=purple,
                 bbox=dict(facecolor="white", edgecolor="none", pad=2))
    axes[2].text(5, 0, "VETO", ha="center", color=orange, weight="bold", fontsize=13)

    fig.suptitle("Where does the first light appear?", fontsize=17, weight="bold", y=0.98)
    fig.text(0.5, 0.065, "Light → photomultiplier → digitized charge + time → event reconstruction",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Functional schematic • dashed: incoming neutrino • solid: muon • not to scale",
             ha="center", fontsize=10, color="#4c5962")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.13, top=0.87, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
