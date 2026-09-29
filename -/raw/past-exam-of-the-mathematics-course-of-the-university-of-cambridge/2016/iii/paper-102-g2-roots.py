"""Draw the G2 roots; output paper-102-g2-roots.png in the working directory.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

alpha = np.array([1.0, 0.0])
beta = np.array([-1.5, np.sqrt(3) / 2])
positive = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
labels = [r'$\alpha$', r'$\beta$', r'$\alpha+\beta$', r'$2\alpha+\beta$', r'$3\alpha+\beta$', r'$3\alpha+2\beta$']
fig, ax = plt.subplots(figsize=(6.8, 5.4), dpi=100, facecolor='white')
ax.set_facecolor('white')
for (m, n), label in zip(positive, labels):
    root = m * alpha + n * beta
    long = np.dot(root, root) > 2
    color = '#b04b32' if long else '#177c91'
    for sign in (1, -1):
        x, y = sign * root
        ax.annotate('', xy=(x, y), xytext=(0, 0), arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5 if (m, n) in ((1, 0), (0, 1)) and sign == 1 else 1.4})
        ax.plot(x, y, 'o', color=color, ms=4)
    pos = root + 0.2 * root / np.linalg.norm(root)
    ax.text(*pos, label, ha='center', va='center', fontsize=11)
ax.plot(0, 0, 'o', color='#333333', ms=3)
ax.plot([], [], color='#177c91', lw=2, label='Short roots: length 1')
ax.plot([], [], color='#b04b32', lw=2, label=r'Long roots: length $\sqrt{3}$')
ax.set(xlim=(-2.25, 2.25), ylim=(-2.05, 2.22), aspect='equal')
ax.axis('off')
ax.set_title(r'$G_2$: a triple bond forces a rank-two component', fontsize=14, pad=12)
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.04), ncol=2, frameon=False, fontsize=10)
fig.subplots_adjust(left=0.03, right=0.97, bottom=0.11, top=0.9)
fig.savefig(Path.cwd() / 'paper-102-g2-roots.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
