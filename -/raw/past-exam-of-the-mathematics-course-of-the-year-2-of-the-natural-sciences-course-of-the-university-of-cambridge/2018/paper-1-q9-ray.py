"""Generate the original optical-ray plot; output goes to cwd.

Tested with Python 3.14; dependencies are in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 4), layout='constrained')
x1 = np.linspace(-7, 0, 350)
x2 = np.linspace(0, 7, 350)
ax.plot(x1, 6-1.5*(1-x1)**(2/3), color='#2465a6', linewidth=2.2)
ax.plot(x2, 2.5+2*np.sqrt(1+x2), color='#b85522', linewidth=2.2)
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
ax.scatter([-7, 0, 7], [0, 4.5, 2.5+4*np.sqrt(2)], color='black', s=22, zorder=3)
ax.annotate('source: (−7, 0)', (-7, 0), xytext=(7, 10), textcoords='offset points')
ax.annotate('interface: (0, 9/2)', (0, 4.5), xytext=(-95, 18), textcoords='offset points')
ax.annotate(r'receiver: $(7,\ 5/2+4\sqrt{2})$', (7, 2.5+4*np.sqrt(2)), xytext=(-160, -25), textcoords='offset points')
ax.set(xlim=(-7.6, 7.6), ylim=(-.5, 9), xlabel='$x$', ylabel='$y$', title='Least-time ray between its fixed endpoints')
ax.set_aspect('equal', adjustable='box')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=170, facecolor='white')
