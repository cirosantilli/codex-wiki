"""Ideal Raman line positions only; no model of populations or intensities."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(8, 4.7), sharex=True, layout='constrained')
for ax in axes:
    ax.axhline(0, color='0.45', lw=.9)
    ax.vlines(0, 0, 1, color='0.4', lw=2)
    ax.text(0, 1.06, 'Rayleigh', ha='center', fontsize=10)
    ax.set(ylim=(-.1, 1.65), xlim=(-1.4, 19.8), yticks=[])
    ax.spines[['left','right','top']].set_visible(False)
    ax.tick_params(axis='x', length=3)
axes[0].vlines([6,10,14,18], 0, 1, color='#245c9f', lw=2.4)
axes[0].set_title('Diatomic: $\\Delta J=+2$', fontsize=12)
axes[0].annotate('', (6, 1.34), (10, 1.34), arrowprops={'arrowstyle':'<->'})
axes[0].text(8, 1.43, '$4\\widetilde B$', ha='center', fontsize=11)
axes[0].text(3, .28, 'first shift $6\\widetilde B$', ha='center', fontsize=10)
axes[1].vlines(np.arange(4,19,2), 0, 1, color='#37774b', lw=2.4,
               label='$\\Delta J=+1$')
axes[1].plot([6,10,14,18], [1]*4, 'o', ms=5.5, color='#b45309',
             label='also $\\Delta J=+2$')
axes[1].set_title('BF$_3$: combined series (no line at $2\\widetilde B$)', fontsize=12)
axes[1].annotate('', (4, 1.34), (6, 1.34), arrowprops={'arrowstyle':'<->'})
axes[1].text(5, 1.43, '$2\\widetilde B$', ha='center', fontsize=11)
axes[1].legend(loc='upper right', fontsize=10, frameon=False)
axes[1].set_xticks(np.arange(0,19,2))
axes[1].set_xlabel(r'positive Raman shift $(\widetilde\nu_L-\widetilde\nu_S)/\widetilde B$')
fig.savefig(Path(__file__).stem+'.png', dpi=140, facecolor='white')
plt.close(fig)
