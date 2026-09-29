"""Planar vector field and Hamiltonian separatrices; output to caller CWD only."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(10.5, 4), dpi=130, facecolor='white')
x = np.linspace(-1.9, 1.9, 200)
y = np.linspace(-1.7, 1.7, 200)
X, Y = np.meshgrid(x, y)
for ax, a in zip(axs, [1., 2.6, 0.]):
    vx, vy = -a*X-2*X*Y, X**2+Y**2-1
    length = np.hypot(vx, vy)
    vx, vy = vx/(1+length), vy/(1+length)
    ax.streamplot(x, y, vx, vy, density=.75, color='#9ab5c5', linewidth=.7, arrowsize=.8)
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), ':', color='.45', lw=1)
    ax.axvline(0, color='.35', lw=1)
    ax.axhline(-a/2, ls=':', color='.45', lw=1)
    ax.scatter([0], [1], marker='x', color='#a52d32', s=50, zorder=5)
    if a < 2:
        ax.scatter([0], [-1], marker='x', color='#a52d32', s=50, zorder=5)
        q = np.sqrt(1-a*a/4)
        ax.scatter([-q, q], [-a/2, -a/2], color='#1a754b', facecolors='none' if a==0 else '#1a754b', s=50, zorder=5)
    else:
        ax.scatter([0], [-1], color='#1a754b', s=50, zorder=5)
    if a == 0:
        H = X**3/3 + X*Y**2 - X
        ax.contour(X, Y, H, levels=[-.6, -.4, -.2, .2, .4, .6], colors='#287647', linewidths=.85)
        ax.plot(np.sqrt(3)*np.cos(theta), np.sin(theta), color='#a52d32', lw=1.3)
        ax.plot([0, 0], [-1, 1], color='#a52d32', lw=1.3)
    ax.set(xlim=(-1.9, 1.9), ylim=(-1.7, 1.7), xlabel='x', ylabel='y', title=f'b = 1, a = {a:g}')
    ax.set_aspect('equal')
fig.suptitle('Planar pitchfork: two sinks, one sink, and the Hamiltonian limit', fontsize=12)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-3-pitchfork-portraits.png', facecolor='white', transparent=False)
