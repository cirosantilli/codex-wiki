#!/usr/bin/env python3
"""Generate paper-315-pressure-temperature.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np



pressure = np.logspace(-5.0, 2.0, 1000)  # bar
x = np.log10(pressure / 1e-3)
temperature = np.where(x <= 0.0, 800.0, 800.0 + 50.0 * x**2)

fig, ax = plt.subplots(figsize=(6.6, 6.0), layout="constrained")
ax.plot(temperature, pressure, color="#d62728", linewidth=2.5)
for p, t, label in (
    (1e-3, 800.0, "1 mbar: 800 K"),
    (1.0, 1250.0, "1 bar: 1250 K"),
    (10.0, 1600.0, "10 bar: 1600 K"),
    (100.0, 2050.0, "100 bar: 2050 K"),
):
    ax.scatter((t,), (p,), color="black", s=26, zorder=3)
    ax.annotate(label, (t, p), xytext=(8, 4), textcoords="offset points", fontsize=9)
ax.set_yscale("log")
ax.invert_yaxis()
ax.set_xlabel("temperature [K]")
ax.set_ylabel("pressure [bar]")
ax.set_title("Retrieved-profile extrapolation")
ax.grid(alpha=0.2, which="both")

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
