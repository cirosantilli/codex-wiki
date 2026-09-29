#!/usr/bin/env python3
"""Original cavity geometry and exact field directions; output PNG to cwd.

Tested with Python3.14.4, NumPy2.3.5, Matplotlib3.10.7.
Dependencies are specified in the root pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def field(x, y):
    # Field inside the smaller void, in units C=4*pi*G*rho/3.
    dx = x - 0.5
    dist = np.hypot(dx, y)
    return 0.25 + 0.125 * dx / dist**3, 0.125 * y / dist**3


def main():
    x_eq = 0.5 - 1 / np.sqrt(2)
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 11})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), dpi=100, facecolor='white')
    ax = axes[0]
    ax.add_patch(Circle((0, 0), 1, fc='#e6e7ea', ec='#58606a', lw=1.8))
    ax.add_patch(Circle((0.5, 0), 0.5, fc='white', ec='#1466a3', lw=1.8))
    ax.add_patch(Circle((-0.25, 0), 0.25, fc='white', ec='#a45424', lw=1.8))
    ax.axhline(0, color='#888888', lw=0.7, zorder=0)
    ax.plot(x_eq, 0, marker='*', ms=12, color='#b31f37', zorder=5)
    ax.text(0.5, 0.16, r'$S_2$: large void', ha='center', fontsize=11)
    ax.text(-0.25, 0.31, r'$S_3$: small void', ha='center', color='#a45424', fontsize=10)
    ax.text(-0.64, 0.64, 'Uniform-density material', ha='center', fontsize=10)
    ax.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), xlabel=r'$x$', ylabel=r'$y$',
           title='Cross-section through both spherical voids', aspect='equal')
    ax = axes[1]
    ax.add_patch(Circle((-0.25, 0), 0.25, fc='#fcfaf6', ec='#a45424', lw=1.5))
    xx, yy = np.meshgrid(np.linspace(-0.49, -0.01, 14), np.linspace(-0.24, 0.24, 15))
    mask = (xx + 0.25)**2 + yy**2 < 0.24**2
    gx, gy = field(xx, yy)
    ax.quiver(xx[mask], yy[mask], gx[mask], gy[mask], color='#1466a3',
              angles='xy', scale_units='xy', scale=5.5, width=0.005, pivot='mid')
    ax.plot(x_eq, 0, marker='*', ms=15, color='#b31f37', zorder=5)
    ax.annotate(r'$x_* = 1/2-1/\sqrt{2}$', (x_eq, 0), xytext=(-0.49, 0.268),
                arrowprops={'arrowstyle': '->', 'color': '#b31f37'}, color='#b31f37', fontsize=11)
    ax.text(-0.49, -0.30, 'Axial: restoring.  Transverse: unstable.', fontsize=10)
    ax.set(xlim=(-0.53, 0.03), ylim=(-0.32, 0.32), xlabel=r'$x$', ylabel=r'$y$',
           title='Field directions inside the small void', aspect='equal')
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle('An unstable gravitational equilibrium in a spherical cavity', fontsize=15)
    fig.subplots_adjust(left=0.07, right=0.985, top=0.82, bottom=0.15, wspace=0.30)
    output = Path.cwd() / 'paper-3-cavity-equilibrium.png'
    fig.savefig(output, facecolor='white', transparent=False)
    plt.close(fig)
    assert output.is_file()


if __name__ == '__main__':
    main()
