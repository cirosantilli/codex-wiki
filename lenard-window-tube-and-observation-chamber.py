"""Generate an original functional Lenard-window teaching diagram.

Tested with Python 3.14 and matplotlib 3.10.7. Run from _media;
the opaque PNG is written to the current directory. No historical scale.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def arrow(ax, start, end, color="#225ea8", lw=2, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=13, color=color, lw=lw))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 6.6), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.5, 1], hspace=0.40, wspace=0.14)
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 11), ylim=(0, 4))
    ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.9), 4.4, 2.1, fc="#eff6fc", ec="#536778", lw=2))
    ax.add_patch(Rectangle((4.95, 0.9), 5.4, 2.1, fc="#fafafa", ec="#536778", lw=2))
    ax.text(2.7, 3.28, "Production chamber: low-pressure discharge", ha="center", weight="bold")
    ax.text(7.7, 3.28, "Observation chamber: gas or vacuum", ha="center", weight="bold")
    ax.plot([1.2, 1.2], [1.35, 2.6], color="#333333", lw=6)
    ax.text(1.2, 1.15, "Cathode (−)", ha="center")
    ax.plot([2.9, 2.9], [2.60, 2.95], color="#333333", lw=5)
    ax.text(2.9, 2.37, "Anode (+)\n(clear of beam)", ha="center", fontsize=10)
    ax.plot([1.2, 1.2, 2.9], [2.6, 3.02, 3.02], color="#606060", lw=1)
    ax.text(1.9, 3.04, "Voltage supply", ha="center", va="bottom", fontsize=9)
    ax.plot([4.91, 4.91], [0.9, 1.73], color="#606060", lw=7)
    ax.plot([4.91, 4.91], [2.23, 3], color="#606060", lw=7)
    ax.plot([4.91, 4.91], [1.73, 2.23], color="#e89b28", lw=4)
    ax.annotate("Thin aluminium window\nseals a small opening", xy=(4.91, 2.1),
                xytext=(5.7, 3.66), ha="center", fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#8c5a0a"})
    arrow(ax, (1.4, 1.98), (4.65, 1.98))
    ax.text(3.05, 1.70, "Cathode rays (electrons)", ha="center", fontsize=10, color="#225ea8")
    for y in (1.42, 1.70, 1.98, 2.26, 2.54):
        arrow(ax, (5.03, 1.98), (9.15, y), lw=1.4)
    ax.add_patch(Rectangle((9.28, 1.15), 0.18, 1.65, fc="#abdda4", ec="#238443", lw=1.5))
    ax.scatter([9.29]*5, [1.42, 1.70, 1.98, 2.26, 2.54], s=[18, 40, 70, 40, 18],
               color="#238443", zorder=5)
    ax.text(9.68, 1.98, "Coated\nscreen", va="center", fontsize=10)
    arrow(ax, (5.15, 0.62), (9.25, 0.62), color="#555555", lw=1, style="<->")
    ax.text(7.2, 0.36, "Change distance; record patch width and brightness", ha="center", fontsize=10)
    for x, label in ((0.8, "Source pump"), (10.05, "Separate pump / gas inlet")):
        ax.plot([x, x], [0.9, 0.57], color="#536778", lw=2)
        ax.text(x, 0.45 if x < 1 else 0.04, label,
                ha="left" if x < 1 else "right", va="top", fontsize=9)

    for index, (title, spread) in enumerate((("Ideal evacuated path: narrow patch", False),
                                             ("Gas: redistribution broadens the patch", True))):
        panel = fig.add_subplot(grid[1, index])
        panel.set(xlim=(0, 5), ylim=(0, 2))
        panel.axis("off")
        panel.set_title(title, fontsize=11, loc="left", pad=5)
        panel.plot([0.9, 0.9], [0.15, 0.85], color="#555555", lw=5)
        panel.plot([0.9, 0.9], [1.15, 1.85], color="#555555", lw=5)
        panel.text(0.9, 0, "Aperture", ha="center", va="top", fontsize=10)
        panel.plot([4.25, 4.25], [0.18, 1.82], color="#238443", lw=5)
        panel.text(4.25, 0, "Screen", ha="center", va="top", fontsize=10)
        arrow(panel, (0.1, 1), (0.75, 1), lw=1.5)
        if spread:
            for d in (-0.60, -0.32, 0, 0.32, 0.60):
                panel.plot([1, 1.7, 2.5, 3.25, 4.20],
                           [1, 1+0.10*d, 1+0.5*d, 1+0.65*d, 1+d],
                           color="#225ea8", lw=1.3)
                panel.scatter([4.2], [1+d], s=40, color="#238443", zorder=4)
            panel.text(2.6, 1.82, "Illustrative paths", fontsize=9, ha="center", color="#555555")
        else:
            for d in (-0.06, 0, 0.06):
                arrow(panel, (1, 1+d), (4.15, 1+d), lw=1.3)
            panel.scatter([4.2], [1], s=90, color="#238443", zorder=4)
    fig.suptitle("A window separates production from propagation", fontsize=16, weight="bold", y=0.98)
    fig.text(0.5, 0.015, "Functional teaching schematic • no historical dimensions, voltages or measured trajectories",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(top=0.86, bottom=0.12, left=0.035, right=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
