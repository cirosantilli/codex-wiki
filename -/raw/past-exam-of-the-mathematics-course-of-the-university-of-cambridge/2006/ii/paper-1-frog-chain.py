"""Original continuous-time transition graph; Python 3.14, root Matplotlib."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
pos={1:(0,0),2:(1,1),3:(2,0)}
fig,ax=plt.subplots(figsize=(5.5,3.7),facecolor='white')
for a,b,rad,labelpos in [(1,2,.12,(.27,.65)),(2,1,.12,(.7,.25)),(2,3,0,(1.6,.65)),(3,1,0,(1,-.14))]:
 ax.add_patch(FancyArrowPatch(pos[a],pos[b],connectionstyle=f'arc3,rad={rad}',shrinkA=20,shrinkB=20,arrowstyle='-|>',mutation_scale=15,lw=1.7,color='#28608d'));ax.text(*labelpos,'1',fontsize=12,ha='center',va='center')
for node,p in pos.items():
 ax.add_patch(Circle(p,.15,facecolor='white',edgecolor='black',lw=1.5,zorder=3));ax.text(*p,str(node),ha='center',va='center',fontsize=13,zorder=4)
ax.set(xlim=(-.4,2.4),ylim=(-.35,1.35),title='Frog transition rates');ax.set_aspect('equal');ax.axis('off');fig.tight_layout();fig.savefig('paper-1-frog-chain.png',dpi=150,facecolor='white')
