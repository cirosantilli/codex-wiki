"""Original two-ray comparison; Python 3.14, numpy and matplotlib.

Write the white PNG to cwd, normally the mirrored media directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    height = np.cosh(1.)
    # Bracket the smaller positive a root, avoiding the exact root a=1.
    low, high = .65, .8
    for _ in range(60):
        mid = (low+high)/2
        if mid*np.cosh(1/mid)>height:
            low=mid
        else:
            high=mid
    second = (low+high)/2
    assert abs(second*np.cosh(1/second)-height)<1e-13
    xx = np.linspace(-1, 1, 600)
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    for a, colour, style in [(1., '#166a9a', '-'), (second, '#b65b20', '--')]:
        time = a+a*a/2*np.sinh(2/a)
        ax.plot(xx, a*np.cosh(xx/a), color=colour, ls=style, lw=2.3,
                label=fr'$a={a:.6f}$, $T={time:.6f}$')
        ax.scatter([0], [a], s=20, color=colour)
    ax.scatter([-1, 1], [height, height], color='black', s=28, zorder=5)
    ax.axhline(0, color='black', lw=1)
    ax.text(-1.02, .06, r'$y=0$ is outside the medium', fontsize=10)
    ax.annotate(r'$(-1,\cosh 1)$', (-1, height), xytext=(-4, 11),
                textcoords='offset points', fontsize=11, ha='left')
    ax.annotate(r'$(1,\cosh 1)$', (1, height), xytext=(4, 11),
                textcoords='offset points', fontsize=11, ha='right')
    ax.set(xlim=(-1.15, 1.15), ylim=(-.04, 1.85), xlabel='$x$', ylabel='$y$',
           title=r'Two stationary rays: $y=a\cosh(x/a)$, speed $c(y)=1/y$')
    ax.legend(loc='lower center', bbox_to_anchor=(.5, .12), facecolor='white', framealpha=1)
    ax.grid(alpha=.15)
    fig.savefig(Path('paper-1-q9-two-catenary-rays.png'), dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
