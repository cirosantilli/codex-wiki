"""Original Fizeau path-accounting schematic; Python 3.14, matplotlib 3.10.7.

Run from _media to emit fizeau-counterflow-paths.png. The optical exchange
block is a schematic connection, not a scaled ray trace or historical copy.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


BLUE = '#1265a8'
ORANGE = '#b94713'
GREY = '#52616b'


def arrow(ax, start, end, color, lw=2.5, size=15):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>',
                                mutation_scale=size, linewidth=lw,
                                color=color, zorder=5))


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=100, facecolor='white')
    fig.subplots_adjust(left=.025, right=.985, top=.91, bottom=.035)
    ax.set(xlim=(0, 12), ylim=(0, 6.7))
    ax.axis('off')
    fig.suptitle('Moving water: count both passages of each beam',
                 fontsize=18, fontweight='bold', y=.975)
    ax.text(6, 6.35, 'Tube exchange on return makes the two flow effects add',
            ha='center', fontsize=13, color=GREY)

    for low in (4.0, 1.7):
        ax.add_patch(Rectangle((3.1, low), 5.25, .70,
                               facecolor='#edf6fa', edgecolor='#859ca8', lw=1.5))
        for x in (3.14, 8.31):
            ax.plot([x, x], [low, low + .7], color='#859ca8', lw=3)
    ax.annotate('', xy=(8.35, 5.22), xytext=(3.1, 5.22),
                arrowprops={'arrowstyle': '|-|', 'color': GREY})
    ax.text(5.72, 5.35, r'one tube length $\ell$', ha='center', color=GREY)
    arrow(ax, (4.2, 4.95), (6.7, 4.95), GREY, lw=3, size=18)
    ax.text(6.95, 4.94, r'water $+u$', va='center', color=GREY)
    arrow(ax, (6.7, 1.37), (4.2, 1.37), GREY, lw=3, size=18)
    ax.text(6.95, 1.37, r'water $-u$', va='center', color=GREY)

    # Separate the counterpropagating rays slightly so their directions are legible.
    for y, color, direction in ((4.52, BLUE, 1), (4.18, ORANGE, -1),
                                 (2.22, BLUE, -1), (1.88, ORANGE, 1)):
        ax.plot([2.75, 8.7], [y, y], color=color, lw=2.5, zorder=4)
        x1, x2 = (5.0, 6.0) if direction == 1 else (6.0, 5.0)
        arrow(ax, (x1, y), (x2, y), color)
    ax.text(3.5, 4.56, 'A', color=BLUE, va='bottom', fontweight='bold')
    ax.text(7.7, 4.12, 'B', color=ORANGE, va='top', fontweight='bold')
    ax.text(7.7, 2.26, 'A', color=BLUE, va='bottom', fontweight='bold')
    ax.text(3.5, 1.82, 'B', color=ORANGE, va='top', fontweight='bold')

    ax.add_patch(FancyBboxPatch((8.78, 1.45), 2.6, 3.72,
                                boxstyle='round,pad=.06',
                                facecolor='#fafafa', edgecolor='#a9a9a9', lw=1.3))
    ax.plot([8.7, 9.1, 10.8, 9.1, 8.7], [4.52, 4.52, 3.2, 2.22, 2.22],
            color=BLUE, lw=2.5)
    ax.plot([8.7, 9.25, 10.6, 9.25, 8.7], [1.88, 1.88, 3.2, 4.18, 4.18],
            color=ORANGE, lw=2.5, linestyle='--')
    ax.text(10.08, 5.34, 'Far telescope\n+ focal mirror', ha='center', fontsize=12)
    ax.text(10.07, 1.02, 'Exchange tubes\non return', ha='center', fontsize=12)
    arrow(ax, (9.18, 4.45), (9.73, 4.02), BLUE, size=13)
    arrow(ax, (9.2, 1.91), (9.73, 2.43), ORANGE, size=13)

    ax.add_patch(FancyBboxPatch((1.48, 1.6), 1.15, 3.25,
                                boxstyle='round,pad=.06',
                                facecolor='#fafafa', edgecolor='#a9a9a9', lw=1.3))
    for y, color in ((4.52, BLUE), (4.18, ORANGE), (2.22, BLUE), (1.88, ORANGE)):
        ax.plot([2.63, 2.75], [y, y], color=color, lw=2.5)
    ax.text(2.06, 3.2, 'Near\ntelescope\n+ slits', ha='center', va='center', fontsize=11)
    ax.text(.70, 5.45, 'Sunlight', ha='center', fontsize=12)
    arrow(ax, (.70, 5.08), (.70, 3.26), '#333333', lw=1.8)
    ax.plot([.40, 1.0], [2.9, 3.5], color='#333333', lw=2)
    arrow(ax, (.84, 3.2), (1.43, 3.2), '#333333', lw=1.8)
    ax.text(.72, 2.35, 'Partial\nmirror', ha='center', fontsize=11)
    arrow(ax, (1.43, 2.75), (.68, 1.25), '#333333', lw=1.8)
    ax.text(.72, .72, 'Recombined\nfringe readout', ha='center', fontsize=11)
    ax.text(5.70, .72, 'A: with flow twice    B: against flow twice',
            ha='center', fontsize=13, fontweight='bold')
    ax.text(5.70, .25, r'Water length per beam: $L=\ell+\ell=2\ell$',
            ha='center', fontsize=13)
    ax.text(11.85, .12, 'Schematic; paths\nseparated for clarity',
            ha='right', fontsize=9, color=GREY)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
