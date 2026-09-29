"""Draw an original SCC example and its condensation; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams.update({'font.size': 14, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), dpi=100, facecolor='white', gridspec_kw={'width_ratios': [1.5, 1]})
pos = {'a': (0, 1), 'b': (1.1, 1.9), 'c': (1.1, .1), 'd': (3, 1.65), 'e': (3, .35), 'f': (5, 1.65), 'g': (5, .35)}
colors = {'a': '#dbeafe', 'b': '#dbeafe', 'c': '#dbeafe', 'd': '#dcfce7', 'e': '#dcfce7', 'f': '#ffedd5', 'g': '#ffedd5'}
ax = axes[0]
def arrow(u, v, curve=0):
    ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle='-|>', mutation_scale=17,
        shrinkA=17, shrinkB=17, connectionstyle=f'arc3,rad={curve}', color='#334155', linewidth=1.7))
for u, v in [('a','b'), ('b','c'), ('c','a'), ('c','d'), ('e','f')]:
    arrow(u,v)
for u, v in [('d','e'), ('e','d'), ('f','g'), ('g','f')]:
    arrow(u,v,.22)
for v, (x,y) in pos.items():
    ax.add_patch(Circle((x,y), .22, facecolor=colors[v], edgecolor='#334155', zorder=3))
    ax.text(x,y,v,ha='center',va='center',zorder=4)
ax.set(xlim=(-.5,5.5),ylim=(-.7,2.5),aspect='equal',title='Seven-vertex directed graph')
ax.axis('off')
ax=axes[1]
for i, (label,color) in enumerate([('{a,b,c}', '#dbeafe'), ('{d,e}', '#dcfce7'), ('{f,g}', '#ffedd5')]):
    ax.text(1.6*i, 1, label, ha='center', va='center', bbox={'boxstyle':'round,pad=.5','facecolor':color,'edgecolor':'#334155'})
    if i<2:
        ax.annotate('',(1.6*i+1.12,1),(1.6*i+.55,1),arrowprops={'arrowstyle':'->','lw':2})
ax.set(xlim=(-.7,4),ylim=(-.7,2.5),aspect='equal',title='Condensation: an acyclic chain')
ax.axis('off')
fig.text(.5,.1,'Mutual reachability stays within each colored component.',ha='center',fontsize=13)
fig.subplots_adjust(left=.025,right=.98,bottom=.18,top=.9,wspace=.08)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
