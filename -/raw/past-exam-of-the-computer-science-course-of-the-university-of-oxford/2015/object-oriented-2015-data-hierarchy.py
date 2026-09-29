"""Render the Q1 class hierarchy into the current working directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10.5, 6.4), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
boxes = {
    'Data': (.50, .88, '«interface»\nData', False),
    'AbstractData': (.50, .64, 'AbstractData\nalignment', True),
    'StringData': (.20, .39, 'StringData\ntext', False),
    'NumericData': (.68, .39, 'NumericData\nminimum digits', True),
    'IntegerData': (.48, .13, 'IntegerData\ninteger value', False),
    'RealData': (.85, .13, 'RealData\nreal value; places', False),
}
w, h = .245, .14
for name, (x, y, label, abstract) in boxes.items():
    ax.add_patch(Rectangle((x-w/2, y-h/2), w, h,
                          facecolor='#f4f7fa', edgecolor='#26374a', linewidth=1.4))
    ax.text(x, y, label, ha='center', va='center', fontsize=12,
            fontstyle='italic' if abstract else 'normal', color='#172d43', linespacing=1.5)
for child, parent, realization in [
    ('AbstractData', 'Data', True),
    ('StringData', 'AbstractData', False),
    ('NumericData', 'AbstractData', False),
    ('IntegerData', 'NumericData', False),
    ('RealData', 'NumericData', False),
]:
    cx, cy, _, _ = boxes[child]
    px, py, _, _ = boxes[parent]
    ax.add_patch(FancyArrowPatch((cx, cy+h/2), (px, py-h/2),
        arrowstyle='-|>', mutation_scale=20, linewidth=1.5,
        linestyle='--' if realization else '-', edgecolor='#26374a', facecolor='white',
        shrinkA=3, shrinkB=3))
ax.text(.02, .015, 'Hollow triangles point to the general type.  Dashed = realization.  Italic = abstract class.',
        fontsize=10, color='#26374a', va='bottom')
fig.subplots_adjust(left=.015, right=.985, top=.985, bottom=.025)
fig.savefig(Path.cwd() / 'object-oriented-2015-data-hierarchy.png', facecolor='white', metadata={'Software': 'Matplotlib'})
plt.close(fig)
