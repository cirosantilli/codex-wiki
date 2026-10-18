"""Original bipartite degree-two packing example. Python 3.14, Matplotlib 3.10.
Writes algorithms-path-cycle-flow.png to the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), dpi=110, facecolor='white')
blue = '#17658a'
orange = '#b35c18'
left = {'a': (0, 2), 'b': (0, 1), 'c': (0, 0)}
right = {'x': (2, 2), 'y': (2, 1), 'z': (2, 0)}
selected = [('a', 'x'), ('a', 'y'), ('b', 'x'), ('b', 'y'), ('c', 'z')]
all_edges = selected + [('b', 'z')]

def node(ax, xy, label, color=blue):
    ax.add_patch(Circle(xy, 0.13, facecolor='white', edgecolor=color, lw=1.8, zorder=4))
    ax.text(*xy, label, ha='center', va='center', fontsize=11, zorder=5)

def arrow(ax, u, v, label, active=True, offset=(0, 0)):
    color = blue if active else '#b8b8b8'
    ax.add_patch(FancyArrowPatch(u, v, arrowstyle='-|>', mutation_scale=10,
                                shrinkA=11, shrinkB=11, color=color,
                                lw=1.6 if active else 1, linestyle='-' if active else '--', zorder=1))
    mid = ((u[0]+v[0])/2+offset[0], (u[1]+v[1])/2+offset[1])
    ax.text(*mid, label, fontsize=9, color=color, ha='center', va='center',
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 0.6}, zorder=3)

ax = axes[0]
ax.set_title('Selected edges: a cycle and a path', fontsize=12, pad=15)
for a, b in all_edges:
    u, v = left[a], right[b]
    active = (a,b) in selected
    ax.plot([u[0],v[0]], [u[1],v[1]], color=blue if active else '#b8b8b8',
            lw=2.5 if active else 1.1, linestyle='-' if active else '--', zorder=1)
for label, pos in (left | right).items(): node(ax, pos, label)
ax.text(1, -0.55, '5 selected edges; every degree is at most 2', ha='center', fontsize=10)
ax.set_xlim(-0.5,2.5); ax.set_ylim(-0.8,2.45)

ax = axes[1]
ax.set_title('Integral flow: labels are flow / capacity', fontsize=12, pad=15)
pos = {'s':(-1.4,1),'t':(3.4,1)} | left | right
for v, f in [('a',2),('b',2),('c',1)]:arrow(ax,pos['s'],pos[v],f'{f}/2',offset=(-.04,0))
for v, f in [('x',2),('y',2),('z',1)]:arrow(ax,pos[v],pos['t'],f'{f}/2',offset=(.04,0))
for a,b in all_edges:
    arrow(ax,pos[a],pos[b],'1/1' if (a,b) in selected else '0/1', (a,b) in selected,
          offset=(-.35,.175) if (a,b)==('a','y') else (-.35,-.175) if (a,b)==('b','x') else (0,0))
for label, xy in pos.items():node(ax, xy, label, orange if label in ['s','t'] else blue)
ax.text(1,-.55,'Flow value 5 = selected-edge count',ha='center',fontsize=10)
ax.set_xlim(-1.8,3.8);ax.set_ylim(-.8,2.45)
for ax in axes:ax.set_aspect('equal');ax.axis('off')
fig.subplots_adjust(left=.025,right=.985,top=.84,bottom=.07,wspace=.17)
fig.savefig('algorithms-path-cycle-flow.png',facecolor='white',transparent=False)
