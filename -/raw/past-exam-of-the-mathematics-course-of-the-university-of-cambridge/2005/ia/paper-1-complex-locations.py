"""Original complex-plane diagram. Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.

Writes paper-1-complex-locations.png to the caller's current working directory.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

angle = np.linspace(0, 2 * np.pi, 500)
fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=120, facecolor='white')
ax.fill(1 + np.cos(angle), np.sin(angle), color='#eef3f9', zorder=1)
ax.plot(1 + np.cos(angle), np.sin(angle), color='#465c78', linewidth=1.6,
        label=r'Allowed disk: $|z-1|\leq1$', zorder=2)
food_x = 1 / np.sqrt(2)
food_y = np.array([1, -1]) / np.sqrt(2)
ax.scatter([food_x, food_x], food_y, color='#067c74', marker='*', s=160,
           label='Food', zorder=4)
ax.scatter([2], [0], color='#c26016', s=60, label='Drink', zorder=4)
ax.scatter([0], [0], facecolors='white', edgecolors='#555555', s=50, zorder=4)
ax.annotate(r'$e^{i\pi/4}$', (food_x, food_y[0]), xytext=(12, 9),
            textcoords='offset points', fontsize=12)
ax.annotate(r'$e^{-i\pi/4}$', (food_x, food_y[1]), xytext=(12, -15),
            textcoords='offset points', fontsize=12)
ax.annotate(r'$z=2$', (2, 0), xytext=(8, 10), textcoords='offset points', fontsize=12)
ax.annotate('0: equations undefined', (0, 0), xytext=(-8, -25),
            textcoords='offset points', ha='left', fontsize=9, color='#555555')
ax.axhline(0, color='#b7bdc5', linewidth=.7, zorder=0)
ax.axvline(0, color='#b7bdc5', linewidth=.7, zorder=0)
ax.set(xlim=(-.3, 2.45), ylim=(-1.25, 1.25), xlabel=r'$\operatorname{Re}z$',
       ylabel=r'$\operatorname{Im}z$', title='Food and drink in the complex plane')
ax.set_aspect('equal', adjustable='box')
ax.set_xticks([0, .5, 1, 1.5, 2]); ax.set_yticks([-1, -.5, 0, .5, 1])
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper right', fontsize=9, framealpha=1)
fig.tight_layout()
fig.savefig('paper-1-complex-locations.png', facecolor='white', transparent=False)
plt.close(fig)
