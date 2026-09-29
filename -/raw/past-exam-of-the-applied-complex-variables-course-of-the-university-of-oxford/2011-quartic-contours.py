"""Original quartic decay and contour sketch. Python 3.14, numpy 2.3.5,
matplotlib 3.10.7. Writes 2011-quartic-contours.png to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig, ax = plt.subplots(figsize=(5.8, 5.2), facecolor='white')
for j in range(4):
    ang = 45+90*j
    ax.add_patch(Wedge((0, 0), 2.15, ang-22.5, ang+22.5, facecolor='#e1edf8', edgecolor='none'))
    theta = np.deg2rad(ang)
    end = 1.95*np.array([np.cos(theta), np.sin(theta)])
    color = '#555555' if j == 0 else ['#2166a5', '#bb493d', '#6e5495'][j-1]
    ax.plot([0, end[0]], [0, end[1]], color=color, lw=2)
    lo, hi = 0.85*end, 0.55*end
    if j != 0:lo, hi = hi, lo
    ax.annotate('', hi, lo, arrowprops=dict(arrowstyle='->', color=color, lw=2))
    label = 'Common incoming ray' if j == 0 else r'$\Gamma_'+str(j)+'$ outgoing'
    off = 1.13*end
    ax.text(off[0], off[1], label, ha='center', va='center', fontsize=10)
ax.axhline(0, color='0.75', lw=0.7, zorder=0)
ax.axvline(0, color='0.75', lw=0.7, zorder=0)
ax.scatter([0], [0], s=18, color='black', zorder=5)
ax.text(0.1, -0.2, '$0$')
ax.text(0.18, 2.25, r'$\mathrm{Im}\,\zeta$')
ax.text(2.12, 0.1, r'$\mathrm{Re}\,\zeta$')
ax.set_title(r'Decay sectors: $\mathrm{Re}(\zeta^4)<0$', pad=14)
ax.set_aspect('equal');ax.set_xlim(-2.6, 2.75);ax.set_ylim(-2.4, 2.6);ax.axis('off')
fig.tight_layout()
fig.savefig('2011-quartic-contours.png', dpi=160, facecolor='white')
