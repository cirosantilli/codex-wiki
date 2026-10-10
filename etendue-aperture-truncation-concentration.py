"""Compare opaque aperture clipping with the filled-cone concentration bound.

Output the matching PNG basename to the CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5; run from _media with MPLBACKEND=Agg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (clip, port) = plt.subplots(1, 2, figsize=(11, 5.5), gridspec_kw={"width_ratios": [1, 1.55]})
    blue, green, red = "#2166ac", "#16846b", "#a23b3b"
    clip.add_patch(Circle((0, 0), 5, facecolor="#f6dcdc", edgecolor=red, lw=2))
    clip.add_patch(Circle((0, 0), 3, facecolor="#d7e9f6", edgecolor=blue, lw=2))
    clip.annotate("6 mm stop", xy=(1.5, 1.7), xytext=(0, 6.5), ha="center", color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue})
    clip.text(0, 0, "transmitted\n36%", color=blue, ha="center", va="center", weight="bold")
    clip.text(0, -4, "blocked annulus", color=red, ha="center", fontsize=10)
    clip.set(xlim=(-6, 6), ylim=(-6, 7.5), xlabel="x (mm)", ylabel="y (mm)")
    clip.set_aspect("equal")
    clip.set_title("Clipping in the aperture plane\nIncident diameter: 10 mm", pad=15)
    clip.spines[["top", "right"]].set_visible(False)
    clip.text(0.5, -0.19, "Same 30° directional cone\n"
              + r"$G_{\rm transmitted}=0.36\,G_{\rm incident}$",
              transform=clip.transAxes, ha="center", va="top")

    # The dashed envelope connects ports symbolically: no reflecting shape is asserted.
    port.plot([1.8, 5.5], [2, 1], "--", color="#999999", lw=1.5)
    port.plot([1.8, 5.5], [-2, -1], "--", color="#999999", lw=1.5)
    port.plot([1.8, 1.8], [-2, 2], color=blue, lw=4)
    port.plot([5.5, 5.5], [-1, 1], color=green, lw=4)
    for angle in [-30, 0, 30]:
        t = np.radians(angle)
        port.annotate("", xy=(1.8, 0), xytext=(1.8 - 1.6 * np.cos(t), 1.6 * np.sin(t)),
                      arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.5})
    port.add_patch(Arc((1.8, 0), 1.4, 1.4, theta1=150, theta2=180, color=blue))
    port.text(0.72, 0.33, "30°", color=blue, fontsize=10)
    for angle in [-90, -60, -30, 0, 30, 60, 90]:
        t = np.radians(angle)
        port.annotate("", xy=(5.5 + 1.45 * np.cos(t), 1.45 * np.sin(t)), xytext=(5.5, 0),
                      arrowprops={"arrowstyle": "->", "color": green, "lw": 1.2})
    port.add_patch(Arc((5.5, 0), 2.2, 2.2, theta1=-90, theta2=90, color=green, lw=1))
    port.text(1.8, 2.43, "Entrance: 10 mm", color=blue, ha="center")
    port.text(5.5, 2.43, "Receiver: 5 mm", color=green, ha="center")
    port.text(3.65, 0.15, "Symbolic\nconnection", color="#666666", ha="center", va="center", fontsize=10)
    port.text(1.8, -2.95, "Filled input cone\nat every position", color=blue, ha="center")
    port.text(5.5, -2.95, "Full output hemisphere\n(limit: half-angle 90°)", color=green, ha="center")
    port.set(xlim=(-0.25, 7.3), ylim=(-3.65, 3.1))
    port.set_aspect("equal")
    port.axis("off")
    port.set_title("Concentration needs angular room\nAll input rays retained; n = 1 at both ports", pad=15)
    port.text(0.5, -0.13,
              r"$C=A_{\rm in}/A_{\rm out}\leq1/\sin^2(30^\circ)=4$",
              transform=port.transAxes, ha="center", va="top", fontsize=12)
    fig.suptitle("Two different operations on a 10 mm, 30° filled bundle", fontsize=15)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.80, bottom=0.23, wspace=0.24)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
