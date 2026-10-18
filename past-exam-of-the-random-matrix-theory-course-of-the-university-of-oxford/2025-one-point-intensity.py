"""Generate the original GUE n=3 intensity figure (Python 3.14; dependencies in pyproject.toml)."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2025-rmt-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def intensity(x):
    return (x**4 + 3) * np.exp(-x*x/2) / (2*np.sqrt(2*np.pi))


fig, ax = plt.subplots(figsize=(6.6, 3.1), dpi=100, facecolor='white')
ax.set_facecolor('white')
x = np.linspace(-4.6, 4.6, 1500)
ax.plot(x, intensity(x), color='#195f93', linewidth=2)
maxima = np.array([-np.sqrt(3), 0, np.sqrt(3)])
ax.scatter(maxima, intensity(maxima), color='#195f93', s=27, zorder=3)
minima = np.array([-1., 1.])
ax.scatter(minima, intensity(minima), facecolor='white', edgecolor='#195f93', s=27, zorder=3)
ax.set_xlim(-4.6, 4.6)
ax.set_ylim(0, .67)
ax.set_xticks([-4, -np.sqrt(3), -1, 0, 1, np.sqrt(3), 4],
              ['$-4$', '$-\\sqrt{3}$', '$-1$', '$0$', '$1$', '$\\sqrt{3}$', '$4$'])
ax.set_yticks([0, .2, .4, .6])
ax.set_xlabel('$\\lambda$', fontsize=12, labelpad=2)
ax.set_ylabel('$R_3^{(1)}(\\lambda)$', fontsize=12)
ax.set_title('GUE with three eigenvalues: one-point intensity', fontsize=12)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e4e4e4', linewidth=.6)
fig.tight_layout(pad=1.0)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False,
            metadata={'Description': 'Original plot of (lambda^4+3) exp(-lambda^2/2)/(2 sqrt(2 pi)).'})
plt.close(fig)
