"""Draw the ideal balanced cart and two nonrotating reference frames.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes inertial-cart-force-balance.png to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def arrow(ax, start, end, color, label, label_position):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=19, linewidth=2.5, color=color))
    ax.text(*label_position, label, color=color, fontsize=12, ha="center")


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6.8), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.25, 1], hspace=0.28)
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    ax.set_title("One cart: nonzero individual forces, zero net force", fontsize=15, pad=10)
    ax.plot([0.4, 9.6], [1.3, 1.3], color="#707070", linewidth=2)
    ax.add_patch(Rectangle((4.1, 1.4), 1.8, 1.1, facecolor="#e4ecf6",
                           edgecolor="#334e70", linewidth=2))
    ax.text(5, 1.92, "2 kg cart", ha="center", va="center", fontsize=13)
    arrow(ax, (4.1, 1.95), (1.9, 1.95), "#b3482f", "−6 N", (2.8, 2.2))
    arrow(ax, (5.9, 1.95), (8.1, 1.95), "#b3482f", "+6 N", (7.2, 2.2))
    arrow(ax, (5, 2.5), (5, 3.65), "#b3482f", "support", (4.2, 3.55))
    arrow(ax, (5, 1.4), (5, 0.22), "#b3482f", "weight", (4.2, 0.35))
    arrow(ax, (6.5, 3.2), (8.6, 3.2), "#176a9b", "v = +1.5 m/s", (7.55, 3.55))
    ax.text(0.5, 4.25, "Laboratory inertial frame\nHorizontal forces balance; vertical forces balance.",
            fontsize=11, va="center")
    ax.text(8.4, 0.6, "+x →", ha="center")
    for column, title, origin, velocity, acceleration in [
        (0, "Constant-velocity origin", "R(t) = Ut,   U = +1.5 m/s",
         "v′ = v − U = 0", "a′ = 0: cart remains at rest"),
        (1, "Accelerating origin", "R(t) = ½At²,   A = +0.50 m/s²",
         "v′ = 1.5 − 0.50t  (m/s)", "a′ = −0.50 m/s²"),
    ]:
        panel = fig.add_subplot(grid[1, column])
        panel.axis("off")
        panel.set_title(title, fontsize=14, pad=12)
        panel.text(0.5, 0.87, origin, ha="center", transform=panel.transAxes)
        panel.plot([0.1, 0.9], [0.57, 0.57], color="#707070", transform=panel.transAxes)
        panel.add_patch(Rectangle((0.4, 0.58), 0.2, 0.18, transform=panel.transAxes,
                                  facecolor="#e4ecf6", edgecolor="#334e70"))
        panel.text(0.5, 0.41, velocity, ha="center", transform=panel.transAxes, color="#176a9b")
        panel.text(0.5, 0.26, acceleration, ha="center", transform=panel.transAxes)
        panel.text(0.5, 0.08, "Actual net force = 0" if column == 0 else
                   "Actual net force = 0; effective term = −mA", ha="center",
                   fontsize=10, transform=panel.transAxes)
    fig.subplots_adjust(top=0.92, bottom=0.08, left=0.055, right=0.95)
    fig.text(0.5, 0.025, "Stipulated ideal model. Blue arrow is velocity, not another force.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "inertial-cart-force-balance.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
