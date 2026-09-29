"""Draw point-mass gravity and its linear tidal residual.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the matching opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    mu = 9.0
    center = np.array([3.0, 0.0])
    radius = 0.36
    angles = np.arange(8) * np.pi / 4
    offsets = radius * np.column_stack((np.cos(angles), np.sin(angles)))
    points = center + offsets
    gravity = -mu * points / np.linalg.norm(points, axis=1)[:, None] ** 3
    tensor = mu / np.linalg.norm(center) ** 3 * np.diag([2.0, -1.0])
    residual = offsets @ tensor.T

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), dpi=120)
    labels = [
        ("Gravity at each position", "Exact field: all arrows point toward the source", gravity, 0.60, "#24699c"),
        ("After subtracting common acceleration", "Linear residual: radial stretch, transverse squeeze", residual, 2.60, "#c45c1b"),
    ]
    for ax, (title, subtitle, vectors, scale, color) in zip(axes, labels):
        ax.set_aspect("equal")
        ax.set_xlim(-0.45, 4.15)
        ax.set_ylim(-1.40, 1.45)
        ax.set_axis_off()
        ax.set_title(title, fontsize=12, pad=8, fontweight="bold")
        ax.plot([-0.05, 3.95], [0, 0], color="#d4d7db", linewidth=1, zorder=0)
        ax.add_patch(Circle((0, 0), 0.12, color="#30343b"))
        ax.text(0, -0.32, "Source M", ha="center", fontsize=11)
        ax.add_patch(Circle(center, radius, fill=False, linestyle="--", color="#b2b7bc", linewidth=1))
        ax.scatter(*center, marker="+", s=80, linewidth=1.5, color="#30343b", zorder=4)
        ax.scatter(points[:, 0], points[:, 1], s=22, color="#30343b", zorder=4)
        for point, vector in zip(points, vectors):
            ax.annotate("", xy=point + scale * vector, xytext=point,
                        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.8, "mutation_scale": 13}, zorder=3)
        ax.text(3, -0.94, "Reference point R", ha="center", fontsize=11)
        ax.annotate("", xy=(2.98, -0.65), xytext=(0.10, -0.65),
                    arrowprops={"arrowstyle": "<->", "lw": 1, "color": "#767d85"})
        ax.text(1.5, -0.57, "R", ha="center", color="#555c64")
        ax.text(1.8, -1.30, subtitle, ha="center", fontsize=9.5, color="#555c64")
    axes[0].text(1.5, 1.1, r"$\mathbf{g}(\mathbf{R}+\mathbf{x})$", ha="center", color="#24699c", fontsize=13)
    axes[1].text(1.5, 1.1, r"$\mathbf{g}(\mathbf{R}+\mathbf{x})-\mathbf{g}(\mathbf{R})\simeq T\mathbf{x}$", ha="center", color="#c45c1b", fontsize=12)
    fig.suptitle("Point-mass tides reveal differences in the pull", fontsize=15, y=0.99)
    fig.text(0.5, 0.025, "Arrows use separate length scales in the two panels. Dots mark positions, not a time sequence.",
             ha="center", fontsize=10, color="#555c64")
    fig.subplots_adjust(left=0.035, right=0.985, top=0.84, bottom=0.12, wspace=0.18)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
