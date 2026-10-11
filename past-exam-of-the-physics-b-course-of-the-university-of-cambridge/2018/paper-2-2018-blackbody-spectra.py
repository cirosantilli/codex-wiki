"""Original frequency spectra. Python 3.14; dependencies in pyproject.toml.

Run from the mirrored _media directory; writes the PNG basename to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 20, 1800)
fig, ax = plt.subplots(figsize=(7.0, 4.1), facecolor='white', layout='constrained')
for ratio, color in [(1.0, '#29688d'), (1.5, '#d38b19'), (2.0, '#a73939')]:
    y = x**3 / np.expm1(x / ratio)
    ax.plot(x, y, color=color, lw=2, label=f'$T/T_{{\\mathrm{{ref}}}}={ratio:g}$')
    peak = 2.821439372 * ratio
    ax.plot(peak, peak**3 / np.expm1(peak / ratio), '.', color=color, ms=8)
ax.set(xlim=(0, 20), ylim=(0, 12.5), xlabel='$h\\nu/(k_B T_{\\mathrm{ref}})$', ylabel='$u_\\nu c^3h^2/[8\\pi(k_BT_{\\mathrm{ref}})^3]$', title='Thermal radiation: frequency spectra')
ax.legend(frameon=False)
ax.spines[['top', 'right']].set_visible(False)
ax.set_facecolor('white')
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
