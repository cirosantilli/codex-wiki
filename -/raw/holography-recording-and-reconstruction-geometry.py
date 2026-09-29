"""Functional in-line holography geometry; Python 3.14, matplotlib 3.10.7.

Run from _media. Draws a chosen plane-reference, point-object scalar model,
not the detailed historical pinhole apparatus. All dimensions are schematic.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle

BLUE, ORANGE, PURPLE = '#1967a3', '#ba5316', '#7950a1'
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(2, 1, figsize=(10, 6.4))
fig.subplots_adjust(left=.035, right=.985, top=.88, bottom=.07, hspace=.48)
fig.suptitle('Holography: recording intensity, reconstructing a field', fontsize=16)

def arrow(ax, a, b, color, **kw):
    ax.annotate('', xy=b, xytext=a, arrowprops={'arrowstyle': '->', 'color': color, 'lw': 1.5, **kw})

for ax in axes:
    ax.set(xlim=(0, 10.6), ylim=(-1.7, 1.7))
    ax.axis('off')
    ax.plot([.1, 10.4], [0, 0], color='.85', lw=1, zorder=0)
    ax.add_patch(Rectangle((5.92, -1.25), .16, 2.5, facecolor='#eeeeee', edgecolor='.3'))

ax = axes[0]
ax.set_title('1  RECORD: object present', loc='left', fontsize=13, pad=11)
for y in [-.95, .95]:
    arrow(ax, (.3, y), (5.85, y), BLUE)
for x in [.65, 1.2, 1.75]:
    ax.plot([x, x], [-1.15, 1.15], color=BLUE, lw=1, alpha=.4)
ax.scatter([3], [0], s=38, color=ORANGE, zorder=4)
for y in [-1.1, -.55, .55, 1.1]:
    arrow(ax, (3, 0), (5.85, y), ORANGE)
for r in [.65, 1.25, 1.9]:
    ax.add_patch(Arc((3, 0), 2*r, 2*r, theta1=-25, theta2=25, color=ORANGE, alpha=.5))
ax.text(.3, -1.5, 'Coherent plane illumination', color=BLUE)
ax.text(3, -.55, 'Object point', ha='center', color=ORANGE)
ax.text(2.7, 1.15, 'Undiffracted reference R', color=BLUE, ha='center')
ax.text(4.55, -1.5, 'Object wave O', color=ORANGE, ha='center')
ax.text(6.35, .55, 'Sensitive plate records', fontsize=12)
ax.text(6.35, .02, r'$I=|R+O|^2$', fontsize=17)
ax.text(6.35, -.55, 'Relative phase → fringe positions', fontsize=10)

ax = axes[1]
ax.set_title('2  RECONSTRUCT: object removed', loc='left', fontsize=13, pad=11)
for y in [-.95, 0, .95]:
    arrow(ax, (.3, y), (5.85, y), BLUE)
    arrow(ax, (6.1, y), (10.35, y), BLUE, alpha=.45)
for y in [-.75, .75]:
    end_y = y*(9.6-3)/(6-3)
    arrow(ax, (6.1, y*(6.1-3)/3), (9.6, end_y), ORANGE)
    ax.plot([3, 6], [0, y], '--', color=ORANGE, lw=1)
    arrow(ax, (6.1, y*(9-6.1)/3), (9, 0), PURPLE)
    ax.plot([9, 10.35], [0, -y*1.35/3], color=PURPLE, lw=1, alpha=.5)
ax.scatter([3], [0], s=42, facecolors='white', edgecolors=ORANGE, zorder=4)
ax.scatter([9], [0], s=30, color=PURPLE, zorder=4)
ax.text(.3, -1.5, 'Readout with reference R only', color=BLUE)
ax.text(3, -.97, 'Desired virtual image\n(backward extensions)', ha='center', color=ORANGE, fontsize=10, bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1})
ax.text(6, -1.55, 'Developed hologram: t', ha='center')
ax.text(9, -.9, 'Conjugate real image', ha='center', color=PURPLE, fontsize=10)
ax.text(8.1, 1.52, 'Desired field ∝ O', ha='center', color=ORANGE, fontsize=10)
ax.text(8.4, .6, 'Zero order ∝ R', ha='center', color=BLUE, fontsize=10)
fig.text(.5, .015, 'Term colours are not wavelengths. Distances and field strengths are schematic.', ha='center', fontsize=10, color='.35')
fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png', dpi=120, facecolor='white')
plt.close(fig)
