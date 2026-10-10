"""Compare Gershgorin disk bounds before and after diagonal similarity scaling.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def add_disk(ax, center, radius, color):
    ax.add_patch(Circle((center, 0), radius, facecolor=color,
                        edgecolor='none', alpha=.14))
    ax.add_patch(Circle((center, 0), radius, fill=False,
                        edgecolor=color, linewidth=1.9))


def main():
    matrix = np.array([[2., 100.], [.01, 3.]])
    scaling = np.diag([100., 1.])
    transformed = np.linalg.solve(scaling, matrix @ scaling)
    eigenvalues = (5 + np.array([-1., 1.]) * np.sqrt(5)) / 2
    assert np.allclose(transformed, [[2, 1], [1, 3]])
    assert np.allclose(np.sort(np.linalg.eigvals(matrix)), eigenvalues)
    assert np.allclose(np.linalg.eigvalsh(transformed), eigenvalues)
    original_radii = np.abs(matrix).sum(axis=1) - np.abs(np.diag(matrix))
    scaled_radii = np.abs(transformed).sum(axis=1) - np.abs(np.diag(transformed))
    assert np.allclose(original_radii, [100, .01])
    assert np.allclose(scaled_radii, [1, 1])

    plt.rcParams.update({'font.size': 11})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 5.5), dpi=110,
                             facecolor='white')
    fig.subplots_adjust(left=.055, right=.985, bottom=.30, top=.77, wspace=.32)
    blue, orange, dark = '#287ba3', '#c47a23', '#17212d'
    for ax in axes:
        ax.axhline(0, color='#89929d', linewidth=.8, zorder=0)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel(r'Real part of $z$')
        ax.set_ylabel(r'Imaginary part of $z$')
        ax.spines[['top', 'right']].set_visible(False)

    ax = axes[0]
    add_disk(ax, 2, original_radii[0], blue)
    add_disk(ax, 3, original_radii[1], orange)
    ax.scatter(eigenvalues, [0, 0], color=dark, s=15, zorder=5)
    ax.add_patch(Rectangle((.6, -1.5), 3.8, 3, fill=False,
                           edgecolor=dark, linewidth=1, zorder=6))
    ax.annotate('Zoom window', xy=(4.4, 1.5), xytext=(25, 55),
                fontsize=10, arrowprops={'arrowstyle': '->', 'color': dark})
    ax.set(xlim=(-110, 114), ylim=(-112, 112), title='Original: full scale')
    ax.set_xticks([-100, 0, 100])
    ax.set_yticks([-100, 0, 100])
    ax.text(.5, -.34, 'Centres 2, 3; radii 100, 0.01', ha='center',
            transform=ax.transAxes, fontsize=10)

    ax = axes[1]
    # The large disk is rendered at its actual radius, clipped by the zoom.
    add_disk(ax, 2, original_radii[0], blue)
    add_disk(ax, 3, original_radii[1], orange)
    ax.annotate(r'$|z-3|\leq0.01$', xy=(3, .01), xytext=(2.5, 1.1),
                color=orange, ha='center',
                arrowprops={'arrowstyle': '->', 'color': orange})
    ax.text(2.5, -1.1, 'Radius-100 disk fills this zoom', color=blue,
            ha='center', fontsize=9)
    ax.set(xlim=(.6, 4.4), ylim=(-1.9, 1.9), title='Original: zoom')
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([-1, 0, 1])
    ax.text(.5, -.34, 'The tiny disk contains no eigenvalue', ha='center',
            transform=ax.transAxes, fontsize=10)

    ax = axes[2]
    add_disk(ax, 2, scaled_radii[0], blue)
    add_disk(ax, 3, scaled_radii[1], orange)
    ax.set(xlim=(.6, 4.4), ylim=(-1.9, 1.9), title='Scaled: same zoom')
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([-1, 0, 1])
    ax.text(.5, -.34, 'Centres 2, 3; both radii 1', ha='center',
            transform=ax.transAxes, fontsize=10)

    for ax in axes[1:]:
        ax.scatter(eigenvalues, [0, 0], color=dark, s=34, zorder=5)
        for value in eigenvalues:
            ax.text(value, -.42, f'{value:.6f}', ha='center',
                    fontsize=10, color=dark)

    fig.suptitle('Change coordinate scales; keep the eigenvalues',
                 fontsize=17, y=.98)
    fig.text(.5, .855,
             r'$A=[2\ \ 100;\ 0.01\ \ 3]\qquad D=\mathrm{diag}(100,1)'
             r'\qquad D^{-1}AD=[2\ \ 1;\ 1\ \ 3]$',
             ha='center', fontsize=13)
    fig.text(.5, .03, r'Black dots: $\lambda_\pm=(5\pm\sqrt{5})/2$ in every panel'
             '\nThe scaled symmetric matrix certifies real eigenvalues in [1, 4].',
             ha='center', fontsize=11, linespacing=1.6)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
