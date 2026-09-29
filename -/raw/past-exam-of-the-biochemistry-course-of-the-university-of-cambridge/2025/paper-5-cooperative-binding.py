"""Original Hill-equation illustration, not a digitization of the exam data.

Run from the desired media directory; the PNG is written to the cwd.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ligand = np.linspace(0, 2.4, 500)
half = 0.9
fig, ax = plt.subplots(figsize=(7.5, 4.8), layout='constrained', facecolor='white')
for n, colour in [(1, '#777777'), (4, '#245c9f')]:
    occupancy = ligand**n/(half**n+ligand**n)
    ax.plot(ligand, occupancy, color=colour, linewidth=2.4, label=f'Hill coefficient n = {n}')
ax.scatter([half], [0.5], color='black', zorder=4)
ax.axvline(half, color='#aaaaaa', linestyle=':', linewidth=1)
ax.axhline(0.5, color='#aaaaaa', linestyle=':', linewidth=1)
ax.set(xlabel='Free ligand concentration (µM)', ylabel='Fractional occupancy',
       xlim=(0, 2.4), ylim=(0, 1.04), title='Equal half-occupancy concentration; different response steepness')
ax.text(1.25, 0.33, r'$K_{1/2}=0.9\ \mu\mathrm{M}$', fontsize=13)
ax.legend(loc='lower right')
ax.spines[['top', 'right']].set_visible(False)
fig.savefig(Path('paper-5-cooperative-binding.png'), dpi=130, facecolor='white')
plt.close(fig)
