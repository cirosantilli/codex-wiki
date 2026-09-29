"""Python 3.14 / matplotlib 3.10: write this opaque solution figure to cwd only."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Circle
positions={1:(0,0),2:(1,1),3:(1,-1),4:(2,0),5:(3,1),6:(3,-1),7:(4,0),8:(5,1)}
edges={(1,2):3,(1,3):2,(2,4):1,(2,5):4,(3,4):1,(3,6):3,(4,5):3,(4,6):2,(4,7):3,(5,7):1,(5,8):1,(6,7):2,(7,8):2}
flow={(1,3):4,(3,4):4,(4,5):2,(4,6):2,(5,8):1};potential={1:0,2:-3,3:-2,4:-3,5:-6,6:-5,7:-5,8:-7}
fig,ax=plt.subplots(figsize=(10,4.8),dpi=100,facecolor='white');ax.set_facecolor('white')
for (i,j),cost in edges.items():
 positive=(i,j) in flow;start=positions[i];end=positions[j]
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15 if positive else 10,linewidth=2.5 if positive else 1,color='#176eaa' if positive else '#d0d5db',shrinkA=15,shrinkB=15,zorder=2 if positive else 1))
 if positive:
  x=(start[0]+end[0])/2;y=(start[1]+end[1])/2;dx,dy={(1,3):(-.05,-.15),(3,4):(-.07,.17),(4,5):(-.08,.17),(4,6):(.09,-.18),(5,8):(0,.15)}[(i,j)]
  ax.text(x+dx,y+dy,f'{flow[(i,j)]} × {cost}',ha='center',va='center',fontsize=12,color='#075486',bbox=dict(facecolor='white',edgecolor='none',pad=1),zorder=4)
for i,(x,y) in positions.items():
 ax.add_patch(Circle((x,y),.15,facecolor='white',edgecolor='#243746',linewidth=1.4,zorder=5));ax.text(x,y,str(i),ha='center',va='center',fontsize=13,zorder=6);ax.text(x,y-.3,fr'$\pi_{i}={potential[i]}$',ha='center',va='top',fontsize=11,color='#46535d',zorder=6)
for i,label in [(1,'supply 4'),(5,'demand 1'),(6,'demand 2'),(8,'demand 1')]:
 x,y=positions[i];ax.text(x,y-.62 if i==6 else y+.35,label,ha='center',fontsize=11,color='#243746')
ax.set_xlim(-.55,5.55);ax.set_ylim(-1.7,1.75);ax.set_aspect('equal');ax.axis('off');fig.suptitle('Optimal flow: cost 23',fontsize=17,y=.97);fig.text(.5,.04,'Blue edges: positive flow × unit cost.  Grey edges: zero flow.  Vertex labels give dual potentials.',ha='center',fontsize=10);fig.subplots_adjust(left=.025,right=.975,bottom=.12,top=.86);fig.savefig(Path.cwd()/'paper-38-optimal-flow.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
