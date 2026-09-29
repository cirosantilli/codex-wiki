"""Changing flux and signed induction; write the PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    t = np.linspace(0.0, 1.0, 101)
    area, resistance = 0.020, 2.0
    field = 0.10 + 0.30 * t
    flux = area * field
    emf = -np.gradient(flux, t)
    current = emf / resistance
    np.testing.assert_allclose(flux[[0, -1]], [0.002, 0.008])
    np.testing.assert_allclose(emf, -0.006, atol=1e-14)
    np.testing.assert_allclose(current, -0.003, atol=1e-14)
    # Independently check the sign of the field at the loop center using
    # Biot-Savart direction dl x (center - source) for a clockwise circle.
    angle = np.linspace(0, -2 * np.pi, 721)
    points = np.column_stack((np.cos(angle), np.sin(angle), np.zeros_like(angle)))
    dl = np.diff(points, axis=0)
    to_center = -(points[1:] + points[:-1]) / 2
    assert np.all(np.cross(dl, to_center)[:, 2] < 0)

    blue, orange, green = "#176997", "#bd5723", "#337b56"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 5.8), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=(1.0, 1.15), hspace=0.53, wspace=0.35)
    diagram = fig.add_subplot(grid[:, 0])
    diagram.add_patch(Rectangle((0, 0), 1, 1, fill=False, lw=3, edgecolor="#59636c"))
    for x in (0.2, 0.5, 0.8):
        for y in (0.2, 0.5, 0.8):
            diagram.plot(x, y, "o", ms=10, mfc="white", mec=blue, mew=1.4)
            diagram.plot(x, y, ".", ms=3, color=blue)
    for x, y in ((0.35, 0.35), (0.65, 0.35), (0.35, 0.65), (0.65, 0.65)):
        diagram.plot(x, y, "x", ms=8, mew=1.6, color=orange)
    for start, end in (((0.3, 1), (0.7, 1)), ((1, 0.7), (1, 0.3)),
                       ((0.7, 0), (0.3, 0)), ((0, 0.3), (0, 0.7))):
        diagram.annotate("", end, start, arrowprops={"arrowstyle": "->", "color": orange, "lw": 3})
    diagram.annotate("", (0.18, 1.22), (0.82, 1.22),
                     arrowprops={"arrowstyle": "->", "color": green, "lw": 1.7})
    diagram.text(0.5, 1.29, "Positive boundary: CCW", ha="center", color=green)
    diagram.text(0.5, 1.52, "Fixed loop; normal out of page", ha="center", fontsize=12)
    diagram.text(0.5, -0.16, "Actual current: clockwise (−3 mA)", ha="center", color=orange)
    diagram.text(0.5, -0.36, "Dots: external B out, increasing", ha="center", color=blue)
    diagram.text(0.5, -0.52, "Crosses: induced B into page", ha="center", color=orange)
    diagram.text(0.5, -0.73, "A = 0.020 m²     R = 2.0 Ω", ha="center")
    diagram.set(xlim=(-0.3, 1.3), ylim=(-0.88, 1.68), aspect="equal")
    diagram.axis("off")

    flux_ax = fig.add_subplot(grid[0, 1])
    flux_ax.plot(t, flux * 1000, lw=2.5, color=blue)
    flux_ax.scatter([0, 1], flux[[0, -1]] * 1000, color=blue, s=25)
    flux_ax.set(xlim=(-0.03, 1.03), ylim=(0, 10), xlabel="Time t (s)", ylabel="External flux (mWb)")
    flux_ax.set_title("Flux: 2 → 8 mWb", fontsize=12)
    flux_ax.grid(alpha=0.18)
    drive_ax = fig.add_subplot(grid[1, 1])
    drive_ax.axhline(0, color="#96a1a8", lw=1)
    drive_ax.plot(t, emf * 1000, lw=2.5, color=orange, label="Emf (mV)")
    drive_ax.plot(t, current * 1000, lw=2.5, color=green, ls="--", label="Current (mA)")
    drive_ax.set(xlim=(-0.03, 1.03), ylim=(-8, 1), xlabel="Time t (s)", ylabel="Signed emf / current")
    drive_ax.legend(loc="lower right", fontsize=10, framealpha=1)
    drive_ax.set_title("CCW-positive: emf = −6 mV, current = −3 mA", fontsize=11)
    drive_ax.grid(alpha=0.18)
    fig.suptitle("A steady flux ramp produces a constant opposing drive", fontsize=15, y=0.98)
    fig.text(0.5, 0.915, "External B(t) = 0.10 T + (0.30 T/s)t; 0 ≤ t ≤ 1 s", ha="center", fontsize=11)
    fig.text(0.5, 0.03, "Quasistatic resistive toy model: neglect self-inductance. Field symbols show direction, not magnitude.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.035, right=0.97, bottom=0.15, top=0.79)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
