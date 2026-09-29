"""Original solution figure; tested with Python 3.14 and root pyproject dependencies.

Write the opaque PNG basename in cwd, including when run from its _media mirror.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5.3, 5.3), dpi=130, facecolor='white')
t = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(t), -2*np.sin(t), color='#31688e', lw=2)
ax.axhline(0, color='0.6', lw=.8)
ax.axvline(0, color='0.6', lw=.8)
for end, color in [((1, 0), '#d55e00'), ((0, -2), '#009e73')]:
    ax.annotate('', end, (0, 0), arrowprops=dict(arrowstyle='->', lw=2.5, color=color))
ax.annotate(r'$\omega t=0:\ (1,0)$', (1, 0), (.45, .6), fontsize=11, color='#d55e00')
ax.annotate(r'$\omega t=\pi/2:\ (0,-2)$', (0, -2), (-1.45, -2.45), fontsize=11, color='#009e73')
for a in [.4, 2.1, 3.7, 5.3]:
    ax.annotate('', (np.cos(a+.2), -2*np.sin(a+.2)), (np.cos(a), -2*np.sin(a)),
                arrowprops=dict(arrowstyle='->', color='#31688e', lw=1.8))
ax.set(xlim=(-1.65, 1.65), ylim=(-2.7, 2.65), xlabel=r'$\Psi_x$', ylabel=r'$\Psi_y$')
ax.set_aspect('equal')
ax.set_title('A = +2i; viewed from +z toward the source', fontsize=11)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
