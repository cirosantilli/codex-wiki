"""Original optical schematics; Python 3.14, matplotlib 3.10.7.

Run from _media; writes the matching opaque PNG into the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=100, facecolor='white')
blue, red, ink = '#1767a0', '#b84827', '#26313d'

def arrow(ax, start, end, color, lw=2.5):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': lw,
                            'mutation_scale': 14})

def splitter(ax, x, y, size=.9):
    ax.add_patch(Rectangle((x-size/2, y-size/2), size, size,
                           facecolor='#eef5f8', edgecolor='#778895', lw=1.5))
    ax.plot([x-size/2, x+size/2], [y-size/2, y+size/2], color=ink, lw=3)

for ax in axes:
    ax.set(xlim=(-2.7, 2.7), ylim=(-2.3, 2.9), aspect='equal')
    ax.axis('off')

ax = axes[0]
ax.set_title('Four ports, two selected inputs', fontsize=15, pad=18)
splitter(ax, 0, 0)
arrow(ax, (-2.25, 0), (-.5, 0), blue)
arrow(ax, (0, -1.95), (0, -.5), red)
arrow(ax, (.5, 0), (2.25, 0), blue)
arrow(ax, (0, .5), (0, 2.25), red)
ax.text(-1.6, .22, r'Input $a_1$', color=blue, ha='center')
ax.text(.18, -1.55, r'Input $a_2$', color=red)
ax.text(1.6, .22, r'Output $b_1$', color=blue, ha='center')
ax.text(.18, 1.65, r'Output $b_2$', color=red)
ax.text(-.9, .67, 'Splitting surface', fontsize=11, ha='right')
ax.plot([-.8, -.2], [.62, .2], color='#778895', lw=1)
ax.text(0, -2.22, r'Transmission: $a_1\to b_1$, $a_2\to b_2$'
        '\n' r'Reflection: $a_1\to b_2$, $a_2\to b_1$',
        va='top', ha='center', fontsize=12, linespacing=1.7)

ax = axes[1]
ax.set_title('Michelson: split, return, recombine', fontsize=15, pad=18)
splitter(ax, 0, 0, .72)
ax.add_patch(Rectangle((-2.55, -.2), .62, .4, facecolor='#edf1f4', edgecolor=ink))
ax.text(-2.24, .33, 'Laser', ha='center')
arrow(ax, (-1.92, 0), (-.4, 0), ink)
# Slight offsets separate the outward/return directions on the same arm.
arrow(ax, (.4, .09), (1.94, .09), blue)
arrow(ax, (1.94, -.09), (.4, -.09), red)
arrow(ax, (-.09, .4), (-.09, 1.98), blue)
arrow(ax, (.09, 1.98), (.09, .4), red)
ax.plot([2.05, 2.05], [-.5, .5], color=ink, lw=5)
ax.plot([-.5, .5], [2.08, 2.08], color=ink, lw=5)
ax.text(1.25, .65, 'Movable mirror', ha='center', fontsize=11)
ax.annotate('', xy=(2.5, -.75), xytext=(1.6, -.75),
            arrowprops={'arrowstyle': '<->', 'color': ink, 'lw': 1.5})
ax.text(2.04, -1.03, 'Micrometer travel', ha='center', fontsize=10)
ax.text(0, 2.36, 'Fixed mirror', ha='center')
arrow(ax, (0, -.4), (0, -1.3), red)
ax.add_patch(Rectangle((-.42, -1.73), .84, .4, facecolor='#edf1f4', edgecolor=ink))
ax.text(-.6, -1.53, 'Detector', ha='right', va='center')
arrow(ax, (-.4, -.12), (-1.7, -.12), red, lw=1.5)
ax.text(-1.2, -.56, 'Return toward source', ha='center', fontsize=10)
ax.text(0, -2.22, 'Blue: outward    Red: returning / recombined'
        '\nSteering optics omitted; schematic is not to scale.',
        va='top', ha='center', fontsize=10.5, linespacing=1.8)

fig.subplots_adjust(left=.035, right=.975, bottom=.20, top=.88, wspace=.28)
fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
plt.close(fig)
