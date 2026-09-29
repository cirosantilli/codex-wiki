"""Show boundary correspondence and hyperbolic routes under the Cayley map.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
import numpy as np


def cayley(z):
    return (z - 1j) / (z + 1j)


def check_geometry():
    # Boundary correspondence, including the separately evaluated limit at infinity.
    np.testing.assert_allclose(cayley(np.array([-1, 0, 1, 2])), [1j, -1, -1j, (3 - 4j) / 5])
    np.testing.assert_allclose(abs(cayley(np.linspace(-10, 10, 101))), 1, atol=3e-16)
    np.testing.assert_allclose(cayley(np.array([1j, 2j])), [0, 1 / 3])
    z = np.array([0.2 + 0.4j, 1 + 1j, -1 + 2j])
    for a, b, c, d in [(1, 1, 0, 1), (0, -1, 1, 0), (2, 1, 1, 1)]:
        delta = a * d - b * c
        f = (a * z + b) / (c * z + d)
        np.testing.assert_allclose(f.imag, delta * z.imag / abs(c * z + d) ** 2)
        np.testing.assert_allclose((d * f - b) / (-c * f + a), z, atol=1e-14)
        np.testing.assert_allclose(abs(delta / (c * z + d) ** 2) / f.imag, 1 / z.imag)
    np.testing.assert_allclose(cayley(-1 / z), -cayley(z), atol=3e-16)
    np.testing.assert_allclose(-1 / (1 + 1j), (-1 + 1j) / 2)
    # Fit the two curved image circles and verify orthogonality to the unit circle:
    # |centre|^2 = radius^2 + 1. Diameters are checked separately.
    theta = np.linspace(0.05, np.pi - 0.05, 300)
    for route in [1 + 1j * np.geomspace(0.05, 20, 300), 1 + np.exp(1j * theta)]:
        w = cayley(route)
        design = np.column_stack((2 * w.real, 2 * w.imag, np.ones(w.size)))
        cx, cy, k = np.linalg.lstsq(design, abs(w) ** 2, rcond=None)[0]
        radius_squared = k + cx**2 + cy**2
        np.testing.assert_allclose(abs(w - (cx + 1j * cy)) ** 2, radius_squared, atol=2e-14)
        np.testing.assert_allclose(cx**2 + cy**2, radius_squared + 1, atol=2e-14)
    np.testing.assert_allclose(cayley(1j * np.geomspace(0.01, 100, 100)).imag, 0, atol=1e-15)
    np.testing.assert_allclose(cayley(np.exp(1j * theta)).real, 0, atol=1e-15)


def main():
    check_geometry()
    colors = ["#236ca0", "#d47723", "#8456a4", "#278568"]
    labels = [r"Vertical $x=0$", r"Vertical $x=1$", r"Semicircle $-1$ to $1$", r"Semicircle $0$ to $2$"]
    fig, (plane, disk) = plt.subplots(1, 2, figsize=(10, 5.3), dpi=125)
    fig.patch.set_facecolor("white")
    plane.set_facecolor("#f5f9fc")
    plane.axhline(0, color="0.3", lw=1.7)
    disk.add_patch(Circle((0, 0), 1, facecolor="#f5f9fc", edgecolor="0.3", lw=1.7))
    theta = np.linspace(0, np.pi, 800)
    source_y = np.linspace(0, 3.1, 500)
    # Sampling infinity via finite heights and appending its known image avoids poles.
    disk_y = np.r_[0, np.geomspace(1e-5, 1e5, 1500)]
    for x, color in zip([0, 1], colors[:2]):
        plane.plot(np.full_like(source_y, x), source_y, color=color, lw=2.3)
        w = np.r_[cayley(x + 1j * disk_y), 1 + 0j]
        assert np.all(np.isfinite(w))
        disk.plot(w.real, w.imag, color=color, lw=2.3)
        plane.annotate("", (x, 3.16), (x, 2.87),
                       arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
    for center, color in zip([0, 1], colors[2:]):
        z = center + np.exp(1j * theta)
        w = cayley(z)
        plane.plot(z.real, z.imag, color=color, lw=2.3)
        disk.plot(w.real, w.imag, color=color, lw=2.3)
    # Boundary points are hollow: they are not points of either hyperbolic domain.
    for x in [-1, 0, 1, 2]:
        plane.scatter([x], [0], s=40, facecolor="white", edgecolor="0.2", zorder=6)
        plane.annotate(str(x), (x, 0), xytext=(0, -19), textcoords="offset points", ha="center")
    boundary = [(1j, r"$C(-1)=i$", (0, 11), "center"),
                (-1 + 0j, r"$C(0)=-1$", (-5, -21), "left"),
                (-1j, r"$C(1)=-i$", (0, -19), "center"),
                ((3 - 4j) / 5, r"$C(2)=(3-4i)/5$", (15, -6), "left"),
                (1 + 0j, r"$C(\infty)=1$", (8, 10), "left")]
    for w, label, offset, align in boundary:
        disk.scatter([w.real], [w.imag], s=40, facecolor="white", edgecolor="0.2", zorder=6)
        disk.annotate(label, (w.real, w.imag), xytext=offset, textcoords="offset points",
                      fontsize=9, ha=align)
    plane.scatter([0], [1], s=38, color="0.15", marker="D", zorder=6)
    plane.annotate(r"$i$", (0, 1), xytext=(-18, 8), textcoords="offset points")
    disk.scatter([0], [0], s=38, color="0.15", marker="D", zorder=6)
    disk.annotate(r"$C(i)=0$", (0, 0), xytext=(-52, 12), textcoords="offset points")
    plane.set(xlim=(-1.6, 2.6), ylim=(-0.25, 3.35), xticks=[], yticks=[1, 2, 3],
              xlabel=r"$\operatorname{Re}z$", ylabel=r"$\operatorname{Im}z$",
              title=r"Upper half-plane: vertical routes end at $\infty$")
    plane.tick_params(axis="x", labelbottom=False)
    disk.set(xlim=(-1.15, 1.7), ylim=(-1.22, 1.25), xticks=[], yticks=[],
             xlabel=r"$\operatorname{Re}w$", ylabel=r"$\operatorname{Im}w$",
             title="Disk: arcs meet the boundary at right angles")
    for ax in (plane, disk):
        ax.set_aspect("equal")
        ax.spines[["top", "right", "bottom"]].set_visible(False)
    fig.suptitle(r"Boundary correspondence and shortest hyperbolic routes: $w=(z-i)/(z+i)$", fontsize=13)
    handles = [Line2D([0], [0], color=color, lw=2.3, label=label)
               for color, label in zip(colors, labels)]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, 0.045), fontsize=10)
    fig.text(0.5, 0.015, "Hollow endpoints lie outside the domains; their hyperbolic distance from interior points is infinite.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.15, 1, 0.93))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
