"""Antipodal Bloch vectors, tested with Python 3.14 and root-pinned dependencies.

Write paper-58-bloch-povm.png to the caller's current working directory.
Matplotlib uses the caller's MPLCONFIGDIR without overriding it.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(5.3, 4.6), dpi=140, facecolor='white')
    ax = fig.add_subplot(111, projection='3d', facecolor='white')
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, 25), np.linspace(0, np.pi, 13))
    ax.plot_wireframe(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v),
                      color='#c7ced6', linewidth=.5, alpha=.7)
    for k, name in enumerate(['x', 'y', 'z']):
        direction = np.eye(3)[k]
        ax.plot(*np.vstack([-1.1*direction, 1.15*direction]).T,
                color='#a8b0b8', linewidth=.8)
        ax.text(*(1.21*direction), name, color='#555e66', fontsize=10)
    n = np.array([.55, -.35, np.sqrt(1-.55**2-.35**2)])
    for sign, color, label in [(1, '#1565a6', r'$E_1:\ \mathbf{n}$'),
                                (-1, '#bf3d35', r'$E_2:\ -\mathbf{n}$')]:
        endpoint = sign*n
        ax.quiver(0, 0, 0, *endpoint, color=color, linewidth=2,
                  arrow_length_ratio=.12)
        ax.scatter(*endpoint, color=color, s=42, depthshade=False)
        ax.text(*(1.15*endpoint), label, color=color, fontsize=11,
                horizontalalignment='center')
    ax.scatter(0, 0, 0, color='#545b63', s=12)
    ax.set(xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), zlim=(-1.35, 1.35))
    ax.set_box_aspect((1, 1, 1), zoom=1.4)
    ax.view_init(elev=24, azim=-56)
    ax.set_axis_off()
    fig.suptitle('Two rank-one qubit effects: antipodal directions', fontsize=12, y=.96)
    fig.text(.5, .04, r'$E_1+E_2=I,\qquad |\mathbf{n}|=1$', ha='center', fontsize=12)
    fig.subplots_adjust(left=0, right=1, bottom=.09, top=.93)
    fig.savefig(Path.cwd()/'paper-58-bloch-povm.png', facecolor='white',
                transparent=False, dpi=140)
    plt.close(fig)


if __name__ == '__main__':
    main()
