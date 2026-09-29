"""Draw a complete queue-based 2-core trace. Python 3.14; matplotlib 3.10.7.

Run from the desired output directory; emits this script's basename.png there.
"""
from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

VERTICES = tuple('abcdefgz')
EDGES = ('ab', 'bc', 'ca', 'cd', 'de', 'ef', 'dg')
POSITIONS = {'a': (-.7, .15), 'b': (-.7, 1.5), 'c': (.55, .82),
             'd': (1.85, .82), 'e': (3.15, .82), 'f': (4.45, .82),
             'g': (1.85, 2.12), 'z': (4.45, 2.12)}


def compute_trace():
    adjacency = {v: [] for v in VERTICES}
    for u, v in EDGES:
        adjacency[u].append(v)
        adjacency[v].append(u)
    degrees = {v: len(adjacency[v]) for v in VERTICES}
    alive = set(VERTICES)
    queue = deque(v for v in VERTICES if degrees[v] < 2)
    trace = [(None, alive.copy(), dict(degrees), tuple(queue))]
    while queue:
        v = queue.popleft()
        alive.remove(v)
        for u in adjacency[v]:
            if u in alive:
                degrees[u] -= 1
                if degrees[u] == 1:
                    queue.append(u)
        trace.append((v, alive.copy(), {u: degrees[u] for u in alive}, tuple(queue)))
    return trace


def main():
    trace = compute_trace()
    fig, axes = plt.subplots(2, 3, figsize=(11.7, 7.2), dpi=100, facecolor='white')
    fig.suptitle('A triangle survives; its entire tail and isolated vertex disappear',
                 fontsize=16, y=.97, weight='bold')
    for step, (ax, (deleted, alive, degrees, queue)) in enumerate(zip(axes.flat, trace)):
        for u, v in EDGES:
            active = u in alive and v in alive
            ax.plot([POSITIONS[u][0], POSITIONS[v][0]],
                    [POSITIONS[u][1], POSITIONS[v][1]],
                    color='#3a8795' if active else '#e0e3e5',
                    lw=2.7 if active else 1.2, zorder=1)
        for v, (x, y) in POSITIONS.items():
            active = v in alive
            fill = '#d7eef0' if active and v in 'abc' else '#fff0d4' if active else 'white'
            color = '#174d59' if active else '#ced3d6'
            ax.add_patch(Circle((x, y), .23, facecolor=fill, edgecolor=color, lw=1.5, zorder=2))
            ax.text(x, y, v, ha='center', va='center', color=color, fontsize=13, zorder=3)
            if active:
                ax.text(x, y-.43, f'deg {degrees[v]}', ha='center', va='center', fontsize=10,
                        color='#353d44')
        title = '0. Original graph' if deleted is None else f'{step}. Delete {deleted}'
        ax.set_title(title, loc='left', fontsize=13, weight='bold', pad=8)
        qtext = ', '.join(queue) if queue else 'empty'
        ax.text(.02, -.02, f'Queue: {qtext}', transform=ax.transAxes, fontsize=12,
                color='#a24e13' if queue else '#174d59')
        if not queue:
            ax.text(.02, -.17, 'Remaining: triangle abc', transform=ax.transAxes,
                    fontsize=11, color='#174d59', weight='bold')
        ax.set(xlim=(-1.3, 5.05), ylim=(-.6, 2.75), aspect='equal')
        ax.axis('off')
    fig.text(.5, .025, 'Blue: surviving triangle   |   Amber: surviving tail / isolate   |   Pale: deleted   |   Degrees are current',
             ha='center', fontsize=11, color='#353d44')
    fig.subplots_adjust(left=.035, right=.98, bottom=.12, top=.88, wspace=.15, hspace=.45)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', dpi=100)
    plt.close(fig)


if __name__ == '__main__':
    main()
