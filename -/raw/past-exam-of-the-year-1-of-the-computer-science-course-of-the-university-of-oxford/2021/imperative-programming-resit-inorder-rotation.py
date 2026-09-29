from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
before={4:(2,1),2:(1,.55),6:(3,.55),1:(.5,.1),3:(1.5,.1),5:(2.5,.1),7:(3.5,.1)}
after={2:(1.3,1),1:(.5,.55),4:(2.2,.55),3:(1.6,.1),6:(3,.1),5:(2.5,-.35),7:(3.5,-.35)}
e0=[(4,2),(4,6),(2,1),(2,3),(6,5),(6,7)]
e1=[(2,1),(2,4),(4,3),(4,6),(6,5),(6,7)]
assert len(e0)==len(e1)==6
fig,axes=plt.subplots(1,2,figsize=(7.6,3.8),dpi=100,facecolor='white')
for ax,pos,edges,spine,title in [(axes[0],before,e0,{(4,6),(6,7)},'Before: 7 nodes, L = 4'),(axes[1],after,e1,{(2,4),(4,6),(6,7)},'After: 7 nodes, L = 3')]:
 ax.set_facecolor('white');ax.set_xlim(0,4);ax.set_ylim(-.65,1.35);ax.axis('off');ax.set_title(title,fontsize=12)
 for a,b in edges:
  x0,y0=pos[a];x1,y1=pos[b];ax.plot([x0,x1],[y0,y1],color='#d6604d' if (a,b) in spine else '#999999',lw=2.5 if (a,b) in spine else 1.3,zorder=1)
 for v,(x,y) in pos.items():
  ax.add_patch(Circle((x,y),.105,facecolor='white',edgecolor='#2166ac',lw=1.5,zorder=2));ax.text(x,y,str(v),ha='center',va='center',fontsize=11,zorder=3)
fig.suptitle('A right rotation extends the right spine by one node',fontsize=13,y=.99)
fig.text(.5,.035,'Inorder sequence in both panels: 1, 2, 3, 4, 5, 6, 7',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.08,1,.94));fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
