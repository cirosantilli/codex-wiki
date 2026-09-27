#!/usr/bin/env python3
"""Generate paper-315-planet-star-flux-ratio.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def planck_ratio(wavelength_m, planet_temperature, star_temperature):
    c2 = 1.438776877e-2
    return np.expm1(c2 / (wavelength_m * star_temperature)) / np.expm1(c2 / (wavelength_m * planet_temperature))


wavelength_um = np.geomspace(0.3, 80, 900)
wavelength_m = wavelength_um * 1e-6
reflected = np.full_like(wavelength_um, 2.0e-5)
thermal = 0.01 * planck_ratio(wavelength_m, 1200.0, 5800.0)
total = reflected + thermal

fig, ax = plt.subplots(figsize=(9.0, 5.2), layout="constrained")
ax.loglog(wavelength_um, total, color="black", linewidth=2.6, label="total eclipse depth")
ax.loglog(wavelength_um, reflected, color="#1f77b4", linewidth=2.0, label="reflected light")
ax.loglog(wavelength_um, thermal, color="#d62728", linewidth=2.0, label="planetary thermal emission")
ax.axhline(reflected[0] + 0.01 * 1200 / 5800, color="0.45", linestyle="--", linewidth=1.1, label="Rayleigh–Jeans limit")
ax.annotate("thermal rise", (4.5, total[np.searchsorted(wavelength_um, 4.5)]), (1.5, 2e-4), arrowprops={"arrowstyle": "->"})
ax.set(xlabel="wavelength ($\\mu$m)", ylabel="$F_{p,\\lambda}/F_{*,\\lambda}$", title="Schematic planet–star flux ratio at secondary eclipse", xlim=(0.3, 80), ylim=(2e-8, 4e-3))
ax.grid(alpha=0.18, which="both")
ax.legend(loc="lower right")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
