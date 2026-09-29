"""Original thin-lens cone geometry and analytical scalings; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; the output basename follows this generator's basename.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (geometry, scaling) = plt.subplots(1, 2, figsize=(11, 5.3))
    fig.patch.set_facecolor("white")
    colors = ["#2364aa", "#c05a13"]
    f_mm, wavelength_um = 100.0, 0.55
    geometry.axhline(0, color="0.65", lw=1, ls="--")
    geometry.axvline(f_mm, color="0.5", lw=1, ls=":")
    for diameter, color in zip([25.0, 12.5], colors):
        number = f_mm / diameter
        x = np.array([0.0, f_mm])
        for sign in [-1, 1]:
            y = sign * diameter / 2 * (1 - x / f_mm)
            geometry.plot([-15, 0], [y[0], y[0]], color=color, lw=2)
            geometry.plot(x, y, color=color, lw=2)
            assert abs(y[-1]) < 1e-12
        geometry.plot([0, 0], [-diameter/2, diameter/2], color=color,
                      lw=4, alpha=0.65)
        geometry.plot([], [], color=color, lw=2,
                      label=f"D = {diameter:g} mm, f/{number:g}")
    geometry.scatter([f_mm], [0], color="black", s=25, zorder=4)
    geometry.annotate("common focus", (100, 0), (60, -25),
                      arrowprops={"arrowstyle": "->", "color": "0.3"})
    geometry.text(0, 22, "thin lens + stop", ha="center")
    geometry.annotate("", (0, -19), (100, -19),
                      arrowprops={"arrowstyle": "<->", "color": "0.3"})
    geometry.text(50, -16, "f = 100 mm", ha="center")
    geometry.set(xlim=(-18, 113), ylim=(-30, 30),
                 xlabel="axial position (mm)", ylabel="ray height (mm)",
                 title="Smaller opening, same focal length")
    geometry.set_aspect("equal", adjustable="box")
    geometry.legend(loc="upper left", bbox_to_anchor=(0, -0.21), frameon=False)
    numbers = np.linspace(4, 16, 301)
    flux_relative = (4 / numbers) ** 2
    radius_relative = numbers / 4
    scaling.plot(numbers, radius_relative, color="#7042a1", lw=2.5,
                 label="first dark-ring radius / radius at f/4")
    scaling.plot(numbers, flux_relative, color="#16806a", lw=2.5,
                 label="collected flux / flux at f/4")
    scaling.axhline(1, color="0.65", lw=1, ls=":")
    for n in [4, 8, 16]:
        scaling.scatter([n], [(4/n)**2], color="#16806a", zorder=4)
        scaling.scatter([n], [n/4], color="#7042a1", zorder=4)
    scaling.annotate("f/8: radius ×2", (8, 2), (9, 2.15), color="#7042a1")
    scaling.annotate("f/8: flux ×¼", (8, 0.25), (9, 0.55), color="#16806a")
    scaling.set(xlim=(3.6, 16.4), ylim=(0, 4.4), xticks=[4, 8, 12, 16],
                xlabel="f-number N = f / D", ylabel="dimensionless ratio",
                title="Analytical scaling at fixed f and λ")
    scaling.legend(loc="upper left", bbox_to_anchor=(-0.04, -0.15),
                   frameon=False, fontsize=9.5)
    assert np.isclose(1.22 * wavelength_um * 4, 2.684)
    assert np.isclose((12.5/25)**2, 0.25)
    assert np.isclose(np.tan(np.arctan(25/(2*f_mm))), 1/8)
    fig.suptitle("Aperture and focal ratio: cone, collection and diffraction", fontsize=16)
    fig.text(0.5, 0.015,
             "Ideal unobscured circular pupil; uniform incident beam; λ = 0.55 μm. Calculated, not measured.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.23, top=0.85, wspace=0.32)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
