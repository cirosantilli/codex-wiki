"""An original support-relation timeline of the derived three-action plan.
Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. Output goes to CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

blocks = ('A', 'B', 'C')
support = {'A': 'table', 'B': 'table', 'C': 'A'}
states = [support.copy()]
steps = [('C', 'table'), ('B', 'C'), ('A', 'B')]
for block, destination in steps:
    assert block not in support.values()
    assert destination == 'table' or destination not in support.values()
    assert block != destination
    support = support | {block: destination}
    states.append(support.copy())
assert support == {'A': 'B', 'B': 'C', 'C': 'table'}
colors = {'table': '#edf0f2', 'A': '#fae1bb', 'B': '#c6e4f2', 'C': '#ded6ec'}
fig, ax = plt.subplots(figsize=(8.6, 3.5), dpi=110, facecolor='white')
for col, state in enumerate(states):
    for row, block in enumerate(blocks):
        y = 2-row
        target = state[block]
        ax.add_patch(Rectangle((col, y), .9, .8, facecolor=colors[target], edgecolor='white', lw=2))
        ax.text(col+.45, y+.4, target, ha='center', va='center', fontsize=13)
        if (block == 'A' and target == 'B') or (block == 'B' and target == 'C'):
            ax.add_patch(Rectangle((col+.025, y+.025), .85, .75, fill=False, edgecolor='#1f7346', lw=2))
for row, block in enumerate(blocks):
    ax.text(-.15, 2-row+.4, block, ha='right', va='center', fontsize=13, fontweight='bold')
for col, title in enumerate(['Initial', 'After step 1', 'After step 2', 'After step 3']):
    ax.text(col+.45, 2.97, title, ha='center', fontsize=11)
for col, title in enumerate(['C to table', 'B onto C', 'A onto B'], start=1):
    ax.annotate('', xy=(col+.25, -.16), xytext=(col-.35, -.16), arrowprops={'arrowstyle':'->','color':'#52616a','lw':1.4})
    ax.text(col-.05, -.43, title, ha='center', fontsize=10)
ax.text(-.15, 3.38, 'Block', fontsize=10, ha='right')
ax.text(1.95, 3.38, 'Cell entry = the block’s current support', fontsize=12, ha='center')
ax.text(1.9, -.88, r'Prepare first; $G_2$ holds after step 2, then $G_1$ after step 3.', fontsize=11, ha='center')
ax.set_xlim(-.45,4.05);ax.set_ylim(-1.05,3.6);ax.axis('off')
fig.subplots_adjust(left=.04,right=.98,bottom=.04,top=.95)
fig.savefig('artificial-intelligence-plan-supports.png', facecolor='white', transparent=False)
