"""Original calculated contours of the dipole interaction; output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def energy(x, y):
    return -3*np.cos(x+y)-np.cos(x-y)


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(7.0, 5.7), layout='constrained')
    theta = np.linspace(0, np.pi, 601)
    x, y = np.meshgrid(theta, theta)
    u = energy(x, y)
    colors = ax.contourf(x, y, u, levels=np.linspace(-4, 4, 33), cmap='coolwarm', vmin=-4, vmax=4)
    lines = ax.contour(x, y, u, levels=[-3, -2, -1, 0, 1, 2, 3], colors='#343434', linewidths=.7)
    ax.clabel(lines, inline=True, fontsize=9, fmt='%g')
    # The odd grid includes the exact saddle coordinates (pi/2, pi/2).
    for point, marker, color, label in [((0, 0), 'o', '#123878', 'minima: U=-4'),
                                       ((np.pi, np.pi), 'o', '#123878', None),
                                       ((0, np.pi), '^', '#9b1d1d', 'maxima: U=4'),
                                       ((np.pi, 0), '^', '#9b1d1d', None),
                                       ((np.pi/2, np.pi/2), 'X', 'black', 'saddle: U=2')]:
        ax.scatter(*point, marker=marker, s=70, facecolor=color, edgecolor='white',
                   linewidth=.8, zorder=5, clip_on=False, label=label)
    ticks = [0, np.pi/2, np.pi]
    labels = ['0', r'$\pi/2$', r'$\pi$']
    ax.set(aspect='equal', xlim=(0, np.pi), ylim=(0, np.pi),
           xticks=ticks, yticks=ticks, xticklabels=labels, yticklabels=labels,
           xlabel=r'$\theta_1$', ylabel=r'$\theta_2$',
           title=r'$U=-3\cos(\theta_1+\theta_2)-\cos(\theta_1-\theta_2)$')
    ax.legend(loc='lower center', bbox_to_anchor=(.5, 1.025), ncol=3,
              fontsize=9, handletextpad=.35, columnspacing=.8, frameon=False)
    fig.colorbar(colors, ax=ax, label='$U$', ticks=[-4, -2, 0, 2, 4], shrink=.8)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
