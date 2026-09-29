"""Original phi-fourth diagrams. Tested with Python 3.14 and Matplotlib 3.10.7.
Writes a white opaque PNG to the caller's CWD; respects supplied MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), dpi=120)

def line(ax, a, b, label=None, offset=(0, 0), arrow=False):
    if arrow:
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle='->', mutation_scale=12, linewidth=1.5, color='#253a55'))
    else:
        ax.plot([a[0], b[0]], [a[1], b[1]], color='#253a55', linewidth=1.7)
    if label:
        ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1], label,
                ha='center', va='center', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})

def vertex(ax, pos):
    ax.scatter(*pos, s=28, color='#253a55', zorder=5)

ax = axs[0]
a, b = (-.45, 0), (.55, 0)
line(ax, (-1.55, .65), a, r'$p_1$', offset=(-.08, .1), arrow=True)
line(ax, (-1.55, -.65), a, r'$p_2$', offset=(-.08, -.1), arrow=True)
line(ax, a, (-.55, 1.25), r'$q_1$', offset=(.18, 0), arrow=True)
line(ax, a, b, r'$r=p_1+p_2-q_1$', offset=(0, -.27))
for end, lab, off in [((1.65, .8), r'$q_2$', (0, .1)), ((1.75, 0), r'$q_3$', (0, .14)), ((1.65, -.8), r'$q_4$', (0, -.1))]:
    line(ax, b, end, lab, offset=off, arrow=True)
for v in [a,b]: vertex(ax,v)
ax.set_title('Tree: two quartic vertices', pad=14)

ax = axs[1]
a, b, c = (-.35, .72), (.8, 0), (-.35, -.72)
line(ax, a, b, r'$\ell-P$', offset=(.14, .12))
line(ax, b, c, r'$\ell-Q_{34}$', offset=(.16, -.12))
line(ax, c, a, r'$\ell$', offset=(.18, 0))
line(ax, (-1.4, .9), a, r'$p_1$', offset=(0, .15), arrow=True)
line(ax, (-.7, 1.5), a, r'$p_2$', offset=(.16, .06), arrow=True)
line(ax, b, (1.65, .55), r'$q_1$', offset=(0, .1), arrow=True)
line(ax, b, (1.65, -.55), r'$q_2$', offset=(0, -.1), arrow=True)
line(ax, c, (-1.4, -.9), r'$q_3$', offset=(0, -.15), arrow=True)
line(ax, c, (-.7, -1.5), r'$q_4$', offset=(.17, -.05), arrow=True)
for v in [a,b,c]: vertex(ax,v)
ax.set_title('One loop: scalar triangle', pad=14)
for ax in axs:
    ax.set_xlim(-1.85, 1.95); ax.set_ylim(-1.75, 1.75); ax.set_aspect('equal'); ax.axis('off')
fig.text(.5, .035, r'$P=p_1+p_2,\quad Q_{34}=q_3+q_4$; arrows on external lines indicate momentum, not particle charge.', ha='center', fontsize=10)
fig.subplots_adjust(bottom=.13, wspace=.08, top=.87)
fig.savefig(Path.cwd() / 'paper-48-scattering-diagrams.png', facecolor='white', transparent=False)
plt.close(fig)
