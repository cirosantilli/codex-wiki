"""Original cylindrical basis sketch; Python 3.14, numpy and matplotlib.

Write the white PNG to cwd, normally the mirrored media directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    phi = np.deg2rad(32)
    er = np.array([np.cos(phi), np.sin(phi)])
    ep = np.array([-np.sin(phi), np.cos(phi)])
    point = 1.25*er
    fig, ax = plt.subplots(figsize=(7, 5.3), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    arc = np.linspace(0, 2*np.pi, 500)
    ax.plot(1.25*np.cos(arc), 1.25*np.sin(arc), color='0.85', lw=1)
    ax.annotate('', xy=(2.15, 0), xytext=(-0.25, 0), arrowprops={'arrowstyle': '->', 'color': 'black'})
    ax.annotate('', xy=(0, 1.95), xytext=(0, -0.25), arrowprops={'arrowstyle': '->', 'color': 'black'})
    ax.text(2.16, -.08, '$x$', fontsize=13)
    ax.text(-.12, 1.96, '$y$', fontsize=13)
    ax.plot([0, point[0]], [0, point[1]], '--', color='0.5', lw=1.1)
    ax.text(.48, .37, r'$\rho$', fontsize=13)
    theta = np.linspace(0, phi, 100)
    ax.plot(.42*np.cos(theta), .42*np.sin(theta), color='0.35')
    ax.text(.48, .09, r'$\phi$', fontsize=13)
    for direction, label, colour in [(er, r'$\mathbf{e}_\rho$', '#1671a3'),
                                      (ep, r'$\mathbf{e}_\phi$', '#b3581c')]:
        endpoint = point+.85*direction
        ax.annotate('', xy=endpoint, xytext=point,
                    arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': colour, 'mutation_scale': 15})
        ax.text(*(endpoint+.10*direction), label, fontsize=15, color=colour)
    ax.scatter(*point, s=105, facecolor='white', edgecolor='#333333', zorder=6)
    ax.scatter(*point, s=12, color='#333333', zorder=7)
    ax.annotate(r'$\mathbf{e}_z$: out of the plane', xy=point,
                xytext=(.55, 1.75), arrowprops={'arrowstyle': '-', 'color': '.35'}, fontsize=12)
    ax.text(-.17, -.16, '$O$', fontsize=12)
    ax.set(xlim=(-.45, 2.45), ylim=(-.35, 2.15), aspect='equal',
           title=r'Local cylindrical basis at $\phi=32^\circ$')
    ax.axis('off')
    fig.savefig(Path('paper-1-q1-cylindrical-basis.png'), dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
