"""Original Bragg geometry; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes an opaque PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 6.2), facecolor="white")
    ax = fig.add_axes((0.035, 0.21, 0.64, 0.66))
    theta = np.pi / 6  # Schematic angle chosen for clear geometry.
    u = np.array([np.cos(theta), -np.sin(theta)])
    v = np.array([np.cos(theta), np.sin(theta)])
    a, b = np.array([0., 0.]), np.array([0., -1.])
    c, e = b - np.sin(theta) * u, b + np.sin(theta) * v
    blue, orange, gray = "#2166ac", "#c45b10", "#6b7280"
    for y in (0, -1):
        ax.plot([-3.1, 3.1], [y, y], color=gray, lw=1.5)
    for p in (a, b):
        for start, end in ((p - 2.9 * u, p), (p, p + 2.9 * v)):
            ax.annotate("", xy=end, xytext=start,
                        arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    for p in (c, e):
        ax.plot([a[0], p[0]], [a[1], p[1]], "--", color=gray, lw=1.4)
    ax.plot([c[0], b[0], e[0]], [c[1], b[1], e[1]], color=orange, lw=4)
    for p, name, offset in ((a, "A", (0, 13)), (b, "B", (0, -21)),
                            (c, "C", (-20, -5)), (e, "D", (13, -5))):
        ax.plot(*p, "o", color="#202938", ms=5)
        ax.annotate(name, p, xytext=offset, textcoords="offset points", ha="center")
    # Right-angle marks at the two wavefront/ray intersections.
    for p, along, normal in ((c, u, np.array([np.sin(theta), np.cos(theta)])),
                              (e, -v, np.array([-np.sin(theta), np.cos(theta)]))):
        corners = np.array([p + .11 * along, p + .11 * (along + normal),
                            p + .11 * normal])
        ax.plot(corners[:, 0], corners[:, 1], color=gray, lw=1)
    ax.annotate("", xy=(-2.95, 0), xytext=(-2.95, -1),
                arrowprops={"arrowstyle": "<->", "color": "#202938"})
    ax.text(-3.13, -.5, "$d$", ha="right", va="center", fontsize=17)
    ax.add_patch(Arc(a, 1.5, 1.5, theta1=150, theta2=180, color=blue, lw=1.5))
    ax.text(-1.02, .16, r"$\theta$", color=blue, fontsize=16)
    ax.text(-1.35, -.76, r"$CB=d\sin\theta$", ha="center", color=orange)
    ax.text(1.35, -.76, r"$BD=d\sin\theta$", ha="center", color=orange)
    ax.text(-2.65, 1.53, "Incoming parallel rays", color=blue)
    ax.text(1.25, 1.53, "Outgoing rays", color=blue)
    ax.text(1.65, -.32, "Upper lattice plane", color=gray, fontsize=11)
    ax.text(1.2, -1.20, "Adjacent lattice plane", color=gray, fontsize=11)
    ax.set(xlim=(-3.4, 3.4), ylim=(-1.6, 1.9), aspect="equal")
    ax.axis("off")

    inset = fig.add_axes((.72, .34, .25, .42))
    inset.annotate("", xy=(0, 0), xytext=(-1.3, 0),
                   arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    inset.annotate("", xy=(.73, 1.26), xytext=(0, 0),
                   arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    inset.plot([0, 1.3], [0, 0], "--", color=gray)
    inset.plot([-1.2, 1.4], [-1.2 / np.sqrt(3), 1.4 / np.sqrt(3)], color=gray)
    inset.add_patch(Arc((0, 0), 1.4, 1.4, theta1=0, theta2=60, color=orange))
    inset.text(.77, .32, r"$2\theta$", fontsize=17, color=orange)
    inset.add_patch(Arc((0, 0), 2.1, 2.1, theta1=0, theta2=30, color=blue))
    inset.text(1.05, .10, r"$\theta$", fontsize=14, color=blue)
    inset.text(-1.3, -.28, "Beam", color=blue)
    inset.text(.30, 1.48, "Scattered", color=blue)
    inset.text(-.7, -.85, "Planes tilted to beam", color=gray, fontsize=11)
    inset.set(xlim=(-1.5, 1.65), ylim=(-1.05, 1.8), aspect="equal")
    inset.axis("off")
    fig.text(.5, .94, "Bragg geometry: compare paths between equal-phase fronts",
             ha="center", fontsize=17, weight="bold")
    fig.text(.355, .18, r"Extra path: $CB+BD=2d\sin\theta$", ha="center", fontsize=16)
    fig.text(.5, .095, "Dashed AC and AD are wavefront comparisons, perpendicular to the rays.",
             ha="center", fontsize=12)
    fig.text(.5, .045, "Schematic coherent elastic scattering; planes represent periodic order, not reflecting surfaces.",
             ha="center", fontsize=11, color=gray)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
