"""Generate regular-polygon-edge-rotation.png in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.7), dpi=100, facecolor='white')
    square = np.array([[-1., -1.], [1., -1.], [1., 1.], [-1., 1.]])
    rhombus = np.array([[0., 0.], [2., 0.], [3., np.sqrt(3.)], [1., np.sqrt(3.)]])
    angles = np.pi / 2 + np.arange(5) * 4 * np.pi / 5
    star = np.column_stack([np.cos(angles), np.sin(angles)])
    panels = [(square, 'Regular square', 'Equal sides; each exterior turn is 90°', '#176438'),
              (rhombus, 'Nonregular rhombus', 'Equal sides; turns alternate 60° and 120°', '#a84c13'),
              (star, 'Regular star traversal', 'Equal sides; each exterior turn is 144°', '#8b345f')]
    for ax, (points, title, caption, color) in zip(axes, panels):
        points = points - points.mean(axis=0)
        points = points / max(np.ptp(points[:, 0]), np.ptp(points[:, 1])) * 2
        closed = np.vstack([points, points[0]])
        ax.plot(closed[:, 0], closed[:, 1], '-o', color=color, lw=2.2, ms=4)
        start, end = points[0], points[1]
        ax.annotate('', xy=start + .68 * (end-start), xytext=start + .32 * (end-start),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
        ax.set_aspect('equal'); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.35, 1.35)
        ax.set_title(title, fontsize=12, pad=14)
        ax.text(.5, -.07, caption.replace('; ', ';\n'), ha='center', va='top', transform=ax.transAxes, fontsize=10)
        ax.axis('off')
    fig.suptitle('Ordinary regular polygons need the fundamental turn 360°/n', fontsize=14)
    fig.subplots_adjust(left=.025, right=.975, bottom=.22, top=.79, wspace=.16)
    fig.savefig(Path.cwd() / 'regular-polygon-edge-rotation.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
