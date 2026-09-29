"""Draw the two computed maximum independent sets; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

points = {'A':(0,1.2), 'D':(-.65,0), 'E':(.65,0),
          'B':(1.4,1.2), 'C':(2.8,1.2), 'F':(3.7,.2)}
edges = [('A','B'), ('B','C'), ('C','F'), ('A','D'), ('D','E'), ('E','A')]
fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.2), dpi=100, facecolor='white')
for ax, chosen in zip(axes, [{'B','D','F'}, {'B','E','F'}]):
    for a,b in edges:
        x,y = points[a], points[b]
        ax.plot([x[0],y[0]], [x[1],y[1]], color='#59636e', linewidth=1.5, zorder=1)
    for name,(x,y) in points.items():
        selected = name in chosen
        ax.add_patch(Circle((x,y), .17, facecolor='#238b45' if selected else 'white',
                            edgecolor='#334155', linewidth=1.3, zorder=2))
        ax.text(x,y,name,ha='center',va='center',color='white' if selected else '#17212b',
                fontsize=12,zorder=3)
    ax.set_title('{'+', '.join(sorted(chosen))+'}',fontsize=13,pad=12)
    ax.set(xlim=(-1,4.05),ylim=(-.45,1.7),aspect='equal')
    ax.axis('off')
fig.suptitle(r'Two optimal choices: $\alpha(G)=3$',fontsize=14,y=.97)
fig.text(.5,.075,'Green vertices are selected; no edge joins two selected vertices.',
         ha='center',fontsize=10)
fig.subplots_adjust(left=.035,right=.98,top=.78,bottom=.2,wspace=.2)
fig.savefig(Path.cwd()/'functional-main-2015-independent-sets.png',
            facecolor='white',transparent=False)
