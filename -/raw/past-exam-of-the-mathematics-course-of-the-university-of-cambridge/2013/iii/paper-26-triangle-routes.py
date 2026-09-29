"""Original triangle-route diagram. Python 3.14; NumPy/Matplotlib per root pyproject.
Writes only paper-26-triangle-routes.png into the current working directory.
Set MPLCONFIGDIR externally to the desired private cache directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), dpi=100, facecolor='white')
ports = {'a': (-.55, -.45), 'b': (.55, -.45), 'c': (0, .5)}
outer = {'A': (-1.25, -.45), 'B': (1.25, -.45), 'C': (0, 1.15)}
for j, ax in enumerate(axes):
    coords = outer | ({'w': (0, .05)} if j == 0 else ports)
    edges = [('A', 'w'), ('w', 'B'), ('w', 'C')] if j == 0 else [('A', 'a'), ('B', 'b'), ('C', 'c'), ('a', 'b'), ('b', 'c'), ('c', 'a')]
    route = [('A', 'w'), ('w', 'B')] if j == 0 else ([('A', 'a'), ('a', 'b'), ('b', 'B')] if j == 1 else [('A', 'a'), ('a', 'c'), ('c', 'b'), ('b', 'B')])
    for u, v in edges:
        ax.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color='#c8cdd2', lw=2, zorder=1)
    for u, v in route:
        ax.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color=['#333333', '#146fa8', '#b75e18'][j], lw=4, zorder=2)
    for name, (x, y) in coords.items():
        ax.add_patch(Circle((x, y), .055, facecolor='black' if name in outer else 'white', edgecolor='black', lw=1.4, zorder=3))
        ax.text(x, y - .18 if name in ['A', 'B', 'a', 'b'] else y + .13, name, ha='center', va='center', fontsize=12)
    ax.set_title(['Original passage', 'Direct triangle route', 'Detour through third port'][j], fontsize=12, pad=8)
    ax.text(0, -.97, ['$2$ edges: weight $x^2$', '$3$ edges: weight $x^3$', '$4$ edges: weight $x^4$'][j], ha='center', fontsize=12)
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.13, 1.5), aspect='equal')
    ax.axis('off')
fig.subplots_adjust(left=.025, right=.975, bottom=.07, top=.87, wspace=.18)
fig.savefig(Path.cwd() / 'paper-26-triangle-routes.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
