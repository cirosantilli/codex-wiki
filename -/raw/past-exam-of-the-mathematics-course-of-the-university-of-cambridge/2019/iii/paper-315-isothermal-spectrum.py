#!/usr/bin/env python3
"""Write the isothermal circumbinary-planet emission sketch as a PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

h = 6.62607015e-34
c = 299792458.0
k = 1.380649e-23
r_sun = 6.957e8
au = 1.495978707e11
temperature = 6000 * np.sqrt(r_sun / (2 * au)) * (1 + 0.3**2 * 0.5**4)**0.25
wavelength_um = np.linspace(1, 45, 1600)
wavelength = wavelength_um * 1e-6
surface_flux = np.pi * 2 * h * c**2 / wavelength**5 / np.expm1(h * c / (wavelength * k * temperature)) * 1e-6
peak_um = 2.897771955e-3 / temperature * 1e6

fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.plot(wavelength_um, surface_flux, color='#235d88', lw=2.5)
ax.axvline(peak_um, color='#8a4d24', ls='--', lw=1)
ax.annotate(f'Peak near {peak_um:.1f} μm', xy=(peak_um, surface_flux.max()),
            xytext=(18, surface_flux.max() * 0.95),
            arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=11)
ax.set_title(f'Opaque isothermal atmosphere: T = {temperature:.0f} K')
ax.set_xlabel('Wavelength (μm)')
ax.set_ylabel('Emergent surface flux (W m⁻² μm⁻¹)')
ax.set_xlim(1, 45)
ax.set_ylim(0, surface_flux.max() * 1.15)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white')
plt.close(fig)
