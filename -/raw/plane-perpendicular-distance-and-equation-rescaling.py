"""Original perpendicular-distance proof and orientation diagram; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.3), facecolor='white')
    p = np.array([0., 8/3])
    q = np.array([0., 0.])
    r = np.array([2., 0.])
    ax = axes[0]
    ax.axhline(0, color='#226483', lw=2)
    ax.plot([q[0], p[0]], [q[1], p[1]], color='#b44e22', lw=3)
    ax.plot([r[0], p[0]], [r[1], p[1]], color='#777d89', lw=2)
    ax.plot([0, .17, .17], [.17, .17, 0], color='#146352', lw=1.5)
    for point, name, offset in [(p, 'p', (-.19, .18)), (q, 'q', (-.2, -.3)), (r, 'r', (.06, -.3))]:
        ax.scatter(*point, s=42, color='#183e50', zorder=4)
        ax.text(*(point + offset), name, fontsize=13)
    ax.text(-.17, 1.25, '8/3', ha='right', fontsize=14, color='#b44e22')
    ax.text(1.28, 1.43, '10/3', fontsize=14, color='#5f6571')
    ax.text(1, -.32, '2', ha='center', fontsize=13)
    ax.text(.9, -.69, r'$(10/3)^2=(8/3)^2+2^2$', ha='center', fontsize=13)
    ax.text(2.38, .13, 'plane', fontsize=11, color='#226483')
    ax.set_title('Shortest route: perpendicular', fontsize=13, weight='bold')
    ax.set_xlim(-.7, 3.1)
    ax.set_ylim(-1.05, 3.25)
    ax.set_aspect('equal')
    ax.axis('off')

    ax = axes[1]
    ax.axhline(0, color='#226483', lw=2)
    for x, label, direction, color in [(-.85, r'$\widehat{\mathbf{n}}$', 1, '#146352'), (1.1, r'$-\widehat{\mathbf{n}}$', -1, '#78508b')]:
        ax.annotate('', xy=(x, .85*direction), xytext=(x, 0), arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.1})
        ax.text(x + .1, .48*direction, label, fontsize=13, color=color)
    ax.scatter(0, 8/3, color='#b44e22', s=42, zorder=4)
    ax.text(.12, 8/3, 'p', fontsize=13)
    ax.plot([0, 0], [0, 8/3], color='#b44e22', lw=2, ls='--')
    ax.text(-.95, 1.54, r'$s=+8/3$', fontsize=13, color='#146352')
    ax.text(.6, 1.54, r'$s=-8/3$', fontsize=13, color='#78508b')
    ax.text(0, -.68, r'$2x-y+2z=3$', ha='center', fontsize=13)
    ax.text(0, -1.07, r'$-6x+3y-6z=-9$', ha='center', fontsize=13)
    ax.text(0, -1.43, 'Same plane; same unsigned distance 8/3', ha='center', fontsize=11)
    ax.set_xlim(-1.8, 2)
    ax.set_ylim(-1.7, 3.3)
    ax.set_aspect('equal')
    ax.set_title('Reverse orientation, keep distance', fontsize=13, weight='bold')
    ax.axis('off')
    fig.suptitle('Perpendicular distance does not depend on equation scale', fontsize=17, weight='bold', y=.98)
    fig.subplots_adjust(top=.86, bottom=.12, left=.04, right=.98, wspace=.18)
    fig.text(.5, .035, 'Orthogonal cross-sections: positions along the plane are schematic, perpendicular lengths are explicit.', ha='center', fontsize=10.5, color='#405063')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
