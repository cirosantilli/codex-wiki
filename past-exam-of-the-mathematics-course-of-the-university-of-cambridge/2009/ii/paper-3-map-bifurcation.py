"""Cubic-map fixed points; Python 3.14, NumPy/Matplotlib from root pyproject."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=140, facecolor='white')
r = np.linspace(4, 9, 1000)
xlo = (1 - np.sqrt(1 - 4/r))/2
xhi = 1 - xlo
ax.plot([0, 9], [0, 0], color='#1769aa', lw=2, label='Attracting fixed points')
ax.plot(r, xlo, '--', color='#b33b35', lw=2, label='Repelling fixed points')
cut = r <= 16/3
ax.plot(r[cut], xhi[cut], color='#1769aa', lw=2)
ax.plot(r[~cut], xhi[~cut], '--', color='#b33b35', lw=2)
ax.scatter([4, 16/3], [.5, .75], c='black', s=28, zorder=5)
ax.annotate('Saddle-node\n(4, 1/2)', (4, .5), (2.5, .72), arrowprops={'arrowstyle':'->'})
ax.annotate('Period doubling\n(16/3, 3/4)', (16/3, .75), (5.8, .52), arrowprops={'arrowstyle':'->'})
ax.axvline(27/4, color='.6', lw=1, ls=':')
ax.text(27/4+.12, .17, 'Interval-invariance\nlimit r = 27/4', fontsize=9)
ax.set(xlabel='Parameter r', ylabel='Fixed point x', xlim=(0, 9), ylim=(-.06, 1.03), title='Fixed points of x ↦ r x²(1 − x)')
ax.legend(loc='upper left', fontsize=9)
ax.grid(alpha=.2)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-3-map-bifurcation.png', facecolor='white', transparent=False)
