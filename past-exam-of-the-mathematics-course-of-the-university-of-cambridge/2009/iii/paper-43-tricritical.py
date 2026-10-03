"""Sextic Landau phase diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-43-tricritical.png to the caller's current directory.
MPLCONFIGDIR is deliberately left under the caller's control.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

fig = plt.figure(figsize=(12, 5.5), facecolor='white', layout='constrained')
ax = fig.add_subplot(121, projection='3d')
s, t = np.meshgrid(np.linspace(0, 1.23, 45), np.linspace(0, 0.5, 30))
p = t * (1-t) * s**2
u = (2/3) * (-2*s**2 + 3*p)
r = (s**4 - s**2*p + 3*p**2) / 3
h = s**3 * p / 3
for sign, color in [(1, '#df9e38'), (-1, '#71a9d5')]:
    ax.plot_surface(u, r, sign*h, color=color, alpha=0.7, linewidth=0, antialiased=True)
    ax.plot(u[-1], r[-1], sign*h[-1], color='#254c32', linewidth=2.3)
ug, frac = np.meshgrid(np.linspace(-2, 1.1, 45), np.linspace(0, 1, 22))
coex = np.where(ug < 0, 3*ug**2/16, 0)
rg = -0.35 + frac * (coex + 0.35)
ax.plot_surface(ug, rg, np.zeros_like(rg), color='#ababab', alpha=0.32, linewidth=0)
uneg = np.linspace(-2, 0, 150)
ax.plot(uneg, 3*uneg**2/16, 0*uneg, color='#a93e35', linewidth=2.8)
uplus = np.linspace(0, 1.1, 80)
ax.plot(uplus, 0*uplus, 0*uplus, color='#254c32', linewidth=2.8)
ax.scatter([0], [0], [0], color='black', s=38, depthshade=False)
ax.set(xlabel='Quartic coefficient u', ylabel='Quadratic coefficient r', zlabel='Field h',
       title='Three control parameters (v = 1)', xlim=(-2.1, 1.2), ylim=(-0.36, 0.82), zlim=(-0.27, 0.27))
ax.view_init(elev=23, azim=-54)
ax.set_box_aspect((1.15, 1, 0.9))
ax.legend(handles=[Patch(facecolor='#df9e38', label='First-order wings'),
                   Patch(facecolor='#ababab', alpha=.5, label='Opposite-sign coexistence'),
                   Line2D([], [], color='#254c32', lw=2, label='Continuous critical edges'),
                   Line2D([], [], color='black', marker='o', linestyle='', label='Tricritical point')],
          loc='upper left', fontsize=8)
ax2 = fig.add_subplot(122)
ux = np.linspace(-2, 1.1, 301)
bound = np.where(ux < 0, 3*ux**2/16, 0)
ax2.fill_between(ux, -.35, bound, color='#e7eff5')
ax2.fill_between(ux, bound, .82, color='#fff2da')
ax2.plot(uneg, 3*uneg**2/16, color='#a93e35', lw=2.6, label='First order: r = 3u²/16')
ax2.plot(uplus, 0*uplus, color='#254c32', lw=2.6, label='Continuous: r = 0')
ax2.scatter([0], [0], color='black', s=40, zorder=5)
ax2.annotate('Tricritical point', (0, 0), (.12, .13), arrowprops={'arrowstyle':'->'}, fontsize=10)
ax2.text(-1.65, .68, 'Disordered: M = 0', fontsize=10)
ax2.text(-1.62, -.19, 'Ordered: two minima ±M', fontsize=10)
ax2.set(xlabel='Quartic coefficient u', ylabel='Quadratic coefficient r', title='Zero-field slice h = 0',
        xlim=(-2.05, 1.15), ylim=(-.35, .82))
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(alpha=.2)
fig.savefig('paper-43-tricritical.png', dpi=130, facecolor='white', transparent=False)
plt.close(fig)
