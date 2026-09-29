"""Original ideal octahedral donor positions and chelate connections; output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(10,5.3),facecolor='white')
xyz=[np.array(p) for p in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
pr=np.array([[1,-.55,0],[.18,.43,1]])
ps=[pr@p for p in xyz]
data=[({0,2,4},[(0,3),(2,5),(4,1)],'fac: pyridyl donors on one face'),({0,1,4},[(0,2),(1,5),(4,3)],'mer: one trans pyridyl pair')]
for a,(pyr,pairs,title) in zip(axs,data):
 a.axis('off');a.set(xlim=(-1.7,1.7),ylim=(-1.65,1.65),aspect='equal');a.set_title(title,fontsize=12,weight='bold')
 for i,p in enumerate(ps):
  a.plot([0,p[0]],[0,p[1]],color='#777',lw=1.2,zorder=1)
 for k,(i,j) in enumerate(pairs,1):
  p,q=ps[i],ps[j];m=(p+q)/2;v=m/(np.linalg.norm(m) or 1)*.28
  a.plot([p[0],m[0]+v[0],q[0]],[p[1],m[1]+v[1],q[1]],color='#b7682c',lw=2.2,zorder=2)
  a.text(m[0]+v[0]+(-.16 if title.startswith('mer') and k==1 else .16 if title.startswith('mer') and k==3 else 0),m[1]+v[1]+(-.10 if title.startswith('mer') and k==1 else .10 if title.startswith('mer') and k==3 else 0),str(k),ha='center',va='center',fontsize=10,color='#a34f19',bbox=dict(fc='white',ec='none',pad=.5))
 for i,p in enumerate(ps):
  a.scatter(*p,s=700,c='#d9e8f3' if i in pyr else '#f4e2d1',edgecolors='white',zorder=3);a.text(*p,'P' if i in pyr else 'A',ha='center',va='center',fontsize=13,zorder=4)
 a.text(0,0,'Fe',ha='center',va='center',fontsize=13,bbox=dict(fc='white',ec='none',pad=2),zorder=4)
 a.text(0,-1.45,'Mirror reflection gives a second enantiomer',ha='center',fontsize=10)
fig.text(.5,.035,'P = pyridyl nitrogen; A = amino nitrogen. Each numbered orange path is one bidentate ligand. Idealized positions only.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.08,1,1));fig.savefig('paper-2-isomers.png',dpi=170,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
