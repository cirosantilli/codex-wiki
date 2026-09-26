#!/usr/bin/env python3
"""Generate paper-312-cmb-temperature-power.svg."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.hashsalt"] = "codex-wiki"


def gaussian(x: np.ndarray, centre: float, width: float, height: float) -> np.ndarray:
    return height * np.exp(-0.5 * ((x - centre) / width) ** 2)


ell = np.linspace(2.0, 3000.0, 4000)

# These curves are schematic. They show the large-angle Sachs--Wolfe
# contribution, Doppler/acoustic structure, and Silk damping rather than a
# fit to a particular cosmological data set.
sachs_wolfe = 1000.0 * np.exp(-(ell / 250.0) ** 1.35)
doppler = (
    gaussian(ell, 390.0, 72.0, 1000.0)
    + gaussian(ell, 680.0, 82.0, 650.0)
    + gaussian(ell, 980.0, 92.0, 360.0)
)
acoustic = (
    gaussian(ell, 220.0, 62.0, 4550.0)
    + gaussian(ell, 535.0, 88.0, 2050.0)
    + gaussian(ell, 780.0, 92.0, 1650.0)
    + gaussian(ell, 1060.0, 125.0, 760.0)
)
total = sachs_wolfe + acoustic
total += 35.0 * np.exp(-ell / 1300.0)

fig, ax = plt.subplots(figsize=(10.0, 5.6), layout="constrained")
ax.plot(ell, total, color="black", linewidth=2.5, label="total")
ax.plot(ell, sachs_wolfe, color="#1f77b4", linewidth=2.0, label="Sachs–Wolfe")
ax.plot(ell, doppler, color="#d62728", linewidth=2.0, label="Doppler")

ax.axvline(30.0, color="0.45", linestyle=":", linewidth=1.0)
ax.axvline(220.0, color="0.45", linestyle=":", linewidth=1.0)
ax.axvline(1000.0, color="0.45", linestyle=":", linewidth=1.0)
ax.text(45.0, 5100.0, r"$\ell\sim30$", rotation=90, va="top")
ax.text(235.0, 5100.0, "first peak " + r"$\ell\sim220$", rotation=90, va="top")
ax.text(1015.0, 5100.0, "damping tail", rotation=90, va="top")

ax.set_xlim(0.0, 3000.0)
ax.set_ylim(0.0, 5800.0)
ax.set_xlabel(r"angular multipole $\ell$")
ax.set_ylabel(r"$D_\ell=\ell(\ell+1)C_\ell/(2\pi)\;[\mu{\rm K}^2]$")
ax.set_title("Schematic CMB temperature anisotropy spectrum")
ax.grid(alpha=0.2)
ax.legend(loc="upper right")

output = Path(__file__).with_suffix(".svg")
fig.savefig(output, metadata={"Date": None})
plt.close(fig)
# Matplotlib writes spaces after many SVG path commands. Removing them keeps
# the generated artifact clean under \`git diff --check\`.
output.write_text(
    "\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n"
)
