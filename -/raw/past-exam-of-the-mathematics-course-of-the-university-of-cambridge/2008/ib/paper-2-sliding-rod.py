"""Sliding-rod current diagram; Python 3.14, matplotlib 3.10.7.

Write the PNG basename to the caller's current directory. Honour MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=100, facecolor='white')
ax.set_facecolor('white')
rail = '#253448'
current = '#bd3329'
bar = '#27709d'
ax.plot([0, 5.45], [0, 0], color=rail, lw=3)
ax.plot([0, 5.45], [2.4, 2.4], color=rail, lw=3)
ax.plot([0, 0], [0, .65], color=rail, lw=3)
ax.plot([0, 0], [1.75, 2.4], color=rail, lw=3)
ax.plot([0, -.12, .12, -.12, .12, -.12, .12, 0],
        [.65, .8, .95, 1.1, 1.25, 1.4, 1.55, 1.75], color=rail, lw=2.5)
ax.text(-.43, 1.2, '$R$', fontsize=18, va='center', ha='center')
ax.plot([4.3, 4.3], [0, 2.4], color=bar, lw=7, solid_capstyle='round')

def arrow(start, end, color=current, label=None, offset=(0, 0)):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5,
                            'mutation_scale': 19})
    if label:
        mid = ((start[0]+end[0])/2+offset[0], (start[1]+end[1])/2+offset[1])
        ax.text(*mid, label, color=color, fontsize=17, ha='center', va='center')

arrow((1.2, 2.4), (2.9, 2.4), label='$I$', offset=(0, .28))
arrow((4.3, 1.85), (4.3, .65), label='$I$', offset=(.35, 0))
arrow((2.9, 0), (1.2, 0), label='$I$', offset=(0, -.3))
arrow((-.58, .65), (-.58, 1.75), label='$I$', offset=(-.24, 0))
arrow((4.3, 3), (5.65, 3), color=bar, label='$v$', offset=(0, .24))
arrow((4.2, -.8), (2.95, -.8), color='#506432', label='$F_B$', offset=(0, -.28))
for x in [1.0, 2.0, 3.0]:
    for y in [.65, 1.7]:
        ax.add_patch(Circle((x, y), .09, edgecolor='#66798e', facecolor='white', lw=1.5))
        ax.plot(x, y, 'o', color='#66798e', markersize=2.5)
ax.text(2, 1.18, '$B$ out of the page', ha='center', fontsize=15, color=rail,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
ax.annotate('', xy=(5.8, 2.4), xytext=(5.8, 0),
            arrowprops={'arrowstyle': '<->', 'color': rail, 'lw': 1.5})
ax.text(6.03, 1.2, r'$\ell$', fontsize=18, ha='center')
ax.text(0, -.36, '$(0,0)$', fontsize=12, ha='center')
ax.text(0, 2.65, r'$(0,\ell)$', fontsize=12, ha='center')
ax.text(4.3, 2.68, 'sliding rod', fontsize=13, ha='center', color=bar)
ax.set_title('Induced current and magnetic braking', fontsize=19, pad=16)
ax.set_xlim(-1.2, 6.45)
ax.set_ylim(-1.32, 3.6)
ax.set_aspect('equal')
ax.axis('off')
fig.subplots_adjust(left=.04, right=.98, bottom=.06, top=.88)
fig.savefig(Path.cwd() / 'paper-2-sliding-rod.png', dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
