"""Generate two-beam-interference-fringes.png in CWD on white.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Ideal plane waves at +/-30 degrees, both E along y. Lambda is the length
unit; I0 is each beam's along-beam flux. Plot scalar E-squared intensity,
not z-normal flux, which has an extra cos(theta) projection.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    wavelength, theta, i0 = 1., np.pi / 6, 1.
    k = 2 * np.pi / wavelength
    x = np.linspace(-3, 3, 1201)
    z = np.linspace(0, 4, 401)
    xx, zz = np.meshgrid(x, z)
    phase_plus = k * (xx * np.sin(theta) + zz * np.cos(theta))
    phase_minus = k * (-xx * np.sin(theta) + zz * np.cos(theta))
    field = np.exp(1j * phase_plus) + np.exp(1j * phase_minus)
    scalar_intensity = i0 * np.abs(field) ** 2
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (geometry, grid) = plt.subplots(1, 2, figsize=(10, 5.6), dpi=110,
                                       gridspec_kw={"width_ratios": [1, 2.25]})
    fig.subplots_adjust(left=.065, right=.96, top=.78, bottom=.23, wspace=.32)
    geometry.set(xlim=(-1.3, 1.3), ylim=(-.3, 2.5), aspect="equal")
    geometry.axis("off")
    geometry.annotate("", xy=(0, 2.25), xytext=(0, 0),
                      arrowprops={"arrowstyle": "->", "color": ".45", "lw": 1.2})
    geometry.annotate("", xy=(1.2, 0), xytext=(-1.2, 0),
                      arrowprops={"arrowstyle": "->", "color": ".45", "lw": 1.2})
    for sign, colour in [(1, "#1768ac"), (-1, "#cb6418")]:
        geometry.annotate("", xy=(sign * 2 * np.sin(theta), 2 * np.cos(theta)),
                          xytext=(0, 0),
                          arrowprops={"arrowstyle": "->", "color": colour, "lw": 2.7})
    geometry.text(0, 2.3, "z", ha="center")
    geometry.text(1.2, -.18, "x", ha="center")
    geometry.text(.58, 2, "+30°", color="#1768ac", ha="center")
    geometry.text(-.58, 2, "−30°", color="#cb6418", ha="center")
    geometry.text(0, -.48, "Both E along y\n(out of the page)", ha="center", va="top", fontsize=10)
    geometry.set_title("Propagation directions", fontsize=11, pad=15)
    mesh = grid.pcolormesh(xx / wavelength, zz / wavelength,
                          scalar_intensity / i0, shading="gouraud",
                          cmap="magma", vmin=0, vmax=4, rasterized=True)
    grid.set(xlim=(-3, 3), ylim=(0, 4), aspect="equal",
             xlabel=r"$x/\lambda$ (dimensionless)", ylabel=r"$z/\lambda$ (dimensionless)")
    grid.set_xticks(np.arange(-3, 4))
    grid.set_yticks(np.arange(5))
    grid.set_title(r"Scalar fringes: $\Lambda/\lambda=1$; no $z$ dependence", fontsize=11, pad=15)
    colourbar = fig.colorbar(mesh, ax=grid, pad=.025, fraction=.045, ticks=np.arange(5))
    colourbar.set_label(r"$I_{\mathrm{scalar}}/I_0$", fontsize=11)
    fig.suptitle("Two ideal plane waves: stationary interference stripes", fontsize=15, y=.98)
    fig.text(.5, .89, r"$\delta=2kx\sin\theta$, $\theta=30^\circ$, length unit $\lambda=1$",
             ha="center", fontsize=12)
    fig.text(.5, .105, r"$I_0$: each beam's along-beam flux; $\langle S_z\rangle=I_{\mathrm{scalar}}\cos\theta$.",
             ha="center", fontsize=11)
    fig.text(.5, .045, "Ideal plane-wave model; no slits, point sources or near-field calculation.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "two-beam-interference-fringes.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
