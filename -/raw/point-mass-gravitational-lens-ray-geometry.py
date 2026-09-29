"""Draw an original thin-lens geometry; write the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Transverse coordinates are exaggerated; model angles are in radians.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    theta_e = 0.02
    beta = 0.6 * theta_e
    d_l, d_s = 4.0, 10.0
    roots = (beta + np.array([1.0, -1.0]) * np.sqrt(beta**2 + 4 * theta_e**2)) / 2
    # Divide transverse coordinates by theta_e to make the paths readable.
    b = d_l * roots / theta_e
    source_y = d_s * beta / theta_e
    images_y = d_s * roots / theta_e
    colors = ["#1268a1", "#bc472d"]
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9.2, 5.8), facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(0, color="#626262", lw=1)
    for z in [d_l, d_s]:
        ax.axvline(z, color="#b8b8b8", lw=1, zorder=0)
    ax.plot([0, d_s], [0, source_y], ":", color="#767676", lw=1.6)
    for index, color in enumerate(colors):
        ax.plot([0, d_l, d_s], [0, b[index], source_y], color=color, lw=2.3)
        ax.plot([d_l, d_s], [b[index], images_y[index]], "--", color=color, lw=1.6)
        # Arrows show actual propagation from source toward observer.
        z1, z2 = 8.0, 7.1
        slope = (source_y - b[index]) / (d_s - d_l)
        y1, y2 = b[index] + slope * (z1 - d_l), b[index] + slope * (z2 - d_l)
        ax.annotate("", (z2, y2), (z1, y1), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        ax.scatter(d_s, images_y[index], s=55, facecolors="white", edgecolors=color, linewidths=1.8)
        ax.text(d_s + 0.16, images_y[index], rf"$I_{'+' if index == 0 else '-'}$", color=color, va="center")
    ax.scatter([0, d_l], [0, 0], s=[50, 90], color="#232323", zorder=5)
    ax.scatter(d_s, source_y, s=100, marker="*", color="#7d4394", zorder=6)
    ax.text(-0.1, -1.2, "Observer O", ha="left")
    ax.text(d_l + 0.18, -1.25, "Lens M")
    ax.text(d_s + 0.16, source_y, "Source S", va="center", color="#7d4394")
    ax.text(0.8, 1.8, r"$\theta_+$", color=colors[0])
    ax.text(1.7, -2.35, r"$\theta_-$", color=colors[1])
    ax.text(2.3, 0.65, r"$\beta$", color="#626262")
    ax.annotate("", (d_l - 0.2, b[0]), (d_l - 0.2, 0), arrowprops={"arrowstyle": "<->", "color": "#444444"})
    ax.text(d_l - 0.42, b[0] / 2, r"$b_+=D_l\theta_+$", rotation=90, va="center", ha="right")
    ax.text(d_l, 15.0, "Lens plane", ha="center", color="#626262")
    ax.text(d_s, 15.0, "Source plane", ha="center", color="#626262")
    for start, stop, height, label in [(0, d_l, -9.0, r"$D_l$"), (d_l, d_s, -9.0, r"$D_{ls}$"), (0, d_s, -11.4, r"$D_s$ (nearby Euclidean sketch)")]:
        ax.annotate("", (stop, height), (start, height), arrowprops={"arrowstyle": "<->", "color": "#444444"})
        ax.text((start + stop) / 2, height - 0.4, label, ha="center", va="top")
    ax.text(0.4, 11.9, "Solid: actual light paths\nDashed: apparent image directions\nDotted: unlensed source direction", fontsize=11, linespacing=1.5)
    ax.set_title("One source, two weak-field light paths", pad=17, fontsize=17)
    ax.set_xlim(-0.4, 11.8)
    ax.set_ylim(-13.0, 16.0)
    ax.axis("off")
    fig.text(0.5, 0.025, r"Transverse scale exaggerated; $\beta=0.6\theta_E$. Schematic theoretical geometry.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.035, right=0.98, top=0.88, bottom=0.09)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
