"""Draw tensor coefficient grids; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; output has this script's basename in the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

BLUE = '#206b98'
GREEN = '#21745b'

def grid(ax, x, y, values, size=0.62, color=BLUE, labels=False):
    values = np.asarray(values)
    for i in range(2):
        for j in range(2):
            xx, yy = x + j * size, y + (1 - i) * size
            ax.add_patch(Rectangle((xx, yy), size, size, facecolor='#f0f6fa' if values[i, j] else 'white', edgecolor=color, linewidth=1.5))
            ax.text(xx + size/2, yy + size/2, str(values[i, j]), ha='center', va='center', fontsize=18, color=color)
    if labels:
        for j in range(2):
            ax.text(x+(j+.5)*size, y+2*size+.14, rf'$f_{j+1}$', ha='center', fontsize=13)
        for i in range(2):
            ax.text(x-.20, y+(1.5-i)*size, rf'$e_{i+1}$', ha='center', va='center', fontsize=13)


def main():
    fig, ax = plt.subplots(figsize=(9.6, 5.3), dpi=110, facecolor='white')
    ax.set(xlim=(0, 9.6), ylim=(0, 5.3))
    ax.axis('off')
    ax.text(.25, 5.06, 'Tensor coefficients: one product versus a sum', fontsize=19, weight='bold', va='top')
    ax.text(.32, 4.3, 'One pure tensor', fontsize=15, weight='bold', color=BLUE)
    ax.text(.32, 3.65, r'$v=(2,1),\quad w=(-1,3)$', fontsize=16)
    ax.text(.32, 3.05, r'$C(v\otimes w)=vw^T$', fontsize=17)
    grid(ax, 4.0, 2.95, np.outer([2, 1], [-1, 3]), labels=True)
    ax.text(5.75, 3.95, 'Columns share one direction', fontsize=14)
    ax.text(5.75, 3.45, r'column 2 = $-3$ × column 1', fontsize=13)
    ax.text(5.75, 2.97, 'matrix rank = 1; determinant = 0', fontsize=13, color=BLUE)
    ax.plot([.25, 9.3], [2.62, 2.62], color='#ccd6db')
    ax.text(.32, 2.27, 'Two pure tensors', fontsize=15, weight='bold', color=GREEN)
    ax.text(.32, 1.69, r'$t=e_1\otimes f_1+e_2\otimes f_2$', fontsize=16)
    grid(ax, 4.0, .70, [[1, 0], [0, 1]], color=GREEN)
    ax.text(5.42, 1.29, '=', fontsize=23, va='center')
    grid(ax, 5.91, .70, [[1, 0], [0, 0]], color=GREEN)
    ax.text(7.36, 1.29, '+', fontsize=23, va='center')
    grid(ax, 7.86, .70, [[0, 0], [0, 1]], color=GREEN)
    ax.text(4.62, .40, r'$C(t)$', ha='center', fontsize=13)
    ax.text(6.53, .40, r'$C(e_1\otimes f_1)$', ha='center', fontsize=13)
    ax.text(8.48, .40, r'$C(e_2\otimes f_2)$', ha='center', fontsize=13)
    ax.text(.32, .81, 'matrix rank = 2', fontsize=14, color=GREEN)
    ax.text(.32, .37, 'No single outer product gives this grid.', fontsize=12)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
