"""Draw the counterexample to the simple-cycle version of the SCC criterion.

Run with Python 3.14 and matplotlib 3.10.7. Writes an opaque PNG in cwd.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/functional-programming-2013-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import matplotlib.patheffects as pe


def main():
    fig, ax = plt.subplots(figsize=(9.6, 4.3), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.16)
    ax.set(xlim=(-3.1, 3.1), ylim=(-1.45, 1.45), aspect='equal')
    ax.axis('off')
    points = {'a': (0, 0), 'b': (-2.1, 1.05), 'c': (-2.1, -1.05),
              'd': (2.1, 1.05), 'e': (2.1, -1.05)}
    for u, v, white in [('a','b',False), ('b','c',False), ('c','a',False),
                        ('a','d',True), ('d','e',True), ('e','a',True)]:
        arrow = FancyArrowPatch(points[u], points[v], arrowstyle='-|>',
                                mutation_scale=22, shrinkA=20, shrinkB=20,
                                linewidth=2.8, color='white' if white else '#202020',
                                zorder=2)
        if white:
            arrow.set_path_effects([pe.Stroke(linewidth=5.0, foreground='#555555'),
                                   pe.Normal()])
        ax.add_patch(arrow)
    for name, (x, y) in points.items():
        ax.add_patch(Circle((x, y), .20, facecolor='#e9f1fa', edgecolor='#24456a',
                            linewidth=1.4, zorder=3))
        ax.text(x, y, name, fontsize=15, ha='center', va='center', zorder=4)
    ax.text(-1.55, 0, 'black\ntriangle', ha='center', va='center', fontsize=12)
    ax.text(1.55, 0, 'white\ntriangle', ha='center', va='center', fontsize=12)
    fig.suptitle('One strongly connected component; no mixed simple cycle',
                 fontsize=15, y=.96)
    fig.text(.5, .07, 'A mixed closed walk traverses both triangles and revisits a.',
             ha='center', fontsize=12)
    fig.savefig(Path.cwd() / 'functional-programming-2013-mixed-cycles.png',
                facecolor='white', transparent=False,
                metadata={'Software': 'functional-programming-2013-mixed-cycles.py'})
    plt.close(fig)


if __name__ == '__main__':
    main()
