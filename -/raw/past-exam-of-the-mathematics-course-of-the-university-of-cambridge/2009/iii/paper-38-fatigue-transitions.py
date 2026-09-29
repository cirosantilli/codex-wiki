"""Draw the fitted fatigue CTMC. Python 3.14; root numpy/matplotlib versions.

Run from the desired output directory with MPLCONFIGDIR supplied by the caller.
Only the PNG basename is written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(8.4, 3.0), dpi=150, facecolor='white')
ax.set_facecolor('white')
for x, label in zip([0, 3, 6], ['1\nMild', '2\nModerate', '3\nSevere']):
    ax.add_patch(FancyBboxPatch((x-.68, -.45), 1.36, .90,
                              boxstyle='round,pad=0.03',
                              facecolor='#edf4fb', edgecolor='#234d75', linewidth=1.5))
    ax.text(x, 0, label, ha='center', va='center', fontsize=13)
for left, right, forward, backward in [(0, 3, .173, .4684), (3, 6, .3835, .3655)]:
    for start, end, y, value, label_y in [
        (left+.75, right-.75, .22, forward, .52),
        (right-.75, left+.75, -.22, backward, -.57),
    ]:
        ax.add_patch(FancyArrowPatch((start, y), (end, y), arrowstyle='-|>',
                                    mutation_scale=15, linewidth=1.7, color='#234d75'))
        ax.text((left+right)/2, label_y, f'{value:g}', ha='center', va='center', fontsize=12)
ax.text(3, 1.08, 'Fitted fatigue transition rates (per year)', ha='center', fontsize=14)
ax.text(3, -.99, 'No direct jumps between mild and severe states', ha='center', fontsize=10)
ax.set_xlim(-.95, 6.95)
ax.set_ylim(-1.25, 1.35)
ax.axis('off')
fig.subplots_adjust(left=.025, right=.975, bottom=.07, top=.95)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
