"""Draw Cantor's diagonal enumeration; write the PNG basename to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media to place the generated image beside the other wiki media.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def pairing(x, y):
    s = x + y
    return s * (s + 1) // 2 + y


def main():
    fig = plt.figure(figsize=(7.5, 5.5), facecolor="white")
    ax = fig.add_axes((0.09, 0.13, 0.64, 0.75), facecolor="white")
    colors = ["#2a6398", "#4278ac", "#548ab7", "#679bc3", "#7badd0", "#93bfdb"]
    for s in range(13):
        x = np.arange(max(0, s - 6), min(s, 6) + 1)
        y = s - x
        ax.plot(x, y, color=colors[s] if s <= 5 else "#d9dee4",
                linewidth=1.7 if s <= 5 else 1, linestyle="--", zorder=1)
    xx, yy = np.meshgrid(np.arange(7), np.arange(7))
    for x, y in zip(xx.ravel(), yy.ravel()):
        x, y = int(x), int(y)
        s = x + y
        highlighted = s <= 5
        ax.scatter(x, y, s=600,
                   facecolor=colors[s] if highlighted else "#f3f5f7",
                   edgecolor="#17466a" if (x, y) == (2, 3) else "white",
                   linewidth=2.5 if (x, y) == (2, 3) else 0.7, zorder=3)
        ax.text(x, y, str(pairing(x, y)), ha="center", va="center", fontsize=10.5,
                color="white" if s <= 3 else "#182c3b", zorder=4)
    ax.set(xlim=(-0.5, 6.5), ylim=(-0.5, 6.5), xticks=np.arange(7), yticks=np.arange(7),
           xlabel="First coordinate x", ylabel="Second coordinate y")
    ax.set_aspect("equal")
    ax.tick_params(labelsize=10, length=0)
    for spine in ax.spines.values():
        spine.set_color("#aab7c2")
    fig.suptitle("Cantor pairing: an infinite grid, one code per pair", fontsize=14, y=0.97)
    fig.text(0.76, 0.83, "Diagonals x + y = s", fontsize=10.5, weight="bold")
    handles = [Line2D([], [], marker="o", linestyle="--", color=color,
                      markersize=9, label=f"s = {s}") for s, color in enumerate(colors)]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.75, 0.81),
               frameon=False, fontsize=10, handlelength=1.4)
    fig.text(0.76, 0.40, "Highlighted: codes 0–20\nLater pairs: pale gray", fontsize=10,
             linespacing=1.5)
    fig.text(0.76, 0.25, "Outlined example:\n(2, 3) lies on s = 5\nT(5) + 3 = 15 + 3 = 18",
             fontsize=10, linespacing=1.5)
    fig.text(0.09, 0.025, "Labels are π(x, y) = (x + y)(x + y + 1)/2 + y.  The grid continues beyond this window.",
             fontsize=9.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
