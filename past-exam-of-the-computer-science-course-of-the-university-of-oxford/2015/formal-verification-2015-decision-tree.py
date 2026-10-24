"""Draw the full tree in Oxford CAFV 2015 Q1(c); output in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(11.5, 5.8), dpi=100, facecolor='white')
    ax.set_facecolor('white')
    levels = [[3.5], [1.5, 5.5], [.5, 2.5, 4.5, 6.5], list(range(8))]
    values = [0, 0, 1, 1, 0, 1, 1, 1]
    for depth in range(3):
        for i, x in enumerate(levels[depth]):
            for bit in (0, 1):
                x2 = levels[depth + 1][2 * i + bit]
                p = (x, 3 - depth)
                q = (x2, 2 - depth)
                ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=13,
                    linewidth=1.5, linestyle='--' if bit == 0 else '-',
                    shrinkA=14, shrinkB=14, color='#222222'))
    for depth in range(3):
        for x in levels[depth]:
            ax.add_patch(Circle((x, 3 - depth), .16, facecolor='white', edgecolor='black', lw=1.5, zorder=3))
            ax.text(x, 3 - depth, ['z', 'y', 'x'][depth], ha='center', va='center', fontsize=16, zorder=4)
    for x, value in zip(levels[3], values):
        ax.add_patch(Rectangle((x - .17, -.16), .34, .32, facecolor='white', edgecolor='black', lw=1.5, zorder=3))
        ax.text(x, 0, str(value), ha='center', va='center', fontsize=15, zorder=4)
        ax.text(x, -.42, format(x, '03b'), ha='center', va='center', fontsize=12, color='#444444')
    ax.text(3.5, -.72, 'Leaf labels: (z, y, x)       Dashed edge = 0       Solid edge = 1', ha='center', fontsize=13)
    ax.set_title('Complete decision tree: z < y < x', fontsize=18, pad=15)
    ax.set_xlim(-.55, 7.55)
    ax.set_ylim(-.95, 3.4)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.tight_layout(pad=1.2)
    fig.savefig(Path('formal-verification-2015-decision-tree.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
