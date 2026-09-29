"""Original conformal diagrams for unlimited and limited message exchanges."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(9.2, 5.5), layout='constrained')
for ax in axes:
    ax.set(xlim=(-0.18, 1.18), xticks=[0, 1], xticklabels=['Our galaxy', 'Other galaxy'],
           xlabel=r'Comoving position $x/\chi$')
    ax.axvline(0, color='#777777', lw=1)
    ax.axvline(1, color='#777777', lw=1)
    ax.grid(axis='y', alpha=0.2)
    ax.set_aspect(0.34)
axes[0].set(ylim=(-0.15, 4.65), yticks=range(5),
            ylabel=r'Conformal time elapsed / $(\chi/c)$',
            title='Matter-only: unlimited future conformal time')
for n in range(4):
    start, end = (0, 1) if n%2==0 else (1, 0)
    axes[0].annotate('', (end, n+1), (start, n),
                     arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#16659c'})
b = 1-1/np.sqrt(2)
axes[0].text(0.1, 0.13, r'$t_0$', fontsize=10)
axes[0].text(0.13, 2.04, r'$t_2/t_0\approx3.988$', fontsize=10)
axes[0].text(0.13, 4.08, r'$t_4/t_0\approx$'+f'{(1+4*b)**3:.2f}', fontsize=10)
axes[0].annotate('Future continues', (0.5, 4.6), (0.5, 4.3), ha='center',
                 arrowprops={'arrowstyle': '->', 'color': '#777777'}, fontsize=10)

ax=axes[1]
ax.set(ylim=(-0.15, 4.65), yticks=[0, 1, 1.6, 2, 3, 4],
       title=r'Persistent $\Lambda>0$: finite future interval')
ax.axhspan(1.6, 4.65, color='#eeeeee')
ax.axhline(1.6, color='#b22428', ls='--', lw=1.7)
ax.annotate('', (1, 1), (0, 0), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#16659c'})
ax.annotate('', (0.4, 1.6), (1, 1), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#b45b14'})
ax.text(0.5, 2.0, 'Future conformal boundary\n(at infinite cosmic time)', ha='center', fontsize=10)
ax.text(0.5, 3.15, 'Illustrative remaining interval: 1.6\nOne outward leg fits.\nA two-leg round trip cannot fit.', ha='center', va='center', fontsize=10)
ax.text(0.13, 0.14, 'Send now', fontsize=9)
ax.text(0.35, 1.02, 'Immediate reply', fontsize=9, color='#99480a')
fig.suptitle('Signal paths are straight in conformal coordinates', fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
