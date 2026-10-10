"""Draw a constructed finite chain, not measured data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../markov-classes-absorption-terminal-routine.py
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, PathPatch
from matplotlib.path import Path as MPath
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(7.6, 4.5), dpi=120, facecolor='white')
    ax.set_facecolor('white')
    ax.set(xlim=(-1.35, 4.35), ylim=(-1.9, 2.4), aspect='equal')
    ax.axis('off')
    ink, blue, green = '#273746', '#246b9b', '#267050'
    pos = {'u': (0, 1), 'v': (3, 1), 'A': (0, -0.7), 'B': (3, -0.7)}
    for name, xy in pos.items():
        terminal = name in 'AB'
        ax.add_patch(Circle(xy, .29, facecolor='#e8f4eb' if terminal else '#e8f1fa', edgecolor=green if terminal else blue, lw=2, zorder=3))
        if terminal:
            ax.add_patch(Circle(xy, .23, fill=False, edgecolor=green, lw=1, zorder=4))
        ax.text(*xy, name, ha='center', va='center', fontsize=15, color=ink, zorder=5)
    def edge(start, end, label, xy, rad=0):
        ax.add_patch(FancyArrowPatch(pos[start], pos[end], arrowstyle='-|>', mutation_scale=15, shrinkA=23, shrinkB=23, connectionstyle=f'arc3,rad={rad}', lw=1.7, color=ink))
        ax.text(*xy, label, ha='center', va='center', color=ink, bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    edge('u', 'v', '1/4', (1.5, 1.55), -.28)
    edge('v', 'u', '1/4', (1.5, .46), -.28)
    edge('u', 'A', '1/4', (-.32, .15))
    edge('v', 'B', '1/2', (3.33, .15))
    # Cubic Bezier loops start and finish on the node boundary.
    def loop(name, label, direction):
        x, y = pos[name]
        d = direction
        vertices = [(x-.17, y+.24*d), (x-.9, y+1.15*d), (x+.9, y+1.15*d), (x+.17, y+.24*d)]
        path = MPath(vertices, [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
        ax.add_patch(FancyArrowPatch(path=path, arrowstyle='-|>', mutation_scale=13, lw=1.7, color=ink))
        ax.text(x, y+.93*d, label, ha='center', va='center', color=ink, bbox={'facecolor':'white','edgecolor':'none','pad':1})
    loop('u', '1/2', 1)
    loop('v', '1/4', 1)
    loop('A', '1', -1)
    loop('B', '1', -1)
    fig.text(.5, .96, 'Two unfinished modes, two absorbing outcomes', ha='center', va='top', fontsize=15, weight='bold', color=ink)
    fig.text(.5, .895, 'Constructed toy chain • each outgoing row sums to 1', ha='center', fontsize=10, color=ink)
    fig.text(.5, .10, r'From $u$:  P(end at $A$) = 3/5;  mean terminal time = 16/5 steps', ha='center', fontsize=11, color=blue)
    fig.text(.5, .045, r'From $v$:  P(end at $A$) = 1/5;  mean terminal time = 12/5 steps', ha='center', fontsize=11, color=blue)
    fig.subplots_adjust(left=.06, right=.94, top=.85, bottom=.15)
    # Check displayed summaries against the transition model.
    q = np.array([[.5, .25], [.25, .25]])
    r = np.array([[.25, 0], [0, .5]])
    n = np.linalg.solve(np.eye(2)-q, np.eye(2))
    assert np.allclose(n @ r, [[.6, .4], [.2, .8]])
    assert np.allclose(n @ np.ones(2), [3.2, 2.4])
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
