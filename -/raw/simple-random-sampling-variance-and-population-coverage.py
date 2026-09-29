"""Exact finite-population variance and distinct-label coverage; Python 3.14."""
from itertools import combinations, product
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.arange(2, 13, 2)
    population_size = len(values)
    sizes = np.arange(1, population_size + 1)
    variance_wor, variance_wr, coverage_wr = [], [], []
    for n in sizes:
        wor = np.array(list(combinations(values, int(n))))
        wr = np.array(list(product(values, repeat=int(n))))
        variance_wor.append(np.var(wor.mean(axis=1)))
        variance_wr.append(np.var(wr.mean(axis=1)))
        coverage_wr.append(np.mean([len(set(row)) / population_size for row in wr]))
    S2 = np.var(values, ddof=1)
    assert np.allclose(variance_wor, (1 - sizes / population_size) * S2 / sizes)
    assert np.allclose(variance_wr, np.var(values) / sizes)
    assert np.allclose(coverage_wr, 1 - (1 - 1 / population_size) ** sizes)
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.3))
    fig.suptitle('The same fixed population: 2, 4, 6, 8, 10, 12', fontsize=15, y=.97)
    blue, orange = '#146b8c', '#c05b15'
    ax = axes[0]
    ax.plot(sizes, variance_wr, 's--', color=orange, label='Independent draws with replacement', lw=2)
    ax.plot(sizes, variance_wor, 'o-', color=blue, label='Simple random sampling without replacement', lw=2)
    ax.set(title='Exact variance of the sample mean', xlabel='Number of draws n',
           ylabel='Variance', xticks=sizes, ylim=(-.35, 13))
    ax.annotate('n = 2: 35/6', (2, 35 / 6), xytext=(2.7, 7.5), color=orange,
                arrowprops={'arrowstyle': '-', 'color': orange})
    ax.annotate('n = 2: 14/3', (2, 14 / 3), xytext=(2.8, 4.8), color=blue,
                arrowprops={'arrowstyle': '-', 'color': blue})
    ax.annotate('All six distinct labels:\nvariance = 0', (6, 0), xytext=(3.4, 9.5), color=blue,
                arrowprops={'arrowstyle': '->', 'color': blue})
    ax = axes[1]
    ax.plot(sizes, sizes / population_size, 'o-', color=blue, lw=2)
    ax.plot(sizes, coverage_wr, 's--', color=orange, lw=2)
    ax.set(title='Expected fraction of distinct labels seen', xlabel='Number of draws n',
           ylabel='Population coverage', xticks=sizes, ylim=(0, 1.08), yticks=np.arange(0, 1.01, .2))
    ax.annotate('n/6: no duplicates', (4, 4 / 6), xytext=(1.1, .84), color=blue,
                arrowprops={'arrowstyle': '-', 'color': blue})
    ax.annotate('1 − (5/6)ⁿ\nSix draws: about 66.5%', (6, coverage_wr[-1]),
                xytext=(2.4, .22), color=orange,
                arrowprops={'arrowstyle': '->', 'color': orange})
    for ax in axes:
        ax.grid(alpha=.2)
    fig.legend(*axes[0].get_legend_handles_labels(), loc='lower center', bbox_to_anchor=(.5, .095),
               frameon=False, ncol=1, fontsize=10)
    fig.text(.5, .035, 'Without replacement: dependent draws, Cov(Xᵣ, Xₛ) = −7/3 for r ≠ s.\n'
             'Coverage here counts observed population labels; it is not confidence-interval coverage.',
             ha='center', fontsize=10)
    fig.subplots_adjust(left=.075, right=.97, bottom=.29, top=.81, wspace=.28)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
