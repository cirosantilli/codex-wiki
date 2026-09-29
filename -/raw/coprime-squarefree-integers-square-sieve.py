"""Original exact finite square-divisor sieve; Python 3.14, matplotlib 3.10.

Run from _media; the PNG is written to the current working directory.
Every exclusion displays its smallest prime-square divisor.
"""

from math import isqrt
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


def primes_through(bound):
    return [p for p in range(2, bound + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def main():
    bound = 60
    primes = primes_through(isqrt(bound))
    assert primes == [2, 3, 5, 7]
    witnesses = {n: next((p * p for p in primes if n % (p * p) == 0), None)
                 for n in range(1, bound + 1)}
    count = sum(w is None for w in witnesses.values())
    assert count == 37
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(9.6, 6.5), facecolor='white')
    fig.subplots_adjust(left=0.045, right=0.985, top=0.79, bottom=0.19)
    green, red = '#d5eee5', '#f8ded3'
    dark_green, dark_red = '#12574e', '#8f321e'
    fig.suptitle('Square-free means no repeated prime factor', fontsize=19, y=0.96)
    fig.text(0.5, 0.89, 'Exact enumeration for 1–60: test prime squares 4, 9, 25, 49',
             ha='center', fontsize=12)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    for n, witness in witnesses.items():
        col = (n - 1) % 10
        y = 5 - (n - 1) // 10
        squarefree = witness is None
        ax.add_patch(Rectangle((col + 0.04, y + 0.045), 0.92, 0.91,
                               facecolor=green if squarefree else red,
                               edgecolor='white', linewidth=1))
        color = dark_green if squarefree else dark_red
        ax.text(col + 0.5, y + (0.51 if squarefree else 0.64), str(n),
                ha='center', va='center', fontsize=16, color=color, weight='bold')
        if witness is not None:
            ax.text(col + 0.5, y + 0.28, f'{witness} | {n}',
                    ha='center', va='center', fontsize=10, color=dark_red)
    fig.legend(handles=[Patch(facecolor=green, label=f'Square-free: {count} integers'),
                        Patch(facecolor=red, label='Excluded: a displayed square divides n')],
               loc='lower center', bbox_to_anchor=(0.5, 0.09), ncol=2,
               frameon=False, fontsize=11)
    fig.text(0.5, 0.04, '6 and 10 are square-free; their product 60 is not, because 2 occurs twice.',
             ha='center', fontsize=12)
    output = Path(__file__).with_suffix('.png').name
    fig.savefig(output, dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
