"""Illustrate an exact entropy-achieving prefix code; save to the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    probabilities = np.array([0.5, 0.25, 0.125, 0.125])
    codewords = ['0', '10', '110', '111']
    lengths = np.array([len(word) for word in codewords])
    entropy = -np.dot(probabilities, np.log2(probabilities))
    mean_length = np.dot(probabilities, lengths)
    assert entropy == mean_length == 1.75
    assert all(not b.startswith(a) for a in codewords for b in codewords if a != b)

    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout='constrained')
    fig.set_facecolor('white')
    labels = ['A: 0', 'B: 10', 'C: 110', 'D: 111']
    colors = ['#2563a6', '#238a71', '#d47b25', '#9a51a3']
    axes[0].bar(labels, probabilities, color=colors, width=0.65)
    for i, p in enumerate(probabilities):
        axes[0].text(i, p + 0.012, '1/%d' % int(1/p), ha='center')
    axes[0].set(ylim=(0, 0.59), ylabel='Probability', title='Frequent symbols get short codewords')
    axes[0].tick_params(axis='x', labelrotation=15)

    xs = np.arange(4)
    axes[1].bar(xs - 0.18, lengths, width=0.36, color=colors, label='Prefix-code length')
    axes[1].bar(xs + 0.18, np.full(4, 2), width=0.36, color='#bdc7d4', label='Fixed length')
    axes[1].axhline(mean_length, color='#aa2626', linestyle='--', linewidth=2,
                   label='Mean prefix length = entropy = 1.75')
    axes[1].set(xticks=xs, xticklabels=['A', 'B', 'C', 'D'], ylim=(0, 3.75),
                ylabel='Bits per symbol', title='Long rare words still reduce the average')
    axes[1].legend(loc='upper left', fontsize=9)
    for ax in axes:
        ax.set_axisbelow(True)
        ax.grid(axis='y', alpha=0.22)
    fig.suptitle('A lossless binary prefix code: 12.5% shorter on average', fontsize=15)
    fig.savefig(Path.cwd() / 'entropy-prefix-code.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
