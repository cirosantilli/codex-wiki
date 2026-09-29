"""Original exact fair-coin limit curves; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes its own PNG basename to the current working directory.
No sampling or experimental data: points are exact model probabilities.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(1, 11)
    tail = 2.0 ** (-n)
    success = 1 - tail
    blue, orange = '#246ca6', '#c76624'
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.7), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.09, right=0.96, bottom=0.27, top=0.72, wspace=0.30)
    fig.suptitle('Finite waiting horizons and the infinite limit', fontsize=16, y=0.97)
    fig.text(0.5, 0.865, r'$A_n$: head by toss $n$;   $B_n=A_n^c$: first $n$ tosses all tails',
             ha='center', fontsize=12)
    ax = axes[0]
    ax.axhline(1, color=blue, linewidth=1, linestyle='--', alpha=0.65)
    ax.axhline(0, color=orange, linewidth=1, linestyle='--', alpha=0.65)
    ax.scatter(n, success, color=blue, label=r'$P(A_n)=1-2^{-n}$', s=30, zorder=3)
    ax.scatter(n, tail, color=orange, label=r'$P(B_n)=2^{-n}$', s=30, zorder=3)
    ax.set_title('One probability scale', fontsize=12)
    ax.set_ylim(-0.045, 1.045)
    ax.set_ylabel('Probability')
    ax.legend(loc='center right', fontsize=10, framealpha=1)
    ax = axes[1]
    ax.scatter(n, tail, color=orange, s=30, zorder=3)
    ax.set_yscale('log', base=2)
    ax.set_ylim(2**-11, 1)
    ax.set_yticks([2**-1, 2**-4, 2**-7, 2**-10], ['1/2', '1/16', '1/128', '1/1024'])
    ax.set_title('Tail detail (logarithmic scale)', fontsize=12)
    ax.set_ylabel(r'$P(B_n)$')
    ax.annotate('Ten tosses: 1/1024', xy=(10, 2**-10), xytext=(4.0, 2**-9),
                fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#444444'})
    for ax in axes:
        ax.set_xlim(0.5, 10.5)
        ax.set_xticks([1, 2, 4, 6, 8, 10])
        ax.set_xlabel(r'Finite number of tosses $n$')
        ax.grid(alpha=0.2)
        ax.spines[['top', 'right']].set_visible(False)
    fig.text(0.5, 0.10, r'As $n\to\infty$: $P(\bigcup_n A_n)=1$,  $P(\bigcap_n B_n)=0$ (the all-tails sequence remains).',
             ha='center', fontsize=11)
    fig.text(0.5, 0.04, 'Independent fair-coin model. Dots are exact probabilities at integer n, not experimental observations.',
             ha='center', fontsize=10, color='#444444')
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
