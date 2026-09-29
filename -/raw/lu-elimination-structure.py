"""Original LU elimination diagram; writes its matching PNG in the CWD.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def matrix(ax, x, y, values, label, pivot=None, lower=False):
    cell = 0.47
    ax.text(x + 1.5 * cell, y + 0.35, label, ha='center', fontsize=15)
    for i, row in enumerate(values):
        for j, value in enumerate(row):
            face = '#ffffff'
            if pivot == (i, j):
                face = '#ffe2a1'
            elif lower and i > j:
                face = '#dbece5'
            elif value == 0:
                face = '#f0f3f6'
            ax.add_patch(Rectangle((x+j*cell, y-(i+1)*cell), cell, cell,
                                   facecolor=face, edgecolor='#bac4ce', lw=0.8))
            ax.text(x+(j+0.5)*cell, y-(i+0.5)*cell, str(value),
                    ha='center', va='center', fontsize=15,
                    color='#8b969f' if value == 0 else '#172c40')


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    a = np.array([[2,1,1],[4,5,3],[-2,8,4]])
    a1 = np.array([[2,1,1],[0,3,1],[0,9,5]])
    l = np.array([[1,0,0],[2,1,0],[-1,3,1]])
    u = np.array([[2,1,1],[0,3,1],[0,0,2]])
    assert np.array_equal(l @ u, a)
    fig, ax = plt.subplots(figsize=(9.4, 6.1), facecolor='white')
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.025, top=0.97)
    ax.set(xlim=(0,9.4), ylim=(0,6.1)); ax.axis('off')
    ax.text(4.7, 5.85, 'Elimination zeros go into U; multipliers go into L',
            ha='center', fontsize=17, fontweight='bold', color='#172c40')
    matrix(ax, 0.5, 5.1, a, '$A$', pivot=(0,0))
    matrix(ax, 3.95, 5.1, a1, '$A^{(1)}$', pivot=(1,1))
    matrix(ax, 7.4, 5.1, u, '$U$', pivot=(2,2))
    for x0, x1 in [(2.07,3.77),(5.52,7.22)]:
        ax.annotate('', xy=(x1,4.36), xytext=(x0,4.36),
                    arrowprops={'arrowstyle':'->','lw':2,'color':'#31678d'})
    ax.text(2.92, 3.22, '$R_2 \\leftarrow R_2-2R_1$\n$R_3 \\leftarrow R_3+R_1$',
            ha='center', va='center', fontsize=13)
    ax.text(6.38, 3.22, '$R_3 \\leftarrow R_3-3R_2$', ha='center', va='center', fontsize=13)
    ax.plot([0.4,9.0],[2.75,2.75],color='#d8dee5',lw=1)
    matrix(ax, 0.7, 2.1, l, '$L$', lower=True)
    ax.text(2.35, 1.35, r'$\times$', ha='center', fontsize=24)
    matrix(ax, 2.7, 2.1, u, '$U$')
    ax.text(4.4, 1.35, '$=$', ha='center', fontsize=24)
    matrix(ax, 4.75, 2.1, a, '$A$')
    ax.text(6.6, 1.5, 'Store the multipliers,\nnot their negatives.\n\nThe second multiplier uses\nthe updated entry: 9/3 = 3.',
            va='center', fontsize=12, linespacing=1.5, color='#244636')
    ax.text(4.7, 0.2, 'Unpivoted teaching example • pivots 2, 3, 2 • exact integer factors',
            ha='center', fontsize=11, color='#52606d')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
