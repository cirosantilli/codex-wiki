"""Original tree sketch: Python 3.14, Matplotlib 3.10.7.

Writes its opaque PNG basename to cwd. The caller supplies MPLCONFIGDIR;
Matplotlib respects that setting. The repository Makefile supplies it in use.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=100, facecolor='white')
for ax, depth in zip(axes, (2, 4)):
    for j in range(depth):
        ax.plot([0, 0], [-j, -j - 1], color='#17324d', lw=2)
    for x in (-0.9, 0.9):
        ax.plot([0, x], [-depth, -depth - 1], color='#17324d', lw=2)
        ax.scatter([x], [-depth - 1], s=55, color='#17324d', zorder=3)
    ax.scatter([0] * depth, [-j for j in range(depth)], s=55, color='#17324d', zorder=3)
    ax.scatter([0], [-depth], s=85, color='#ce641b', zorder=4)
    ax.text(-0.2, 0.22, 'root', ha='right', fontsize=11)
    ax.text(0.25, -depth, f'branch at depth {depth}', va='center', fontsize=11, color='#a14c12')
    ax.set_title(f'$T_{depth}$', fontsize=16)
    ax.set_xlim(-1.7, 2.5)
    ax.set_ylim(-5.45, 0.65)
    ax.set_facecolor('white')
    ax.axis('off')
fig.suptitle('Root-preserving adjacency embeddings preserve branching depth', fontsize=13)
fig.subplots_adjust(top=0.80, bottom=0.05, left=0.03, right=0.98, wspace=0.10)
fig.savefig(Path('paper-20-tree-antichain.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
