"""Exact cubic subdivision and tangents; output PNG in the working directory.

Uses the repository's NumPy and Matplotlib dependencies; tested with Python 3.14.4.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def cubic(points, t):
    t = np.asarray(t)
    weights = np.stack(((1 - t) ** 3, 3 * (1 - t) ** 2 * t,
                        3 * (1 - t) * t**2, t**3), axis=-1)
    return weights @ points


def derivative(points, t):
    t = np.asarray(t)
    weights = np.stack(((1 - t) ** 2, 2 * t * (1 - t), t**2), axis=-1)
    return weights @ (3 * np.diff(points, axis=0))


def main():
    points = np.array([[0, 0], [1, 2], [3, 2], [4, 0]], dtype=float)
    q = (points[:-1] + points[1:]) / 2
    r = (q[:-1] + q[1:]) / 2
    s = (r[0] + r[1]) / 2
    left = np.array([points[0], q[0], r[0], s])
    right = np.array([s, r[1], q[2], points[3]])
    np.testing.assert_array_equal(left, [[0, 0], [0.5, 1], [1.25, 1.5], [2, 1.5]])
    np.testing.assert_array_equal(right, [[2, 1.5], [2.75, 1.5], [3.5, 1], [4, 0]])
    u = np.linspace(0, 1, 1001)
    left_error = float(np.max(np.abs(cubic(left, u) - cubic(points, u / 2))))
    right_error = float(np.max(np.abs(cubic(right, u) - cubic(points, (1 + u) / 2))))
    assert left_error < 3e-15 and right_error < 3e-15
    np.testing.assert_allclose(derivative(left, u), derivative(points, u / 2) / 2,
                               rtol=0, atol=3e-15)
    np.testing.assert_allclose(derivative(right, u), derivative(points, (1 + u) / 2) / 2,
                               rtol=0, atol=3e-15)
    np.testing.assert_array_equal(derivative(points, 0), [3, 6])
    np.testing.assert_array_equal(derivative(points, 1), [3, -6])
    np.testing.assert_array_equal(derivative(left, 1), [2.25, 0])
    np.testing.assert_array_equal(derivative(right, 0), [2.25, 0])
    speeds = np.linalg.norm(derivative(points, np.array([0, 0.5])), axis=1)
    np.testing.assert_allclose(speeds, [np.sqrt(45), 4.5], rtol=0, atol=1e-14)
    sample_t = np.linspace(0, 1, 5)
    samples = cubic(points, sample_t)
    chords = np.linalg.norm(np.diff(samples, axis=0), axis=1)
    assert chords[0] > chords[1] + 0.2

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13,
                         "axes.labelsize": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.25), dpi=120)
    blue, orange, dark = "#155b8b", "#ba570d", "#263c50"
    ax = axes[0]
    ax.plot(*points.T, "--", color="#c0c6cc", lw=1.2, label="Original polygon")
    ax.plot(*left.T, "o--", color=blue, lw=1.5, ms=6, label="Left control polygon")
    ax.plot(*right.T, "s--", color=orange, lw=1.5, ms=6, label="Right control polygon")
    ax.plot(*cubic(left, u).T, color=blue, lw=3)
    ax.plot(*cubic(right, u).T, color=orange, lw=3)
    for label, point, offset, color in [
        ("$P_0$", left[0], (0, -15), blue),
        ("$Q_0$", left[1], (-18, 11), blue),
        ("$R_0$", left[2], (-8, 15), blue),
        ("$R_1$", right[1], (8, 15), orange),
        ("$Q_2$", right[2], (18, 11), orange),
        ("$P_3$", right[3], (0, -15), orange),
    ]:
        ax.annotate(label, point, xytext=offset, textcoords="offset points",
                    ha="center", color=color)
    ax.scatter(*s, s=60, color=dark, zorder=5)
    ax.annotate("Shared endpoint\n$S=(2,1.5)$", s, xytext=(2, 0.6),
                ha="center", fontsize=11, color=dark,
                arrowprops={"arrowstyle": "->", "color": dark})
    ax.set_title("Subdivision changes the controls, preserves the curve", fontsize=12, pad=16)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.39),
              frameon=False, fontsize=10)

    ax = axes[1]
    ax.plot(*points.T, "o--", color="#a1aab3", lw=1.2, ms=5, label="Control polygon")
    ax.plot(*cubic(points, u).T, color=dark, lw=2.6, label="Bézier curve")
    for start, end, color in [
        (points[0], points[0] + 0.18 * derivative(points, 0), blue),
        (points[3] - 0.18 * derivative(points, 1), points[3], orange),
    ]:
        ax.annotate("", end, xytext=start,
                    arrowprops={"arrowstyle": "->", "lw": 2.7, "color": color}, zorder=6)
    ax.scatter(*samples.T, color=dark, s=36, zorder=5)
    for value, point, offset in zip(sample_t, samples,
                                    [(0, -15), (-20, 13), (0, 20), (20, 13), (0, -15)]):
        ax.annotate(f"$t={value:g}$", point, xytext=offset,
                    textcoords="offset points", ha="center", fontsize=10)
    ax.text(0.45, 2.55, "$C'(0)=(3,6)$", color=blue, ha="center")
    ax.text(3.55, 2.55, "$C'(1)=(3,-6)$", color=orange, ha="center")
    ax.set_title("Endpoint tangents and equal steps in t", pad=16)
    ax.text(0.5, -0.28, "Tangent arrows show direction (lengths scaled).\n"
            r"Speed: $\|C'(0)\|=\sqrt{45}$,  $\|C'(1/2)\|=4.5$."
            "\nEqual parameter steps need not give equal distances.",
            transform=ax.transAxes, ha="center", va="top", fontsize=10, linespacing=1.5)
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
    print(f"{output.name}: 1320x630; 1001-point subdivision errors "
          f"left={left_error:.3g}, right={right_error:.3g}; "
          f"endpoint tangents=(3,6),(3,-6); local join tangents=(2.25,0); "
          f"speeds={speeds.tolist()}; sampled chord lengths={chords.tolist()}")


if __name__ == "__main__":
    main()
