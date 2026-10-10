"""Original normalized deposition-density predictions; no experimental data.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Integrals use deterministic Gauss–Legendre quadrature (no sampling noise).
Positions and density calculations below use millimetres.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.legendre import leggauss


MASS = 1.79e-25
MU_B = 9.274e-24
GRADIENT = 300.0
LENGTH = 0.035
DRIFT = 0.100
SIGMA = 0.035


def offset(speed):
    return 1000 * MU_B * GRADIENT * LENGTH * (DRIFT + LENGTH / 2) / (MASS * np.asarray(speed)**2)


def gaussian(z, sigma=SIGMA):
    return np.exp(-.5 * (np.asarray(z) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))


def profiles(z, speeds, weights):
    """Two-state and isotropic fixed-magnitude classical densities."""
    two = np.zeros_like(z)
    classical = np.zeros_like(z)
    u, wu = leggauss(64)
    for v, w in zip(speeds, weights):
        d = offset(v)
        two += w * (gaussian(z - d) + gaussian(z + d)) / 2
        classical += w * (gaussian(z[:, None] - d * u[None, :]) @ (wu / 2))
    return two, classical


def draw():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    z = np.linspace(-.60, .60, 1801)
    mono = profiles(z, [500.0], [1.0])
    nodes, weights = leggauss(96)
    finite = profiles(z, 500 + 100 * nodes, weights / 2)
    off = gaussian(z)
    fig = plt.figure(figsize=(11, 7.5), facecolor="white")
    fig.suptitle("Two discrete components versus continuous orientations", fontsize=17, y=.97)
    fig.text(.5, .915, "Hypothetical predictions · identical flight geometry and spatial width σ = 0.035 mm", ha="center", fontsize=11)
    axes = [fig.add_axes((.075, .46, .39, .37)), fig.add_axes((.57, .46, .39, .37))]
    for ax, curves, title in zip(axes, [mono, finite],
                                 ["Single speed: 500 m/s", "Chosen speeds: uniform 400–600 m/s"]):
        ax.plot(z, curves[0], color="#186a9c", lw=2.5, label="Two-state model")
        ax.plot(z, curves[1], color="#bc5732", lw=2.2, ls="--", label="Classical isotropic moments")
        ax.plot(z, off, color=".5", lw=1.2, alpha=.7, label="Field off")
        ax.set(xlim=(-.60, .60), ylim=(0, 12.5), xlabel="Landing position z (mm)", ylabel="Number density (1/mm)")
        ax.set_title(title, fontsize=12, pad=12)
        ax.grid(alpha=.18)
    axes[0].legend(loc="upper left", fontsize=9, framealpha=.95)
    axes[1].annotate("Slower atoms\nland farther out", xy=(.37, 1.7), xytext=(.12, 7.2),
                     fontsize=10, arrowprops={"arrowstyle": "->", "color": ".3"})
    # Density-proportional synthetic strips, not photographs; one shared scale.
    strips = fig.add_axes((.26, .15, .64, .17))
    arr = np.vstack([np.tile(a, (18, 1)) for a in [finite[0], finite[1], off]])
    strips.imshow(arr, extent=(-.60, .60, 0, 3), origin="upper", aspect="auto", cmap="Greys", vmin=0, vmax=off.max(), interpolation="nearest")
    strips.set(yticks=[2.5, 1.5, .5], yticklabels=["Two-state", "Classical", "Field off"],
               xlabel="Landing position z (mm)", xlim=(-.60, .60))
    strips.tick_params(axis="y", length=0, pad=12)
    strips.set_title("Synthetic deposition strips for the finite-speed model · common density scale", fontsize=11, pad=12)
    for y in [1, 2]:
        strips.axhline(y, color="white", lw=3)
    fig.text(.075, .025, "M = 1.79 × 10⁻²⁵ kg; |μz| = μB for two-state model; G = 300 T/m; ℓ = 3.5 cm; D = 10 cm.\n"
             "Classical moments have magnitude μB and uniform cos θ. Strip darkness represents number density, not developed-film optics.", fontsize=10)
    path = Path(Path(__file__).stem + ".png")
    fig.savefig(path, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw()
