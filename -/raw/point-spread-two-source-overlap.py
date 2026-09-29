"""Ideal scalar circular-pupil model; writes its PNG to the current directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def bessel(order, z):
    """Periodic integral representation, without a SciPy dependency."""
    z = np.asarray(z, dtype=float)
    angles = 2 * np.pi * (np.arange(512) + 0.5) / 512
    return np.mean(np.cos(z[..., None] * np.sin(angles) - order * angles), axis=-1)


def amplitude(q):
    q = np.asarray(q, dtype=float)
    safe = np.where(q == 0, 1.0, q)
    return np.where(q == 0, 1.0, 2 * bessel(1, q) / safe)


def main():
    # t = theta / (lambda / D); q = pi t. P is peak normalized.
    q = np.linspace(0, 18, 9001)
    profile = amplitude(q) ** 2

    def airy(t):
        return np.interp(np.pi * np.abs(t), q, profile)

    zero = 3.8317059702075125
    rayleigh = zero / np.pi
    assert abs(float(amplitude(zero))) < 1e-13
    assert float(amplitude(0)) == 1
    x = np.linspace(-2.3, 2.3, 1401)
    xy = np.linspace(-2.3, 2.3, 401)
    xx, yy = np.meshgrid(xy, xy)
    cases = [("One point source", [0.0]),
             ("Two sources: Rayleigh separation", [-rayleigh / 2, rayleigh / 2]),
             ("Two sources: closer together", [-0.30, 0.30])]
    cmap = LinearSegmentedColormap.from_list("white_blue", ["white", "#bdd8ec", "#18577b"])
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 3, figsize=(11.4, 6.9), layout="constrained",
                             gridspec_kw={"height_ratios": [1.1, 1]})
    for col, (title, centers) in enumerate(cases):
        weight = 1 / len(centers)
        image = sum(weight * airy(np.hypot(xx - c, yy)) for c in centers)
        parts = [weight * airy(x - c) for c in centers]
        ax = axes[0, col]
        ax.imshow(image, extent=(-2.3, 2.3, -2.3, 2.3), origin="lower",
                  vmin=0, vmax=1, cmap=cmap)
        ax.scatter(centers, np.zeros(len(centers)), marker="x", color="#ce641c", s=35)
        ax.set(title=title, xlabel=r"$\theta_x/(\lambda/D)$")
        if col == 0:
            ax.set_ylabel(r"$\theta_y/(\lambda/D)$")
        ax = axes[1, col]
        if len(centers) > 1:
            for i, part in enumerate(parts):
                ax.plot(x, part, "--", color=["#46a1a3", "#b375a9"][i], lw=1.6,
                        label=f"Source {i + 1} contribution")
        ax.plot(x, sum(parts), color="#18577b", lw=2.3, label="Total intensity")
        for c in centers:
            ax.axvline(c, color="#ce641c", lw=0.9, ls=":")
        ax.set(xlim=(-2.3, 2.3), ylim=(0, 1.08), xlabel=r"$\theta_x/(\lambda/D)$")
        ax.grid(alpha=0.2)
        if col == 0:
            ax.set_ylabel("Intensity / single-source peak")
        ax.legend(loc="upper right", fontsize=8, frameon=False)
        if col:
            separation = centers[1] - centers[0]
            ax.text(0.04, 0.88, rf"$s={separation:.3f}\,\lambda/D$",
                    transform=ax.transAxes, fontsize=10)
    fig.suptitle("Point responses overlap smoothly as separation decreases", fontsize=15)
    fig.supxlabel("Ideal model, not measured data. Equal total flux in all panels; incoherent intensities add.\n"
                  "Orange crosses / dotted lines mark object positions. Maps use the same linear intensity scale.",
                  fontsize=10)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"path": path, "dimensions": [1140, 690],
                      "rayleigh_scale_lambda_over_D": rayleigh,
                      "central_value": float(amplitude(0)),
                      "first_zero_amplitude": float(amplitude(zero)),
                      "equal_total_flux": True, "data": "ideal model"}))


if __name__ == "__main__":
    main()
