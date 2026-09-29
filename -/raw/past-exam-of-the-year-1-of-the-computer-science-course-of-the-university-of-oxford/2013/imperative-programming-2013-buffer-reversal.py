"""Draw physical and logical orders for the reversible linked buffer.

Tested with Python 3.14, matplotlib 3.10.7. Writes its PNG to the current
working directory, as required by the repository media build.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9.8, 5.3), dpi=120)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.6)
ax.axis('off')
ax.text(0.1, 6.22, 'Reversal changes the interpretation of the links', fontsize=16, weight='bold')
rows = [
    (4.85, [10, 20, 30], 'backwards = false', 'logical order:  [10, 20, 30]'),
    (3.05, [10, 20, 30], 'rev: backwards = true', 'logical order:  [30, 20, 10]'),
    (1.25, [40, 10, 20, 30], 'append(40), still backwards', 'logical order:  [30, 20, 10, 40]'),
]
for y, values, label, abstract in rows:
    ax.text(0.1, y + .5, label, fontsize=12, weight='bold', color='#264b73')
    xs = [3.0 + i * 1.45 for i in range(len(values))]
    for x, value in zip(xs, values):
        color = '#ffedd0' if value == 40 else '#e4f0fa'
        ax.add_patch(FancyBboxPatch((x-.42, y-.22), .84, .44,
                                  boxstyle='round,pad=.06', facecolor=color,
                                  edgecolor='#264b73', linewidth=1.4))
        ax.text(x, y, str(value), ha='center', va='center', fontsize=12)
    for x1, x2 in zip(xs, xs[1:]):
        ax.annotate('', (x2-.5, y+.095), (x1+.5, y+.095),
                    arrowprops=dict(arrowstyle='->', color='#264b73', linewidth=1.4))
        ax.annotate('', (x1+.5, y-.095), (x2-.5, y-.095),
                    arrowprops=dict(arrowstyle='->', color='#758499', linewidth=1.4))
    ax.text(xs[0]-.7, y, 'first', ha='right', va='center', fontsize=10)
    ax.text(xs[-1]+.7, y, 'last', ha='left', va='center', fontsize=10)
    ax.text(3.0, y-.65, abstract, fontsize=12)
ax.text(.1, .16, 'Upper arrow: next     Lower arrow: prev     Only append creates a new node.',
        fontsize=10, color='#454545')
fig.subplots_adjust(left=.025, right=.985, bottom=.025, top=.99)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
