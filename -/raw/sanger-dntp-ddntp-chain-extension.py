"""Original feature schematic. Run from _media; Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, xy, width, height, text, color="#eef3f7", edge="#526577", size=12):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.04",
                              facecolor=color, edgecolor=edge, linewidth=1.5))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=size)


def arrow(ax, start, end, color="#526577"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=15, color=color, linewidth=1.8))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 7.2), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Chain termination: the NEXT addition needs a 3′-OH", fontsize=18, y=.965)
    green, red = "#167052", "#b23a3a"
    for ax, is_dd in zip(axes, [False, True]):
        color = red if is_dd else green
        name = "ddNTP: 2′,3′-dideoxy" if is_dd else "dNTP: already 2′-deoxy"
        end = "H" if is_dd else "OH"
        ax.set(xlim=(0, 10), ylim=(0, 12))
        ax.axis("off")
        ax.text(5, 11.4, name, ha="center", fontsize=15, weight="bold", color=color)
        ax.text(5, 10.78, "Free substrate", ha="center", fontsize=11)
        box(ax, (3.2, 8.25), 3.0, 1.85, "Sugar\n2′: H\n3′: " + end,
            color="#f6f8fa", edge=color, size=14)
        box(ax, (7.2, 8.85), 2.05, .8, "Base", size=13)
        ax.plot([6.25, 7.15], [9.25, 9.25], color="#526577", lw=1.5)
        ax.text(6.67, 9.6, "1′", ha="center", fontsize=11)
        for x in [.35, 1.12, 1.89]:
            box(ax, (x, 8.87), .56, .76, "P", color="#fff1cd", size=12)
        ax.plot([.95, 1.08], [9.25, 9.25], color="#526577")
        ax.plot([1.72, 1.85], [9.25, 9.25], color="#526577")
        ax.plot([2.49, 3.15], [9.25, 9.25], color="#526577", lw=1.5)
        ax.text(2.82, 9.6, "5′", ha="center", fontsize=11)
        ax.text(1.4, 8.5, "Triphosphate", ha="center", fontsize=10)
        ax.text(5, 7.7, "Both substrates can be incorporated", ha="center", fontsize=12)
        arrow(ax, (5, 7.35), (5, 6.65))
        ax.text(5, 6.3, "Previous strand end supplies 3′-OH", ha="center", fontsize=11)
        ax.text(5, 5.8, "It joins the incoming 5′ phosphate", ha="center", fontsize=11)
        box(ax, (.35, 4.45), 3.0, .7, "5′—old strand", color="#e5edf5", size=11)
        ax.plot([3.4, 4.05], [4.8, 4.8], color="#526577", lw=2)
        ax.text(4.68, 4.8, "O—P—O", ha="center", va="center", fontsize=11)
        ax.plot([5.3, 5.65], [4.8, 4.8], color="#526577", lw=2)
        box(ax, (5.7, 4.4), 1.9, .8, "Added\nunit", edge=color, size=11)
        ax.plot([7.65, 7.95], [4.8, 4.8], color=color, lw=2)
        ax.text(8.65, 4.8, "3′-" + end, ha="center", va="center",
                fontsize=14, color=color, weight="bold")
        ax.text(5, 3.85, "Incorporated unit: one backbone phosphate", ha="center", fontsize=10)
        if is_dd:
            ax.plot([4.8, 5.2], [3.35, 2.95], color=red, lw=3)
            ax.plot([4.8, 5.2], [2.95, 3.35], color=red, lw=3)
            ax.text(5, 2.35, "No terminal 3′-OH", ha="center", color=red, weight="bold")
            ax.text(5, 1.75, "No next phosphodiester bond", ha="center", color=red, fontsize=12)
            ax.text(5, 1.2, "Extension stops here", ha="center", color=red, fontsize=12)
        else:
            arrow(ax, (5, 3.35), (5, 2.8), green)
            ax.text(5, 2.35, "Terminal 3′-OH remains", ha="center", color=green, weight="bold")
            ax.text(5, 1.75, "Next nucleotide can join", ha="center", color=green, fontsize=12)
            ax.text(5, 1.2, "Extension can continue", ha="center", color=green, fontsize=12)
    fig.text(.5, .065, "Feature schematic: most atoms and stereochemistry omitted; P denotes a phosphate group.",
             ha="center", fontsize=10, color="#526577")
    fig.text(.5, .035, "Incorporation releases the substrate’s two outer phosphates; it does not leave a triphosphate in the chain.",
             ha="center", fontsize=10, color="#526577")
    fig.subplots_adjust(top=.9, bottom=.1, left=.035, right=.985, wspace=.08)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
