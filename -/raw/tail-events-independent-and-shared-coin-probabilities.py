"""Compare exact probabilities, not simulated frequencies (Python 3.14)."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.arange(1, 13)
    independent = 1 - np.exp2(-r.astype(float))
    shared = np.full(r.shape, 0.5)
    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=120, facecolor='white')
    ax.set_facecolor('white')
    fig.suptitle('At least one head in a window of r coordinates', fontsize=17, weight='bold', y=0.96)
    ax.plot(r, independent, 'o-', color='#1766a3', lw=2.4,
            label=r'Independent fair coins: $1-2^{-r}$', markersize=5)
    ax.plot(r, shared, 's-', color='#d16a13', lw=2.4,
            label=r'One shared fair coin: $1/2$', markersize=5)
    ax.axhline(1, color='#7c858f', ls='--', lw=1.2)
    ax.text(12.1, 1, '1', va='center', color='#555d66')
    ax.annotate('r = 3: 7/8', xy=(3, 0.875), xytext=(4.1, 0.75),
                arrowprops={'arrowstyle': '->', 'color': '#1766a3'}, fontsize=12, color='#1766a3')
    ax.text(6.4, 0.55, r'$X_j=Z$ for every $j$: no new chance', fontsize=12, color='#b45810')
    ax.set(xlim=(0.7, 12.6), ylim=(0, 1.06), xlabel='Window length r', ylabel='Exact model probability')
    ax.set_xticks([1, 2, 3, 4, 6, 8, 10, 12])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.grid(alpha=0.2)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='lower right', framealpha=1, facecolor='white', fontsize=11)
    fig.text(0.5, 0.035, 'Constructed probability curves • no measurements or simulation',
             ha='center', fontsize=11, color='#4c5662')
    fig.subplots_adjust(left=0.09, right=0.96, bottom=0.16, top=0.86)
    fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
