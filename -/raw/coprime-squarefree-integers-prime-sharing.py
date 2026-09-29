"""Original exact prime-membership diagrams; Python 3.14, matplotlib 3.10.

Run from _media; the PNG is written to the current working directory.
No simulated measurements or probability estimates are used.
"""

from math import gcd
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def prime_support(n):
    """Trial division records each prime once, regardless of multiplicity."""
    support = set()
    candidate = 2
    while candidate * candidate <= n:
        if n % candidate == 0:
            support.add(candidate)
            while n % candidate == 0:
                n //= candidate
        candidate += 1
    if n > 1:
        support.add(n)
    return support


def main():
    panels = [
        ((8, 9), 'Coprime pair', 'gcd(8, 9) = 1', '#176b62'),
        ((6, 10, 15), 'Jointly, but not pairwise',
         'gcd(6, 10, 15) = 1\nPair gcds: 2, 3, 5', '#a24725'),
        ((4, 9, 25), 'Pairwise coprime', 'Every pair has gcd 1', '#176b62'),
    ]
    primes = (2, 3, 5)
    assert gcd(8, 9) == 1
    assert gcd(*panels[1][0]) == 1
    assert [gcd(6, 10), gcd(6, 15), gcd(10, 15)] == [2, 3, 5]
    assert all(gcd(a, b) == 1 for a, b in ((4, 9), (4, 25), (9, 25)))
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 4.8), facecolor='white')
    fig.subplots_adjust(left=0.06, right=0.98, top=0.77, bottom=0.21, wspace=0.3)
    fig.suptitle('Coprimality asks which primes are shared', fontsize=19, y=0.96)
    fig.text(0.5, 0.865, 'Exact prime membership: filled = divides; empty = does not divide',
             ha='center', fontsize=12, color='#444444')
    for ax, (entries, title, conclusion, color) in zip(axes, panels):
        ax.set_facecolor('white')
        ax.set_xlim(-1.05, 2.65)
        ax.set_ylim(-1.35, 3.15)
        ax.axis('off')
        ax.set_title(title, fontsize=13, color=color, pad=12, weight='bold')
        ax.text(-0.92, 2.7, 'n', ha='center', fontsize=13)
        for col, p in enumerate(primes):
            ax.text(col, 2.7, f'p = {p}', ha='center', fontsize=12)
        for row, n in enumerate(entries):
            y = 2.0 - row * 0.83
            support = prime_support(n)
            assert support <= set(primes)
            ax.text(-0.92, y, str(n), ha='center', va='center', fontsize=15)
            for col, p in enumerate(primes):
                present = p in support
                ax.add_patch(Rectangle((col - 0.32, y - 0.28), 0.64, 0.56,
                                       facecolor=color if present else 'white',
                                       edgecolor=color if present else '#b3bbc3', linewidth=1.3))
                if present:
                    ax.text(col, y, '1', ha='center', va='center', color='white', fontsize=13)
                else:
                    ax.text(col, y, '0', ha='center', va='center', color='#65717c', fontsize=13)
        ax.text(0.85, -0.9, conclusion, ha='center', va='center', fontsize=12, color=color)
    fig.text(0.5, 0.085, 'Joint: no column filled in every row.    Pairwise: no column filled in two rows.',
             ha='center', fontsize=12)
    output = Path(__file__).with_suffix('.png').name
    fig.savefig(output, dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
