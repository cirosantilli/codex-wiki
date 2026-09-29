"""Draw an original maximum-flow certificate; Python 3.14, root Matplotlib.

Output paper-35-maximum-flow.png to the caller's current directory.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'paper-35-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.lines import Line2D


def main():
    pos = {1: (0, 0), 2: (1, 1), 3: (1, -1), 4: (2.1, 1),
           5: (2.1, -1), 6: (3.2, 1), 7: (3.2, -1), 8: (4.2, 0)}
    capacity = {(1, 2): 6, (1, 3): 5, (2, 3): 2, (2, 4): 2,
                (2, 5): 3, (3, 5): 4, (5, 4): 1, (4, 6): 4,
                (5, 6): 2, (5, 7): 1, (6, 7): 3, (6, 8): 4, (7, 8): 2}
    flow = {(1, 2): 4, (1, 3): 2, (2, 3): 0, (2, 4): 2,
            (2, 5): 2, (3, 5): 2, (5, 4): 1, (4, 6): 3,
            (5, 6): 2, (5, 7): 1, (6, 7): 1, (6, 8): 4, (7, 8): 2}
    source_side = {1, 2, 3, 5}
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for edge, cap in capacity.items():
        u, v = edge
        is_cut = u in source_side and v not in source_side
        color = '#ba4938' if is_cut else '#35485e' if flow[edge] else '#999999'
        arrow = FancyArrowPatch(pos[u], pos[v], arrowstyle='-|>', mutation_scale=15,
                                shrinkA=15, shrinkB=15, linewidth=1.7, color=color)
        ax.add_patch(arrow)
        dx, dy = pos[v][0] - pos[u][0], pos[v][1] - pos[u][1]
        length = (dx * dx + dy * dy)**0.5
        offset_x, offset_y = -0.11 * dy / length, 0.11 * dx / length
        if edge == (5, 4):
            offset_x, offset_y = 0.16, 0
        ax.text((pos[u][0] + pos[v][0])/2 + offset_x,
                (pos[u][1] + pos[v][1])/2 + offset_y,
                f'{flow[edge]}/{cap}', ha='center', va='center', color=color,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.2})
    for vertex, xy in pos.items():
        face = '#d9e9f6' if vertex in source_side else '#fae6cd'
        ax.add_patch(Circle(xy, 0.135, facecolor=face, edgecolor='#334455', linewidth=1.6, zorder=3))
        ax.text(*xy, str(vertex), ha='center', va='center', fontsize=12, zorder=4)
    handles = [Line2D([], [], marker='o', linestyle='none', markerfacecolor='#d9e9f6',
                      markeredgecolor='#334455', label=r'$S=\{1,2,3,5\}$'),
               Line2D([], [], marker='o', linestyle='none', markerfacecolor='#fae6cd',
                      markeredgecolor='#334455', label=r'$S^c=\{4,6,7,8\}$'),
               Line2D([], [], color='#ba4938', label='Cut capacity = 2 + 1 + 2 + 1 = 6')]
    ax.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, -0.07),
              ncol=3, frameon=False, fontsize=10)
    ax.set_title('Maximum flow 6; arc labels show flow / capacity', pad=15)
    ax.set(xlim=(-0.3, 4.5), ylim=(-1.45, 1.4), aspect='equal')
    ax.axis('off')
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.14, top=0.86)
    fig.savefig('paper-35-maximum-flow.png', dpi=150, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
