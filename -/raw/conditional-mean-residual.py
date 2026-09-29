"""Show exact conditional-mean residuals; tested on Python 3.14."""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    outcomes = [Fraction(x) for x in (1, 3, 5, 11)]
    means = [Fraction(x) for x in (2, 2, 8, 8)]
    residuals = [x - m for x, m in zip(outcomes, means)]
    overall = sum(outcomes) / 4
    centered = [m - overall for m in means]
    products = [r * m for r, m in zip(residuals, centered)]
    mse = sum(r * r for r in residuals) / 4
    baseline = sum((x - overall) ** 2 for x in outcomes) / 4
    assert residuals == [-1, 1, -3, 3] and sum(residuals) == 0
    assert sum(residuals[:2]) == sum(residuals[2:]) == 0
    assert products == [3, -3, -9, 9] and sum(products) == 0
    assert mse == 5 and baseline == 14
    # Unequal weights: the four probabilities are 3/8, 3/8, 1/8, 1/8.
    weights = [Fraction(3, 8), Fraction(3, 8), Fraction(1, 8), Fraction(1, 8)]
    shifted_mean = sum(p * x for p, x in zip(weights, outcomes))
    shifted_within = sum(p * r * r for p, r in zip(weights, residuals))
    shifted_between = sum(p * (m - shifted_mean) ** 2 for p, m in zip(weights, means))
    shifted_total = sum(p * (x - shifted_mean) ** 2 for p, x in zip(weights, outcomes))
    assert shifted_mean == Fraction(7, 2) and shifted_within == 3
    assert shifted_between == Fraction(27, 4) and shifted_total == Fraction(39, 4)
    assert shifted_within + shifted_between == shifted_total
    print(f'residuals={residuals}; cross products={products}; covariance=0; '
          f'MSE={mse}, baseline={baseline}; unequal weights: '
          f'mean={shifted_mean}, within={shifted_within}, '
          f'between={shifted_between}, total={shifted_total}')

    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False})
    blue, orange = '#2878ac', '#c26916'
    fig, (ax, errors) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained',
                                    gridspec_kw={'width_ratios': [1.25, 1]},
                                    facecolor='white')
    for y, rs, color, label in ((1, residuals[:2], blue, 'A: errors -1, +1'),
                               (0, residuals[2:], orange, 'B: errors -3, +3')):
        values = list(map(float, rs))
        ax.plot(values, [y, y], color=color, lw=4, alpha=.45)
        ax.scatter(values, [y, y], color=color, s=80, zorder=3)
        ax.scatter(0, y, color=color, marker='D', s=65, zorder=4)
        ax.text(0, y - .23, label, ha='center', color=color)
    ax.axvline(0, color='#444444', ls='--', lw=1.5)
    ax.set(xlim=(-4, 4), ylim=(-.6, 1.5), xticks=np.arange(-3, 4),
           yticks=[0, 1], yticklabels=['Group B', 'Group A'],
           xlabel='Residual R = X - E[X | Y]', title='Both group error means are zero')
    errors.bar([0, 1], [float(baseline), float(mse)], width=.55,
               color=['#a4a4a4', blue])
    errors.text(0, 7, '14', ha='center', va='center', fontsize=15)
    errors.text(1, 2.5, '5', ha='center', va='center', color='white', fontsize=15)
    errors.annotate('Gain = 9', xy=(1, 14), xytext=(1, 9), ha='center', va='center',
                    arrowprops={'arrowstyle': '-|>', 'color': '#555555'})
    errors.set(xticks=[0, 1], xticklabels=['Predict 5', 'Predict group mean'],
               ylim=(0, 16), ylabel='Mean squared prediction error',
               title='Information improves prediction')
    errors.set_axisbelow(True)
    errors.yaxis.grid(alpha=.2)
    fig.suptitle('Uncorrelated residuals can still have group-dependent spread', fontsize=14)
    fig.savefig(Path.cwd() / 'conditional-mean-residual.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
