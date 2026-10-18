"""Original hop-count weight bands. Python 3.14.4, Matplotlib 3.10.7.

Run from any working directory; writes the PNG into that directory.
"""

import os
from pathlib import Path

os.environ['MPLCONFIGDIR'] = '/tmp/oxford-matplotlib'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    n = 8
    fig, ax = plt.subplots(figsize=(7.6, 3.8), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    for hops in range(1, n):
        upper = hops * (1 + 1 / n)
        assert upper < hops + 1
        ax.plot([hops, upper], [hops, hops], color='#176b8c',
                linewidth=8, solid_capstyle='butt')
        ax.plot([hops, upper], [hops, hops], 'o', color='#176b8c',
                markersize=4)
        ax.plot([upper, hops + 1], [hops, hops], color='#b65317',
                linewidth=1.5, linestyle=':')
    ax.set_xlim(0.7, 8.25)
    ax.set_ylim(0.5, 7.7)
    ax.set_xticks(range(1, 9))
    ax.set_yticks(range(1, 8))
    ax.set_xlabel('Total path weight')
    ax.set_ylabel('Number of edges in a simple path')
    ax.set_title('Nearly unit weights: fewer hops always win', pad=13)
    ax.text(0.02, 0.97, 'n = 8; each edge weight is in [1, 1 + 1/8]',
            transform=ax.transAxes, va='top', fontsize=9)
    ax.grid(axis='x', color='#dddddd', linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False,
                metadata={'Software': 'Matplotlib; original generated diagram'})
    plt.close(fig)


if __name__ == '__main__':
    main()
