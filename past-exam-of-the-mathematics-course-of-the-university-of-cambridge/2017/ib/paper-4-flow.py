"""Original network solution; output same-basename opaque PNG in CWD.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
P={'s':(0,0),'a':(1.3,1),'b':(1.3,-1),'c':(2.8,0),'d':(4.3,1),'e':(4.3,-1),'t':(5.6,0)}
E=[('s','a',6,8),('s','b',8,9),('s','c',5,5),('a','d',6,6),('c','a',0,4),('b','c',3,7),('b','e',5,5),('c','d',2,2),('c','e',6,6),('e','d',0,4),('d','t',8,11),('e','t',11,13)]
S={'s','a','b','c'}
# Tiny canvas allowance prevents float truncation of 460 px to 459 px.
fig,ax=plt.subplots(figsize=(8.8,4.6001),dpi=100,facecolor='white')
for u,v,f,cap in E:
 a=np.array(P[u],float);b=np.array(P[v],float);delta=b-a;unit=delta/np.linalg.norm(delta);a+=.17*unit;b-=.17*unit
 col='#bc601d' if u in S and v not in S else '#424b54'
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,color=col,lw=2 if col=='#bc601d' else 1.4))
 m=(a+b)/2;perp=np.array([-unit[1],unit[0]])
 if (u,v)==('e','d'):perp=-perp
 m+=.12*perp
 ax.text(*m,f'{f}/{cap}',ha='center',va='center',fontsize=10,color=col,bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
for name,p in P.items():
 ax.add_patch(Circle(p,.17,facecolor='#d6e9f5' if name in S else '#f3f3f3',edgecolor='#293c49',lw=1.6))
 ax.text(*p,name,ha='center',va='center',fontsize=14,fontstyle='italic')
ax.plot([3.48,3.48],[-1.5,1.5],ls='--',lw=1.3,color='#bc601d')
ax.text(3.48,1.62,'minimum cut: 19',ha='center',fontsize=10,color='#a24d15')
ax.text(1.8,-1.65,'source side S = {s, a, b, c}',ha='center',fontsize=11,color='#1763a4')
ax.text(4.9,-1.65,'sink side',ha='center',fontsize=11)
ax.set_title('Maximum flow = 19    •    edge labels = flow / capacity',fontsize=13,pad=12)
ax.set(xlim=(-.5,6.1),ylim=(-2,1.9));ax.set_aspect('equal');ax.axis('off');fig.tight_layout(pad=1)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
