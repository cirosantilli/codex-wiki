"""Original conceptual care pathway; no empirical counts or source artwork.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the PNG is written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, ax = plt.subplots(figsize=(11.4, 5.0), dpi=120, facecolor='white')
ax.set(xlim=(0, 11.4), ylim=(0, 5.0))
ax.axis('off')
ax.text(5.7, 4.72, 'Access is a pathway to effective care', ha='center', va='center', fontsize=17, weight='bold')
xs = [0.18, 2.47, 4.76, 7.05, 9.34]
stages = [
 ('Recognise need', 'Notice avoidance\nand impairment'),
 ('Enter care', 'Find assessment\nand an accessible route'),
 ('Receive treatment', 'Practise active content\nwith suitable guidance'),
 ('Check progress', 'Measure symptoms\nand everyday functioning'),
 ('Adapt support', 'Maintain gains or\nescalate care promptly'),
]
for i, (x, (title, body)) in enumerate(zip(xs, stages)):
 ax.add_patch(FancyBboxPatch((x, 2.52), 1.88, 1.27, boxstyle='round,pad=0.07', facecolor='#eaf1fa', edgecolor='#315b88', linewidth=1.4))
 ax.text(x + .94, 3.48, title, ha='center', va='center', fontsize=11.2, weight='bold')
 ax.text(x + .94, 2.98, body, ha='center', va='center', fontsize=10.1, linespacing=1.4)
 if i < 4:
  ax.add_patch(FancyArrowPatch((x+1.99, 3.15), (xs[i+1]-.09, 3.15), arrowstyle='-|>', mutation_scale=15, linewidth=1.4, color='#315b88'))
ax.text(5.7, 2.05, 'Caregiver roles: recognise difficulties • navigate services • support practice • review progress', ha='center', fontsize=11.2)
ax.add_patch(FancyBboxPatch((.3, .49), 10.76, .91, boxstyle='round,pad=0.09', facecolor='#f4f5f3', edgecolor='#686f63'))
ax.text(5.68, 1.11, 'Check who is missing at every stage', ha='center', weight='bold', fontsize=12)
ax.text(5.68, .75, 'Time, language, cost, digital access and family burden can prevent participation.', ha='center', fontsize=11)
ax.text(5.7, .12, 'Conceptual diagram; stages are not population counts. Child perspectives and appropriate urgent routes remain essential.', ha='center', fontsize=9.0, color='#444444')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False, metadata={'Software': 'Matplotlib'})
plt.close(fig)
