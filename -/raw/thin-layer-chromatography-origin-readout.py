"""Original stylized TLC readout; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; coordinates are chosen examples, not measured pigment positions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle


ORIGIN_CM = 1
FRONT_CM = 11
SPOTS_CM = {"A": 4, "B": 8}


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    ink, orange, teal = "#26384b", "#bd5519", "#087e8b"
    fig, ax = plt.subplots(figsize=(9.2, 6.8))
    fig.subplots_adjust(left=.10, right=.97, bottom=.16, top=.80)
    fig.suptitle("Thin-layer chromatography: start every distance at the origin",
                 fontsize=15, y=.96, color=ink)
    fig.text(.5, .895, "Stylized chosen positions • anonymous components • not experimental data",
             ha="center", fontsize=11, color="#536170")
    ax.set(xlim=(-1.4, 10.5), ylim=(-.8, 12.6),
           ylabel="Absolute height above plate bottom (cm)")
    ax.set_yticks([0, 1, 4, 8, 11, 12])
    ax.set_xticks([])
    for spine in ["top", "right", "bottom"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#a0acb4")
    ax.add_patch(Rectangle((0, 0), 4, 12, facecolor="#faf8f0",
                           edgecolor="#6a7783", linewidth=1.5))
    ax.axhline(0, xmin=.118, xmax=.50, color="#6a7783", linewidth=.8, linestyle=":")
    ax.plot([0, 4], [ORIGIN_CM] * 2, color=ink, linewidth=1.4)
    ax.plot([0, 4], [FRONT_CM] * 2, color="#477eaa", linewidth=1.7, linestyle="--")
    ax.text(4.25, 11.55, r"Marked solvent front: $y=11$ cm", color="#326b99")
    ax.text(4.25, .25, r"Pencil origin: $y_0=1$ cm", color=ink)
    ax.text(1.95, -.60, "Plate bottom: y = 0 cm", ha="center", fontsize=10, color=ink)
    for label, y, color in [("A", SPOTS_CM["A"], orange), ("B", SPOTS_CM["B"], teal)]:
        ax.add_patch(Ellipse((2, y), .90, .48, facecolor=color, alpha=.82,
                             edgecolor=color, linewidth=1.2))
        ax.plot(2, y, "+", color="white", markersize=8)
        ax.text(.28, y + .42, f"Spot {label}: y = {y} cm", color=color, fontsize=10)
        ax.plot([2.6, 4], [y, y], color=color, alpha=.5, linestyle=":")
    measurements = [(4.8, SPOTS_CM["A"], orange, "3 cm"),
                    (6.4, SPOTS_CM["B"], teal, "7 cm"),
                    (8.5, FRONT_CM, "#326b99", "10 cm")]
    ax.plot([4, 9.05], [ORIGIN_CM] * 2, color=ink, linewidth=.8, linestyle=":")
    for x, top, color, text in measurements:
        ax.annotate("", xy=(x, top), xytext=(x, ORIGIN_CM),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.7})
        ax.text(x + .18, (top + ORIGIN_CM) / 2, text, color=color,
                va="center", fontsize=12)
    fig.text(.5, .09, r"$R_{f,A}=(4-1)/(11-1)=0.3$          $R_{f,B}=(8-1)/(11-1)=0.7$",
             ha="center", fontsize=14, color=ink)
    fig.text(.5, .035, "Origin-to-spot centre ÷ origin-to-front; never measure from the plate bottom.",
             ha="center", fontsize=10, color="#536170")
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
