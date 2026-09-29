"""Original diagram; tested with Python 3.14, NumPy and Matplotlib.
Write the matching PNG basename to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
eps={1:(1,0),2:(-1,1),3:(0,-1)}
weights={}
for i in range(1,4):
 for j in range(1,4):
  for k in range(j,4):
   w=tuple(eps[j][a]+eps[k][a]-eps[i][a] for a in range(2))
   weights.setdefault(w,[]).append((i,j,k))
def point(w):return np.array([w[0]+w[1]/2,np.sqrt(3)*w[1]/2])
def tensor(t):return r'$T_{%d}^{%d%d}$'%t
def draw(ax,kind):
 keys=list(weights) if kind!='V' else list(eps.values())
 for n,w in enumerate(keys):
  p=point(w)
  for ww in keys[n+1:]:
   d=tuple(w[a]-ww[a] for a in range(2))
   if d in [(2,-1),(-2,1),(-1,2),(1,-2),(1,1),(-1,-1)]:
    q=point(ww);ax.plot([p[0],q[0]],[p[1],q[1]],color='#dddddd',lw=.8,zorder=0)
 for w in keys:
  p=point(w);inner=w in eps.values()
  idx=next((i for i in eps if eps[i]==w),None)
  highest=w==((1,0) if kind=='V' else (2,1))
  if kind=='V':labels=[r'$S_%d$'%idx];m=1
  elif inner and kind=='K':labels=[r'$K_{%d%d}$'%(idx,j) for j in range(1,4) if j!=idx];m=2
  else:labels=[tensor(t) for t in weights[w]];m=len(labels)
  color='#bd3d36' if highest else '#245f9e'
  ax.scatter([p[0]],[p[1]],s=190 if m>1 else 125,color=color,marker='*' if highest else 'o',zorder=4)
  if not highest:ax.text(*p,str(m),ha='center',va='center',fontsize=8,color='white',zorder=5)
  dx=0;dy=.16;ha='center';va='bottom'
  if w==(-2,0):dx=-.16;dy=0;ha='right';va='center'
  elif p[0]>2:dx=.16;dy=0;ha='left';va='center'
  elif p[0]<-1.5:dx=-.12;dy=.13 if p[1]>0 else -.13;ha='right';va='bottom' if p[1]>0 else 'top'
  elif p[1]<0:dy=-.18;va='top'
  if kind=='V':dx=.18 if idx==1 else -.16;dy=.08 if idx!=3 else -.12;ha='left' if idx==1 else 'right'
  ax.text(p[0]+dx,p[1]+dy,'\n'.join(labels),ha=ha,va=va,fontsize=11 if kind=='V' else 10,color=color,bbox=dict(facecolor='white',edgecolor='none',alpha=.9,pad=1),zorder=6)
 ax.set_aspect('equal');ax.axis('off')
 if kind=='V':ax.set_xlim(-1.35,1.8);ax.set_ylim(-1.5,1.5)
 else:ax.set_xlim(-3.2,3.55);ax.set_ylim(-3.25,3.25)
fig,axes=plt.subplots(1,2,figsize=(11.5,6.7),dpi=140,gridspec_kw=dict(width_ratios=[2,1]),facecolor='white')
draw(axes[0],'K');draw(axes[1],'V')
axes[0].set_title(r'$\ker C=L(2,1)$, dimension 15',fontsize=15)
axes[1].set_title(r'$s(V)=L(1,0)$, dimension 3',fontsize=15)
fig.text(.5,.055,r'$K_{ij}=2T_j^{ij}-T_i^{ii}$ ($j\ne i$), $S_i=\sum_jT_j^{ij}$.',ha='center',fontsize=12)
fig.text(.5,.02,'Red stars mark highest-weight vectors; other marker numbers are multiplicities.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.09,1,1));fig.savefig('paper-1-sl3-summands.png',facecolor='white',transparent=False);plt.close(fig)
