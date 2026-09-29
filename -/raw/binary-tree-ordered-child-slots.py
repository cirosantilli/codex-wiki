"""Draw ordered child slots; tested with Python 3.14 and matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

INK = '#243449'
BLUE = '#dceafb'
GREY = '#8290a0'


def draw(ax, nodes, children, title, note):
    ax.set_aspect('equal')
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-0.8, 3.45)
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold', color=INK, pad=10)
    for name, (x, y) in nodes.items():
        for slot, child in zip(('L', 'R'), children.get(name, (None, None))):
            direction = -1 if slot == 'L' else 1
            if child is None:
                end = (x + direction * 0.36, y - 0.50)
                ax.plot([x, end[0]], [y, end[1]], '--', color=GREY, lw=1.25, zorder=1)
                ax.add_patch(Rectangle((end[0] - 0.065, end[1] - 0.065), 0.13, 0.13,
                                       facecolor='white', edgecolor=GREY, lw=1.2, zorder=2))
                label = (x + direction * 0.27, y - 0.19)
            else:
                end = nodes[child]
                ax.plot([x, end[0]], [y, end[1]], color=INK, lw=1.8, zorder=1)
                label = ((x + end[0]) / 2 + direction * 0.11, (y + end[1]) / 2 + 0.10)
            ax.text(*label, slot, ha='center', va='center', fontsize=9, color=INK,
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 0.3}, zorder=3)
    for name, (x, y) in nodes.items():
        ax.add_patch(Circle((x, y), 0.17, facecolor=BLUE, edgecolor=INK, lw=1.6, zorder=4))
        ax.text(x, y, name, ha='center', va='center', fontsize=11, color=INK, zorder=5)
    ax.text(0, -0.68, note, ha='center', fontsize=11, color=INK)


def main():
    fig, axes = plt.subplots(1, 4, figsize=(12, 4.8), facecolor='white')
    draw(axes[0], {'A': (0, 2.8), 'B': (-0.8, 1.75)}, {'A': ('B', None)},
         'Only a left child', 'n = 2, h = 1\n3 empty child slots')
    draw(axes[1], {'A': (0, 2.8), 'B': (0.8, 1.75)}, {'A': (None, 'B')},
         'Only a right child', 'n = 2, h = 1\n3 empty child slots')
    draw(axes[2], {'A': (0, 2.8), 'B': (-0.85, 1.75), 'C': (-0.35, 0.7), 'D': (0.85, 1.75)},
         {'A': ('B', 'D'), 'B': (None, 'C')}, 'A mixed shape',
         'n = 4, h = 2\n5 empty child slots')
    draw(axes[3], {'A': (-0.8, 2.8), 'B': (-0.3, 2.0), 'C': (0.2, 1.2), 'D': (0.7, 0.4)},
         {'A': (None, 'B'), 'B': (None, 'C'), 'C': (None, 'D')}, 'A right-child chain',
         'n = 4, h = 3\n5 empty child slots')
    fig.suptitle('Binary trees distinguish LEFT and RIGHT slots', fontsize=18, color=INK, y=0.96)
    fig.text(0.5, 0.055, 'Circle: vertex    Square: empty slot    L / R: slot name    h: longest root-to-leaf path in edges',
             ha='center', fontsize=11, color=INK)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.80, bottom=0.17, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
