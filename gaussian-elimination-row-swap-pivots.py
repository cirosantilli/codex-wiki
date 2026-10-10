"""Original row-operation diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; emits gaussian-elimination-row-swap-pivots.png to CWD.
"""

from pathlib import Path
from fractions import Fraction

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def stages():
    rows = [[Fraction(v) for v in row] for row in
            [[0, 2, 1, 3], [1, -2, -3, 0], [2, 3, 1, 7]]]
    result = [[row[:] for row in rows]]
    rows[0], rows[1] = rows[1], rows[0]
    result.append([row[:] for row in rows])
    rows[2] = [a - 2 * b for a, b in zip(rows[2], rows[0])]
    result.append([row[:] for row in rows])
    rows[2] = [a - Fraction(7, 2) * b for a, b in zip(rows[2], rows[1])]
    result.append([row[:] for row in rows])
    return result


def label(value):
    if value.denominator == 1:
        return str(value.numerator)
    sign = '-' if value < 0 else ''
    return rf'${sign}\frac{{{abs(value.numerator)}}}{{{value.denominator}}}$'


def matrix(ax, rows, pivots=(), zeros=(), blocked=False):
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            color = '#ecf0f4' if j == 3 else 'white'
            if (i, j) in pivots:
                color = '#bce7d7'
            if (i, j) in zeros:
                color = '#d6e9fb'
            if blocked and (i, j) == (0, 0):
                color = '#f8d6cd'
            ax.add_patch(Rectangle((j, 2-i), 1, 1, facecolor=color,
                                   edgecolor='white', linewidth=2))
            ax.text(j+.5, 2.5-i, label(value), ha='center', va='center',
                    fontsize=21, color='#20364a')
    ax.plot([3, 3], [0, 3], color='#435568', linewidth=1.3)
    for x, sign in [(-.12, 1), (4.12, -1)]:
        ax.plot([x+.10*sign, x, x, x+.10*sign], [0, 0, 3, 3],
                color='#435568', linewidth=1.5)
    for j, name in enumerate([r'$x_1$', r'$x_2$', r'$x_3$', 'RHS']):
        ax.text(j+.5, 3.32, name, ha='center', fontsize=11, color='#526475')
    ax.set(xlim=(-.4, 4.4), ylim=(-.62, 3.7))
    ax.axis('off')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans'})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.2), facecolor='white')
    fig.subplots_adjust(left=.05, right=.95, top=.82, bottom=.18,
                        wspace=.18, hspace=.60)
    fig.suptitle('Gaussian elimination: a zero pivot needs a row swap',
                 fontsize=19, y=.965, color='#20364a')
    fig.text(.5, .905, 'Every row operation acts on the right-hand side too.',
             ha='center', fontsize=12, color='#526475')
    titles = ['1. Original augmented matrix', r'2. Swap $R_1$ and $R_2$',
              r'3. $R_3\leftarrow R_3-2R_1$',
              r'4. $R_3\leftarrow R_3-\frac{7}{2}R_2$']
    notes = ['Zero cannot be the first pivot.', 'A nonzero pivot starts elimination.',
             'First-column zeros are preserved.', 'Three nonzero pivots: solve upward.']
    pivots = [(), ((0, 0),), ((0, 0), (1, 1)), ((0, 0), (1, 1), (2, 2))]
    zeros = [(), (), ((1, 0), (2, 0)), ((1, 0), (2, 0), (2, 1))]
    for k, (ax, rows) in enumerate(zip(axes.flat, stages())):
        matrix(ax, rows, pivots[k], zeros[k], blocked=k == 0)
        ax.set_title(titles[k], fontsize=14, pad=15, color='#20364a')
        ax.text(2, -.48, notes[k], ha='center', fontsize=11, color='#526475')
    fig.text(.5, .10, r'Back substitution: $x_3=-1\quad\longrightarrow\quad'
             r'x_2=2\quad\longrightarrow\quad x_1=1$',
             ha='center', fontsize=17, color='#20364a')
    fig.text(.5, .04, 'Green: chosen pivots     Blue: zeros created by elimination'
             '     Gray: right-hand side', ha='center', fontsize=11, color='#526475')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
