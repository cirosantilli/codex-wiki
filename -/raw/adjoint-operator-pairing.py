"""Illustrate how an adjoint transfers a measured direction.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG with the script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[2., 1.], [0., 1.]])
    x = np.array([1., 1.])
    y = np.array([1., 0.])
    image = a @ x
    measured_direction = a.T @ y
    value = image @ y
    assert np.isclose(value, x @ measured_direction)
    assert np.isclose(value, 3)

    blue, orange = '#286c9a', '#bd6426'
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.4), dpi=110,
                             facecolor='white')
    fig.subplots_adjust(left=.07, right=.98, bottom=.19, top=.72, wspace=.3)
    configurations = [
        (axes[0], x, measured_direction, r'$x=(1,1)$', r'$A^*y=(2,1)$',
         'Input space', r'$x_1$', r'$x_2$'),
        (axes[1], image, y, r'$Ax=(3,1)$', r'$y=(1,0)$',
         'Output space', r'$u_1$', r'$u_2$'),
    ]
    for ax, vector, direction, vector_label, direction_label, title, xlabel, ylabel in configurations:
        ax.set(xlim=(-.5, 3.8), ylim=(-.6, 2.8), aspect='equal',
               xlabel=xlabel, ylabel=ylabel, title=title)
        ax.axhline(0, color='#b9c1ca', lw=.8)
        ax.axvline(0, color='#b9c1ca', lw=.8)
        ax.grid(color='#e6e9ed', lw=.7)
        ax.set_xticks([0, 1, 2, 3])
        ax.set_yticks([0, 1, 2])
        for endpoint, color in [(vector, blue), (direction, orange)]:
            ax.annotate('', xy=endpoint, xytext=(0, 0),
                        arrowprops={'arrowstyle': '-|>', 'color': color,
                                    'lw': 2.5, 'mutation_scale': 15})
        ax.scatter(*vector, color=blue, s=40, zorder=4)
        ax.text(vector[0] - .06, vector[1] + .19, vector_label,
                fontsize=12, color=blue, ha='right' if ax is axes[0] else 'center',
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
        ax.text(direction[0] + .13, direction[1] - .19,
                direction_label, fontsize=12, color=orange,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
        ax.spines[['top', 'right']].set_visible(False)

    t = np.linspace(-.6, 2.8, 101)
    # Matching level sets: y . (A z) = (A* y) . z = 3.
    input_points = np.column_stack([(3 - t) / 2, t])
    assert np.allclose(input_points @ measured_direction, 3)
    assert np.allclose((input_points @ a.T) @ y, 3)
    axes[0].plot(input_points[:, 0], input_points[:, 1], '--',
                 color='#6d757e', lw=1.5, zorder=1)
    axes[1].axvline(3, ls='--', color='#6d757e', lw=1.5, zorder=1)
    axes[0].text(.38, 2.53, r'$2x_1+x_2=3$', fontsize=12,
                 bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    axes[1].text(3.1, 2.53, r'$u_1=3$', fontsize=12)

    fig.suptitle('The adjoint transfers the measurement', fontsize=17, y=.98)
    fig.text(.5, .885, r'$A=[2\ \ 1;\ 0\ \ 1]$', ha='center', fontsize=13)
    overlay = fig.add_axes([0, 0, 1, 1], frameon=False)
    overlay.set(xlim=(0, 1), ylim=(0, 1))
    overlay.axis('off')
    overlay.annotate('', xy=(.72, .815), xytext=(.28, .815),
                     arrowprops={'arrowstyle': '->', 'lw': 2, 'color': blue})
    overlay.text(.5, .83, r'$x\ \longmapsto\ Ax$', ha='center',
                 color=blue, fontsize=12)
    overlay.annotate('', xy=(.28, .765), xytext=(.72, .765),
                     arrowprops={'arrowstyle': '->', 'lw': 2, 'color': orange})
    overlay.text(.5, .778, r'$A^*y\ \longleftarrow\ y$', ha='center',
                 color=orange, fontsize=12)
    fig.text(.5, .095, r'$\langle Ax,y\rangle=3=\langle x,A^*y\rangle$',
             fontsize=16, ha='center')
    fig.text(.5, .035, 'Dashed lines: every point gives the same measured value 3.',
             fontsize=11, ha='center', color='#444d56')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
