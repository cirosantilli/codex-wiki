"""Enumerate two-draw designs; Python 3.14, matplotlib 3.10, numpy 2.3."""
from itertools import combinations, product
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np


def main():
    values = np.arange(2, 13, 2)
    subsets = list(combinations(values, 2))
    replacement = list(product(values, repeat=2))
    assert len(subsets) == 15 and len(replacement) == 36
    assert np.isclose(np.var(np.mean(subsets, axis=1)), 14 / 3)
    assert np.isclose(np.var(np.mean(replacement, axis=1)), 35 / 6)
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.9), gridspec_kw={'width_ratios': [1, 1.12]})
    fig.suptitle('Six labelled values: 2, 4, 6, 8, 10, 12   |   Two selections', fontsize=15, y=.97)
    cmap = plt.get_cmap('Blues')
    norm = Normalize(2, 12)
    ax = axes[0]
    ax.set_title('Without replacement: all 15 subsets\nEach subset has probability 1/15', pad=15)
    for row, (a, b) in enumerate(subsets):
        mean = (a + b) / 2
        ax.scatter([a, b], [row, row], s=46, color='#116a8e', zorder=3)
        ax.plot([a, b], [row, row], color='#8db9cc', lw=2)
        ax.text(14.2, row, f'{mean:g}', ha='center', va='center', fontsize=10)
    ax.text(14.2, -1.1, 'Mean', ha='center', weight='bold')
    ax.set(xticks=values, yticks=np.arange(15),
           yticklabels=[f'{{{a}, {b}}}' for a, b in subsets], ylim=(15, -1.8), xlim=(1, 15.2),
           xlabel='Selected values')
    ax.grid(axis='x', alpha=.15)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax = axes[1]
    means = (values[:, None] + values[None, :]) / 2
    ax.imshow(means, cmap=cmap, norm=norm, origin='upper', extent=(-.5, 5.5, 5.5, -.5))
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f'{means[i, j]:g}', ha='center', va='center',
                    color='white' if means[i, j] >= 8 else '#183340', fontsize=12)
            if i == j:
                ax.add_patch(plt.Rectangle((j - .5, i - .5), 1, 1, fill=False,
                                          edgecolor='#d55e00', lw=2.5))
    ax.set_title('With replacement: all 36 ordered outcomes\nEach cell has probability 1/36; text = mean', pad=15)
    ax.set(xticks=np.arange(6), yticks=np.arange(6), xticklabels=values, yticklabels=values,
           xlabel='Second selected value', ylabel='First selected value')
    fig.text(.75, .11, 'Orange diagonal: the same label is selected twice',
             ha='center', fontsize=10, color='#a74900')
    fig.text(.25, .045, 'Expected mean = 7\nMean variance = 14/3', ha='center', fontsize=12)
    fig.text(.75, .045, 'Expected mean = 7\nMean variance = 35/6', ha='center', fontsize=12)
    fig.subplots_adjust(left=.09, right=.97, bottom=.19, top=.81, wspace=.34)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
