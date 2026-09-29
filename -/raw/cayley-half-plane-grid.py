"""Map an upper half-plane grid into the disk with the Cayley transform.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def cayley(z):
    return (z - 1j) / (z + 1j)


def check_map():
    rng = np.random.default_rng(42)
    z = rng.uniform(-4, 4, 200) + 1j * rng.uniform(0.05, 5, 200)
    w = cayley(z)
    np.testing.assert_allclose(1 - abs(w) ** 2, 4 * z.imag / abs(z + 1j) ** 2)
    np.testing.assert_allclose(1j * (1 + w) / (1 - w), z, atol=2e-14)
    derivative = 2j / (z + 1j) ** 2
    np.testing.assert_allclose(2 * abs(derivative) / (1 - abs(w) ** 2), 1 / z.imag)
    np.testing.assert_allclose(cayley(np.array([1j, 2j, 1 + 1j])), [0, 1 / 3, (1 - 2j) / 5])
    right = -1j * z
    r = (right - 1) / (right + 1)
    np.testing.assert_allclose(r, w)
    np.testing.assert_allclose((1 + r) / (1 - r), right, atol=2e-14)
    np.testing.assert_allclose(1 - abs(r) ** 2, 4 * right.real / abs(right + 1) ** 2)
    # Multiplication by a nonzero complex derivative preserves tangent angles.
    np.testing.assert_allclose((derivative * 1j) / derivative, 1j, atol=1e-15)


def main():
    check_map()
    blue, orange = "#236ca0", "#d47723"
    fig, (plane, disk) = plt.subplots(1, 2, figsize=(10, 4.9), dpi=125)
    fig.patch.set_facecolor("white")
    plane.set_facecolor("#f5f9fc")
    disk.add_patch(Circle((0, 0), 1, facecolor="#f5f9fc", edgecolor="0.3", lw=1.7))
    y = np.linspace(0, 3.5, 700)
    x = np.linspace(-3.5, 3.5, 900)
    for a in np.arange(-3, 3.1, 0.5):
        z = a + 1j * y
        w = cayley(z)
        plane.plot(z.real, z.imag, color=blue, lw=0.9, alpha=0.8)
        disk.plot(w.real, w.imag, color=blue, lw=0.9, alpha=0.8)
    for b in [0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3]:
        z = x + 1j * b
        w = cayley(z)
        plane.plot(z.real, z.imag, color=orange, lw=0.9, alpha=0.85)
        disk.plot(w.real, w.imag, color=orange, lw=0.9, alpha=0.85)
    plane.axhline(0, color="0.3", lw=1.7)
    # A shared grid intersection shows the preserved right angle.
    for ax, point, label, offset in [
        (plane, 1 + 1j, r"$1+i$", (12, 12)),
        (disk, cayley(1 + 1j), r"$(1-2i)/5$", (12, 12)),
    ]:
        ax.scatter(point.real, point.imag, color="#b63348", s=34, zorder=5)
        ax.annotate(label, (point.real, point.imag), xytext=offset,
                    textcoords="offset points", color="#9a2639", fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    plane.scatter([0], [1], color="0.2", s=25, zorder=5)
    plane.annotate(r"$i$", (0, 1), xytext=(-17, 9), textcoords="offset points")
    disk.scatter([0, 1], [0, 0], color="0.2", s=25, zorder=5)
    disk.annotate(r"$0=C(i)$", (0, 0), xytext=(-52, 9), textcoords="offset points",
                  bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    disk.annotate(r"$1=C(\infty)$", (1, 0), xytext=(-3, 15),
                  textcoords="offset points", ha="right",
                  bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    plane.set(xlim=(-3.5, 3.5), ylim=(-0.08, 3.5), xlabel=r"$\operatorname{Re}z$",
              ylabel=r"$\operatorname{Im}z$", title=r"Upper half-plane: $\operatorname{Im}z>0$")
    disk.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), xlabel=r"$\operatorname{Re}w$",
             ylabel=r"$\operatorname{Im}w$", title=r"Unit disk: $w=(z-i)/(z+i)$")
    for ax in (plane, disk):
        ax.set_aspect("equal")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A rectangular grid bends; tangent angles stay the same", fontsize=13)
    fig.text(0.5, 0.035, "Blue: vertical lines   •   Orange: horizontal lines   •   Only finite grid segments are drawn",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.085, 1, 0.93))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
