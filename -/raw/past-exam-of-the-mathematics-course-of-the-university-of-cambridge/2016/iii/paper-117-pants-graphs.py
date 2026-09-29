"""Two genus-three pants graphs related by recutting; writes PNG to cwd.
Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def graph(ax, positions, edges):
    for a, b, curve in edges:
        ax.add_patch(FancyArrowPatch(positions[a], positions[b], arrowstyle='-', connectionstyle=f'arc3,rad={curve}', lw=2.3, color='#356282'))
    for name, (x, y) in positions.items():
        ax.scatter([x], [y], s=640, c='#fff1bf', edgecolors='#333333', linewidths=1.4, zorder=3)
        ax.text(x, y, name, ha='center', va='center', fontsize=13, zorder=4)
    ax.set_xlim(-.4, 2.4)
    ax.set_ylim(-.45, 2.45)
    ax.set_aspect('equal')
    ax.axis('off')

def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), dpi=100, facecolor='white')
    pos = {'A': (0, 2), 'B': (2, 2), 'C': (0, 0), 'D': (2, 0)}
    graph(axes[0], pos, [(a, b, 0) for a, b in [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]])
    pos = {'E': (0, 2), 'F': (2, 2), 'C': (0, 0), 'D': (2, 0)}
    graph(axes[1], pos, [('C', 'E', .19), ('C', 'E', -.19), ('D', 'F', .19), ('D', 'F', -.19), ('C', 'D', 0), ('E', 'F', 0)])
    axes[0].set_title('Four pants, graph K₄', fontsize=13)
    axes[1].set_title('Recut A ∪ B as E ∪ F', fontsize=13)
    fig.text(.5, .04, 'Both graphs: V = 4, E = 6, genus = E − V + 1 = 3', ha='center', fontsize=11)
    fig.subplots_adjust(left=.025, right=.975, top=.86, bottom=.12, wspace=.18)
    fig.savefig(Path.cwd() / 'paper-117-pants-graphs.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
