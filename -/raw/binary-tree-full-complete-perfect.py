"""Draw independent examples of three tree shape conditions.

Tested with Python 3.14 and matplotlib 3.10.7. Integer positions encode
left/right paths, rather than imposing an ordering on stored values.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

INK = '#243449'
BLUE = '#dceafb'
GREY = '#a8b2bf'


def position(i):
    depth = i.bit_length() - 1
    offset = i - 2 ** depth
    return (-1.5 + 3 * (offset + 0.5) / 2 ** depth, 2.8 - depth * 0.85)


def panel(ax, occupied, title, verdict):
    ax.set_aspect('equal')
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-0.10, 3.5)
    ax.axis('off')
    ax.set_title(title, fontsize=13, color=INK, fontweight='bold', pad=5)
    depth = max(occupied).bit_length() - 1
    for i in range(1, 2 ** (depth + 1)):
        x, y = position(i)
        if i in occupied:
            if i > 1:
                px, py = position(i // 2)
                ax.plot([px, x], [py, y], color=INK, lw=1.5, zorder=1)
            ax.add_patch(Circle((x, y), 0.13, facecolor=BLUE, edgecolor=INK, lw=1.5, zorder=3))
            ax.text(x, y, chr(64 + sorted(occupied).index(i) + 1), ha='center', va='center',
                    color=INK, fontsize=9, zorder=4)
        else:
            ax.add_patch(Circle((x, y), 0.11, facecolor='white', edgecolor=GREY,
                                linestyle='--', lw=1.1, zorder=2))
    ax.text(0, 0.30, verdict, ha='center', va='center', color=INK, fontsize=11,
            linespacing=1.5)


def main():
    fig, axes = plt.subplots(2, 3, figsize=(10.4, 7.5), facecolor='white')
    examples = [
        ({1, 2, 3, 4, 5, 6, 7}, 'Every level filled', 'Full: yes   Complete: yes\nPerfect: yes'),
        ({1, 2, 3, 6, 7}, 'A gap before the last leaves', 'Full: yes   Complete: no\nPerfect: no'),
        ({1, 2, 3, 4, 5, 6}, 'One child at C', 'Full: no   Complete: yes\nPerfect: no'),
        ({1, 2, 3, 4, 5}, 'Both full and complete', 'Full: yes   Complete: yes\nPerfect: no'),
        ({1, 3}, 'Only a right child', 'Full: no   Complete: no\nPerfect: no'),
        ({1}, 'One vertex is enough', 'Full: yes   Complete: yes\nPerfect: yes'),
    ]
    for ax, (occupied, title, verdict) in zip(axes.flat, examples):
        panel(ax, occupied, title, verdict)
    fig.suptitle('Full, complete, and perfect are different conditions', fontsize=17, color=INK, y=0.975)
    fig.text(0.5, 0.034, 'Full: 0 or 2 children per vertex    Complete: levels filled from the left    Perfect: every level filled',
             ha='center', fontsize=10.5, color=INK)
    fig.text(0.5, 0.010, 'Dashed circles show unoccupied positions in the displayed levels; they are not vertices.',
             ha='center', fontsize=10, color=INK)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.88, bottom=0.09, hspace=0.30, wspace=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
