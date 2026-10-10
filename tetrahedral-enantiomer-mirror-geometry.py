"""Spatial mirror model. Run from _media.

Tested: Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Dimensionless point substituents, not measured molecular coordinates.
"""
from pathlib import Path
import json
import matplotlib.pyplot as plt
import numpy as np

V = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
S = np.diag([-1., 1., 1.])
COLORS = ['#bb4a24', '#08699b', '#6e4096', '#237e43']


def volume6(points):
    return np.linalg.det((points[:3] - points[3]).T)


def draw(ax, points, title):
    ax.set_proj_type('ortho')
    ax.view_init(elev=22, azim=-90)
    for i, p in enumerate(points):
        ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color='#666666',
                lw=2.5, ls='--' if p[1] > 0 else '-')
        ax.scatter(*p, s=620, color=COLORS[i], edgecolors='white',
                   linewidths=1.5, depthshade=False)
        ax.text(*p, 'ABCD'[i], ha='center', va='center',
                color='white', fontsize=16, fontweight='bold', zorder=100)
    ax.scatter(0, 0, 0, s=210, color='#444444', depthshade=False)
    ax.text(0, 0, .28, 'X', ha='center', fontsize=12)
    ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.7), zlim=(-1.7, 1.7))
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title(title, fontsize=15, pad=-3)


def main():
    mirror = V @ S.T
    delta, delta_mirror = volume6(V), volume6(mirror)
    assert np.isclose(delta, 16) and np.isclose(delta_mirror, -16)
    assert np.isclose(np.linalg.det(S), -1)
    assert np.allclose(V @ V.T, mirror @ mirror.T)
    fig = plt.figure(figsize=(9, 4.8), facecolor='white')
    draw(fig.add_subplot(121, projection='3d'), V, 'Four distinct groups')
    draw(fig.add_subplot(122, projection='3d'), mirror, 'Spatial mirror image')
    fig.subplots_adjust(left=.02, right=.98, bottom=.22, top=.84, wspace=.12)
    fig.suptitle('A mirror reverses the labelled tetrahedron', fontsize=18, y=.96)
    fig.add_artist(plt.Line2D([.5, .5], [.27, .78], transform=fig.transFigure,
                             color='#93b6c7', lw=3, ls='--'))
    fig.text(.5, .81, 'mirror: x → −x', ha='center', fontsize=12,
             bbox=dict(facecolor='white', edgecolor='none', pad=3))
    fig.text(.26, .19, 'Δ = +16', ha='center', fontsize=15)
    fig.text(.74, .19, 'Δ = −16', ha='center', fontsize=15)
    fig.text(.5, .105, 'Every spatial rotation preserves Δ. These mirror forms cannot superpose.',
             ha='center', fontsize=12)
    fig.text(.5, .055, 'Point substituents • dashed bonds: farther side (y > 0) • same camera in both panels',
             ha='center', fontsize=10, color='#555555')
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)
    print(json.dumps({'determinants': [delta, delta_mirror], 'mirror_det': -1,
                      'dimensions': [1080, 576]}))


if __name__ == '__main__':
    main()
