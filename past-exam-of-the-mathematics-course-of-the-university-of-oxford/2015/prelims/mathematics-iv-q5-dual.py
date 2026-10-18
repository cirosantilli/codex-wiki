"""Original dual-region sketch; run from mirrored _media. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 4.3, 900)
    boundary = np.maximum.reduce([np.zeros_like(x), x - 1, 3 - 0.75 * x, 6 - 3 * x])
    fig, ax = plt.subplots(figsize=(7.2, 5.4), facecolor='white', layout='constrained')
    ax.set_facecolor('white')
    ax.fill_between(x, boundary, 7, color='#d8eaf1', label='Feasible region')
    ax.plot(x, 6 - 3 * x, '--', color='#b37520', lw=1.2, label=r'$3y_1+y_2=6$')
    ax.plot(x, 3 - 0.75 * x, '--', color='#476e32', lw=1.2, label=r'$3y_1+4y_2=12$')
    ax.plot(x, x - 1, '--', color='#6d5792', lw=1.2, label=r'$-y_1+y_2=-1$')
    ax.plot(x, boundary, color='#1e607b', lw=2.2)
    ax.plot(x, 14 / 3 - 2 * x, color='#b5412e', lw=1.6, label=r'$2y_1+y_2=14/3$')
    vertices = [(0, 6), (4 / 3, 2), (16 / 7, 9 / 7)]
    ax.scatter(*np.array(vertices).T, color='#1e607b', s=24, zorder=5)
    for point, label, offset in [
        (vertices[0], r'$(0,6)$', (10, 8)),
        (vertices[1], r'$(4/3,2)$', (10, 15)),
        (vertices[2], r'$(16/7,9/7)$', (13, -19)),
    ]:
        ax.annotate(label, point, xytext=offset, textcoords='offset points', fontsize=10)
    ax.text(2.7, 5.8, 'Feasible region', color='#1e607b', fontsize=12)
    ax.set(xlim=(0, 4.3), ylim=(0, 7), xlabel=r'$y_1$', ylabel=r'$y_2$',
           title='The lowest objective line touches at $(4/3,2)$')
    ax.legend(loc='upper right', bbox_to_anchor=(1, 0.79), fontsize=9, framealpha=0.95)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(alpha=0.18)
    fig.savefig(Path('mathematics-iv-q5-dual.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
