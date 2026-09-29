"""Sine-Gordon fluctuation plot. Tested with Python 3.14 and root pyproject dependencies.

Run from the desired output directory; Make controls the final _media location.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 801)
s = 1 / np.cosh(x)
fig, axes = plt.subplots(1, 2, figsize=(8, 4.2), dpi=100, facecolor='white')
axes[0].plot(x, 1 - 2*s*s, color='#35618f', linewidth=2.5)
axes[0].axhline(1, color='#777777', linestyle='--', linewidth=1)
axes[0].axhline(0, color='#dddddd', linewidth=1)
axes[0].set(title=r'Fluctuation potential $1-2\,\mathrm{sech}^2 x$', xlabel=r'$x$', ylabel=r'$V(x)$', ylim=(-1.2, 1.2))
axes[1].plot(x, s / np.sqrt(2), color='#b05d28', linewidth=2.5)
axes[1].set(title=r'Translational zero mode $\mathrm{sech}\,x/\sqrt{2}$', xlabel=r'$x$', ylabel=r'$\psi_0(x)$', ylim=(0, .8))
for ax in axes:
    ax.set_facecolor('white')
    ax.grid(alpha=.18)
    ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout(pad=1.5)
fig.savefig(Path.cwd() / 'paper-50-fluctuation.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
