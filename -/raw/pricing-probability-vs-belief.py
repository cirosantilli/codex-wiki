"""Original comparison of physical expectation and replication price.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from _media; the PNG output basename is written into the current directory.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    gross = Fraction(21, 20)
    q = Fraction(5, 8)
    price = q * 20 / gross
    assert price == Fraction(250, 21)
    assert Fraction(1, 2) * 20 / gross == Fraction(200, 21)
    assert Fraction(4, 5) * 20 / gross == Fraction(320, 21)
    p = np.linspace(.001, .999, 401)
    plt.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots(figsize=(8, 5), layout='constrained', facecolor='white')
    ax.plot(p, 20 * p / float(gross), color='#b76816', linewidth=2.5,
            label=r'Discounted physical expectation $20p/1.05$')
    ax.axhline(float(price), color='#2563a6', linewidth=2.5,
               label=r'Replication price $250/21$')
    ax.axvline(float(q), color='#777777', linestyle='--', linewidth=1.2)
    ax.scatter([float(q)], [float(price)], color='#2563a6', s=45, zorder=4)
    ax.text(.64, 8.8, 'They coincide at\np = q = 0.625', color='#444444', fontsize=11)
    for belief, exact, offset in [(.5, '200/21 ≈ 9.52', (-135, -40)),
                                 (.8, '320/21 ≈ 15.24', (-145, 22))]:
        value = 20 * belief / float(gross)
        ax.scatter([belief], [value], color='#b76816', s=35, zorder=4)
        ax.annotate(f'p = {belief}: {exact}', (belief, value), xytext=offset,
                    textcoords='offset points', fontsize=11,
                    arrowprops={'arrowstyle': '->', 'color': '#777777'})
    ax.set(xlim=(0, 1), ylim=(0, 21), xlabel='Physical up probability p (0 < p < 1)',
           ylabel='Amount at time zero', title='Beliefs change expectations; replication fixes the price')
    ax.grid(alpha=.18)
    ax.legend(loc='upper left', fontsize=11)
    fig.savefig(Path.cwd() / 'pricing-probability-vs-belief.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
