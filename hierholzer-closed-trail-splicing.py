"""Draw a verified closed-trail splice; Python 3.14, Matplotlib 3.10.7.

Run from _media with MPLBACKEND=Agg. Output uses the script basename in CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


POSITIONS = {'A': (0, 0), 'B': (-1.35, .95), 'C': (-1.35, -.95),
             'D': (1.35, .95), 'E': (1.35, -.95)}
EDGES = [('A', 'B'), ('B', 'C'), ('C', 'A'),
         ('A', 'D'), ('D', 'E'), ('E', 'A')]
BLUE, ORANGE = '#17679a', '#b6531d'


def check_trail(vertices, expected):
    traversed = [frozenset(e) for e in zip(vertices, vertices[1:])]
    assert vertices[0] == vertices[-1]
    assert len(traversed) == len(set(traversed))
    assert set(traversed) == {frozenset(e) for e in expected}


def draw(ax, numbered):
    for i, (u, v) in enumerate(EDGES):
        color = BLUE if i < 3 else ORANGE
        ax.add_patch(FancyArrowPatch(POSITIONS[u], POSITIONS[v],
                     arrowstyle='-|>', mutation_scale=15, lw=2.7,
                     color=color, shrinkA=21, shrinkB=21))
        x = (POSITIONS[u][0] + POSITIONS[v][0]) / 2
        y = (POSITIONS[u][1] + POSITIONS[v][1]) / 2
        if i in (1, 4):
            x += -.18 if i == 1 else .18
        ax.text(x, y, str(i + 1) if numbered else u + v, fontsize=12,
                ha='center', va='center', color=color,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    for v, (x, y) in POSITIONS.items():
        ax.scatter([x], [y], s=740, facecolor='white', edgecolor='#263540',
                   linewidth=2, zorder=4)
        ax.text(x, y, v, ha='center', va='center', fontsize=15, zorder=5)
    ax.set(xlim=(-1.9, 1.9), ylim=(-1.45, 1.45), aspect='equal')
    ax.axis('off')


def main():
    first, second = ['A', 'B', 'C', 'A'], ['A', 'D', 'E', 'A']
    spliced = first + second[1:]
    check_trail(first, EDGES[:3])
    check_trail(second, EDGES[3:])
    check_trail(spliced, EDGES)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=110)
    draw(axes[0], False)
    draw(axes[1], True)
    axes[0].set_title('1. Grow two closed trails at A', fontsize=15)
    axes[1].set_title('2. Splice: each edge appears once', fontsize=15)
    axes[0].text(.5, -.035, 'A → B → C → A     +     A → D → E → A',
                 ha='center', transform=axes[0].transAxes, fontsize=12)
    axes[1].text(.5, -.035, 'A → B → C → A → D → E → A', ha='center',
                 transform=axes[1].transAxes, fontsize=13)
    fig.suptitle('Hierholzer splicing preserves closure and edge identity',
                 fontsize=17, y=.97)
    fig.text(.5, .065, 'Degrees: A = 4; B, C, D, E = 2.   Six edges; A is revisited.',
             ha='center', fontsize=12)
    fig.text(.5, .02, 'Arrows show traversal direction along undirected edges.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.03, right=.97, bottom=.22, top=.81, wspace=.14)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
