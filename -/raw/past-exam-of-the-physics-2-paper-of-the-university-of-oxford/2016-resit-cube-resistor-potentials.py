"""Original illustration for the 2016 Oxford Physics 2 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

from itertools import product
verts=list(product([0,1],repeat=3));xy={v:np.array([v[0]+.42*v[2],v[1]+.36*v[2]])for v in verts}
pot={(0,0,0):1,(1,0,0):0,(0,1,0):9/14,(0,0,1):9/14,(1,1,0):5/14,(1,0,1):5/14,(0,1,1):4/7,(1,1,1):3/7}
labels={(0,0,0):'$A:1$',(1,0,0):'$B:0$',(0,1,0):'$9/14$',(0,0,1):'$9/14$',(1,1,0):'$5/14$',(1,0,1):'$5/14$',(0,1,1):'$4/7$',(1,1,1):'$3/7$'}
offsets={(0,0,0):(-.12,-.14),(1,0,0):(-.02,-.14),(0,1,0):(-.14,.04),(0,0,1):(-.18,-.12),(1,1,0):(.02,-.12),(1,0,1):(.02,-.11),(0,1,1):(-.16,.06),(1,1,1):(.03,.04)}
fig,ax=plt.subplots(figsize=(6.5,5.5),layout='constrained')
for i,u in enumerate(verts):
 for v in verts[i+1:]:
  if sum(a!=b for a,b in zip(u,v))!=1:continue
  p,q=xy[u],xy[v];d=q-p;perp=np.array([-d[1],d[0]])/np.linalg.norm(d);t=np.linspace(0,1,65);zig=np.zeros_like(t);mask=(t>.3)&(t<.7);zig[mask]=.025*np.sin(10*np.pi*(t[mask]-.3)/.4);line=p[None,:]+t[:,None]*d+zig[:,None]*perp
  ax.plot(line[:,0],line[:,1],color='.45',lw=1.4,zorder=1)
for v in verts:
 p=xy[v];ax.scatter([p[0]],[p[1]],s=75,c=[plt.cm.viridis(pot[v])],edgecolors='black',lw=.6,zorder=3);off=np.array(offsets[v]);ax.text(*(p+off),labels[v],fontsize=12,zorder=4,bbox={'facecolor':'white','edgecolor':'none','alpha':.88,'pad':1})
ax.set_aspect('equal');ax.set(xlim=(-.3,1.8),ylim=(-.3,1.66),title='Adjacent cube terminals: unit voltage, every edge $R$');ax.axis('off');ax.text(.7,-.27,r'$I_A=12/(7R)$, so $R_{AB}=7R/12$',ha='center',fontsize=12)
fig.savefig(Path.cwd()/'2016-resit-cube-resistor-potentials.png',dpi=140,transparent=False);plt.close(fig)
