"""Plot exponential solutions, their initial-data area, and Abel evolution.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    blue, orange, green = '#2269a8', '#c65b18', '#28704e'
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.4))
    fig.subplots_adjust(left=0.065, right=0.975, bottom=0.22, top=0.76, wspace=0.45)
    fig.suptitle(r"One equation: $y''-y'-2y=0$", y=0.97, fontsize=17)
    x = np.linspace(-1, 0.8, 400)
    ax = axes[0]
    ax.plot(x, np.exp(-x), color=blue, lw=2.5, label=r'$y_1=e^{-x}$')
    ax.plot(x, np.exp(2*x), color=orange, lw=2.5, label=r'$y_2=e^{2x}$')
    ax.axvline(0, color='0.65', lw=1, ls=':')
    ax.scatter([0], [1], color='0.25', zorder=5, s=25)
    ax.set(xlabel=r'$x$', ylabel=r'$y$', title='Independent solution functions')
    ax.legend(loc='upper left', fontsize=10, frameon=False)
    ax.grid(alpha=0.18)

    ax = axes[1]
    ax.add_patch(Polygon([(0, 0), (1, -1), (2, 1), (1, 2)],
                         facecolor='#dce8f1', edgecolor='0.55', lw=1.2))
    for end, color in [((1, -1), blue), ((1, 2), orange)]:
        ax.annotate('', xy=end, xytext=(0, 0),
                    arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5})
    ax.text(1.06, -1.18, r'$(1,-1)$', color=blue, fontsize=10)
    ax.text(1.05, 2.1, r'$(1,2)$', color=orange, fontsize=10)
    ax.text(1.1, 0.25, r'$W(0)=3$', ha='center', fontsize=12)
    ax.axhline(0, color='0.65', lw=0.8)
    ax.axvline(0, color='0.65', lw=0.8)
    ax.set(xlim=(-0.4, 2.4), ylim=(-1.7, 2.7), xlabel='Value',
           ylabel='First derivative', title=r'Initial-data vectors at $x=0$')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([-1, 0, 1, 2])

    ax = axes[2]
    ax.plot(x, 3*np.exp(x), color=green, lw=2.5)
    ax.scatter([0], [3], color=green, zorder=5)
    ax.annotate(r'$W(0)=3$', xy=(0, 3), xytext=(-0.8, 4.6),
                arrowprops={'arrowstyle': '->', 'color': green}, color=green)
    ax.set(xlabel=r'$x$', ylabel=r'$W$', title=r"Abel: $W'=W$, so $W=3e^x$", ylim=(0, 7.1))
    ax.grid(alpha=0.18)
    fig.text(0.5, 0.065, 'A nonzero initial-data area allows value and derivative to be chosen independently.',
             ha='center', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
