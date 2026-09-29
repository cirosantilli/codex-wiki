"""Render all self-maps of a two-point set and their composition table to cwd."""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def compose(f, g):
    return tuple(f[g[x]] for x in range(2))


def main():
    names = ['i', 's', 'c₀', 'c₁']
    maps = [(0, 1), (1, 0), (0, 0), (1, 1)]
    index = {f: k for k, f in enumerate(maps)}
    table = np.array([[index[compose(f, g)] for g in maps] for f in maps])
    identity, swap, zero, one = maps
    assert set(maps) == set(product(range(2), repeat=2))
    assert all(compose(identity, f) == compose(f, identity) == f for f in maps)
    assert all(compose(compose(f, g), h) == compose(f, compose(g, h))
               for f, g, h in product(maps, repeat=3))
    invertible = [f for f in maps if any(compose(f, g) == compose(g, f) == identity
                                        for g in maps)]
    assert invertible == [identity, swap]
    assert compose(zero, swap) == zero and compose(swap, zero) == one
    assert compose(zero, zero) == zero and compose(one, one) == one
    assert np.array_equal(table[0], np.arange(4))
    assert np.array_equal(table[:, 0], np.arange(4))

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig = plt.figure(figsize=(12.2, 7.2), dpi=120, facecolor='white')
    outer = fig.add_gridspec(1, 2, width_ratios=[1.1, 1], wspace=.25)
    diagrams = outer[0].subgridspec(2, 2, hspace=.35, wspace=.25)
    for k, (f, name) in enumerate(zip(maps, names)):
        ax = fig.add_subplot(diagrams[k//2, k % 2])
        for x in range(2):
            y = 1-x
            ax.scatter([0, 1], [y, y], s=330, facecolor='#e9f0f6',
                       edgecolor='#4c6d86', zorder=3)
            ax.text(0, y, str(x), ha='center', va='center', fontsize=12, zorder=4)
            ax.text(1, y, str(x), ha='center', va='center', fontsize=12, zorder=4)
            ax.annotate('', xy=(.91, 1-f[x]), xytext=(.09, y),
                        arrowprops={'arrowstyle': '->', 'lw': 1.7,
                                    'color': '#246ea0', 'shrinkA': 4, 'shrinkB': 4})
        desc = ['identity', 'swap', 'constant 0', 'constant 1'][k]
        ax.set_title(f'{name}: {desc}', pad=10)
        ax.text(.5, -.35, 'has an inverse' if k < 2 else 'has no inverse',
                ha='center', fontsize=11,
                color='#277c54' if k < 2 else '#965225')
        ax.set(xlim=(-.22, 1.22), ylim=(-.45, 1.35)); ax.axis('off')
    ax = fig.add_subplot(outer[1])
    palette = ListedColormap(['#d8eddc', '#cbdcf0', '#f8e5c9', '#e7d7ed'])
    ax.imshow(table, cmap=palette, vmin=0, vmax=3)
    for row, col in product(range(4), repeat=2):
        ax.text(col, row, names[table[row, col]], ha='center', va='center', fontsize=22)
    ax.set_xticks(range(4), names); ax.set_yticks(range(4), names)
    ax.set_xticks(np.arange(-.5, 4), minor=True)
    ax.set_yticks(np.arange(-.5, 4), minor=True)
    ax.grid(which='minor', color='white', lw=3)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
    ax.set(xlabel='g: applied first (column)', ylabel='f: applied second (row)')
    ax.set_title('Cell = f ∘ g', pad=55)
    ax.text(.5, -.15, 'c₀ ∘ s = c₀      but      s ∘ c₀ = c₁',
            transform=ax.transAxes, ha='center', fontsize=13)
    fig.suptitle('Composition is associative even when transformations lose information',
                 fontsize=16, y=.97)
    fig.text(.5, .06, 'Only the identity and swap are reversible; the four maps together form a monoid.',
             ha='center', fontsize=12)
    fig.subplots_adjust(left=.045, right=.975, bottom=.20, top=.78)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
