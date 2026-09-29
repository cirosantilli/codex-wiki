"""Original solution diagram. Python 3.14, Matplotlib 3.10.7.

Writes paper-38-optimal-flow.png in the caller's cwd, respecting MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
fig,ax=plt.subplots(figsize=(8,4),dpi=100,facecolor='white')
ax.set_facecolor('white');ax.set_xlim(-.5,5.7);ax.set_ylim(-.5,3.1);ax.axis('off')
pos={'S':(0,1.2),'A':(2,2.3),'B':(2,.1),'C':(5,2.3),'T':(5,.1)}
flows={('S','A'):5,('S','B'):20,('A','B'):0,('A','C'):5,('B','C'):0,('B','T'):20,('C','T'):5}
offsets={('S','A'):(-.1,.16),('S','B'):(-.1,-.16),('A','B'):(-.28,0),('A','C'):(0,.22),('B','C'):(.16,-.12),('B','T'):(0,-.2),('C','T'):(.27,0)}
for (u,v),x in flows.items():
 color='#154b61' if x else '#7d8d95'
 ax.add_patch(FancyArrowPatch(pos[u],pos[v],arrowstyle='-|>',mutation_scale=15,shrinkA=15,shrinkB=15,color=color,linewidth=2,linestyle='-' if x else '--'))
 dx,dy=offsets[u,v];label=((pos[u][0]+pos[v][0])/2+dx,(pos[u][1]+pos[v][1])/2+dy)
 ax.text(*label,str(x),ha='center',va='center',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','pad':1})
for k,(x,y) in pos.items():
 ax.add_patch(Circle((x,y),.17,facecolor='#e9f2f5',edgecolor='#154b61',linewidth=1.7,zorder=4));ax.text(x,y,k,ha='center',va='center',fontsize=11,zorder=5)
ax.text(0,1.62,'supply 25',ha='center',fontsize=10)
ax.text(5,-.35,'demand 25',ha='center',fontsize=10)
ax.text(2.6,2.87,'Optimal flow: cost 220',ha='center',fontsize=14)
fig.subplots_adjust(left=.045,right=.98,top=.98,bottom=.06)
fig.savefig('paper-38-optimal-flow.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
