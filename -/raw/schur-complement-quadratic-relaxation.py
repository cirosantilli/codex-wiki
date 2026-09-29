"""Contours and minimized profile of a stipulated quadratic form, not measured data."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2.5, 2.5, 401)
    y = np.linspace(-2.5, 2.5, 401)
    xx, yy = np.meshgrid(x, y)
    q = 2*xx**2+2*xx*yy+3*yy**2
    assert np.allclose(q, 2*(xx+yy/2)**2+2.5*yy**2)
    assert np.all(3*y**2 >= 2.5*y**2)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 4.4), dpi=125,
                                     layout='constrained', facecolor='white')
    cs = left.contour(xx, yy, q, levels=[1, 2, 4, 8, 12, 16, 24], colors='#8799ad')
    left.clabel(cs, inline=True, fontsize=9)
    left.plot(-y/2, y, color='#0072b2', linewidth=2.3, label=r'Minimizers: $x=-y/2$')
    left.axvline(0, color='#d55e00', linestyle='--', linewidth=1.7, label=r'Held at $x=0$')
    left.plot([-1, 0], [2, 2], ':', color='#555555', linewidth=1.5)
    left.scatter([-1, 0], [2, 2], c=['#0072b2', '#d55e00'], s=50, zorder=4)
    left.annotate('10', (-1, 2), xytext=(-1.45, 2.17), fontsize=11)
    left.annotate('12', (0, 2), xytext=(.14, 2.17), fontsize=11)
    left.set(xlabel=r'Eliminated variable $x$', ylabel=r'Retained variable $y$',
             title=r'Contours of $q=2x^2+2xy+3y^2$', aspect='equal')
    left.legend(loc='lower left', fontsize=9)
    right.plot(y, 3*y**2, '--', color='#d55e00', linewidth=2, label=r'$q(0,y)=3y^2$')
    right.plot(y, 2.5*y**2, color='#0072b2', linewidth=2.3,
               label=r'$\min_x q(x,y)=\frac{5}{2}y^2$')
    right.scatter([2, 2], [10, 12], c=['#0072b2', '#d55e00'], s=50, zorder=4)
    right.annotate('10', (2, 10), xytext=(1.4, 8.8), fontsize=11)
    right.annotate('12', (2, 12), xytext=(2.1, 12.6), fontsize=11)
    right.set(xlabel=r'Retained variable $y$', ylabel='Quadratic cost',
              title=r'Relaxing $x$ leaves $S=3-1\cdot 2^{-1}\cdot 1=5/2$')
    right.grid(alpha=.18); right.legend(loc='upper center', fontsize=10)
    fig.suptitle('The Schur complement keeps the effect of eliminated variables', fontsize=14)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
