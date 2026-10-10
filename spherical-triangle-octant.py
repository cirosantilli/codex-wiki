"""Draw a great-circle octant triangle; write an opaque PNG to the cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    vertices = np.eye(3)
    # The outgoing tangents at each vertex are the other two coordinate vectors.
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        assert np.isclose(np.dot(vertices[j], vertices[k]), 0)
    central_angles = np.arccos(vertices @ vertices.T)
    assert np.allclose(central_angles[np.triu_indices(3, 1)], np.pi / 2)
    excess = 3 * np.pi / 2 - np.pi
    assert np.isclose(excess, 4 * np.pi / 8)
    # Independently integrate sin(theta) dtheta dphi over the octant.
    theta_edges = np.linspace(0, np.pi / 2, 2001)
    theta_mid = (theta_edges[:-1] + theta_edges[1:]) / 2
    area = np.sum(np.sin(theta_mid) * np.diff(theta_edges)) * np.pi / 2
    assert np.isclose(area, np.pi / 2, rtol=1e-7)

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(9, 6.4), facecolor='white')
    ax = fig.add_axes([.00, .08, .69, .80], projection='3d', computed_zorder=False)
    ax.set_facecolor('white')
    ax.set_proj_type('ortho')
    ax.view_init(elev=24, azim=40)
    ax.set_box_aspect((1, 1, 1), zoom=1.17)
    ax.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), zlim=(-1.12, 1.12))
    ax.set_axis_off()

    longitude = np.linspace(0, 2 * np.pi, 85)
    colatitude = np.linspace(0, np.pi, 43)
    phi, theta = np.meshgrid(longitude, colatitude)
    ax.plot_wireframe(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi),
                      np.cos(theta), rstride=4, cstride=7, color='#b7c3ce', alpha=.32, lw=.65, zorder=1)
    phi, theta = np.meshgrid(np.linspace(0, np.pi / 2, 65), np.linspace(0, np.pi / 2, 65))
    ax.plot_surface(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi),
                    np.cos(theta), color='#9ddac9', shade=False, alpha=1, linewidth=0,
                    rcount=65, ccount=65, antialiased=False, zorder=2)
    t = np.linspace(0, np.pi / 2, 200)
    for curve in [(np.cos(t), np.sin(t), np.zeros_like(t)),
                  (np.cos(t), np.zeros_like(t), np.sin(t)),
                  (np.zeros_like(t), np.cos(t), np.sin(t))]:
        assert np.allclose(np.sum(np.array(curve)**2, axis=0), 1)
        ax.plot(*curve, color='#12675a', lw=3, zorder=4)
    # Small angle arcs lie on the sphere between the two edge tangents.
    eps = .12
    arc_t = np.linspace(0, np.pi / 2, 40)
    for i in range(3):
        j, k = [v for v in range(3) if v != i]
        arc = (np.cos(eps) * vertices[i, :, None]
               + np.sin(eps) * (vertices[j, :, None] * np.cos(arc_t)
                               + vertices[k, :, None] * np.sin(arc_t)))
        ax.plot(*arc, color='#b56720', lw=2.2, zorder=5)
    labels = ['A = (R, 0, 0)', 'B = (0, R, 0)', 'C = (0, 0, R)']
    for vertex, label, align in zip(vertices, labels, ['right', 'left', 'center']):
        ax.scatter(*vertex, color='#12675a', s=24, depthshade=False, zorder=6)
        ax.text(*(1.12 * vertex), label, ha=align, va='bottom', fontsize=10,
                color='#244840', zorder=7)

    fig.suptitle('A spherical triangle with three right angles', fontsize=17, y=.96)
    fig.text(.68, .73, 'Positive coordinate octant', fontsize=13, weight='bold')
    fig.text(.68, .65, 'Each edge is a quarter\nof a great circle.', linespacing=1.6)
    fig.text(.68, .52, r'$a=b=c=\pi R/2$', fontsize=16)
    fig.text(.68, .43, r'$\alpha=\beta=\gamma=\pi/2$', fontsize=16)
    fig.text(.68, .32, r'$E=3(\pi/2)-\pi=\pi/2$', fontsize=15)
    fig.text(.68, .22, r'$\mathrm{Area}=R^2E=\pi R^2/2$', fontsize=15)
    fig.text(.5, .035, 'Eight congruent octants cover the sphere: each has one eighth of its area.',
             ha='center', fontsize=12)
    fig.savefig(Path.cwd() / 'spherical-triangle-octant.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
