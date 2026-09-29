"""Generate paper-1-q16-contours.png. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (repository pyproject.toml)."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2025-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.2, 4.2, 501)
y = np.linspace(-4.2, 2.2, 501)
X, Y = np.meshgrid(x, y)
U, V = X-1, Y+1
F = U*V*np.exp(-(U*U+V*V)/2)
fig, ax = plt.subplots(figsize=(7.1, 6.6), layout='constrained', facecolor='white')
neg = ax.contour(X, Y, F, levels=[-0.32, -0.22, -0.12, -0.04], colors='#b3472d', linewidths=1.2, linestyles='dashed')
pos = ax.contour(X, Y, F, levels=[0.04, 0.12, 0.22, 0.32], colors='#17679a', linewidths=1.2)
ax.clabel(neg, inline=True, fontsize=8, fmt='%g')
ax.clabel(pos, inline=True, fontsize=8, fmt='%g')
ax.axvline(1, color='gray', linewidth=1)
ax.axhline(-1, color='gray', linewidth=1)
# Equal-length arrows show direction, including on the saddle's axes and diagonals.
points = []
for cx, cy in [(2, 0), (0, -2), (2, -2), (0, 0), (1, -1)]:
    for angle in np.arange(8)*np.pi/4:
        points.append((cx+0.31*np.cos(angle), cy+0.31*np.sin(angle)))
px, py = np.array(points).T
pu, pv = px-1, py+1
gradx, grady = pv*(1-pu*pu), pu*(1-pv*pv)
length = np.hypot(gradx, grady)
ax.quiver(px, py, gradx/length, grady/length, angles='xy', scale_units='xy', scale=5.5,
          color='#222222', width=0.0035, pivot='mid', zorder=4)
for cx, cy, label, color in [(2, 0, 'maximum', '#17679a'), (0, -2, 'maximum', '#17679a'),
                            (2, -2, 'minimum', '#b3472d'), (0, 0, 'minimum', '#b3472d'),
                            (1, -1, 'saddle', '#222222')]:
    ax.plot(cx, cy, 'o', color=color, markersize=5, zorder=5)
    ax.annotate(label, (cx, cy), xytext=(0, 32), textcoords='offset points', ha='center',
                fontsize=9, color=color, bbox=dict(facecolor='white', alpha=0.85, edgecolor='none', pad=1))
ax.set(xlim=(-2.2, 4.2), ylim=(-4.2, 2.2), xlabel='$x$', ylabel='$y$',
       title='Question 16: contours and gradient directions')
ax.set_aspect('equal')
ax.grid(alpha=0.12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white')
plt.close(fig)
