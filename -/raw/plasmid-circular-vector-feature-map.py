"""Draw an original hypothetical plasmid map. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG to the current working directory.
Coordinates are boundaries, not inclusive base-pair indices. No real sequence is asserted.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np

LENGTH = 6000
FEATURES = [(200, 700, '#2475b0', 'Origin of replication', '200–700: 500 bp', 'Supports copying in a compatible host'),
            (3200, 4000, '#27845b', 'Selectable marker', '3200–4000: 800 bp', 'Permits recovery under chosen conditions'),
            (1000, 2500, '#d77722', 'Insert', '1000–2500: 1500 bp', 'The chosen DNA fragment under study')]
CUTS = [(1000, 'A'), (2500, 'B'), (4500, 'B')]


def position(coordinate, radius=1.0):
    theta = np.deg2rad(90 - 360 * coordinate / LENGTH)
    return radius * np.array([np.cos(theta), np.sin(theta)])


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig = plt.figure(figsize=(10, 6.4), dpi=130, facecolor='white')
    fig.text(.04, .95, 'Reading a circular plasmid feature map', fontsize=19, weight='bold')
    fig.text(.04, .905, 'Hypothetical engineered DNA • 6000 base pairs • clockwise boundary coordinates', color='#475569')
    ax = fig.add_axes([.015, .15, .59, .71], aspect='equal')
    ax.set(xlim=(-1.55, 1.55), ylim=(-1.5, 1.5))
    ax.axis('off')
    ax.add_patch(Circle((0, 0), 1, fill=False, lw=15, edgecolor='#e2e8f0'))
    for start, stop, color, *_ in FEATURES:
        ax.add_patch(Wedge((0, 0), 1.075, 90-360*stop/LENGTH, 90-360*start/LENGTH,
                           width=.15, facecolor=color, edgecolor='white', linewidth=1))
    for coordinate in (0, 2000, 3000, 4000, 5000):
        p, q = position(coordinate, 1.10), position(coordinate, 1.17)
        ax.plot([p[0], q[0]], [p[1], q[1]], color='#94a3b8', lw=1)
        label = '0 = 6000' if coordinate == 0 else f'{coordinate}'
        xy = position(coordinate, 1.32)
        ax.text(*xy, label, ha='center', va='center', fontsize=10, color='#475569')
    for coordinate, enzyme in CUTS:
        p, q = position(coordinate, .87), position(coordinate, 1.16)
        ax.plot([p[0], q[0]], [p[1], q[1]], color='#172033', lw=2)
        xy = position(coordinate, 1.37)
        ax.text(*xy, f'{enzyme}\n{coordinate}', ha='center', va='center', weight='bold', fontsize=11)
    ax.text(0, .12, '6000 bp', fontsize=23, weight='bold', ha='center', color='#172033')
    ax.text(0, -.13, 'One continuous circle', ha='center', color='#475569')
    ax.text(0, -.32, 'Zero is a label, not an end', ha='center', fontsize=10, color='#475569')
    for y, (start, stop, color, title, interval, job) in zip((.77, .58, .39), FEATURES):
        fig.text(.64, y, title, color=color, fontsize=13, weight='bold')
        fig.text(.64, y-.044, interval, fontsize=11)
        # Deliberate line breaks keep the explanatory column readable.
        wrapped = {'Origin of replication': 'Supports copying in\na compatible host',
                   'Selectable marker': 'Permits recovery under\nchosen conditions',
                   'Insert': 'The chosen DNA fragment\nunder study'}[title]
        fig.text(.64, y-.115, wrapped, color='#475569', fontsize=10, linespacing=1.5)
    fig.text(.64, .19, 'Cut boundaries', fontsize=11, weight='bold')
    fig.text(.64, .13, 'A: 1000     B: 2500, 4500\nAbstract enzymes; no sequence specified', fontsize=9.8, linespacing=1.5)
    fig.text(.04, .045, 'Coloured regions: 500 + 800 + 1500 = 2800 bp; remaining DNA: 3200 bp.\nPosition diagram, not a physical conformation or a real commercial vector.', fontsize=10, color='#475569', linespacing=1.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
