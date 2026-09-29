"""Circular and helical magnetic-only orbits; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Write lorentz-force-orbits.png to the working directory, as expected by Make.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def orbit(t, parallel_speed=0.0):
    return np.column_stack((np.sin(t), np.cos(t) - 1, parallel_speed * t))


def main():
    t = np.linspace(0, 4 * np.pi, 1001)
    velocity = np.column_stack((np.cos(t), -np.sin(t), np.full_like(t, 0.5)))
    acceleration = np.column_stack((-np.sin(t), -np.cos(t), np.zeros_like(t)))
    # Independent geometric and dynamical checks, including the force sign.
    np.testing.assert_allclose(np.cross(velocity, (0, 0, 1)), acceleration)
    np.testing.assert_allclose(np.sum(velocity * acceleration, axis=1), 0, atol=1e-15)
    np.testing.assert_allclose(np.sum(velocity**2, axis=1), 1.25, atol=1e-15)
    positions = orbit(t, 0.5)
    np.testing.assert_allclose(positions[:, 0]**2 + (positions[:, 1] + 1)**2, 1)
    np.testing.assert_allclose(orbit(np.array([0, np.pi/2, np.pi, 2*np.pi])),
                               [[0, 0, 0], [1, -1, 0], [0, -2, 0], [0, 0, 0]], atol=1e-14)
    np.testing.assert_allclose(orbit(np.array([2*np.pi]), 0.5)[0, 2], np.pi)
    reversed_velocity = np.column_stack((np.cos(t), np.sin(t), np.zeros_like(t)))
    reversed_acceleration = np.column_stack((-np.sin(t), np.cos(t), np.zeros_like(t)))
    np.testing.assert_allclose(-np.cross(reversed_velocity, (0, 0, 1)), reversed_acceleration)

    blue, orange, grey = "#176997", "#b55d20", "#637783"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10.8, 5.8), dpi=120, facecolor="white")
    left = fig.add_subplot(1, 2, 1)
    right = fig.add_subplot(1, 2, 2, projection="3d")

    # Dots are cross-sections of straight +z field lines, not orbit samples.
    for x in np.linspace(-1.25, 1.25, 6):
        for y in np.linspace(-2.25, 0.25, 6):
            left.plot(x, y, "o", ms=6, mfc="white", mec="#c9d3d9", zorder=0)
            left.plot(x, y, ".", ms=2, color="#9babb5", zorder=0)
    planar = orbit(np.linspace(0, 2*np.pi, 501))
    left.plot(planar[:, 0], planar[:, 1], color=blue, lw=2.8)
    for phase in (0.75, 3.9):
        begin, end = orbit(np.array([phase, phase + 0.20]))[:, :2]
        left.annotate("", end, begin, arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    left.scatter([0, 1], [0, -1], s=32, color=blue, zorder=5)
    left.annotate("Start: t = 0", (0, 0), xytext=(-1.50, 0.55), fontsize=10,
                  arrowprops={"arrowstyle": "-", "color": grey})
    left.annotate("", (0.75, 0), (0, 0), arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    left.text(0.82, 0.03, r"$\mathbf{v}$", color=blue, fontsize=13)
    left.annotate("", (0, -0.65), (0, 0), arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    left.text(0.08, -0.48, r"$\mathbf{F}_B$", color=orange, fontsize=13)
    left.plot([0, 1], [-1, -1], color=grey, ls=":", lw=1.2)
    left.plot(0, -1, "+", color=grey, ms=9)
    left.text(0.26, -0.94, "r = 1", fontsize=10, color=grey)
    left.annotate(r"$t=\pi/2$", (1, -1), xytext=(1.16, -0.70), fontsize=10)
    left.annotate("", (1, -1.65), (1, -1), arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    left.annotate("", (0.35, -1), (1, -1), arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    left.text(-1.55, -2.60, r"Dots: $\mathbf{B}$ out of page (+z)", fontsize=10, color=grey)
    left.set(xlim=(-1.65, 1.65), ylim=(-2.75, 0.85), xlabel="x", ylabel="y")
    left.set_aspect("equal")
    left.set_xticks([-1, 0, 1])
    left.set_yticks([-2, -1, 0])
    left.set_title("Transverse motion: clockwise", fontsize=12, pad=12)

    right.plot(*positions.T, color=blue, lw=2.6)
    right.scatter([0], [0], [0], color=blue, s=28)
    right.text(0, 0.12, 0.18, "Start", fontsize=10)
    for phase in (1.3, 7.8):
        point = orbit(np.array([phase]), 0.5)[0]
        tangent = np.array([np.cos(phase), -np.sin(phase), 0.5])
        right.quiver(*point, *tangent, length=0.48, color=blue, arrow_length_ratio=0.35, linewidth=1.5)
    for x, y in ((-1.25, -2.1), (1.25, -2.1), (0, -1)):
        right.plot([x, x], [y, y], [0, 6.5], color="#bbc7ce", lw=1.1, ls=":")
        right.quiver(x, y, 4.8, 0, 0, 1, length=1.5, color=grey, arrow_length_ratio=0.17)
    right.text(-1.25, -2.1, 6.9, r"$\mathbf{B}$", color=grey, fontsize=13)
    right.set(xlim=(-1.5, 1.5), ylim=(-2.5, 0.5), zlim=(0, 7.0), xlabel="x", ylabel="y", zlabel="z")
    right.set_xticks([-1, 0, 1])
    right.set_yticks([-2, -1, 0])
    right.set_zticks([0, np.pi, 2*np.pi], ["0", "π", "2π"])
    right.set_box_aspect((3, 3, 5))
    right.view_init(elev=23, azim=-55)
    right.set_title("Add parallel velocity: z = 0.5t", fontsize=12, pad=12)
    for axis in (right.xaxis, right.yaxis, right.zaxis):
        axis.set_pane_color((1, 1, 1, 1))
    right.grid(False)

    fig.suptitle("Magnetic force bends motion without changing speed", fontsize=15, y=0.97)
    fig.text(0.5, 0.895, r"Rescaled $m=q=B=1$, $\mathbf{E}=0$; initial transverse velocity $(1,0,0)$", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Both: radius 1, angular frequency 1, period 2π.   Helix: advance π per turn; no z acceleration.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.94, bottom=0.17, top=0.79, wspace=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
