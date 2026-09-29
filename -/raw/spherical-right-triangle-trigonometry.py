"""Draw a non-octant spherical right triangle; output PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media to regenerate the published image.
"""

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def arc(p, q, samples=201):
    angle = np.arccos(np.clip(p @ q, -1, 1))
    t = np.linspace(0, 1, samples)
    return (np.sin((1 - t) * angle)[:, None] * p
            + np.sin(t * angle)[:, None] * q) / np.sin(angle)


def main():
    vertices = np.array([[0, 0, 1], [np.sqrt(3) / 2, 0, .5],
                         [0, np.sqrt(3) / 2, .5]])
    a, b, c = [np.arccos(vertices[j] @ vertices[k])
               for j, k in [(1, 2), (2, 0), (0, 1)]]
    angles = []
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        p = vertices[i]
        tangents = [vertices[v] - (p @ vertices[v]) * p for v in [j, k]]
        tangents = [t / np.linalg.norm(t) for t in tangents]
        angles.append(np.arccos(np.clip(tangents[0] @ tangents[1], -1, 1)))
    assert np.allclose([a, b, c], [np.arccos(.25), np.pi / 3, np.pi / 3])
    assert np.allclose(angles, [np.pi / 2, np.arccos(1 / np.sqrt(5)),
                               np.arccos(1 / np.sqrt(5))])
    assert np.allclose(np.sin(angles) / np.sin([a, b, c]), 4 / np.sqrt(15))

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(9.2, 6.5), facecolor='white')
    ax = fig.add_axes([0, .06, .64, .83], projection='3d', computed_zorder=False)
    ax.set_facecolor('white')
    ax.set_proj_type('ortho')
    ax.view_init(elev=22, azim=45)
    ax.set_box_aspect((1, 1, 1), zoom=1.16)
    ax.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), zlim=(-1.12, 1.12))
    ax.set_axis_off()
    phi, theta = np.meshgrid(np.linspace(0, 2 * np.pi, 85), np.linspace(0, np.pi, 43))
    ax.plot_wireframe(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi),
                      np.cos(theta), rstride=4, cstride=7, color='#acbdca',
                      alpha=.35, lw=.65, zorder=1)
    # Normalized convex combinations fill exactly the minor spherical triangle.
    t, s = np.meshgrid(np.linspace(0, 1, 61), np.linspace(0, 1, 61))
    patch = ((1 - t)[..., None] * vertices[0]
             + t[..., None] * ((1 - s)[..., None] * vertices[1]
                               + s[..., None] * vertices[2]))
    patch /= np.linalg.norm(patch, axis=2)[..., None]
    ax.plot_surface(*patch.transpose(2, 0, 1), color='#dceee9', shade=False,
                    rcount=61, ccount=61, linewidth=0, antialiased=False, zorder=2)
    colors = ['#cf6422', '#126f80', '#126f80']
    for (j, k), color in zip([(1, 2), (2, 0), (0, 1)], colors):
        curve = arc(vertices[j], vertices[k])
        assert np.allclose(np.linalg.norm(curve, axis=1), 1)
        ax.plot(*curve.T, color=color, lw=3.2, zorder=4)
    for vertex, label, align in zip(vertices, ['A', 'B', 'C'], ['center', 'right', 'left']):
        ax.scatter(*vertex, s=28, color='#263945', depthshade=False, zorder=6)
        ax.text(*(1.12 * vertex), label, ha=align, va='bottom', fontsize=16, zorder=7)
    for (j, k), label, color, factor in zip(
            [(1, 2), (2, 0), (0, 1)],
            [r'$a=75.5225^\circ$', r'$b=60^\circ$', r'$c=60^\circ$'],
            colors, [1.05, 1.13, 1.13]):
        point = arc(vertices[j], vertices[k], 3)[1] * factor
        ax.text(*point, label, ha='center', va='center', color=color, fontsize=12,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9}, zorder=8)
    # An angle arc at A lies on the sphere, between the two outgoing directions.
    t = np.linspace(0, np.pi / 2, 50)
    eps = .17
    angle_arc = np.array([np.sin(eps) * np.cos(t), np.sin(eps) * np.sin(t),
                          np.full_like(t, np.cos(eps))])
    ax.plot(*angle_arc, color='#703e98', lw=2.5, zorder=5)
    ax.text(.18, .18, .87, r'$90^\circ$', color='#703e98', ha='center', fontsize=12,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9}, zorder=9)

    fig.suptitle('A right triangle on the unit sphere', fontsize=18, y=.96)
    fig.text(.65, .78, 'Angular sides', weight='bold', fontsize=14)
    fig.text(.65, .71, r'$b=c=\pi/3=60^\circ$', fontsize=15)
    fig.text(.65, .63, r'$\cos a=\cos b\cos c=1/4$', fontsize=14)
    fig.text(.65, .55, r'$a\approx1.318116\ \mathrm{rad}$', fontsize=15)
    fig.text(.65, .43, 'Interior angles', weight='bold', fontsize=14)
    fig.text(.65, .36, r'$A=90^\circ$', color='#703e98', fontsize=15)
    fig.text(.65, .29, r'$B=C\approx63.434949^\circ$', fontsize=14)
    fig.text(.65, .17, 'On radius R: physical lengths\nare R times the sides in radians.',
             fontsize=11, linespacing=1.6)
    fig.text(.5, .035, 'All three edges are shorter great-circle arcs; angles are measured between tangents.',
             ha='center', fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
