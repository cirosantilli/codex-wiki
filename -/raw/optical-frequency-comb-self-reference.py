"""Original functional comb diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; writes the matching PNG into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6.5))
    ax.axis("off")
    blue, orange = "#156a9c", "#a35c11"

    def box(x, y, w, h, text, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor="white", edgecolor=color, linewidth=1.5))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=11)

    def arrow(points, electronic=False):
        color = orange if electronic else blue
        for a, b in zip(points[:-2], points[1:-1]):
            ax.plot([a[0], b[0]], [a[1], b[1]], color=color,
                    linestyle="--" if electronic else "-", linewidth=1.5)
        ax.annotate("", xy=points[-1], xytext=points[-2],
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.5,
                                    linestyle="--" if electronic else "-"))

    ax.text(5.5, 6.22, "Two readouts fix spacing and offset", ha="center", fontsize=17)
    box(.35, 3.8, 2.0, .8, "Mode-locked laser\n"+r"$f_n=n f_r+f_0$")
    box(3.1, 3.8, 1.9, .8, "Coherent\nbroadening")
    arrow([(2.41, 4.2), (3.04, 4.2)])
    ax.plot([2.7, 2.7], [4.2, 5.1], color=blue, lw=1.5)
    box(3.1, 4.85, 1.9, .65, "Pulse detector")
    arrow([(2.7, 5.17), (3.04, 5.17)])
    box(5.9, 4.85, 2.0, .65, r"Measure $f_r$", orange)
    arrow([(5.06, 5.17), (5.84, 5.17)], True)
    box(5.9, 3.8, 1.45, .8, "Double red\n"+r"$f_n\to2f_n$")
    arrow([(5.06, 4.2), (5.84, 4.2)])
    arrow([(5.35, 4.2), (5.35, 2.85), (8.15, 2.85), (8.15, 3.64)])
    ax.text(6.8, 3.02, r"Blue tooth $f_{2n}$", ha="center", fontsize=11, color=blue)
    box(7.95, 3.7, 2.6, 1.0, "Overlap + photodiode\n"+r"$2f_n-f_{2n}=f_0$")
    arrow([(7.41, 4.2), (7.89, 4.2)])
    box(8.25, 1.9, 2.0, .65, r"Measure $f_0$", orange)
    arrow([(9.25, 3.64), (9.25, 2.61)], True)
    box(3.1, .8, 4.25, .9, "Reference + two feedback loops\nControl round-trip delay and phase slip", orange)
    arrow([(6.9, 5.56), (6.9, 5.85), (10.8, 5.85), (10.8, 1.25), (7.41, 1.25)], True)
    arrow([(9.25, 1.84), (9.25, 1.55), (7.41, 1.55)], True)
    arrow([(3.04, 1.25), (1.35, 1.25), (1.35, 3.74)], True)
    ax.text(5.5, .28, "Solid: optical paths     Dashed: electronic signals and control\nFunctional scheme; optical filters and actuator coupling are omitted.",
            fontsize=10, ha="center", va="center")
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.98)
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
