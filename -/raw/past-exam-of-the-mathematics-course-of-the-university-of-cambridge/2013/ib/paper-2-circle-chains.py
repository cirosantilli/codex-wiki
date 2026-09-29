"""Original circle configurations. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-2-circle-chains.png to the current working directory.
Matplotlib configuration is controlled by the caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.2), dpi=100, facecolor='white')
for ax, n in zip(axes, (2, 5)):
    rho = 1.0
    outer = 3.0 if n == 2 else (1 + np.sin(np.pi/n))/(1 - np.sin(np.pi/n))
    radius, distance = (outer-rho)/2, (outer+rho)/2
    for r in (rho, outer):
        ax.add_patch(Circle((0, 0), r, fill=False, lw=1.7, color='#303030'))
    angles = np.array((-np.pi/6, np.pi/6)) if n == 2 else np.arange(n)*2*np.pi/n + np.pi/2
    centres = distance*np.column_stack((np.cos(angles), np.sin(angles)))
    for j, centre in enumerate(centres):
        ax.add_patch(Circle(centre, radius, facecolor='#c5deee', edgecolor='#225a83', lw=1.7))
        ax.text(*centre, f'$X_{j}$', ha='center', va='center', fontsize=12)
    if n == 5:
        locus = np.sqrt(outer*rho)
        ax.add_patch(Circle((0, 0), locus, fill=False, ls='--', lw=1, color='#bc6540'))
        pts = (centres + np.roll(centres, -1, axis=0))/2
        ax.scatter(pts[:, 0], pts[:, 1], c='#bc6540', s=22, zorder=5)
    ax.text(0, 0, '$A$', ha='center', va='center', fontsize=12)
    ax.text(-0.8*outer, 0.75*outer, '$B$', fontsize=12)
    ax.set_title('Two-circle literal constellation' if n == 2 else 'Five-circle forward chain', fontsize=11)
    ax.set_xlim(-outer*1.1, outer*1.1); ax.set_ylim(-outer*1.1, outer*1.1)
    ax.set_aspect('equal'); ax.axis('off')
fig.subplots_adjust(left=.025, right=.975, top=.9, bottom=.06, wspace=.15)
fig.savefig('paper-2-circle-chains.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
