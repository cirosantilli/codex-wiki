"""Draw a directed DFS return. Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.

Writes the PNG basename in the current working directory, with opaque white background.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import numpy as np

fig = plt.figure(figsize=(9, 4), dpi=120, facecolor='white')
ax = fig.add_axes([0.025, 0.10, 0.48, 0.76])
ax.set(xlim=(-0.35, 2.35), ylim=(-0.35, 1.85), aspect='equal')
ax.axis('off')
positions = {0: np.array((0., 0.)), 1: np.array((1., 1.5)), 2: np.array((2., 0.))}
for u, v in [(0,1), (1,2), (2,0)]:
    start, end = positions[u], positions[v]
    direction = (end-start)/np.linalg.norm(end-start)
    ax.add_patch(FancyArrowPatch(start+0.18*direction, end-0.18*direction,
        arrowstyle='-|>', mutation_scale=20, linewidth=2.3, color='#526270'))
# Highlight the routed return 2 -> 0 -> 1 alongside the physical edges.
for u,v in [(2,0),(0,1)]:
    start,end=positions[u],positions[v]
    direction=(end-start)/np.linalg.norm(end-start)
    offset=np.array((-direction[1],direction[0]))*0.095
    ax.add_patch(FancyArrowPatch(start+0.23*direction+offset,end-0.23*direction+offset,
        arrowstyle='-|>', mutation_scale=18, linewidth=2.6, color='#b83c20'))
for n, p in positions.items():
    ax.add_patch(Circle(p,0.18,facecolor='white',edgecolor='#263c4a',linewidth=2,zorder=5))
    ax.text(*p,str(n),ha='center',va='center',fontsize=15,fontweight='bold',zorder=6)
fig.suptitle('Returning a DFS token on a directed cycle',x=0.5,y=0.97,fontsize=15)
ax.text(1,-0.29,'Grey: directed graph     Red: routed return',ha='center',fontsize=10)
fig.text(0.55,0.76,'Discovery tree:  0 → 1 → 2',fontsize=13,color='#263c4a')
fig.text(0.55,0.59,'Logical return:  2 back to 1',fontsize=13)
fig.text(0.55,0.43,'Network route:  2 → 0 → 1',fontsize=13,color='#b83c20')
fig.text(0.55,0.25,'Stack (top first):\n[2, 1, 0]  →  [1, 0]',fontsize=12,linespacing=1.6)
fig.text(0.55,0.08,'Node 0 only forwards: no new DFS visit.',fontsize=10,color='#526270')
fig.savefig(Path.cwd() / 'concurrent-programming-2015-directed-return.png',facecolor='white',transparent=False)
plt.close(fig)
