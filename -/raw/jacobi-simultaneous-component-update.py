"""Draw the information flow of two original three-variable update sweeps.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; emits this script's basename.png into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

BLUE = '#2563a6'
ORANGE = '#ba4e17'
INK = '#1e293b'


def box(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012',
                              facecolor='white', edgecolor=color, linewidth=1.7,
                              zorder=3))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=13,
            color=INK, zorder=4)


def arrow(ax, start, end, color, bend=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=14,
                                color=color, linewidth=1.8,
                                connectionstyle=f'arc3,rad={bend}', zorder=2))


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), dpi=120, facecolor='white')
    fig.subplots_adjust(left=.025, right=.975, top=.745, bottom=.15, wspace=.12)
    fig.suptitle('Same equations, different information flow', fontsize=20,
                 color=INK, y=.97)
    fig.text(.5, .865, r'$4x_1-x_2=2,\quad -x_1+4x_2-x_3=4,\quad -x_2+4x_3=10$'
             '\nStarting vector: (0, 0, 0)', ha='center', va='center', fontsize=14, color=INK)
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis('off')
    left, right = axes
    left.text(.5, 1.03, 'Jacobi: all inputs from the old vector', ha='center',
              fontsize=14, weight='bold', color=BLUE)
    ys = [.74, .44, .14]
    for i, y in enumerate(ys, 1):
        box(left, .025, y, .23, .14, rf'$x_{i}^{{(0)}}=0$', BLUE)
    formulas = [r'$x_1^{(1)}=(2+0)/4=1/2$',
                r'$x_2^{(1)}=(4+0+0)/4=1$',
                r'$x_3^{(1)}=(10+0)/4=5/2$']
    for y, label in zip(ys, formulas):
        box(left, .47, y, .49, .14, label, ORANGE)
    for source, target in [(1, 0), (0, 1), (2, 1), (1, 2)]:
        arrow(left, (.265, ys[source]+.07), (.457, ys[target]+.07), BLUE)
    left.text(.12, .975, 'Frozen inputs', ha='center', color=BLUE, fontsize=11)
    left.text(.715, .975, 'New outputs', ha='center', color=ORANGE, fontsize=11)
    left.text(.5, -.05, 'Replace the old vector only after the whole sweep.',
              ha='center', fontsize=11, color=INK)
    right.text(.5, 1.03, 'Gauss-Seidel: use each new value immediately', ha='center',
               fontsize=14, weight='bold', color=ORANGE)
    gs_formulas = [r'$x_1^{(1)}=(2+0)/4=1/2$',
                   r'$x_2^{(1)}=(4+1/2+0)/4=9/8$',
                   r'$x_3^{(1)}=(10+9/8)/4=89/32$']
    for y, label in zip(ys, gs_formulas):
        box(right, .095, y, .81, .14, label, ORANGE)
    for i, label in [(0, r'new $x_1^{(1)}=1/2$'), (1, r'new $x_2^{(1)}=9/8$')]:
        arrow(right, (.26, ys[i]-.017), (.26, ys[i+1]+.157), ORANGE)
        right.text(.31, (ys[i]+ys[i+1])/2+.07, label, color=ORANGE,
                   va='center', fontsize=12)
    right.text(.5, .965, r'Old $x_2^{(0)}=0$ and $x_3^{(0)}=0$ where still needed',
               ha='center', fontsize=11, color=BLUE)
    right.text(.5, -.05, 'Later rows read the newly updated coordinates.',
               ha='center', fontsize=11, color=INK)
    fig.text(.5, .035, 'Blue: old data     Orange: new data     Coordinate order: 1, 2, 3',
             ha='center', color=INK, fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
