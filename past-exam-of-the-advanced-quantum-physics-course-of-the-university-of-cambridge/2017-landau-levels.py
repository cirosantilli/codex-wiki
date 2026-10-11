"""Original Landau-level schematic. Python 3.14; matplotlib 3.10.7; numpy 2.3.5.

Run from the mirrored _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

b = np.linspace(0, 2.0, 500)
fig, ax = plt.subplots(figsize=(7.2, 4.2), layout='constrained', facecolor='white')
colors = ['#0072b2', '#e69f00', '#009e73', '#cc79a7']
for n, color in enumerate(colors):
    energy = (n + 0.5) * b
    ax.plot(b, energy, color=color, lw=2, label=rf'$n={n}$')
    crossing = 2 / (n + 0.5)
    if crossing <= 2:
        ax.plot(crossing, 2, 'o', color=color, ms=6)
ax.axhline(2, color='#333333', ls='--', lw=1.3)
ax.text(0.04, 2.08, r'$E_F$ (fixed reference)', fontsize=11)
ax.set(xlim=(0, 2), ylim=(0, 4), xlabel=r'$B/B_*$ field',
       ylabel=r'$E/(hbar eB_*/m)$', title='Orbital Landau levels (spin omitted)')
ax.legend(loc='upper left', ncols=2)
ax.grid(alpha=0.18)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
