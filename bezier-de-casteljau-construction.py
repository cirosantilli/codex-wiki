"""Cubic Bézier hull and midpoint construction; output PNG in the working directory.

Uses the repository's NumPy and Matplotlib dependencies; tested with Python 3.14.4.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def bernstein_cubic(points, t):
    t = np.asarray(t)
    weights = np.stack(((1 - t) ** 3, 3 * (1 - t) ** 2 * t,
                        3 * (1 - t) * t**2, t**3), axis=-1)
    return weights @ points


def construction(points, t):
    levels = [np.asarray(points, dtype=float)]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append((1 - t) * row[:-1] + t * row[1:])
    return levels


def main():
    points = np.array([[0, 0], [1, 2], [3, 2], [4, 0]], dtype=float)
    p, q, r, s = construction(points, 0.5)
    np.testing.assert_array_equal(q, [[0.5, 1], [2, 2], [3.5, 1]])
    np.testing.assert_array_equal(r, [[1.25, 1.5], [2.75, 1.5]])
    np.testing.assert_array_equal(s, [[2, 1.5]])
    t = np.linspace(0, 1, 1001)
    curve = bernstein_cubic(points, t)
    expanded = np.column_stack((3 * t + 3 * t**2 - 2 * t**3, 6 * t * (1 - t)))
    np.testing.assert_allclose(curve, expanded, rtol=0, atol=2e-15)
    recursive = np.array([construction(points, float(u))[-1][0] for u in t])
    evaluation_error = float(np.max(np.abs(curve - recursive)))
    assert evaluation_error < 2e-15
    # The trapezoidal hull is 0 <= y <= min(2, 2x, 8 - 2x).
    x, y = curve.T
    assert np.all(y >= 0) and np.all(y <= 1.5)
    assert np.all(y <= 2 * x + 1e-14) and np.all(y <= 8 - 2 * x + 1e-14)
    assert 2 > 2 * 0  # Bounding-box corner (0, 2) is outside that hull.
    matrix = np.array([[2, 1], [0, 1]], dtype=float)
    shift = np.array([0, 1], dtype=float)
    transformed = points @ matrix.T + shift
    np.testing.assert_array_equal(transformed, [[0, 1], [4, 3], [8, 3], [8, 1]])
    affine_error = float(np.max(np.abs(
        bernstein_cubic(transformed, t) - (curve @ matrix.T + shift))))
    assert affine_error < 4e-15
    np.testing.assert_array_equal(bernstein_cubic(transformed, 0.5), [5.5, 2.5])

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13,
                         "axes.labelsize": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.25), dpi=120)
    blue, orange, green, purple = "#155b8b", "#ba570d", "#16744b", "#79439b"
    ax = axes[0]
    ax.add_patch(Polygon(points, closed=True, facecolor="#edf0f3",
                         edgecolor="#98a2ac", lw=1, label="Convex hull"))
    ax.add_patch(Rectangle((0, 0), 4, 2, fill=False, ls=":", lw=1.8,
                           edgecolor="#606c78", label="Bounding box"))
    ax.plot(*points.T, "o--", color="#687582", lw=1.5, ms=6,
            label="Control polygon", zorder=3)
    ax.plot(*curve.T, color=blue, lw=2.8, label="Bézier curve", zorder=4)
    ax.scatter([2], [1.5], s=45, color=blue, zorder=5)
    for i, point in enumerate(points):
        offset = [(0, -16), (-12, 15), (12, 15), (0, -16)][i]
        ax.annotate(f"$P_{i}$ ({point[0]:g}, {point[1]:g})", point,
                    xytext=offset, textcoords="offset points", ha="center")
    ax.annotate("Box corner lies\noutside the hull", (0, 2), xytext=(0.15, 2.65),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#606c78"})
    ax.annotate("$C(1/2)=(2,1.5)$", (2, 1.5), xytext=(2, 0.65),
                ha="center", color=blue,
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.set_title("Curve, controls and two different enclosures", pad=16)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.38), ncol=2,
              frameon=False, fontsize=10)

    ax = axes[1]
    ax.plot(*curve.T, color=blue, lw=2.4, label="Bézier curve", zorder=3)
    ax.plot(*p.T, "o--", color="#a1aab3", lw=1.2, ms=5, label="Original controls")
    ax.plot(*q.T, "o-", color=orange, lw=1.8, ms=6, label="Level 1: Q")
    ax.plot(*r.T, "s-", color=green, lw=2.1, ms=6, label="Level 2: R")
    ax.scatter(*s.T, color=purple, marker="D", s=70, zorder=7, label="Level 3: S")
    for i, point in enumerate(p):
        ax.annotate(f"$P_{i}$", point, xytext=(0, 13 if i in (1, 2) else -15),
                    textcoords="offset points", ha="center", color="#687582")
    for i, point in enumerate(q):
        offsets = [(-22, -24), (0, 22), (22, -24)]
        ax.annotate(f"$Q_{i}$\n({point[0]:g}, {point[1]:g})", point,
                    xytext=offsets[i], textcoords="offset points", ha="center",
                    fontsize=10, color=orange)
    for i, point in enumerate(r):
        ax.annotate(f"$R_{i}$\n({point[0]:g}, {point[1]:g})", point,
                    xytext=(0, 9),
                    textcoords="offset points", ha="center", fontsize=10, color=green,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.annotate("$S=(2,1.5)$", s[0], xytext=(0, -40),
                textcoords="offset points", ha="center", color=purple,
                arrowprops={"arrowstyle": "->", "color": purple})
    ax.set_title("Three levels: take each neighboring midpoint", pad=16)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.38), ncol=2,
              frameon=False, fontsize=10)
    for ax in axes:
        ax.set(xlim=(-0.45, 4.45), ylim=(-0.35, 2.9), xlabel="x", ylabel="y")
        ax.set_aspect("equal")
        ax.set_xticks(range(5))
        ax.set_yticks([0, 1, 2])
        ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=0.055, right=0.98, top=0.91, bottom=0.26, wspace=0.18)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: 1320x630; midpoint={s[0].tolist()}; "
          f"1001-point Bernstein/recursion error={evaluation_error:.3g}; "
          f"affine error={affine_error:.3g}; hull inequalities passed")


if __name__ == "__main__":
    main()
