"""Original elliptic-coordinate diagram; Python 3.14, numpy and matplotlib.

Write the PNG to the current working directory (the mirrored media directory).
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(8, 5.5), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    v = np.linspace(0, 2 * np.pi, 1200)
    u0 = np.arccosh(np.sqrt(2))
    for u in [0.30, 0.60, u0, 1.20, 1.50, 1.80]:
        chosen = np.isclose(u, u0)
        ax.plot(np.cosh(u) * np.cos(v), np.sinh(u) * np.sin(v),
                color='#176a9e', lw=2.4 if chosen else 1.0,
                alpha=1 if chosen else 0.6,
                label=r'$u=\operatorname{arcosh}\sqrt{2}$' if chosen else None)
    u = np.linspace(0, 2.1, 800)
    for angle in np.arange(1, 12) * np.pi / 6:
        ax.plot(np.cosh(u) * np.cos(angle), np.sinh(u) * np.sin(angle),
                color='#b65d22', lw=1.0, ls='--', alpha=0.8)
    ax.plot([], [], color='#176a9e', lw=1, label=r'$u$ constant: ellipses')
    ax.plot([], [], color='#b65d22', lw=1, ls='--', label=r'$v$ constant: hyperbolae')
    ax.scatter([-1, 1], [0, 0], s=30, color='#252525', zorder=5)
    ax.annotate('focus $-1$', (-1, 0), xytext=(-36, -18), textcoords='offset points')
    ax.annotate('focus $+1$', (1, 0), xytext=(5, -18), textcoords='offset points')
    ax.axhline(0, color='0.75', lw=0.7, zorder=0)
    ax.axvline(0, color='0.75', lw=0.7, zorder=0)
    ax.set(xlim=(-3.3, 3.3), ylim=(-2.25, 2.25), xlabel='$x$', ylabel='$y$',
           title=r'$z=\cosh(u+iv)$: orthogonal confocal coordinates')
    ax.set_aspect('equal')
    ax.legend(loc='upper right', fontsize=9, facecolor='white', framealpha=0.95)
    fig.savefig(Path('paper-1-q7-elliptic-coordinates.png'), dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
