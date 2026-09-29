"""Exact coefficient accounting; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG to the current directory.
"""
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    px = [Fraction(7, 10), Fraction(3, 10)]
    py = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    cells = [[a * b for b in py] for a in px]
    totals = [sum((cells[x][y] for x in range(2) for y in range(3)
                   if x + y == n), Fraction()) for n in range(4)]
    assert totals == [Fraction(7, 40), Fraction(17, 40),
                      Fraction(13, 40), Fraction(3, 40)]
    assert sum(totals) == 1
    colors = ['#466b9c', '#168477', '#c1841a', '#99538a']
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(10, 5.5), dpi=120, facecolor='white')
    fig.suptitle('Adding counts multiplies their probability generating functions',
                 fontsize=17, y=.96)
    fig.text(.5, .875, r'$G_{X+Y}(s)=(0.7+0.3s)(1+2s+s^2)/4$',
             ha='center', fontsize=17)
    ax = fig.add_axes([.06, .22, .49, .53])
    ax.set_xlim(-.75, 3.1)
    ax.set_ylim(-.1, 2.6)
    ax.axis('off')
    fig.text(.30, .79, 'Each cell: joint mass × monomial', ha='center', fontsize=13)
    for y in range(3):
        ax.text(y + .5, 2.18, f'Y = {y}\nP = {float(py[y]):g}',
                ha='center', va='bottom', fontsize=11)
    for x in range(2):
        ax.text(-.12, 1.5 - x, f'X = {x}\nP = {float(px[x]):g}',
                ha='right', va='center', fontsize=11)
        for y in range(3):
            n = x + y
            ax.add_patch(Rectangle((y, 1-x), .97, .94,
                                  facecolor=colors[n], alpha=.16,
                                  edgecolor=colors[n], linewidth=2))
            power = '' if n == 0 else ('s' if n == 1 else f's^{n}')
            ax.text(y+.485, 1.47-x, rf'${float(cells[x][y]):.3f}\,{power}$',
                    ha='center', va='center', fontsize=15, color=colors[n])
    ax2 = fig.add_axes([.66, .22, .30, .53])
    bottoms = [0.0] * 4
    for x in range(2):
        for y in range(3):
            n = x+y
            mass = float(cells[x][y])
            ax2.bar(n, mass, bottom=bottoms[n], color=colors[n],
                    edgecolor='white', linewidth=1.5,
                    alpha=.62 if x == 0 else 1)
            ax2.text(n, bottoms[n]+mass/2, f'{mass:.3f}', ha='center',
                     va='center', color='white' if x else '#162a38', fontsize=11)
            bottoms[n] += mass
    for n, total in enumerate(totals):
        ax2.text(n, float(total)+.012, f'{float(total):.3f}', ha='center',
                 fontsize=12, weight='bold', color=colors[n])
    ax2.set(xticks=range(4), xlabel='Total n = X + Y', ylabel='Probability mass',
            ylim=(0, .49), title='Group equal powers')
    ax2.spines[['top', 'right']].set_visible(False)
    ax2.grid(axis='y', alpha=.15)
    ax2.set_axisbelow(True)
    fig.text(.5, .09, 'Exact chosen model probabilities • all six pairs accounted for • total mass = 1',
             ha='center', fontsize=12)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
