"""Original five-state transition diagram; Python 3.14, Matplotlib 3.10.7.

Run from the desired output directory; writes only the matching PNG basename.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.4, 4.6), facecolor='white')
ax.set_facecolor('white')
pos = {1: (0, 0), 2: (2, 1.4), 3: (2, -1.4), 4: (4, 0), 5: (6, 0)}
labels = {1: '1\nDisease-free', 2: '2\nLocal only', 3: '3\nDistant only', 4: '4\nBoth', 5: '5\nDeath'}
nodes = {}
for k,(x,y) in pos.items():
 nodes[k] = FancyBboxPatch((x-.58,y-.33),1.16,.66,boxstyle='round,pad=0.03,rounding_size=0.11',
                          facecolor='#f2f7fa' if k<5 else '#e4eaf0',edgecolor='#245272',linewidth=1.5,zorder=2)
 ax.add_patch(nodes[k])
edges = [(1,2,'0.025',0,(.84,.78)), (1,3,'0.056',0,(.84,-.78)),
         (2,4,'0.164',0,(3,.79)), (3,4,'0.064',0,(3,-.79)),
         (4,5,'0.513',0,(5,.16)), (1,5,'0.004',-.82,(3,2.55)),
         (2,5,'0.017',-.35,(4.30,1.25)), (3,5,'0.305',.35,(4.30,-1.25))]
for a,b,label,rad,loc in edges:
 ax.add_patch(FancyArrowPatch(pos[a],pos[b], arrowstyle='-|>', mutation_scale=15,
                             linewidth=1.7, color='#245272', patchA=nodes[a], patchB=nodes[b], shrinkA=3, shrinkB=4,
                             connectionstyle=f'arc3,rad={rad}', zorder=1))
 ax.text(*loc,label,ha='center',va='center',fontsize=11,color='#13364e',
         bbox={'facecolor':'white','edgecolor':'none','pad':1.7},zorder=3)
for k,(x,y) in pos.items():
 ax.text(x,y,labels[k],ha='center',va='center',fontsize=10.5,zorder=4)
ax.set_aspect('equal');ax.set_xlim(-.73,6.73);ax.set_ylim(-2.08,2.95);ax.axis('off')
ax.set_title('Allowed transitions and rates per year',fontsize=14,pad=10)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
plt.close(fig)
