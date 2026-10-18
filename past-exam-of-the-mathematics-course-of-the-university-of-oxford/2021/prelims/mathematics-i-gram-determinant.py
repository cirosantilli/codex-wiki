"""Original Oxford 2021 Mathematics I Q4 illustration.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7;
see the repository pyproject.toml. Writes an opaque white PNG to the cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.6, 3.4), layout='constrained')
    v1 = np.array([0.9, 1.25])
    v2 = np.array([1.9, 0.0])
    vertices = np.array([np.zeros(2), v2, v1 + v2, v1])
    ax.add_patch(Polygon(vertices, facecolor='#d7eaf5', edgecolor='#246289', lw=1.5))
    for v, name, color, offset in [(v1, '$v_1$', '#246289', (-0.28, 0.04)),
                                  (v2, '$v_2$', '#9b4b1f', (0.0, -0.26))]:
        ax.annotate('', xy=v, xytext=(0, 0),
                    arrowprops={'arrowstyle': '->', 'color': color, 'lw': 2})
        ax.text(*(v + np.array(offset)), name, color=color)
    ax.plot([v1[0], v1[0]], [0, v1[1]], '--', color='#377c47', lw=1.5)
    ax.plot([v1[0] - 0.12, v1[0] - 0.12, v1[0]], [0, 0.12, 0.12],
            color='#377c47', lw=1)
    ax.text(1.04, 0.52, r'$h=\|v_1-tv_2\|$', color='#377c47')
    ax.text(1.48, 1.43, r'$\det A=(\|v_2\|h)^2$')
    ax.set(xlim=(-0.35, 3.1), ylim=(-0.38, 1.7), aspect='equal',
           title='Base and perpendicular height')
    ax.axis('off')

    theta = np.linspace(0, np.pi, 401)
    bx.plot(theta, np.sin(theta)**2, color='#246289', lw=2)
    bx.scatter([0, np.pi / 2, np.pi], [0, 1, 0], color='#246289', s=22, zorder=3)
    bx.set(xticks=[0, np.pi / 2, np.pi], xticklabels=['0', r'$\pi/2$', r'$\pi$'],
           yticks=[0, 0.5, 1], ylim=(-0.06, 1.12), xlim=(0, np.pi),
           xlabel=r'Angle $\theta$ between unit vectors',
           ylabel=r'$\det A=1-\cos^2\theta=\sin^2\theta$',
           title=r'Unit vectors: $0\leq\det A\leq1$')
    bx.text(0.07, 0.12, 'parallel', fontsize=9)
    bx.text(np.pi / 2, 1.03, 'orthogonal', ha='center', fontsize=9)
    bx.text(np.pi - 0.07, 0.12, 'opposite', ha='right', fontsize=9)
    bx.grid(alpha=0.2)
    bx.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path.cwd() / 'mathematics-i-gram-determinant.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
