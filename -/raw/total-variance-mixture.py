"""Illustrate exact population variance decomposition; tested on Python 3.14."""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    groups = ((1, 3), (5, 11))
    means = [sum(map(Fraction, group)) / 2 for group in groups]
    variances = [sum((Fraction(x) - m) ** 2 for x in group) / 2
                 for group, m in zip(groups, means)]
    mean = sum(means) / 2
    within = sum(variances) / 2
    between = sum((m - mean) ** 2 for m in means) / 2
    total = sum((Fraction(x) - mean) ** 2 for group in groups for x in group) / 4
    assert means == [2, 8] and variances == [1, 9]
    assert mean == 5 and within == 5 and between == 9 and total == 14
    assert within + between == total
    # Equal group means leave only within-group spread; deterministic groups
    # leave only between-group spread. Both are exact population calculations.
    aligned = [Fraction(x) for x in (4, 6, 2, 8)]
    assert sum(aligned) / 4 == 5
    assert sum((x - 5) ** 2 for x in aligned) / 4 == 5
    deterministic = [Fraction(x) for x in (2, 2, 8, 8)]
    assert sum((x - 5) ** 2 for x in deterministic) / 4 == 9
    print(f'means={means}, variances={variances}; mean={mean}, within={within}, '
          f'between={between}, total={total}')

    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False})
    blue, orange, purple = '#2878ac', '#c26916', '#7556a7'
    fig, (ax, bars) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained',
                                  gridspec_kw={'width_ratios': [1.4, 1]},
                                  facecolor='white')
    for y, group, m, color in zip((1, 0), groups, means, (blue, orange)):
        ax.plot(group, [y, y], color=color, lw=4, alpha=.45)
        ax.scatter(group, [y, y], color=color, s=80, zorder=3)
        ax.scatter(float(m), y, color=color, marker='D', s=65, zorder=4)
        for x in group:
            ax.text(x, y + .13, f'{x}', ha='center', color=color)
        ax.text(float(m), y - .24, f'mean {m}; variance {variances[1-y]}',
                ha='center', color=color)
    ax.axvline(float(mean), color='#444444', ls='--', lw=1.5,
               label='Overall mean 5')
    ax.plot([], [], marker='D', ls='', color='#555555', label='Group mean')
    ax.set(xlim=(0, 12), ylim=(-.55, 1.5), xticks=np.arange(0, 13, 2),
           yticks=[0, 1], yticklabels=['B (weight 1/2)', 'A (weight 1/2)'],
           xlabel='Outcome X', title='Each dot has probability 1/4')
    ax.legend(loc='upper right', fontsize=9, frameon=False)
    bars.bar([0, 1], [float(within), float(total)], width=.55,
             color=[blue, '#cccccc'])
    bars.bar(0, float(between), bottom=float(within), width=.55, color=purple)
    bars.text(0, 2.5, 'Within\n5', ha='center', va='center', color='white', fontsize=13)
    bars.text(0, 9.5, 'Between\n9', ha='center', va='center', color='white', fontsize=13)
    bars.text(1, 7, 'Total\n14', ha='center', va='center', fontsize=13)
    bars.set(xticks=[0, 1], xticklabels=['Decomposed', 'Direct check'],
             ylim=(0, 16), ylabel='Variance (squared units)', title='14 = 5 + 9')
    bars.set_axisbelow(True)
    bars.yaxis.grid(alpha=.2)
    fig.suptitle('Total variance: spread within groups + spread of group means', fontsize=14)
    fig.savefig(Path.cwd() / 'total-variance-mixture.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
