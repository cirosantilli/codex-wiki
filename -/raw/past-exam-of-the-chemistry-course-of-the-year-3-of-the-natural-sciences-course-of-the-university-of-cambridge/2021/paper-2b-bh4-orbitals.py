#!/usr/bin/env python3
"""Original solution figure. Python 3.14; numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#276ba2"
ORANGE="#c7602b"

fig=plt.figure(figsize=(13,4.8));gs=fig.add_gridspec(1,4,width_ratios=[2.1,1.25,1.25,1.25]);ax=fig.add_subplot(gs[0])
levels=[(-2.6,'1a₁',1,True),(-1.8,'1e',2,True),(-1,'b₁',1,False),(-.5,'2a₁',1,False),(.8,'2e',2,False),(1.6,'3a₁',1,False)]
for y,l,n,filled in levels:
 for x in ([.25,.75] if n==2 else [.5]):
  ax.plot([x-.16,x+.16],[y,y],c=BLUE if filled else '0.4',lw=2)
  if filled:ax.text(x,y+.05,'↑↓',ha='center',fontsize=14)
 ax.text(1.,y,l,va='center',fontsize=11)
ax.set(xlim=(-.2,1.7),ylim=(-3,2),ylabel='Illustrative valence energy');ax.set_xticks([]);ax.set_yticks([]);ax.set_title('6 electrons',fontsize=12)
xy=np.array([[1,0],[0,1],[-1,0],[0,-1]])
for index,(label,signs) in enumerate([(r'$1a_1$',(1,1,1,1)),(r'$1e_x$',(1,0,-1,0)),(r'$1e_y$',(0,1,0,-1))],1):
 a=fig.add_subplot(gs[index]);a.set_aspect('equal');a.axis('off');a.set(xlim=(-1.5,1.5),ylim=(-1.6,1.6));a.set_title(label)
 for j,((x,y),sgn) in enumerate(zip(xy,signs),1):
  color=BLUE if sgn>0 else ORANGE if sgn<0 else '0.8'
  a.add_patch(Circle((x,y),.20,facecolor=color,alpha=.85));a.text(x,y,'+' if sgn>0 else '−' if sgn<0 else '0',color='white',ha='center',va='center',fontsize=16)
  a.text(x*1.3,y*1.3,str(j),ha='center',va='center',fontsize=9)
 if index==1:
  a.add_patch(Circle((0,0),.28,facecolor=BLUE,alpha=.6));a.text(0,0,'+',ha='center',va='center',color='white',fontsize=19);a.text(0,-1.58,'B: s/pz hybrid',ha='center',fontsize=9)
 else:
  vec=np.array([1,0]) if index==2 else np.array([0,1])
  for sign,col in [(1,BLUE),(-1,ORANGE)]:
   a.add_patch(Circle(sign*.30*vec,.22,facecolor=col,alpha=.85))
  a.text(0,-1.58,'B: '+('px' if index==2 else 'py'),ha='center',fontsize=9)
fig.suptitle('Square-pyramidal BH₄⁺: symmetry diagram and occupied-orbital phases')
fig.text(.5,.015,'Ligand phases shown for matching B hybrids; empty-level ordering is illustrative.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.06,1,.92))
fig.savefig("paper-2b-bh4-orbitals.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
