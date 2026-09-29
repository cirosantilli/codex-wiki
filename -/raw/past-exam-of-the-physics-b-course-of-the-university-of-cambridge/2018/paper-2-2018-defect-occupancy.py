"""Original occupation plots. Python 3.14; NumPy/Matplotlib from pyproject.toml.

Run from the mirrored _media directory; writes the PNG basename to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(10, 3.5), sharey=True, facecolor='white', layout='constrained')
settings = [
    ('Repulsion: $U>0$', [0, 1], ['$\\epsilon$', '$\\epsilon+U$']),
    ('No interaction: $U=0$', [0.5], ['$\\epsilon$']),
    ('Attraction: $U<0$', [0.5], ['$\\epsilon+U/2$']),
]
for ax, (title, thresholds, labels) in zip(axes, settings):
    edges = [-0.8, *thresholds, 1.8]
    heights = [0, 1, 2] if len(thresholds) == 2 else [0, 2]
    for left, right, value in zip(edges[:-1], edges[1:], heights):
        ax.plot([left, right], [value, value], color='#17658a', lw=2.6)
    for index, x in enumerate(thresholds):
        ax.axvline(x, color='0.72', lw=0.8, zorder=0)
        ax.plot([x, x], heights[index:index + 2], color='#17658a', lw=1.2, ls='--')
        ax.scatter([x, x], heights[index:index + 2], facecolors='white', edgecolors='#17658a', zorder=4, s=24)
    ax.set(title=title, xticks=thresholds, xticklabels=labels, xlim=(-0.8, 1.8), ylim=(-0.2, 2.3), yticks=[0, 1, 2])
    ax.set_xlabel('Chemical potential $\\mu$')
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_facecolor('white')
axes[0].set_ylabel('Minimizing occupation $N$')
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
