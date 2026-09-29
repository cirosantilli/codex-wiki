"""Draw closed classes versus an absorbing state in a constructed chain.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../markov-classes-absorption-closed-cycle.py
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as MPath


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(7.6, 4.6), dpi=120, facecolor='white')
    ax.set_facecolor('white')
    ax.set(xlim=(-1.25, 5.6), ylim=(-2.25, 2.2), aspect='equal')
    ax.axis('off')
    ink, blue, orange, green = '#273746', '#246b9b', '#b46418', '#267050'
    pos = {'s': (0, 0), 'c1': (2.6, .95), 'c2': (4.65, .95), 'a': (3.65, -1.15)}
    for x, y, w, h, color in [(-.7, -.6, 1.4, 1.95, orange), (1.95, .1, 3.4, 1.65, blue), (2.75, -1.9, 2.15, 1.45, green)]:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.15', lw=1.4, linestyle=(0, (4, 3)), facecolor='white', edgecolor=color, zorder=0))
    for name, xy in pos.items():
        color = orange if name == 's' else green if name == 'a' else blue
        ax.add_patch(Circle(xy, .28, facecolor='#f8f4ee' if name == 's' else '#e8f4eb' if name == 'a' else '#e8f1fa', edgecolor=color, lw=2, zorder=3))
        if name == 'a':
            ax.add_patch(Circle(xy, .22, fill=False, edgecolor=green, lw=1, zorder=4))
        text = {'s': '$s$', 'c1': '$c_1$', 'c2': '$c_2$', 'a': '$a$'}[name]
        ax.text(*xy, text, ha='center', va='center', fontsize=15, color=ink, zorder=5)
    def edge(start, end, label, xy, rad=0):
        ax.add_patch(FancyArrowPatch(pos[start], pos[end], arrowstyle='-|>', mutation_scale=15, shrinkA=22, shrinkB=22, connectionstyle=f'arc3,rad={rad}', lw=1.7, color=ink))
        ax.text(*xy, label, ha='center', va='center', color=ink, bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1.5})
    edge('s', 'c1', '1/4', (1.13, .65))
    edge('s', 'a', '1/4', (1.3, -.70))
    edge('c1', 'c2', '1', (3.65, 1.45), -.3)
    edge('c2', 'c1', '1', (3.65, .46), -.3)
    def loop(name, label, direction):
        x, y = pos[name]
        d = direction
        vertices = [(x-.16, y+.23*d), (x-.8, y+1.02*d), (x+.8, y+1.02*d), (x+.16, y+.23*d)]
        path = MPath(vertices, [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
        ax.add_patch(FancyArrowPatch(path=path, arrowstyle='-|>', mutation_scale=13, lw=1.7, color=ink))
        ax.text(x, y+.85*d, label, ha='center', va='center', color=ink, bbox={'facecolor':'white','edgecolor':'none','pad':1})
    loop('s', '1/2', 1)
    # Side loop keeps the absorbing state and its class label apart.
    x, y = pos['a']
    path = MPath([(x+.23,y+.16),(x+1.2,y+.7),(x+1.2,y-.7),(x+.23,y-.16)], [MPath.MOVETO,MPath.CURVE4,MPath.CURVE4,MPath.CURVE4])
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle='-|>', mutation_scale=13, lw=1.7, color=ink))
    ax.text(x+1.0,y,'1', ha='center', va='center', color=ink, bbox={'facecolor':'white','edgecolor':'none','pad':1})
    ax.text(0, -.46, 'open', color=orange, ha='center', fontsize=11)
    ax.text(3.65, .22, 'closed: alternates forever', color=blue, ha='center', fontsize=10)
    ax.text(3.65, -1.72, 'closed: absorbing', color=green, ha='center', fontsize=10)
    fig.text(.5, .96, 'A closed class need not be an absorbing state', ha='center', va='top', fontsize=15, weight='bold', color=ink)
    fig.text(.5, .89, 'Constructed toy chain • dashed outlines are communicating classes', ha='center', fontsize=10, color=ink)
    fig.text(.5, .09, r'From $s$:  P(enter the pair) = P(hit $a$) = 1/2', ha='center', fontsize=12, color=ink)
    fig.text(.5, .035, r'Mean time to either closed class: 2 steps', ha='center', fontsize=11, color=ink)
    fig.subplots_adjust(left=.035, right=.965, top=.84, bottom=.15)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
