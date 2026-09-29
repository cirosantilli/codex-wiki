"""Exact original graph and elimination trace; write PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dashed edges denote symbolic fill, not observations or numerical measurements.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


OUTPUT = Path(__file__).with_suffix('.png').name
EDGES = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'),
         ('c', 'd'), ('c', 'e'), ('d', 'e')]
FILL = [('a', 'd'), ('a', 'e'), ('b', 'e')]
POS = {'a': (0, 0), 'b': (0.9, 1), 'c': (1.8, 0),
       'd': (2.7, 1), 'e': (3.6, 0)}
INK, BLUE, TEAL, RED = '#243447', '#2563a0', '#087e82', '#b43c38'


def draw(ax, bad=False):
    if not bad:
        for clique, color in [(('a', 'b', 'c'), '#e4f1fb'),
                               (('b', 'c', 'd'), '#e8f4ee'),
                               (('c', 'd', 'e'), '#fff1da')]:
            ax.add_patch(Polygon([POS[v] for v in clique], facecolor=color,
                                 edgecolor='none', zorder=0))
    for u, v in EDGES:
        if bad and 'c' in (u, v):
            continue
        ax.plot(*zip(POS[u], POS[v]), color=INK, lw=2.2, zorder=1)
    if bad:
        for u, v in FILL:
            ax.plot(*zip(POS[u], POS[v]), color=RED, lw=2.4,
                    ls=(0, (4, 3)), zorder=2)
    for v, (x, y) in POS.items():
        if bad and v == 'c':
            ax.text(x, y - 0.12, 'c removed', fontsize=11, ha='center',
                    color='#6e7a87')
            continue
        ax.scatter(x, y, s=620, color='white', edgecolor=BLUE, lw=2, zorder=3)
        ax.text(x, y, v, fontsize=16, color=INK, ha='center', va='center', zorder=4)
    ax.set(xlim=(-0.3, 3.9), ylim=(-0.45, 1.42), aspect='equal')
    ax.axis('off')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig = plt.figure(figsize=(11, 6.25), dpi=110, facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=[1.02, 1.15],
                           left=0.04, right=0.97, top=0.84, bottom=0.11,
                           wspace=0.15, hspace=0.23)
    fig.suptitle('The same chordal graph, two first-pivot choices',
                 fontsize=19, color=INK, y=0.96)
    a = fig.add_subplot(grid[0, 0])
    b = fig.add_subplot(grid[0, 1])
    draw(a)
    draw(b, bad=True)
    a.set_title('Three triangles: start with a', fontsize=14, color=INK)
    b.set_title('Start with c: three fill edges', fontsize=14, color=INK)
    a.text(1.8, -0.38, 'Neighbors {b, c} already form a clique.', ha='center', fontsize=12)
    b.text(1.8, -0.38, 'Dashed new edges: ad, ae, be', ha='center', fontsize=12, color=RED)
    trace = fig.add_subplot(grid[1, 0])
    trace.axis('off')
    trace.set_title('Perfect deletion order: a, b, c, d, e', fontsize=13, color=INK, pad=8)
    table = trace.table(cellText=[['a', '{b, c}', 'bc'], ['b', '{c, d}', 'cd'],
                                  ['c', '{d, e}', 'de'], ['d', '{e}', 'none needed'],
                                  ['e', '{}', 'none needed']],
                        colLabels=['Delete', 'Later neighbors', 'Existing edge'],
                        cellLoc='center', colWidths=[0.17, 0.43, 0.40],
                        bbox=[0, 0.02, 1, 0.91])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#c9d4df')
        cell.set_facecolor('#edf6f8' if row == 0 else 'white')
        cell.get_text().set_color(INK)
    explain = fig.add_subplot(grid[1, 1])
    explain.axis('off')
    explain.text(0.5, 0.92, 'Clique tree: shared variables stay connected', ha='center',
                 fontsize=13, color=INK)
    labels = ['{a, b, c}', '{b, c, d}', '{c, d, e}']
    for x, label in zip([0.14, 0.50, 0.86], labels):
        explain.text(x, 0.64, label, ha='center', va='center', fontsize=12,
                     bbox={'boxstyle': 'round,pad=0.35', 'facecolor': '#edf6f8',
                           'edgecolor': TEAL, 'linewidth': 1.5})
    for x, label in [(0.32, '{b, c}'), (0.68, '{c, d}')]:
        explain.plot([x - 0.085, x + 0.085], [0.64, 0.64], color=TEAL, lw=2)
        explain.text(x, 0.44, label, ha='center', fontsize=12, color=TEAL)
    explain.text(0.5, 0.22, 'Maximum cardinality search selects e, d, c, b, a.\n'
                 'Reverse this sequence for deletion.\nNo symbolic fill with the perfect order.',
                 ha='center', va='center', fontsize=12, color=INK, linespacing=1.6)
    explain.set(xlim=(0, 1), ylim=(0, 1))
    fig.text(0.5, 0.035, 'Exact finite graphs • fill edges show the structural elimination rule',
             ha='center', fontsize=11, color='#536274')
    fig.savefig(OUTPUT, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
