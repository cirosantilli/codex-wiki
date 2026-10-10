"""Rearrange four 3-4-5 triangles; write an opaque PNG to the cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def polygon_area(vertices):
    vertices = np.asarray(vertices, dtype=float)
    x, y = vertices.T
    return abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2


def main():
    a, b = 3.0, 4.0
    side = a + b
    c = np.hypot(a, b)
    left = [
        [(0, 0), (a, 0), (0, b)],
        [(side, 0), (side, a), (a, 0)],
        [(side, side), (b, side), (side, a)],
        [(0, side), (0, b), (b, side)],
    ]
    right = [
        [(0, a), (a, a), (0, side)],
        [(a, a), (a, side), (0, side)],
        [(a, 0), (side, 0), (side, a)],
        [(a, 0), (a, a), (side, a)],
    ]
    tilted = np.array([(a, 0), (side, a), (b, side), (0, b)])
    small = [(0, 0), (a, 0), (a, a), (0, a)]
    large = [(a, a), (side, a), (side, side), (a, side)]
    for triangle in left + right:
        assert np.isclose(polygon_area(triangle), a * b / 2)
        edges = np.roll(triangle, -1, axis=0) - np.array(triangle)
        assert np.allclose(np.sort(np.linalg.norm(edges, axis=1)), [a, b, c])
    edges = np.roll(tilted, -1, axis=0) - tilted
    assert np.allclose(np.linalg.norm(edges, axis=1), c)
    assert np.allclose(np.sum(edges * np.roll(edges, -1, axis=0), axis=1), 0)
    assert np.isclose(polygon_area(tilted), c**2)
    assert np.isclose(polygon_area(small) + polygon_area(large), c**2)
    assert np.isclose(4 * a * b / 2 + c**2, side**2)

    plt.rcParams.update({'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.8), facecolor='white')
    colors = ['#b6d8eb', '#f2c9a7', '#b6dfc7', '#d9c6e8']
    for ax, triangles in zip(axes, [left, right]):
        ax.set_facecolor('white')
        for triangle, color in zip(triangles, colors):
            ax.add_patch(Polygon(triangle, facecolor=color, edgecolor='#354354', lw=1.5))
        ax.plot([0, side, side, 0, 0], [0, 0, side, side, 0], color='#354354', lw=1.8)
        ax.set(xlim=(-.7, side + .4), ylim=(-.9, side + .5), aspect='equal')
        ax.axis('off')

    axes[0].add_patch(Polygon(tilted, facecolor='#fff5cd', edgecolor='#354354', lw=1.6))
    axes[0].text(3.5, 3.5, '$c^2=25$', ha='center', va='center', fontsize=20)
    axes[0].text(5.35, 1.0, '$c=5$', rotation=37, ha='center', color='#6a5413')
    axes[0].text(a / 2, -.45, '$a=3$', ha='center')
    axes[0].text(a + b / 2, -.45, '$b=4$', ha='center')
    axes[0].text(-.4, b / 2, '$b=4$', ha='center', rotation=90)
    axes[0].text(-.4, b + a / 2, '$a=3$', ha='center', rotation=90)
    axes[0].set_title('Four triangles leave one tilted square', fontsize=13, pad=10)

    for polygon, start, length in [(small, 0, a), (large, a, b)]:
        axes[1].add_patch(Polygon(polygon, facecolor='#fff5cd', edgecolor='#354354', lw=1.6))
        for value in np.arange(start + 1, start + length):
            axes[1].plot([value, value], [start, start + length], color='#ddcd94', lw=.8)
            axes[1].plot([start, start + length], [value, value], color='#ddcd94', lw=.8)
    for x, y, label in [(a / 2, a / 2, '$a^2=9$'), (a + b / 2, a + b / 2, '$b^2=16$')]:
        axes[1].text(x, y, label, ha='center', va='center', fontsize=18,
                     bbox={'facecolor': '#fff5cd', 'edgecolor': 'none', 'pad': 3})
    axes[1].text(a / 2, -.45, '$a=3$', ha='center')
    axes[1].text(a + b / 2, -.45, '$b=4$', ha='center')
    axes[1].set_title('Rearrange them to leave two squares', fontsize=13, pad=10)
    fig.suptitle('Same outer area, same four triangles: $c^2=a^2+b^2$', fontsize=16, y=.98)
    fig.text(.5, .085, 'Each triangle has area 6; each outer square has area 49.', ha='center')
    fig.text(.5, .035, '$49-4(6)=25=9+16$', ha='center', fontsize=16)
    fig.subplots_adjust(left=.05, right=.98, bottom=.15, top=.85, wspace=.15)
    fig.savefig(Path.cwd() / 'pythagorean-area-dissection.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
