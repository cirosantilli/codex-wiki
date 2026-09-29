"""Exact ceiling staircases and a stipulated whole-box capacity example.

White PNG output in CWD; supported dependency versions are in pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.grid(alpha=0.17)
for m in range(-3, 5):
    axes[0].plot([m-1, m], [m, m], color='#286f99', lw=2)
    axes[0].scatter([m-1], [m], facecolors='white', edgecolors='#286f99', s=36, zorder=4)
    axes[0].scatter([m], [m], color='#286f99', s=36, zorder=5)
axes[0].axhline(0, color='#626c72', lw=0.8)
axes[0].axvline(0, color='#626c72', lw=0.8)
axes[0].scatter([-2.7, 2.7], [-2, 3], color='#bf7042', zorder=6, s=50)
axes[0].annotate('ceil(−2.7) = −2', (-2.7, -2), xytext=(-2.95, -0.55), fontsize=10,
                 arrowprops={'arrowstyle': '->', 'color': '#bf7042'})
axes[0].annotate('ceil(2.7) = 3', (2.7, 3), xytext=(0.8, 1.55), fontsize=10,
                 arrowprops={'arrowstyle': '->', 'color': '#bf7042'})
axes[0].set(xlim=(-3.4, 3.4), ylim=(-3.6, 4.1), xticks=range(-3, 4),
            xlabel='Real input x', ylabel='Least integer at least x',
            title='Each interval (m−1, m] maps to m')
N = np.arange(111)
boxes = (N+19)//20
axes[1].scatter(N, boxes, s=10, color='#286f99')
axes[1].scatter([100, 101], [5, 6], s=45, color='#bf7042', zorder=5)
axes[1].annotate('100 items: 5 boxes', (100, 5), xytext=(30, 4.4), fontsize=10,
                 arrowprops={'arrowstyle': '->', 'color': '#bf7042'})
axes[1].annotate('101 items: 6 boxes\n120 places; 19 unused', (101, 6), xytext=(30, 6.35), fontsize=10,
                 arrowprops={'arrowstyle': '->', 'color': '#bf7042'})
axes[1].set(xlim=(-3, 112), ylim=(-0.35, 7.15), xticks=[0, 20, 40, 60, 80, 100],
            yticks=range(7), xlabel='Integer number of items N', ylabel='Boxes required: ceil(N/20)',
            title='Whole-box count with 20 places per box')
fig.text(0.5, 0.025, 'Filled endpoints are included; open endpoints are excluded. Capacity example uses nonnegative integer counts.',
         ha='center', fontsize=9.5)
fig.subplots_adjust(left=0.07, right=0.98, top=0.9, bottom=0.17, wspace=0.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), facecolor='white')
plt.close(fig)
