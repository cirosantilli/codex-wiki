"""Original characteristic-domain diagram. Python 3.14; numpy 2.3.5,
matplotlib 3.10.7. Writes 2012-characteristics.png to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.2, 5.2), facecolor='white')
x = np.linspace(-1, 2.4, 600)
ax.fill_between(x, -x-1, x*x+x, color='#e1eef8', label='Data determine the solution')
ax.plot(x, -x-1, '--', color='#b23b38', lw=1.8, label=r'Fold: $y=-x-1$ (excluded)')
ax.plot(x, x*x+x, color='#82559a', lw=1.9, label=r'Endpoint characteristic: $y=x^2+x$')
for t in [0.3, 0.7, 1.2, 1.8, 2.6]:
    s = np.linspace(-0.985, 2.6-t, 400)
    cx, cy = t+s, -t+s+s*s
    ax.plot(cx, cy, color='#1965a0', lw=1.1)
    mid = min(0.1, 2.2-t)
    s1, s2 = mid-0.07, mid+0.07
    ax.annotate('', (t+s2, -t+s2+s2*s2), (t+s1, -t+s1+s1*s1), arrowprops=dict(arrowstyle='->', color='#1965a0', lw=1.1))
    ax.scatter([t-1], [-t], facecolors='white', edgecolors='#b23b38', s=22, zorder=5)
xx = np.linspace(0, 2.4, 100)
ax.plot(xx, -xx, color='#262626', lw=2.5, label=r'Initial data: $y=-x,\ x\geq0$')
ax.scatter([0], [0], color='#262626', s=28, zorder=5)
ax.axhline(0, color='0.7', lw=0.7, zorder=0)
ax.axvline(0, color='0.7', lw=0.7, zorder=0)
ax.set_xlim(-1.2, 2.4)
ax.set_ylim(-3.6, 4.4)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$', rotation=0, labelpad=12)
ax.set_title('Characteristic branch through the prescribed half-line')
ax.legend(loc='upper left', fontsize=9, framealpha=1)
ax.grid(alpha=0.16)
fig.tight_layout()
fig.savefig('2012-characteristics.png', dpi=160, facecolor='white')
