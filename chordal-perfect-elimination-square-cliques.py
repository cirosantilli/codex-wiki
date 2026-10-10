"""Original finite graphs; output basename to CWD, using an opaque white canvas.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


OUTPUT = Path(__file__).with_suffix('.png').name
SQUARE = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
POS = {'a': (0, 1), 'b': (1, 1), 'c': (1, 0), 'd': (0, 0)}
BLUE, TEAL, INK = '#2563a0', '#087e82', '#243447'


def graph(ax, diagonal=False):
    for u, v in SQUARE:
        ax.plot(*zip(POS[u], POS[v]), color=INK, lw=2.4, zorder=1)
    if diagonal:
        ax.plot(*zip(POS['a'], POS['c']), color=TEAL, lw=3, zorder=2)
        ax.text(0.37, 0.40, 'chord ac', color=TEAL, fontsize=12,
                rotation=-45, ha='center', va='center',
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    for v, (x, y) in POS.items():
        ax.scatter(x, y, s=650, color='white', edgecolor=BLUE, lw=2.2, zorder=3)
        ax.text(x, y, v, ha='center', va='center', fontsize=17,
                color=INK, zorder=4)
    ax.set(xlim=(-0.28, 1.28), ylim=(-0.45, 1.3), aspect='equal')
    ax.axis('off')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.1), dpi=110,
                             facecolor='white', gridspec_kw={'width_ratios': [1, 1, 1.28]})
    fig.suptitle('One chord turns a square into overlapping cliques',
                 fontsize=18, color=INK, y=0.96)
    graph(axes[0])
    graph(axes[1], diagonal=True)
    axes[0].set_title('$C_4$: not chordal', fontsize=14, color=INK, pad=8)
    axes[1].set_title('$C_4 + ac$: chordal', fontsize=14, color=INK, pad=8)
    axes[0].text(0.5, -0.32, 'Four-cycle with no chord', ha='center', fontsize=12)
    axes[1].text(0.5, -0.32, 'Triangles abc and acd', ha='center', fontsize=12)
    ax = axes[2]
    ax.axis('off')
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.set_title('Clique tree', fontsize=14, color=INK, pad=8)
    for y, label in [(0.74, '{a, b, c}'), (0.28, '{a, c, d}')]:
        ax.add_patch(FancyBboxPatch((0.20, y - 0.10), 0.60, 0.20,
                                    boxstyle='round,pad=0.015',
                                    facecolor='#edf6f8', edgecolor=TEAL, lw=2))
        ax.text(0.5, y, label, ha='center', va='center', fontsize=17, color=INK)
    ax.plot([0.5, 0.5], [0.39, 0.63], color=TEAL, lw=2.5)
    ax.text(0.5, 0.51, '{a, c}', ha='center', va='center', fontsize=14,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    ax.text(0.5, 0.04, 'Nodes are maximal cliques;\nedge label is their intersection.',
            ha='center', va='center', fontsize=12, color=INK)
    fig.text(0.5, 0.035, 'Exact constructed graphs • adjacency is independent of the drawing',
             ha='center', color='#536274', fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.98, top=0.79, bottom=0.14, wspace=0.17)
    fig.savefig(OUTPUT, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
