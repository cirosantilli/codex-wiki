"""Circular pupil and inverse PSF scale; writes its PNG to the current directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Scalar, monochromatic, in-focus model, without aberration or obscuration.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle
import numpy as np


def bessel(order, z):
    z = np.asarray(z, dtype=float)
    angles = 2 * np.pi * (np.arange(512) + 0.5) / 512
    return np.mean(np.cos(z[..., None] * np.sin(angles) - order * angles), axis=-1)


def amplitude(q):
    q = np.asarray(q, dtype=float)
    safe = np.where(q == 0, 1.0, q)
    return np.where(q == 0, 1.0, 2 * bessel(1, q) / safe)


def main():
    wavelength = 0.550  # Vacuum wavelength, micrometres.
    apertures = [0.25, 0.50]
    zero = 3.8317059702075125
    radii = [zero * wavelength / (2 * np.pi * na) for na in apertures]
    assert abs(radii[0] / radii[1] - 2) < 1e-14
    assert abs(float(amplitude(zero))) < 1e-13
    q = np.linspace(0, 18, 9001)
    profile = amplitude(q) ** 2
    x = np.linspace(-2.1, 2.1, 1401)
    xy = np.linspace(-2.1, 2.1, 401)
    xx, yy = np.meshgrid(xy, xy)
    cmap = LinearSegmentedColormap.from_list("white_blue", ["white", "#bdd8ec", "#18577b"])
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 3, figsize=(11.4, 7.4), layout="constrained",
                             gridspec_kw={"width_ratios": [1, 1, 1.3]})
    for row, (na, radius) in enumerate(zip(apertures, radii)):
        ax = axes[row, 0]
        ax.add_patch(Circle((0, 0), na, facecolor="#bdd8ec", edgecolor="#18577b", lw=2))
        ax.set(xlim=(-0.65, 0.65), ylim=(-0.65, 0.65), aspect="equal",
               title=f"Pupil: NA = {na:.2f}",
               xlabel=r"$\lambda_0 k_x/(2\pi)$", ylabel=r"$\lambda_0 k_y/(2\pi)$")
        ax.annotate("", (na, 0), (0, 0), arrowprops={"arrowstyle": "->", "color": "#18577b"})
        ax.text(0, -0.09, f"radius {na:.2f}", ha="center", fontsize=9)
        factor = 2 * np.pi * na / wavelength
        image = np.interp(factor * np.hypot(xx, yy), q, profile)
        ax = axes[row, 1]
        ax.imshow(image, extent=(-2.1, 2.1, -2.1, 2.1), origin="lower",
                  vmin=0, vmax=1, cmap=cmap)
        ax.add_patch(Circle((0, 0), radius, fill=False, ls=":", ec="#ce641c", lw=1.5))
        ax.set(title="Point response, same spatial scale", xlabel=r"$x$ (µm)", ylabel=r"$y$ (µm)")
        ax = axes[row, 2]
        line = np.interp(factor * np.abs(x), q, profile)
        ax.plot(x, line, color="#18577b", lw=2.3)
        for sign in [-1, 1]:
            ax.axvline(sign * radius, color="#ce641c", ls=":", lw=1.5)
        ax.set(xlim=(-2.1, 2.1), ylim=(0, 1.08), title=f"First zero: r = {radius:.3f} µm",
               xlabel=r"$x$ (µm)", ylabel="Intensity / own peak")
        ax.grid(alpha=0.2)
    fig.suptitle("A wider circular pupil makes a narrower point response", fontsize=15)
    fig.supxlabel("Ideal scalar model, not measured data. Vacuum wavelength 550 nm; in focus.\n"
                  "Each response has unit peak. Orange dotted circles / lines mark the first zero.", fontsize=10)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"path": path, "dimensions": [1140, 740],
                      "vacuum_wavelength_um": wavelength, "NA": apertures,
                      "first_zero_radii_um": radii, "inverse_scale_ratio": radii[0] / radii[1],
                      "data": "ideal model"}))


if __name__ == "__main__":
    main()
