"""Draw brouwer-disk-map.png in cwd using NumPy and Matplotlib.

Tested with Python 3.14.4 and the repository's declared dependencies.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    rotation = np.array([[0.0, -1.0], [1.0, 0.0]])
    offset = np.array([0.3, 0.1])
    fixed = np.array([13 / 58, 11 / 58])
    assert np.allclose(0.4 * rotation @ fixed + offset, fixed)
    bound = 0.4 + np.linalg.norm(offset)
    assert bound < 1
    assert np.isclose(np.linalg.norm(fixed), np.sqrt(290) / 58)

    grid = np.linspace(-0.9, 0.9, 7)
    points = np.array([(u, v) for u in grid for v in grid if u * u + v * v <= 1])
    images = 0.4 * points @ rotation.T + offset
    displacements = images - points
    assert np.all(np.linalg.norm(images, axis=1) <= bound)

    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(7.4, 6.4), facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 0), 1, facecolor="#f1f5f8", edgecolor="#334155", lw=2))
    ax.add_patch(Circle(offset, 0.4, facecolor="#d5ebe4", edgecolor="#147d64", lw=2, zorder=2))
    ax.quiver(
        points[:, 0], points[:, 1], displacements[:, 0], displacements[:, 1],
        angles="xy", scale_units="xy", scale=1, color="#426ca1", alpha=0.72,
        width=0.004, headwidth=4, zorder=3,
    )
    ax.scatter(*fixed, marker="*", s=190, color="#d05c16", edgecolors="white", zorder=5)
    ax.scatter(*offset, s=25, color="#147d64", zorder=4)
    ax.annotate(
        "Fixed point\n(13/58, 11/58)", fixed, xytext=(-0.86, 0.70),
        arrowprops={"arrowstyle": "->", "color": "#d05c16"}, color="#a94712",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95}, zorder=6,
    )
    ax.annotate(
        "Image disk: radius 0.4\ncentre (0.3, 0.1)", (0.65, 0.28), xytext=(0.27, 0.87),
        arrowprops={"arrowstyle": "->", "color": "#147d64"}, color="#11664f",
        fontsize=11, ha="center", zorder=6,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95},
    )
    ax.text(-0.90, -0.99, r"$D: u^2+v^2\leq 1$", color="#334155")
    ax.axhline(0, color="#94a3b8", lw=0.7, zorder=1)
    ax.axvline(0, color="#94a3b8", lw=0.7, zorder=1)
    ax.set(xlim=(-1.13, 1.13), ylim=(-1.13, 1.13), xlabel="u", ylabel="v")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title(r"$F(u,v)=0.4(-v,u)+(0.3,0.1)$", fontsize=17, pad=14)
    fig.text(0.5, 0.068, "Arrows run from x to F(x); the orange star has zero displacement.", ha="center", fontsize=11)
    fig.text(0.5, 0.025, r"Every output satisfies $\|F(x)\|\leq 0.4+\sqrt{0.1}\approx 0.716228<1$.", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.10, right=0.95, bottom=0.17, top=0.90)
    fig.savefig("brouwer-disk-map.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
