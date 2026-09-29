"""Pentagon and its independent five-word code; Python 3.14 and root dependencies."""
import os
import tempfile

_cache = None
if 'MPLCONFIGDIR' not in os.environ:
    _cache = tempfile.TemporaryDirectory(prefix='paper-14-mpl-')
    os.environ['MPLCONFIGDIR'] = _cache.name

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(8.2, 4.1), dpi=120, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
angles = np.pi/2-2*np.pi*np.arange(5)/5
positions = np.column_stack([np.cos(angles), np.sin(angles)])
left = axes[0]
for j in range(5):
    segment = positions[[j, (j+1)%5]]
    left.plot(segment[:, 0], segment[:, 1], color='#356580', lw=2)
left.scatter(positions[:, 0], positions[:, 1], s=100, color='#356580', zorder=3)
for j, point in enumerate(positions):
    left.text(*(1.24*point), str(j), ha='center', va='center', fontsize=12)
left.set(xlim=(-1.4, 1.4), ylim=(-1.4, 1.4), title=r'$C_5$: edges at differences $\pm1$')
left.set_aspect('equal')
left.axis('off')
right = axes[1]
x, y = np.meshgrid(np.arange(5), np.arange(5))
right.scatter(x, y, color='#c4ccd2', s=40)
for j in range(5):
    k = (2*j)%5
    right.scatter(j, k, color='#a73562', s=110, zorder=3)
    right.annotate(f'({j},{k})', (j, k), xytext=(7, 7), textcoords='offset points', fontsize=10)
right.set(xlim=(-.45, 4.9), ylim=(-.45, 4.6), xticks=range(5), yticks=range(5),
          xlabel='First coordinate', ylabel='Second coordinate', title=r'Independent words $(j,2j)$')
right.set_aspect('equal')
right.grid(alpha=.12)
fig.suptitle('Five independent words in the strong square of the pentagon', fontsize=13)
fig.text(.69, .03, r'Coordinates are modulo 5; adjacent entries differ by $0$ or $\pm1$.',
         ha='center', fontsize=9)
fig.tight_layout(rect=(0, .07, 1, .91))
fig.savefig('paper-14-pentagon-code.png', facecolor='white', transparent=False)
plt.close(fig)
if _cache is not None:
    _cache.cleanup()
