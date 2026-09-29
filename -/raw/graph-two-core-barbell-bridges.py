"""A 2-core containing bridges. Python 3.14; matplotlib 3.10.7.

Run from the desired output directory; emits this script's basename.png there.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

VERTICES = tuple('abcxydef')
EDGES = ('ab', 'bc', 'ca', 'cx', 'xy', 'yd', 'de', 'ef', 'fd')
POSITIONS = {'a': (0, .2), 'b': (0, 2), 'c': (1.55, 1.1),
             'x': (3, 1.1), 'y': (4.45, 1.1), 'd': (5.9, 1.1),
             'e': (7.45, 2), 'f': (7.45, .2)}


def components_without(edge):
    remaining = [e for e in EDGES if e != edge]
    unseen = set(VERTICES)
    count = 0
    while unseen:
        stack = [unseen.pop()]
        count += 1
        while stack:
            v = stack.pop()
            for a, b in remaining:
                u = b if a == v else a if b == v else None
                if u in unseen:
                    unseen.remove(u)
                    stack.append(u)
    return count


def main():
    degrees = {v: sum(v in e for e in EDGES) for v in VERTICES}
    bridges = {e for e in EDGES if components_without(e) > components_without(None)}
    assert bridges == {'cx', 'xy', 'yd'}
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=100, facecolor='white')
    fig.suptitle('A 2-core can contain bridges', fontsize=19, weight='bold', y=.95)
    ax.set_title('All eight vertices survive: every current degree is at least two', fontsize=12, pad=19)
    for u, v in EDGES:
        bridge = u+v in bridges
        ax.plot([POSITIONS[u][0], POSITIONS[v][0]],
                [POSITIONS[u][1], POSITIONS[v][1]],
                color='#b04d19' if bridge else '#267d91',
                lw=3.3, linestyle='--' if bridge else '-', zorder=1)
    for v, (x, y) in POSITIONS.items():
        ax.add_patch(Circle((x, y), .24, facecolor='#e1f1f4', edgecolor='#174d59', lw=1.6, zorder=2))
        ax.text(x, y, v, ha='center', va='center', fontsize=14, zorder=3)
        ax.text(x, y-.43, f'deg {degrees[v]}', ha='center', va='center', fontsize=11)
    ax.text(3.72, 1.75, 'cx, xy, yd: bridges', ha='center', fontsize=13, color='#a14314', weight='bold')
    ax.text(3.72, .12, 'x and y lie on no cycle', ha='center', fontsize=12, color='#a14314')
    ax.set(xlim=(-.65, 8.1), ylim=(-.5, 2.6), aspect='equal')
    ax.axis('off')
    fig.text(.5, .12, 'Delete any dashed edge: the graph splits into two components.', ha='center', fontsize=12)
    fig.text(.5, .045, 'Solid blue edges: two triangles   |   Dashed amber edges: joining path', ha='center', fontsize=11)
    fig.subplots_adjust(top=.77, bottom=.2, left=.045, right=.955)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', dpi=100)
    plt.close(fig)


if __name__ == '__main__':
    main()
