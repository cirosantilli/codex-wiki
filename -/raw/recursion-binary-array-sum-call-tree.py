"""Draw an original range-halving sum call tree; write the PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 (no optional dependencies).
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


INK = '#23313d'
BLUE = '#235f91'
GREEN = '#287052'
GRAY = '#85919b'


def main():
    fig, ax = plt.subplots(figsize=(11, 6.7), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 11), ylim=(0, 6.7))
    ax.axis('off')
    ax.text(5.5, 6.32, 'Array sum: combine answers from two smaller ranges',
            ha='center', fontsize=18, weight='bold', color=INK)
    ax.text(5.5, 5.94, 'A = [6, −2, 5, 1]     •     Ranges [l, r) include l and exclude r',
            ha='center', fontsize=13, color=INK)
    # Each tuple: position, range, returned value, invocation entry order.
    nodes = [(5.5, 5.05, '[0, 4)', 10, 1), (2.8, 3.32, '[0, 2)', 4, 2),
             (8.2, 3.32, '[2, 4)', 6, 5), (1.4, 1.58, '[0, 1)', 6, 3),
             (4.1, 1.58, '[1, 2)', -2, 4), (6.9, 1.58, '[2, 3)', 5, 6),
             (9.6, 1.58, '[3, 4)', 1, 7)]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    active = {0, 1, 4}
    for parent, child in edges:
        px, py, *_ = nodes[parent]
        cx, cy, _, value, _ = nodes[child]
        color = BLUE if parent in active and child in active else GRAY
        ax.annotate('', xy=(px + (cx - px) * 0.23, py - 0.43),
                    xytext=(cx + (px - cx) * 0.23, cy + 0.43),
                    arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2})
        ax.text((px + cx) / 2, (py + cy) / 2, f'return {value}',
                ha='center', va='center', fontsize=11, color=GREEN,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    for i, (x, y, interval, value, order) in enumerate(nodes):
        color = BLUE if i in active else GREEN if i == 3 else GRAY
        face = '#eaf3fc' if i in active else '#eaf5ed' if i == 3 else '#f7f8f9'
        ax.add_patch(FancyBboxPatch((x - 1.02, y - 0.39), 2.04, 0.78,
                                  boxstyle='round,pad=0.04', edgecolor=color,
                                  facecolor=face, linewidth=2 if i in active else 1.4))
        label = f'{interval}\n' + (f'sum = {value}' if i < 3 else f'A[{interval[1]}] = {value}')
        ax.text(x, y, label, ha='center', va='center', fontsize=12, color=INK)
        ax.text(x + 0.89, y + 0.32, str(order), ha='center', va='center',
                fontsize=10, weight='bold', color='white',
                bbox={'boxstyle': 'circle,pad=0.16', 'facecolor': color, 'edgecolor': 'white'})
    ax.text(5.5, 0.86, 'Blue path: 3 frames active at call 4.  Green leaf: call 3 has already returned 6.',
            ha='center', fontsize=12, color=INK)
    ax.text(5.5, 0.52, 'The [0, 2) frame retains 6 while its right child reads −2.  Badges: call entry order.',
            ha='center', fontsize=12, color=INK)
    ax.text(5.5, 0.18, '4 entry leaves + 3 combining calls = 7 total calls; 3 additions give 10.',
            ha='center', fontsize=12, weight='bold', color=INK)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
