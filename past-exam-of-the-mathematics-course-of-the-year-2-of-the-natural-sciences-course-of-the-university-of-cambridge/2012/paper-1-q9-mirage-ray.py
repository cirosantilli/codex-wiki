"""Original catenary ray sketch; Python 3.14, numpy and matplotlib.

Write the white PNG to cwd, normally the mirrored media directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Plot dimensionless height X=beta*x against Y=beta*(y-y0).
    c = 1.4
    Y = np.linspace(-2.5, 2.5, 800)
    X = c * np.cosh(Y / c) - 1
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    ax.axhspan(-0.18, 0, color='#656565')
    ax.axhline(0, color='black', lw=1.2)
    ax.plot(Y, X, color='#146c9a', lw=2.6, label=r'$X=-1+c\cosh(Y/c),\quad c=1.4$')
    for start, end in [(-1.9, -1.65), (1.2, 1.45)]:
        ax.annotate('', xy=(end, c*np.cosh(end/c)-1),
                    xytext=(start, c*np.cosh(start/c)-1),
                    arrowprops={'arrowstyle': '->', 'lw': 2.2, 'color': '#146c9a'})
    ax.plot([0], [c-1], 'o', color='#146c9a', ms=5)
    ax.plot([-0.6, 0.6], [c-1, c-1], ':', color='#555555', lw=1)
    ax.annotate(r'minimum height $X_0=c-1>0$', xy=(0, c-1), xytext=(-0.9, 1.55),
                arrowprops={'arrowstyle': '-', 'color': '#555555'}, fontsize=10)
    ax.text(-2.4, 0.08, 'hot road: $X=0$', fontsize=10)
    ax.text(1.6, 0.65, 'index increases\nwith height', ha='center', fontsize=10)
    ax.annotate('', xy=(2.25, 1.65), xytext=(2.25, 0.4),
                arrowprops={'arrowstyle': '->', 'color': '#666666', 'lw': 1.3})
    ax.set(xlim=(-2.55, 2.55), ylim=(-0.18, 3.45),
           xlabel=r'horizontal position $Y=\beta(y-y_0)$',
           ylabel=r'height $X=\beta x$',
           title='A ray turns smoothly above the road')
    ax.legend(loc='upper center', framealpha=1, facecolor='white', fontsize=10)
    fig.savefig(Path('paper-1-q9-mirage-ray.png'), dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
