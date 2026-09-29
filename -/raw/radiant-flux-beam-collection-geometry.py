"""Ideal beam collection, with fixed total power; no measured data.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def main():
    power_w, collector_m = 2.0, 0.005
    radii_m = np.array([0.01, 0.02])
    irradiance = power_w / (np.pi * radii_m**2)
    collected = irradiance * np.pi * collector_m**2
    np.testing.assert_allclose(collected, [0.5, 0.125], rtol=1e-14)
    theta = np.deg2rad(60)
    np.testing.assert_allclose(np.cos(theta), 0.5, atol=1e-14)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Collecting part of an ideal beam: total power stays 2 W", fontsize=15)
    blue, orange = "#17649c", "#bd570c"
    for ax, radius, e, p in zip(axes[:2], radii_m * 100, irradiance, collected):
        ax.set_aspect("equal")
        ax.add_patch(Circle((0, 0), radius, facecolor="#dceaf4", edgecolor=blue, lw=2))
        ax.add_patch(Circle((0, 0), 0.5, facecolor="#f3cc9e", edgecolor=orange, lw=2))
        ax.annotate("", xy=(radius, 0), xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": blue})
        ax.text(radius / 2, 0.16, f"b = {radius:g} cm", ha="center", color=blue)
        ax.text(0, -2.18, "collector a = 0.5 cm", ha="center", color=orange)
        ax.set_title(f"Beam cross-section: radius {radius:g} cm")
        ax.text(0, -2.65, f"Irradiance = {e:,.2f} W/m²\nCollected power = {p:g} W",
                ha="center", va="center", linespacing=1.6)
        ax.plot([-2, -1], [-3.23, -3.23], color="#333333", lw=3)
        ax.text(-1.5, -3.48, "1 cm", ha="center", fontsize=10)
        ax.set(xlim=(-2.5, 2.5), ylim=(-3.65, 2.5))
        ax.axis("off")

    ax = axes[2]
    center = np.array([0.8, 0.0])
    normal = np.array([np.cos(theta), np.sin(theta)])
    tangent = np.array([-np.sin(theta), np.cos(theta)])
    endpoints = np.array([center - tangent, center + tangent])
    projection_x = 2.55
    for y in [-0.9, 0, 0.9]:
        ax.annotate("", xy=(-0.35, y), xytext=(-1.45, y),
                    arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.8})
    ax.text(-0.92, 1.2, "parallel rays", ha="center", color=blue)
    ax.plot(endpoints[:, 0], endpoints[:, 1], color=orange, lw=5)
    for x, y in endpoints:
        ax.plot([x, projection_x], [y, y], color="#8b8b8b", ls="--", lw=1)
    ax.plot([projection_x, projection_x], endpoints[:, 1], color=blue, lw=5)
    ax.text(projection_x + 0.14, 0, "2a cos θ", va="center", rotation=90, color=blue)
    ax.text(0.01, -0.68, "actual width 2a", color=orange, ha="center", rotation=-30)
    ax.annotate("", xy=center + normal * 1.25, xytext=center,
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#303030"})
    ax.text(*(center + normal * 1.42), "normal n", ha="center", fontsize=10)
    ax.plot([center[0], center[0] + 0.8], [0, 0], color="#777777", lw=1)
    ax.add_patch(Arc(center, 1.1, 1.1, theta1=0, theta2=60, lw=1.4))
    ax.text(1.45, 0.36, "60°", ha="center", fontsize=10)
    ax.set_title("Side view: tilted small collector")
    ax.text(0.6, -2.05, "Projected width is halved.\nDepth into page is unchanged.",
            ha="center", va="center", linespacing=1.5)
    ax.text(0.6, -2.95, "Collected power at 60°:\n0.25 W or 0.0625 W", ha="center",
            va="center", linespacing=1.5, color=orange)
    ax.set(xlim=(-1.7, 3.2), ylim=(-3.65, 2.5), aspect="equal")
    ax.axis("off")
    fig.text(0.5, 0.008, "Synthetic geometry • Uniform beam • Tilted projected collector stays inside beam",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
