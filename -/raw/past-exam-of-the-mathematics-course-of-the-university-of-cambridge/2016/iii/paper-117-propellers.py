"""Draw reflected seven-triangle propellers; PNG is written only to cwd.
Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

PAIRINGS = [
    [[(0, 1), (2, 5)], [(0, 2), (4, 3)], [(0, 4), (1, 6)]],
    [[(0, 4), (2, 3)], [(0, 1), (4, 6)], [(0, 2), (1, 5)]],
]
COLOURS = ['#cc5533', '#2477ad', '#35854b']

def reflected_tiles(edges):
    tiles = {0: np.array([[0., 0.], [1.45, 0.], [.32, 1.18]])}
    while len(tiles) < 7:
        old_size = len(tiles)
        for colour, pairs in enumerate(edges):
            for i, j in pairs:
                if i not in tiles and j in tiles:
                    i, j = j, i
                if i in tiles and j not in tiles:
                    tile = tiles[i]
                    u, v = [tile[k] for k in range(3) if k != colour]
                    direction = (v - u) / np.linalg.norm(v - u)
                    delta = tile[colour] - u
                    reflected = tile.copy()
                    reflected[colour] = u + 2 * np.dot(delta, direction) * direction - delta
                    tiles[j] = reflected
        assert len(tiles) > old_size
    return tiles

def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=100, facecolor='white')
    for ax, pairings, name in zip(axes, PAIRINGS, ['Left propeller', 'Right propeller']):
        tiles = reflected_tiles(pairings)
        for i in range(7):
            tile = tiles[i]
            ax.add_patch(Polygon(tile, facecolor='#fff1bf' if i == 0 else '#eaf0f5', edgecolor='none'))
            for colour in range(3):
                u, v = [tile[k] for k in range(3) if k != colour]
                internal = any(i in pair for pair in pairings[colour])
                ax.plot([u[0], v[0]], [u[1], v[1]], color=COLOURS[colour], lw=1.8, ls='--' if internal else '-')
            xy = tile.mean(axis=0)
            ax.text(*xy, str(i), ha='center', va='center', fontsize=14, weight='bold')
        cloud = np.concatenate(list(tiles.values()))
        ax.set_xlim(cloud[:, 0].min() - .18, cloud[:, 0].max() + .18)
        ax.set_ylim(cloud[:, 1].min() - .18, cloud[:, 1].max() + .18)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(name, fontsize=14)
    from matplotlib.lines import Line2D
    handles = [Line2D([0], [0], color=c, lw=2, label=f'Side {s}') for c, s in zip(COLOURS, 'abc')]
    fig.legend(handles=handles, loc='lower center', ncol=3, frameon=False)
    fig.subplots_adjust(left=.03, right=.98, top=.89, bottom=.10, wspace=.11)
    fig.savefig(Path.cwd() / 'paper-117-propellers.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
