"""Tile a 252-by-198 rectangle using exact Euclidean division steps."""

from math import gcd
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


def main():
    width, height, x, y, stage = 252, 198, 0, 0, 0
    colors = ['#9ac5e5', '#f3c277', '#a7c49b', '#bfafd4']
    squares = []
    while width and height:
        side = min(width, height)
        count = max(width, height) // side
        for k in range(count):
            sx = x + k * side if width >= height else x
            sy = y if width >= height else y + k * side
            squares.append((sx, sy, side, stage))
        if width >= height:
            x += count * side
            width -= count * side
        else:
            y += count * side
            height -= count * side
        stage += 1
    assert [s[2] for s in squares] == [198, 54, 54, 54, 36, 18, 18]
    assert sum(s[2] ** 2 for s in squares) == 252 * 198
    assert gcd(252, 198) == min(s[2] for s in squares) == 18
    assert 4 * 252 - 5 * 198 == 18
    plt.rcParams.update({'font.size': 12})
    fig, (ax, steps) = plt.subplots(1, 2, figsize=(10.5, 5.1), layout='constrained',
                                   facecolor='white', gridspec_kw={'width_ratios': [1.5, 1]})
    for sx, sy, side, group in squares:
        ax.add_patch(Rectangle((sx, sy), side, side, facecolor=colors[group],
                               edgecolor='white', linewidth=2))
        ax.text(sx + side / 2, sy + side / 2, str(side), ha='center', va='center',
                fontsize=10 if side == 18 else 12, color='#16232d')
    ax.add_patch(Rectangle((0, 0), 252, 198, fill=False, edgecolor='#333333'))
    ax.set(aspect='equal', xlim=(-5, 257), ylim=(-5, 203), xticks=[0, 198, 252],
           yticks=[0, 198], xlabel='Length', ylabel='Length', title='Numbers label square side lengths')
    steps.axis('off')
    steps.text(0, .98, 'Successive divisions', fontsize=14, va='top')
    labels = ['252 = 1 × 198 + 54', '198 = 3 × 54 + 36',
              '54 = 1 × 36 + 18', '36 = 2 × 18 + 0']
    steps.legend(handles=[Patch(facecolor=c, label=l) for c, l in zip(colors, labels)],
                 loc='upper left', bbox_to_anchor=(-.03, .84), frameon=False, labelspacing=1.4)
    steps.text(0, .32, 'Final nonzero remainder: 18\ngcd(252, 198) = 18', fontsize=13, va='top')
    steps.text(0, .13, 'Back-substitution:\n18 = 4 × 252 − 5 × 198', fontsize=12, va='top')
    fig.suptitle('Removing squares is a geometric form of the Euclidean algorithm', fontsize=15)
    fig.savefig(Path.cwd() / 'euclidean-algorithm-rectangles.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
