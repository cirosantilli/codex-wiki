"""Original schematic only; run from _media with Python 3.14 and Matplotlib."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon


FOLDED = np.array([
    [-3.2, -1.8], [-2.5, -1.0], [-0.85, 0.0], [-2.3, 0.9],
    [-2.0, 2.0], [-0.5, 2.5], [0.0, 0.95], [1.8, 2.3],
    [2.6, 1.2], [0.9, 0.0], [2.2, -1.0], [0.2, -2.0],
])
ROLES = {3: '#2479b0', 7: '#d86b18', 10: '#8855a5'}


def chain(ax, positions, radius):
    """Preserve every residue and the eleven backbone connections."""
    ax.plot(*positions.T, color='#adb7c0', linewidth=3, zorder=1)
    for i, (x, y) in enumerate(positions, 1):
        ax.add_patch(Circle((x, y), radius, facecolor=ROLES.get(i, '#e7edf2'),
                            edgecolor='#435363', linewidth=1.2, zorder=3))
        ax.text(x, y, str(i), ha='center', va='center', fontsize=10,
                color='white' if i in ROLES else '#253544', zorder=4)
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig = plt.figure(figsize=(10, 6.4), facecolor='white')
    fig.suptitle('An active site is a spatial team within a larger chain',
                 fontsize=16, x=0.5, y=0.975)
    top = fig.add_axes([0.05, 0.72, 0.90, 0.19])
    linear = np.column_stack((np.arange(12), np.zeros(12)))
    chain(top, linear, 0.29)
    top.set_xlim(-0.7, 11.7)
    top.set_ylim(-0.8, 1.2)
    top.text(5.5, 0.85, 'Sequence order: highlighted positions are separated',
             ha='center', fontsize=12)
    top.text(-0.35, -0.65, 'N end', ha='center', fontsize=10)
    top.text(11.35, -0.65, 'C end', ha='center', fontsize=10)

    folded = fig.add_axes([0.04, 0.09, 0.57, 0.60])
    chain(folded, FOLDED, 0.22)
    folded.set_xlim(-3.7, 3.1)
    folded.set_ylim(-2.5, 3.2)
    folded.text(-0.3, 3.0, 'Imagined fold: positions 3, 7 and 10 meet',
                ha='center', fontsize=12)
    substrate = np.array([[-0.35, -0.35], [0.28, -0.35], [0.42, 0.12],
                          [0.12, 0.43], [-0.36, 0.24]])
    folded.add_patch(Polygon(substrate, facecolor='#dbf0df',
                             edgecolor='#367846', linewidth=1.7, zorder=2))
    folded.text(0, 0, 'S', color='#255c33', ha='center', va='center',
                fontsize=13, weight='bold', zorder=4)
    for i in ROLES:
        folded.plot([0, FOLDED[i-1, 0]], [0, FOLDED[i-1, 1]],
                    linestyle='--', linewidth=1.2, color=ROLES[i], zorder=2)
    folded.text(-3.25, -2.2, 'N end', fontsize=10)
    folded.text(0.2, -2.4, 'C end', ha='center', fontsize=10)

    legend = fig.add_axes([0.63, 0.13, 0.34, 0.52])
    legend.axis('off')
    entries = [(0.85, '#2479b0', '3: substrate recognition'),
               (0.67, '#d86b18', '7: catalytic chemistry'),
               (0.49, '#8855a5', '10: both roles'),
               (0.31, '#e7edf2', 'Other positions: folded support')]
    for y, color, label in entries:
        legend.scatter([0.05], [y], s=175, color=color, edgecolor='#435363')
        legend.text(0.14, y, label, va='center', fontsize=11)
    legend.text(0.03, 0.10, 'S = generic substrate\nRoles may overlap.', fontsize=11)
    legend.set_xlim(0, 1)
    legend.set_ylim(0, 1)
    fig.text(0.5, 0.025, 'Original toy diagram • no actual coordinates, bond geometry or universal site size',
             ha='center', fontsize=10, color='#53616d')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
