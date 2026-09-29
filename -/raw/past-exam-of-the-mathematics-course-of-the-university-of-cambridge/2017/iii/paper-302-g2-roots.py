"""Generate original G2 root/weight geometry; output PNG in CWD.
Python 3.14, matplotlib 3.10.7, numpy 2.3.5; final source paper-302-g2-roots.py.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
alpha = np.array([np.sqrt(6.0), 0.0])
beta = np.array([-np.sqrt(1.5), 1.0 / np.sqrt(2.0)])
positive = [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)]
roots = positive + [(-a, -b) for a, b in positive]
weights = [(0, 0), (0, 1), (1, 1), (1, 2), (0, -1), (-1, -1), (-1, -2)]
fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=100, facecolor='white')
for ax, values, title in zip(axes, [roots, weights], ['G₂ roots: 6 long + 6 short', 'Weights of V(0,1): 6 short + zero']):
    ax.set_aspect('equal')
    ax.set(xlim=(-3.25, 3.25), ylim=(-3.25, 3.25), title=title)
    ax.axhline(0, color='#cccccc', linewidth=0.7)
    ax.axvline(0, color='#cccccc', linewidth=0.7)
    for a, b in values:
        v = a * alpha + b * beta
        color = '#b85b23' if np.dot(v, v) > 3 else '#2166ac'
        if a == b == 0:
            color = '#202020'
            offset = np.array([0.0, 0.22])
        else:
            offset = v / np.linalg.norm(v) * 0.32
            ax.annotate('', xy=v, xytext=(0, 0), arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 1.25, 'alpha': 0.7})
        ax.scatter(*v, color=color, s=35, zorder=4)
        ax.text(*(v + offset), f'({a},{b})', ha='center', va='center', fontsize=9, color=color)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
fig.text(0.5, 0.075, 'Coordinates (a,b) mean aα + bβ;  |α|²=6, |β|²=2, α·β=−3', ha='center', fontsize=11)
fig.tight_layout(rect=(0, 0.1, 1, 0.96), w_pad=2)
fig.savefig(Path.cwd() / 'paper-302-g2-roots.png', facecolor='white', transparent=False)
plt.close(fig)
