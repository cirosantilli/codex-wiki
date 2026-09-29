"""Reveal a quadratic form's ellipse in an orthonormal eigenbasis.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Output an opaque PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[2., 1.], [1., 2.]])
    q = np.array([[1., -1.], [1., 1.]]) / np.sqrt(2)
    diagonal = np.diag([3., 1.])
    assert np.allclose(q.T @ q, np.eye(2))
    assert np.allclose(q.T @ a @ q, diagonal)
    assert np.allclose(a @ q, q @ diagonal)
    projections = [np.outer(q[:, j], q[:, j]) for j in range(2)]
    assert np.allclose(sum(projections), np.eye(2))
    assert np.allclose(projections[0] @ projections[1], np.zeros((2, 2)))
    assert np.allclose(3 * projections[0] + projections[1], a)
    assert np.allclose(9 * projections[0] + projections[1], a @ a)
    for projection in projections:
        assert np.allclose(projection.T, projection)
        assert np.allclose(projection @ projection, projection)
    angles = np.linspace(0, 2 * np.pi, 601)
    coordinates = np.column_stack([np.cos(angles) / np.sqrt(3), np.sin(angles)])
    points = coordinates @ q.T
    assert np.allclose(np.einsum('ni,ij,nj->n', points, a, points), 1)
    assert np.allclose(np.sum(points**2, axis=1), np.sum(coordinates**2, axis=1))
    for vector in [np.array([1., 0.]), np.array([1., 2.]), np.array([-3., .5])]:
        c = q.T @ vector
        assert np.isclose(vector @ a @ vector, 3 * c[0]**2 + c[1]**2)

    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.7), dpi=110, facecolor='white')
    colors = ['#b25235', '#286e98']
    for ax, curve, title, labels in zip(
            axes, [points, coordinates],
            ['Original coordinates', 'Orthonormal eigenvector coordinates'],
            [(r'$x_1$', r'$x_2$'), (r'$c$', r'$d$')]):
        ax.fill(*curve.T, color='#eef2f6')
        ax.plot(*curve.T, color='#3b5268', lw=2.6)
        ax.axhline(0, color='#a8afb7', lw=.9)
        ax.axvline(0, color='#a8afb7', lw=.9)
        ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), aspect='equal',
               xlabel=labels[0], ylabel=labels[1], title=title)
        ax.set_xticks([-1, -.5, 0, .5, 1])
        ax.set_yticks([-1, -.5, 0, .5, 1])
        ax.grid(color='#e2e5e8', lw=.6)
        ax.spines[['top', 'right']].set_visible(False)
        ax.tick_params(labelsize=10)
        ax.title.set_fontsize(12)
    for j, color in enumerate(colors):
        direction = q[:, j]
        axes[0].plot(*np.column_stack([-1.15 * direction, 1.15 * direction]),
                     color=color, ls='--', lw=1.2)
        axes[0].annotate('', xy=.95 * direction, xytext=(0, 0),
                         arrowprops={'arrowstyle': '->', 'color': color, 'lw': 2.2})
    axes[0].text(.72, .78, r'$e_+,\ \lambda=3$', fontsize=12, color=colors[0])
    axes[0].text(-1.18, .84, r'$e_-,\ \lambda=1$', fontsize=12, color=colors[1])
    axes[1].plot([-1/np.sqrt(3), 1/np.sqrt(3)], [0, 0], color=colors[0], lw=3)
    axes[1].plot([0, 0], [-1, 1], color=colors[1], lw=3)
    axes[1].annotate(r'$1/\sqrt{3}$', xy=(1/np.sqrt(3), 0), xytext=(.55, -.33),
                     fontsize=13, color=colors[0],
                     arrowprops={'arrowstyle': '->', 'color': colors[0]})
    axes[1].text(.08, .94, r'$1$', fontsize=13, color=colors[1])
    axes[0].text(.5, -.21, r'$2x_1^2+2x_1x_2+2x_2^2=1$',
                 transform=axes[0].transAxes, ha='center', fontsize=14)
    axes[1].text(.5, -.21, r'$3c^2+d^2=1$',
                 transform=axes[1].transAxes, ha='center', fontsize=14)
    fig.suptitle('The spectral theorem reveals the axes of a quadratic form', fontsize=16, y=.96)
    fig.text(.5, .025, 'The same ellipse in two coordinate systems: rotation preserves lengths and angles.',
             ha='center', fontsize=12)
    fig.subplots_adjust(left=.07, right=.97, bottom=.22, top=.84, wspace=.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
