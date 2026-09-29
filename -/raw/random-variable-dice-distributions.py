"""Count exact PMFs of two observables on one finite dice sample space."""

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    outcomes = list(product(range(1, 7), repeat=2))
    sums = Counter(u + v for u, v in outcomes)
    maxima = Counter(max(u, v) for u, v in outcomes)
    assert sum(sums.values()) == sum(maxima.values()) == 36
    assert all(sums[s] == 6 - abs(s - 7) for s in range(2, 13))
    assert all(maxima[m] == 2 * m - 1 for m in range(1, 7))
    sum_mean = sum(Fraction(s * count, 36) for s, count in sums.items())
    max_mean = sum(Fraction(m * count, 36) for m, count in maxima.items())
    sum_variance = sum(Fraction((s - 7) ** 2 * count, 36) for s, count in sums.items())
    assert sum_mean == 7 and max_mean == Fraction(161, 36)
    assert sum_variance == Fraction(35, 6)
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4), layout='constrained', facecolor='white')
    for ax, counts, color, title, xlabel in [
        (axes[0], sums, '#2563a6', 'Sum S = U + V', 'Sum'),
        (axes[1], maxima, '#b76816', 'Maximum M = max(U, V)', 'Maximum')
    ]:
        xs = sorted(counts)
        ps = [counts[x] / 36 for x in xs]
        ax.bar(xs, ps, color=color, width=.75)
        for x, p in zip(xs, ps):
            ax.text(x, p + .009, str(counts[x]), ha='center', va='bottom', fontsize=10)
        ax.set(xticks=xs, xlabel=xlabel, ylabel='Probability', ylim=(0, .37), title=title)
        ax.grid(axis='y', alpha=.2)
    fig.suptitle('One outcome space, two observables; labels count outcomes out of 36', fontsize=14)
    fig.savefig(Path.cwd() / 'random-variable-dice-distributions.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
