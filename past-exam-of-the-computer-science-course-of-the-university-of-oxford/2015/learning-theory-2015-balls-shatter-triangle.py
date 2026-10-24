"""Draw eight ball labellings; tested with the root pyproject.toml environment.

Run from any output directory. The PNG is written to the current directory.
"""
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    angles = np.deg2rad([90, 210, 330])
    vertices = np.column_stack((np.cos(angles), np.sin(angles)))
    interpolation = np.column_stack((vertices, np.ones(3)))
    fig, axes = plt.subplots(2, 4, figsize=(11.2, 6.2), layout='constrained')
    fig.patch.set_facecolor('white')
    for ax, bits in zip(axes.flat, product((0, 1), repeat=3)):
        signs = 2 * np.array(bits) - 1
        a_x, a_y, intercept = np.linalg.solve(interpolation, signs)
        a = np.array([a_x, a_y])
        eta = 0.75
        centre = eta * a / 2
        radius_squared = 1 + eta * intercept + centre @ centre
        assert radius_squared > 0
        scores = radius_squared - np.sum((vertices - centre) ** 2, axis=1)
        assert np.allclose(scores, eta * signs)
        ax.add_patch(Circle(centre, np.sqrt(radius_squared), facecolor='#e0effb',
                            edgecolor='#3976a8', linewidth=1.5))
        for index, (vertex, bit) in enumerate(zip(vertices, bits)):
            if bit:
                ax.scatter(*vertex, c='#1269a8', s=60, zorder=3)
            else:
                ax.scatter(*vertex, c='#bd3838', marker='x', linewidths=2, s=65, zorder=3)
            ax.annotate(str(index), vertex, xytext=(5, 5), textcoords='offset points', fontsize=9)
        ax.set(xlim=(-1.9, 1.9), ylim=(-1.9, 1.9), aspect='equal')
        ax.set_title('Labels: ' + ''.join(map(str, bits)), fontsize=12)
        ax.axis('off')
    fig.suptitle('Every labelling of three fixed points is realized by a disk', fontsize=15)
    fig.savefig(Path.cwd() / 'learning-theory-2015-balls-shatter-triangle.png', dpi=100,
                facecolor='white', transparent=False, metadata={'Software': 'Matplotlib'})
    plt.close(fig)


if __name__ == '__main__':
    main()
