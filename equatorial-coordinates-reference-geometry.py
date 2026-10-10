"""Original equatorial-coordinate geometry; run from _media to write the PNG.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
All coordinates are analytical examples, not a star catalogue.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def project(points):
    """Linear schematic projection onto a readable two-dimensional drawing."""
    points = np.asarray(points)
    return np.column_stack((0.9 * points[..., 0] + 0.4 * points[..., 1],
                            -0.25 * points[..., 0] + 0.5 * points[..., 1]
                            + 0.85 * points[..., 2]))


def curve(ax, points, **kwargs):
    xy = project(points)
    ax.plot(xy[:, 0], xy[:, 1], **kwargs)


def label(ax, point, text, offset=(5, 5), **kwargs):
    ax.annotate(text, project([point])[0], xytext=offset,
                textcoords="offset points", **kwargs)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 5.6),
                                gridspec_kw={"width_ratios": [1.25, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Equatorial coordinates: directions on a reference sphere", fontsize=15)
    blue, orange, green = "#1966a3", "#be510b", "#22805b"
    t = np.linspace(0, 2 * np.pi, 500)
    equator = np.column_stack((np.cos(t), np.sin(t), np.zeros_like(t)))
    curve(ax, equator, color=blue, lw=2)
    alpha, delta = np.deg2rad([60, 30])
    d = np.linspace(-np.pi / 2, np.pi / 2, 300)
    hour_half = np.column_stack((np.cos(d) * np.cos(alpha),
                                 np.cos(d) * np.sin(alpha), np.sin(d)))
    curve(ax, hour_half, color="#969696", lw=1.3)
    back = hour_half.copy()
    back[:, :2] *= -1
    curve(ax, back, color="#b6b6b6", lw=1, ls="--")
    for endpoint in ([1, 0, 0], [0, 1, 0], [0, 0, 1.2], [0, 0, -1.12]):
        p = project([endpoint])[0]
        ax.annotate("", p, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": "#666666"})
    n = [np.cos(delta) * np.cos(alpha), np.cos(delta) * np.sin(alpha), np.sin(delta)]
    curve(ax, [[0, 0, 0], n], color=green, lw=2)
    xy = project([n])[0]
    ax.scatter(*xy, s=85, marker="*", color=green, zorder=5)
    a = np.linspace(0, alpha, 100)
    curve(ax, np.column_stack((np.cos(a), np.sin(a), a * 0)), color=orange, lw=4)
    dd = np.linspace(0, delta, 100)
    curve(ax, np.column_stack((np.cos(dd) * np.cos(alpha),
                               np.cos(dd) * np.sin(alpha), np.sin(dd))), color=green, lw=4)
    label(ax, [1, 0, 0], "reference equinox\nα = 0", offset=(4, -33), ha="left", color=orange)
    label(ax, [0, 0, 1.2], "north reference pole\nδ = +90°", ha="center", offset=(0, 8))
    label(ax, n, "synthetic direction\nα = 4 h, δ = 30°", offset=(10, 12), ha="left", color=green)
    label(ax, [0, 1, 0], "y", offset=(-10, -12))
    label(ax, [0.86, 0.5, 0], "α: eastward", offset=(9, -14), color=orange)
    label(ax, [np.cos(.18) * .5, np.cos(.18) * np.sqrt(3) / 2, np.sin(.18)],
          "δ: northward", offset=(12, 0), color=green)
    ax.text(-1.35, -1.24, "Blue: reference celestial equator\nGrey: hour circle through the direction\nCentre: origin of viewing directions", fontsize=10, va="top")
    ax.set(xlim=(-1.48, 1.85), ylim=(-1.8, 1.7), aspect="equal")
    ax.axis("off")

    bx.set_title("A parallel shrinks toward a pole", fontsize=12)
    for cy, dec, color in [(0.88, 0, blue), (-.15, 60, green)]:
        radius = np.cos(np.deg2rad(dec))
        u = np.linspace(0, 2 * np.pi, 360)
        bx.plot(radius * np.cos(u), cy + .30 * radius * np.sin(u), color="#aeb8bf", lw=1.4)
        u = np.deg2rad(np.linspace(55, 70, 100))
        bx.plot(radius * np.cos(u), cy + .30 * radius * np.sin(u), color=color, lw=5)
        bx.plot([0, radius * np.cos(u[0])], [cy, cy + .30 * radius * np.sin(u[0])],
                color=color, lw=1)
        bx.plot([0, radius * np.cos(u[-1])], [cy, cy + .30 * radius * np.sin(u[-1])],
                color=color, lw=1)
        bx.text(-1.05, cy - .40, f"δ = {dec}°: parallel radius = {radius:g}", color=color, fontsize=11)
    bx.text(0, 1.46, "Same RA increment: Δα = 1 h = 15°", ha="center", fontsize=11)
    bx.text(0, .30, "Equator: arc length = 15°", ha="center", color=blue)
    bx.text(0, -.72, "δ = 60°: arc length = 7.5°", ha="center", color=green)
    bx.text(0, -1.13, "At δ = ±90°, the parallel is one point.\nAll α values describe the same direction.",
            ha="center", fontsize=10, bbox={"boxstyle": "round,pad=.5", "fc": "#f3f5f7", "ec": "none"})
    bx.text(0, -1.56, "Arc lengths follow the parallel, not a great circle.\nAnalytical illustration; no measured star positions.",
            ha="center", fontsize=9, color="#555555")
    bx.set(xlim=(-1.35, 1.35), ylim=(-1.8, 1.8), aspect="equal")
    bx.axis("off")
    fig.subplots_adjust(left=.025, right=.98, bottom=.04, top=.86, wspace=.05)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
