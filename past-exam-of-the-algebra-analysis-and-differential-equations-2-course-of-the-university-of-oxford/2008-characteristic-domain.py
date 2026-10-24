"""Generate the characteristic-domain sketch. Python 3.14, numpy, matplotlib.

Writes the matching PNG into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 1000)
fig, ax = plt.subplots(figsize=(7.0, 4.8), facecolor='white')
ax.set_facecolor('white')
ax.fill_between(x, -9*x/40, 3, where=x >= 0, color='#b9dbe9')
ax.fill_between(x, -3, -9*x/40, where=x <= 0, color='#b9dbe9')
ax.plot(x, -9*x/40, color='#234c70', linewidth=1.6)
ax.axvline(0, color='#234c70', linewidth=1.6)
ax.axhline(0, color='#555555', linewidth=0.7)
ax.plot([0], [0], 'o', color='#234c70', markersize=3)
ax.text(1.9, 1.7, r'$9x^2+40xy>0$', ha='center', fontsize=12)
ax.text(-1.9, -1.7, r'$9x^2+40xy>0$', ha='center', fontsize=12)
ax.text(1.5, -2.0, 'No real branch', ha='center', fontsize=10, color='#555555')
ax.text(-1.5, 2.0, 'No real branch', ha='center', fontsize=10, color='#555555')
ax.text(2.4, -0.93, r'$y=-9x/40$', ha='center', fontsize=11)
ax.set(xlim=(-4, 4), ylim=(-3, 3), xlabel='$x$', ylabel='$y$')
ax.set_title('Real domain of the characteristic solution')
ax.text(0.5, -0.17, 'Shaded interiors: classical branches. Blue boundary: continuous values.',
        transform=ax.transAxes, ha='center', fontsize=9)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path('2008-characteristic-domain.png'), dpi=160, facecolor='white')
plt.close(fig)
