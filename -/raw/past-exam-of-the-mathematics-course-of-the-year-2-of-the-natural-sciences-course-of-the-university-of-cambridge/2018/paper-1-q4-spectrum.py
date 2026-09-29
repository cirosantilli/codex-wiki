"""Generate the original spectrum plot. Run from the mirrored _media directory.

Tested with Python 3.14; dependencies are in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 3.4), layout='constrained')
ax.plot([-3, -2, -2, -1, -1, 1, 1, 2, 2, 3], [0, 0, 1, 1, 4, 4, 1, 1, 0, 0], color='#2465a6', linewidth=2.2)
ax.fill_between([-2, -1, -1, 1, 1, 2], [1, 1, 4, 4, 1, 1], alpha=.14, color='#2465a6')
ax.set(xlim=(-3, 3), ylim=(-.2, 4.5), xticks=[-2, -1, 0, 1, 2], yticks=[0, 1, 4], xlabel=r'$\omega$', ylabel=r'$|\widetilde z(\omega)|^2$', title='Squared magnitude of the Fourier transform')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=170, facecolor='white')
