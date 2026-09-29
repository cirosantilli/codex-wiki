"""Draw a typical diploid nuclear cycle; Python 3.14, matplotlib 3.10.7.

Run from _media. This schematic has no measured timings or phase proportions.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path as PlotPath

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(10, 6.8), dpi=100, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 6.8))
ax.axis('off')
ax.text(5, 6.47, 'One nuclear replication, then two diploid daughters',
        ha='center', fontsize=17, weight='bold', color='#17324d')

def box(x, y, w, h, color, heading, body):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.12',
                               facecolor=color, edgecolor='#385064', linewidth=1.4))
    ax.text(x+w/2, y+h-0.32, heading, ha='center', va='center',
            weight='bold', fontsize=14)
    ax.text(x+w/2, y+0.48, body, ha='center', va='center', fontsize=12,
            linespacing=1.4)

def arrow(a, b, **kwargs):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=18,
                               linewidth=1.8, color='#385064', **kwargs))

box(0.45, 4.1, 3.45, 1.65, '#e7effc', r'$G_1$ — growth before copying',
    '2n chromosomes; 2C DNA\nOne unreplicated copy each')
box(6.0, 4.1, 3.45, 1.65, '#e2f3ed', r'S — DNA replication',
    '2n chromosomes throughout\n2C → 4C DNA')
box(6.0, 1.3, 3.45, 1.65, '#fff2db', r'$G_2$ — preparation for division',
    '2n chromosomes; 4C DNA\nPaired sister chromatids')
box(0.45, 1.3, 3.45, 1.65, '#f6e9f1', 'M — mitosis + cytokinesis',
    'Each completed daughter:\n2n chromosomes; 2C DNA')
arrow((4.08, 4.92), (5.82, 4.92))
arrow((7.72, 3.95), (7.72, 3.1))
arrow((5.82, 2.12), (4.08, 2.12))
arrow((1.0, 3.1), (1.0, 3.95))
ax.text(5, 6.02, 'Interphase = G₁ + S + G₂', ha='center', fontsize=12,
        color='#385064')
ax.text(0.95, 3.52, 'next\ncycle', ha='left', va='center', fontsize=10,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5})
box(0.45, 0.2, 3.45, 0.71, '#f1f3f5', r'$G_0$ — outside the cycle', '')
# Separate paths through the central gap avoid crossing any phase box.
for points in [[(4.04, 4.45), (4.7, 4.45), (4.7, 0.56), (4.04, 0.56)],
               [(4.04, 0.82), (4.42, 0.82), (4.42, 4.7), (4.04, 4.7)]]:
    path = PlotPath(points, [PlotPath.MOVETO, PlotPath.LINETO,
                            PlotPath.LINETO, PlotPath.LINETO])
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle='-|>',
                               mutation_scale=16, linewidth=1.4,
                               color='#385064', linestyle='--'))
ax.text(4.8, 3.48, 'exit', fontsize=10, ha='left')
ax.text(4.05, 3.35, 're-entry\nwhen possible', fontsize=10, ha='center',
        rotation=90, va='center',
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5})
ax.text(9.45, 0.22, 'Schematic; arrows do not encode time',
        fontsize=10, ha='right', color='#536575')
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
