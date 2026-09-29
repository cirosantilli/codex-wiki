"""Original functional diagram of a counter-triggered expansion cloud chamber.

Blackett and Occhialini, Proc. R. Soc. A 139 (1933), pp. 699–701,
describe the component sequence. No historical photograph, scale or data
is reproduced. Write basename.png in the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def block(ax, xy, width, height, text, color="#e7eef5"):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=.03",
                              facecolor=color, edgecolor="#42576b", lw=1.5))
    ax.text(xy[0]+width/2, xy[1]+height/2, text, ha="center", va="center", fontsize=11)


def arrow(ax, start, end, color="#b1543b"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})


def main():
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 7))
    ax.axis("off")
    ax.text(5.5, 6.73, "Let a passing particle initiate its own photograph", ha="center", fontsize=17)
    ax.add_patch(Rectangle((2.0, 2.15), 3.65, 2.9, facecolor="#edf6fc", edgecolor="#467a99", lw=2))
    ax.text(3.83, 4.63, "Expansion cloud chamber", ha="center", fontsize=12)
    ax.text(3.83, 3.32, "Ionization trail\nbefore expansion", ha="center", fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    ax.plot([3.2, 3.37, 3.55, 3.8, 4.12], [5.8, 4.6, 3.5, 2.6, 1.42], color="#385774", lw=2.4, zorder=1)
    ax.plot([2.1, 5.55], [2.25, 2.25], color="#73716c", lw=7)
    ax.text(3.8, 1.98, "Movable piston", ha="center", va="top", fontsize=10)
    for yy, label in [(5.65, "Upper counter"), (1.1, "Lower counter")]:
        block(ax, (2.15, yy), 3.2, .42, label)
    ax.text(.25, 5.84, "Particle", fontsize=11, color="#385774")
    arrow(ax, (1.2, 5.82), (2.9, 5.82), "#385774")
    block(ax, (7.65, 5.05), 2.65, .9, "Coincidence circuit\nwithin full window w")
    ax.plot([5.35, 6.4, 6.4], [5.86, 5.86, 5.68], color="#b1543b", lw=1.8)
    arrow(ax, (6.4, 5.68), (7.65, 5.68))
    ax.plot([5.35, 6.85, 6.85], [1.3, 1.3, 5.28], color="#b1543b", lw=1.8)
    arrow(ax, (6.85, 5.28), (7.65, 5.28))
    block(ax, (7.65, 3.55), 2.65, .9, "Relay and release\nopen expansion valve", "#f4e6dc")
    arrow(ax, (8.98, 5.05), (8.98, 4.45))
    arrow(ax, (7.65, 3.98), (5.65, 2.25))
    block(ax, (7.65, 1.75), 2.65, 1.05, "Illuminating flash\nand two camera views", "#f5efce")
    arrow(ax, (8.98, 3.55), (8.98, 2.8))
    arrow(ax, (7.65, 2.25), (5.65, 3.35), "#9b8a32")
    ax.text(.25, 3.55, "Bending\nmagnetic field", fontsize=11, color="#467a99")
    ax.text(5.5, .6, "Coincidence timing and mechanical expansion latency are different quantities.", ha="center", fontsize=11)
    ax.text(5.5, .16, "Original functional schematic: invented track, no historical dimensions or camera geometry.", ha="center", fontsize=10)
    fig.tight_layout(pad=1)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
