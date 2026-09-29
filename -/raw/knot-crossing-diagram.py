"""Draw the verified four-crossing xy projection of meridional T(2,3).

All double points are derived from positive radius and equal polar angles:
t' - t = 2π/3 or 4π/3, and cos(2t') = cos(2t).
The four unordered pairs below exhaust these possibilities. Underpassing
parameters are masked, never the higher branches. This is not a minimum
crossing diagram. Run from the output directory; writes knot-crossing-diagram.png.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


R, r = 2.0, 0.7
PAIRS = np.pi * np.array([[1 / 6, 5 / 6], [1 / 3, 5 / 3], [2 / 3, 4 / 3], [7 / 6, 11 / 6]])
GAP_HALF_WIDTH = 0.026


def curve(t):
    rho = R + r * np.cos(2 * t)
    return np.stack((rho * np.cos(3 * t), rho * np.sin(3 * t), r * np.sin(2 * t)), axis=-1)


def projected_tangent(t):
    rho, drho = R + r * np.cos(2 * t), -2 * r * np.sin(2 * t)
    return np.array([drho * np.cos(3 * t) - 3 * rho * np.sin(3 * t), drho * np.sin(3 * t) + 3 * rho * np.cos(3 * t)])


def periodic_distance(t, center):
    return np.abs((t - center + np.pi) % (2 * np.pi) - np.pi)


def main():
    under, over, crossing_points = [], [], []
    for a, b in PAIRS:
        first, second = curve(a), curve(b)
        assert np.allclose(first[:2], second[:2], atol=1e-12)
        assert np.allclose([first[2], second[2]], [r * np.sin(2 * a), r * np.sin(2 * b)])
        assert np.isclose(first[2], -second[2])
        assert np.isclose(abs(first[2]), r * np.sqrt(3) / 2)
        va, vb = projected_tangent(a), projected_tangent(b)
        assert abs(va[0] * vb[1] - va[1] * vb[0]) > 1
        under.append(a if first[2] < second[2] else b)
        over.append(b if first[2] < second[2] else a)
        crossing_points.append(first[:2])
    assert len(np.unique(np.round(crossing_points, 10), axis=0)) == 4
    # Every underpass is actually removed; every overpass remains intact.
    assert all(periodic_distance(u, v) > 2 * GAP_HALF_WIDTH for u in under for v in over)
    assert all(curve(u)[2] < 0 < curve(v)[2] for u, v in zip(under, over))

    t = np.linspace(0, 2 * np.pi, 12001)
    points = curve(t)
    gaps = np.zeros(t.shape, dtype=bool)
    for parameter in under:
        gaps |= periodic_distance(t, parameter) < GAP_HALF_WIDTH
    broken = points.copy()
    broken[gaps] = np.nan
    for parameter in under:
        assert gaps[np.argmin(periodic_distance(t, parameter))]
    for parameter in over:
        assert not gaps[np.argmin(periodic_distance(t, parameter))]

    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("The same trefoil projection, with and without crossing information", fontsize=13)
    for ax, drawing, title in zip(axes, [points, broken], ["Shadow: heights forgotten", "Knot diagram: viewed from positive z"]):
        ax.plot(drawing[:, 0], drawing[:, 1], color="#176b9a", linewidth=3.5, solid_capstyle="round")
        ax.set(xlim=(-2.95, 2.95), ylim=(-2.95, 2.95), aspect="equal")
        ax.set_title(title, fontsize=11)
        ax.axis("off")
    axes[0].text(0.5, -0.015, "Four double points; over/under choices unspecified", transform=axes[0].transAxes, ha="center", fontsize=9)
    axes[1].text(0.5, -0.015, "Four crossings; each gap marks the lower strand", transform=axes[1].transAxes, ha="center", fontsize=9)
    fig.savefig(Path.cwd() / "knot-crossing-diagram.png", dpi=100, facecolor="white", transparent=False)
    print("Validated all four analytic crossing pairs, transverse tangents, opposite heights, and underpass masks.")


if __name__ == "__main__":
    main()
