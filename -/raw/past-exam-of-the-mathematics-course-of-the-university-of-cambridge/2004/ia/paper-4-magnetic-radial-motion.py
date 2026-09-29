"""Original radial-motion sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-4-magnetic-radial-motion.png to the caller's working
 directory. The caller supplies MPLCONFIGDIR when needed.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r = np.linspace(0.30, 7.0, 1600)
fig, ax = plt.subplots(figsize=(8.4, 4.8), facecolor='white')
colors = ['#2166ac', '#a05a00', '#208346']
for speed, color, label in zip([0.6, 1.0, 1.3], colors,
                               [r'Bound: $v_\perp/|c|=0.6$',
                                r'Marginal escape: $v_\perp/|c|=1$',
                                r'Escape: $v_\perp/|c|=1.3$']):
    w = speed**2 - (1/r - 1)**2
    ax.plot(r, w, color=color, lw=2, label=label)
    ax.axhline(speed**2 - 1, color=color, ls='--', lw=0.8, alpha=0.6)
    roots = [1/(1+speed)]
    if speed < 1:
        roots.append(1/(1-speed))
    ax.plot(roots, np.zeros(len(roots)), 'o', color=color, ms=5)
ax.axhline(0, color='black', lw=1)
ax.axvline(1, color='#888888', ls=':', lw=1)
ax.axvspan(0.30, 1/2.3, color='#eeeeee', alpha=0.7)
ax.text(4.35, -0.58, 'Negative values are inaccessible', fontsize=10)
ax.text(1.08, 1.95, r'Maximum at $r=r_c$', fontsize=10)
ax.set(xlim=(0.30, 7), ylim=(-0.8, 2.2),
       xlabel=r'$r/r_c$, with $r_c=|\ell/c|$ and $\ell c>0$',
       ylabel=r'$\dot r^2/c^2$',
       title='Radial motion in an inverse-radius axial magnetic field')
ax.legend(loc='upper right', framealpha=1, fontsize=9)
ax.grid(alpha=0.18)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-4-magnetic-radial-motion.png', dpi=130,
            facecolor='white', transparent=False)
plt.close(fig)
