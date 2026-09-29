"""Original regularized vortex-filament calculation, Python 3.14.
Uses NumPy/Matplotlib from pyproject.toml; writes PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.0, 3.0, 121)
z = np.linspace(-6.0, 6.0, 241)
X, Z = np.meshgrid(x, z)
ux = np.zeros_like(X)
uz = np.zeros_like(X)
phi = (np.arange(64) + 0.5) * (2 * np.pi / 64)
co, si = np.cos(phi), np.sin(phi)
for centre in np.linspace(-4, 4, 81):
    dz = Z[..., None] - centre
    denom = ((X[..., None] - co)**2 + si**2 + dz**2 + 0.035**2)**1.5
    ux += np.mean(co * dz / denom, axis=-1) / 2
    uz += np.mean((1 - X[..., None] * co) / denom, axis=-1) / 2
fig, ax = plt.subplots(figsize=(5.6, 7), facecolor='white', layout='constrained')
speed = np.hypot(ux, uz)
ax.streamplot(x, z, ux, uz, density=1.7, color='#216b8c', linewidth=0.6 + 0.8 * np.minimum(speed / 10, 1), arrowsize=0.8)
for side in [-1, 1]:
    ax.plot([side, side], [-4, 4], color='0.45', lw=1, ls='--')
    ax.scatter(np.full(11, side), np.linspace(-4, 4, 11), marker='o', s=10, color='0.35', zorder=4)
ax.text(0, 0, 'Strong axial flow', ha='center', rotation=90, bbox=dict(facecolor='white', edgecolor='none', alpha=.85))
ax.set(xlabel='Transverse coordinate $x/r$', ylabel='Axial coordinate $z/r$', title='Co-oriented vortex rings: meridional flow', xlim=(-3, 3), ylim=(-6, 6), aspect='equal')
ax.spines[['top', 'right']].set_visible(False)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
