"""Python 3.14; Matplotlib 3.10.7. Writes only the PNG basename in cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
fig,axs=plt.subplots(1,2,figsize=(10,4.7),dpi=100,facecolor='white')
original={('A','1'):(40,60),('A','4'):(50,50),('1','3'):(10,10),('1','2'):(30,30),('4','2'):(20,40),('4','5'):(30,30),('2','3'):(30,40),('2','5'):(20,30),('3','B'):(40,40),('5','B'):(50,50)}
storm={('A','1'):(30,60),('A','4'):(30,50),('1','3'):(10,10),('1','2-'):(20,30),('4','2-'):(0,40),('4','5'):(30,30),('2+','3'):(20,40),('2+','5'):(0,30),('3','B'):(30,40),('5','B'):(30,50),('2-','2+'):(20,20)}
for ax,edges,title in zip(axs,[original,storm],['Before storm: maximum flow 90','After storm: maximum flow 60']):
 pos={'A':(0,0),'1':(1,1),'4':(1,-1),'2':(2,0),'3':(3,1),'5':(3,-1),'B':(4,0),'2-':(1.8,0),'2+':(2.4,0)}
 for (u,v),(flow,cap) in edges.items():
  x,y=pos[u];xx,yy=pos[v];col='#b33b33' if (u,v)==('2-','2+') else '#444444'
  arrow=FancyArrowPatch((x,y),(xx,yy),arrowstyle='-|>',mutation_scale=12,shrinkA=12,shrinkB=12,color=col,lw=1.4)
  ax.add_patch(arrow)
  dx,dy=xx-x,yy-y;off=.105;length=(dx*dx+dy*dy)**.5
  tx=(x+xx)/2-off*dy/length;ty=(y+yy)/2+off*dx/length
  if (u,v)==('2-','2+'):ty-=.25
  ax.text(tx,ty,f'{flow}/{cap}',fontsize=8,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
 nodes=set(sum(([u,v] for u,v in edges),[]))
 for node in nodes:
  x,y=pos[node];ax.plot(x,y,'o',ms=17,color='#e4edf4',mec='#315676',zorder=4)
  label=node if node in ['A','B'] else '$R_{'+node[0]+'}'+({'2-':'^-','2+':'^+'}.get(node,''))+'$'
  ax.text(x,y,label,ha='center',va='center',fontsize=10,zorder=5)
 ax.set_aspect('equal');ax.set_xlim(-.35,4.35);ax.set_ylim(-1.5,1.5);ax.axis('off');ax.set_title(title,fontsize=12)
fig.suptitle('Road flows / capacities (vehicles per minute)',fontsize=13,y=.95)
fig.text(.5,.06,'The internal red edge limits the flooded roundabout to 20. All other capacities are unchanged.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.1,1,.9),pad=1.5)
fig.savefig('paper-4-network-flows.png',facecolor='white',transparent=False)
plt.close(fig)
