"""Show the solution line and the single free coordinate of a rank-two system.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                         'mathtext.fontset': 'dejavusans'})
    x0 = np.array([-3, 2, 0])
    v = np.array([7, -3, 1])
    t = np.linspace(-0.5, 1.25, 150)
    affine = x0[:, None] + v[:, None]*t
    kernel = v[:, None]*t
    fig = plt.figure(figsize=(10.2, 4.9), facecolor='white')
    fig.suptitle('One free coordinate traces a whole solution line',
                 fontsize=18, fontweight='bold', y=0.98)
    ax = fig.add_subplot(121, projection='3d')
    ax.plot(*affine, color='#176b9c', lw=3,
            label=r'$x_0+t v$: $Ax=(1,4,5,3)^T$')
    ax.plot(*kernel, color='#75818b', lw=2, linestyle='--',
            label=r'$t v$: $Ax=0$')
    for point, label, offset in [(x0, r'$x_0$', (-1, 0.7, 0.08)),
                                 (x0+v, r'$x_0+v$', (-1.8, 0, 0.18))]:
        ax.scatter(*point, color='#176b9c', s=40, depthshade=False)
        ax.text(*(point+np.array(offset)), label, fontsize=11)
    ax.scatter(0, 0, 0, color='#75818b', s=25)
    ax.quiver(0, 0, 0, *x0, color='#b88010', lw=2,
              arrow_length_ratio=0.12)
    ax.text2D(0.04, -0.12, r'Gold arrow: translate by $x_0$',
              transform=ax.transAxes, color='#986900', fontsize=11)
    ax.set(xlabel='$x_1$', ylabel='$x_2$', zlabel='$x_3=t$',
           xlim=(-7, 9), ylim=(-4, 4), zlim=(-0.6, 1.6))
    ax.view_init(elev=21, azim=-61)
    ax.set_box_aspect((1.25, 1, 0.9))
    ax.tick_params(labelsize=9)
    ax.legend(loc='upper left', bbox_to_anchor=(-0.03, 1.05), fontsize=10,
              frameon=False)
    ax2 = fig.add_subplot(122)
    for values, color, label in zip(affine, ['#176b9c', '#b88010', '#6e4aa0'],
                                    [r'$x_1=-3+7t$', r'$x_2=2-3t$', r'$x_3=t$']):
        ax2.plot(t, values, color=color, lw=2.4, label=label)
        for tt in [0, 1]:
            ax2.scatter(tt, np.interp(tt, t, values), color=color, s=30, zorder=3)
    ax2.axvline(0, color='#aeb7be', lw=0.8, zorder=0)
    ax2.axvline(1, color='#aeb7be', lw=0.8, linestyle=':', zorder=0)
    ax2.axhline(0, color='#aeb7be', lw=0.8, zorder=0)
    ax2.set(xlabel='Free choice $t$', ylabel='Coordinate value', xlim=(-0.5, 1.25),
            ylim=(-7, 7), title='Every choice gives exactly one solution')
    ax2.legend(loc='upper left', fontsize=11, frameon=False)
    ax2.grid(alpha=0.16)
    ax2.spines[['top', 'right']].set_visible(False)
    fig.subplots_adjust(left=0.02, right=0.97, bottom=0.2, top=0.8, wspace=0.28)
    fig.text(0.5, 0.05,
             r'$x_0=(-3,2,0)^T,\quad v=(7,-3,1)^T,\quad Ax_0=(1,4,5,3)^T,\quad Av=0$',
             ha='center', fontsize=13)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
