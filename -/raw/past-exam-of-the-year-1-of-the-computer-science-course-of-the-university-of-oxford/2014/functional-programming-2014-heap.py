"""Draw the best-case maximum deletion example; writes PNG to the cwd.
Tested environment is recorded by the paper's private figure checks.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BEFORE = [15, 14, 13, 9, 8, 12, 11, 1, 2, 3, 4, 5, 6, 7, 10]
AFTER = [14, 10, 13, 9, 8, 12, 11, 1, 2, 3, 4, 5, 6, 7]

def draw(ax, values, title, changed):
    positions = {}
    for i, value in enumerate(values):
        level = (i + 1).bit_length() - 1
        first = 2**level - 1
        x = (i - first + 0.5) / 2**level
        positions[i] = (x, 3 - level)
    for i in range(1, len(values)):
        px, py = positions[(i - 1) // 2]
        x, y = positions[i]
        ax.plot([px, x], [py, y], color='#718096', lw=1.4, zorder=1)
    for i, value in enumerate(values):
        x, y = positions[i]
        face = '#fff0be' if value in changed else '#e7f1fa'
        ax.scatter([x], [y], s=530, c=face, edgecolors='#233c55',
                   linewidths=1.2, zorder=3)
        ax.text(x, y, str(value), ha='center', va='center', fontsize=12,
                color='#102a43', zorder=4)
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.45, 3.55)
    ax.set_title(title, fontsize=13, pad=7)
    ax.axis('off')

fig, axes = plt.subplots(2, 1, figsize=(9.2, 7.2), facecolor='white')
draw(axes[0], BEFORE, 'Before: exchange 15 with 10, then exchange 10 with 14', {15, 14, 10})
draw(axes[1], AFTER, 'After: 10 stops above 9 and 8; two pairwise exchanges in total', {14, 10})
fig.subplots_adjust(left=0.035, right=0.965, top=0.94, bottom=0.035, hspace=0.24)
fig.savefig(Path.cwd() / 'functional-programming-2014-heap.png', dpi=120,
            facecolor='white', metadata={'Software': 'codex-wiki matplotlib'})
plt.close(fig)
