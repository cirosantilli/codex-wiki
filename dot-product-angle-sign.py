"""Draw dot-product signs for fixed lengths; write an opaque PNG to the cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([3.0, 4.0])
    angles = np.deg2rad([0, 60, 90, 120, 180])
    alpha = np.arctan2(a[1], a[0])
    vectors = 2 * np.column_stack((np.cos(alpha + angles), np.sin(alpha + angles)))
    products = vectors @ a
    expected = np.array([10, 5, 0, -5, -10])
    np.testing.assert_allclose(products, expected, atol=1e-13)
    np.testing.assert_allclose(np.linalg.norm(vectors, axis=1), 2)
    np.testing.assert_allclose(products / (np.linalg.norm(a) * 2), np.cos(angles), atol=1e-14)
    for direction in [np.array([2.0, 0.0]), np.array([-2.0, 0.0])]:
        projection = np.dot(a, direction) / np.dot(direction, direction) * direction
        np.testing.assert_allclose(projection, [3, 0])
        np.testing.assert_allclose(np.dot(a - projection, direction), 0)
    np.testing.assert_allclose(np.dot(a, [4, -3]), 0)
    np.testing.assert_allclose(np.linalg.norm([4, -3]), 5)
    np.testing.assert_allclose(np.dot(a, [-2, 0]), -6)
    np.testing.assert_allclose(np.dot(a, [-1, 0]), -3)
    np.testing.assert_allclose([np.dot(a, [2, 0]) / 10, np.dot(a, [-2, 0]) / 10], [.6, -.6])
    np.testing.assert_allclose(np.degrees(np.arccos(-.6)), 126.86989764584402)
    np.testing.assert_allclose(np.dot([1, 1], [1, -4]), -3)
    np.testing.assert_allclose(np.dot(np.array([4, 1]) * [1, 1], [1, -4]), 0)

    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (curve, rays) = plt.subplots(1, 2, figsize=(10.2, 5.1),
                                    gridspec_kw={"width_ratios": [1.2, 1]}, facecolor="white")
    fig.subplots_adjust(left=.08, right=.97, bottom=.19, top=.78, wspace=.32)
    theta = np.linspace(0, np.pi, 501)
    curve.plot(theta, 10 * np.cos(theta), color="#245b96", lw=2.3)
    curve.axhline(0, color="#888888", lw=.9)
    curve.axvline(np.pi / 2, color="#999999", ls="--", lw=1)
    colors = ["#287446", "#287446", "#666666", "#b34e12", "#b34e12"]
    for t, value, color in zip(angles, expected, colors):
        curve.plot(t, value, "o", color=color, ms=7)
        label = f"{int(value):+d}" if value != 0 else "0"
        curve.annotate(label, xy=(t, value), xytext=(0, 12 if value >= 0 else -20),
                       textcoords="offset points", ha="center", color=color, weight="bold")
    curve.set_xlim(-.12, np.pi + .12)
    curve.set_ylim(-12.5, 13)
    curve.set_xticks(angles, [r"$0^\circ$", r"$60^\circ$", r"$90^\circ$", r"$120^\circ$", r"$180^\circ$"])
    curve.set_yticks([-10, -5, 0, 5, 10])
    curve.set_xlabel(r"Angle $\theta$ between $a$ and $b$")
    curve.set_ylabel(r"Dot product $a\cdot b$")
    curve.set_title(r"$a\cdot b=10\cos\theta$", fontsize=13, pad=10)
    curve.grid(color="#e7e7e7", lw=.7)

    rays.set_aspect("equal")
    rays.set_xlim(-3.8, 4.2)
    rays.set_ylim(-3.2, 5.1)
    rays.axhline(0, color="#cccccc", lw=.8)
    rays.axvline(0, color="#cccccc", lw=.8)
    circle = np.linspace(0, 2 * np.pi, 361)
    rays.plot(2 * np.cos(circle), 2 * np.sin(circle), color="#cccccc", ls="--", lw=1)
    rays.annotate("", xy=a, xytext=(0, 0),
                  arrowprops=dict(arrowstyle="-|>", color="#245b96", lw=2.1, mutation_scale=16))
    rays.text(2.6, 4.28, r"$a=(3,4)$", color="#245b96", fontsize=11)
    for index, (vector, color, degree, value) in enumerate(zip(vectors, colors, [0, 60, 90, 120, 180], expected)):
        rays.annotate("", xy=vector, xytext=(0, 0),
                      arrowprops=dict(arrowstyle="-|>", color=color, lw=2.8, mutation_scale=14))
        point = vector * ([1.3, 1.3, 1.8, 1.3, 1.3][index])
        label = f"{degree}°\ndot {int(value):+d}" if value != 0 else f"{degree}°\ndot 0"
        rays.text(*point, label, ha="center", va="center", color=color, fontsize=10,
                  bbox=dict(facecolor="white", edgecolor="none", pad=1))
    rays.text(.16, -.3, "O", fontsize=10)
    rays.set_xticks([])
    rays.set_yticks([])
    for spine in rays.spines.values():
        spine.set_visible(False)
    rays.set_title(r"Same $a$; every $b$ has length $2$", fontsize=12, pad=10)
    fig.suptitle("Alignment changes the sign of the dot product", y=.96, fontsize=17)
    fig.text(.5, .86, r"$\|a\|=5,\quad \|b\|=2,\quad 0\leq\theta\leq\pi$", ha="center", fontsize=13)
    fig.text(.5, .07, "Green: aligned component    Grey: perpendicular    Orange: opposing component",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified dot products [10, 5, 0, -5, -10], all b lengths 2, cosine ratios, "
          "both projection directions, perpendicular pair, and zero residual dot products.")


if __name__ == "__main__":
    main()
