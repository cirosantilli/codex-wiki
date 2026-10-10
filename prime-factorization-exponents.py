"""Show prime exponents, gcd/lcm, and all divisors of 360.

Run from _media: MPLBACKEND=Agg python ../prime-factorization-exponents.py
Writes the PNG in the working directory.
Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from math import gcd, lcm, prod
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    primes = (2, 3, 5, 7)
    rows = [(3, 2, 1, 0), (2, 1, 0, 1)]
    rows += [tuple(min(a, b) for a, b in zip(*rows)),
             tuple(max(a, b) for a, b in zip(*rows))]
    values = [prod(p**e for p, e in zip(primes, row)) for row in rows]
    assert values == [360, 84, gcd(360, 84), lcm(360, 84)]
    assert values[2:] == [12, 2520]
    layers = [[[2**a * 3**b * 5**c for a in range(4)] for b in range(3)]
              for c in range(2)]
    divisors = [d for layer in layers for row in layer for d in row]
    assert len(set(divisors)) == 24
    # Exhaustive division independently checks the exponent enumeration.
    assert sorted(divisors) == [d for d in range(1, 361) if 360 % d == 0]
    assert 360 % 72 == 0 and 360 % 48 != 0
    assert 12 * 2520 == 360 * 84 == 30240

    fig = plt.figure(figsize=(10, 7.4), dpi=110, facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=(1.25, 1), hspace=.65,
                           left=.085, right=.94, top=.83, bottom=.13, wspace=.38)
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(-2.7, 5.1), ylim=(-.15, 4.9))
    ax.axis('off')
    palette = ['#e5eff8', '#e5eff8', '#d6eddb', '#f8e6c5']
    labels = ['360', '84', 'gcd = 12', 'lcm = 2520']
    notes = ['2³ × 3² × 5', '2² × 3 × 7', 'Take each minimum', 'Take each maximum']
    ax.text(-.14, 4.5, 'Prime p:', ha='right', va='center', fontsize=12)
    for j, p in enumerate(primes):
        ax.text(j + .5, 4.5, str(p), ha='center', va='center',
                fontsize=14, fontweight='bold')
    for i, (row, label, note) in enumerate(zip(rows, labels, notes)):
        y = 3 - i
        ax.text(-.18, y + .45, label, ha='right', va='center',
                fontsize=13, fontweight='bold')
        ax.text(4.13, y + .45, note, ha='left', va='center', fontsize=11)
        for j, e in enumerate(row):
            ax.add_patch(Rectangle((j + .04, y + .05), .92, .8,
                                  facecolor=palette[i], edgecolor='white'))
            ax.text(j + .5, y + .45, str(e), ha='center', va='center',
                    fontsize=16, color='#84909c' if e == 0 else '#263e51')
    ax.set_title('Exponents at each prime determine gcd and lcm', fontsize=14, pad=6)

    for c in range(2):
        ax = fig.add_subplot(grid[1, c])
        ax.set(xlim=(-.8, 4), ylim=(-.05, 3.7), aspect='equal')
        ax.axis('off')
        ax.set_title(f'All divisors 2ᵃ 3ᵇ 5ᶜ with c = {c}', fontsize=13, pad=10)
        ax.text(2, 3.48, 'Exponent a of 2', ha='center', fontsize=10)
        ax.text(-.74, 1.5, 'Exponent b of 3', va='center', ha='center',
                rotation=90, fontsize=10)
        for a in range(4):
            ax.text(a + .5, 3.1, str(a), ha='center', fontsize=11)
        for b in range(3):
            y = 2 - b
            ax.text(-.22, y + .5, str(b), ha='center', va='center', fontsize=11)
            for a in range(4):
                ax.add_patch(Rectangle((a + .035, y + .035), .93, .93,
                                      facecolor='#edf4fa' if c == 0 else '#e2f0e5',
                                      edgecolor='white'))
                ax.text(a + .5, y + .5, str(layers[c][b][a]),
                        ha='center', va='center', fontsize=13)
    fig.suptitle('Prime factorization gives a complete set of multiplicative coordinates',
                 fontsize=16, y=.975)
    fig.text(.5, .918, '360 = 2³ × 3² × 5     and     84 = 2² × 3 × 7',
             ha='center', fontsize=14)
    fig.text(.5, .045, 'Two layers × three rows × four columns = 24 divisors.  '
             'Each divisor appears exactly once.', ha='center', fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
