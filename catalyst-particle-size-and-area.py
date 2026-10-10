"""Draw the exact fixed-volume sphere model; emit the PNG into the CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 5.7), dpi=120, facecolor="white")
    left = fig.add_axes((.04, .19, .46, .62))
    right = fig.add_axes((.61, .21, .35, .59))
    left.set(xlim=(0, 7.4), ylim=(0, 5), aspect="equal")
    left.axis("off")
    color = "#4d7288"
    left.add_patch(Circle((1.2, 2.8), .8, facecolor="#d2e1ea", edgecolor=color, lw=2))
    left.annotate("", xy=(2.0, 2.8), xytext=(1.2, 2.8), arrowprops={"arrowstyle": "->", "color": color})
    left.text(1.5, 3.02, r"$r_0$", ha="center")
    for x in [4.2, 5.3, 6.4, 7.5]:
        for y in [2.35, 3.45]:
            # Four columns by two rows, all fitting within the panel.
            left.add_patch(Circle((x - .8, y), .4, facecolor="#d2e1ea", edgecolor=color, lw=1.5))
    left.text(1.2, 1.25, "1 sphere", ha="center", weight="bold")
    left.text(1.2, .7, r"$S_0=4\pi r_0^2$", ha="center")
    left.text(5.05, 1.25, r"8 spheres, radius $r_0/2$", ha="center", weight="bold")
    left.text(5.05, .7, r"$S=2S_0$", ha="center")
    left.text(3.5, 4.65, r"Both: $V_s=4\pi r_0^3/3$", ha="center", fontsize=14)
    x = np.linspace(.25, 1, 250)
    right.plot(x, 1/x, lw=2.5, color="#1764a0")
    right.scatter([1, .5, .25], [1, 2, 4], color="#bf6310", s=42, zorder=3)
    for px, py, label, offset in [(1, 1, "1 particle", (-65, -20)), (.5, 2, "8 particles", (10, 8)), (.25, 4, "64 particles", (12, -10))]:
        right.annotate(label, xy=(px, py), xytext=offset, textcoords="offset points", fontsize=11)
    right.set(xlim=(.2, 1.07), ylim=(.65, 4.4), xlabel=r"Particle radius $r/r_0$", ylabel=r"Total external area $S/S_0$")
    right.set_xticks([.25, .5, .75, 1])
    right.grid(alpha=.22)
    right.spines[["top", "right"]].set_visible(False)
    right.set_title(r"$S/S_0=r_0/r$", fontsize=15, pad=12)
    fig.suptitle("Same solid volume, more external surface", fontsize=17, y=.96)
    fig.text(.5, .07, "Separate nonporous spheres; all external surface assumed accessible.", ha="center", fontsize=11)
    fig.text(.5, .025, "Exact geometric model — the curve is not a measured reaction rate or time trace.", ha="center", fontsize=11, color="#394652")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
