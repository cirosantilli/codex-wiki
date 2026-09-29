"""Original contours and normalized gradient. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

x = np.linspace(-2, 2, 1101)
y = np.linspace(-2, 2, 1101)
xx, yy = np.meshgrid(x, y)
value = (xx**2+yy**2)/2 + xx**2*yy-yy**3/3
fig, ax = plt.subplots(figsize=(7.8, 7.8), facecolor='white')
levels = [-1., -.4, 0., .05, .10, .30, .60, 1., 2., 3.]
contours = ax.contour(xx, yy, value, levels=levels, cmap='viridis', linewidths=1.25)
ax.clabel(contours, inline=True, fmt=lambda v: f'{v:g}', fontsize=8)
for line in (np.full_like(x, -.5), 1+np.sqrt(3)*x, 1-np.sqrt(3)*x):
    ax.plot(x, line, color='#ba4138', linestyle='--', linewidth=1.8)
q = np.linspace(-1.85, 1.85, 17)
qx, qy = np.meshgrid(q, q)
gx, gy = qx*(1+2*qy), qy+qx**2-qy**2
norm = np.hypot(gx, gy)
mask = norm > .12
ax.quiver(qx[mask], qy[mask], gx[mask]/norm[mask], gy[mask]/norm[mask],
          color='#555555', angles='xy', scale_units='xy', scale=10.5,
          width=.0025, alpha=.76, pivot='mid', zorder=3)
points = [(0, 0), (0, 1), (np.sqrt(3)/2, -.5), (-np.sqrt(3)/2, -.5)]
for i, (px, py) in enumerate(points):
    ax.plot(px, py, 'o', color='#141414', markersize=5, zorder=6)
    if i == 0:
        ax.annotate('minimum (0, 0)', (px, py), xytext=(15, -35), textcoords='offset points',
                    fontsize=10, bbox=dict(facecolor='white', alpha=.9, edgecolor='none'),
                    arrowprops=dict(arrowstyle='-', color='#222222'))
    elif i == 1:
        ax.annotate('saddle (0, 1)', (px, py), xytext=(12, 12), textcoords='offset points', fontsize=10,
                    bbox=dict(facecolor='white', alpha=.9, edgecolor='none'))
    else:
        label = r'$(\sqrt{3}/2,-1/2)$' if px > 0 else r'$(-\sqrt{3}/2,-1/2)$'
        ax.annotate(label, (px, py), xytext=(9 if px > 0 else -105, -30), textcoords='offset points',
                    fontsize=10, bbox=dict(facecolor='white', alpha=.9, edgecolor='none'))
ax.set(xlim=(-2, 2), ylim=(-2, 2), xlabel='$x$', ylabel='$y$', aspect='equal')
ax.set_xticks(np.arange(-2, 2.1, .5))
ax.set_yticks(np.arange(-2, 2.1, .5))
ax.set_title(r'$f=\frac{1}{2}(x^2+y^2)+x^2y-\frac{1}{3}y^3$', fontsize=16, pad=13)
ax.grid(alpha=.12)
ax.legend(handles=[Line2D([0], [0], color='#ba4138', linestyle='--', label='$f=1/6$'),
                   Line2D([0], [0], marker=r'$\rightarrow$', color='#555555', linestyle='none',
                          markersize=18, label='direction of gradient')], loc='lower center',
          bbox_to_anchor=(.5, -.16), ncol=2, frameon=False)
fig.subplots_adjust(left=.10, right=.97, bottom=.17, top=.91)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=155, facecolor='white')
plt.close(fig)
