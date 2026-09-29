"""Plot separated Gershgorin disks and the independently computed eigenvalues.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    matrix = np.array([[2., .2, .1], [.2, 5., .3], [.1, .3, 9.]])
    centers = np.diag(matrix)
    radii = np.sum(np.abs(matrix), axis=1) - np.abs(centers)
    eigenvalues = np.linalg.eigvalsh(matrix)
    colors = ['#287ba3', '#c47a23', '#4e8b54']

    assert np.allclose(radii, [.3, .5, .4])
    for i in range(3):
        assert np.count_nonzero(np.abs(eigenvalues - centers[i]) <= radii[i]) == 1
        for j in range(i):
            assert abs(centers[i] - centers[j]) > radii[i] + radii[j]

    plt.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots(figsize=(10.8, 4.2), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.085, right=.97, bottom=.19, top=.77)
    ax.axhline(0, color='#89929d', linewidth=1, zorder=0)
    for i, (center, radius, value, color) in enumerate(
            zip(centers, radii, eigenvalues, colors), start=1):
        ax.add_patch(Circle((center, 0), radius, facecolor=color,
                            edgecolor='none', alpha=.15))
        ax.add_patch(Circle((center, 0), radius, fill=False,
                            edgecolor=color, linewidth=2))
        ax.plot([center - radius, center + radius], [0, 0],
                color=color, linewidth=3, alpha=.5)
        ax.scatter([center], [0], marker='+', s=110, color=color,
                   linewidth=1.8, zorder=4)
        ax.scatter([value], [0], s=25, color='#17212d', zorder=5)
        ax.annotate(f'$\\lambda_{i}={value:.6f}$', xy=(value, 0),
                    xytext=(center, .90), ha='center', fontsize=12,
                    arrowprops={'arrowstyle': '-', 'color': '#505b67',
                                'shrinkB': 6})
        ax.text(center, -.83, f'$D_{i}:$ centre {center:g}, radius {radius:g}',
                color=color, ha='center', fontsize=11)
        ax.text(center, -1.16,
                f'[{center - radius:g}, {center + radius:g}]',
                color=color, ha='center', fontsize=12)
    ax.set(xlim=(.3, 10.6), ylim=(-1.4, 1.3),
           xlabel=r'Real part of $z$', ylabel=r'Imaginary part of $z$')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_yticks([-1, 0, 1])
    ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Separated disks certify one eigenvalue each', fontsize=17, y=.97)
    fig.text(.5, .84, 'Symmetry puts every eigenvalue on the real axis',
             ha='center', fontsize=12, color='#505b67')
    fig.text(.5, .025, 'Shading: closed disks    +: diagonal entries    '
             'black dots: computed eigenvalues', ha='center', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
