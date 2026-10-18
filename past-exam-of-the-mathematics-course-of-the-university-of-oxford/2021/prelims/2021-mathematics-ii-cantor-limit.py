"""Partial Cantor construction and a direct limit at 1/4; write PNG in cwd.

Uses the root pyproject.toml environment; tested with Python 3.14.4.
No values are assigned to the residual set and no gaps are joined.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def assigned_segments(rounds):
    """Return closed assigned thirds and the remaining open intervals."""
    gaps = [(0.0, 1.0, 0.0, 1.0)]
    segments = []
    for _ in range(rounds):
        new_gaps = []
        for left, right, low, high in gaps:
            a = left + (right-left)/3
            b = right - (right-left)/3
            mid = (low+high)/2
            segments.append((a, b, mid))
            new_gaps.extend([(left, a, low, mid), (b, right, mid, high)])
        gaps = new_gaps
    return segments, gaps


def main():
    plt.rcParams.update({'font.size': 11, 'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), layout='constrained')
    blue, orange = '#176ba0', '#bb5327'
    for ax, rounds in zip(axes, [2, 6]):
        segments, _ = assigned_segments(rounds)
        for a, b, y in segments:
            ax.plot([a, b], [y, y], color=blue, lw=2.0, solid_capstyle='butt')
        ax.scatter([0, 1], [0, 1], color=blue, s=15, zorder=4)
        ax.set(xlim=(-.025, 1.025), ylim=(-.04, 1.04), xlabel='$t$', ylabel='$f(t)$',
               title=f'After {rounds} rounds: assigned values only')
        ax.set_xticks([0, .25, 1/3, 2/3, 1], ['0', '1/4', '1/3', '2/3', '1'])
        ax.set_yticks([0, 1/3, .5, 1], ['0', '1/3', '1/2', '1'])
        ax.grid(alpha=.15)
        ax.spines[['top', 'right']].set_visible(False)
    ax = axes[1]
    ax.axvline(.25, color=orange, ls='--', lw=1)
    ax.axhline(1/3, color=orange, ls='--', lw=1)
    for m in [1, 2]:
        left = (1-9.0**(-m))/4
        right = .25 + .75*9.0**(-m)
        low = (1-4.0**(-m))/3
        high = 1/3 + (2/3)*4.0**(-m)
        ax.add_patch(Rectangle((left, low), right-left, high-low,
                               facecolor='none', edgecolor=orange, lw=1.2))
    ax.annotate('Nested endpoint bounds', xy=(.33, .49), xytext=(.45, .70),
                arrowprops={'arrowstyle': '->', 'color': orange}, color=orange)
    ax.text(.49, .15, '$t\\to1/4$ on the defined set\n$\\Longrightarrow f(t)\\to1/3$',
            ha='left', color=orange)
    fig.savefig(Path.cwd()/'2021-mathematics-ii-cantor-limit.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
