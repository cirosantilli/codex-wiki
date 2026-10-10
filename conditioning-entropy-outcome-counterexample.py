"""Plot an exact outcome-wise entropy counterexample in the current directory.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def entropy(probabilities):
    positive = np.asarray(probabilities)[np.asarray(probabilities) > 0]
    return max(0.0, -np.dot(positive, np.log2(positive)))


def main():
    joint = np.array([[0.8, 0.1], [0.0, 0.1]])
    marginal = joint.sum(axis=1)
    weights = joint.sum(axis=0)
    conditional = joint / weights
    distributions = [marginal, conditional[:, 0], conditional[:, 1]]
    entropies = np.array([entropy(p) for p in distributions])
    average = np.dot(weights, entropies[1:])
    assert np.isclose(average, 0.2)
    assert entropies[1] == 0 and entropies[2] == 1
    assert average < entropies[0] < entropies[2]

    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig = plt.figure(figsize=(10, 6.5), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 3, height_ratios=[1, 1.1])
    headings = ['Before any report', 'Common report: Y = 0', 'Rare report: Y = 1']
    fractions = [['9/10', '1/10'], ['1', '0'], ['1/2', '1/2']]
    for column, (p, heading) in enumerate(zip(distributions, headings)):
        ax = fig.add_subplot(grid[0, column])
        ax.bar([0, 1], p, color=['#2862a5', '#db802e'], width=0.55)
        for x, probability in enumerate(p):
            ax.text(x, probability + 0.04, fractions[column][x], ha='center')
        ax.set(xticks=[0, 1], xticklabels=['X = 0', 'X = 1'], ylim=(0, 1.25),
               title=heading, ylabel='Probability' if column == 0 else '')
        ax.set_yticks([0, 0.5, 1])
        ax.grid(axis='y', alpha=0.18)
        ax.set_axisbelow(True)
        ax.text(0.5, -0.22, f'Entropy = {entropies[column]:.6g} bits',
                transform=ax.transAxes, ha='center')

    ax = fig.add_subplot(grid[1, :])
    values = [entropies[0], 0, 1, average]
    ax.bar(np.arange(4), values, color=['#526e8c', '#2862a5', '#db802e', '#26866f'],
           width=0.56)
    for x, value in enumerate(values):
        ax.text(x, value + 0.035, f'{value:.6g}', ha='center', weight='bold')
    ax.set(xticks=np.arange(4),
           xticklabels=['Before report', 'Given Y = 0\n(weight 4/5)',
                        'Given Y = 1\n(weight 1/5)', 'Weighted average\nafter report'],
           ylim=(0, 1.4), ylabel='Entropy (bits)')
    ax.grid(axis='y', alpha=0.18)
    ax.set_axisbelow(True)
    ax.text(0.5, 0.95, '(4/5) × 0 + (1/5) × 1 = 1/5 bit',
            transform=ax.transAxes, ha='center', va='top',
            bbox={'facecolor': 'white', 'edgecolor': '#d2d9df', 'pad': 6})
    fig.suptitle('A rare observation increases uncertainty; the average decreases',
                 fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
