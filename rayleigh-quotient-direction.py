"""Show the directional Rayleigh quotient for a symmetric two-by-two matrix.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Output an opaque PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
import numpy as np


def main():
    a = np.array([[2., 1.], [1., 2.]])
    q = np.array([[1., -1.], [1., 1.]]) / np.sqrt(2)
    theta = np.linspace(0, 2 * np.pi, 801)
    coefficients = np.column_stack([np.cos(theta), np.sin(theta)])
    directions = coefficients @ q.T
    rayleigh = np.einsum('ni,ij,nj->n', directions, a, directions)
    assert np.allclose(rayleigh, 1 + 2 * np.cos(theta)**2)
    assert np.allclose(np.sum(directions**2, axis=1), 1)
    assert np.isclose(rayleigh.max(), 3) and np.isclose(rayleigh.min(), 1)
    for vector, expected in [(np.array([1., 0.]), 2), (np.array([1., 1.]), 3),
                             (np.array([-1., 1.]), 1)]:
        value = vector @ a @ vector / (vector @ vector)
        assert np.isclose(value, expected)
        for scale in [-2., .3, 8.]:
            scaled = scale * vector
            assert np.isclose(scaled @ a @ scaled / (scaled @ scaled), value)
    eps = 1.e-3
    assert np.isclose((3 - (1 + 2 * np.cos(eps)**2)) / eps**2, 2, rtol=1.e-6)
    # A nonsymmetric matrix need not have its quotient between its eigenvalues.
    b = np.array([[1., 4.], [0., 1.]])
    assert np.allclose(np.linalg.eigvals(b), [1., 1.])
    v = np.ones(2)
    assert np.isclose(v @ b @ v / (v @ v), 3)
    # Independently check the quotient's gradient by perturbing its input.
    def quotient(vector):
        return vector @ a @ vector / (vector @ vector)

    for vector in [np.array([1., 0.]), np.array([1., 1.]),
                   np.array([-1., 1.]), np.array([2., 3.])]:
        gradient = 2 * (a @ vector - quotient(vector) * vector) / (vector @ vector)
        eps_gradient = 1.e-6
        numeric = np.array([
            (quotient(vector + eps_gradient * axis)
             - quotient(vector - eps_gradient * axis)) / (2 * eps_gradient)
            for axis in np.eye(2)])
        assert np.allclose(gradient, numeric, atol=1.e-9)
    nonsymmetric = np.array([[2., 1.], [0., 1.]])
    initial = np.array([-1., 1.]) / np.sqrt(2)
    assert np.allclose(nonsymmetric @ initial, initial)
    assert initial @ np.array([1., 0.]) != 0
    assert np.isclose(initial @ np.array([1., 1.]), 0)

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.6), dpi=110, facecolor='white',
                             gridspec_kw={'width_ratios': [1, 1.15]})
    norm = Normalize(1, 3)
    segments = np.stack([directions[:-1], directions[1:]], axis=1)
    collection = LineCollection(segments, cmap='viridis', norm=norm, linewidths=6)
    collection.set_array((rayleigh[:-1] + rayleigh[1:]) / 2)
    axes[0].add_collection(collection)
    for angle, label, offset in [(0, r'$e_+:\ R=3$', (.78, .92)),
                                  (np.pi/2, r'$e_-:\ R=1$', (-1.36, .94)),
                                  (np.pi/4, r'$q(\pi/4):\ R=2$', (.12, 1.22))]:
        point = np.array([np.cos(angle), np.sin(angle)]) @ q.T
        color = plt.colormaps['viridis'](norm(1 + 2 * np.cos(angle)**2))
        axes[0].annotate('', xy=point, xytext=(0, 0),
                         arrowprops={'arrowstyle': '->', 'lw': 2, 'color': color})
        axes[0].scatter(*point, c=[color], s=55, zorder=3)
        axes[0].text(*offset, label, fontsize=11.5,
                     bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    axes[0].set(xlim=(-1.5, 1.5), ylim=(-1.4, 1.4), aspect='equal',
                xlabel=r'$x_1$', ylabel=r'$x_2$',
                title='Directional values on the unit circle')
    axes[0].axhline(0, color='#bec3ca', lw=.8)
    axes[0].axvline(0, color='#bec3ca', lw=.8)
    axes[0].set_xticks([-1, 0, 1]); axes[0].set_yticks([-1, 0, 1])
    fig.colorbar(collection, ax=axes[0], shrink=.65, pad=.04, label=r'$R_A(q)$', ticks=[1, 2, 3])
    axes[1].plot(theta, rayleigh, color='#326c9d', lw=2.5)
    for level, label, color in [(1, r'$\lambda_{\min}=1$', '#855234'),
                               (3, r'$\lambda_{\max}=3$', '#537534')]:
        axes[1].axhline(level, ls='--', lw=1.2, color=color)
        axes[1].text(.03, level + .075, label, fontsize=12, color=color)
    axes[1].scatter([0, np.pi/4, np.pi/2], [3, 2, 1], color='#326c9d', s=35, zorder=4)
    axes[1].set(xlim=(-.04, 2 * np.pi + .04), ylim=(.75, 3.4),
                xlabel=r'$\theta$ measured from $e_+$', ylabel=r'$R_A(q(\theta))$',
                title=r'$R_A(q(\theta))=3\cos^2\theta+\sin^2\theta$')
    axes[1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
                       [r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    axes[1].set_yticks([1, 2, 3]); axes[1].grid(color='#e6e8ea', lw=.7)
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
        ax.title.set_fontsize(12)
    fig.suptitle('Eigenvalues bound the Rayleigh quotient in every direction', fontsize=16, y=.96)
    fig.text(.5, .865, r'$A=[2\ \ 1;\ 1\ \ 2]\qquad q(\theta)=\cos\theta\,e_++\sin\theta\,e_-$',
             ha='center', fontsize=14)
    fig.text(.5, .035, 'The quotient measures a direction, not its length; its extrema are eigendirections.',
             ha='center', fontsize=12)
    fig.subplots_adjust(left=.055, right=.975, bottom=.17, top=.77, wspace=.29)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
