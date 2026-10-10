"""Exact finite-model Bayesian updates for one hidden selected coin."""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def posterior(sequence):
    biased = Fraction(1, 5)
    fair = Fraction(4, 5)
    for toss in sequence:
        biased *= Fraction(3, 4) if toss == 'H' else Fraction(1, 4)
        fair *= Fraction(1, 2)
    return biased / (biased + fair)


def main():
    assert posterior('H') == Fraction(3, 11)
    assert posterior('HHH') == Fraction(27, 59)
    assert posterior('HHHH') == Fraction(81, 145)
    p_head = Fraction(4, 5) * Fraction(1, 2) + Fraction(1, 5) * Fraction(3, 4)
    p_two = Fraction(4, 5) * Fraction(1, 2) ** 2 + Fraction(1, 5) * Fraction(3, 4) ** 2
    assert p_head == Fraction(11, 20)
    assert p_two == Fraction(5, 16) and p_two - p_head ** 2 == Fraction(1, 100)
    heads = np.arange(9)
    after_heads = np.array([float(posterior('H' * int(n))) for n in heads])
    mixed_sequence = 'HHHTHTHT'
    mixed = np.array([float(posterior(mixed_sequence[:n])) for n in range(9)])
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), layout='constrained', facecolor='white')
    ax, bars = axes
    ax.plot(heads, after_heads, 'o-', color='#b76816', label='Only heads observed')
    ax.plot(heads, mixed, 's-', color='#2563a6', label='Sequence H H H T H T H T')
    ax.axhline(.5, color='#777777', linewidth=1, linestyle='--')
    ax.set(xlabel='Number of observations', ylabel='Posterior probability of the 3/4-head coin',
           ylim=(0, 1), xticks=heads, title='One selected coin, repeatedly tossed')
    ax.grid(alpha=.2)
    ax.legend(fontsize=10, loc='upper left')
    ax.annotate('4 heads: 81/145', (4, after_heads[4]), xytext=(4.35, .42),
                fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#555555'})
    values = np.array([[.8, .2], [8 / 11, 3 / 11]])
    labels = ['Before data', 'After one head']
    positions = np.arange(2)
    bars.bar(positions, values[:, 0], color='#9ab6ca', label='Fair coin')
    bars.bar(positions, values[:, 1], bottom=values[:, 0], color='#e2a451', label='3/4-head coin')
    for i in range(2):
        bars.text(i, values[i, 0] / 2, ['4/5', '8/11'][i], ha='center', va='center')
        bars.text(i, values[i, 0] + values[i, 1] / 2, ['1/5', '3/11'][i],
                  ha='center', va='center')
    bars.set(xticks=positions, xticklabels=labels, ylim=(0, 1), ylabel='Probability',
             title='A head favors the biased coin\nbut does not yet make it more likely')
    bars.legend(loc='lower center', bbox_to_anchor=(.5, -.26), fontsize=11, ncol=2)
    fig.suptitle('Bayes: posterior odds = prior odds × likelihood ratio', fontsize=15)
    fig.savefig(Path.cwd() / 'bayes-coin-updating.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
