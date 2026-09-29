"""Radial cubic-diffusion profiles. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Emit the opaque PNG basename in the caller's cwd; preserve supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4.6), dpi=120, facecolor='white')
for tau, color in [(0.1, '#0072B2'), (1.0, '#D55E00'), (10.0, '#009E73')]:
    scale = tau ** (1 / 6)
    xi = np.linspace(0, 1, 1001)
    radius = np.concatenate((scale * xi, [1.7]))
    density = np.concatenate((scale ** -2 * np.sqrt(np.maximum(1 - xi ** 2, 0)), [0]))
    ax.plot(radius, density, color=color, linewidth=2.2, label=rf'$\tau={tau:g}$')
    ax.plot([scale], [0], 'o', color=color, markersize=5)
ax.set(xlim=(0, 1.7), ylim=(0, 2.35), xlabel=r'Radius $r/r_0$', ylabel=r'Density $n/n_0$', title='Radial cubic diffusion: expanding front, falling peak')
ax.text(0.97, 0.93, r'$\tau=6D_0t/r_0^2$', ha='right', va='top', transform=ax.transAxes)
ax.legend(loc='upper center', frameon=False)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(Path('paper-66-insect-spread.png'), facecolor='white', transparent=False)
plt.close(fig)
