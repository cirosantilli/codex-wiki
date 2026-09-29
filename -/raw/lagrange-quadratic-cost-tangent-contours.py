"""Render an original dimensionless equality-constrained quadratic example to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, (ax, right) = plt.subplots(1, 2, figsize=(12, 6), layout='constrained', facecolor='white')
    x = np.linspace(-1.4, 4.4, 450)
    y = np.linspace(-2, 4.4, 450)
    xx, yy = np.meshgrid(x, y)
    levels = [2, 4, 6, 9, 16]
    cs = ax.contour(xx, yy, xx**2 + 2*yy**2, levels=levels, colors='#a7a7a7', linewidths=1)
    ax.clabel(cs, fmt='%g', fontsize=10)
    ax.contour(xx, yy, xx**2 + 2*yy**2, levels=[6], colors=['#2375b9'], linewidths=2.4)
    ax.plot(x, 3-x, color='#d85b26', lw=2.4, label=r'Constraint $x+y=3$')
    ax.scatter([2], [1], c='#162f46', s=65, zorder=5)
    ax.annotate(r'$(2,1)$; cost $6$', (2, 1), xytext=(0.1, 2.4), arrowprops={'arrowstyle': '->'})
    ax.annotate('', xy=(3, 2), xytext=(2, 1), arrowprops={'arrowstyle': '->', 'color': '#2375b9', 'lw': 3})
    ax.annotate('', xy=(2.65, 1.65), xytext=(2, 1), arrowprops={'arrowstyle': '->', 'color': '#d85b26', 'lw': 1.6})
    ax.text(2.75, 2.2, r'$\nabla f/4=\nabla g=(1,1)$', fontsize=10, ha='center')
    ax.set(xlim=(-1.2, 4.2), ylim=(-1.5, 4.1), xlabel=r'$x$', ylabel=r'$y$', title='A minimum where contours touch')
    ax.set_aspect('equal')
    ax.legend(loc='lower left', fontsize=10)
    line = np.linspace(-0.5, 4.5, 350)
    cost = line**2 + 2*(3-line)**2
    right.plot(line, cost, c='#2375b9', lw=2.5, label=r'$x^2+2(3-x)^2$')
    right.axhline(6, c='#888888', ls=':', lw=1)
    right.scatter([2], [6], c='#162f46', s=65, zorder=4)
    right.annotate('Unique global minimum', (2, 6), xytext=(0.15, 19), arrowprops={'arrowstyle': '->'})
    right.text(2, 25, r'$3(x-2)^2+6$', ha='center', fontsize=16)
    right.set(xlim=(-0.5, 4.5), ylim=(0, 31), xlabel=r'$x$ along $y=3-x$', ylabel='Cost', title='Check the whole feasible line')
    right.legend(loc='upper right', fontsize=10)
    fig.suptitle('Lagrange multipliers: minimize $x^2+2y^2$ with $x+y=3$', fontsize=17)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
