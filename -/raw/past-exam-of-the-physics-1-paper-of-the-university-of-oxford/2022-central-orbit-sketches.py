"""Original orbit sketches. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(9, 4), dpi=120)
theta = np.linspace(0, 2 * np.pi, 1201)
e = 0.12
radius = 1 / (1 + e * np.cos(theta))
paths = [(radius * np.cos(theta), radius * np.sin(theta)), (1.1 * np.cos(theta), 0.9 * np.sin(theta))]
titles = [r'$k=-1$: inverse-distance potential', r'$k=2$: quadratic potential']
notes = ['Force centre at a focus\n1 radial cycle per revolution', 'Force centre at the ellipse centre\n2 radial cycles per revolution']
for ax, (x, y), title, note in zip(axes, paths, titles, notes):
    ax.axhline(0, color='#cbd5e1', linewidth=0.7)
    ax.axvline(0, color='#cbd5e1', linewidth=0.7)
    ax.plot(x, y, color='#126782', linewidth=2.4)
    ax.scatter([0], [0], marker='+', color='#b93730', s=110, linewidths=2, label='force centre', zorder=5)
    ax.annotate('', xy=(x[230], y[230]), xytext=(x[192], y[192]), arrowprops={'arrowstyle': '->', 'color': '#126782', 'lw': 2})
    ax.set_title(title, pad=14)
    ax.set_aspect('equal')
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(0.5, -0.04, note, ha='center', va='top', transform=ax.transAxes, linespacing=1.5)
axes[0].scatter([1/(1+e), -1/(1-e)], [0, 0], color='#126782', s=30, zorder=5)
axes[1].scatter([1.1, -1.1, 0, 0], [0, 0, 0.9, -0.9], color='#126782', s=30, zorder=5)
fig.subplots_adjust(left=0.03, right=0.97, top=0.86, bottom=0.20, wspace=0.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False, metadata={'Software': 'Matplotlib'})
plt.close(fig)
