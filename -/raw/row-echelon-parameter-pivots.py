"""Draw a rectangular row reduction and its two compatibility cases.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

BLUE = '#176b9c'
GOLD = '#986900'
RED = '#b02e38'


def panel(ax, entries, title, note, pivots=(), contradiction=None):
    ax.set(xlim=(-0.85, 4.3), ylim=(-1.45, 4.45))
    ax.axis('off')
    ax.set_title(title, fontsize=15, fontweight='bold', loc='left', pad=10)
    ax.add_patch(Rectangle((1.6, -0.4), 0.8, 4.0,
                           color='#fff3cf', zorder=0))
    ax.add_patch(Rectangle((2.7, -0.4), 1.1, 4.0,
                           color='#e9f3fa', zorder=0))
    if contradiction is not None:
        ax.add_patch(Rectangle((-0.45, 2.6-contradiction), 4.25, 0.8,
                               color='#fce3e5', zorder=1))
    xs = [0, 1, 2, 3.3]
    for i, row in enumerate(entries):
        for j, entry in enumerate(row):
            color = RED if contradiction == i else '#202830'
            ax.text(xs[j], 3-i, f'${entry}$', ha='center', va='center',
                    fontsize=20, color=color, zorder=3)
    for i, j in pivots:
        ax.add_patch(Circle((xs[j], 3-i), 0.33, fill=False,
                            lw=2.2, edgecolor=RED if j == 3 else BLUE,
                            zorder=4))
    ax.plot([-0.55, -0.68, -0.68, -0.55], [-0.4, -0.4, 3.4, 3.4],
            color='#3d4650', lw=1.5)
    ax.plot([3.9, 4.03, 4.03, 3.9], [-0.4, -0.4, 3.4, 3.4],
            color='#3d4650', lw=1.5)
    ax.plot([2.6, 2.6], [-0.4, 3.4], color='#3d4650', lw=1.4)
    ax.text(2, 4.04, '$x_3$', color=GOLD, ha='center', fontsize=12)
    ax.text(3.3, 4.04, 'RHS', color=BLUE, ha='center', fontsize=11)
    ax.text(-0.65, -0.83, note, fontsize=12, va='top', linespacing=1.5)


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 7.5), facecolor='white')
    fig.subplots_adjust(left=0.055, right=0.965, bottom=0.06,
                        top=0.86, wspace=0.28, hspace=0.5)
    fig.suptitle('A right-hand-side pivot decides consistency',
                 fontsize=19, fontweight='bold', y=0.98)
    fig.text(0.5, 0.917,
             r'Four equations, three unknowns; coefficient rank $=2$',
             ha='center', fontsize=13)
    panel(axes[0, 0], [['1', '2', '-1', '1'], ['2', '5', '1', '4'],
                       ['3', '7', '0', r'\tau'], ['1', '3', '2', '3']],
          r'1. Original $[A\mid b(\tau)]$',
          r'$a_{3,:}=a_{1,:}+a_{2,:}$'+'\n'+r'$a_{4,:}=a_{2,:}-a_{1,:}$')
    panel(axes[0, 1], [['1', '2', '-1', '1'], ['0', '1', '3', '2'],
                       ['0', '0', '0', r'\tau-5'], ['0', '0', '0', '0']],
          '2. Echelon form (five operations)',
          r'Compatibility requires $0=\tau-5$.', pivots=[(0, 0), (1, 1)])
    panel(axes[1, 0], [['1', '0', '-7', '-3'], ['0', '1', '3', '2'],
                       ['0', '0', '0', '0'], ['0', '0', '0', '0']],
          r'3a. $\tau=5$: full augmented RREF',
          r'$x_3=t$ is free; $x_1=-3+7t$, $x_2=2-3t$.',
          pivots=[(0, 0), (1, 1)])
    panel(axes[1, 1], [['1', '0', '-7', '0'], ['0', '1', '3', '0'],
                       ['0', '0', '0', '1'], ['0', '0', '0', '0']],
          r'3b. $\tau\ne5$: full augmented RREF',
          'The RHS pivot says $0=1$: no solution.',
          pivots=[(0, 0), (1, 1), (2, 3)], contradiction=2)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
