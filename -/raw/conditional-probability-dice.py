"""Show exact conditional probabilities on the 36 ordered dice outcomes."""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np


def main():
    first, second = np.meshgrid(np.arange(1, 7), np.arange(1, 7))
    event_a = first + second >= 9
    event_b = first == 6
    both = event_a & event_b
    assert event_a.sum() == 10 and event_b.sum() == 6 and both.sum() == 4
    assert Fraction(int(both.sum()), int(event_b.sum())) == Fraction(2, 3)
    assert Fraction(int(both.sum()), int(event_a.sum())) == Fraction(2, 5)
    categories = event_a.astype(int) + 2 * event_b.astype(int)
    colors = ['#edf1f5', '#f3c277', '#9ac5e5', '#9e86c8']
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.8), layout='constrained',
                             facecolor='white', gridspec_kw={'width_ratios': [1.3, 1]})
    ax, summary = axes
    ax.imshow(categories, origin='lower', cmap=ListedColormap(colors),
              vmin=-.5, vmax=3.5, extent=(.5, 6.5, .5, 6.5))
    for x in range(1, 7):
        for y in range(1, 7):
            ax.text(x, y, f'{x + y}', ha='center', va='center', color='#18212b')
    ax.set(xticks=range(1, 7), yticks=range(1, 7), xlabel='First die', ylabel='Second die',
           title='36 equally likely ordered outcomes\nNumbers inside cells are the sums')
    ax.set_xticks(np.arange(.5, 7), minor=True)
    ax.set_yticks(np.arange(.5, 7), minor=True)
    ax.grid(which='minor', color='white', linewidth=2)
    ax.tick_params(which='minor', length=0)
    summary.axis('off')
    summary.text(0, .96, 'A: sum is at least 9\nB: first die is 6', va='top', fontsize=14)
    summary.legend(handles=[Patch(facecolor=colors[1], label='A only'),
                            Patch(facecolor=colors[2], label='B only'),
                            Patch(facecolor=colors[3], label='Both A and B'),
                            Patch(facecolor=colors[0], label='Neither')],
                   loc='upper left', bbox_to_anchor=(-.02, .76), frameon=False)
    summary.text(0, .40, 'Condition on B: retain 6 cells\n4 satisfy A, so P(A | B) = 2/3',
                 va='top', fontsize=13)
    summary.text(0, .22, 'Condition on A: retain 10 cells\n4 satisfy B, so P(B | A) = 2/5',
                 va='top', fontsize=13)
    summary.text(0, .04, 'Same overlap, different denominators', fontsize=12, color='#4a4a4a')
    fig.suptitle('Conditional probability restricts the outcome space', fontsize=16)
    fig.savefig(Path.cwd() / 'conditional-probability-dice.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
