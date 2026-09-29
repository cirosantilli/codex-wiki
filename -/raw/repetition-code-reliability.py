"""Visualize three-bit majority decoding; save an opaque PNG in cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout='constrained', facecolor='white')
    ax = axes[0]
    groups = [('000', ['000', '001', '010', '100'], '#2563a6'),
              ('111', ['111', '110', '101', '011'], '#b74c2f')]
    for i, (center, words, color) in enumerate(groups):
        x = i * 1.9
        ax.text(x, 1.08, 'Decode to %d' % i, ha='center', va='center', color=color, fontsize=15)
        for j, word in enumerate(words):
            y = .83 - .23*j
            ax.text(x, y, word, ha='center', va='center', fontsize=18,
                    bbox={'boxstyle': 'round,pad=0.24', 'facecolor': '#eef2f6',
                          'edgecolor': color, 'linewidth': 2 if word == center else 1})
        ax.text(x, -.12, 'Original or one flipped bit', ha='center', fontsize=10)
    ax.set(xlim=(-.92, 2.82), ylim=(-.26, 1.35), title='All eight received words have a unique majority')
    ax.axis('off')

    q = np.linspace(0, .5, 501)
    coded = 3*q*q - 2*q*q*q
    assert np.isclose(3*.1**2 - 2*.1**3, .028)
    assert np.all(coded <= q + 1e-15)
    axes[1].plot(q, q, '--', color='#717b87', linewidth=2, label='Uncoded: q')
    axes[1].plot(q, coded, color='#2563a6', linewidth=2.5, label='Three-bit majority: 3q² - 2q³')
    axes[1].scatter([.1, .1], [.1, .028], color=['#717b87', '#2563a6'], zorder=3)
    axes[1].annotate('0.1 → 0.028', (.1, .028), xytext=(.19, .055),
                     arrowprops={'arrowstyle': '->'}, fontsize=11)
    axes[1].set(xlabel='Independent bit-flip probability q', ylabel='Decoded error probability',
                xlim=(0, .5), ylim=(0, .53), title='Improved reliability; rate drops to 1/3')
    axes[1].grid(alpha=.2)
    axes[1].legend(loc='upper left', fontsize=10)
    fig.suptitle('Three-bit repetition corrects one error, but not a common flip of all bits', fontsize=14)
    fig.savefig(Path.cwd() / 'repetition-code-reliability.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
