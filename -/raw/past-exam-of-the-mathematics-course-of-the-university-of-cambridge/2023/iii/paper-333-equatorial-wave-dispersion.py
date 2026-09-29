#!/usr/bin/env python3
"""Generate paper-333-equatorial-wave-dispersion.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


k = np.linspace(-4.5, 4.5, 900)
roots = np.empty((3, len(k)))
for index, wave_number in enumerate(k):
    roots[:, index] = np.sort(np.roots((1, 0, -(wave_number**2 + 3), -wave_number)).real)

fig, ax = plt.subplots(figsize=(8.5, 5.2), layout="constrained")
ax.plot(k, roots[2], color="#d62728", linewidth=2.1, label="eastward inertia–gravity")
ax.plot(k, roots[0], color="#9467bd", linewidth=2.1, label="westward inertia–gravity")
ax.plot(k, roots[1], color="#1f77b4", linewidth=2.5, label="Rossby")
ax.plot(k, k, color="#2ca02c", linewidth=2.0, label="Kelvin $\\omega=k c$")
ax.plot(k, -k / 3, color="0.35", linestyle="--", linewidth=1.2, label="long-wave Rossby $\\omega=-kc/3$")
ax.axhline(0, color="0.75", linewidth=0.8)
ax.axvline(0, color="0.75", linewidth=0.8)
ax.set(xlabel="dimensionless zonal wavenumber $k(c/\\beta)^{1/2}$", ylabel="dimensionless frequency $\\omega/(\\beta c)^{1/2}$", title="$n=1$ equatorial shallow-water dispersion", xlim=(-4.5, 4.5), ylim=(-5.2, 5.2))
ax.grid(alpha=0.18)
ax.legend(ncol=2, fontsize=8, loc="upper left")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
