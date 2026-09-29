"""Original qualitative Lyot coronagraph schematic; output PNG to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Shapes illustrate optical planes, not measured or computed irradiance.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.6, 4.6), facecolor="white")
    centers = [0.13, 0.375, 0.62, 0.865]
    titles = ["1  Entrance pupil", "2  Focal plane", "3  Reimaged pupil", "4  Final image"]
    notes = ["Uniform incident field\ninside a finite aperture",
             "Opaque mask blocks core;\nouter rings remain",
             "Lyot stop clips rim field;\ninterior leakage remains",
             "Fainter stellar rings;\nnearby light can pass"]
    for j, (cx, title, note) in enumerate(zip(centers, titles, notes)):
        ax = fig.add_axes([cx - .105, .30, .21, .48])
        ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12, pad=11)
        if j == 0:
            ax.add_patch(Circle((0, 0), 1, facecolor="#bad9ef", edgecolor="#245e87", lw=2))
            for x in [-.55, 0, .55]:
                for y in [-.55, 0, .55]:
                    ax.plot(x, y, ".", color="#245e87", ms=5)
        elif j == 1:
            for r, alpha in [(.51, .9), (.76, .65), (1.02, .4)]:
                ax.add_patch(Circle((0, 0), r, fill=False, edgecolor="#d07a16", alpha=alpha, lw=3))
            ax.add_patch(Circle((0, 0), .35, facecolor="#30343b", edgecolor="#30343b"))
            ax.annotate("mask", (0, 0), (.45, -1.17), arrowprops={"arrowstyle": "->", "color": "#30343b"}, fontsize=10)
        elif j == 2:
            ax.add_patch(Circle((0, 0), 1, facecolor="#ededed", edgecolor="#30343b", hatch="////", lw=1))
            ax.add_patch(Circle((0, 0), .83, facecolor="#f5d5a4", edgecolor="#d07a16", lw=8))
            ax.add_patch(Circle((0, 0), .69, facecolor="#fffaf3", edgecolor="#245e87", lw=2))
            ax.text(0, 0, "passes", ha="center", va="center", color="#245e87", fontsize=10)
            ax.annotate("blocked rim", (.9, -.6), (0, -1.17), ha="center", arrowprops={"arrowstyle": "->"}, fontsize=10)
        else:
            for r, alpha in [(.18, .4), (.51, .35), (.76, .25), (1.02, .15)]:
                ax.add_patch(Circle((0, 0), r, fill=False, edgecolor="#d07a16", alpha=alpha, lw=2))
            ax.plot(.93, .73, "o", color="#245e87", ms=6)
            ax.annotate("off-axis source", (.93, .73), (-.1, 1.12), ha="center", fontsize=9,
                        arrowprops={"arrowstyle": "->", "color": "#245e87"})
        fig.text(cx, .245, note, ha="center", va="top", fontsize=10.5, linespacing=1.5)
    for left, right, label in zip(centers[:-1], centers[1:], ["focus", "relay pupil", "focus"]):
        fig.add_artist(FancyArrowPatch((left + .105, .55), (right - .105, .55),
                       transform=fig.transFigure, arrowstyle="->", mutation_scale=14, color="#30343b"))
        fig.text((left + right) / 2, .49, label, ha="center", fontsize=8.5)
    fig.suptitle("A Lyot coronagraph selects light in two different planes", fontsize=15, y=.96)
    fig.text(.5, .065, "Qualitative schematic: sizes and brightness are illustrative; relay lenses are omitted.",
             ha="center", fontsize=10, color="#454545")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
