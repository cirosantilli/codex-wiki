"""Exterior-square weight diagram; Python 3.14, matplotlib 3.10.7.
Output is a white opaque PNG in the caller's CWD. Respect caller MPLCONFIGDIR.
"""
from itertools import combinations
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

weights = {}
for i, j in combinations(range(5), 2):
    weights.setdefault(8 - 2 * (i + j), []).append((i, j))
assert sum(map(len, weights.values())) == 10
fig, ax = plt.subplots(figsize=(8.5, 2.6), dpi=110, facecolor='white')
ax.axhline(0, color='#8794a5', linewidth=1)
for weight, basis in sorted(weights.items()):
    ax.scatter([weight], [0], s=600, color='#1f618d', zorder=3)
    ax.text(weight, 0, str(len(basis)), ha='center', va='center', color='white', weight='bold', fontsize=13)
    ax.text(weight, -.38, str(weight), ha='center', va='center', fontsize=12)
ax.text(0, .63, r'$\bigwedge^2\mathrm{Sym}^4\mathbb{C}^2$: weights and multiplicities', ha='center', fontsize=15)
ax.text(0, -.8, 'Numbers in circles are weight-space dimensions', ha='center', fontsize=11)
ax.set_xlim(-7.5, 7.5)
ax.set_ylim(-1.1, 1.1)
ax.axis('off')
fig.tight_layout()
fig.savefig(Path('paper-3-sl2-weights.png'), facecolor='white', transparent=False)
plt.close(fig)
