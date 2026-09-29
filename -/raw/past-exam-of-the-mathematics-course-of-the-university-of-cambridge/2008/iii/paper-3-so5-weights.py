"""Defining and adjoint B2 weights; Python 3.14, matplotlib 3.10.7.
Output is a white opaque PNG in caller CWD; caller MPLCONFIGDIR is respected.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

short=[(1, 0), (-1, 0), (0, 1), (0, -1)]
long=[(x, y) for x in (-1, 1) for y in (-1, 1)]
fig, axes=plt.subplots(1, 2, figsize=(9.2, 4.5), dpi=110, facecolor='white')
for ax, title, weights in zip(axes, ['Defining representation', 'Adjoint representation'], [dict.fromkeys(short+[(0, 0)], 1), dict.fromkeys(short+long, 1)|{(0, 0):2}]):
    for t in (-1, 0, 1):
        ax.axhline(t, color='#e3e8ef', lw=.8, zorder=0)
        ax.axvline(t, color='#e3e8ef', lw=.8, zorder=0)
    for (x, y), multiplicity in weights.items():
        ax.scatter([x], [y], s=380, color='#1f618d', zorder=3)
        ax.text(x, y, str(multiplicity), color='white', ha='center', va='center', fontsize=12, weight='bold', zorder=4)
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.55, 1.55)
    ax.set_aspect('equal')
    ax.set_xticks([-1, 0, 1], [r'$-L_1$', '0', r'$L_1$'])
    ax.set_yticks([-1, 0, 1], [r'$-L_2$', '0', r'$L_2$'])
    ax.set_title(title, fontsize=14)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
fig.suptitle(r'$\mathfrak{so}_5$: weights and multiplicities', fontsize=17)
fig.text(.5, .045, 'Circle numbers are weight-space dimensions; coordinate axes are $L_1$ and $L_2$', ha='center', fontsize=11)
fig.subplots_adjust(left=.06, right=.97, top=.8, bottom=.19, wspace=.25)
fig.savefig(Path('paper-3-so5-weights.png'), facecolor='white', transparent=False)
plt.close(fig)
