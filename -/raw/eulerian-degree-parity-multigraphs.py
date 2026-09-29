"""Draw exact undirected multigraph examples; Python 3.14, Matplotlib 3.10.7.

Run from _media with MPLBACKEND=Agg. Output uses the script basename in CWD.
"""
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.path import Path as PlotPath
from matplotlib.patches import FancyArrowPatch, PathPatch


def degrees(vertices, edges):
    result = Counter({v: 0 for v in vertices})
    for _, u, v in edges:
        result[u] += 1
        result[v] += 1
    return result


def draw(ax, positions, edges, bends, offsets, title, subtitle):
    degree = degrees(positions, edges)
    for name, u, v in edges:
        x, y = positions[u]
        if u == v:
            loop = PlotPath([(x - .08, y + .12), (x - .85, y + .95),
                             (x - .85, y - .4), (x - .12, y - .07)],
                            [PlotPath.MOVETO, PlotPath.CURVE4,
                             PlotPath.CURVE4, PlotPath.CURVE4])
            ax.add_patch(PathPatch(loop, fill=False, lw=2, color='#536575'))
        else:
            ax.add_patch(FancyArrowPatch(positions[u], positions[v],
                         connectionstyle=f'arc3,rad={bends.get(name, 0)}',
                         arrowstyle='-', lw=2, color='#536575',
                         shrinkA=17, shrinkB=17))
        lx, ly = offsets[name]
        ax.text(lx, ly, name, ha='center', va='center', fontsize=11,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    for v, (x, y) in positions.items():
        odd = degree[v] % 2
        color = '#ba4728' if odd else '#17785e'
        ax.scatter([x], [y], s=580, facecolor='white', edgecolor=color,
                   linewidth=2.4, zorder=3)
        ax.text(x, y, v, ha='center', va='center', fontsize=13, zorder=4)
        label_y = y + .32 if v == 'A' and len(positions) == 4 else y - .32
        ax.text(x, label_y, f'degree {degree[v]}', ha='center', fontsize=10,
                color=color)
    ax.set_title(title, fontsize=14, pad=16)
    ax.text(.5, -.03, subtitle, transform=ax.transAxes, ha='center',
            va='top', fontsize=11, linespacing=1.5)
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.25, 1.75), aspect='equal')
    ax.axis('off')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'figure.facecolor': 'white'})
    positions = {'A': (0, 0), 'B': (-1, 1.15), 'C': (-1, -.85), 'D': (1.1, .1)}
    edges = [('p₁', 'A', 'B'), ('p₂', 'A', 'B'), ('q₁', 'A', 'C'),
             ('q₂', 'A', 'C'), ('t', 'A', 'D'), ('r', 'B', 'D'), ('s', 'C', 'D')]
    bends = {'p₁': .23, 'p₂': -.23, 'q₁': .23, 'q₂': -.23}
    offsets = {'p₁': (-.72, .38), 'p₂': (-.23, .77), 'q₁': (-.22, -.66),
               'q₂': (-.74, -.23), 't': (.57, .17), 'r': (.18, .86), 's': (.25, -.6)}
    reduced = [e for e in edges if e[0] != 't']
    pair_loop = [('ℓ', 'A', 'A'), ('p', 'A', 'B'), ('q', 'A', 'B')]
    assert list(degrees(positions, edges).values()) == [5, 3, 3, 3]
    assert list(degrees(positions, reduced).values()) == [4, 3, 3, 2]
    assert list(degrees(['A', 'B', 'Z'], pair_loop).values()) == [4, 2, 0]
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.5), dpi=110)
    draw(axes[0], positions, edges, bends, offsets, 'Four odd vertices',
         'Seven bridges: no Eulerian trail')
    draw(axes[1], positions, reduced, bends, offsets, 'Two odd vertices',
         'Remove AD: endpoints B and C\nB — A — C — D — B — A — C')
    draw(axes[2], {'A': (-.7, .35), 'B': (.8, .35), 'Z': (.5, -.75)},
         pair_loop, {'p': .28, 'q': -.28},
         {'ℓ': (-1.14, .96), 'p': (.05, .07), 'q': (.05, .65)},
         'All degrees even', 'Loop + parallel edges: Euler circuit\nA — A — B — A; Z is isolated')
    fig.suptitle('Degree parity controls edge-covering trails', fontsize=17, y=.99)
    fig.subplots_adjust(left=.025, right=.975, bottom=.19, top=.80, wspace=.14)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
