"""Original solution state diagram; write the PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 5), dpi=100, facecolor='white')
pos = [(i*2, 0) for i in range(5)]
r = 0.38
for i, (x, y) in enumerate(pos):
    ax.add_patch(Circle((x, y), r, facecolor='#dceede' if i == 4 else '#edf3fa', edgecolor='#25384b', lw=1.5, zorder=4))
    if i == 4:
        ax.add_patch(Circle((x, y), r-0.065, fill=False, edgecolor='#25384b', zorder=5))
    ax.text(x, y, f'$S_{i}$', ha='center', va='center', fontsize=14, zorder=6)
    ax.text(x, -0.63, f'output {int(i == 4)}', ha='center', fontsize=10)
for i, bit in enumerate([1, 1, 0, 1]):
    x, _ = pos[i]
    ax.add_patch(FancyArrowPatch((x+r, 0), (x+2-r, 0), arrowstyle='-|>', mutation_scale=14, lw=1.6, color='#1264a3'))
    ax.text(x+1, 0.13, str(bit), ha='center', fontsize=12)
# Returns above the state row are nested orthogonal arcs with explicit labels.
for source, height, endoffset in [(1, 0.85, -0.1), (3, 1.40, 0), (4, 2.00, 0.1)]:
    x = pos[source][0]
    ax.plot([x, x, endoffset, endoffset], [r, height, height, r+0.15], color='#555555', lw=1.4)
    ax.annotate('', xy=(endoffset, r-0.01), xytext=(endoffset, r+0.2), arrowprops=dict(arrowstyle='-|>', color='#555555', lw=1.4))
    ax.text((x+endoffset)/2, height+0.1, '0', ha='center', fontsize=12)
# The post-recognition overlap returns from S4 to S2 below the state row.
ax.plot([8, 8, 4, 4], [-r, -1.35, -1.35, -r-0.15], color='#1264a3', lw=1.5)
ax.annotate('', xy=(4, -r+0.01), xytext=(4, -r-0.2), arrowprops=dict(arrowstyle='-|>', color='#1264a3', lw=1.5))
ax.text(6, -1.25, '1 (overlap)', ha='center', fontsize=11, color='#1264a3')
for i, bit in [(0, 0), (2, 1)]:
    x = pos[i][0]
    if i == 2:
        start, end, curve = (x-r*0.7, r*0.7), (x+r*0.7, r*0.7), -1.8
        label = (x, 1.0)
    else:
        start, end, curve = (x-r*0.75, -r*0.7), (x-r*0.75, r*0.7), -2.0
        label = (x-0.95, 0)
    loop = FancyArrowPatch(start, end, connectionstyle=f'arc3,rad={curve}',
                          arrowstyle='-|>', mutation_scale=13, lw=1.3,
                          color='#555555', zorder=2)
    ax.add_patch(loop)
    ax.text(*label, str(bit), ha='center', va='center', fontsize=12)
ax.annotate('start', xy=(-r, 0), xytext=(-1.2, -0.65), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#333333'))
ax.set(xlim=(-1.5, 8.7), ylim=(-1.75, 2.7))
ax.set_title('Overlapping recognition of 1101', fontsize=15, pad=12)
ax.axis('off')
fig.subplots_adjust(left=0.02, right=0.98, top=0.90, bottom=0.03)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', dpi=100)
plt.close(fig)
