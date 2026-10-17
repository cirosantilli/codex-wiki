"""Quadratic contour models. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    grid = np.linspace(-1.6, 1.6, 501)
    x, y = np.meshgrid(grid, grid)
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.65), dpi=120, layout='constrained')
    models = [(-x*x-y*y, 'Maximum', r'$f-f_0=-X^2-Y^2$', [-2, -1, -.25]),
              (x*x+y*y, 'Minimum', r'$f-f_0=X^2+Y^2$', [.25, 1, 2]),
              (x*x-y*y, 'Saddle', r'$f-f_0=X^2-Y^2$', [-2, -1, -.25, .25, 1, 2])]
    for ax, (z, name, formula, levels) in zip(axes, models):
        cs = ax.contour(x, y, z, levels=levels, cmap='coolwarm', vmin=-2, vmax=2, linewidths=1.5)
        ax.clabel(cs, fmt='%g', fontsize=8)
        if name == 'Saddle':
            ax.plot(grid, grid, '--', color='#63348c', lw=1.5)
            ax.plot(grid, -grid, '--', color='#63348c', lw=1.5)
            ax.text(1.05, 1.23, '0', color='#63348c')
        ax.scatter([0], [0], c='black', s=23, zorder=5)
        ax.axhline(0, c='.75', lw=.65, zorder=0)
        ax.axvline(0, c='.75', lw=.65, zorder=0)
        ax.set(xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), xlabel='X', ylabel='Y', title=f'{name}\n{formula}', xticks=[-1, 0, 1], yticks=[-1, 0, 1])
        ax.set_aspect('equal')
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
