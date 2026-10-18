"""Generate mathematics-iii-cardioid.png in CWD; Python 3.14, NumPy/Matplotlib per pyproject.toml."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.0, 5.8), layout='constrained', facecolor='white')
right = np.linspace(-np.pi / 2, np.pi / 2, 600)
upper = np.linspace(np.pi / 2, np.pi, 400)
lower = np.linspace(np.pi, 3 * np.pi / 2, 400)

def region(theta, colour):
    r = 1 + np.cos(theta)
    outer = np.column_stack((r * np.cos(theta), r * np.sin(theta)))
    inner = np.column_stack((np.cos(theta[::-1]), np.sin(theta[::-1])))
    ax.fill(*np.vstack((outer, inner)).T, color=colour, alpha=0.65, linewidth=0)

region(right, '#8ac6e8')
region(upper, '#f1c172')
region(lower, '#b5d89a')
theta = np.linspace(0, 2 * np.pi, 1601)
r = 1 + np.cos(theta)
ax.plot(r * np.cos(theta), r * np.sin(theta), color='#165a8b', lw=2.2,
        label=r'Cardioid $r=1+\cos\theta$')
ax.plot(np.cos(theta), np.sin(theta), color='#333333', lw=1.6, ls='--',
        label=r'Unit circle $r=1$')
ax.scatter([0, 0, 0, 2], [0, 1, -1, 0], s=22, color='#333333', zorder=5)
ax.annotate('cusp', (0, 0), (-0.43, -0.14), fontsize=10,
            arrowprops={'arrowstyle': '->', 'lw': 0.8})
ax.text(1.18, 0.10, r'$A_R=2+\pi/4$', ha='center', fontsize=12)
ax.text(-0.56, 0.48, r'$A_U$', ha='center', fontsize=13)
ax.text(-0.56, -0.48, r'$A_L$', ha='center', fontsize=13)
ax.axhline(0, color='#999999', lw=0.6, zorder=0)
ax.axvline(0, color='#999999', lw=0.6, zorder=0)
ax.set(xlim=(-1.2, 2.2), ylim=(-1.5, 1.5), xlabel='$x$', ylabel='$y$',
       title='Cardioid and the three regions between the curves', aspect='equal')
ax.legend(loc='upper left', framealpha=1, fontsize=9)
ax.spines[['top', 'right']].set_visible(False)
fig.savefig(Path.cwd() / 'mathematics-iii-cardioid.png', dpi=140, facecolor='white')
