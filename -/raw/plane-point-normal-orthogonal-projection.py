"""Original plane/point/normal geometry; write the opaque PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.array([2., -1., 2.])
    p = np.array([4., 1., 2.])
    q = p - (np.dot(n, p) - 3) / np.dot(n, n) * n
    x, y = np.meshgrid(np.linspace(.4, 4.7, 19), np.linspace(.35, 3.4, 15))
    z = (3 - 2*x + y) / 2
    fig = plt.figure(figsize=(10.4, 6.4), facecolor='white')
    ax = fig.add_axes((.03, .15, .66, .73), projection='3d')
    ax.plot_surface(x, y, z, color='#94c5dd', alpha=.3, linewidth=0)
    ax.plot_wireframe(x, y, z, color='#7298ac', linewidth=.45, alpha=.65)
    ax.plot(*np.array([p, q]).T, color='#b44e22', lw=3.4)
    ax.scatter(*p, color='#b44e22', s=65, depthshade=False)
    ax.scatter(*q, color='#146352', s=65, depthshade=False)
    ax.text(*(p + [.12, -.06, .2]), 'p = (4, 1, 2)', fontsize=11, color='#923c19')
    ax.text(*(q + [.09, -.13, -.36]), 'q', fontsize=12, color='#146352')
    unit = n / np.linalg.norm(n)
    ax.quiver(*q, *unit, length=.72, color='#146352', linewidth=2,
              arrow_length_ratio=.22)
    ax.set_xlabel('x', labelpad=8)
    ax.set_ylabel('y', labelpad=8)
    ax.set_zlabel('z', labelpad=6)
    ax.set_xlim(.3, 4.8)
    ax.set_ylim(.25, 3.55)
    ax.set_zlim(-3.3, 2.8)
    ax.set_box_aspect((4.5, 3.3, 6.1))
    ax.view_init(elev=23, azim=-61)
    ax.set_facecolor('white')
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor((1, 1, 1, 1))
    fig.suptitle('A plane, its normal, and the closest point', fontsize=18, weight='bold', y=.965)
    fig.text(.71, .75, 'Plane', fontsize=12, weight='bold', color='#226483')
    fig.text(.71, .70, r'$2x-y+2z=3$', fontsize=15)
    fig.text(.71, .59, 'Normal vector', fontsize=12, weight='bold', color='#146352')
    fig.text(.71, .54, r'$\mathbf{n}=(2,-1,2)$', fontsize=14)
    fig.text(.71, .43, 'Closest point', fontsize=12, weight='bold', color='#146352')
    fig.text(.71, .38, r'$\mathbf{q}=(20/9,17/9,2/9)$', fontsize=13)
    fig.text(.71, .27, 'Perpendicular distance', fontsize=12, weight='bold', color='#b44e22')
    fig.text(.71, .22, r'$\|\mathbf{p}-\mathbf{q}\|=8/3$', fontsize=14)
    fig.text(.5, .055, 'The mesh is a displayed patch; the mathematical plane has no edges.',
             ha='center', fontsize=11, color='#405063')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
