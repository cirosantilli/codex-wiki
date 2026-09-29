"""Plot a projection, perpendicular residual and distance curve; save to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12})
    vector = np.array([1., 3.])
    direction = np.array([2., 1.])
    alpha = np.dot(vector, direction)/np.dot(direction, direction)
    projected = alpha*direction
    residual = vector-projected
    assert np.allclose(projected, [2, 1])
    assert np.isclose(np.dot(residual, direction), 0)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.1), layout='constrained', facecolor='white')
    line_parameter = np.array([-.4, 2])
    axes[0].plot(*(direction[:, None]*line_parameter), color='#a4aeb8', lw=2,
                 label=r'$F=\operatorname{span}(2,1)$')
    for start, end, color in [([0, 0], vector, '#2772aa'),
                              ([0, 0], projected, '#d47222'),
                              (projected, vector, '#218466')]:
        axes[0].annotate('', xy=end, xytext=start,
                         arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5})
    axes[0].scatter(*vector, color='#2772aa', zorder=4)
    axes[0].scatter(*projected, color='#d47222', zorder=4)
    axes[0].text(.22, 3.12, 'v = (1, 3)', color='#2772aa')
    axes[0].text(2.02, .75, 'Pv = (2, 1)', color='#d47222')
    axes[0].text(1.7, 2.45, 'r = (-1, 2)', color='#218466')
    unit_direction = direction/np.linalg.norm(direction)
    unit_residual = residual/np.linalg.norm(residual)
    marker = np.array([projected + .16*unit_direction,
                       projected + .16*(unit_direction+unit_residual),
                       projected + .16*unit_residual])
    axes[0].plot(*marker.T, color='#555b61', lw=1)
    axes[0].set(xlim=(-.8, 4.3), ylim=(-.7, 3.7), aspect='equal',
                xlabel='x', ylabel='y', title='The residual is perpendicular to the line')
    axes[0].axhline(0, color='#a7afb7', lw=.8)
    axes[0].axvline(0, color='#a7afb7', lw=.8)
    axes[0].grid(alpha=.18)
    axes[0].legend(loc='lower right', fontsize=10)

    a = np.linspace(-.3, 2.3, 401)
    distances = ((vector[:, None]-direction[:, None]*a)**2).sum(axis=0)
    assert np.allclose(distances, 5+5*(a-1)**2)
    axes[1].plot(a, distances, color='#2772aa', lw=2.5)
    axes[1].scatter([1], [5], color='#d47222', zorder=3)
    axes[1].annotate('Unique minimum: a = 1, squared error = 5', (1, 5),
                     xytext=(.0, 11), arrowprops={'arrowstyle': '->'}, fontsize=10)
    axes[1].set(xlabel=r'Coefficient $a$ in candidate $au$', ylabel=r'$\|v-au\|^2$',
                title=r'Pythagorean identity: $5+5(a-1)^2$', ylim=(0, 15))
    axes[1].grid(alpha=.2)
    fig.suptitle('Nearest-point approximation is an orthogonal decomposition', fontsize=15)
    fig.savefig(Path.cwd() / 'orthogonal-projection-geometry.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
