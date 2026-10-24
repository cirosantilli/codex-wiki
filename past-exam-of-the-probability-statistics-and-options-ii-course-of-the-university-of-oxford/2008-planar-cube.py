"""Original planar cube drawing; Python 3.14, matplotlib. Output is in CWD."""
from pathlib import Path
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

corners={'00':(-1,-1),'01':(1,-1),'11':(1,1),'10':(-1,1)}
pos={str(a)+bc:tuple((2 if a==0 else .85)*u for u in xy)for a in [0,1]for bc,xy in corners.items()}
fig,ax=plt.subplots(figsize=(5,5),facecolor='white');ax.set_facecolor('white')
for v,w in itertools.combinations(pos,2):
 if sum(a!=b for a,b in zip(v,w))==1:
  ax.plot([pos[v][0],pos[w][0]],[pos[v][1],pos[w][1]],color='#285b79',lw=2,zorder=1)
for v,(x,y)in pos.items():
 ax.scatter([x],[y],s=100,color='white',edgecolor='#285b79',zorder=2)
 dx,dy=((.25 if x>0 else -.25),(.22 if y>0 else -.22))if v[0]=='0'else((-.26 if x>0 else .26),(-.22 if y>0 else .22))
 ax.text(x+dx,y+dy,v,ha='center',va='center',fontsize=11,zorder=3)
ax.set(xlim=(-2.7,2.7),ylim=(-2.7,2.7));ax.set_aspect('equal');ax.axis('off');ax.set_title('A planar embedding of the cube graph')
fig.tight_layout();fig.savefig(Path('2008-planar-cube.png'),dpi=160,facecolor='white');plt.close(fig)
