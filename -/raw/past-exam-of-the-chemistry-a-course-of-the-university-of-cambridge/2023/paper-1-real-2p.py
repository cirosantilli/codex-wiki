"""Real hydrogen 2p sections; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

u = np.linspace(-7, 7, 401)
x, y = np.meshgrid(u, u)
r = np.hypot(x, y)
fields = [x * np.exp(-r / 2) / np.sqrt(32*np.pi),
          y * np.exp(-r / 2) / np.sqrt(32*np.pi)]
limit = max(np.max(np.abs(a)) for a in fields)
fig, axes = plt.subplots(1, 2, figsize=(8, 3.8), layout='constrained')
for ax, field, name, node in zip(axes, fields, ['$2p_x$', '$2p_y$'], ['x', 'y']):
    im = ax.contourf(x, y, field, levels=np.linspace(-limit, limit, 19),
                     cmap='RdBu_r', norm=TwoSlopeNorm(0, -limit, limit))
    if node == 'x':
        ax.axvline(0, ls='--', color='0.18', lw=1)
        ax.text(.35, 5.5, '$x=0$', fontsize=10)
    else:
        ax.axhline(0, ls='--', color='0.18', lw=1)
        ax.text(3.8, .35, '$y=0$', fontsize=10)
    ax.plot(0, 0, 'ko', ms=3)
    ax.set(xlabel='$x/a_0$', ylabel='$y/a_0$', aspect='equal', title=name+' at $z=0$')
    ax.set_xticks([-6, -3, 0, 3, 6]); ax.set_yticks([-6, -3, 0, 3, 6])
cbar = fig.colorbar(im, ax=axes, shrink=.8, ticks=[-limit, 0, limit])
cbar.set_ticklabels(['negative', '0', 'positive'])
cbar.set_label('wavefunction sign and amplitude')
fig.savefig(Path(__file__).stem+'.png', dpi=130, facecolor='white')
plt.close(fig)
