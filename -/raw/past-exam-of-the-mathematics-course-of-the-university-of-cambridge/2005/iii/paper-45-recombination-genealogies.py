"""Draw incompatible marginal genealogies; write PNG to the caller's CWD.
Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.4), facecolor='white')
orders = [('00', '01', '10', '11'), ('00', '10', '01', '11')]
colors = ['#1858a8', '#923b8f']
xs = np.array([0.1, 0.9, 2.1, 2.9])
for ax, order, color, site in zip(axs, orders, colors, ['A', 'B']):
    root = (1.5, 2.25)
    for parent, leaves in [((0.5, 1.2), [0, 1]), ((2.5, 1.2), [2, 3])]:
        ax.plot([root[0], parent[0]], [root[1], parent[1]], color='#303030', lw=1.8)
        for j in leaves:
            ax.plot([parent[0], xs[j]], [parent[1], 0.25], color='#303030', lw=1.8)
            ax.text(xs[j], 0.02, order[j], ha='center', va='top', fontsize=12,
                    color=color if j >= 2 else '#303030')
        ax.plot(*parent, 'o', ms=4, color='#303030')
    ax.plot(*root, 'o', ms=4, color='#303030')
    dot = (2.15, 1.57)
    ax.plot(*dot, 'o', ms=7, color=color)
    ax.annotate(f'{site}: 0 → 1', xy=dot, xytext=(2.7, 1.98), fontsize=10,
                color=color, ha='center', arrowprops={'arrowstyle': '-', 'color': color})
    ax.set_title(f'Site {site}: derived clade {"{10,11}" if site == "A" else "{01,11}"}', fontsize=11)
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-0.38, 2.65)
    ax.axis('off')
fig.suptitle('Different local trees admit all four haplotypes', fontsize=13, y=0.98)
fig.text(0.5, 0.025, 'Leaf labels give alleles at A and B; each local tree needs just one mutation.',
         ha='center', fontsize=10)
fig.tight_layout(rect=(0, 0.075, 1, 0.9))
fig.savefig(Path.cwd() / 'paper-45-recombination-genealogies.png', dpi=130,
            facecolor='white', transparent=False)
plt.close(fig)
