"""Original sketches for MCB 2025 Paper 1; write the PNG to the cwd."""
from pathlib import Path
from math import lgamma
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout='constrained', facecolor='white')
x = np.linspace(0.0001, 3.5, 1200)
axes[0].plot(x, x - 1 - x * np.log(x), color='#245c9f', lw=2.4)
axes[0].axhline(0, color='0.45', lw=0.8)
axes[0].axvline(0, color='0.45', lw=0.8)
axes[0].plot(0, -1, marker='o', mfc='white', mec='#245c9f', ms=7, clip_on=False)
axes[0].plot(1, 0, 'o', color='#245c9f')
axes[0].annotate('Maximum (1, 0)', (1, 0), xytext=(1.5, -0.4), arrowprops={'arrowstyle': '->'})
axes[0].set(xlim=(-0.08, 3.5), ylim=(-2.1, 0.25), xlabel='x', ylabel='f(x)', title=r'$f(x)=x-1-x\log x$')
p = np.linspace(0.00001, 0.7, 1200)
log_beta = lgamma(9) + lgamma(38) - lgamma(47)
y = np.exp(8 * np.log(p) + 37 * np.log1p(-p) - log_beta)
axes[1].plot(p, y, color='#245c9f', lw=2.4)
axes[1].fill_between(p, y, alpha=0.12, color='#245c9f')
axes[1].axvline(8 / 45, color='#b45309', lw=1.3, ls='--', label='Mode 8/45')
axes[1].axvline(9 / 47, color='#21633d', lw=1.3, ls=':', label='Mean 9/47')
axes[1].set(xlim=(0, 0.7), ylim=(0, y.max() * 1.13), xlabel='Daily event probability p', ylabel='Posterior density', title=r'Censored observations: $\mathrm{Beta}(9,38)$')
axes[1].legend(frameon=False, loc='upper right', fontsize=10)
for ax in axes:
    ax.grid(alpha=0.16)
    ax.spines[['top', 'right']].set_visible(False)
fig.savefig(Path('paper-1-sketches.png'), dpi=140, facecolor='white')
plt.close(fig)
