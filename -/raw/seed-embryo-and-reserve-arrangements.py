"""Original seed-section schematic; Python 3.14, matplotlib 3.10.7.
Run from _media; writes seed-embryo-and-reserve-arrangements.png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(11.2, 6.8), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 11.2), ylim=(0, 6.8), aspect='equal')
ax.axis('off')
brown, yellow, green = '#78502d', '#f6d77e', '#267348'
ax.text(5.6, 6.48, 'A seed carries both a young plant and its food supply', ha='center', fontsize=17, weight='bold')
for x in (2.8, 8.4):
    ax.add_patch(Ellipse((x, 3.65), 3.6, 4, facecolor='#fff9e9', edgecolor=brown, linewidth=5))
ax.text(2.8, 5.97, 'Reserves in cotyledons', ha='center', fontsize=14, weight='bold')
ax.text(8.4, 5.97, 'Reserves in endosperm', ha='center', fontsize=14, weight='bold')
for x in (2.17, 3.43):
    ax.add_patch(Ellipse((x, 3.6), 1.18, 2.65, facecolor=yellow, edgecolor=green, linewidth=2))
ax.plot([2.8, 2.8, 3.0], [4.6, 2.4, 2.15], color=green, linewidth=9, solid_capstyle='round')
ax.add_patch(Ellipse((2.8, 4.75), .48, .5, facecolor=green, edgecolor='white'))
ax.text(2.8, 3.6, 'Cotyledons\n(part of embryo)', ha='center', va='center', fontsize=11, bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.add_patch(Ellipse((8.4, 3.65), 3.34, 3.75, facecolor=yellow, edgecolor='none'))
ax.add_patch(Ellipse((8.45, 2.9), 1.65, 1.55, facecolor='#d5ecd9', edgecolor=green, linewidth=2))
ax.plot([8.3, 8.3, 8.48], [3.4, 2.5, 2.2], color=green, linewidth=7, solid_capstyle='round')
ax.add_patch(Ellipse((8.05, 3.32), .52, .3, angle=35, facecolor='#d5ecd9', edgecolor=green, linewidth=2))
ax.add_patch(Ellipse((8.62, 3.32), .52, .3, angle=-35, facecolor='#d5ecd9', edgecolor=green, linewidth=2))
ax.text(8.4, 4.47, 'Endosperm\n(outside embryo)', ha='center', va='center', fontsize=12)
ax.text(8.45, 2.95, 'Embryo', ha='center', va='center', fontsize=11, bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
for text, xy, pos in [('Seed coat', (1.1, 4.3), (.15, 5.2)), ('Radicle\n(future root)', (2.99, 2.15), (.2, 1.35)), ('Seed coat', (10.14, 4.3), (10.1, 5.2)), ('Radicle', (8.48, 2.2), (10.15, 1.6))]:
    ax.annotate(text, xy, xytext=pos, ha='left' if pos[0]<6 else 'center', va='center', fontsize=12, arrowprops={'arrowstyle':'->','color':'#333','lw':1.5})
ax.text(5.6, .8, 'Yellow = major food reserve     Green outline / axis = embryo structures', ha='center', fontsize=12)
ax.text(5.6, .33, 'Alternative tissue arrangements • schematic sections • not to scale', ha='center', fontsize=11, color='#555')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
plt.close(fig)
