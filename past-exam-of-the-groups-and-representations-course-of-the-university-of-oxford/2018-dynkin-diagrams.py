"""Draw the root diagrams from their bonds. Python 3.14, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.size': 13, 'figure.facecolor': 'white'})
BLUE = '#205c96'
BLACK = '#222222'
RED = '#a6342a'


def bond(ax, p, q, double=False, color=BLACK):
    if double:
        for offset in (-0.055, 0.055):
            ax.plot([p[0], q[0]], [p[1]+offset, q[1]+offset], color=color, linewidth=1.8)
        midpoint = (p[0]+q[0])/2
        ax.plot([midpoint-0.08, midpoint+0.08, midpoint-0.08],
                [p[1]+0.15, p[1], p[1]-0.15], color=color, linewidth=1.8)
    else:
        ax.plot([p[0], q[0]], [p[1], q[1]], color=color, linewidth=2)


def node(ax, p, label, color=BLACK, above=False):
    ax.add_patch(Circle(p, 0.095, facecolor='white', edgecolor=color, linewidth=2, zorder=3))
    ax.text(p[0], p[1]+(0.25 if above else -0.30), label, ha='center', va='center', color=color)


def prepare(ax):
    ax.set_aspect('equal')
    ax.set_xlim(-0.45, 2.45)
    ax.set_ylim(-0.60, 0.70)
    ax.axis('off')


fig = plt.figure(figsize=(10, 6), layout='constrained')
grid = fig.add_gridspec(2, 2, height_ratios=(1, 1.6))
left, right, bottom = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1]), fig.add_subplot(grid[1, :])
for ax, title, double in [(left, r'$B_3$', True), (right, r'$A_3$', False)]:
    prepare(ax)
    ax.set_title(title, fontsize=18)
    bond(ax, (0, 0), (1, 0))
    bond(ax, (1, 0), (2, 0), double=double)
    for j in range(3):
        node(ax, (j, 0), rf'$\alpha_{j+1}$')
    if double:
        ax.text(2, 0.38, 'short', ha='center', fontsize=11)

bottom.set_aspect('equal')
bottom.set_xlim(-0.8, 2.8)
bottom.set_ylim(-0.85, 1.7)
bottom.axis('off')
bottom.set_title(r'Extended $B_3$: delete short node 3', fontsize=16)
points = {0:(1, 1), 1:(0, 0), 2:(1, 0), 3:(2, 0)}
bond(bottom, points[0], points[2], color=BLUE)
bond(bottom, points[1], points[2], color=BLUE)
bond(bottom, points[2], points[3], double=True)
for j, p in points.items():
    node(bottom, p, rf'$\alpha_{j}$', color=BLUE if j != 3 else RED, above=(j == 0))
bottom.plot([1.85, 2.15], [-0.15, 0.15], color=RED, linewidth=2, zorder=4)
bottom.text(1, -0.68, r'Remaining single-bond chain: $0\;—\;2\;—\;1\;\cong A_3$', ha='center', color=BLUE, fontsize=13)
fig.suptitle('Dynkin diagrams and the long-root subalgebra', fontsize=16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
