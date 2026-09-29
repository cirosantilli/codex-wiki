"""Original network diagram; Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.

Writes paper-34-braess.png to the caller's current directory.
The caller's MPLCONFIGDIR is preserved; no TeX installation is needed.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), dpi=130, facecolor='white')
positions = {'s': (0, 0), 'u': (1, 1), 'v': (1, -1), 't': (2, 0)}
for index, ax in enumerate(axes):
    ax.set_facecolor('white')
    edges = [('s', 'u', '$z$', (.36, .63)), ('u', 't', '$1$', (1.64, .63)),
             ('s', 'v', '$1$', (.36, -.63)), ('v', 't', '$z$', (1.64, -.63))]
    for source, target, label, labelpos in edges:
        arrow = FancyArrowPatch(positions[source], positions[target], shrinkA=16,
                                shrinkB=16, arrowstyle='-|>', mutation_scale=15,
                                linewidth=1.9, color='#334155')
        ax.add_patch(arrow)
        ax.text(*labelpos, label, fontsize=14, ha='center', va='center',
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    if index:
        ax.add_patch(FancyArrowPatch(positions['u'], positions['v'], shrinkA=16,
                                    shrinkB=16, arrowstyle='-|>', mutation_scale=16,
                                    linewidth=2.4, color='#b45309'))
        ax.text(1.12, 0, '$0$', fontsize=14, color='#92400e', va='center')
    for node, xy in positions.items():
        ax.add_patch(Circle(xy, .11, facecolor='white', edgecolor='#0f172a',
                            linewidth=1.7, zorder=5))
        ax.text(*xy, node, ha='center', va='center', fontsize=13, zorder=6)
    ax.set_title('Two available routes' if not index else 'A third route is added', fontsize=13)
    ax.text(1, -1.42, 'Each route carries 1/2' if not index else 'All demand uses s → u → v → t',
            ha='center', fontsize=10.5)
    ax.text(1, -1.66, 'Equilibrium delay: 3/2' if not index else 'Equilibrium delay: 2',
            ha='center', fontsize=12, fontweight='bold')
    ax.set_xlim(-.25, 2.25)
    ax.set_ylim(-1.8, 1.25)
    ax.set_aspect('equal')
    ax.axis('off')
fig.text(.5, .025, 'One unit of demand; each edge label is its delay at throughput z.',
         ha='center', fontsize=10, color='#475569')
fig.tight_layout(rect=(0, .045, 1, 1), w_pad=3)
fig.savefig('paper-34-braess.png', facecolor='white', transparent=False)
plt.close(fig)
