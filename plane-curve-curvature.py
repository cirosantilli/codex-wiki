"""Illustrate parabola curvature; write plane-curve-curvature.png to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def tangent(t):
    return np.array([1.0, 2.0 * t]) / np.sqrt(1.0 + 4.0 * t * t)


def curvature(t):
    return 2.0 / (1.0 + 4.0 * t * t) ** 1.5


def main():
    # Independently check turning per arc length by finite differences of T.
    samples = np.array([-0.65, 0.0, 0.65])
    step = 1e-5
    errors = []
    for t in samples:
        derivative = (tangent(t + step) - tangent(t - step)) / (2 * step)
        turning = np.linalg.norm(derivative) / np.sqrt(1 + 4 * t * t)
        errors.append(abs(turning - curvature(t)))
    assert max(errors) < 2e-9
    assert curvature(0.0) == 2.0
    np.testing.assert_allclose(curvature(0.5), 1 / np.sqrt(2))
    center = np.array([0.0, 0.5])
    radius = 1 / curvature(0.0)
    np.testing.assert_allclose(np.linalg.norm(center), radius)
    # The circle's lower graph has y''(0)=1/radius, matching y=x^2.
    assert 1 / radius == 2.0
    print(f"Parabola: kappa(0)=2; radius={radius}; center={tuple(center)}; "
          f"kappa(0.5)={curvature(0.5):.12f}; max turning error={max(errors):.3g}")

    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, (shape, bending) = plt.subplots(1, 2, figsize=(10, 5), facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.28, top=0.80, wspace=0.32)
    curve_color, tangent_color, normal_color = "#5d3b83", "#1d68a6", "#23845b"
    circle_color = "#c77817"
    t = np.linspace(-1.2, 1.2, 501)
    shape.plot(t, t * t, color=curve_color, lw=2.6)
    angle = np.linspace(0, 2 * np.pi, 361)
    shape.plot(radius * np.cos(angle), center[1] + radius * np.sin(angle),
               color=circle_color, lw=2, ls="--")
    for t0 in samples:
        point = np.array([t0, t0 * t0])
        unit_tangent = tangent(t0)
        unit_normal = np.array([-unit_tangent[1], unit_tangent[0]])
        shape.plot(*point, "o", color=curve_color, ms=5, zorder=5)
        for vector, color in [(unit_tangent, tangent_color), (unit_normal, normal_color)]:
            shape.annotate("", xy=point + 0.42 * vector, xytext=point,
                           arrowprops={"arrowstyle": "-|>", "color": color,
                                       "lw": 2, "mutation_scale": 15})
    shape.plot(*center, "+", color=circle_color, ms=11, mew=2)
    shape.annotate(r"Center $(0,\frac{1}{2})$", xy=center, xytext=(0.18, 1.18),
                   fontsize=11, arrowprops={"arrowstyle": "-", "color": circle_color})
    shape.text(-0.08, -0.22, r"$(0,0)$", ha="right", fontsize=11)
    shape.text(0.44, 0.12, r"$T$", color=tangent_color)
    shape.text(-0.18, 0.23, r"$N_L$", color=normal_color)
    shape.set(xlim=(-1.25, 1.35), ylim=(-0.30, 1.65), xlabel=r"$x$", ylabel=r"$y$")
    shape.set_aspect("equal", adjustable="box")
    shape.set_title(r"$r(t)=(t,t^2)$", pad=13)

    bending.plot(t, curvature(t), color=curve_color, lw=2.6)
    bending.scatter([0, -0.5, 0.5], curvature(np.array([0, -0.5, 0.5])),
                     color=curve_color, zorder=5)
    bending.annotate(r"$\kappa(0)=2$", xy=(0, 2), xytext=(0.18, 1.94), fontsize=12)
    bending.annotate(r"$\kappa(\pm\frac{1}{2})=1/\sqrt{2}$", xy=(0.5, curvature(0.5)),
                     xytext=(-1.05, 1.38), fontsize=12,
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    bending.set(xlim=(-1.2, 1.2), ylim=(0, 2.25), xlabel=r"Parameter $t$",
                 ylabel=r"Curvature $\kappa$ (inverse length)")
    bending.set_title(r"$\kappa(t)=2/(1+4t^2)^{3/2}$", pad=13)
    for ax in (shape, bending):
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.legend(handles=[Line2D([], [], color=curve_color, lw=2.6, label="Parabola"),
                        Line2D([], [], color=circle_color, lw=2, ls="--", label="Osculating circle"),
                        Line2D([], [], color=tangent_color, lw=2, label="Unit tangent T"),
                        Line2D([], [], color=normal_color, lw=2, label="Left unit normal")],
               loc="lower center", bbox_to_anchor=(0.5, 0.078), ncol=4, frameon=False,
               fontsize=10.5)
    fig.suptitle("Curvature measures turning per unit distance", fontsize=17, y=0.97)
    fig.text(0.5, 0.89, "At the vertex: curvature 2, osculating radius 1/2. The arrows show directions at three points.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035, "The circle matches the parabola through second order at the vertex; the bend weakens away from it.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
