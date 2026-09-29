"""Matter-only curvature examples. Python 3.14.4, root pinned NumPy/Matplotlib.

Writes its opaque 720x360 PNG to the current working directory. Main's Make
workflow renders directly into the mirrored _media publication directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

eta_closed = np.linspace(0, 2*np.pi, 700)
closed_t = (eta_closed-np.sin(eta_closed))/2
closed_a = (1-np.cos(eta_closed))/2
eta_open = np.linspace(0, 3.4, 700)
open_t = (np.sinh(eta_open)-eta_open)/2
open_a = (np.cosh(eta_open)-1)/2
flat_t = np.linspace(0, 3.4, 700)
flat_a = (1.5*flat_t)**(2/3)

fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.plot(open_t, open_a, color='#007d60', lw=2.3, label='Open: K = -1')
ax.plot(flat_t, flat_a, color='#1764a1', lw=2.3, label='Flat: K = 0')
ax.plot(closed_t, closed_a, color='#9a3c79', lw=2.3, label='Closed: K = +1')
ax.scatter([np.pi/2, np.pi], [1, 0], color='#9a3c79', s=20, zorder=4)
ax.annotate('Maximum size', xy=(np.pi/2, 1), xytext=(1.65, .35),
            ha='center', fontsize=9, arrowprops={'arrowstyle':'->','color':'#555555'})
ax.annotate('Big Crunch', xy=(np.pi, 0), xytext=(2.75, 1.35),
            ha='center', fontsize=9, arrowprops={'arrowstyle':'->','color':'#555555'})
ax.set(xlim=(0, 3.4), ylim=(0, 4.6), xlabel='Dimensionless cosmic time t',
       ylabel='Scale factor a', title=r'Matter-only examples: $\dot a^2=1/a-K$')
ax.grid(alpha=.18)
ax.legend(loc='upper left', frameon=True, facecolor='white', framealpha=1,
          fontsize=9)
fig.tight_layout(pad=1)
fig.savefig(Path.cwd()/'paper-310-matter-expansion.png', dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
