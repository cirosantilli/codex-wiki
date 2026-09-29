"""Plot an ideal circular pupil's Airy response (Python 3.14, NumPy, Matplotlib).

Run from _media; the opaque PNG is written into the current directory.
Bessel values use the integer-order integral and NumPy Gauss-Legendre nodes.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Circle
import numpy as np


FIRST_ZERO = 3.8317059702075125
_nodes, _weights = np.polynomial.legendre.leggauss(128)
_angles = (_nodes + 1) * np.pi / 2


def bessel_j(order, argument):
    """Jn(u) = pi^-1 integral_0^pi cos(u sin(t) - n t) dt."""
    values = np.asarray(argument, dtype=float)
    flat = values.ravel()
    result = np.empty_like(flat)
    for start in range(0, flat.size, 2048):
        part = flat[start:start + 2048]
        phase = part[:, None] * np.sin(_angles) - order * _angles
        result[start:start + part.size] = np.cos(phase) @ (_weights / 2)
    return result.reshape(values.shape)


def airy_intensity(argument):
    """Peak-normalized intensity; series avoids small-u cancellation."""
    values = np.asarray(argument, dtype=float)
    small = np.abs(values) < 0.1
    amplitude = np.empty_like(values)
    square = values[small] ** 2
    amplitude[small] = 1 - square / 8 + square ** 2 / 192 - square ** 3 / 9216
    amplitude[~small] = 2 * bessel_j(1, values[~small]) / values[~small]
    return amplitude ** 2


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.2), layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=(1, 1.12))
    image_ax = fig.add_subplot(grid[:, 0])
    linear_ax = fig.add_subplot(grid[0, 1])
    log_ax = fig.add_subplot(grid[1, 1], sharex=linear_ax)
    extent = 3.2
    xy = np.linspace(-extent, extent, 441)
    radius = np.hypot(xy[:, None], xy[None, :])
    field = airy_intensity(FIRST_ZERO * radius)
    artist = image_ax.imshow(np.maximum(field, 1e-5), origin="lower",
                            extent=(-extent, extent, -extent, extent), cmap="Blues",
                            norm=LogNorm(vmin=1e-5, vmax=1), interpolation="nearest")
    image_ax.add_patch(Circle((0, 0), 1, fill=False, linestyle="--",
                              linewidth=1.4, edgecolor="#d56a00"))
    image_ax.set(xlabel=r"$x/r_1$", ylabel=r"$y/r_1$",
                 title="Image intensity (log colour scale)")
    image_ax.text(0, -2.85, "Dashed circle: first zero", ha="center",
                  color="#7b3d00", bbox={"facecolor": "white", "alpha": 0.95,
                                          "edgecolor": "none"})
    colorbar = fig.colorbar(artist, ax=image_ax, fraction=0.046, pad=0.02,
                           ticks=[1, 1e-2, 1e-4])
    colorbar.set_label(r"$I/I_0$")
    radial_x = np.linspace(0, extent, 2001)
    profile = airy_intensity(FIRST_ZERO * radial_x)
    linear_ax.plot(radial_x, profile, color="#1764a0", linewidth=2)
    linear_ax.set(ylabel=r"$I/I_0$", ylim=(-0.025, 1.07), title="Same radial profile")
    linear_ax.tick_params(labelbottom=False)
    log_ax.semilogy(radial_x, np.maximum(profile, 1e-8), color="#1764a0", linewidth=2)
    log_ax.set(xlabel=r"Radius $r/r_1$", ylabel=r"$I/I_0$ (log)", ylim=(1e-5, 1.2))
    for ax in (linear_ax, log_ax):
        ax.axvline(1, color="#d56a00", linestyle="--", linewidth=1.4)
        ax.set_xlim(0, extent)
        ax.grid(alpha=0.18)
    linear_ax.annotate("First dark ring", xy=(1, 0), xytext=(1.4, 0.4),
                       arrowprops={"arrowstyle": "->", "color": "#7b3d00"},
                       color="#7b3d00")
    fig.suptitle("Circular aperture: the Airy disk and its surrounding rings", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
