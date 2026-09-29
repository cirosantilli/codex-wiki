"""Original functional beam diagrams; no historical dimensions or copied traces.

The rotating-wheel and gravity methods are described in Otto Stern's
The method of molecular rays, lecture 12 December 1946, pp. 8–11.
Write basename.png in the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def slit(ax, x, y, color="#384d61"):
    ax.plot([x, x], [y - .6, y - .10], color=color, lw=4)
    ax.plot([x, x], [y + .10, y + .6], color=color, lw=4)


def main():
    fig, axes = plt.subplots(2, 1, figsize=(10.8, 7.5), dpi=110, facecolor="white")
    fig.suptitle("Measure flight time using moving openings or gravity", fontsize=16)
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 3.6))
        ax.axis("off")
    ax = axes[0]
    ax.text(.15, 3.22, "Rotating wheels: transit time matches an opening pitch", fontsize=13)
    ax.add_patch(Rectangle((.3, 1), 1.1, 1.1, facecolor="#f8dfba", edgecolor="#a45e25"))
    ax.text(.85, 1.55, "Oven", ha="center", va="center", fontsize=12)
    slit(ax, 2.2, 1.55)
    ax.text(2.2, 2.42, "Collimation", ha="center", fontsize=11)
    for x, label in [(4.35, "Wheel 1"), (6.55, "Wheel 2")]:
        slit(ax, x, 1.55, "#9c4c36")
        ax.text(x, 2.42, label, ha="center", fontsize=11)
    ax.annotate("", xy=(8.65, 1.55), xytext=(1.4, 1.55), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#36779d"})
    ax.text(8.75, 1.55, "Counter", va="center", fontsize=11)
    ax.annotate("", xy=(6.55, .65), xytext=(4.35, .65), arrowprops={"arrowstyle": "<->"})
    ax.text(5.45, .31, "Flight distance L", ha="center", fontsize=11)
    ax.text(7.6, .45, "Same rotation rate f\nFixed relative phase", fontsize=10)
    ax.text(.3, .12, r"N openings per wheel: transmission orders $v_k=NfL/k$", fontsize=11)
    ax = axes[1]
    ax.text(.15, 3.25, "Gravity: slower atoms fall farther before reaching the detector", fontsize=13)
    ax.add_patch(Rectangle((.3, 1.93), 1.1, .9, facecolor="#f8dfba", edgecolor="#a45e25"))
    ax.text(.85, 2.38, "Source", ha="center", va="center", fontsize=12)
    for x in [2.1, 3.1]:
        slit(ax, x, 2.38)
    ax.plot([1.4, 9], [2.38, 2.38], color="#888888", ls="--", lw=1)
    xs = np.linspace(3.1, 9, 250)
    for fall, color, label in [(0.45, "#36779d", "Faster"), (1.5, "#b34e33", "Slower")]:
        ys = 2.38 - fall*((xs - 3.1)/5.9)**2
        ax.plot(xs, ys, color=color, lw=2.6)
        ax.text(7.7, 2.38 - fall*.7 + .12, label, fontsize=11, color=color)
    ax.plot([9, 9], [.6, 2.8], color="#384d61", lw=4)
    ax.text(9.15, 2.7, "Scan\nheight", fontsize=10)
    ax.annotate("", xy=(9.45, .88), xytext=(9.45, 2.38), arrowprops={"arrowstyle": "<->"})
    ax.text(9.6, 1.6, "y", fontsize=12)
    ax.text(3.9, .48, r"Point-launch model: $t=L/v$, $y=gt^2/2$", fontsize=12)
    ax.text(.3, .05, "Functional schematics. The fall is exaggerated; finite slits and detector width broaden a real profile.", fontsize=10)
    fig.tight_layout(rect=(0, .01, 1, .95), h_pad=1.4)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
