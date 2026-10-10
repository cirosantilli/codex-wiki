"""Compare exact areas for four linear flows at abstract parameter t = 0.4.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Save an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def polygon_area(vertices):
    x, y = vertices.T
    return abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2


def main():
    t = 0.4
    generators = [np.diag([1, 1]), np.diag([1, -1]), np.diag([-1, -1]),
                  np.array([[0, 1], [0, 0]])]
    maps = [np.diag(np.exp(t * np.diag(a))) for a in generators[:3]]
    maps.append(np.eye(2) + t * generators[3])
    assert np.array_equal(generators[3] @ generators[3], np.zeros((2, 2)))
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    expected = [np.exp(0.8), 1, np.exp(-0.8), 1]
    for a, mapping, area in zip(generators, maps, expected):
        assert np.isclose(np.linalg.det(mapping), np.exp(t * np.trace(a)))
        assert np.isclose(polygon_area(corners @ mapping.T), area)
    assert np.isclose(np.linalg.det(np.eye(2) + t * generators[1]), 0.84)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 4, figsize=(10.8, 4.9), facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.985, bottom=0.23, top=0.68, wspace=0.3)
    headings = ["Expansion", "Saddle", "Contraction", "Nilpotent shear"]
    formulas = ["A = diag(1, 1)", "A = diag(1, −1)", "A = diag(−1, −1)", "A = [0  1; 0  0]"]
    colors = ["#237aa3", "#28876d", "#a75156", "#8566ab"]
    for ax, a, mapping, heading, formula, color, area in zip(
            axes, generators, maps, headings, formulas, colors, expected):
        ax.set_aspect("equal")
        ax.set_xlim(-0.15, 1.7)
        ax.set_ylim(-0.15, 1.7)
        ax.set_xticks([0, 0.5, 1, 1.5])
        ax.set_yticks([0, 0.5, 1, 1.5])
        ax.tick_params(labelsize=9, length=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.axhline(0, color="#b5b5b5", lw=0.8)
        ax.axvline(0, color="#b5b5b5", lw=0.8)
        vertices = corners @ mapping.T
        ax.fill(*vertices.T, color=color, alpha=0.17, zorder=2)
        for coordinate in [0.25, 0.5, 0.75]:
            for segment in [np.array([[coordinate, 0], [coordinate, 1]]),
                            np.array([[0, coordinate], [1, coordinate]])]:
                ax.plot(*(segment @ mapping.T).T, color=color, lw=0.55, alpha=0.65)
        ax.plot(*np.vstack([vertices, vertices[0]]).T, color=color, lw=2.2, zorder=3)
        ax.plot(*np.vstack([corners, corners[0]]).T, color="#555555", ls="--", lw=1.25, zorder=4)
        # Follow a material corner through the exact flow, rather than Euler steps.
        sample = np.linspace(0, t, 50)
        path = (np.column_stack([np.exp(sample * a[0, 0]), np.exp(sample * a[1, 1])])
                if heading != "Nilpotent shear" else np.column_stack([1 + sample, np.ones_like(sample)]))
        ax.plot(*path.T, color=color, lw=1.5, zorder=5)
        ax.annotate("", path[-1], path[-8], arrowprops={"arrowstyle": "->", "lw": 1.5,
                    "color": color, "mutation_scale": 12, "shrinkA": 0, "shrinkB": 0}, zorder=6)
        ax.set_title(heading + "\n" + formula, fontsize=11.5, pad=13)
        ax.text(0.5, -0.14, f"trace A = {int(np.trace(a))}", transform=ax.transAxes,
                ha="center", fontsize=12, color=color)
        area_text = f"area = {area:.4f}" if heading in ["Expansion", "Contraction"] else "area = 1"
        ax.text(0.5, -0.265, area_text, transform=ax.transAxes, ha="center", fontsize=12)

    fig.suptitle("Trace controls the volume rate of a linear flow", fontsize=17, y=0.96)
    fig.text(0.5, 0.865, r"$x'=Ax\qquad x(t)=e^{tA}x(0)\qquad \det(e^{tA})=e^{t\,\mathrm{tr}\,A}$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.79, "t = 0.4   •   Dashed = initial unit square   •   Colored = exact image   •   Same axis scale",
             ha="center", fontsize=10.5)
    fig.text(0.5, 0.045, "Zero trace preserves area while allowing stretching, contraction in one direction, or shear.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
