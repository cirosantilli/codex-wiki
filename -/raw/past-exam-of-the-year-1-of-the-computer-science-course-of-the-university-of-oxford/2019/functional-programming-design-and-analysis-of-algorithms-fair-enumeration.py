"""Original diagonal-enumeration diagram. Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Writes its PNG to the current working directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    rounds = np.add.outer(np.arange(5), np.arange(6))
    fig, ax = plt.subplots(figsize=(6.5, 3.7), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    im = ax.imshow(rounds, cmap='YlGnBu', vmin=0, vmax=9, interpolation='nearest')
    for i in range(5):
        for j in range(6):
            ax.text(j, i, f'({i}, {j})', ha='center', va='center', fontsize=10,
                    color='white' if i+j >= 5 else '#172131')
    ax.set_xticks(np.arange(6))
    ax.set_yticks(np.arange(5))
    ax.set_xticks(np.arange(-0.5, 6, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 5, 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=2)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.set_xlabel('Position within a row, j', fontsize=10)
    ax.set_ylabel('Input row, i', fontsize=10)
    bar = fig.colorbar(im, ax=ax, pad=0.04, fraction=0.05, ticks=np.arange(10))
    bar.set_label('Output round = i + j', fontsize=10)
    fig.suptitle('Every entry has a finite output round', fontsize=13, y=0.98)
    fig.text(0.5, 0.905, 'Row i enters in round i; every active row advances once per round.',
             ha='center', fontsize=9)
    fig.subplots_adjust(left=0.1, right=0.84, bottom=0.14, top=0.84)
    target = Path.cwd() / (Path(__file__).stem + '.png')
    fig.savefig(target, dpi=120, facecolor='white', transparent=False,
                metadata={'Title': 'Original diagonal merging of lazy lists'})
    plt.close(fig)


if __name__ == '__main__':
    main()
