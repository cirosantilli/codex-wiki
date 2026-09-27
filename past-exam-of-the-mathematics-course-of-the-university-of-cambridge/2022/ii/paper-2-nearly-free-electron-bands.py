#!/usr/bin/env python3
"""Generate paper-2-nearly-free-electron-bands.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


q = np.linspace(-5.2, 5.2, 1800)
fig, ax = plt.subplots(figsize=(9.0, 5.4), layout="constrained")
for reciprocal_shift in range(-4, 5, 2):
    ax.plot(q, (q - reciprocal_shift) ** 2 / 2 + 1, color="0.75", linewidth=1.0)

for crossing, gap, color, label in ((2.0, 4 / 3, "#d62728", "$n=2$ gap"), (4.0, 1 / 3, "#1f77b4", "$n=4$ gap")):
    for sign in (-1, 1):
        centre = sign * crossing
        local = np.linspace(centre - 0.72, centre + 0.72, 260)
        kappa = local - centre
        centre_energy = 1 + crossing**2 / 2 + kappa**2 / 2
        splitting = np.sqrt((crossing * kappa) ** 2 + (gap / 2) ** 2)
        ax.plot(local, centre_energy + splitting, color=color, linewidth=2.5, label=label if sign == 1 else None)
        ax.plot(local, centre_energy - splitting, color=color, linewidth=2.5)
        ax.annotate("", (centre + 0.03, centre_energy[len(local)//2] + gap / 2), (centre + 0.03, centre_energy[len(local)//2] - gap / 2), arrowprops={"arrowstyle": "<->", "color": color})

ax.set(xlabel="$ka/\\pi$", ylabel="energy in schematic units", title="Extended-zone nearly-free-electron bands", xlim=(-5.2, 5.2), ylim=(0.5, 16))
ax.grid(alpha=0.16)
ax.legend(loc="upper center", ncol=2)
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
