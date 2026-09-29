"""Original exact probability-area diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes its own PNG basename to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    weights = np.arange(1, 7) / 21
    edges = np.concatenate(([0.0], np.cumsum(weights)))
    colors = ['#246ca6', '#246ca6', '#c76624', '#c76624', '#38855e', '#38855e']
    fig, ax = plt.subplots(figsize=(9, 4.6), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.065, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle('Adding probability by grouping disjoint outcomes', fontsize=16, y=0.96)
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.19, 1.53)
    ax.axis('off')
    ax.text(0, 1.43, r'Exact model: $\Omega=\{1,2,3,4,5,6\}$,  $P(\{k\})=k/21$', fontsize=12)
    ax.text(0, 1.24, 'Individual outcomes (equal height; width = probability)', fontsize=11)
    for k, (left, width, color) in enumerate(zip(edges[:-1], weights, colors), start=1):
        ax.add_patch(Rectangle((left, 0.80), width, 0.32, facecolor=color,
                               edgecolor='white', linewidth=2))
        ax.text(left + width / 2, 0.97, str(k), ha='center', va='center',
                color='white', fontsize=13, fontweight='bold')
        ax.text(left + width / 2, 0.73, f'{k}/21', ha='center', va='center', fontsize=10)
    ax.text(0, 0.56, 'Same mass, regrouped into three disjoint events', fontsize=11)
    for start, stop, name, color in [(0, 2, 'A', colors[0]), (2, 4, 'B', colors[2]), (4, 6, 'C', colors[4])]:
        left, width = edges[start], edges[stop] - edges[start]
        total = sum(range(start + 1, stop + 1))
        ax.add_patch(Rectangle((left, 0.13), width, 0.32, facecolor=color,
                               edgecolor='white', linewidth=2))
        ax.text(left + width / 2, 0.29, f'{name}: {total}/21', ha='center', va='center',
                color='white', fontsize=12)
    ax.annotate('', xy=(0, 0.05), xytext=(edges[4], 0.05),
                arrowprops={'arrowstyle': '|-|', 'color': '#333333', 'lw': 1.4})
    ax.text(edges[4] / 2, -0.055, r'$P(A\cup B)=3/21+7/21=10/21$',
            ha='center', va='top', fontsize=11)
    ax.text(0.73, -0.055, r'$P(\Omega)=21/21=1$', ha='center', va='top', fontsize=11)
    fig.text(0.065, 0.025, 'Mathematical area model, not measured frequencies. All region widths use the same probability scale.',
             fontsize=10, color='#444444')
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
