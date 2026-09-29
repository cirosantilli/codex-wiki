"""Show one vector in Cartesian and oblique bases; write the PNG to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, label=None, label_offset=(0, 0)):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.4,
                            'mutation_scale': 16})
    if label:
        midpoint = (np.asarray(start) + end)/2 + np.asarray(label_offset)
        ax.text(*midpoint, label, color=color, fontsize=12,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .8})


def main():
    plt.rcParams.update({'font.size': 12})
    basis = np.array([[2., 1.], [1., 2.]])
    vector = np.array([5., 4.])
    coefficients = np.linalg.solve(basis, vector)
    assert np.allclose(coefficients, [2, 1])
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.3), layout='constrained', facecolor='white')
    colors = ['#2670aa', '#cd6523', '#228268']
    for ax in axes:
        ax.axhline(0, color='#7c838a', lw=.8)
        ax.axvline(0, color='#7c838a', lw=.8)
        ax.set(xlim=(-.7, 6.2), ylim=(-.7, 5.2), xlabel='x', ylabel='y', aspect='equal')
        ax.set_xticks(range(0, 7))
        ax.set_yticks(range(0, 6))
        arrow(ax, [0, 0], vector, colors[2])
        ax.scatter(*vector, color=colors[2], zorder=4)
        ax.text(4.85, 4.18, 'v = (5, 4)', color=colors[2], fontsize=12, ha='right')
    axes[0].grid(alpha=.2)
    arrow(axes[0], [0, 0], [5, 0], colors[0], r'$5e_1$', (-.3, .15))
    arrow(axes[0], [5, 0], vector, colors[1], r'$4e_2$', (.12, 0))
    axes[0].plot([0, 5], [4, 4], '--', color='#b0b6be')
    axes[0].plot([0, 0], [0, 4], '--', color='#b0b6be')
    axes[0].set_title(r'Cartesian basis: $v=5e_1+4e_2$')

    b1, b2 = basis[:, 0], basis[:, 1]
    for coefficient in range(-3, 5):
        t = np.array([-4, 5])
        line1 = coefficient*b1[:, None] + t*b2[:, None]
        line2 = coefficient*b2[:, None] + t*b1[:, None]
        axes[1].plot(*line1, color='#dce3e9', lw=.8, zorder=0)
        axes[1].plot(*line2, color='#dce3e9', lw=.8, zorder=0)
    arrow(axes[1], [0, 0], 2*b1, colors[0], r'$2b_1$', (0, -.4))
    arrow(axes[1], 2*b1, vector, colors[1], r'$b_2$', (.12, -.3))
    axes[1].plot([0, b2[0], vector[0]], [0, b2[1], vector[1]], '--', color='#a6afb8')
    axes[1].scatter(*b1, color=colors[0], s=30)
    axes[1].text(2.08, 1.16, r'$b_1=(2,1)$', color=colors[0], fontsize=10)
    axes[1].text(.05, 2.05, r'$b_2=(1,2)$', color=colors[1], fontsize=10)
    axes[1].set_title(r'Oblique basis: $v=2b_1+b_2$')
    fig.suptitle('Coordinates change; the underlying vector stays the same', fontsize=16)
    fig.savefig(Path.cwd() / 'vector-basis-coordinates.png', dpi=120, facecolor='white', bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
