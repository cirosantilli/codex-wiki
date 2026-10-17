"""Triangular domain of an iterated integral. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(6.5, 4.6), dpi=120, layout='constrained')
    ax.fill([0, 2, 1], [0, 0, 1], color='#dcecf2', zorder=1)
    ax.plot([0, 1, 2, 0], [0, 1, 0, 0], color='#267897', lw=2, zorder=2)
    yy = .42
    ax.annotate('', xy=(2-yy, yy), xytext=(yy, yy), arrowprops={'arrowstyle': '<->', 'color': '#ad5f25', 'lw': 2})
    ax.text(1, yy+.065, r'$y\leq x\leq2-y$', ha='center', color='#934b18')
    ax.plot([0, yy], [yy, yy], '--', color='.6', lw=.8)
    ax.text(-.08, yy, 'y', ha='right', va='center')
    for point, label, offset in [((0, 0), '(0,0)', (-12, -19)), ((2, 0), '(2,0)', (-6, -19)), ((1, 1), '(1,1)', (-16, 9))]:
        ax.scatter(*point, color='#164f68', s=30, zorder=3)
        ax.annotate(label, point, xytext=offset, textcoords='offset points')
    ax.text(.23, .65, r'$x=y$', rotation=45, color='#164f68')
    ax.text(1.42, .69, r'$x=2-y$', rotation=-45, color='#164f68')
    ax.text(1, -.13, r'$y=0$', ha='center', color='#164f68')
    ax.set(xlim=(-.25, 2.3), ylim=(-.22, 1.3), xlabel='x', ylabel='y', title=r'$0\leq y\leq1,\quad y\leq x\leq2-y$', xticks=[0, 1, 2], yticks=[0, 1])
    ax.set_aspect('equal')
    ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
