"""Render addition and subtraction modulo three operation tables to cwd."""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def main():
    add = lambda a, b: (a+b) % 3
    subtract = lambda a, b: (a-b) % 3
    addition = np.array([[add(a, b) for b in range(3)] for a in range(3)])
    subtraction = np.array([[subtract(a, b) for b in range(3)] for a in range(3)])
    assert np.all(addition == addition.T)
    assert not np.all(subtraction == subtraction.T)
    assert all(add(add(a, b), c) == add(a, add(b, c))
               for a, b, c in product(range(3), repeat=3))
    failures = [(a, b, c) for a, b, c in product(range(3), repeat=3)
                if subtract(subtract(a, b), c) != subtract(a, subtract(b, c))]
    assert len(failures) == 18
    assert subtract(subtract(2, 1), 1) == 0
    assert subtract(2, subtract(1, 1)) == 2
    assert all(0 <= operation(a, b) < 3 for operation in (add, subtract)
               for a, b in product(range(3), repeat=2))
    plt.rcParams.update({'font.size': 13, 'axes.titlesize': 15})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.6), dpi=120, facecolor='white')
    palette = ListedColormap(['#f6efd6', '#cce6e7', '#cbd5ee'])
    for ax, table, title in zip(axes, [addition, subtraction],
                               ['Addition modulo 3', 'Subtraction modulo 3']):
        ax.imshow(table, cmap=palette, vmin=0, vmax=2)
        for row, col in product(range(3), repeat=2):
            ax.text(col, row, str(table[row, col]), ha='center', va='center',
                    fontsize=24, color='#253848')
        ax.set_xticks(range(3)); ax.set_yticks(range(3))
        ax.set_xticks(np.arange(-.5, 3), minor=True)
        ax.set_yticks(np.arange(-.5, 3), minor=True)
        ax.grid(which='minor', color='white', linewidth=3)
        ax.tick_params(which='minor', bottom=False, left=False)
        ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
        ax.set(xlabel='Second input b (column)', ylabel='First input a (row)',
               title=title)
        ax.set_title(title, pad=55)
    axes[0].text(.5, -.13, 'Symmetric: commutative', transform=axes[0].transAxes,
                 ha='center', fontsize=13, color='#256855')
    axes[1].text(.5, -.13, 'Not symmetric: not commutative',
                 transform=axes[1].transAxes, ha='center', fontsize=13,
                 color='#965225')
    fig.suptitle('A binary operation needs a result for every ordered pair',
                 fontsize=16, y=.97)
    fig.text(.5, .20, 'Associativity also fails for subtraction:', ha='center', fontsize=13)
    fig.text(.5, .14, '((2 − 1) − 1) mod 3 = 0       but       (2 − (1 − 1)) mod 3 = 2',
             ha='center', fontsize=14)
    fig.text(.5, .065, 'Every displayed result belongs to {0, 1, 2}; closure alone does not supply other laws.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.09, right=.98, bottom=.31, top=.78, wspace=.35)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
