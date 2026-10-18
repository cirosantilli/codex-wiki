"""Original 2021 short-options solution figure; Python 3.14, NumPy/Matplotlib.

Run from the desired output directory. The only figure output is the PNG
with this script's basename, written in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

h = 6.62607015e-34
c = 299792458.0
k = 1.380649e-23
wavelength_um = np.linspace(0.5, 60.0, 2500)
wavelength_m = wavelength_um * 1e-6

def exitance(temperature):
    """Hemispherical spectral exitance in W m^-2 micrometre^-1."""
    return (2 * np.pi * h * c**2 / wavelength_m**5
            / np.expm1(h * c / (wavelength_m * k * temperature)) * 1e-6)

skin = exitance(308.15)
room = exitance(293.15)
fig, ax = plt.subplots(figsize=(8.8, 4.5), dpi=120, facecolor="white")
ax.set_facecolor("white")
ax.plot(wavelength_um, skin, color="#b83f32", lw=2.2, label="Skin: 35 °C (308.15 K)")
ax.plot(wavelength_um, room, color="#286ba5", lw=2.2, label="Surroundings: 20 °C (293.15 K)")
ax.fill_between(wavelength_um, room, skin, color="#e4a25b", alpha=0.48,
                label="Difference: net outward emission")
ax.set(xlim=(0, 50), ylim=(0, 40), xlabel="Wavelength (µm)",
       ylabel="Spectral exitance (W m⁻² µm⁻¹)",
       title="Overlapping thermal spectra reduce net radiative loss")
ax.annotate("Skin wavelength peak: 9.40 µm", xy=(9.40377, np.max(skin)),
            xytext=(18, 35), arrowprops={"arrowstyle": "->", "color": "#555555"},
            fontsize=10)
ax.text(25, 18, "Full-spectrum net flux: 92.5 W m⁻²\nFor 2 m² of exposed skin: 185 W", fontsize=10,
        bbox={"boxstyle": "round,pad=0.5", "facecolor": "white", "edgecolor": "#bbbbbb"})
ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.83), fontsize=9, frameon=False)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
plt.close(fig)
