"""Exact axis intercepts of outgoing rays from a submerged object.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media. The two rays represent different viewing directions;
they do not enter one eye. Model indices: water 4/3 and air 1.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (ax, curve) = plt.subplots(1, 2, figsize=(11.8, 6.5), layout="constrained",
                                   gridspec_kw={"width_ratios": [1.2, 1]})
    d, ratio = 12.0, 0.75
    colors = ["#176b92", "#bd5125"]
    ax.axhspan(-13, 0, color="#edf6fb")
    ax.axhline(0, color="#333333", lw=1.8)
    ax.axvline(0, color="#666666", ls=":", lw=1.5)
    ax.axhline(-9, color="#666666", ls="-.", lw=1)
    ax.scatter([0], [-d], color="black", s=42, zorder=5)
    ax.text(0.3, -12.55, "Object: 12 cm deep", va="center", fontsize=11)
    ax.text(0.3, -9.55, "Near-normal depth: 9 cm", fontsize=10, color="#444444")
    for angle, color in zip([30, 60], colors):
        theta = np.radians(angle)
        water = np.arcsin(ratio * np.sin(theta))
        x = d * np.tan(water)
        depth = x / np.tan(theta)
        end = np.array([x + 4.0 * np.tan(theta), 4.0])
        ax.plot([0, x], [-d, 0], color=color, lw=2)
        ax.annotate("", xy=end, xytext=(x, 0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
        ax.plot([0, x], [-depth, 0], color=color, ls="--", lw=1.7)
        ax.plot([x, x], [-2, 2.9], color="#777777", ls=":", lw=1)
        ax.add_patch(Arc((x, 0), 2.4, 2.4, theta1=90-angle, theta2=90, color=color, lw=1.3))
        ax.text(x + 0.24, 1.65, rf"${angle}^\circ$", color=color)
        ax.text(x + 0.3, -2.1, rf"${np.degrees(water):.4f}^\circ$", color=color, fontsize=10)
        ax.scatter([0], [-depth], color=color, s=35, zorder=6)
        ax.text(-0.4, -depth, f"{depth:.4f} cm", color=color, ha="right", va="center", fontsize=11)
        curve.scatter([angle], [depth], color=color, s=48, zorder=5)
    ax.text(-3.9, 3.1, "Air  n = 1", fontsize=11)
    ax.text(11.0, -11.7, "Water  n = 4/3", fontsize=11)
    ax.set(xlim=(-4.7, 18.1), ylim=(-13.25, 4.5), aspect="equal",
           xlabel="Horizontal position x (cm)", ylabel="Height z (cm)",
           title="Actual rays and backward extensions")
    angles = np.linspace(0, 85, 500)
    theta = np.radians(angles)
    depths = d * ratio * np.cos(theta) / np.sqrt(1 - ratio**2 * np.sin(theta)**2)
    curve.plot(angles, depths, color="#333333", lw=2, label="Exact axis-intercept depth")
    curve.axhline(9, color="#666666", ls="-.", lw=1.6, label="Near-normal approximation")
    for angle, color in zip([30, 60], colors):
        depth = d * ratio * np.cos(np.radians(angle)) / np.sqrt(1-ratio**2*np.sin(np.radians(angle))**2)
        curve.annotate(f"{depth:.4f} cm", (angle, depth), xytext=(6, -20), textcoords="offset points", color=color, fontsize=11)
    curve.set(xlim=(0, 85), ylim=(0, 12.5), xlabel="Outgoing air angle from normal (degrees)",
              ylabel="Depth below interface (cm)", title="Depth depends on viewing direction")
    curve.set_xticks([0, 15, 30, 45, 60, 75])
    curve.grid(alpha=0.2)
    curve.legend(loc="upper right", fontsize=10)
    fig.suptitle("Apparent depth at a flat water–air boundary", fontsize=17)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
