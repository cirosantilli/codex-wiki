"""Generate cell-wall-osmotic-experiment-logic.png in CWD; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, FancyBboxPatch, Rectangle


INK = "#233747"
MEMBRANE = "#2479a5"
WALL = "#bc7831"
FILL = "#d7edf7"


def arrow(ax, start, end, text=None, y=None, color=INK):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})
    if text:
        ax.text((start[0] + end[0]) / 2, y if y is not None else start[1] + 0.08,
                text, ha="center", va="bottom", fontsize=11, color=color)


def plant(ax, x, y, contracted):
    ax.add_patch(Rectangle((x - 0.11, y - 0.14), 0.22, 0.28,
                          facecolor="white", edgecolor=WALL, linewidth=5))
    width, height = (0.13, 0.17) if contracted else (0.204, 0.264)
    ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height,
                          facecolor=FILL, edgecolor=MEMBRANE, linewidth=2.3))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.8, 7.8), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    fig.suptitle("Wall support and osmotic challenge: experiment logic", fontsize=18, y=0.96, color=INK)
    ax.text(0.03, 0.93, "A. Plant cells: change surroundings, retain the wall", fontsize=13,
            fontweight="bold", color=INK)
    plant(ax, 0.23, 0.70, False)
    plant(ax, 0.76, 0.70, True)
    ax.text(0.23, 0.88, "Turgid cell", ha="center", color=INK)
    ax.text(0.76, 0.88, "Plasmolysis", ha="center", color=INK)
    arrow(ax, (0.38, 0.72), (0.60, 0.72), "More external\nexcluded solute", 0.75)
    arrow(ax, (0.23, 0.50), (0.23, 0.56), color=MEMBRANE)
    arrow(ax, (0.76, 0.56), (0.76, 0.50), color=MEMBRANE)
    ax.text(0.23, 0.46, "Water entry builds pressure;\nwall bears the load", ha="center", color=INK)
    ax.text(0.76, 0.46, "Water exits; contents withdraw\nfrom a retained wall", ha="center", color=INK)
    ax.plot([0.02, 0.98], [0.41, 0.41], color="#ccd5db", lw=1)
    ax.text(0.03, 0.37, "B. Susceptible bacteria: remove wall, then dilute surroundings", fontsize=13,
            fontweight="bold", color=INK)
    ax.add_patch(FancyBboxPatch((0.07, 0.16), 0.16, 0.09,
                               boxstyle="round,pad=0.006,rounding_size=0.04",
                               facecolor=FILL, edgecolor=WALL, linewidth=6))
    ax.add_patch(FancyBboxPatch((0.079, 0.166), 0.142, 0.077,
                               boxstyle="round,pad=0.006,rounding_size=0.035",
                               facecolor=FILL, edgecolor=MEMBRANE, linewidth=2))
    ax.add_patch(Ellipse((0.50, 0.205), 0.083, 0.132, facecolor=FILL,
                         edgecolor=MEMBRANE, lw=2.5))
    for angle in (10, 145, 270):
        ax.add_patch(Arc((0.87, 0.22), 0.107, 0.14, theta1=angle, theta2=angle + 65,
                         color=MEMBRANE, lw=2.5))
    for x, y in [(0.83, 0.18), (0.90, 0.23), (0.93, 0.16), (0.87, 0.28)]:
        ax.add_patch(Circle((x, y), 0.006, facecolor=MEMBRANE, edgecolor="none"))
    arrow(ax, (0.26, 0.205), (0.41, 0.205), "Lysozyme +\nosmotic support", 0.265)
    arrow(ax, (0.59, 0.205), (0.76, 0.205), "Dilute external\nsupporting solute", 0.265)
    ax.text(0.15, 0.09, "Walled starting cell", ha="center", color=INK)
    ax.text(0.50, 0.09, "Supported protoplast:\nmembrane retained", ha="center", color=INK)
    ax.text(0.87, 0.09, "Osmotic lysis:\nrupture and release", ha="center", color=INK)
    fig.text(0.5, 0.045, "Orange = wall     Blue outline = membrane     Blue arrows = possible net water movement",
             ha="center", fontsize=10, color=INK)
    fig.text(0.5, 0.018, "Qualitative schematics, not measured data. Lysis depends on susceptibility and experimental conditions.",
             ha="center", fontsize=10, color=INK)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.91, bottom=0.09)
    fig.savefig(Path.cwd() / "cell-wall-osmotic-experiment-logic.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
