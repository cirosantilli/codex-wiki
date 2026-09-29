"""Finite pair geometry and exact/ideal field ratios; analytical model.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'figure.facecolor': 'white'})
fig, (geometry, ratios) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained',
                                      gridspec_kw={'width_ratios': [0.9, 1.1]})
fig.suptitle('Finite pair versus ideal dipole — exact analytical model, not data', fontsize=15)
geometry.axhline(0, color='#aab2b8', lw=1)
geometry.axvline(0, color='#aab2b8', lw=1)
geometry.plot([0, 0], [-0.5, 0.5], color='#6b7379', lw=3)
for z, label, color in [(-0.5, r'$-q$', '#2879aa'), (0.5, r'$+q$', '#c44335')]:
    geometry.scatter(0, z, s=470, color=color, zorder=4)
    geometry.text(0, z, label, ha='center', va='center', color='white', zorder=5)
geometry.annotate('', (-0.55, 0.5), (-0.55, -0.5), arrowprops={'arrowstyle': '<->', 'color': '#6b7379'})
geometry.text(-0.72, 0, r'$d$', va='center')
geometry.annotate('', (0.4, 0.42), (0.4, -0.42), arrowprops={'arrowstyle': '-|>', 'color': '#168059', 'lw': 2})
geometry.text(0.51, 0.05, r'$\mathbf{p}$', color='#168059')
geometry.scatter([0, 1.6], [1.7, 0], color=['#7b4b9b', '#d78316'], zorder=4)
geometry.annotate('', (0, 2.35), (0, 1.8), arrowprops={'arrowstyle': '-|>', 'color': '#7b4b9b', 'lw': 2.3})
geometry.annotate('', (1.6, -0.72), (1.6, -0.12), arrowprops={'arrowstyle': '-|>', 'color': '#d78316', 'lw': 2.3})
geometry.text(0.16, 1.72, 'Outer axis', color='#7b4b9b', fontsize=11)
geometry.text(0.88, -1.0, 'Perpendicular bisector', color='#b86e0e', fontsize=11)
geometry.text(-0.16, 2.55, '$z$', ha='center')
geometry.text(2.32, -0.2, '$x$')
geometry.text(-0.1, -1.5, 'Arrows show field direction only', ha='center', fontsize=10)
geometry.set(xlim=(-1.1, 2.5), ylim=(-1.7, 2.8), aspect='equal', title='Pair centered at the origin')
geometry.axis('off')

r_over_d = np.geomspace(0.8, 20, 450)
axial_ratio = (1 - 1 / (4 * r_over_d**2))**-2
bisector_ratio = (1 + 1 / (4 * r_over_d**2))**-1.5
ratios.semilogx(r_over_d, axial_ratio, color='#7b4b9b', lw=2.6, label='Outer axial component')
ratios.semilogx(r_over_d, bisector_ratio, color='#d78316', lw=2.6, label='Perpendicular-bisector component')
ratios.axhline(1, color='#5e6870', ls='--', lw=1.4, label='Ideal dipole: ratio = 1')
ratios.axvline(5, color='#bfc7cc', ls=':', lw=1)
ratios.scatter([5, 5], [(1 - 1/100)**-2, (1 + 1/100)**-1.5], color=['#7b4b9b', '#d78316'], zorder=4)
ratios.text(5.35, 1.23, 'At r = 5d:\n+2.03% axial\n−1.48% bisector', fontsize=10,
            bbox={'facecolor': 'white', 'edgecolor': '#dce0e3', 'boxstyle': 'round,pad=0.4'})
ratios.set(xlim=(0.8, 20), ylim=(0.45, 2.8), xlabel=r'Distance / separation $r/d$',
           ylabel=r'Exact component / ideal component', title='Convergence far from the charges')
ratios.set_xticks([1, 2, 5, 10, 20], ['1', '2', '5', '10', '20'])
ratios.legend(fontsize=9, loc='upper right')
ratios.grid(alpha=0.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
plt.close(fig)
