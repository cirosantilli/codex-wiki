"""Original channel cartoon; writes an opaque PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Particle shapes, counts and dimensions are illustrative, not microscopic data.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon
import numpy as np


INK = "#263749"
BLUE = "#207ea2"
TEAL = "#b0d9d1"
GOLD = "#d48a25"
RED = "#b34445"


def ion(ax, x, y):
    ax.add_patch(Circle((x, y), .16, fc="#d7eff9", ec=BLUE, lw=1.6, zorder=4))
    ax.text(x, y, "+", color=BLUE, ha="center", va="center", fontsize=14, zorder=5)


def excluded(ax, x, y):
    ax.add_patch(Polygon([(x, y+.19), (x-.19, y-.15), (x+.19, y-.15)],
                         fc="#f7dfb3", ec=GOLD, lw=1.5, zorder=4))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(9.4, 5.6), facecolor="white")
    fig.subplots_adjust(left=.035, right=.98, top=.87, bottom=.11)
    ax.set(xlim=(0, 10), ylim=(0, 5.65), aspect="equal")
    ax.axis("off")
    fig.suptitle("An open ion channel: selective passage + electrochemical drive",
                 fontsize=14, color=INK, y=.96)

    # Interrupted bilayer; the central space is occupied by the pore protein.
    for x in np.r_[np.linspace(.3, 4.02, 13), np.linspace(6.15, 9.85, 13)]:
        for y, direction in [(3.45, -1), (2.15, 1)]:
            ax.add_patch(Circle((x, y), .105, fc="#d1dce8", ec="#7e93ab", lw=.8))
            for offset in [-.037, .037]:
                ax.plot([x+offset, x+offset+.025], [y+direction*.12, y+direction*.54],
                        color="#91a4b9", lw=1.35)
    for x in [4.25, 5.42]:
        ax.add_patch(FancyBboxPatch((x, 1.93), .5, 1.76,
                                   boxstyle="round,pad=0.04,rounding_size=0.16",
                                   fc=TEAL, ec="#427d71", lw=1.7, zorder=2))
    ax.text(1.0, 4.85, "Outside", color=INK, fontsize=12)
    ax.text(1.0, .82, "Inside", color=INK, fontsize=12)
    ax.annotate("Lipid bilayer", xy=(2.1, 2.8), xytext=(.4, 1.35),
                arrowprops={"arrowstyle": "->", "color": INK}, color=INK)
    ax.annotate("Membrane protein", xy=(5.77, 2.35), xytext=(6.8, 1.2),
                arrowprops={"arrowstyle": "->", "color": INK}, color=INK)
    ax.annotate("Open pore", xy=(5.08, 3.05), xytext=(6.9, 3.8),
                arrowprops={"arrowstyle": "->", "color": INK}, color=INK)

    for x, y in [(3.2, 4.8), (4.1, 4.9), (5.08, 4.55),
                 (5.08, 2.82), (5.08, 1.05), (3.5, .65)]:
        ion(ax, x, y)
    for y_start, y_end in [(4.3, 3.23), (2.56, 1.32)]:
        ax.annotate("", xy=(5.08, y_end), xytext=(5.08, y_start),
                    arrowprops={"arrowstyle": "-|>", "color": BLUE, "lw": 2.1}, zorder=3)
    ax.text(2.9, 5.38, "Selected positive ions", color=BLUE, fontsize=11)
    for x, y in [(6.3, 4.65), (7.7, 4.75), (8.9, 4.75)]:
        excluded(ax, x, y)
    ax.text(6.6, 5.38, "Excluded in this model", color=GOLD, fontsize=11)
    ax.plot([6.07, 5.46], [4.52, 4.06], color=RED, lw=1.5)
    ax.plot(5.46, 4.06, marker="x", color=RED, ms=9, mew=2)
    ax.text(6.5, .22, "Shown drive favors entry;\nreversed drive can favor exit.",
            color=BLUE, fontsize=10, ha="center")
    fig.text(.5, .035, "Model schematic • not microscopic data or a scale drawing • "
             "an open channel is a passive pathway, not a pump",
             ha="center", fontsize=9.5, color=INK)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
