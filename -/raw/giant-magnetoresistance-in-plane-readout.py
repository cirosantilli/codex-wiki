"""Original functional CIP diagram; not a reconstruction of a historical sample."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, axs = plt.subplots(1, 2, figsize=(12, 4.4), dpi=140, facecolor='white')
for ax, parallel in zip(axs, [False, True]):
    ax.set(xlim=(-1, 11), ylim=(-1.8, 5.9)); ax.axis('off')
    for y, height, color, label in [(0, 1, '#c7dced', 'Fe'), (1, .5, '#ddd', 'Cr'), (1.5, 1, '#c7dced', 'Fe')]:
        ax.add_patch(Rectangle((1, y), 8, height, facecolor=color, edgecolor='#444', lw=1.2))
        ax.text(9.35, y+height/2, label, va='center', fontsize=12)
    for y, direction in [(.5, 1), (2, 1 if parallel else -1)]:
        start, end = (3.3, 6.7) if direction == 1 else (6.7, 3.3)
        ax.annotate('', (end,y), (start,y), arrowprops=dict(arrowstyle='-|>', color='#234d72', lw=3, mutation_scale=20))
    ax.plot([-0.3, 1], [.4, .4], color='#9b3b19', lw=2)
    ax.plot([9, 10.3], [.4, .4], color='#9b3b19', lw=2)
    ax.annotate('', (8, -.65), (2, -.65), arrowprops=dict(arrowstyle='->', color='#9b3b19', lw=2))
    ax.text(5, -1.05, 'Current along the layers (CIP)', ha='center', color='#9b3b19', fontsize=11)
    for x in [3,7]:
        ax.plot([x,x], [2.5,3.4], color='#555', lw=1.4)
    ax.plot([3,7], [3.4,3.4], color='#555', lw=1.4)
    ax.text(5,3.4,' V ', ha='center', va='center', bbox=dict(facecolor='white',edgecolor='#555', boxstyle='circle'), fontsize=12)
    ax.text(5,4.2, 'Separate voltage contacts', ha='center', fontsize=11)
    ax.text(5,5.1,'Parallel' if parallel else 'Antiparallel',ha='center',fontsize=15,weight='bold')
fig.suptitle('Giant magnetoresistance: compare transport and magnetic alignment', fontsize=16, y=.98)
fig.text(.5,.025,'Functional diagram only: layer thicknesses and contact positions are illustrative. Arrows show magnetization.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.12,top=.88,wspace=.12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white')
