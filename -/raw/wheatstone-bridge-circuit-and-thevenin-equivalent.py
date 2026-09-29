"""Draw the DC bridge and its detector-port equivalent; Python 3.14/matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


WIRE = "#263442"
BLUE = "#1767a6"
RED = "#b64629"


def wire(ax, xs, ys):
    ax.plot(xs, ys, color=WIRE, lw=2, solid_capstyle="round")


def resistor(ax, x, y, label, color=BLUE, vertical=True):
    if vertical:
        rect = Rectangle((x - 0.17, y - 0.44), 0.34, 0.88)
        ax.text(x + 0.34, y, label, va="center", fontsize=12, color=color)
    else:
        rect = Rectangle((x - 0.48, y - 0.16), 0.96, 0.32)
        ax.text(x, y + 0.35, label, ha="center", fontsize=12, color=color)
    rect.set(facecolor="white", edgecolor=color, linewidth=2, zorder=3)
    ax.add_patch(rect)


def node(ax, x, y, label, dy=0.21):
    ax.plot(x, y, "o", color=WIRE, ms=5)
    ax.text(x, y + dy, label, ha="center", fontsize=12, fontweight="bold")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 6.3), dpi=110)
    fig.patch.set_facecolor("white")
    for ax in (left, right):
        ax.set_xlim(-0.3, 7.4)
        ax.set_ylim(-0.8, 6.4)
        ax.set_aspect("equal")
        ax.axis("off")

    left.set_title("Four-arm DC bridge", fontsize=15, pad=15)
    wire(left, [1.0, 1.0, 6.0, 6.0, 1.0], [0.4, 5.4, 5.4, 0.4, 0.4])
    # The ideal supply interrupts the outer left wire.
    left.add_patch(Circle((1.0, 2.9), 0.43, facecolor="white", edgecolor=WIRE, lw=2, zorder=3))
    left.text(1.0, 3.10, "+", ha="center", va="center", fontsize=14)
    left.text(1.0, 2.69, "−", ha="center", va="center", fontsize=14)
    left.text(0.28, 2.9, "$V_s$", ha="center", va="center", fontsize=14)
    wire(left, [2.8, 2.8], [0.4, 5.4])
    resistor(left, 2.8, 4.16, "$R_1$")
    resistor(left, 2.8, 1.64, "$R_2$")
    resistor(left, 6.0, 4.16, "$R_3$\nadjustable")
    resistor(left, 6.0, 1.64, "$R_x$\nunknown", color=RED)
    left.annotate("", xy=(6.24, 4.62), xytext=(5.74, 3.74),
                  arrowprops={"arrowstyle": "->", "lw": 1.5, "color": BLUE}, zorder=4)
    wire(left, [2.8, 6.0], [2.9, 2.9])
    resistor(left, 4.4, 2.9, "$R_d$", color=RED, vertical=False)
    left.text(3.66, 2.6, "+", color=RED, fontsize=13)
    left.text(4.97, 2.6, "−", color=RED, fontsize=13)
    left.text(4.4, 2.23, "null detector", ha="center", color=RED)
    node(left, 4.4, 5.4, "$A: V_s$")
    node(left, 4.4, 0.4, "$D: 0$", dy=-0.4)
    node(left, 2.8, 2.9, "$B$", dy=0.24)
    node(left, 6.0, 2.9, "$C$", dy=0.24)
    left.text(4.4, -0.48, "$V_d=V_B-V_C$", ha="center", fontsize=13)

    right.set_title("Equivalent seen between B and C", fontsize=15, pad=15)
    wire(right, [1.0, 1.0, 5.8], [1.2, 4.2, 4.2])
    wire(right, [1.0, 5.8], [1.2, 1.2])
    right.add_patch(Circle((1.0, 2.7), 0.43, facecolor="white", edgecolor=WIRE, lw=2, zorder=3))
    right.text(1.0, 2.91, "+", ha="center", va="center", fontsize=14)
    right.text(1.0, 2.49, "−", ha="center", va="center", fontsize=14)
    right.text(0.4, 2.7, "$V_{oc}$", ha="right", va="center", fontsize=13)
    resistor(right, 3.4, 4.2, "$R_{th}$", vertical=False)
    wire(right, [5.8, 5.8], [1.2, 4.2])
    resistor(right, 5.8, 2.7, "$R_d$", color=RED)
    node(right, 5.8, 4.2, "$B$", dy=0.25)
    node(right, 5.8, 1.2, "$C$", dy=-0.4)
    right.text(6.28, 3.49, "+", color=RED, fontsize=13)
    right.text(6.28, 1.89, "−", color=RED, fontsize=13)
    right.text(3.4, 5.25, "Ideal supply set to zero when finding $R_{th}$", ha="center", fontsize=10)
    right.text(3.5, 0.25, "$R_{th}=(R_1\\parallel R_2)+(R_3\\parallel R_x)$", ha="center", fontsize=13)
    right.text(3.5, -0.35, "$V_d=V_{oc}R_d/(R_{th}+R_d)$", ha="center", fontsize=13)
    fig.tight_layout(pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
