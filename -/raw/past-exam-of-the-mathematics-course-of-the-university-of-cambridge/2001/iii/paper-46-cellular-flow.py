"""Unperturbed cellular streamlines; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Writes its basename PNG to the caller's working directory. The caller controls
MPLCONFIGDIR; this script does not create caches in the media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    low, high = -np.pi / 2, 3 * np.pi / 2
    grid = np.linspace(low, high, 321)
    x, y = np.meshgrid(grid, grid)
    psi = -np.sin(x) * np.sin(y)
    ux = np.sin(x) * np.cos(y)
    uy = -np.cos(x) * np.sin(y)
    fig, ax = plt.subplots(figsize=(7.6, 7.0), facecolor='white')
    ax.set_facecolor('white')
    ax.contour(x, y, psi, levels=[-.85, -.6, -.3, .3, .6, .85], colors='#8bb4d1', linewidths=1.05)
    ax.streamplot(grid, grid, ux, uy, density=.8, color='#62778a', linewidth=.55, arrowsize=.75)
    for coordinate in [0, np.pi]:
        ax.axhline(coordinate, color='#344451', linewidth=1.2)
        ax.axvline(coordinate, color='#344451', linewidth=1.2)
    stable, unstable = '#c77c19', '#27845b'
    for n in [0, 1]:
        for m in [0, 1]:
            p = np.array([n * np.pi, m * np.pi])
            h_unstable = (n + m) % 2 == 0
            for direction, is_unstable in [(np.array([1., 0.]), h_unstable), (np.array([0., 1.]), not h_unstable)]:
                for sign in [-1, 1]:
                    near, far = p + sign * .10 * direction, p + sign * .66 * direction
                    start, finish = (near, far) if is_unstable else (far, near)
                    ax.annotate('', xy=finish, xytext=start,
                                arrowprops={'arrowstyle': '-|>', 'lw': 2.1, 'color': unstable if is_unstable else stable})
            ax.plot(*p, marker='x', color='#912a36', ms=9, mew=2)
            ax.text(p[0] + .10, p[1] + .13, f'S{n}{m}', fontsize=10, color='#912a36',
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .92, 'pad': 1})
    ax.plot(np.pi / 2, np.pi / 2, marker='o', color='#245f95', ms=7)
    ax.text(np.pi / 2 + .12, np.pi / 2 + .08, 'centre', fontsize=10, color='#245f95')
    ticks = [low, 0, np.pi / 2, np.pi, high]
    labels = [r'$-\pi/2$', '$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$']
    ax.set_xticks(ticks, labels); ax.set_yticks(ticks, labels)
    ax.set(xlim=(low, high), ylim=(low, high), xlabel='$x$', ylabel='$y$', aspect='equal')
    ax.set_title(r'Cellular flow: $\psi_0=-\sin x\sin y$', fontsize=14, pad=12)
    ax.legend(handles=[Line2D([0], [0], color=stable, lw=2, label='stable: toward a saddle'),
                       Line2D([0], [0], color=unstable, lw=2, label='unstable: away from a saddle')],
              loc='upper center', bbox_to_anchor=(.5, -.10), ncol=2, fontsize=9, frameon=False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=135, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
