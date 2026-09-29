"""Enumerate uniform permutations and render their fixed-point counts to cwd."""

from collections import Counter
from itertools import permutations
from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def count_fixed(permutation):
    return sum(value == index for index, value in enumerate(permutation, 1))


def main():
    outcomes = list(permutations(range(1, 5)))
    counts = Counter(count_fixed(p) for p in outcomes)
    assert len(outcomes) == factorial(4)
    assert counts == {0: 9, 1: 8, 2: 6, 4: 1}
    assert sum(k*v for k, v in counts.items()) == 24
    assert all(sum(p[i] == i+1 for p in outcomes) == 6 for i in range(4))
    assert sum(p[0] == 1 and p[1] == 2 for p in outcomes) == 2
    for n in range(1, 8):
        assert sum(count_fixed(p) for p in permutations(range(1, n+1))) == factorial(n)

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig = plt.figure(figsize=(12.5, 7.5), dpi=120, facecolor='white')
    grid = fig.add_gridspec(1, 2, width_ratios=[1.25, 1], wspace=.20)
    cards = fig.add_subplot(grid[0])
    bars = fig.add_subplot(grid[1])
    cards.set_title('All 24 equally likely permutations', pad=30)
    cards.text(.5, 1.025, r'Each row of boxes lists $pi(1),pi(2),pi(3),pi(4)$',
               transform=cards.transAxes, ha='center', fontsize=11)
    for position, p in enumerate(outcomes):
        row, col = divmod(position, 4)
        x0 = col*1.25
        y0 = (5-row)*1.02
        for i, value in enumerate(p):
            fixed = value == i+1
            x = x0+i*.255
            color = '#d5eee1' if fixed else '#eef1f4'
            border = '#277c54' if fixed else '#a4afbb'
            cards.add_patch(Rectangle((x, y0+.23), .235, .40,
                                      facecolor=color, edgecolor=border, lw=1))
            cards.text(x+.1175, y0+.43, str(value), ha='center', va='center',
                       color='#155a38' if fixed else '#293b4a', fontsize=12)
        cards.text(x0+.49, y0+.04, f'M = {count_fixed(p)}',
                   ha='center', va='center', fontsize=10.5)
    cards.set(xlim=(-.13, 4.93), ylim=(-.30, 6))
    cards.axis('off')
    k = np.arange(5)
    masses = np.array([counts[i] for i in k])/24
    bars.bar(k, masses, width=.65, color='#246ea0', zorder=3)
    bars.axvline(1, color='#c06620', linestyle='--', lw=2,
                 label=r'$E[M]=1$')
    for value, mass in zip(k, masses):
        bars.text(value, mass+.013, f'{counts[value]}/24',
                  ha='center', color='#205d87', fontsize=12)
    bars.text(.5, 1.13, r'$E[M]=(0\cdot 9+1\cdot 8+2\cdot 6+4\cdot 1)/24=1$',
              transform=bars.transAxes, fontsize=10.5, ha='center')
    bars.set(xlim=(-.6, 4.6), ylim=(0, .48), xlabel='Number M of fixed points',
             ylabel='Probability mass', title='Exact fixed-point distribution')
    bars.set_xticks(k)
    bars.legend(loc='upper right', frameon=False)
    bars.grid(axis='y', color='#e6eaed', zorder=0)
    bars.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Count fixed points with indicators: the average is one',
                 fontsize=16, y=.98)
    fig.text(.5, .04,
             'Green boxes are fixed points. Three fixed points are impossible: the remaining object must also be fixed.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.035, right=.975, bottom=.14, top=.83)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
