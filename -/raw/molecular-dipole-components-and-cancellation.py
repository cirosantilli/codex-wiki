"""Compare exact charge moments with bond-vector sums for a toy AB2 model.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is an opaque white PNG in the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

BLUE, ORANGE, RED = '#2468a0', '#bb6425', '#b53848'
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(2, 2, figsize=(10, 7.4), dpi=120)
fig.patch.set_facecolor('white')
for col, angle in enumerate((180, 120)):
    half = np.deg2rad(angle/2)
    positions = np.array([[-np.sin(half), np.cos(half)], [np.sin(half), np.cos(half)]])
    dipoles = -positions
    ax = axes[0, col]
    ax.set(xlim=(-1.5, 1.5), ylim=(-0.7, 1.12), aspect='equal')
    ax.axis('off')
    ax.set_title(f'{angle}°: '+('linear and symmetric' if col == 0 else 'bent, equal bond moments'),
                 fontsize=14, pad=12, weight='bold')
    for pos in positions:
        ax.plot([0, pos[0]], [0, pos[1]], color='#bbbbbb', lw=3, zorder=0)
        # Arrows start at negative terminals and point toward the positive centre.
        ax.annotate('', xy=0.16*pos, xytext=0.78*pos,
                    arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2.8})
        ax.add_patch(Circle(pos, 0.12, facecolor='white', edgecolor=BLUE, lw=2))
        ax.text(*pos, 'B', ha='center', va='center', weight='bold')
        ax.text(pos[0], pos[1]+0.21, r'$-q$', ha='center', color=BLUE, fontsize=14)
    ax.add_patch(Circle((0, 0), 0.13, facecolor='white', edgecolor=ORANGE, lw=2))
    ax.text(0, 0, 'A', ha='center', va='center', weight='bold')
    ax.text(0, -0.29, r'$+2q$', ha='center', color=ORANGE, fontsize=14)
    if col:
        ax.add_patch(Arc((0, 0), 0.65, 0.65, theta1=30, theta2=150, color='#666666', lw=1.2))
        ax.text(0, 0.44, r'$\theta$', ha='center', color='#555555', fontsize=14)
    ax.text(0, -0.59, r'Total charge $=0$; each bond magnitude $p_0=qr$', ha='center', fontsize=11)
    ax = axes[1, col]
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.37, 0.42), aspect='equal')
    ax.axis('off')
    ax.text(0, 0.25, 'Vectors translated to a common origin', ha='center', fontsize=12)
    ax.scatter([0], [0], s=18, color='#333333', zorder=4)
    for k, vector in enumerate(dipoles):
        ax.annotate('', xy=vector, xytext=(0, 0),
                    arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2.6})
        x, y = vector
        ax.text(x*1.12, y-0.10, rf'$\mathbf{{p}}_{k+1}$', ha='center', fontsize=14, color=BLUE)
        if col:
            ax.plot([0, x], [y, y], color='#777777', ls='--', lw=1.2)
            ax.plot([x, x], [0, y], color='#777777', ls='--', lw=1.2)
    if col:
        total = dipoles.sum(axis=0)
        ax.annotate('', xy=total, xytext=(0, 0),
                    arrowprops={'arrowstyle': '->', 'color': RED, 'lw': 3})
        ax.text(0.14, -0.93, r'$\mathbf{p}_{\rm mol}$', color=RED, fontsize=14)
        ax.text(0, -1.28, r'$|\mathbf{p}_{\rm mol}|=2p_0\cos 60^\circ=p_0$', ha='center', fontsize=14)
    else:
        ax.text(0, -0.58, r'$\mathbf{p}_1+\mathbf{p}_2=\mathbf{0}$', ha='center', fontsize=16, color=RED)
        ax.text(0, -1.0, 'Equal and opposite: complete cancellation', ha='center', fontsize=12)
fig.suptitle('Molecular dipoles: components cancel or add', fontsize=17, weight='bold', y=0.975)
fig.text(0.5, 0.027, 'All arrows use the physical convention: negative → positive.\n'
         'Original three-site model; 120° is stipulated, not the water bond angle.',
         ha='center', fontsize=11, linespacing=1.6)
fig.subplots_adjust(left=0.05, right=0.97, top=0.86, bottom=0.12, hspace=0.2, wspace=0.17)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), facecolor='white')
plt.close(fig)
