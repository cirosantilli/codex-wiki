#!/usr/bin/env python3
"""Draw the solution dendrogram; run from the mirrored _media directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5, as declared
in the repository's root pyproject.toml. Writes only a PNG in the cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def complete_linkage(distances):
    """Return (left, right, height, members) merges with deterministic ties."""
    active = {i: (i,) for i in range(len(distances))}
    merges = []
    while len(active) > 1:
        ids = sorted(active)
        height, left, right = min(
            (max(distances[i, j] for i in active[a] for j in active[b]), a, b)
            for pos, a in enumerate(ids) for b in ids[pos + 1:]
        )
        members = active.pop(left) + active.pop(right)
        active[len(distances) + len(merges)] = members
        merges.append((left, right, float(height), members))
    return merges


def main():
    distances = np.array([
        [0, 1.41, 2.68, .67, 3.01],
        [1.41, 0, 2.95, 1.19, 2.37],
        [2.68, 2.95, 0, 2.19, 2.82],
        [.67, 1.19, 2.19, 0, 3.32],
        [3.01, 2.37, 2.82, 3.32, 0],
    ])
    merges = complete_linkage(distances)
    assert [m[2] for m in merges] == [.67, 1.41, 2.82, 3.32]
    order = [0, 3, 1, 2, 4]
    positions = {leaf: (float(pos), 0.) for pos, leaf in enumerate(order)}
    blue, orange = '#2476a3', '#c06c22'
    fig, ax = plt.subplots(figsize=(6.8, 3.9), facecolor='white')
    ax.set_facecolor('white')
    for node, (left, right, height, members) in enumerate(merges, 5):
        xl, yl = positions[left]
        xr, yr = positions[right]
        color = blue if set(members) <= {0, 1, 3} else orange
        if len(members) == 5:
            color = '#444444'
        ax.plot([xl, xl, xr, xr], [yl, height, height, yr], color=color, lw=2.3)
        center = (xl + xr) / 2
        positions[node] = (center, height)
        ax.annotate(f'{height:.2f}', (center, height), xytext=(0, 7),
                    textcoords='offset points', ha='center', fontsize=10)
    ax.axhline(3.05, color='#777777', lw=1, ls='--')
    ax.text(4.28, 3.05, 'two-cluster cut', ha='right', va='bottom', fontsize=9,
            color='#555555', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    ax.set_xticks(range(5), [str(i + 1) for i in order])
    ax.set_xlim(-.4, 4.4)
    ax.set_ylim(0, 3.7)
    ax.set_xlabel('Observation')
    ax.set_ylabel('Complete-linkage distance')
    ax.set_title('Complete linkage after removing observation 6', pad=14)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', alpha=.15)
    ax.set_axisbelow(True)
    fig.tight_layout()
    output = Path(Path(__file__).stem + '.png')
    fig.savefig(output, dpi=150, facecolor='white', transparent=False)
    plt.close(fig)
    print(output)


if __name__ == '__main__':
    main()
