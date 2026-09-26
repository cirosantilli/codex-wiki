#!/usr/bin/env python3
"""Generate paper-315-earth-m-dwarf-eclipse.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np



PLANCK = 6.62607015e-34
LIGHT_SPEED = 299792458.0
BOLTZMANN = 1.380649e-23
EARTH_RADIUS = 6.371e6
SOLAR_RADIUS = 6.957e8


def planck_ratio(wavelength: np.ndarray, cool: float, hot: float) -> np.ndarray:
    factor = PLANCK * LIGHT_SPEED / (wavelength * BOLTZMANN)
    return np.expm1(factor / hot) / np.expm1(factor / cool)


wavelength_um = np.linspace(1.0, 20.0, 1000)
wavelength = wavelength_um * 1e-6
radius_ratio = EARTH_RADIUS / (0.1 * SOLAR_RADIUS)
contrast_ppm = 1e6 * radius_ratio**2 * planck_ratio(wavelength, 600.0, 3500.0)
at_17 = 1e6 * radius_ratio**2 * planck_ratio(np.array([17e-6]), 600.0, 3500.0)[0]

fig, ax = plt.subplots(figsize=(8.0, 5.2), layout="constrained")
ax.plot(wavelength_um, contrast_ppm, color="#1f77b4", linewidth=2.5)
ax.axhline(100.0, color="0.5", linestyle=":", linewidth=1.6, label="100 ppm precision")
ax.scatter((17.0,), (at_17,), color="#d62728", s=35, zorder=3)
ax.annotate(
    f"17 μm: {at_17:.0f} ppm\nSNR ≈ {at_17 / 100.0:.1f}",
    (17.0, at_17),
    xytext=(-92, -5),
    textcoords="offset points",
)
ax.set_yscale("log")
ax.set_xlim(1.0, 20.0)
ax.set_ylim(8e-6, 2e3)
ax.set_xlabel("wavelength [μm]")
ax.set_ylabel("planet-star flux ratio [ppm]")
ax.set_title("600 K Earth-size planet / 3500 K, 0.1-solar-radius star")
ax.grid(alpha=0.2, which="both")
ax.legend(loc="upper left")

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=160, facecolor="white")
plt.close(fig)
