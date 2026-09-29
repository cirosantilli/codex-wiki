"""Functional cyclotron schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Radii are illustrative; no historical dimensions are inferred.
Each arc solves uniform-B motion at fixed speed. Kicks occur at a zero-width gap.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyBboxPatch


def orbit(n=12, scale=0.27):
    y = 0.0
    for j in range(1, n + 1):
        radius = scale * np.sqrt(j)
        side = (-1) ** (j + 1)
        theta = np.linspace(0, np.pi, 150)
        x = side * radius * np.sin(theta)
        yy = y + side * radius * (1 - np.cos(theta))
        yield j, radius, x, yy
        y = yy[-1]


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig = plt.figure(figsize=(11, 6.8), dpi=130)
    ax = fig.add_axes([0.03, 0.14, 0.57, 0.75])
    ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0.1), 1.48, fill=False, lw=1.4, ec='#536471'))
    ax.add_patch(Wedge((0, 0.1), 1.34, 90, 270, fc='#e4edf5', ec='#6488a2', lw=1.5))
    ax.add_patch(Wedge((0, 0.1), 1.34, -90, 90, fc='#eaf3e4', ec='#779960', lw=1.5))
    ax.axvspan(-0.035, 0.035, color='white', zorder=3)
    paths = list(orbit())
    for j, radius, x, y in paths:
        color = plt.cm.viridis(0.18 + j / 18)
        ax.plot(x, y, color=color, lw=1.5, zorder=4)
        if j in (3, 8, 12):
            k = 70
            ax.annotate('', (x[k + 9], y[k + 9]), (x[k], y[k]),
                        arrowprops={'arrowstyle': '->', 'lw': 1.5, 'color': color}, zorder=5)
    ax.scatter([0], [0], c='#ab382b', s=35, zorder=6)
    ax.annotate('Ion source', (0, 0), (-0.77, -0.14),
                arrowprops={'arrowstyle': '->', 'color': '#ab382b'}, color='#912f24')
    ax.text(-1.03, 0.9, 'Dee L', weight='bold')
    ax.text(0.65, 0.9, 'Dee R', weight='bold')
    ax.text(-1.1, -1.1, 'Vacuum chamber', color='#536471')
    ax.text(0.88, 0.2, r'$\otimes\ B$', fontsize=15)
    ax.text(0.78, 0.02, 'into page', fontsize=9)
    ax.annotate('Gap: energy kicks', (0, 0.64), (0.06, 1.78), ha='center',
                arrowprops={'arrowstyle': '->', 'color': '#ab382b'}, color='#912f24')
    ax.text(0, -1.68, 'Constant speed on each arc; larger radius after each kick', ha='center', fontsize=10)
    end_y = paths[-1][3][-1]
    ax.annotate('Extraction', (0.14, end_y), (0.82, -1.4),
                arrowprops={'arrowstyle': '->', 'color': '#155e85'}, color='#155e85')
    ax.plot([0, 0.48, 1.13, 1.63], [end_y, end_y, -1.03, -1.03], c='#155e85', lw=2)
    ax.set_xlim(-1.65, 1.85); ax.set_ylim(-1.8, 1.95)
    bx = fig.add_axes([0.64, 0.13, 0.33, 0.75]); bx.axis('off')
    def box(y, label, color='#edf3f6'):
        bx.add_patch(FancyBboxPatch((0.04, y), 0.91, 0.105, boxstyle='round,pad=0.01',
                                   fc=color, ec='#748795', transform=bx.transAxes))
        bx.text(0.495, y + 0.0525, label, ha='center', va='center', transform=bx.transAxes, fontsize=11)
    box(0.80, 'RF oscillator → voltage between dees')
    bx.text(0.5, 0.74, 'One sign reversal per half-turn', ha='center', fontsize=10)
    t = np.linspace(0, 3, 600)
    bx.plot(0.1 + t * 0.26, 0.61 + 0.065 * np.cos(np.pi * t), color='#a73928', lw=1.7)
    for k, label in enumerate(('L → R', 'R → L', 'L → R')):
        xx = 0.1 + k * 0.26
        bx.scatter(xx, 0.61 + 0.065 * (-1) ** k, c='#a73928', s=22)
        bx.text(xx, 0.46, label, ha='center', fontsize=9)
    bx.text(0.5, 0.40, 'Direction and voltage reverse together:\npositive energy gain on both passages', ha='center', fontsize=10)
    box(0.22, 'Deflection / slits → collector', '#eaf3e4')
    bx.annotate('', (0.5, 0.19), (0.5, 0.215), xycoords='axes fraction', arrowprops={'arrowstyle': '->'})
    box(0.07, 'Electrometer → collected current')
    bx.set_xlim(0, 1); bx.set_ylim(0, 1)
    fig.suptitle('A cyclotron reuses the gap: bend, kick, return', fontsize=17, y=0.97)
    fig.text(0.5, 0.025, 'Ideal two-dee functional model • zero-width-gap orbit • illustrative geometry, not a historical reconstruction', ha='center', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
