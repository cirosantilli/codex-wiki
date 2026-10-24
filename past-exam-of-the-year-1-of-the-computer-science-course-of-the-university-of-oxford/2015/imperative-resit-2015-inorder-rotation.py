"""Generate imperative-resit-2015-inorder-rotation.png in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5, as documented
in the repository pyproject.toml. Uses only matplotlib and the standard library.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'imperative-resit-2015-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch


def draw_tree(ax, nodes, edges, subtrees):
    for a, b in edges:
        ax.plot([nodes[a][0], nodes[b][0]], [nodes[a][1], nodes[b][1]], color='#344454', lw=1.6, zorder=1)
    for name in ('x', 'y'):
        x, y = nodes[name]
        ax.add_patch(Circle((x, y), 0.19, facecolor='#dceaf5', edgecolor='#264d70', lw=1.8, zorder=3))
        ax.text(x, y, name, ha='center', va='center', fontsize=15, zorder=4)
    for name in subtrees:
        x, y = nodes[name]
        ax.add_patch(Polygon([(x, y+0.10), (x-.28, y-.39), (x+.28, y-.39)], closed=True,
                             facecolor='#f0f2f3', edgecolor='#52616b', lw=1.5, zorder=2))
        ax.text(x, y-.23, name, ha='center', va='center', fontsize=13, zorder=4)
    ax.set_xlim(-.45, 3.5)
    ax.set_ylim(-.65, 3.15)
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), facecolor='white')
    before = {'y': (2.2, 2.45), 'x': (1.05, 1.4), 'A': (.35, .30), 'B': (1.75, .30), 'C': (3.0, 1.25)}
    after = {'x': (.8, 2.45), 'y': (2.0, 1.4), 'A': (0., 1.25), 'B': (1.3, .30), 'C': (2.7, .30)}
    draw_tree(axes[0], before, [('y','x'),('y','C'),('x','A'),('x','B')], 'ABC')
    draw_tree(axes[1], after, [('x','A'),('x','y'),('y','B'),('y','C')], 'ABC')
    axes[0].set_title('Before: y is the current root', fontsize=12)
    axes[1].set_title('After: promote left child x', fontsize=12)
    fig.suptitle('One right rotation', fontsize=16, y=.97)
    fig.text(.5, .055, 'Inorder in both trees:  A, x, B, y, C', ha='center', fontsize=13)
    fig.add_artist(FancyArrowPatch((.465,.51),(.535,.51), transform=fig.transFigure,
                                  arrowstyle='-|>', mutation_scale=20, color='#264d70', lw=2))
    fig.subplots_adjust(left=.035, right=.965, top=.83, bottom=.13, wspace=.26)
    out = Path('imperative-resit-2015-inorder-rotation.png')
    fig.savefig(out, dpi=140, facecolor='white', transparent=False,
                metadata={'Software':'imperative-resit-2015-inorder-rotation.py'})
    plt.close(fig)
    print(out.resolve())


if __name__ == '__main__':
    main()
